#!/usr/bin/env python3
"""Audit the separate English and Chinese full-manuscript release package."""
from __future__ import annotations

import json
from pathlib import Path
import re
import xml.etree.ElementTree as ET
import zipfile

ROOT = Path(__file__).resolve().parents[1]
FULL = ROOT / "manuscript" / "full"
OUT = ROOT / "quality_reports" / "full_manuscript_audit.json"
EXPECTED_FILES = {"English.md", "Chinese.md", "English.docx", "Chinese.docx"}
SEQUENCES = {
    "FLLHTTR", "YLSLLQR", "ALLLHRC", "FCLHLQLR", "YHHLLCRR", "LLHLPKRTT",
    "LLHPLRL", "WLLVHLKK", "LLHPLRC", "HLLTLKKHV", "HLPLLHRCC", "HVLLLRQCA",
}
LOCKED_NUMBERS = {
    "11,269,961", "11,721,988", "31,510", "33,786", "3,518", "3,299",
    "923", "111", "15", "12", "8", "−9.60", "−8.25",
}
W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"

SPECS = {
    "English": {
        "hidden_title": "Deep-Learning-Guided Multi-Model Prioritization of Periodontitis-Cohort Oral Micropeptides",
        "abstract_heading": "## Abstract",
        "intro_heading": "## 1. Introduction",
        "methods_heading": "## 2. Materials and Methods",
        "results_heading": "## 3. Results",
        "discussion_heading": "## 4. Discussion",
        "conclusions_heading": "## 5. Conclusions",
        "declarations_heading": "## Declarations",
        "references_heading": "## References",
        "required": [
            "computation-only",
            "does not report participant, specimen, assembly-analysis, or metagenome-assembled-genome totals",
            "PRJEB65451 is not an independent clinical cohort",
            "metaSPAdes v3.15.3",
            "esm2_t6_8M_UR50D",
            "six-layer task-specific convolutional neural network",
            "fine-tuning the ESM2-t30 protein language model",
            "two-tier artificial-neural-network framework",
            "multi-task deep convolutional neural network",
            "not orthogonal biological confirmation",
            "Prospective GROMACS molecular-dynamics protocol",
            "100 ns with a 2-fs time step",
            "no molecular-dynamics result is reported",
        ],
        "prohibited": [
            "Article type:", "Draft status:", "user-designated", "external-v0.4",
            "teacher", "supervisor", "pre-submission", "accountable authors",
            "11 orally healthy controls", "11 patients with periodontitis",
            "22 participants", "66 specimens", "118 sequence-assembly analyses",
            "24 healthy", "24 controls", "26 periodontitis", "26 patients",
            "296 high-quality", "PRJEB65451 remains unresolved",
            "could not be independently resolved",
        ],
    },
    "Chinese": {
        "hidden_title": "深度学习引导的牙周炎队列口腔微肽多模型优选",
        "abstract_heading": "## 摘要",
        "intro_heading": "## 1. 引言",
        "methods_heading": "## 2. 材料与方法",
        "results_heading": "## 3. 结果",
        "discussion_heading": "## 4. 讨论",
        "conclusions_heading": "## 5. 结论",
        "declarations_heading": "## 声明",
        "references_heading": "## 参考文献",
        "required": [
            "纯计算",
            "不报告参与者、标本、组装分析或宏基因组组装基因组总数",
            "PRJEB65451并非独立临床队列",
            "metaSPAdes v3.15.3",
            "esm2_t6_8M_UR50D",
            "六层卷积神经网络",
            "微调ESM2-t30蛋白质语言模型",
            "两级人工神经网络框架",
            "多任务深度卷积神经网络",
            "不构成相互独立的生物学确认",
            "前瞻性GROMACS分子动力学方案",
            "生产阶段为100 ns，步长2 fs",
            "不报告任何分子动力学结果",
        ],
        "prohibited": [
            "文章类型：", "草稿状态：", "用户指定", "外部v0.4", "老师",
            "导师", "投稿前", "责任作者", "11名口腔健康对照",
            "11名牙周炎患者", "22名参与者", "66份标本", "118项序列组装分析",
            "24名健康", "26名牙周炎", "296个高质量", "无法独立解析PRJEB65451",
        ],
    },
}


def ordered_sections(text: str, headings: list[str]) -> tuple[bool, list[str]]:
    positions = [text.find(heading) for heading in headings]
    missing = [heading for heading, position in zip(headings, positions) if position < 0]
    return not missing and positions == sorted(positions), missing


def introduction(text: str, start_heading: str, end_heading: str) -> str:
    return text.split(start_heading, 1)[1].split(end_heading, 1)[0]


def grouped_citations(intro: str) -> list[str]:
    bad = []
    for match in re.finditer(r"\[([^\]]+)\]", intro):
        value = match.group(1).strip()
        if not value.isdigit():
            bad.append(match.group(0))
    return sorted(set(bad))


