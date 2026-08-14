#!/usr/bin/env python3
"""Audit the concise, separately packaged English and Chinese manuscripts."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "manuscript" / "concise"
OUT = ROOT / "quality_reports" / "concise_package_audit.json"
DOI_RE = re.compile(r"10\.\d{4,9}/[-._;()/:A-Z0-9]+", re.I)
CITATION_RE = re.compile(r"\[([0-9,;\-–—\s]+)\]")
EXPECTED_LOCKED = [
    "11,269,961", "11,721,988", "31,510", "33,786", "3,518", "3,299",
    "923", "111", "15", "12", "8", "FLLHTTR", "HVLLLRQCA", "−9.60", "−8.25",
]
EXPECTED_PROVENANCE = [
    "PRJNA678453", "PRJEB65451", "metaSPAdes v3.15.3", "22", "11", "66", "118",
]
EXPECTED_MODELS = [
    "deep-learning-guided", "protein language model", "320-dimensional", "six-layer deep convolutional",
    "fine-tuning", "ESM2-t30", "two-tier artificial-neural-network", "mebipred", "5-mer",
    "multi-task deep convolutional neural network", "AnOxPePred", "one-dimensional convolutional layer",
]
EXPECTED_MODELS_ZH = [
    "深度学习引导", "蛋白质语言模型", "320维", "六层深度卷积神经网络", "迁移学习",
    "ESM2-t30", "两级人工神经网络", "mebipred", "5-mer", "多任务深度卷积神经网络",
    "AnOxPePred", "一维卷积层",
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


def ordered(text: str, anchors: list[str]) -> bool:
    positions = [text.find(anchor) for anchor in anchors]
    return all(pos >= 0 for pos in positions) and positions == sorted(positions)


def audit(
    path: Path,
    ref_heading: str,
    prohibited: list[str],
    model_terms: list[str],
    introduction_heading: str,
    next_heading: str,
    introduction_anchors: list[str],
) -> dict:
    text = path.read_text(encoding="utf-8")
    body, refs = text.split(ref_heading, 1)
    introduction = body.split(introduction_heading, 1)[1].split(next_heading, 1)[0]
    ref_numbers = [int(x) for x in re.findall(r"(?m)^(\d+)\.\s", refs)]
    unnumbered_reference_lines = [
        line for line in refs.splitlines()
        if line.strip() and not re.match(r"^\d+\.\s", line)
    ]
    cited = citations(body)
    introduction_citation_tokens = CITATION_RE.findall(introduction)
    grouped_introduction_citations = [
        token for token in introduction_citation_tokens if not token.strip().isdigit()
    ]
    return {
        "path": str(path.relative_to(ROOT)),
        "sha256": sha256(path),
        "characters": len(text),
        "body_whitespace_tokens": len(body.split()),
        "h2_sections": re.findall(r"(?m)^##\s+(.+)$", text),
        "missing_locked_values": [x for x in EXPECTED_LOCKED if x not in body],
        "missing_provenance_terms": [x for x in EXPECTED_PROVENANCE if x not in body],
        "missing_model_terms": [x for x in model_terms if x not in body],
        "introduction_sequence_present": ordered(introduction, introduction_anchors),
        "introduction_cited_numbers": citations(introduction),
        "grouped_introduction_citations": grouped_introduction_citations,
        "cited_numbers": cited,
        "all_references_cited": cited == list(range(1, 21)),
        "reference_numbers_sequential": ref_numbers == list(range(1, 21)),
        "unnumbered_reference_lines": unnumbered_reference_lines,
        "doi_set": sorted(dois(refs)),
        "prohibited_hits": [phrase for phrase in prohibited if phrase.lower() in body.lower()],
        "gap_markers": sorted(set(re.findall(r"\b(?:TODO|TBD|RESULT GAP|MATERIAL GAP)\b", text, re.I))),
    }


def main() -> int:
    en = audit(
        BASE / "English.md",
        "## References",
        [
            "interim", "teacher", "supervisor", "stage-deliverable", "draft status",
            "proved that", "periodontitis-specific oral micropeptides",
            "experimentally validated binding",
        ],
        EXPECTED_MODELS,
        "## Introduction",
        "## Materials and methods",
        ["Alzheimer’s disease", "*Porphyromonas gingivalis*", "Several non-exclusive mechanisms", "mechanistic gap", "We therefore"],
    )
    zh = audit(
        BASE / "Chinese.md",
        "## 参考文献",
        [
            "阶段性", "导师", "提交包", "简稿", "证明这些候选", "牙周炎特异性微肽",
            "经实验验证的结合",
        ],
        EXPECTED_MODELS_ZH,
        "## 引言",
        "## 材料与方法",
        ["阿尔茨海默病", "牙龈卟啉单胞菌", "多条互不排斥的路径", "机制空白", "本研究实施"],
    )
    expected_files = {"English.md", "English.docx", "Chinese.md", "Chinese.docx", "README.md"}
    observed_files = {path.name for path in BASE.iterdir() if path.is_file()}
    old_paths = [
        ROOT / "manuscript" / "interim_teacher",
        BASE / "interim_teacher_en.md",
        BASE / "interim_teacher_en.docx",
        BASE / "interim_teacher_zh.md",
        BASE / "interim_teacher_zh.docx",
    ]
    checks = {
        "plain_separate_filenames_present": expected_files <= observed_files,
        "old_teacher_filenames_absent": not any(path.exists() for path in old_paths),
        "english_has_seven_h2_sections": len(en["h2_sections"]) == 7,
        "chinese_has_seven_h2_sections": len(zh["h2_sections"]) == 7,
        "locked_values_present_bilingual": not en["missing_locked_values"] and not zh["missing_locked_values"],
        "verified_provenance_present_bilingual": not en["missing_provenance_terms"] and not zh["missing_provenance_terms"],
        "prediction_algorithms_present_bilingual": not en["missing_model_terms"] and not zh["missing_model_terms"],
        "introduction_flow_present_bilingual": en["introduction_sequence_present"] and zh["introduction_sequence_present"],
        "introduction_uses_single_references_1_to_10_bilingual": (
            en["introduction_cited_numbers"] == list(range(1, 11))
            and zh["introduction_cited_numbers"] == list(range(1, 11))
            and not en["grouped_introduction_citations"]
            and not zh["grouped_introduction_citations"]
        ),
        "references_1_to_20_sequential_bilingual": en["reference_numbers_sequential"] and zh["reference_numbers_sequential"],
        "references_1_to_20_cited_bilingual": en["all_references_cited"] and zh["all_references_cited"],
        "reference_entries_are_one_numbered_record_per_line": (
            not en["unnumbered_reference_lines"] and not zh["unnumbered_reference_lines"]
        ),
        "twenty_doi_inventory_parity": len(en["doi_set"]) == 20 and en["doi_set"] == zh["doi_set"],
        "administrative_and_prohibited_assertions_absent": not en["prohibited_hits"] and not zh["prohibited_hits"],
        "gap_markers_absent": not en["gap_markers"] and not zh["gap_markers"],
        "unsupported_24_26_296_claim_explicitly_rejected_bilingual": (
            "those quantities were not used" in (BASE / "English.md").read_text(encoding="utf-8")
            and "本研究不使用这些数量" in (BASE / "Chinese.md").read_text(encoding="utf-8")
        ),
    }
    report = {
        "schema": "local.concise_package_audit.v3",
        "version": "3.3.0",
        "english": en,
        "chinese": zh,
        "checks": checks,
        "verdict": "PASS" if all(checks.values()) else "FAIL",
        "boundary": (
            "This audit checks filenames, bilingual content parity, accession wording, model-method descriptions, "
            "locked aggregate values and references. It does not reproduce screening, model inference or docking."
        ),
    }
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(OUT)
    return 0 if report["verdict"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
