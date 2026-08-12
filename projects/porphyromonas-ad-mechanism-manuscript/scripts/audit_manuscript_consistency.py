#!/usr/bin/env python3
"""Deterministic bilingual number, boundary, and reference audit."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
EN = ROOT / "manuscript" / "manuscript_en.md"
ZH = ROOT / "manuscript" / "manuscript_zh.md"

EXPECTED = [
    "11,269,961", "11,721,988", "31,510", "33,786", "30,557", "32,754",
    "3,359", "3,446", "953", "1,032", "40", "72", "3,518", "3,299",
    "219", "923", "111", "15", "12", "8", "10.99", "10.52", "4.20",
    "6.98", "97.95", "27.98", "13.51", "10.81", "7.21",
]

PROHIBITED_EN = {
    "identified periodontitis-specific": "Disease specificity is not established.",
    "periodontitis-specific oral micropeptides": "Disease specificity is not established.",
    "p. gingivalis-derived candidates": "Taxonomic origin is not established.",
    "proved that": "Causal/mechanistic proof is not available.",
    "demonstrated that the candidates": "Candidate mechanism is not validated.",
}
PROHIBITED_ZH = {
    "牙周炎特异性微肽": "未建立疾病特异性。",
    "牙龈卟啉单胞菌来源候选": "未建立分类学来源。",
    "证明这些候选": "未完成机制验证。",
    "证实这些候选": "未完成机制验证。",
}


def file_sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def before_refs(text: str, marker: str) -> str:
    return text.split(marker, 1)[0]


def audit(path: Path, lang: str):
    text = path.read_text(encoding="utf-8")
    body = before_refs(text, "## References" if lang == "en" else "## 参考文献")
    missing_numbers = [value for value in EXPECTED if value not in body]
    prohibited = PROHIBITED_EN if lang == "en" else PROHIBITED_ZH
    prohibited_hits = [
        {"phrase": phrase, "reason": reason}
        for phrase, reason in prohibited.items()
        if phrase in body.lower() if lang == "en"
    ] if lang == "en" else [
        {"phrase": phrase, "reason": reason}
        for phrase, reason in prohibited.items()
        if phrase in body
    ]
    placeholders = sorted(set(re.findall(r"\b(?:TODO|TBD|RESULT GAP|MATERIAL GAP)\b", text, flags=re.I)))
    ref_block = text.split("## References", 1)[1] if lang == "en" else text.split("## 参考文献", 1)[1]
    reference_numbers = [int(n) for n in re.findall(r"(?m)^(\d+)\.\s", ref_block)]
    return {
        "path": str(path.relative_to(ROOT)),
        "sha256": file_sha(path),
        "missing_expected_numbers": missing_numbers,
        "prohibited_claim_hits": prohibited_hits,
        "placeholder_hits": placeholders,
        "reference_numbers": reference_numbers,
        "reference_sequence_ok": reference_numbers == list(range(1, 18)),
    }


def main() -> int:
    en = audit(EN, "en")
    zh = audit(ZH, "zh")
    checks = {
        "english": en,
        "chinese": zh,
        "core_number_presence_bilingual": not en["missing_expected_numbers"] and not zh["missing_expected_numbers"],
        "prohibited_claims_absent": not en["prohibited_claim_hits"] and not zh["prohibited_claim_hits"],
        "placeholders_absent": not en["placeholder_hits"] and not zh["placeholder_hits"],
        "references_1_to_17_bilingual": en["reference_sequence_ok"] and zh["reference_sequence_ok"],
    }
    checks["verdict"] = "PASS" if all(v for k, v in checks.items() if isinstance(v, bool)) else "FAIL"
    print(json.dumps(checks, ensure_ascii=False, indent=2))
    return 0 if checks["verdict"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
