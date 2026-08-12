#!/usr/bin/env python3
"""Ensure excluded-source identities remain confined to their dedicated audit record."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
RECORD = ROOT / "evidence" / "excluded_source_record.md"
OUT = ROOT / "quality_reports" / "excluded_source_scope.json"
TEXT_SUFFIXES = {".md", ".txt", ".json", ".py", ".bib", ".svg", ".xml", ".yml", ".yaml", ".csv", ".tsv"}


def main() -> int:
    record = RECORD.read_text(encoding="utf-8")
    excluded_section = record.split("## Excluded files", 1)[1].split("## In-scope", 1)[0]
    identities = sorted(set(re.findall(r"`([^`]+\.(?:docx|pdf))`", excluded_section, flags=re.I)))
    violations = []
    forbidden_files_present = []
    for identity in identities:
        fingerprint = hashlib.sha256(identity.encode("utf-8")).hexdigest()
        for path in ROOT.rglob("*"):
            if not path.is_file() or path == RECORD or path == OUT:
                continue
            if ".git" in path.parts:
                continue
            if path.name == identity:
                forbidden_files_present.append({"identity_sha256": fingerprint, "path": str(path.relative_to(ROOT))})
            if path.suffix.lower() not in TEXT_SUFFIXES:
                continue
            try:
                text = path.read_text(encoding="utf-8")
            except (UnicodeDecodeError, OSError):
                continue
            if identity in text:
                violations.append({"identity_sha256": fingerprint, "path": str(path.relative_to(ROOT))})
    report = {
        "schema": "local.excluded_source_scope.v1",
        "identity_count_from_dedicated_record": len(identities),
        "dedicated_record": str(RECORD.relative_to(ROOT)),
        "identity_occurrences_outside_dedicated_record": violations,
        "excluded_files_present": forbidden_files_present,
        "verdict": "PASS" if identities and not violations and not forbidden_files_present else "FAIL",
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(OUT)
    return 0 if report["verdict"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
