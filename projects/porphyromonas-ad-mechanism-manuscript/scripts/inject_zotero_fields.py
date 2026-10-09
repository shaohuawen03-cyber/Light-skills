#!/usr/bin/env python3
"""Insert Zotero Word fields that Refresh can read. Visible citation text unchanged.

Source is the current projects/English.docx (discussion already rewritten).
A no-field snapshot is written to English_backup_pre-zotero.docx first.
PREF uses Zotero DocumentData XML (data-version 3, fieldType=Field).
BIBL field begins inside the first Reference paragraph and ends inside the last.
In-text [n] runs become ADDIN ZOTERO_ITEM CSL_CITATION fields with full itemData.
Library comes from English_Zotero_library.json (not rebuilt).
"""
from __future__ import annotations

import json
import re
import uuid
import zipfile
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MD = ROOT / "manuscript" / "sci_submission" / "English.md"
BIB = ROOT / "references" / "references.bib"
BACKUP = Path("/home/user/Light-skills/projects/English_backup_pre-zotero.docx")
LIBRARY = Path("/home/user/Light-skills/projects/English_Zotero_library.json")
OUT_DOCX = Path("/home/user/Light-skills/projects/English.docx")
DELIVERABLE = Path("/home/user/Light-skills/deliverable/English.docx")

CITE_RE = re.compile(r"^\[(\d+(?:[–-]\d+)?(?:,\s*\d+(?:[–-]\d+)?)*)\]$")
TOKEN_RE = re.compile(r"\[(\d+(?:[–-]\d+)?(?:,\s*\d+(?:[–-]\d+)?)*)\]")
NOPROOF = "<w:rPr><w:noProof/></w:rPr>"
RUN_RE = re.compile(
    r"<w:r>(<w:rPr>.*?</w:rPr>)?<w:t([^>]*)>([^<]*)</w:t></w:r>",
    re.DOTALL,
)


def parse_bib(path: Path) -> dict[str, dict]:
    text = path.read_text(encoding="utf-8")
    entries = {}
    for m in re.finditer(r"(?ms)^@[A-Za-z]+\{([^,]+),(.*?)(?=^@[A-Za-z]+\{|\Z)", text):
        key, fields = m.group(1).strip(), m.group(2)
        rec: dict[str, str] = {}
        for fm in re.finditer(
            r"(?ms)^\s*([A-Za-z]+)\s*=\s*\{(.*?)\}(?=\s*,?\s*^\s*[A-Za-z]+\s*=|\s*\}\s*\Z)",
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
    out = []
    for person in re.split(r"\s+and\s+", raw):
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


def to_csl(key: str, rec: dict, numeric_id: int) -> dict:
    item = {
        "id": numeric_id,
        "type": "article-journal",
        "title": rec.get("title", "").replace("{", "").replace("}", ""),
        "author": parse_authors(rec.get("author", "")),
        "citation-key": key,
    }
    if rec.get("year"):
        m = re.search(r"\d{4}", rec["year"])
        if m:
            item["issued"] = {"date-parts": [[int(m.group())]]}
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
    refs = md.split("## References", 1)[1]
    doi_to_key = {
        rec["doi"].strip().lower().rstrip("."): key
        for key, rec in bib.items()
        if rec.get("doi")
    }
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


def instr_run(code: str) -> str:
    return (
        f'<w:r>{NOPROOF}<w:instrText xml:space="preserve">'
        f"{escape(code, quote=False)}</w:instrText></w:r>"
    )


def item_field_xml(visible: str, items: list[dict]) -> str:
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
                "uris": [
                    f"http://zotero.org/users/local/items/{item['citation-key']}"
                ],
                "itemData": item,
            }
            for item in items
        ],
        "schema": "https://github.com/citation-style-language/schema/raw/master/csl-citation.json",
    }
    code = " ADDIN ZOTERO_ITEM CSL_CITATION " + json.dumps(
        payload, ensure_ascii=False, separators=(",", ":")
    )
    return (
        f"<w:r>{NOPROOF}<w:fldChar w:fldCharType=\"begin\"/></w:r>"
        f"{instr_run(code)}"
        f"<w:r>{NOPROOF}<w:fldChar w:fldCharType=\"separate\"/></w:r>"
        f"<w:r>{NOPROOF}<w:t>{escape(visible)}</w:t></w:r>"
        f"<w:r>{NOPROOF}<w:fldChar w:fldCharType=\"end\"/></w:r>"
    )


