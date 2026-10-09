#!/usr/bin/env python3
"""Wrap existing numbered citations in Zotero Word fields. Visible text unchanged."""
from __future__ import annotations

import json
import re
import shutil
import uuid
import zipfile
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MD = ROOT / "manuscript" / "sci_submission" / "English.md"
BIB = ROOT / "references" / "references.bib"
SRC_DOCX = Path("/home/user/Light-skills/projects/English.docx")
BACKUP = Path("/home/user/Light-skills/projects/English_backup_pre-zotero.docx")
LIBRARY = Path("/home/user/Light-skills/projects/English_Zotero_library.json")
OUT_DOCX = Path("/home/user/Light-skills/projects/English.docx")

CITE_RE = re.compile(
    r"^\[(\d+(?:[–-]\d+)?(?:,\s*\d+(?:[–-]\d+)?)*)\]$"
)


def parse_bib(path: Path) -> dict[str, dict]:
    text = path.read_text(encoding="utf-8")
    entries = {}
    for m in re.finditer(
        r"(?ms)^@[A-Za-z]+\{([^,]+),(.*?)(?=^@[A-Za-z]+\{|\Z)", text
    ):
        key, fields = m.group(1).strip(), m.group(2)
        rec: dict[str, str] = {}
        for fm in re.finditer(
            r'(?ms)^\s*([A-Za-z]+)\s*=\s*\{(.*?)\}(?=\s*,?\s*^\s*[A-Za-z]+\s*=|\s*\}\s*\Z)',
            fields,
        ):
            rec[fm.group(1).lower()] = re.sub(r"\s+", " ", fm.group(2)).strip()
        if "doi" not in rec:
            dm = re.search(r'(?mi)^\s*doi\s*=\s*[\{\"]([^}\"\n]+)', fields)
            if dm:
                rec["doi"] = dm.group(1).strip().rstrip(".")
        entries[key] = rec
    return entries


def parse_authors(raw: str) -> list[dict]:
    if not raw:
        return []
    raw = raw.replace(" and others", "")
    people = re.split(r"\s+and\s+", raw)
    out = []
    for person in people:
        person = person.strip().strip("{}")
        if not person:
            continue
        if "," in person:
            family, given = [p.strip() for p in person.split(",", 1)]
        else:
            parts = person.split()
            family, given = parts[-1], " ".join(parts[:-1])
        family = re.sub(r"\{\\'([A-Za-z])\}", r"\1", family)
        given = re.sub(r"\{\\'([A-Za-z])\}", r"\1", given)
        out.append({"family": family, "given": given})
    return out


def to_csl(key: str, rec: dict) -> dict:
    item = {
        "id": key,
        "type": "article-journal",
        "title": rec.get("title", "").replace("{", "").replace("}", ""),
        "author": parse_authors(rec.get("author", "")),
    }
    if rec.get("year"):
        try:
            item["issued"] = {"date-parts": [[int(re.search(r"\d{4}", rec["year"]).group())]]}
        except Exception:
            pass
    if rec.get("journal"):
        item["container-title"] = rec["journal"].replace("{", "").replace("}", "")
    if rec.get("volume"):
        item["volume"] = rec["volume"]
    if rec.get("number"):
        item["issue"] = rec["number"]
    if rec.get("pages"):
        item["page"] = rec["pages"].replace("--", "-")
    if rec.get("doi"):
        item["DOI"] = rec["doi"].rstrip(".")
    return item


def number_to_key(md: str, bib: dict[str, dict]) -> dict[int, str]:
    head, refs = md.split("## References", 1)
    doi_to_key = {}
    for key, rec in bib.items():
        if rec.get("doi"):
            doi_to_key[rec["doi"].strip().lower().rstrip(".")] = key
    mapping = {}
    for m in re.finditer(r"(?m)^(\d+)\.\s+(.*)$", refs):
        n = int(m.group(1))
        line = m.group(2)
        d = re.search(r"doi:(10\.\d{4,9}/\S+)", line)
        doi = d.group(1).rstrip(".,;:)]}").lower() if d else None
        key = doi_to_key.get(doi) if doi else None
        if key is None:
            raise SystemExit(f"No BibTeX key for reference {n}: {line[:80]}")
        mapping[n] = key
    return mapping


def expand_cluster(inner: str) -> list[int]:
    nums: list[int] = []
    for part in inner.replace(" ", "").split(","):
        if re.search(r"[–-]", part):
            a, b = re.split(r"[–-]", part)
            nums.extend(range(int(a), int(b) + 1))
        else:
            nums.append(int(part))
    return nums


def field_xml(visible: str, items: list[dict]) -> str:
    payload = {
        "citationID": uuid.uuid4().hex[:8],
        "properties": {
            "formattedCitation": visible,
            "plainCitation": visible,
            "dontUpdate": False,
            "noteIndex": 0,
        },
        "citationItems": [
            {
                "id": item["id"],
                "uris": [f"http://zotero.org/users/local/import/items/{item['id']}"],
                "uri": [f"http://zotero.org/users/local/import/items/{item['id']}"],
                "itemData": item,
            }
            for item in items
        ],
        "schema": "https://github.com/citation-style-language/schema/raw/master/csl-citation.json",
    }
    raw = " ADDIN ZOTERO_ITEM CSL_CITATION " + json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
    instr = escape(raw, quote=False)
    chunks = [instr[i : i + 2000] for i in range(0, len(instr), 2000)]
    parts = ['<w:r><w:fldChar w:fldCharType="begin"/></w:r>']
    for i, chunk in enumerate(chunks):
        space = ' xml:space="preserve"' if i == 0 or chunk[:1].isspace() else ""
        parts.append(f'<w:r><w:instrText{space}>{chunk}</w:instrText></w:r>')
    parts.append('<w:r><w:fldChar w:fldCharType="separate"/></w:r>')
    parts.append(f"<w:r><w:t>{escape(visible)}</w:t></w:r>")
    parts.append('<w:r><w:fldChar w:fldCharType="end"/></w:r>')
    return "".join(parts)


