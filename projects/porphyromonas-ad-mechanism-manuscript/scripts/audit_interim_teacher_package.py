#!/usr/bin/env python3
"""Audit the separate English and Chinese interim teacher drafts."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "manuscript" / "interim_teacher"
OUT = ROOT / "quality_reports" / "interim_teacher_package_audit.json"
DOI_RE = re.compile(r"10\.\d{4,9}/[-._;()/:A-Z0-9]+", re.I)
CITATION_RE = re.compile(r"\[([0-9,;\-–—\s]+)\]")
EXPECTED = [
    "11,269,961", "11,721,988", "31,510", "33,786", "3,518", "3,299",
    "923", "111", "15", "12", "8", "FLLHTTR", "HVLLLRQCA", "−9.60", "−8.25",
]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def citations(body: str) -> list[int]:
    found: set[int] = set()
    for match in CITATION_RE.finditer(body):
        for part in re.split(r"[,;]", match.group(1)):
            part = part.strip()
            span = re.fullmatch(r"(\d+)\s*[-–—]\s*(\d+)", part)
            if span:
                start, end = map(int, span.groups())
                found.update(range(min(start, end), max(start, end) + 1))
            elif part.isdigit():
                found.add(int(part))
    return sorted(found)


def dois(text: str) -> set[str]:
    return {m.group(0).rstrip(".,;:)]}").lower() for m in DOI_RE.finditer(text)}


def audit(path: Path, ref_heading: str, prohibited: list[str]) -> dict:
    text = path.read_text(encoding="utf-8")
    body, refs = text.split(ref_heading, 1)
    ref_numbers = [int(x) for x in re.findall(r"(?m)^(\d+)\.\s", refs)]
    return {
        "path": str(path.relative_to(ROOT)),
        "sha256": sha256(path),
        "characters": len(text),
        "body_whitespace_tokens": len(body.split()),
        "h2_sections": re.findall(r"(?m)^##\s+(.+)$", text),
        "missing_expected_values": [x for x in EXPECTED if x not in body],
        "cited_numbers": citations(body),
        "all_references_cited": citations(body) == list(range(1, 21)),
        "reference_numbers_sequential": ref_numbers == list(range(1, 21)),
        "doi_set": sorted(dois(refs)),
        "prohibited_hits": [phrase for phrase in prohibited if phrase.lower() in body.lower()],
        "gap_markers": sorted(set(re.findall(r"\b(?:TODO|TBD|RESULT GAP|MATERIAL GAP)\b", text, re.I))),
    }


def main() -> int:
    en = audit(
        BASE / "interim_teacher_en.md",
        "## References",
        ["proved that", "periodontitis-specific oral micropeptides", "experimentally validated binding"],
    )
    zh = audit(
        BASE / "interim_teacher_zh.md",
        "## 参考文献",
        ["证明这些候选", "牙周炎特异性微肽", "经实验验证的结合"],
    )
    checks = {
        "english_has_seven_h2_sections": len(en["h2_sections"]) == 7,
        "chinese_has_seven_h2_sections": len(zh["h2_sections"]) == 7,
        "locked_values_present_bilingual": not en["missing_expected_values"] and not zh["missing_expected_values"],
        "references_1_to_20_sequential_bilingual": en["reference_numbers_sequential"] and zh["reference_numbers_sequential"],
        "references_1_to_20_cited_bilingual": en["all_references_cited"] and zh["all_references_cited"],
        "twenty_doi_inventory_parity": len(en["doi_set"]) == 20 and en["doi_set"] == zh["doi_set"],
        "prohibited_assertions_absent": not en["prohibited_hits"] and not zh["prohibited_hits"],
        "gap_markers_absent": not en["gap_markers"] and not zh["gap_markers"],
    }
    report = {
        "schema": "local.interim_teacher_package_audit.v1",
        "version": "3.1.0",
        "english": en,
        "chinese": zh,
        "checks": checks,
        "verdict": "PASS" if all(checks.values()) else "FAIL",
        "boundary": "Content parity and deterministic transcription checks only; this does not reproduce screening or docking.",
    }
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(OUT)
    return 0 if report["verdict"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
