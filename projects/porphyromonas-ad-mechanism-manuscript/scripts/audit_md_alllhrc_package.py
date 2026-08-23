#!/usr/bin/env python3
"""Audit the reduced full-only ALLLHRC–AChE MD result reports."""
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
BUILDER = ROOT / "scripts" / "build_docx_stdlib.py"
TIMESTAMP = "2026-08-23T00:00:00Z"
W = shared.W
SPECS = {
    "full/English": {
        "md": "manuscript/md_alllhrc/full/English.md",
        "docx": "manuscript/md_alllhrc/full/English.docx",
        "language": "English",
        "start": "Analysis methods",
        "sections": ["## Analysis methods", "## Results", "## Discussion"],
        "digitized": "digitized RMSD trace",
        "identity": "inherited “AChE–Aβ” label",
        "limits": ["cannot show that ALLLHRC", "does not by itself establish continued binding", "not preservation of a single rigid docking pose"],
    },
    "full/Chinese": {
        "md": "manuscript/md_alllhrc/full/Chinese.md",
        "docx": "manuscript/md_alllhrc/full/Chinese.docx",
        "language": "Chinese",
        "start": "分析方法",
        "sections": ["## 分析方法", "## 结果", "## 讨论"],
        "digitized": "数字化RMSD曲线",
        "identity": "继承的“AChE–Aβ”标签",
        "limits": ["不能证明肽仍与AChE结合", "不能把RMSD模式转化为稳定结合的证据", "该轨迹不能证明ALLLHRC"],
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
SCREENING_DOCX_HASHES = {
    "manuscript/full/Chinese.docx": "610fcb7f7c09287233fa699c8f7043b665aa1a5d06d4d05e0c3f527ee8125c91",
    "manuscript/full/English.docx": "98943ba415134a0ca47b00022371d9e75abe6d76cac9d8f540cc6984adca2c32",
    "manuscript/intermediate/Chinese.docx": "043bf99a69ffbb6a99c0983d35f0efcedc4f08e3d16d99f8c38a8b596b15d7b0",
    "manuscript/intermediate/English.docx": "f725a7ddd473fe76ba417a3373eecff3d7e8ed25156e5d09590d1f06a27627de",
    "manuscript/concise/Chinese.docx": "e1529a0bb0f2e22afc68e7e9966816f4f3d9a3a496159dc9aaf98a42a9241ddc",
    "manuscript/concise/English.docx": "7dfbe9e65504d61e56fb58d39940bc9e0ded439a07557be21913e4def2a994b7",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def markdown_table_rows(text: str) -> list[int]:
    return [
        max(0, len(table.splitlines()) - 2)
        for table in re.findall(r"(?m)(^\|.+\|\n^\|(?:\s*:?-+:?\s*\|)+\n(?:^\|.+\|\n?)+)", text)
    ]


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
        current_section = None
        heading2_texts = []
        body_styles = []
        for paragraph in doc.iter(W + "p"):
            ptext = "".join(node.text or "" for node in paragraph.iter(W + "t")).strip()
            style_node = paragraph.find(f"{W}pPr/{W}pStyle")
            style = style_node.get(W + "val") if style_node is not None else None
            if style == "Heading2":
                current_section = ptext
                heading2_texts.append(ptext)
                continue
            if ptext and current_section in {section.removeprefix("## ") for section in spec["sections"]} and style not in {
                "Heading3", "Heading4", "Caption", "TableText", "ListParagraph"
            }:
                body_styles.append(style)
    three_line = bool(table_audits) and all(
        all(audit[name] for name in (
            "top_and_bottom_rules_present", "vertical_and_body_rules_absent",
            "header_bottom_rule_present_in_every_cell", "body_cells_have_no_overriding_borders", "shading_absent",
        )) for audit in table_audits
    )
    return {
        "sha256": sha256(path), "crc_ok": crc is None, "text": text,
        "core_text": core_text, "media": media, "drawings": drawings,
        "header_footer": header_footer, "comments": comments, "all_xml": all_xml,
        "styles_xml": styles_xml, "table_count": len(tables), "table_audits": table_audits,
        "all_tables_three_line": three_line, "body_styles": body_styles,
        "heading2_texts": heading2_texts,
    }


def rebuild_matches(md: Path, docx: Path, language: str) -> tuple[bool, str]:
    with tempfile.TemporaryDirectory(prefix="md-alllhrc-full-audit-") as tmp:
        rebuilt = Path(tmp) / docx.name
        run = subprocess.run(
            [sys.executable, str(BUILDER), "--clean-manuscript", "--timestamp", TIMESTAMP,
             "--input", str(md), "--output", str(rebuilt), "--title", language],
            cwd=ROOT, capture_output=True, text=True,
        )
        if run.returncode:
            return False, run.stderr.strip() or run.stdout.strip()
        return rebuilt.read_bytes() == docx.read_bytes(), ""


def audit_one(label: str, spec: dict) -> dict:
    md_path = ROOT / spec["md"]
    docx_path = ROOT / spec["docx"]
    md = md_path.read_text(encoding="utf-8")
    sections = re.findall(r"(?m)^##\s+.+$", md)
    methods = md.split(spec["sections"][0], 1)[1].split(spec["sections"][1], 1)[0]
    results = md.split(spec["sections"][1], 1)[1].split(spec["sections"][2], 1)[0]
    discussion = md.split(spec["sections"][2], 1)[1]
    docx = inspect_docx(docx_path, spec)
    reproducible, rebuild_error = rebuild_matches(md_path, docx_path, spec["language"])
    table_rows = markdown_table_rows(md)
    method_tokens = (
        ("GROMACS", "Amber99SB-ILDN", "TIP3P", "2,000", "300 K", "1 bar", "2-fs", "LINCS", "particle-mesh Ewald", "20 ps")
        if spec["language"] == "English" else
        ("GROMACS", "Amber99SB-ILDN", "TIP3P", "2,000", "300 K", "1 bar", "2 fs", "LINCS", "粒子网格Ewald", "20 ps")
    )
    checks = {
        "markdown_begins_with_analysis_methods_and_has_no_visible_title": md.lstrip().startswith(spec["sections"][0]) and not re.search(r"(?m)^#\s+", md),
        "only_analysis_methods_results_and_discussion_sections_remain": sections == spec["sections"],
        "abstract_keywords_introduction_and_references_are_absent": not re.search(
            r"(?m)^##\s+(?:Abstract|摘要|Introduction|引言|References|参考文献)\s*$|^\*\*(?:Keywords|关键词)", md
        ),
        "citation_markup_and_numbered_reference_list_are_absent": "[@" not in md and not re.search(r"(?m)^\d+\.\s+.+doi:10\.", md),
        "analysis_methods_are_detailed": all(value in methods for value in method_tokens),
        "all_principal_numeric_results_are_retained": all(value in results for value in REQUIRED_NUMERIC),
        "digitized_rmsd_status_is_disclosed": spec["digitized"] in md,
        "source_plot_identity_discrepancy_is_disclosed": spec["identity"] in md,
        "atanasova_is_framework_not_transferred_data": "Atanasova" in discussion and ("1-μs" in discussion or "1 μs" in discussion) and "ALLLHRC" in discussion,
        "binding_and_function_boundaries_are_explicit": all(value in md for value in spec["limits"]),
        "single_trajectory_and_raw_archive_limits_are_explicit": ("one trajectory" in discussion if spec["language"] == "English" else "单条轨迹" in discussion) and ("raw" in md.lower() if spec["language"] == "English" else "原始" in md),
        "two_markdown_tables_are_retained": table_rows == [9, 6],
        "docx_zip_crc_is_valid": docx["crc_ok"],
        "docx_visible_content_starts_with_analysis_methods": docx["text"].startswith(spec["start"]),
        "docx_has_only_analysis_methods_results_and_discussion_headings": docx["heading2_texts"] == [heading.removeprefix("## ") for heading in spec["sections"]],
        "docx_core_title_is_neutral": spec["language"] in docx["core_text"] and "ALLLHRC" not in docx["core_text"],
        "docx_has_no_media_drawings_header_footer_page_or_comments": (
            not docx["media"] and docx["drawings"] == 0 and not docx["header_footer"] and not docx["comments"]
            and 'w:instr="PAGE"' not in docx["all_xml"] and "/relationships/image" not in docx["all_xml"]
        ),
        "docx_uses_journal_body_style_and_indent": (
            '<w:sz w:val="24"/><w:szCs w:val="24"/>' in docx["styles_xml"]
            and 'w:line="480" w:lineRule="auto"' in docx["styles_xml"]
            and '<w:ind w:firstLine="480"/>' in docx["styles_xml"]
            and bool(docx["body_styles"]) and all(style == "BodyText" for style in docx["body_styles"])
        ),
        "docx_has_one_inch_margins": all(f'w:{side}="1440"' in docx["all_xml"] for side in ("top", "right", "bottom", "left")),
        "docx_has_two_three_line_tables": docx["table_count"] == 2 and docx["all_tables_three_line"],
        "docx_has_no_zotero_or_numbered_citation_fields": "ADDIN ZOTERO_ITEM CSL_CITATION" not in docx["all_xml"] and "[1]" not in docx["text"],
        "docx_is_byte_reproducible": reproducible,
    }
    return {
        "label": label, "markdown": spec["md"], "docx": spec["docx"],
        "markdown_sha256": sha256(md_path), "docx_sha256": docx["sha256"],
        "body_word_count": len(md.split()), "body_character_count": len(md),
        "table_data_row_counts": table_rows, "embedded_media": docx["media"],
        "drawings": docx["drawings"], "table_audits": docx["table_audits"],
        "rebuild_error": rebuild_error, "checks": checks,
        "verdict": "PASS" if all(checks.values()) else "FAIL",
    }


def main() -> int:
    records = {label: audit_one(label, spec) for label, spec in SPECS.items()}
    source_checks = {path: sha256(ROOT / path) == expected for path, expected in SOURCE_HASHES.items()}
    screening_checks = {path: sha256(ROOT / path) == expected for path, expected in SCREENING_DOCX_HASHES.items()}
    concise_dir = ROOT / "manuscript" / "md_alllhrc" / "concise"
    package_checks = {
        "only_two_full_language_reports_are_delivered": len(records) == 2,
        "all_full_language_reports_pass": all(record["verdict"] == "PASS" for record in records.values()),
        "md_concise_directory_is_absent": not concise_dir.exists(),
        "both_reports_have_no_abstract_or_references": all(record["checks"]["abstract_keywords_introduction_and_references_are_absent"] for record in records.values()),
        "all_source_support_hashes_match": all(source_checks.values()),
        "all_six_screening_docx_files_are_unchanged": all(screening_checks.values()),
        "both_docx_files_are_figure_free": all(not record["embedded_media"] and record["drawings"] == 0 for record in records.values()),
    }
    report = {
        "schema": "local.md_alllhrc_package_audit.v2",
        "scope": "Full-only English/Chinese ALLLHRC–AChE reports containing analysis methods, results and discussion; no abstract or references.",
        "source_support_sha256": {path: {"expected": expected, "matches": source_checks[path]} for path, expected in SOURCE_HASHES.items()},
        "screening_docx_sha256": {path: {"expected": expected, "matches": screening_checks[path]} for path, expected in SCREENING_DOCX_HASHES.items()},
        "records": records, "package_checks": package_checks,
        "citation_mode": "No citation apparatus: no in-text citation fields and no reference list by user instruction.",
        "verdict": "PASS" if all(package_checks.values()) else "FAIL",
    }
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(OUT)
    return 0 if report["verdict"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