def wrap_citations(xml: str, num_key: dict[int, str], csl: dict[str, dict]) -> tuple[str, int]:
    n_max = max(num_key)
    count = 0

    def repl(m: re.Match) -> str:
        nonlocal count
        visible = m.group(1)
        inner = visible[1:-1]
        if not CITE_RE.match(visible):
            return m.group(0)
        nums = expand_cluster(inner)
        if any(n < 1 or n > n_max or n not in num_key for n in nums):
            return m.group(0)
        items = [csl[num_key[n]] for n in nums]
        count += 1
        return field_xml(visible, items)

    pattern = re.compile(r"<w:r><w:t>(\[[^\[\]]+\])</w:t></w:r>")
    xml = pattern.sub(repl, xml)
    return xml, count


def add_bibl_and_pref(xml: str) -> str:
    pref = (
        '<w:p>'
        '<w:r><w:fldChar w:fldCharType="begin"/></w:r>'
        '<w:r><w:instrText xml:space="preserve">'
        " ADDIN ZOTERO_PREF "
        '{"citation_style":"http://www.zotero.org/styles/vancouver",'
        '"features":{"bibliography":true}}'
        "</w:instrText></w:r>"
        '<w:r><w:fldChar w:fldCharType="end"/></w:r>'
        "</w:p>"
    )
    xml = xml.replace("<w:body>", "<w:body>" + pref, 1)

    heading = (
        '<w:p><w:pPr><w:pStyle w:val="Heading2"/><w:keepNext/></w:pPr>'
        "<w:r><w:t>References</w:t></w:r></w:p>"
    )
    bibl_begin = (
        '<w:r><w:fldChar w:fldCharType="begin"/></w:r>'
        '<w:r><w:instrText xml:space="preserve">'
        ' ADDIN ZOTERO_BIBL {"uncited":[],"omitted":[],"custom":[]} CSL_BIBLIOGRAPHY'
        "</w:instrText></w:r>"
        '<w:r><w:fldChar w:fldCharType="separate"/></w:r>'
    )
    bibl_end = '<w:r><w:fldChar w:fldCharType="end"/></w:r>'
    idx = xml.find(heading)
    if idx < 0:
        raise SystemExit("References heading not found")
    insert_at = idx + len(heading)
    sect = xml.find("<w:sectPr>", insert_at)
    if sect < 0:
        raise SystemExit("sectPr not found")
    xml = xml[:insert_at] + bibl_begin + xml[insert_at:sect] + bibl_end + xml[sect:]
    return xml


def rewrite_docx(src: Path, dst: Path, new_xml: str) -> None:
    buf = src.read_bytes()
    with zipfile.ZipFile(src, "r") as zin, zipfile.ZipFile(dst, "w") as zout:
        for info in zin.infolist():
            data = new_xml.encode("utf-8") if info.filename == "word/document.xml" else zin.read(info.filename)
            zout.writestr(info, data)


def plain_text(xml: str) -> str:
    return "".join(re.findall(r"<w:t(?: [^>]*)?>([^<]*)</w:t>", xml))


def main() -> None:
    shutil.copy2(SRC_DOCX, BACKUP)
    bib = parse_bib(BIB)
    md = MD.read_text(encoding="utf-8")
    num_key = number_to_key(md, bib)
    csl = {k: to_csl(k, bib[k]) for k in num_key.values()}
    library = [csl[num_key[i]] for i in sorted(num_key)]
    LIBRARY.write_text(json.dumps(library, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    with zipfile.ZipFile(BACKUP) as z:
        xml = z.read("word/document.xml").decode("utf-8")
    before = plain_text(xml)
    xml, n_fields = wrap_citations(xml, num_key, csl)
    xml = add_bibl_and_pref(xml)
    after = plain_text(xml)
    if after != before:
        # Pref field has no visible text; bibl/citation visible t should match.
        # Pref instrText is not w:t. Difference would be a bug.
        raise SystemExit(
            f"Visible text changed ({len(before)} -> {len(after)}). Abort."
        )
    if "ADDIN ZOTERO_ITEM CSL_CITATION" not in xml:
        raise SystemExit("No Zotero citation fields written")
    tmp = OUT_DOCX.with_suffix(".zotero.tmp.docx")
    rewrite_docx(BACKUP, tmp, xml)
    tmp.replace(OUT_DOCX)
    print(f"backup {BACKUP}")
    print(f"library {LIBRARY} items={len(library)}")
    print(f"docx {OUT_DOCX} zotero_fields={n_fields}")
    print(f"ZOTERO_ITEM={xml.count('ADDIN ZOTERO_ITEM CSL_CITATION')} "
          f"BIBL={xml.count('ADDIN ZOTERO_BIBL')} PREF={xml.count('ADDIN ZOTERO_PREF')}")


if __name__ == "__main__":
    main()
