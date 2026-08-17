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
        "top_heading": "# Deep-Learning-Guided Multi-Model Prioritization",
        "intro_heading": "## 1. Introduction",
        "methods_heading": "## 2. Materials and Methods",
        "results_heading": "## 3. Results",
        "discussion_heading": "## 4. Discussion",
        "conclusions_heading": "## 5. Conclusions",
        "declarations_heading": "## Declarations",
        "references_heading": "## References",
        "required": [
            "11 orally healthy controls and 11 patients with periodontitis",
            "66 specimens",
            "118 sequence-assembly analyses",
            "PRJEB65451 is not an independent cohort",
            "metaSPAdes v3.15.3",
            "esm2_t6_8M_UR50D",
            "six-layer task-specific convolutional neural network",
            "fine-tuning the ESM2-t30 protein language model",
            "two-tier artificial-neural-network framework",
            "multi-task deep convolutional neural network",
            "not orthogonal biological confirmation",
        ],
        "prohibited": [
            "Article type:", "Draft status:", "user-designated", "external-v0.4",
            "teacher", "supervisor", "pre-submission", "accountable authors",
            "24 healthy", "24 controls", "26 periodontitis", "26 patients",
            "296 high-quality", "PRJEB65451 remains unresolved",
            "could not be independently resolved",
        ],
    },
    "Chinese": {
        "top_heading": "# 深度学习引导的牙周炎队列口腔微肽多模型优选",
        "intro_heading": "## 1. 引言",
        "methods_heading": "## 2. 材料与方法",
        "results_heading": "## 3. 结果",
        "discussion_heading": "## 4. 讨论",
        "conclusions_heading": "## 5. 结论",
        "declarations_heading": "## 声明",
        "references_heading": "## 参考文献",
        "required": [
            "11名口腔健康对照和11名牙周炎患者",
            "66份标本",
            "118项序列组装分析",
            "PRJEB65451并非独立队列",
            "metaSPAdes v3.15.3",
            "esm2_t6_8M_UR50D",
            "六层卷积神经网络",
            "微调ESM2-t30蛋白质语言模型",
            "两级人工神经网络框架",
            "多任务深度卷积神经网络",
            "不构成相互独立的生物学确认",
        ],
        "prohibited": [
            "文章类型：", "草稿状态：", "用户指定", "外部v0.4", "老师",
            "导师", "投稿前", "责任作者", "24名健康", "26名牙周炎",
            "296个高质量", "无法独立解析PRJEB65451",
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


def docx_checks(path: Path) -> tuple[dict, str]:
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
    checks = {
        "zip_crc_ok": crc_error is None,
        "header_footer_parts_absent": not header_footer,
        "page_number_fields_absent": "<w:instrText" not in all_xml and 'w:instr="PAGE"' not in all_xml,
        "three_figures_embedded": len(media) == 3,
        "all_locked_numbers_present": all(value in text for value in LOCKED_NUMBERS),
        "all_twelve_sequences_present": all(value in text for value in SEQUENCES),
    }
    return {
        "checks": checks,
        "header_footer_parts": header_footer,
        "embedded_media": media,
        "verdict": "PASS" if all(checks.values()) else "FAIL",
    }, text


def audit_language(language: str, spec: dict) -> dict:
    md_path = FULL / f"{language}.md"
    docx_path = FULL / f"{language}.docx"
    text = md_path.read_text(encoding="utf-8")
    headings = [
        spec["top_heading"], spec["intro_heading"], spec["methods_heading"],
        spec["results_heading"], spec["discussion_heading"],
        spec["conclusions_heading"], spec["declarations_heading"],
        spec["references_heading"],
    ]
    sections_ordered, missing_sections = ordered_sections(text, headings)
    intro = introduction(text, spec["intro_heading"], spec["methods_heading"])
    bad_citations = grouped_citations(intro)
    refs = reference_metadata(text, spec["references_heading"])
    figures = markdown_figures(text)
    missing_figures = [value for value in figures if not (md_path.parent / value).resolve().is_file()]
    prohibited_hits = [value for value in spec["prohibited"] if value.lower() in text.lower()]
    missing_required = [value for value in spec["required"] if value not in text]
    docx, docx_text = docx_checks(docx_path)
    checks = {
        "complete_sections_present_in_order": sections_ordered,
        "introduction_starts_with_ad_and_p_gingivalis_rationale": (
            "Alzheimer" in intro[:2200] and "gingivalis" in intro[:2200]
        ),
        "introduction_citation_brackets_are_single_reference": not bad_citations,
        "reference_numbers_are_consecutive_1_to_53": refs["consecutive_1_to_53"],
        "required_provenance_and_model_descriptions_present": not missing_required,
        "administrative_and_rejected_text_absent": not prohibited_hits,
        "locked_funnel_values_present": all(value in text for value in LOCKED_NUMBERS),
        "all_twelve_sequences_present": all(value in text for value in SEQUENCES),
        "three_figure_links_present": len(figures) == 3,
        "all_figure_links_resolve": not missing_figures,
        "docx_contains_markdown_title": spec["top_heading"].removeprefix("# ") in docx_text,
        "docx_package_passes_clean_checks": docx["verdict"] == "PASS",
    }
    return {
        "markdown": str(md_path.relative_to(ROOT)),
        "docx": str(docx_path.relative_to(ROOT)),
        "missing_sections": missing_sections,
        "grouped_introduction_citations": bad_citations,
        "missing_required_tokens": missing_required,
        "prohibited_tokens_found": prohibited_hits,
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
    en_refs = languages["English"]["references"]
    zh_refs = languages["Chinese"]["references"]
    package_checks = {
        "only_separate_english_and_chinese_deliverables_present": actual_files == EXPECTED_FILES,
        "no_bilingual_full_deliverable": not any("bilingual" in name.lower() for name in actual_files),
        "english_chinese_reference_number_parity": en_refs["numbers"] == zh_refs["numbers"],
        "english_chinese_doi_inventory_parity": en_refs["dois"] == zh_refs["dois"],
        "both_language_audits_pass": all(item["verdict"] == "PASS" for item in languages.values()),
    }
    verdict = "PASS" if all(package_checks.values()) else "FAIL"
    report = {
        "schema": "local.full_manuscript_audit.v1",
        "scope": "Separate full English and Chinese manuscripts; no bilingual full deliverable.",
        "expected_files": sorted(EXPECTED_FILES),
        "actual_files": sorted(actual_files),
        "languages": languages,
        "package_checks": package_checks,
        "verdict": verdict,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(OUT)
    return 0 if verdict == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
