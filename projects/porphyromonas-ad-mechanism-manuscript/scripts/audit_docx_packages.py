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
        "minimum_paragraphs": 500,
        "minimum_tables": 8,
        "minimum_drawings": 6,
        "expected_media": 3,
        "tokens": [
            "Provenance-Aware Multi-Model Prioritization",
            "基于来源边界的牙周炎队列口腔微肽多模型优选",
            "11,269,961",
            "3,518",
            "FLLHTTR",
            "−9.60",
            "References / 参考文献",
        ],
    },
    "manuscript/supplementary_tables_bilingual.docx": {
        "minimum_paragraphs": 350,
        "minimum_tables": 6,
        "minimum_drawings": 0,
        "expected_media": 0,
        "tokens": [
            "Supplementary Tables / 补充表",
            "Supplementary Table S1 / 补充表 S1",
            "Supplementary Table S6 / 补充表 S6",
            "FLLHTTR",
            "computational accounting units",
        ],
    },
    "manuscript/concise/English.docx": {
        "minimum_paragraphs": 140,
        "minimum_tables": 2,
        "minimum_drawings": 1,
        "expected_media": 1,
        "clean_manuscript": True,
        "expected_core_timestamp": "2026-08-14T00:00:00Z",
        "tokens": [
            "Aggregate Prioritization of Oral Micropeptides at the Periodontitis–Alzheimer’s Disease Interface",
            "11 orally healthy controls and 11 patients with periodontitis",
            "metaSPAdes v3.15.3",
            "six-layer convolutional neural network",
            "Extra Trees classifiers",
            "FLLHTTR",
            "−9.60",
            "References",
        ],
    },
    "manuscript/concise/Chinese.docx": {
        "minimum_paragraphs": 140,
        "minimum_tables": 2,
        "minimum_drawings": 1,
        "expected_media": 1,
        "clean_manuscript": True,
        "expected_core_timestamp": "2026-08-14T00:00:00Z",
        "tokens": [
            "牙周炎—阿尔茨海默病界面口腔微肽的汇总优选",
            "11名口腔健康对照和11名牙周炎患者",
            "metaSPAdes v3.15.3",
            "六层卷积神经网络",
            "Extra Trees",
            "FLLHTTR",
            "−9.60",
            "参考文献",
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
        zip_timestamps = sorted({info.date_time for info in zf.infolist()})
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
        xml_package_text = "\n".join(
            zf.read(name).decode("utf-8", errors="replace")
            for name in sorted(names)
            if name.endswith((".xml", ".rels"))
        )
        header_footer_members = sorted(
            name for name in names
            if name.startswith("word/header") or name.startswith("word/footer")
        )
        page_break_before_count = (
            sum(1 for _ in doc_root.iter(f"{{{W}}}pageBreakBefore"))
            if doc_root is not None else 0
        )

    missing_tokens = [token for token in spec["tokens"] if token not in text]
    clean_required = bool(spec.get("clean_manuscript"))
    administrative_tokens = [
        "Bilingual scientific-content draft", "Arena.ai drafting workflow",
        "interim", "teacher", "supervisor", "Draft Note",
    ]
    administrative_hits = [token for token in administrative_tokens if token.lower() in xml_package_text.lower()]
    clean_checks = {
        "header_footer_parts_absent": not header_footer_members,
        "header_footer_relationships_absent": (
            "/relationships/header" not in xml_package_text
            and "/relationships/footer" not in xml_package_text
        ),
        "page_field_absent": (
            '<w:fldSimple w:instr="PAGE"' not in xml_package_text
            and "<w:instrText" not in xml_package_text
        ),
        "automatic_section_page_breaks_absent": page_break_before_count == 0,
        "administrative_metadata_absent": not administrative_hits,
        "zip_member_timestamps_stable": zip_timestamps == [(1980, 1, 1, 0, 0, 0)],
        "core_timestamp_matches_release": (
            xml_package_text.count(spec.get("expected_core_timestamp", "__missing__")) == 2
        ),
    }
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
    if clean_required:
        structural_checks.update(clean_checks)
    result.update({
        "xml_parse_errors": xml_errors,
        "relationship_errors": rel_errors,
        "paragraphs": paragraphs,
        "tables": tables,
        "drawings": drawings,
        "embedded_media": media,
        "missing_expected_tokens": missing_tokens,
        "document_text_characters": len(text),
        "clean_manuscript_required": clean_required,
        "header_footer_members": header_footer_members,
        "page_break_before_count": page_break_before_count,
        "administrative_metadata_hits": administrative_hits,
        "zip_member_timestamps": zip_timestamps,
        "checks": structural_checks,
        "verdict": "PASS" if all(structural_checks.values()) else "FAIL",
    })
    return result


def main() -> int:
    records = {name: audit(ROOT / name, spec) for name, spec in PACKAGES.items()}
    verdict = "PASS" if all(item["verdict"] == "PASS" for item in records.values()) else "FAIL"
    report = {
        "schema": "local.docx_package_audit.v3",
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
