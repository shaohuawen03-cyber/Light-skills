#!/usr/bin/env python3
"""Audit the four clean, figure-free SCI manuscript deliverables."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re
import xml.etree.ElementTree as ET
import zipfile

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "quality_reports" / "submission_manuscript_audit.json"
BIB = ROOT / "references" / "references.bib"
W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
LOCKED = [
    "11,269,961", "11,721,988", "31,510", "33,786", "3,518", "3,299",
    "923", "111", "15", "12", "8", "FLLHTTR", "HVLLLRQCA", "−9.60", "−8.25",
]
COMMON_ADMIN_PATTERNS = [
    r"\bTier\s+[A-D]\b", r"SHA-?256", r"\bcommit\s+[0-9a-f]{7,40}\b",
    r"acceptance decision", r"evidence tier", r"source-reported",
    r"principal-source", r"principal record", r"external source record",
    r"evidence ladder", r"version-control administration", r"workflow governance",
    r"\bDeclarations\b", r"Data availability", r"Code availability",
    r"Generative artificial intelligence use",
]
COMMON_ADMIN_PATTERNS_ZH = [
    r"[A-D]层", r"证据层级", r"证据等级", r"文件哈希", r"提交[`：:]?[0-9a-f]{7,40}",
    r"接纳决策", r"来源报告", r"主要记录", r"外部来源记录", r"证据阶梯",
    r"工作流治理", r"^## 声明$", r"数据可用性", r"代码可用性", r"生成式人工智能使用",
]
PROHIBITED_COUNTS_EN = [
    "11 orally healthy controls", "11 patients with periodontitis", "22 participants",
    "66 specimens", "118 sequence-assembly analyses", "24 healthy", "24 controls",
    "26 periodontitis", "26 patients", "296 high-quality",
]
PROHIBITED_COUNTS_ZH = [
    "11名口腔健康对照", "11名牙周炎患者", "22名参与者", "66份标本",
    "118项序列组装分析", "24名健康", "26名牙周炎", "296个高质量",
]
SPECS = {
    "full/English": {
        "md": "manuscript/full/English.md", "docx": "manuscript/full/English.docx",
        "start": "Abstract", "abstract": "## Abstract", "intro": "## 1. Introduction",
        "methods": "## 2. Materials and Methods", "results": "## 3. Results",
        "discussion": "## 4. Discussion", "conclusion": "## 5. Conclusions",
        "references": "## References", "core_title": "English", "tables": 4, "refs": 55,
        "patterns": COMMON_ADMIN_PATTERNS, "counts": PROHIBITED_COUNTS_EN,
    },
    "full/Chinese": {
        "md": "manuscript/full/Chinese.md", "docx": "manuscript/full/Chinese.docx",
        "start": "摘要", "abstract": "## 摘要", "intro": "## 1. 引言",
        "methods": "## 2. 材料与方法", "results": "## 3. 结果",
        "discussion": "## 4. 讨论", "conclusion": "## 5. 结论",
        "references": "## 参考文献", "core_title": "Chinese", "tables": 4, "refs": 55,
        "patterns": COMMON_ADMIN_PATTERNS_ZH, "counts": PROHIBITED_COUNTS_ZH,
    },
    "concise/English": {
        "md": "manuscript/concise/English.md", "docx": "manuscript/concise/English.docx",
        "start": "Abstract", "abstract": "## Abstract", "intro": "## Introduction",
        "methods": "## Materials and Methods", "results": "## Results",
        "discussion": "## Discussion", "conclusion": "## Conclusion",
        "references": "## References", "core_title": "English", "tables": 2, "refs": 22,
        "patterns": COMMON_ADMIN_PATTERNS, "counts": PROHIBITED_COUNTS_EN,
    },
    "concise/Chinese": {
        "md": "manuscript/concise/Chinese.md", "docx": "manuscript/concise/Chinese.docx",
        "start": "摘要", "abstract": "## 摘要", "intro": "## 引言",
        "methods": "## 材料与方法", "results": "## 结果",
        "discussion": "## 讨论", "conclusion": "## 结论",
        "references": "## 参考文献", "core_title": "Chinese", "tables": 2, "refs": 22,
        "patterns": COMMON_ADMIN_PATTERNS_ZH, "counts": PROHIBITED_COUNTS_ZH,
    },
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def doi_set(text: str) -> set[str]:
    return {
        value.rstrip(".,;:)]}").lower()
        for value in re.findall(r"10\.\d{4,9}/[-._;()/:A-Z0-9]+", text, re.I)
    }


def bib_keys(text: str) -> set[str]:
    return set(re.findall(r"(?m)^@[A-Za-z]+\{([^,]+),", text))


def bib_doi_key_map(text: str) -> dict[str, str]:
    mapping = {}
    for entry in re.finditer(r"(?ms)^@[A-Za-z]+\{([^,]+),(.*?)(?=^@[A-Za-z]+\{|\Z)", text):
        key, fields = entry.groups()
        doi = re.search(r"(?mi)^\s*doi\s*=\s*[\{\"]([^\}\"]+)", fields)
        if doi:
            mapping[doi.group(1).strip().lower().rstrip(".")] = key
    return mapping


def table_checks(table: ET.Element) -> dict:
    borders = table.find(f"{W}tblPr/{W}tblBorders")
    values = {}
    for name in ("top", "left", "bottom", "right", "insideH", "insideV"):
        node = borders.find(W + name) if borders is not None else None
        values[name] = node.get(W + "val") if node is not None else None
    rows = table.findall(W + "tr")
    header_cells = rows[0].findall(W + "tc") if rows else []
    header_bottom = []
    for cell in header_cells:
        node = cell.find(f"{W}tcPr/{W}tcBorders/{W}bottom")
        header_bottom.append(node is not None and node.get(W + "val") == "single")
    body_cell_borders = []
    for row in rows[1:]:
        for cell in row.findall(W + "tc"):
            body_cell_borders.append(cell.find(f"{W}tcPr/{W}tcBorders") is not None)
    return {
        "table_border_values": values,
        "top_and_bottom_rules_present": values["top"] == "single" and values["bottom"] == "single",
        "vertical_and_body_rules_absent": all(values[name] == "nil" for name in ("left", "right", "insideH", "insideV")),
        "header_bottom_rule_present_in_every_cell": bool(header_bottom) and all(header_bottom),
        "body_cells_have_no_overriding_borders": not any(body_cell_borders),
        "shading_absent": table.find(".//" + W + "shd") is None,
    }


def audit_one(label: str, spec: dict, known_bib_keys: set[str], known_dois: set[str], doi_to_key: dict[str, str]) -> dict:
    md_path = ROOT / spec["md"]
    docx_path = ROOT / spec["docx"]
    md = md_path.read_text(encoding="utf-8")
    body, references = md.split(spec["references"], 1)
    h2 = re.findall(r"(?m)^##\s+.+$", md)
    expected_h2 = [
        spec["abstract"], spec["intro"], spec["methods"], spec["results"],
        spec["discussion"], spec["conclusion"], spec["references"],
    ]
    cited = re.findall(r"@([A-Za-z0-9_.:+-]+)", body)
    cited_set = set(cited)
    intro = body.split(spec["intro"], 1)[1].split(spec["methods"], 1)[0]
    intro_clusters = re.findall(r"\[(@[^\]]+)\]", intro)
    grouped_intro = [cluster for cluster in intro_clusters if len(re.findall(r"@[A-Za-z0-9_.:+-]+", cluster)) != 1]
    ref_numbers = [int(x) for x in re.findall(r"(?m)^(\d+)\.\s", references)]
    ref_dois = doi_set(references)
    ref_dois_in_order = [
        match.group(1).rstrip(".,;:)]}").lower()
        for match in re.finditer(r"(?m)^\d+\.\s.*?doi:(10\.\d{4,9}/\S+)", references, re.I)
    ]
    reference_keys_in_order = [doi_to_key[doi] for doi in ref_dois_in_order]
    citation_keys_in_first_appearance_order = list(dict.fromkeys(cited))
    admin_hits = [
        pattern for pattern in spec["patterns"]
        if re.search(pattern, body, flags=re.I | re.M)
    ]
    count_hits = [value for value in spec["counts"] if value.lower() in body.lower()]
    results = body.split(spec["results"], 1)[1].split(spec["discussion"], 1)[0]

    with zipfile.ZipFile(docx_path) as archive:
        names = set(archive.namelist())
        crc = archive.testzip()
        doc = ET.fromstring(archive.read("word/document.xml"))
        doc_text = "".join(node.text or "" for node in doc.iter(W + "t"))
        document_xml = archive.read("word/document.xml").decode("utf-8", errors="replace")
        all_xml = "\n".join(
            archive.read(name).decode("utf-8", errors="replace")
            for name in names if name.endswith((".xml", ".rels"))
        )
        media = sorted(name for name in names if name.startswith("word/media/") and not name.endswith("/"))
        header_footer = sorted(name for name in names if name.startswith(("word/header", "word/footer")))
        comments = sorted(name for name in names if name.startswith(("word/comments", "word/people")))
        tables = list(doc.iter(W + "tbl"))
        table_audits = [table_checks(table) for table in tables]
        core = ET.fromstring(archive.read("docProps/core.xml"))
        core_text = "".join(core.itertext())
        drawings = sum(1 for _ in doc.iter(W + "drawing"))
        citation_fields = document_xml.count("ADDIN ZOTERO_ITEM CSL_CITATION")

    checks = {
        "markdown_starts_with_abstract_and_has_no_h1": md.lstrip().startswith(spec["abstract"]) and not re.search(r"(?m)^#\s+", md),
        "seven_article_sections_in_order": h2 == expected_h2,
        "conclusion_proceeds_directly_to_references": h2[-2:] == [spec["conclusion"], spec["references"]],
        "declarations_and_administrative_prose_absent": not admin_hits,
        "specific_participant_specimen_mag_counts_absent": not count_hits,
        "markdown_has_no_figure_markup": "![" not in body and not re.search(r"(?mi)^\*\*(?:Figure|图)\s*\d", body),
        "all_locked_scientific_values_present": all(value in body for value in LOCKED),
        "pandoc_citation_keys_present": bool(cited),
        "all_citation_keys_exist_in_bibtex": cited_set <= known_bib_keys,
        "introduction_uses_one_reference_per_citation": not grouped_intro,
        "reference_numbers_are_sequential": ref_numbers == list(range(1, spec["refs"] + 1)),
        "numbered_references_follow_first_citation_appearance": reference_keys_in_order == citation_keys_in_first_appearance_order,
        "reference_dois_are_in_bibtex": ref_dois <= known_dois,
        "reference_count_matches_variant": len(ref_dois) == spec["refs"],
        "prospective_md_method_present": bool(re.search(r"100[- ]ns", body)) and ("GROMACS" in body),
        "no_md_result_in_results": not re.search(r"(?i)molecular[- ]dynamics result|分子动力学结果|MD结果", results),
        "docx_zip_crc_ok": crc is None,
        "docx_visible_content_starts_with_abstract": doc_text.startswith(spec["start"]),
        "docx_neutral_core_title": spec["core_title"] in core_text,
        "docx_header_footer_page_number_and_comments_absent": (
            not header_footer and not comments and 'w:instr="PAGE"' not in all_xml
        ),
        "docx_is_figure_free": not media and drawings == 0 and "/relationships/image" not in all_xml,
        "docx_table_count_matches_markdown": len(tables) == spec["tables"],
        "every_docx_table_is_three_line": bool(table_audits) and all(all(
            audit[name] for name in (
                "top_and_bottom_rules_present", "vertical_and_body_rules_absent",
                "header_bottom_rule_present_in_every_cell", "body_cells_have_no_overriding_borders",
                "shading_absent",
            )
        ) for audit in table_audits),
        "docx_contains_rendered_numbers_not_citekeys": "@" not in doc_text and "[1]" in doc_text,
        "docx_does_not_claim_unverified_zotero_live_fields": citation_fields == 0,
        "docx_locked_values_present": all(value in doc_text for value in LOCKED),
    }
    return {
        "label": label,
        "markdown": spec["md"],
        "docx": spec["docx"],
        "markdown_sha256": sha256(md_path),
        "docx_sha256": sha256(docx_path),
        "cited_key_count": len(cited_set),
        "reference_count": len(ref_numbers),
        "reference_doi_count": len(ref_dois),
        "administrative_pattern_hits": admin_hits,
        "prohibited_count_hits": count_hits,
        "grouped_introduction_citations": grouped_intro,
        "unknown_citation_keys": sorted(cited_set - known_bib_keys),
        "unknown_reference_dois": sorted(ref_dois - known_dois),
        "citation_keys_in_first_appearance_order": citation_keys_in_first_appearance_order,
        "reference_keys_in_number_order": reference_keys_in_order,
        "embedded_media": media,
        "drawings": drawings,
        "zotero_live_field_count": citation_fields,
        "citation_mode": "static numbered cache generated from Pandoc citekeys; not Zotero-live",
        "table_audits": table_audits,
        "checks": checks,
        "verdict": "PASS" if all(checks.values()) else "FAIL",
    }


def main() -> int:
    bib_text = BIB.read_text(encoding="utf-8")
    known_keys = bib_keys(bib_text)
    known_dois = doi_set(bib_text)
    doi_to_key = bib_doi_key_map(bib_text)
    records = {
        label: audit_one(label, spec, known_keys, known_dois, doi_to_key)
        for label, spec in SPECS.items()
    }
    checks = {
        "bibtex_has_55_unique_keys_and_dois": len(known_keys) == 55 and len(known_dois) == 55,
        "all_four_manuscripts_pass": all(record["verdict"] == "PASS" for record in records.values()),
        "full_reference_parity": (
            records["full/English"]["reference_doi_count"]
            == records["full/Chinese"]["reference_doi_count"] == 55
        ),
        "concise_reference_parity": (
            records["concise/English"]["reference_doi_count"]
            == records["concise/Chinese"]["reference_doi_count"] == 22
        ),
        "all_delivered_docx_are_figure_free": all(not record["embedded_media"] for record in records.values()),
        "all_delivered_tables_are_three_line": all(record["checks"]["every_docx_table_is_three_line"] for record in records.values()),
    }
    report = {
        "schema": "local.submission_manuscript_audit.v1",
        "scope": "Full and concise English/Chinese clean manuscripts.",
        "records": records,
        "package_checks": checks,
        "zotero_acceptance_state": "setup gate",
        "zotero_note": (
            "Sources use real BibTeX citation keys and static DOCX caches are automatically numbered. "
            "No ADDIN ZOTERO_ITEM fields are claimed; desktop Better BibTeX/Pandoc and Word/Zotero refresh remain required."
        ),
        "verdict": "PASS" if all(checks.values()) else "FAIL",
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(OUT)
    return 0 if report["verdict"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
