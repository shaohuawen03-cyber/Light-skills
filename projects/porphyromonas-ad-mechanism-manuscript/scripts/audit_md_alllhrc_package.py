#!/usr/bin/env python3
"""Audit the standalone, figure-free ALLLHRC–AChE MD manuscript package."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET
import zipfile

import audit_submission_manuscripts as shared

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "quality_reports" / "md_alllhrc_package_audit.json"
BIB = ROOT / "references" / "references.bib"
BUILDER = ROOT / "scripts" / "build_docx_stdlib.py"
TIMESTAMP = "2026-08-23T00:00:00Z"
W = shared.W

SPECS = {
    "full/English": {
        "md": "manuscript/md_alllhrc/full/English.md",
        "docx": "manuscript/md_alllhrc/full/English.docx",
        "language": "English", "start": "Abstract", "refs": 7, "tables": 2,
        "sections": ["## Abstract", "## Introduction", "## Materials and methods", "## Results", "## Discussion", "## References"],
        "keywords": "**Keywords:**", "digitized": "digitized", "identity": "inherited “AChE–Aβ” label",
        "limits": ["cannot show that ALLLHRC", "does not by itself establish continued binding", "not preservation of a single rigid docking pose"],
    },
    "full/Chinese": {
        "md": "manuscript/md_alllhrc/full/Chinese.md",
        "docx": "manuscript/md_alllhrc/full/Chinese.docx",
        "language": "Chinese", "start": "摘要", "refs": 7, "tables": 2,
        "sections": ["## 摘要", "## 引言", "## 材料与方法", "## 结果", "## 讨论", "## 参考文献"],
        "keywords": "**关键词：**", "digitized": "数字化RMSD曲线", "identity": "继承的“AChE–Aβ”标签",
        "limits": ["不能证明肽仍与AChE结合", "不能把RMSD模式转化为稳定结合的证据", "该轨迹不能证明ALLLHRC"],
    },
    "concise/English": {
        "md": "manuscript/md_alllhrc/concise/English.md",
        "docx": "manuscript/md_alllhrc/concise/English.docx",
        "language": "English", "start": "Abstract", "refs": 5, "tables": 1,
        "sections": ["## Abstract", "## Introduction", "## Materials and methods", "## Results", "## Discussion", "## References"],
        "keywords": "**Keywords:**", "digitized": "digitized trace", "identity": "inherited “AChE–Aβ” header",
        "limits": ["cannot by itself establish", "cannot be transferred to ALLLHRC", "cannot show that ALLLHRC"],
    },
    "concise/Chinese": {
        "md": "manuscript/md_alllhrc/concise/Chinese.md",
        "docx": "manuscript/md_alllhrc/concise/Chinese.docx",
        "language": "Chinese", "start": "摘要", "refs": 5, "tables": 1,
        "sections": ["## 摘要", "## 引言", "## 材料与方法", "## 结果", "## 讨论", "## 参考文献"],
        "keywords": "**关键词：**", "digitized": "数字化曲线", "identity": "继承的“AChE–Aβ”标题",
        "limits": ["不能证明酶抑制", "不能迁移到ALLLHRC", "不能证明ALLLHRC"],
    },
}

REQUIRED_NUMERIC = [
    "100 ns", "0.1803", "0.0220", "0.2320", "0.0582", "0.0091", "22.6",
    "0.1432", "0.0161", "23.4", "55.6", "0.2694", "0.0148", "57.0",
    "1.2", "1.4", "210–223", "10–12", "0–11",
]
SOURCE_HASHES = {
    "source_materials/md_alllhrc/digitized_rmsd_100ns.csv": "b34c48db440f5cddd2a782e12713172359edc23c737b14726c602cfef32b565a",
    "source_materials/md_alllhrc/peptide_rmsd_jump_diagnosis.txt": "43f3f84ae57b1f037e80f4aed3d9cb3614a0df92f64a7e3c92c2972291f6f3f3",
}
ORIGINAL_DOCX_HASHES = {
    "manuscript/full/Chinese.docx": "610fcb7f7c09287233fa699c8f7043b665aa1a5d06d4d05e0c3f527ee8125c91",
    "manuscript/full/English.docx": "98943ba415134a0ca47b00022371d9e75abe6d76cac9d8f540cc6984adca2c32",
    "manuscript/concise/Chinese.docx": "e1529a0bb0f2e22afc68e7e9966816f4f3d9a3a496159dc9aaf98a42a9241ddc",
    "manuscript/concise/English.docx": "7dfbe9e65504d61e56fb58d39940bc9e0ded439a07557be21913e4def2a994b7",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def inspect_docx(path: Path, spec: dict) -> dict:
    with zipfile.ZipFile(path) as archive:
        names = set(archive.namelist())
        crc = archive.testzip()
        document_xml = archive.read("word/document.xml").decode("utf-8")
        styles_xml = archive.read("word/styles.xml").decode("utf-8")
        doc = ET.fromstring(document_xml)
        text = "".join(node.text or "" for node in doc.iter(W + "t"))
        core_text = "".join(ET.fromstring(archive.read("docProps/core.xml")).itertext())
        media = sorted(name for name in names if name.startswith("word/media/") and not name.endswith("/"))
        drawings = sum(1 for _ in doc.iter(W + "drawing"))
        header_footer = sorted(name for name in names if name.startswith(("word/header", "word/footer")))
        comments = sorted(name for name in names if name.startswith(("word/comments", "word/people")))
        all_xml = "\n".join(
            archive.read(name).decode("utf-8", errors="replace")
            for name in names if name.endswith((".xml", ".rels"))
        )
        tables = list(doc.iter(W + "tbl"))
        table_audits = [shared.table_checks(table) for table in tables]
        paragraph_styles = []
        current_section = None
        main_sections = set(section.removeprefix("## ") for section in spec["sections"][1:5])
        abstract_paragraphs = []
        for paragraph in doc.iter(W + "p"):
            ptext = "".join(node.text or "" for node in paragraph.iter(W + "t")).strip()
            style_node = paragraph.find(f"{W}pPr/{W}pStyle")
            style = style_node.get(W + "val") if style_node is not None else None
            if style == "Heading2":
                current_section = ptext
                continue
            if not ptext:
                continue
            if current_section == spec["sections"][0].removeprefix("## ") and style != "Keywords":
                abstract_paragraphs.append((ptext, style))
            if current_section in main_sections and style not in {"Heading3", "Heading4", "Caption", "TableText", "ListParagraph"}:
                paragraph_styles.append(style)
    three_line = bool(table_audits) and all(
        all(audit[name] for name in (
            "top_and_bottom_rules_present", "vertical_and_body_rules_absent",
            "header_bottom_rule_present_in_every_cell", "body_cells_have_no_overriding_borders", "shading_absent",
        )) for audit in table_audits
    )
    return {
        "sha256": sha256(path), "crc_ok": crc is None, "text": text,
        "core_text": core_text, "media": media, "drawings": drawings,
        "header_footer": header_footer, "comments": comments,
        "all_xml": all_xml, "styles_xml": styles_xml,
        "table_count": len(tables), "table_audits": table_audits,
        "all_tables_three_line": three_line,
        "abstract_paragraphs": abstract_paragraphs,
        "main_text_paragraph_styles": paragraph_styles,
    }


def rebuild_matches(md: Path, docx: Path, language: str) -> tuple[bool, str]:
    with tempfile.TemporaryDirectory(prefix="md-alllhrc-audit-") as tmp:
        rebuilt = Path(tmp) / docx.name
        run = subprocess.run(
            [sys.executable, str(BUILDER), "--clean-manuscript", "--timestamp", TIMESTAMP,
             "--bibliography", str(BIB), "--input", str(md), "--output", str(rebuilt), "--title", language],
            cwd=ROOT, capture_output=True, text=True,
        )
        if run.returncode != 0:
            return False, run.stderr.strip() or run.stdout.strip()
        return rebuilt.read_bytes() == docx.read_bytes(), ""


def audit_one(label: str, spec: dict, known_keys: set[str], doi_to_key: dict[str, str]) -> dict:
    md_path = ROOT / spec["md"]
    docx_path = ROOT / spec["docx"]
    md = md_path.read_text(encoding="utf-8")
    sections = re.findall(r"(?m)^##\s+.+$", md)
    body, references = md.split(spec["sections"][-1], 1)
    abstract_block = body.split(spec["sections"][0], 1)[1].split(spec["sections"][1], 1)[0]
    abstract_main = abstract_block.split(spec["keywords"], 1)[0].strip()
    abstract_paragraphs = [part for part in re.split(r"\n\s*\n", abstract_main) if part.strip()]
    cited = re.findall(r"@([A-Za-z0-9_.:+-]+)", body)
    cited_order = list(dict.fromkeys(cited))
    ref_numbers = [int(value) for value in re.findall(r"(?m)^(\d+)\.\s", references)]
    ref_dois = [
        match.group(1).rstrip(".,;:)]}").lower()
        for match in re.finditer(r"(?m)^\d+\.\s.*?doi:(10\.\d{4,9}/\S+)", references, re.I)
    ]
    ref_order = [doi_to_key[doi] for doi in ref_dois]
    intro = body.split(spec["sections"][1], 1)[1].split(spec["sections"][2], 1)[0]
    grouped_intro = [
        cluster for cluster in re.findall(r"\[(@[^\]]+)\]", intro)
        if len(re.findall(r"@[A-Za-z0-9_.:+-]+", cluster)) != 1
    ]
    docx = inspect_docx(docx_path, spec)
    reproducible, rebuild_error = rebuild_matches(md_path, docx_path, spec["language"])
    english = spec["language"] == "English"
    table_rows = [
        max(0, len(table.splitlines()) - 2)
        for table in re.findall(r"(?m)(^\|.+\|\n^\|(?:\s*:?-+:?\s*\|)+\n(?:^\|.+\|\n?)+)", md)
    ]
    checks = {
        "markdown_starts_with_abstract_and_has_no_visible_title": md.lstrip().startswith(spec["sections"][0]) and not re.search(r"(?m)^#\s+", md),
        "article_sections_are_complete_and_in_order": sections == spec["sections"],
        "abstract_is_one_unstructured_paragraph": len(abstract_paragraphs) == 1,
        "english_abstract_is_within_250_words": len(abstract_main.split()) <= 250 if english else True,
        "abstract_has_no_citation_or_conclusion_label": "[@" not in abstract_main and "**Conclusions:**" not in abstract_main and "**结论：**" not in abstract_main,
        "statistical_analysis_and_conclusion_sections_absent": not re.search(r"(?m)^###?\s+(?:Statistical analysis|统计分析|Conclusion|结论)\s*$", body),
        "discussion_proceeds_directly_to_references": sections[-2:] == spec["sections"][-2:],
        "figure_markup_is_absent": "![" not in body and not re.search(r"(?mi)^\*\*(?:Figure|图)\s*\d", body),
        "all_principal_numeric_observations_are_retained": all(value in body for value in REQUIRED_NUMERIC),
        "digitized_rmsd_status_is_disclosed": spec["digitized"] in body,
        "source_plot_identity_discrepancy_is_disclosed": spec["identity"] in body,
        "atanasova_is_framework_not_transferred_data": "Atanasova" in body and "1 μs" in body and "ALLLHRC" in body,
        "binding_and_function_boundaries_are_explicit": all(value in body for value in spec["limits"]),
        "single_trajectory_and_raw_archive_limitations_are_explicit": ("single" in body.lower() if english else "单条" in body) and ("raw" in body.lower() if english else "原始" in body),
        "pandoc_citation_keys_are_valid": bool(cited) and set(cited) <= known_keys,
        "introduction_uses_one_reference_per_citation": not grouped_intro,
        "references_are_sequential": ref_numbers == list(range(1, spec["refs"] + 1)),
        "references_follow_first_citation_order": ref_order == cited_order,
        "reference_count_matches_variant": len(ref_dois) == spec["refs"],
        "markdown_table_count_matches_variant": len(table_rows) == spec["tables"],
        "docx_zip_crc_is_valid": docx["crc_ok"],
        "docx_visible_content_starts_with_abstract": docx["text"].startswith(spec["start"]),
        "docx_core_title_is_neutral": spec["language"] in docx["core_text"] and "ALLLHRC" not in docx["core_text"],
        "docx_has_no_media_drawings_header_footer_page_or_comments": (
            not docx["media"] and docx["drawings"] == 0 and not docx["header_footer"] and not docx["comments"]
            and 'w:instr="PAGE"' not in docx["all_xml"] and "/relationships/image" not in docx["all_xml"]
        ),
        "docx_uses_journal_body_style": (
            '<w:sz w:val="24"/><w:szCs w:val="24"/>' in docx["styles_xml"]
            and 'w:line="480" w:lineRule="auto"' in docx["styles_xml"]
            and '<w:ind w:firstLine="480"/>' in docx["styles_xml"]
        ),
        "docx_main_text_is_first_line_indented": bool(docx["main_text_paragraph_styles"]) and all(
            style == "BodyText" for style in docx["main_text_paragraph_styles"]
        ),
        "docx_abstract_is_one_unindented_paragraph": len(docx["abstract_paragraphs"]) == 1 and docx["abstract_paragraphs"][0][1] == "Normal",
        "docx_has_one_inch_margins": all(f'w:{side}="1440"' in docx["all_xml"] for side in ("top", "right", "bottom", "left")),
        "docx_table_count_matches_markdown": docx["table_count"] == spec["tables"],
        "docx_tables_are_three_line": docx["all_tables_three_line"],
        "docx_contains_rendered_citations_not_citekeys": "@" not in docx["text"] and "[1]" in docx["text"],
        "docx_is_byte_reproducible": reproducible,
    }
    return {
        "label": label, "markdown": spec["md"], "docx": spec["docx"],
        "markdown_sha256": sha256(md_path), "docx_sha256": docx["sha256"],
        "abstract_word_count": len(abstract_main.split()),
        "body_word_count": len(body.split()), "body_character_count": len(body),
        "reference_count": len(ref_numbers), "table_data_row_counts": table_rows,
        "grouped_introduction_citations": grouped_intro,
        "unknown_citation_keys": sorted(set(cited) - known_keys),
        "embedded_media": docx["media"], "drawings": docx["drawings"],
        "table_audits": docx["table_audits"], "rebuild_error": rebuild_error,
        "checks": checks, "verdict": "PASS" if all(checks.values()) else "FAIL",
    }


def main() -> int:
    bib_text = BIB.read_text(encoding="utf-8")
    known_keys = shared.bib_keys(bib_text)
    doi_to_key = shared.bib_doi_key_map(bib_text)
    records = {label: audit_one(label, spec, known_keys, doi_to_key) for label, spec in SPECS.items()}
    source_checks = {path: sha256(ROOT / path) == expected for path, expected in SOURCE_HASHES.items()}
    original_checks = {path: sha256(ROOT / path) == expected for path, expected in ORIGINAL_DOCX_HASHES.items()}
    package_checks = {
        "four_new_language_variant_pairs_are_present": len(records) == 4,
        "all_four_new_manuscripts_pass": all(record["verdict"] == "PASS" for record in records.values()),
        "all_source_support_hashes_match": all(source_checks.values()),
        "original_v3_9_docx_files_are_unchanged": all(original_checks.values()),
        "full_language_parity": records["full/English"]["reference_count"] == records["full/Chinese"]["reference_count"] == 7,
        "concise_language_parity": records["concise/English"]["reference_count"] == records["concise/Chinese"]["reference_count"] == 5,
        "all_new_docx_files_are_figure_free": all(not record["embedded_media"] and record["drawings"] == 0 for record in records.values()),
    }
    report = {
        "schema": "local.md_alllhrc_package_audit.v1",
        "scope": "Standalone full/concise English/Chinese ALLLHRC–AChE 100-ns MD manuscripts.",
        "source_support_sha256": {path: {"expected": expected, "matches": source_checks[path]} for path, expected in SOURCE_HASHES.items()},
        "original_v3_9_docx_sha256": {path: {"expected": expected, "matches": original_checks[path]} for path, expected in ORIGINAL_DOCX_HASHES.items()},
        "records": records, "package_checks": package_checks,
        "citation_mode": "BibTeX-linked Markdown with static numbered DOCX cache; not Zotero-live",
        "verdict": "PASS" if all(package_checks.values()) else "FAIL",
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(OUT)
    return 0 if report["verdict"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