def reference_metadata(text: str, heading: str) -> dict:
    block = text.split(heading, 1)[1]
    numbers = [int(item) for item in re.findall(r"(?m)^(\d+)\.\s", block)]
    dois = sorted(set(value.rstrip(".").lower() for value in re.findall(
        r"doi:(10\.\d{4,9}/[^\s]+)", block, flags=re.IGNORECASE
    )))
    return {
        "numbers": numbers,
        "count": len(numbers),
        "consecutive_1_to_53": numbers == list(range(1, 54)),
        "dois": dois,
        "doi_count": len(dois),
    }


def markdown_figures(text: str) -> list[str]:
    return re.findall(r"!\[[^\]]*\]\(([^)]+)\)", text)


def docx_checks(path: Path, language: str, spec: dict) -> tuple[dict, str]:
    with zipfile.ZipFile(path) as archive:
        names = set(archive.namelist())
        crc_error = archive.testzip()
        root = ET.fromstring(archive.read("word/document.xml"))
        text = "".join(node.text or "" for node in root.iter(W + "t"))
        all_xml = "\n".join(
            archive.read(name).decode("utf-8", errors="replace")
            for name in sorted(names)
            if name.endswith((".xml", ".rels"))
        )
        header_footer = sorted(
            name for name in names
            if name.startswith("word/header") or name.startswith("word/footer")
        )
        media = sorted(
            name for name in names
            if name.startswith("word/media/") and not name.endswith("/")
        )
        comment_members = sorted(
            name for name in names
            if name.startswith("word/comments") or name.startswith("word/people")
        )
        core_root = ET.fromstring(archive.read("docProps/core.xml"))
        core_title = "".join(core_root.itertext())
    abstract_label = "Abstract" if language == "English" else "摘要"
    checks = {
        "zip_crc_ok": crc_error is None,
        "header_footer_parts_absent": not header_footer,
        "page_number_fields_absent": "<w:instrText" not in all_xml and 'w:instr="PAGE"' not in all_xml,
        "comments_and_annotations_absent": not comment_members and "commentReference" not in all_xml,
        "three_figures_embedded": len(media) == 3,
        "all_locked_numbers_present": all(value in text for value in LOCKED_NUMBERS),
        "all_twelve_sequences_present": all(value in text for value in SEQUENCES),
        "visible_content_starts_with_abstract": text.startswith(abstract_label),
        "article_title_absent_from_visible_content": spec["hidden_title"] not in text,
        "core_metadata_uses_neutral_language_name": language in core_title and spec["hidden_title"] not in core_title,
    }
    return {
        "checks": checks,
        "header_footer_parts": header_footer,
        "comment_annotation_parts": comment_members,
        "core_metadata_text": core_title,
        "embedded_media": media,
        "verdict": "PASS" if all(checks.values()) else "FAIL",
    }, text


def audit_editable_svgs() -> dict:
    paths = [
        ROOT / "manuscript" / "figures" / "prioritization_funnel.svg",
        ROOT / "manuscript" / "figures" / "fig5_docking_scores.svg",
        ROOT / "manuscript" / "figures" / "evidence_ladder.svg",
    ]
    records = []
    for path in paths:
        root = ET.fromstring(path.read_bytes())
        text_nodes = [node for node in root.iter() if node.tag.rsplit("}", 1)[-1] in {"text", "tspan"}]
        records.append({
            "path": str(path.relative_to(ROOT)),
            "text_nodes": len(text_nodes),
            "characters": sum(len("".join(node.itertext())) for node in text_nodes),
            "editable_text_present": bool(text_nodes),
        })
    checks = {
        "three_svg_source_figures_present": len(records) == 3,
        "all_svgs_retain_editable_text_nodes": all(item["editable_text_present"] for item in records),
    }
    return {
        "figures": records,
        "checks": checks,
        "verdict": "PASS" if all(checks.values()) else "FAIL",
    }


