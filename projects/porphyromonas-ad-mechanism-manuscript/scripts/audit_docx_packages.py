#!/usr/bin/env python3
"""Perform deterministic structural audits of generated OOXML DOCX packages."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path, PurePosixPath
import xml.etree.ElementTree as ET
import zipfile

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "quality_reports" / "docx_package_audit.json"
PACKAGES = {
    "manuscript/manuscript_bilingual.docx": {
        "minimum_paragraphs": 300,
        "minimum_tables": 4,
        "minimum_drawings": 4,
        "expected_media": 2,
        "tokens": [
            "Evidence-Bounded Multi-Model Prioritization",
            "牙周炎队列口腔微肽的证据约束型多模型优先排序",
            "11,269,961",
            "3,518",
            "References / 参考文献",
        ],
    },
    "manuscript/supplementary_tables_bilingual.docx": {
        "minimum_paragraphs": 250,
        "minimum_tables": 3,
        "minimum_drawings": 0,
        "expected_media": 0,
        "tokens": [
            "Supplementary Tables / 补充表",
            "Supplementary Table S1 / 补充表 S1",
            "Supplementary Table S3 / 补充表 S3",
            "computational accounting units",
        ],
    },
}
W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
REL_NS = "http://schemas.openxmlformats.org/package/2006/relationships"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relationship_errors(names: set[str], member: str, root: ET.Element) -> list[str]:
    errors = []
    # A relationship part named a/_rels/b.xml.rels resolves relative to a/b.xml.
    rel_path = PurePosixPath(member)
    if member == "_rels/.rels":
        base = PurePosixPath("")
    else:
        source_dir = rel_path.parent.parent
        source_name = rel_path.name.removesuffix(".rels")
        base = source_dir / source_name
        base = base.parent
    for rel in root.findall(f"{{{REL_NS}}}Relationship"):
        if rel.get("TargetMode") == "External":
            continue
        target = rel.get("Target", "")
        resolved = str(PurePosixPath(base, target))
        # Normalize only the simple relative targets used by these generated packages.
        parts = []
        for part in PurePosixPath(resolved).parts:
            if part == "..":
                if parts:
                    parts.pop()
            elif part not in (".", ""):
                parts.append(part)
        normalized = "/".join(parts)
        if normalized not in names:
            errors.append(f"{member}: missing target {target} -> {normalized}")
    return errors


def audit(path: Path, spec: dict) -> dict:
    result = {
        "path": str(path.relative_to(ROOT)),
        "size_bytes": path.stat().st_size,
        "sha256": sha256(path),
    }
    xml_errors: list[str] = []
    rel_errors: list[str] = []
    with zipfile.ZipFile(path) as zf:
        names = set(zf.namelist())
        result["zip_crc_error"] = zf.testzip()
        roots = {}
        for member in sorted(names):
            if member.endswith((".xml", ".rels")):
                try:
                    roots[member] = ET.fromstring(zf.read(member))
                except ET.ParseError as exc:
                    xml_errors.append(f"{member}: {exc}")
        for member, root in roots.items():
            if member.endswith(".rels"):
                rel_errors.extend(relationship_errors(names, member, root))
        doc_root = roots.get("word/document.xml")
        if doc_root is None:
            text = ""
            paragraphs = tables = drawings = 0
        else:
            text = "".join(node.text or "" for node in doc_root.iter(f"{{{W}}}t"))
            paragraphs = sum(1 for _ in doc_root.iter(f"{{{W}}}p"))
            tables = sum(1 for _ in doc_root.iter(f"{{{W}}}tbl"))
            drawings = sum(1 for _ in doc_root.iter(f"{{{W}}}drawing"))
        media = sorted(name for name in names if name.startswith("word/media/") and not name.endswith("/"))

    missing_tokens = [token for token in spec["tokens"] if token not in text]
    structural_checks = {
        "crc_ok": result["zip_crc_error"] is None,
        "all_xml_parses": not xml_errors,
        "all_internal_relationship_targets_exist": not rel_errors,
        "paragraph_minimum_met": paragraphs >= spec["minimum_paragraphs"],
        "table_minimum_met": tables >= spec["minimum_tables"],
        "drawing_minimum_met": drawings >= spec["minimum_drawings"],
        "media_count_matches": len(media) == spec["expected_media"],
        "expected_tokens_present": not missing_tokens,
    }
    result.update({
        "xml_parse_errors": xml_errors,
        "relationship_errors": rel_errors,
        "paragraphs": paragraphs,
        "tables": tables,
        "drawings": drawings,
        "embedded_media": media,
        "missing_expected_tokens": missing_tokens,
        "document_text_characters": len(text),
        "checks": structural_checks,
        "verdict": "PASS" if all(structural_checks.values()) else "FAIL",
    })
    return result


def main() -> int:
    records = {name: audit(ROOT / name, spec) for name, spec in PACKAGES.items()}
    verdict = "PASS" if all(item["verdict"] == "PASS" for item in records.values()) else "FAIL"
    report = {
        "schema": "local.docx_package_audit.v2",
        "rendering_status": (
            "UNAVAILABLE: no Office/LibreOffice/PDF renderer is installed; package and content checks are structural, not visual."
        ),
        "packages": records,
        "verdict": verdict,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(OUT)
    return 0 if verdict == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