def split_mixed_runs(xml: str) -> str:
    """Pull [n] tokens out of mixed w:t so each citation is its own run."""

    def repl(m: re.Match) -> str:
        rpr, _tattr, text = m.group(1) or "", m.group(2) or "", m.group(3)
        if not TOKEN_RE.search(text) or CITE_RE.match(text):
            return m.group(0)
        parts: list[str] = []
        last = 0
        for cm in TOKEN_RE.finditer(text):
            if cm.start() > last:
                chunk = text[last : cm.start()]
                parts.append(f'<w:r>{rpr}<w:t xml:space="preserve">{chunk}</w:t></w:r>')
            parts.append(f"<w:r>{rpr}<w:t>{cm.group(0)}</w:t></w:r>")
            last = cm.end()
        if last < len(text):
            chunk = text[last:]
            parts.append(f'<w:r>{rpr}<w:t xml:space="preserve">{chunk}</w:t></w:r>')
        return "".join(parts)

    return RUN_RE.sub(repl, xml)


def wrap_citations(xml: str, csl: dict[int, dict]) -> tuple[str, int]:
    n_max = max(csl)
    count = 0

    def repl(m: re.Match) -> str:
        nonlocal count
        visible = m.group(1)
        if not CITE_RE.match(visible):
            return m.group(0)
        nums = expand_cluster(visible[1:-1])
        if any(n < 1 or n > n_max or n not in csl for n in nums):
            return m.group(0)
        count += 1
        return item_field_xml(visible, [csl[n] for n in nums])

    xml = re.sub(
        r"<w:r>(?:<w:rPr>.*?</w:rPr>)?<w:t(?: [^>]*)?>(\[[^\[\]]+\])</w:t></w:r>",
        repl,
        xml,
    )
    return xml, count


def pref_paragraph() -> str:
    session = uuid.uuid4().hex
    data = (
        f'<data data-version="3" zotero-version="7.0.11">'
        f'<session id="{session}"/>'
        f'<style id="http://www.zotero.org/styles/vancouver" locale="en-US" '
        f'hasBibliography="1" bibliographyStyleHasBeenSet="1"/>'
        f"<prefs>"
        f'<pref name="fieldType" value="Field"/>'
        f'<pref name="automaticJournalAbbreviations" value="true"/>'
        f'<pref name="noteType" value="0"/>'
        f"</prefs></data>"
    )
    code = " ADDIN ZOTERO_PREF " + data
    hide = "<w:rPr><w:noProof/><w:vanish/><w:sz w:val=\"2\"/></w:rPr>"
    return (
        "<w:p>"
        f"<w:pPr>{hide}</w:pPr>"
        f"<w:r>{hide}<w:fldChar w:fldCharType=\"begin\"/></w:r>"
        f"<w:r>{hide}<w:instrText xml:space=\"preserve\">{escape(code, quote=False)}</w:instrText></w:r>"
        f"<w:r>{hide}<w:fldChar w:fldCharType=\"end\"/></w:r>"
        "</w:p>"
    )


