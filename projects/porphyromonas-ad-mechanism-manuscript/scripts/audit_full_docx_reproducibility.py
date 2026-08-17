#!/usr/bin/env python3
"""Rebuild both full DOCX files in isolation and require byte-identical output."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
BUILDER = ROOT / "scripts" / "build_docx_stdlib.py"
OUT = ROOT / "quality_reports" / "full_docx_reproducibility.json"
TIMESTAMP = "2026-08-17T00:00:00Z"
SPECS = {
    "English": "English",
    "Chinese": "Chinese",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    records = {}
    with tempfile.TemporaryDirectory(prefix="full-docx-rebuild-") as directory:
        temp = Path(directory)
        for language, title in SPECS.items():
            source = ROOT / "manuscript" / "full" / f"{language}.md"
            released = ROOT / "manuscript" / "full" / f"{language}.docx"
            rebuilt = temp / f"{language}.docx"
            subprocess.run([
                sys.executable,
                str(BUILDER),
                "--clean-manuscript",
                "--timestamp", TIMESTAMP,
                "--input", str(source),
                "--output", str(rebuilt),
                "--title", title,
            ], check=True, stdout=subprocess.DEVNULL)
            released_hash = sha256(released)
            rebuilt_hash = sha256(rebuilt)
            records[language] = {
                "source": str(source.relative_to(ROOT)),
                "released_docx": str(released.relative_to(ROOT)),
                "released_sha256": released_hash,
                "isolated_rebuild_sha256": rebuilt_hash,
                "byte_identical": released.read_bytes() == rebuilt.read_bytes(),
            }
    verdict = "PASS" if all(item["byte_identical"] for item in records.values()) else "FAIL"
    report = {
        "schema": "local.full_docx_reproducibility.v2",
        "fixed_core_timestamp": TIMESTAMP,
        "records": records,
        "verdict": verdict,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(OUT)
    return 0 if verdict == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
