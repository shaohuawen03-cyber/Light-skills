#!/usr/bin/env python3
"""Rebuild all six screening-manuscript DOCX files and require byte-identical output."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
BUILDER = ROOT / "scripts" / "build_docx_stdlib.py"
BIB = ROOT / "references" / "references.bib"
OUT = ROOT / "quality_reports" / "full_docx_reproducibility.json"
SCREENING_TIMESTAMP = "2026-08-17T00:00:00Z"
INTERMEDIATE_TIMESTAMP = "2026-08-23T00:00:00Z"
SPECS = {
    "full/English": ("manuscript/full/English.md", "manuscript/full/English.docx", "English", SCREENING_TIMESTAMP),
    "full/Chinese": ("manuscript/full/Chinese.md", "manuscript/full/Chinese.docx", "Chinese", SCREENING_TIMESTAMP),
    "intermediate/English": ("manuscript/intermediate/English.md", "manuscript/intermediate/English.docx", "English", INTERMEDIATE_TIMESTAMP),
    "intermediate/Chinese": ("manuscript/intermediate/Chinese.md", "manuscript/intermediate/Chinese.docx", "Chinese", INTERMEDIATE_TIMESTAMP),
    "concise/English": ("manuscript/concise/English.md", "manuscript/concise/English.docx", "English", SCREENING_TIMESTAMP),
    "concise/Chinese": ("manuscript/concise/Chinese.md", "manuscript/concise/Chinese.docx", "Chinese", SCREENING_TIMESTAMP),
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    records = {}
    with tempfile.TemporaryDirectory(prefix="manuscript-docx-rebuild-") as directory:
        temp = Path(directory)
        for label, (source_name, released_name, title, timestamp) in SPECS.items():
            source = ROOT / source_name
            released = ROOT / released_name
            rebuilt = temp / (label.replace("/", "-") + ".docx")
            subprocess.run([
                sys.executable, str(BUILDER), "--clean-manuscript",
                "--timestamp", timestamp, "--bibliography", str(BIB),
                "--input", str(source), "--output", str(rebuilt), "--title", title,
            ], check=True, stdout=subprocess.DEVNULL)
            records[label] = {
                "source": source_name,
                "released_docx": released_name,
                "fixed_core_timestamp": timestamp,
                "released_sha256": sha256(released),
                "isolated_rebuild_sha256": sha256(rebuilt),
                "byte_identical": released.read_bytes() == rebuilt.read_bytes(),
            }
    verdict = "PASS" if all(item["byte_identical"] for item in records.values()) else "FAIL"
    report = {
        "schema": "local.docx_reproducibility.v4",
        "fixed_core_timestamps": {
            "full_and_concise": SCREENING_TIMESTAMP,
            "intermediate": INTERMEDIATE_TIMESTAMP,
        },
        "bibliography": str(BIB.relative_to(ROOT)),
        "records": records,
        "verdict": verdict,
    }
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(OUT)
    return 0 if verdict == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
