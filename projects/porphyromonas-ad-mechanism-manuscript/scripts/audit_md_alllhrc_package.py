#!/usr/bin/env python3
"""Audit the expanded full-only docking and molecular-dynamics reports."""
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
        "peptides": [
            "ALLLHRC", "FCLHLQLR", "FLLHTTR", "HLLTLKKHV", "HLPLLHRCC",
            "HVLLLRQCA", "LLHLPKRTT", "LLHPLRC", "LLHPLRL", "WLLVHLKK",
            "YHHLLCRR", "YLSLLQR",
        ],
        "systems": ["apo AChE", "ALLLHRC", "FLLHTTR", "YLSLLQR"],
        "pas_terms": ["Peripheral Anionic Site", "PAS", "Tyr72", "Asp74", "Trp286", "Tyr341"],
        "discussion_authors": ["Atanasova", "Dominy", "Silman", "Inestrosa", "Hampel", "Bartus", "Selkoe"],
        "figures": ["Figure 1", "Figure 2", "Figure 3", "Figure 4", "Figure 5", "Figure 6", "Figure S1"],
        "limits": ["100-ns", "single high-resolution trajectories", "isothermal titration calorimetry", "surface plasmon resonance"],
    },
    "full/Chinese": {
        "md": "manuscript/md_alllhrc/full/Chinese.md",
        "docx": "manuscript/md_alllhrc/full/Chinese.docx",
        "language": "Chinese",
        "start": "分析方法",
        "sections": ["## 分析方法", "## 结果", "## 讨论"],
        "peptides": [
            "ALLLHRC", "FCLHLQLR", "FLLHTTR", "HLLTLKKHV", "HLPLLHRCC",
            "HVLLLRQCA", "LLHLPKRTT", "LLHPLRC", "LLHPLRL", "WLLVHLKK",
            "YHHLLCRR", "YLSLLQR",
        ],
        "systems": ["apo AChE", "ALLLHRC", "FLLHTTR", "YLSLLQR"],
        "pas_terms": ["外周阴离子位点", "PAS", "Tyr72", "Asp74", "Trp286", "Tyr341"],
        "discussion_authors": ["Atanasova", "Dominy", "Silman", "Inestrosa", "Hampel", "Bartus", "Selkoe"],
        "figures": ["图1", "图2", "图3", "图4", "图5", "图6", "图S1"],
        "limits": ["100 ns", "单条", "等温滴定量热", "表面等离子共振"],
    },
}
REQUIRED_NUMERIC = [
    "-9.60", "-9.49", "-9.29", "-8.77", "-9.44", "-9.18", "1.41",
    "0.1562", "0.1916", "0.2102", "0.2064",
    "0.0783", "0.0876", "0.0901", "0.0813", "2.2967", "2.3107", "2.3163", "2.3004",
    "212.41", "217.47", "216.34", "210.37", "2.19", "2.80", "4.23",
]
SOURCE_HASHES = {
    "source_materials/md_alllhrc/digitized_rmsd_100ns.csv": "b34c48db440f5cddd2a782e12713172359edc23c737b14726c602cfef32b565a",
    "source_materials/md_alllhrc/peptide_rmsd_jump_diagnosis.txt": "43f3f84ae57b1f037e80f4aed3d9cb3614a0df92f64a7e3c92c2972291f6f3f3",
    "source_materials/md_results/compare_summary_alllhrc.csv": "aaca2ad9611d20e0c1d1cc2fd318f146964680cc654bd69752beda287b5df5d8",
    "source_materials/md_results/compare_summary_fllhttr.csv": "c48cee16a72c8381cf4d8e6cdcfa21501467962514ee831dba2c4fa0ee96fdf6",
    "source_materials/md_results/compare_summary_ylsllqr.csv": "db561014757d8bfd708e6e8c5aa32f70a614813d315197a02cde491828876f05",
    "source_materials/md_results/docking_12peptides_summary.csv": "055acade7cfba02ac23ff97add253aba0e8fa4882cc4a5d6d8a26bbd37158dcc",
    "source_materials/md_results/local_vina_docking_summary.csv": "7dd9c26e9f5b0cdf4e8b87a55cb498ec5e5f10fe0292eb880c5d74cacd769f82",
    "source_materials/md_results/RESULTS_ANALYSIS_v1.md": "2678919e6033430ad5b556372e7dc96bd9f0fa83d34f60c61aca3b71543608f2",
    "source_materials/md_results/SCI_Methods_GROMACS_MD_Simulation.md": "9d1be85cd0afaa3cc859ac699c91c5b556ff92f9b61cfe968232e696f4402194",
    "docking/Summary_Vina_Docking.csv": "01d7987c43934f55661274694f3d75a307378235aabcf1ff85ec1de634fa50d0",
}
FIGURE_FILES = [
    "manuscript/figures/fig5_docking_scores.svg",
    "manuscript/figures/fig5_docking_scores.png",
    "manuscript/figures/fig_docking_poses_A_F.png",
    "manuscript/figures/fig_docking_poses_G_L.png",
    "manuscript/figures/fig_docking_poses_12_combined.png",
    "manuscript/figures/fig_compare_ache_vs_alllhrc.png",
    "manuscript/figures/fig_compare_ache_vs_fllhttr.png",
    "manuscript/figures/fig_compare_ache_vs_ylsllqr.png",
]
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
                "Heading3", "Heading4", "Caption", "TableText", "ListParagraph", "Reference", "Figure"
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
    with tempfile.TemporaryDirectory(prefix="md-full-audit-") as tmp:
        rebuilt = Path(tmp) / docx.name
        run = subprocess.run(
            [sys.executable, str(BUILDER.resolve()), "--clean-manuscript", "--allow-images", "--timestamp", TIMESTAMP,
             "--input", str(md.resolve()), "--output", str(rebuilt.resolve()), "--title", language],
            cwd=ROOT, capture_output=True, text=True,
        )
        if run.returncode:
            return False, run.stderr.strip() or run.stdout.strip()
        return rebuilt.read_bytes() == docx.read_bytes(), ""


