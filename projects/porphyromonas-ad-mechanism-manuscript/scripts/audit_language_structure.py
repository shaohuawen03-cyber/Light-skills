#!/usr/bin/env python3
"""Audit top-level bilingual structure, in-text reference coverage, and placeholders."""
from __future__ import annotations

import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "quality_reports" / "language_structure_audit.json"
CONFIG = {
    "en": (ROOT / "manuscript" / "manuscript_en.md", "## References"),
    "zh": (ROOT / "manuscript" / "manuscript_zh.md", "## 参考文献"),
}
PLACEHOLDER_RE = re.compile(r"\b(?:TODO|TBD|RESULT GAP|MATERIAL GAP)\b", re.I)
CITATION_RE = re.compile(r"\[([0-9,;\-–—\s]+)\]")


def citation_numbers(body: str) -> list[int]:
    found: set[int] = set()
    for match in CITATION_RE.finditer(body):
        for part in re.split(r"[,;]", match.group(1)):
            part = part.strip()
            if not part:
                continue
            span = re.fullmatch(r"(\d+)\s*[-–—]\s*(\d+)", part)
            if span:
                start, end = map(int, span.groups())
                found.update(range(min(start, end), max(start, end) + 1))
            elif part.isdigit():
                found.add(int(part))
    return sorted(found)


def audit(path: Path, reference_heading: str) -> dict:
    text = path.read_text(encoding="utf-8")
    body = text.split(reference_heading, 1)[0]
    sections = re.findall(r"(?m)^##\s+(.+?)\s*$", text)
    cited = citation_numbers(body)
    return {
        "path": str(path.relative_to(ROOT)),
        "characters": len(text),
        "whitespace_delimited_tokens": len(text.split()),
        "h2_sections": sections,
        "h2_section_count": len(sections),
        "cited_reference_numbers_before_reference_list": cited,
        "all_1_to_25_cited_before_reference_list": cited == list(range(1, 26)),
        "placeholder_count": len(PLACEHOLDER_RE.findall(text)),
    }


def main() -> int:
    en = audit(*CONFIG["en"])
    zh = audit(*CONFIG["zh"])
    section_ok = en["h2_section_count"] == zh["h2_section_count"] == 8
    report = {
        "schema": "local.language_structure_audit.v2",
        "en": en,
        "zh": zh,
        "parallel_h2_section_count": section_ok,
        "all_references_cited_in_both_bodies": (
            en["all_1_to_25_cited_before_reference_list"]
            and zh["all_1_to_25_cited_before_reference_list"]
        ),
        "placeholders_absent": en["placeholder_count"] == zh["placeholder_count"] == 0,
    }
    report["verdict"] = "PASS" if all(
        report[key]
        for key in ("parallel_h2_section_count", "all_references_cited_in_both_bodies", "placeholders_absent")
    ) else "FAIL"
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(OUT)
    return 0 if report["verdict"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
