#!/usr/bin/env python3
"""Produce journal-neutral approximate English manuscript word counts."""
from __future__ import annotations

import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "manuscript" / "manuscript_en.md"
OUT = ROOT / "quality_reports" / "manuscript_word_count.json"
# Treat alphabetic compounds and formatted numbers as one token. This is an estimate,
# not a replacement for the target journal's portal or Microsoft Word count.
TOKEN_RE = re.compile(
    r"[^\W\d_]+(?:[-–—’'][^\W\d_]+)*|"
    r"\d+(?:[,.]\d+)*(?:%|[A-Za-z]+)?|"
    r"[A-Za-z]*\d+[A-Za-z0-9]*"
)
IMAGE_RE = re.compile(r"!\[[^]]*\]\([^)]*\)")


def count(text: str) -> int:
    return len(TOKEN_RE.findall(IMAGE_RE.sub("", text)))


def main() -> int:
    text = SOURCE.read_text(encoding="utf-8")
    abstract = text.split("## Abstract", 1)[1].split("**Keywords:**", 1)[0]
    main_with_declarations = text.split("## 1. Introduction", 1)[1].split("## References", 1)[0]
    main_without_declarations = text.split("## 1. Introduction", 1)[1].split("## Declarations", 1)[0]
    report = {
        "schema": "local.manuscript_word_count.v1",
        "source": "manuscript/manuscript_en.md",
        "structured_abstract_excluding_keywords": count(abstract),
        "main_text_introduction_through_conclusions": count(main_without_declarations),
        "main_text_including_declarations_excluding_references": count(main_with_declarations),
        "counting_boundary": (
            "Journal-neutral regex estimate: alphabetic compounds and formatted numbers count as one token; "
            "Markdown image declarations are excluded. Recount after target-journal formatting in Word and the submission portal."
        ),
        "verdict": "INFORMATIONAL",
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(OUT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