def audit_one(label: str, spec: dict) -> dict:
    md_path = (ROOT / spec["md"]).resolve()
    docx_path = (ROOT / spec["docx"]).resolve()
    md = md_path.read_text(encoding="utf-8")
    sections = re.findall(r"(?m)^##\s+.+$", md)
    methods = md.split(spec["sections"][0], 1)[1].split(spec["sections"][1], 1)[0]
    results = md.split(spec["sections"][1], 1)[1].split(spec["sections"][2], 1)[0]
    discussion = md.split(spec["sections"][2], 1)[1]
    docx = inspect_docx(docx_path, spec)
    reproducible, rebuild_error = rebuild_matches(md_path, docx_path, spec["language"])
    table_rows = markdown_table_rows(md)
    method_tokens = (
        ("GROMACS", "Amber99SB-ILDN", "TIP3P", "2,000", "300 K", "1.0 bar", "2.0 fs", "LINCS", "Particle Mesh Ewald", "20 ps")
        if spec["language"] == "English" else
        ("GROMACS", "Amber99SB-ILDN", "TIP3P", "2,000", "300 K", "1.0 bar", "2.0 fs", "LINCS", "粒子网格Ewald", "20 ps")
    )
    checks = {
        "markdown_begins_with_analysis_methods_and_has_no_visible_title": md.lstrip().startswith(spec["sections"][0]) and not re.search(r"(?m)^#\s+", md),
        "only_analysis_methods_results_and_discussion_sections_remain": sections == spec["sections"],
        "abstract_keywords_introduction_are_absent": not re.search(
            r"(?m)^##\s+(?:Abstract|摘要|Introduction|引言)\s*$|^\*\*(?:Keywords|关键词)", md
        ),
        "methods_and_results_contain_no_citations": "[@" not in methods and "[@" not in results and not re.search(r"(?m)^\d+\.\s+.+doi:10\.", methods) and not re.search(r"(?m)^\d+\.\s+.+doi:10\.", results),
        "discussion_cites_high_impact_sci_literature": all(author in discussion for author in spec["discussion_authors"]),
        "analysis_methods_are_detailed": all(value in methods for value in method_tokens),
        "docking_covers_all_12_candidate_peptides": all(pep in results for pep in spec["peptides"]),
        "pas_site_docking_analysis_is_explicit": all(term in results for term in spec["pas_terms"]),
        "md_covers_apo_and_three_complexes": all(sys_name in results for sys_name in spec["systems"]),
        "all_principal_numeric_results_are_retained": all(value in results for value in REQUIRED_NUMERIC),
        "figures_are_cited_in_text": all(fig in results or fig in methods for fig in spec["figures"]),
        "markdown_embeds_seven_png_figures": len(re.findall(r"(?m)^!\[[^\]]*\]\(\.\./\.\./figures/[^)]+\.png\)$", md)) == 7,
        "binding_and_function_boundaries_are_explicit": all(value.lower() in md.lower() for value in spec["limits"]),
        "three_markdown_tables_are_retained": table_rows == [12, 13, 7],
        "docx_zip_crc_is_valid": docx["crc_ok"],
        "docx_visible_content_starts_with_analysis_methods": docx["text"].startswith(spec["start"]),
        "docx_has_only_analysis_methods_results_and_discussion_headings": docx["heading2_texts"] == [heading.removeprefix("## ") for heading in spec["sections"]],
        "docx_core_title_is_neutral": spec["language"] in docx["core_text"] and "ALLLHRC" not in docx["core_text"],
        "docx_has_no_header_footer_page_or_comments": (
            not docx["header_footer"] and not docx["comments"] and 'w:instr="PAGE"' not in docx["all_xml"]
        ),
        "docx_embeds_seven_figures": (
            docx["drawings"] == 7 and len(docx["media"]) == 7 and "/relationships/image" in docx["all_xml"]
        ),
        "docx_uses_journal_body_style_and_indent": (
            '<w:sz w:val="24"/><w:szCs w:val="24"/>' in docx["styles_xml"]
            and 'w:line="480" w:lineRule="auto"' in docx["styles_xml"]
            and '<w:ind w:firstLine="480"/>' in docx["styles_xml"]
            and bool(docx["body_styles"]) and all(style == "BodyText" for style in docx["body_styles"])
        ),
        "docx_has_one_inch_margins": all(f'w:{side}="1440"' in docx["all_xml"] for side in ("top", "right", "bottom", "left")),
        "docx_has_three_three_line_tables": docx["table_count"] == 3 and docx["all_tables_three_line"],
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
    figure_checks = {path: (ROOT / path).is_file() and (ROOT / path).stat().st_size > 0 for path in FIGURE_FILES}
    concise_dir = ROOT / "manuscript" / "md_alllhrc" / "concise"
    package_checks = {
        "only_two_full_language_reports_are_delivered": len(records) == 2,
        "all_full_language_reports_pass": all(record["verdict"] == "PASS" for record in records.values()),
        "md_concise_directory_is_absent": not concise_dir.exists(),
        "both_reports_have_no_abstract_or_introduction": all(record["checks"]["abstract_keywords_introduction_are_absent"] for record in records.values()),
        "all_source_support_hashes_match": all(source_checks.values()),
        "all_six_screening_docx_files_are_unchanged": all(screening_checks.values()),
        "cited_figure_files_are_present": all(figure_checks.values()),
        "both_docx_files_embed_seven_figures": all(record["drawings"] == 7 and len(record["embedded_media"]) == 7 for record in records.values()),
    }
    report = {
        "schema": "local.md_alllhrc_package_audit.v3",
        "scope": "Full-only English/Chinese docking and MD reports containing analysis methods, results and discussion; Discussion cites high-impact SCI literature.",
        "source_support_sha256": {path: {"expected": expected, "matches": source_checks[path]} for path, expected in SOURCE_HASHES.items()},
        "screening_docx_sha256": {path: {"expected": expected, "matches": screening_checks[path]} for path, expected in SCREENING_DOCX_HASHES.items()},
        "cited_figure_files": figure_checks,
        "records": records, "package_checks": package_checks,
        "citation_mode": "Discussion section cites high-impact SCI literature; Analysis methods and Results contain no citation markup.",
        "verdict": "PASS" if all(package_checks.values()) else "FAIL",
    }
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(OUT)
    return 0 if report["verdict"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
