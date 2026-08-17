#!/usr/bin/env python3
"""Audit DOCX packaging for all four current manuscript deliverables."""
from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
SOURCE_AUDIT = ROOT / "scripts" / "audit_submission_manuscripts.py"
SOURCE_REPORT = ROOT / "quality_reports" / "submission_manuscript_audit.json"
OUT = ROOT / "quality_reports" / "docx_package_audit.json"


def main() -> int:
    run = subprocess.run([sys.executable, str(SOURCE_AUDIT)], cwd=ROOT)
    master = json.loads(SOURCE_REPORT.read_text(encoding="utf-8"))
    packages = {}
    for label, record in master["records"].items():
        checks = {
            name: value for name, value in record["checks"].items()
            if name.startswith("docx_") or name == "every_docx_table_is_three_line"
        }
        packages[label] = {
            "path": record["docx"],
            "sha256": record["docx_sha256"],
            "embedded_media": record["embedded_media"],
            "drawings": record["drawings"],
            "zotero_live_field_count": record["zotero_live_field_count"],
            "citation_mode": record["citation_mode"],
            "table_audits": record["table_audits"],
            "checks": checks,
            "verdict": "PASS" if all(checks.values()) else "FAIL",
        }
    checks = {
        "four_current_docx_packages_audited": len(packages) == 4,
        "all_packages_pass": all(item["verdict"] == "PASS" for item in packages.values()),
        "all_packages_are_figure_free": all(not item["embedded_media"] and item["drawings"] == 0 for item in packages.values()),
        "all_tables_are_three_line": all(
            item["checks"]["every_docx_table_is_three_line"] for item in packages.values()
        ),
        "static_files_are_not_misrepresented_as_zotero_live": all(
            item["zotero_live_field_count"] == 0 for item in packages.values()
        ),
    }
    report = {
        "schema": "local.docx_package_audit.v4",
        "packages": packages,
        "checks": checks,
        "zotero_acceptance_state": master["zotero_acceptance_state"],
        "verdict": "PASS" if run.returncode == 0 and all(checks.values()) else "FAIL",
    }
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(OUT)
    return 0 if report["verdict"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