def wrap_bibliography(xml: str) -> str:
    """Put BIBL begin/separate in first Reference paragraph; end in last."""
    bibl_code = (
        ' ADDIN ZOTERO_BIBL {"uncited":[],"omitted":[],"custom":[]} CSL_BIBLIOGRAPHY'
    )
    begin = (
        f"<w:r>{NOPROOF}<w:fldChar w:fldCharType=\"begin\"/></w:r>"
        f"{instr_run(bibl_code)}"
        f"<w:r>{NOPROOF}<w:fldChar w:fldCharType=\"separate\"/></w:r>"
    )
    end = f"<w:r>{NOPROOF}<w:fldChar w:fldCharType=\"end\"/></w:r>"

    heading = (
        '<w:p><w:pPr><w:pStyle w:val="Heading2"/><w:keepNext/></w:pPr>'
        "<w:r><w:t>References</w:t></w:r></w:p>"
    )
    h = xml.find(heading)
    if h < 0:
        raise SystemExit("References heading not found")
    after = h + len(heading)
    first_p = xml.find("<w:p>", after)
    if first_p < 0:
        raise SystemExit("first reference paragraph not found")
    # insert begin after the first <w:pPr>...</w:pPr> of that paragraph
    ppr_end = xml.find("</w:pPr>", first_p)
    if ppr_end < 0:
        raise SystemExit("first ref pPr not found")
    insert = ppr_end + len("</w:pPr>")
    xml = xml[:insert] + begin + xml[insert:]

    # last reference paragraph is the last <w:p> before <w:sectPr>
    sect = xml.rfind("<w:sectPr>")
    last_p_start = xml.rfind("<w:p>", 0, sect)
    last_p_end = xml.find("</w:p>", last_p_start)
    if last_p_start < 0 or last_p_end < 0:
        raise SystemExit("last reference paragraph not found")
    xml = xml[:last_p_end] + end + xml[last_p_end:]
    return xml


def plain_text(xml: str) -> str:
    return "".join(re.findall(r"<w:t(?: [^>]*)?>([^<]*)</w:t>", xml))


def rewrite_docx(src: Path, dst: Path, new_xml: str) -> None:
    tmp = dst.with_suffix(".zotero.tmp.docx")
    with zipfile.ZipFile(src, "r") as zin, zipfile.ZipFile(tmp, "w") as zout:
        for info in zin.infolist():
            data = (
                new_xml.encode("utf-8")
                if info.filename == "word/document.xml"
                else zin.read(info.filename)
            )
            zout.writestr(info, data)
    tmp.replace(dst)


def main() -> None:
    if not OUT_DOCX.is_file():
        raise SystemExit(f"missing {OUT_DOCX}")
    if not LIBRARY.is_file():
        raise SystemExit(f"missing {LIBRARY}")
    library = json.loads(LIBRARY.read_text(encoding="utf-8"))
    csl = {int(item["id"]): item for item in library}
    if len(csl) != 54:
        raise SystemExit(f"library size {len(csl)} != 54")

    with zipfile.ZipFile(OUT_DOCX) as z:
        xml = z.read("word/document.xml").decode("utf-8")
    if "ZOTERO_ITEM" in xml:
        raise SystemExit("English.docx already has Zotero fields; abort")
    BACKUP.write_bytes(OUT_DOCX.read_bytes())

    before = plain_text(xml)
    xml = split_mixed_runs(xml)
    xml, n_fields = wrap_citations(xml, csl)
    xml = xml.replace("<w:body>", "<w:body>" + pref_paragraph(), 1)
    xml = wrap_bibliography(xml)
    after = plain_text(xml)
    if after != before:
        raise SystemExit(f"Visible text changed ({len(before)} -> {len(after)}). Abort.")
    if n_fields < 1:
        raise SystemExit("no citation fields")
    if re.search(
        r"</w:p><w:r><w:rPr><w:noProof/></w:rPr><w:fldChar w:fldCharType=\"begin\"/>",
        xml,
    ):
        raise SystemExit("BIBL begin still outside a paragraph")
    if "Inestrosa et al. showed" in after or "Dinamarca et al. used" in after:
        raise SystemExit("old Author et al. sentence style still present")
    rewrite_docx(OUT_DOCX, OUT_DOCX, xml)
    if DELIVERABLE.parent.is_dir():
        DELIVERABLE.write_bytes(OUT_DOCX.read_bytes())
    print(f"backup {BACKUP}")
    print(f"library {LIBRARY} items={len(csl)}")
    print(f"docx {OUT_DOCX} zotero_item_fields={n_fields}")
    print(
        f"ITEM={xml.count('ZOTERO_ITEM')} BIBL={xml.count('ZOTERO_BIBL')} "
        f"PREF={xml.count('ZOTERO_PREF')} fieldType={xml.count('fieldType')}"
    )


if __name__ == "__main__":
    main()