def audit_language(language: str, spec: dict) -> dict:
    md_path = FULL / f"{language}.md"
    docx_path = FULL / f"{language}.docx"
    text = md_path.read_text(encoding="utf-8")
    headings = [
        spec["abstract_heading"], spec["intro_heading"], spec["methods_heading"],
        spec["results_heading"], spec["discussion_heading"],
        spec["conclusions_heading"], spec["declarations_heading"],
        spec["references_heading"],
    ]
    sections_ordered, missing_sections = ordered_sections(text, headings)
    abstract = text.split(spec["abstract_heading"], 1)[1].split(spec["intro_heading"], 1)[0]
    intro = introduction(text, spec["intro_heading"], spec["methods_heading"])
    abstract_word_count = len(abstract.split())
    intro_word_count = len(intro.split())
    bad_citations = grouped_citations(intro)
    refs = reference_metadata(text, spec["references_heading"])
    figures = markdown_figures(text)
    missing_figures = [value for value in figures if not (md_path.parent / value).resolve().is_file()]
    prohibited_hits = [value for value in spec["prohibited"] if value.lower() in text.lower()]
    missing_required = [value for value in spec["required"] if value not in text]
    docx, docx_text = docx_checks(docx_path, language, spec)
    abstract_prefix = text.lstrip().splitlines()[0] if text.strip() else ""
    results = text.split(spec["results_heading"], 1)[1].split(spec["discussion_heading"], 1)[0]
    checks = {
        "complete_sections_present_in_order": sections_ordered,
        "markdown_starts_with_abstract_and_has_no_visible_title": abstract_prefix == spec["abstract_heading"],
        "abstract_is_concise_unstructured_sci_narrative": (
            "**Background:**" not in abstract
            and "**Methods:**" not in abstract
            and "**Results:**" not in abstract
            and "**Conclusions:**" not in abstract
            and "**背景：**" not in abstract
            and "**方法：**" not in abstract
            and "**结果：**" not in abstract
            and "**结论：**" not in abstract
            and (
                200 <= abstract_word_count <= 350
                if language == "English" else 600 <= len(abstract) <= 1600
            )
        ),
        "introduction_has_review_grade_depth": (
            intro_word_count >= 2500 if language == "English" else len(intro) >= 5500
        ),
        "introduction_starts_with_ad_then_p_gingivalis_rationale": (
            "Alzheimer" in intro[:3000]
            and "gingivalis" in intro[:7000]
            and intro.find("Alzheimer") < intro.find("gingivalis")
        ),
        "introduction_citation_brackets_are_single_reference": not bad_citations,
        "reference_numbers_are_consecutive_1_to_53": refs["consecutive_1_to_53"],
        "required_provenance_and_model_descriptions_present": not missing_required,
        "administrative_and_rejected_text_absent": not prohibited_hits,
        "locked_funnel_values_present": all(value in text for value in LOCKED_NUMBERS),
        "all_twelve_sequences_present": all(value in text for value in SEQUENCES),
        "three_figure_links_present": len(figures) == 3,
        "all_figure_links_resolve": not missing_figures,
        "no_md_result_subsection_or_claim_in_results": (
            "Molecular-dynamics result" not in results
            and "Molecular dynamics result" not in results
            and "分子动力学结果" not in results
        ),
        "hidden_article_title_absent_from_markdown": spec["hidden_title"] not in text,
        "docx_package_passes_clean_checks": docx["verdict"] == "PASS",
    }
    return {
        "markdown": str(md_path.relative_to(ROOT)),
        "docx": str(docx_path.relative_to(ROOT)),
        "missing_sections": missing_sections,
        "grouped_introduction_citations": bad_citations,
        "missing_required_tokens": missing_required,
        "prohibited_tokens_found": prohibited_hits,
        "abstract_word_count": abstract_word_count,
        "abstract_characters": len(abstract),
        "introduction_word_count": intro_word_count,
        "introduction_characters": len(intro),
        "references": refs,
        "figure_links": figures,
        "missing_figure_targets": missing_figures,
        "docx_audit": docx,
        "checks": checks,
        "verdict": "PASS" if all(checks.values()) else "FAIL",
    }


def main() -> int:
    actual_files = {path.name for path in FULL.iterdir() if path.is_file()}
    languages = {language: audit_language(language, spec) for language, spec in SPECS.items()}
    svg_audit = audit_editable_svgs()
    en_refs = languages["English"]["references"]
    zh_refs = languages["Chinese"]["references"]
    package_checks = {
        "only_separate_english_and_chinese_deliverables_present": actual_files == EXPECTED_FILES,
        "no_bilingual_full_deliverable": not any("bilingual" in name.lower() for name in actual_files),
        "english_chinese_reference_number_parity": en_refs["numbers"] == zh_refs["numbers"],
        "english_chinese_doi_inventory_parity": en_refs["dois"] == zh_refs["dois"],
        "editable_text_svg_sources_pass": svg_audit["verdict"] == "PASS",
        "both_language_audits_pass": all(item["verdict"] == "PASS" for item in languages.values()),
    }
    verdict = "PASS" if all(package_checks.values()) else "FAIL"
    report = {
        "schema": "local.full_manuscript_audit.v2",
        "scope": "Separate full English and Chinese manuscripts; no bilingual full deliverable.",
        "expected_files": sorted(EXPECTED_FILES),
        "actual_files": sorted(actual_files),
        "languages": languages,
        "editable_svg_audit": svg_audit,
        "package_checks": package_checks,
        "verdict": verdict,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(OUT)
    return 0 if verdict == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
