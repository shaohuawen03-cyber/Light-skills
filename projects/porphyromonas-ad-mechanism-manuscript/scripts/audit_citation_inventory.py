#!/usr/bin/env python3
"""Audit BibTeX/citation/reference parity for full, intermediate, and concise manuscripts."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "quality_reports" / "citation_inventory_audit.json"
BIB = ROOT / "references" / "references.bib"
VERIFIED = ROOT / "references" / "verified_references.md"
MANUSCRIPTS = {
    "full_english": ROOT / "manuscript/full/English.md",
    "full_chinese": ROOT / "manuscript/full/Chinese.md",
    "intermediate_english": ROOT / "manuscript/intermediate/English.md",
    "intermediate_chinese": ROOT / "manuscript/intermediate/Chinese.md",
    "concise_english": ROOT / "manuscript/concise/English.md",
    "concise_chinese": ROOT / "manuscript/concise/Chinese.md",
}
DOI_RE = re.compile(r"10\.\d{4,9}/[-._;()/:A-Z0-9]+", re.I)


def dois(text: str) -> set[str]:
    return {m.group(0).rstrip(".,;:)]}").lower() for m in DOI_RE.finditer(text)}


def keys(text: str) -> set[str]:
    return set(re.findall(r"(?m)^@[A-Za-z]+\{([^,]+),", text))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def body_keys(text: str) -> set[str]:
    heading = "## References" if "## References" in text else "## 参考文献"
    return set(re.findall(r"@([A-Za-z0-9_.:+-]+)", text.split(heading, 1)[0]))


def main() -> int:
    bib_text = BIB.read_text(encoding="utf-8")
    bib_dois = dois(bib_text)
    bib_keys = keys(bib_text)
    verified_dois = dois(VERIFIED.read_text(encoding="utf-8"))
    records = {}
    manuscript_dois = {}
    manuscript_keys = {}
    for name, path in MANUSCRIPTS.items():
        text = path.read_text(encoding="utf-8")
        manuscript_dois[name] = dois(text.split("## References", 1)[-1].split("## 参考文献", 1)[-1])
        manuscript_keys[name] = body_keys(text)
        records[name] = {
            "path": str(path.relative_to(ROOT)),
            "sha256": sha256(path),
            "reference_doi_count": len(manuscript_dois[name]),
            "cited_key_count": len(manuscript_keys[name]),
            "unknown_keys": sorted(manuscript_keys[name] - bib_keys),
            "unknown_reference_dois": sorted(manuscript_dois[name] - bib_dois),
        }
    checks = {
        "bibtex_has_55_unique_keys_and_dois": len(bib_keys) == 55 and len(bib_dois) == 55,
        "verified_reference_inventory_matches_bibtex": verified_dois == bib_dois,
        "full_english_chinese_reference_parity": manuscript_dois["full_english"] == manuscript_dois["full_chinese"] == bib_dois,
        "full_cited_keys_exist_in_bibtex": manuscript_keys["full_english"] <= bib_keys and manuscript_keys["full_chinese"] <= bib_keys,
        "intermediate_english_chinese_reference_parity": manuscript_dois["intermediate_english"] == manuscript_dois["intermediate_chinese"],
        "intermediate_reference_count_is_40": len(manuscript_dois["intermediate_english"]) == 40,
        "intermediate_cited_keys_match_reference_subset": manuscript_keys["intermediate_english"] == manuscript_keys["intermediate_chinese"] and len(manuscript_keys["intermediate_english"]) == 40,
        "concise_english_chinese_reference_parity": manuscript_dois["concise_english"] == manuscript_dois["concise_chinese"],
        "concise_reference_count_is_22": len(manuscript_dois["concise_english"]) == 22,
        "concise_cited_keys_match_reference_subset": manuscript_keys["concise_english"] == manuscript_keys["concise_chinese"] and len(manuscript_keys["concise_english"]) == 22,
        "no_unknown_keys_or_dois": all(not item["unknown_keys"] and not item["unknown_reference_dois"] for item in records.values()),
    }
    report = {
        "schema": "local.citation_inventory_audit.v4",
        "bibtex": {"path": str(BIB.relative_to(ROOT)), "sha256": sha256(BIB)},
        "verified_references": {"path": str(VERIFIED.relative_to(ROOT)), "sha256": sha256(VERIFIED)},
        "manuscripts": records,
        "checks": checks,
        "zotero_source_mode": "Pandoc citation keys linked to references/references.bib",
        "verdict": "PASS" if all(checks.values()) else "FAIL",
    }
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(OUT)
    return 0 if report["verdict"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
