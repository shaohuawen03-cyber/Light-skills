#!/usr/bin/env python3
"""Patch discussion in current pre-Zotero English backup and Chinese.docx."""
from __future__ import annotations

import re
import zipfile
from html import escape
from pathlib import Path

from discussion_texts import (
    CN_DELETE_PREFIXES,
    CN_REPLACE,
    EN_DELETE_PREFIXES,
    EN_REPLACE,
    METHOD_CN,
    METHOD_EN,
)

ROOT = Path("/home/user/Light-skills")
BACKUP = ROOT / "projects" / "English_backup_pre-zotero.docx"
EN = ROOT / "projects" / "English.docx"
CN = ROOT / "deliverable" / "Chinese.docx"

TOKEN = re.compile(r"\[(\d+(?:[–-]\d+)?(?:,\s*\d+(?:[–-]\d+)?)*)\]")
P_RE = re.compile(r"<w:p(?: [^>]*)?>.*?</w:p>", re.DOTALL)


def para_text(p_xml: str) -> str:
    return "".join(re.findall(r"<w:t(?: [^>]*)?>([^<]*)</w:t>", p_xml))


def runs_xml(text: str) -> str:
    parts: list[str] = []
    last = 0
    for m in TOKEN.finditer(text):
        if m.start() > last:
            chunk = escape(text[last : m.start()], quote=False)
            parts.append(f'<w:r><w:t xml:space="preserve">{chunk}</w:t></w:r>')
        parts.append(f"<w:r><w:t>{escape(m.group(0), quote=False)}</w:t></w:r>")
        last = m.end()
    if last < len(text):
        chunk = escape(text[last:], quote=False)
        parts.append(f'<w:r><w:t xml:space="preserve">{chunk}</w:t></w:r>')
    return "".join(parts)


def replace_inner(p_xml: str, new_text: str) -> str:
    ppr = p_xml.find("</w:pPr>")
    start = ppr + len("</w:pPr>") if ppr >= 0 else p_xml.find(">") + 1
    return p_xml[:start] + runs_xml(new_text) + "</w:p>"


def rewrite_xml(xml: str, mapping: dict[str, str], deletes: tuple[str, ...]) -> str:
    out: list[str] = []
    last = 0
    unmatched = set(mapping)
    replaced = 0
    deleted = 0
    for m in P_RE.finditer(xml):
        p = m.group(0)
        txt = para_text(p).strip()
        out.append(xml[last : m.start()])
        if any(txt.startswith(d) for d in deletes):
            deleted += 1
            last = m.end()
            continue
        hit = next((k for k in mapping if txt.startswith(k)), None)
        if hit:
            out.append(replace_inner(p, mapping[hit]))
            unmatched.discard(hit)
            replaced += 1
        else:
            out.append(p)
        last = m.end()
    out.append(xml[last:])
    if unmatched:
        raise SystemExit(f"unmatched: {sorted(unmatched)}")
    print(f"replaced={replaced} deleted={deleted}")
    return "".join(out)


def patch_docx(path: Path, mapping: dict[str, str], deletes: tuple[str, ...], dest: Path | None = None) -> None:
    dest = dest or path
    with zipfile.ZipFile(path) as z:
        xml = z.read("word/document.xml").decode("utf-8")
    new_xml = rewrite_xml(xml, mapping, deletes)
    after = "".join(re.findall(r"<w:t(?: [^>]*)?>([^<]*)</w:t>", new_xml))
    if "Dinamarca et al. used" in after or "Inestrosa et al. showed" in after:
        raise SystemExit("old Author et al. style still present")
    if "Inestrosa 等证明" in after or "Dinamarca 等用" in after:
        raise SystemExit("old Author et al. Chinese style still present")
    tmp = dest.with_suffix(".tmp.docx")
    with zipfile.ZipFile(path, "r") as zin, zipfile.ZipFile(tmp, "w") as zout:
        for info in zin.infolist():
            data = new_xml.encode("utf-8") if info.filename == "word/document.xml" else zin.read(info.filename)
            zout.writestr(info, data)
    tmp.replace(dest)
    print("wrote", dest, dest.stat().st_size)


def main() -> None:
    # English.docx currently has Zotero fields; patch the clean backup.
    patch_docx(BACKUP, {**EN_REPLACE, **METHOD_EN}, EN_DELETE_PREFIXES, BACKUP)
    EN.write_bytes(BACKUP.read_bytes())
    print("copied clean English")
    patch_docx(CN, {**CN_REPLACE, **METHOD_CN}, CN_DELETE_PREFIXES, CN)


if __name__ == "__main__":
    main()
