#!/usr/bin/env python3
"""Audit the new intermediate English/Chinese screening manuscripts."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
SOURCE_AUDIT = ROOT / "scripts" / "audit_submission_manuscripts.py"
SOURCE_REPORT = ROOT / "quality_reports" / "submission_manuscript_audit.json"
OUT = ROOT / "quality_reports" / "intermediate_package_audit.json"
UNCHANGED_DOCX = {
    "manuscript/full/Chinese.docx": "610fcb7f7c09287233fa699c8f7043b665aa1a5d06d4d05e0c3f527ee8125c91",
    "manuscript/full/English.docx": "98943ba415134a0ca47b00022371d9e75abe6d76cac9d8f540cc6984adca2c32",
    "manuscript/concise/Chinese.docx": "e1529a0bb0f2e22afc68e7e9966816f4f3d9a3a496159dc9aaf98a42a9241ddc",
    "manuscript/concise/English.docx": "7dfbe9e65504d61e56fb58d39940bc9e0ded439a07557be21913e4def2a994b7",
    "manuscript/md_alllhrc/full/Chinese.docx": "be279a68ceb41515bcd097b9a73b05be49e44cccff7aad8ab502ca9dc200b50f",
    "manuscript/md_alllhrc/full/English.docx": "bf52b704c4f187ac721e5a936243726c97102eff0389fc1b8ba55c0f936973aa",
    "manuscript/md_alllhrc/concise/Chinese.docx": "87d6d37a2d2918335a1d334b7be08f51c493b29dae6bebb4adf3e8fdbc389f94",
    "manuscript/md_alllhrc/concise/English.docx": "e0564158aff137fc75d8e807b098229b7f10fadb7f514f7f0cdc66a2f81cc4c9",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    run = subprocess.run([sys.executable, str(SOURCE_AUDIT)], cwd=ROOT)
    master = json.loads(SOURCE_REPORT.read_text(encoding="utf-8"))
    records = {key: value for key, value in master["records"].items() if key.startswith("intermediate/")}
    unchanged = {
        path: {"expected": expected, "actual": sha256(ROOT / path), "matches": sha256(ROOT / path) == expected}
        for path, expected in UNCHANGED_DOCX.items()
    }
    en = records["intermediate/English"]
    zh = records["intermediate/Chinese"]
    checks = {
        "english_intermediate_pass": en["verdict"] == "PASS",
        "chinese_intermediate_pass": zh["verdict"] == "PASS",
        "reference_inventory_is_synchronized_at_40": en["reference_doi_count"] == zh["reference_doi_count"] == 40,
        "each_intermediate_docx_has_four_three_line_tables": (
            all(item["checks"]["docx_table_count_matches_markdown"] for item in records.values())
            and all(item["checks"]["every_docx_table_is_three_line"] for item in records.values())
            and all(len(item["table_audits"]) == 4 for item in records.values())
        ),
        "complete_multidimensional_table_is_retained": all(
            item["multidimensional_table_data_row_counts"] == [22]
            and item["checks"]["long_and_short_multidimensional_results_retained"]
            for item in records.values()
        ),
        "long_peptide_attrition_limitation_is_retained": all(
            item["checks"]["short_only_final_set_and_long_peptide_attrition_limit_reported"]
            for item in records.values()
        ),
        "both_docx_files_are_titleless_and_figure_free": all(
            item["checks"]["markdown_starts_with_abstract_and_has_no_h1"]
            and item["checks"]["docx_is_figure_free"]
            for item in records.values()
        ),
        "conclusion_and_statistical_analysis_sections_are_absent": all(
            item["checks"]["standalone_conclusion_section_absent"]
            and item["checks"]["statistical_analysis_subsection_absent"]
            and item["checks"]["discussion_proceeds_directly_to_references"]
            for item in records.values()
        ),
        "intermediate_length_is_between_full_and_concise": master["package_checks"]["length_order_is_full_then_intermediate_then_concise"],
        "preexisting_full_concise_and_md_docx_files_are_unchanged": all(item["matches"] for item in unchanged.values()),
        "zotero_live_status_is_not_misrepresented": all(item["zotero_live_field_count"] == 0 for item in records.values()),
    }
    report = {
        "schema": "local.intermediate_package_audit.v1",
        "scope": "Separate titleless, figure-free intermediate English and Chinese screening manuscripts; MD package excluded.",
        "records": records,
        "unchanged_preexisting_docx": unchanged,
        "checks": checks,
        "zotero_acceptance_state": master["zotero_acceptance_state"],
        "verdict": "PASS" if run.returncode == 0 and all(checks.values()) else "FAIL",
    }
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(OUT)
    return 0 if report["verdict"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
