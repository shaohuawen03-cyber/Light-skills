#!/usr/bin/env python3
"""Audit the clean, separate English and Chinese full manuscripts."""
from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
SOURCE_AUDIT = ROOT / "scripts" / "audit_submission_manuscripts.py"
SOURCE_REPORT = ROOT / "quality_reports" / "submission_manuscript_audit.json"
OUT = ROOT / "quality_reports" / "full_manuscript_audit.json"


def main() -> int:
    run = subprocess.run([sys.executable, str(SOURCE_AUDIT)], cwd=ROOT)
    master = json.loads(SOURCE_REPORT.read_text(encoding="utf-8"))
    records = {
        key: value for key, value in master["records"].items()
        if key.startswith("full/")
    }
    checks = {
        "english_full_pass": records["full/English"]["verdict"] == "PASS",
        "chinese_full_pass": records["full/Chinese"]["verdict"] == "PASS",
        "reference_inventory_is_synchronized": (
            records["full/English"]["reference_doi_count"]
            == records["full/Chinese"]["reference_doi_count"] == 55
        ),
        "both_docx_files_are_figure_free": all(not item["embedded_media"] for item in records.values()),
        "all_eight_tables_are_three_line": all(
            item["checks"]["every_docx_table_is_three_line"] for item in records.values()
        ),
        "conclusion_and_statistical_analysis_sections_are_absent": all(
            item["checks"]["standalone_conclusion_section_absent"]
            and item["checks"]["statistical_analysis_subsection_absent"]
            and item["checks"]["discussion_proceeds_directly_to_references"]
            for item in records.values()
        ),
        "zotero_live_status_is_not_misrepresented": all(
            item["zotero_live_field_count"] == 0 for item in records.values()
        ),
    }
    report = {
        "schema": "local.full_manuscript_audit.v3",
        "scope": "Separate, titleless, figure-free full English and Chinese manuscripts.",
        "records": records,
        "checks": checks,
        "zotero_acceptance_state": master["zotero_acceptance_state"],
        "verdict": "PASS" if run.returncode == 0 and all(checks.values()) else "FAIL",
    }
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(OUT)
    return 0 if report["verdict"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
