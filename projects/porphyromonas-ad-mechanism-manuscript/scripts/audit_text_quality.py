#!/usr/bin/env python3
"""Dependency-free mechanical and claim-boundary lint for active language manuscripts."""
from __future__ import annotations

import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
REPORTS = ROOT / "quality_reports"
CONFIG = {
    "en": {
        "path": ROOT / "manuscript" / "manuscript_en.md",
        "ref_heading": "## References",
        "required": ["source-reported", "not independently reproduced", "FLLHTTR", "PDB 4EY6"],
        "prohibited": [
            "identified periodontitis-specific oral micropeptides",
            "proved that the candidates",
            "demonstrated that the candidates bind",
            "experimentally validated candidates",
            "docking free energies",
        ],
    },
    "zh": {
        "path": ROOT / "manuscript" / "manuscript_zh.md",
        "ref_heading": "## 参考文献",
        "required": ["来源报告", "未被独立复现", "FLLHTTR", "PDB 4EY6"],
        "prohibited": [
            "鉴定出牙周炎特异性微肽",
            "证明这些候选肽",
            "证实这些候选与AChE结合",
            "经实验验证的候选",
            "对接自由能",
        ],
    },
}
PLACEHOLDER = re.compile(r"\b(?:TODO|TBD|RESULT GAP|MATERIAL GAP)\b", re.I)
IMAGE = re.compile(r"!\[[^]]*\]\(([^)]+)\)")


def heading_jumps(text: str) -> list[dict]:
    issues = []
    previous = None
    for lineno, line in enumerate(text.splitlines(), 1):
        m = re.match(r"^(#{1,6})\s+", line)
        if not m:
            continue
        level = len(m.group(1))
        if previous is not None and level > previous + 1:
            issues.append({"line": lineno, "from": previous, "to": level})
        previous = level
    return issues


def table_width_issues(text: str) -> list[dict]:
    issues = []
    expected = None
    in_table = False
    for lineno, line in enumerate(text.splitlines(), 1):
        if not line.startswith("|"):
            expected = None
            in_table = False
            continue
        width = len(line.strip().strip("|").split("|"))
        if not in_table:
            expected = width
            in_table = True
        elif width != expected:
            issues.append({"line": lineno, "expected_columns": expected, "observed_columns": width})
    return issues


def main() -> int:
    REPORTS.mkdir(parents=True, exist_ok=True)
    all_pass = True
    for lang, cfg in CONFIG.items():
        path: Path = cfg["path"]
        text = path.read_text(encoding="utf-8")
        body = text.split(cfg["ref_heading"], 1)[0]
        images = IMAGE.findall(body)
        missing_images = [p for p in images if not (path.parent / p).exists()]
        mechanical = {
            "schema": "local.mechanical_text_audit.v1",
            "source": str(path.relative_to(ROOT)),
            "characters": len(text),
            "lines": len(text.splitlines()),
            "replacement_character_count": text.count("�"),
            "placeholder_hits": sorted(set(PLACEHOLDER.findall(text))),
            "trailing_whitespace_lines": [i for i, line in enumerate(text.splitlines(), 1) if line.rstrip() != line],
            "heading_level_jumps": heading_jumps(text),
            "table_width_issues": table_width_issues(text),
            "image_references": images,
            "missing_images": missing_images,
        }
        mechanical["verdict"] = "PASS" if (
            mechanical["replacement_character_count"] == 0
            and not mechanical["placeholder_hits"]
            and not mechanical["heading_level_jumps"]
            and not mechanical["table_width_issues"]
            and not missing_images
        ) else "FAIL"
        claim = {
            "schema": "local.draft_claim_lint.v1",
            "source": str(path.relative_to(ROOT)),
            "mode": "final",
            "required_boundary_phrases_present": {p: p in body for p in cfg["required"]},
            "prohibited_assertion_hits": [p for p in cfg["prohibited"] if p.lower() in body.lower()],
            "reference_entries": len(re.findall(r"(?m)^\d+\.\s", text.split(cfg["ref_heading"], 1)[1])),
            "top_level_sections": len(re.findall(r"(?m)^##\s+", text)),
        }
        claim["verdict"] = "PASS" if (
            all(claim["required_boundary_phrases_present"].values())
            and not claim["prohibited_assertion_hits"]
            and claim["reference_entries"] == 53
            and claim["top_level_sections"] == 8
        ) else "FAIL"
        for stem, report in ((f"mechanical_check_{lang}", mechanical), (f"draft_lint_{lang}", claim)):
            (REPORTS / f"{stem}.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            lines = [f"{stem}: {report['verdict']}"]
            for key, value in report.items():
                if key not in {"schema", "source", "verdict"}:
                    lines.append(f"- {key}: {value}")
            (REPORTS / f"{stem}.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
        all_pass &= mechanical["verdict"] == claim["verdict"] == "PASS"
    print(f"text_quality_pass={all_pass}")
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
