#!/usr/bin/env python3
"""Audit DOI-set parity across both manuscripts and reference records."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
FILES = {
    "manuscript_en": ROOT / "manuscript" / "manuscript_en.md",
    "manuscript_zh": ROOT / "manuscript" / "manuscript_zh.md",
    "verified_references": ROOT / "references" / "verified_references.md",
    "bibtex": ROOT / "references" / "references.bib",
}
OUT = ROOT / "quality_reports" / "citation_inventory_audit.json"
DOI_RE = re.compile(r"10\.\d{4,9}/[-._;()/:A-Z0-9]+", re.I)
TRAILING = ".,;:)]}"


def dois(text: str) -> set[str]:
    return {match.group(0).rstrip(TRAILING).lower() for match in DOI_RE.finditer(text)}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    sets: dict[str, set[str]] = {}
    records = {}
    for name, path in FILES.items():
        found = dois(path.read_text(encoding="utf-8"))
        sets[name] = found
        records[name] = {
            "path": str(path.relative_to(ROOT)),
            "sha256": sha256(path),
            "unique_doi_count": len(found),
        }

    canonical = sets["verified_references"]
    missing = {name: sorted(canonical - found) for name, found in sets.items()}
    extra = {name: sorted(found - canonical) for name, found in sets.items()}
    parity = all(found == canonical for found in sets.values())
    expected_count = len(canonical) == 25
    report = {
        "schema": "local.citation_inventory_audit.v2",
        "files": records,
        "canonical_dois": sorted(canonical),
        "canonical_count_is_25": expected_count,
        "english_chinese_doi_parity": sets["manuscript_en"] == sets["manuscript_zh"],
        "all_file_doi_parity": parity,
        "missing_by_file": missing,
        "extra_by_file": extra,
        "verification_boundary": (
            "Inventory parity only. Title, identifier, and core metadata checks are recorded in "
            "references/verified_references.md; final Crossmark, correction, and retraction screening remains required."
        ),
        "verdict": "PASS" if parity and expected_count else "FAIL",
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(OUT)
    return 0 if report["verdict"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
