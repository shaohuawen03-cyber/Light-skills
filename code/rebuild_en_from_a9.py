#!/usr/bin/env python3
"""Rebuild English.docx from a9e6101 backup XML (namespaces/zip intact).

Replace discussion by string-level paragraph edits only:
fact + [n], no 'Author et al. used', no RMSD recap.
Citations stay in their own <w:r><w:t>[n]</w:t></w:r> so the a9 injector matches.
"""
from __future__ import annotations

import io
import re
import subprocess
import zipfile
from html import escape
from pathlib import Path

from discussion_texts import EN_DELETE_PREFIXES, EN_REPLACE

ROOT = Path("/home/user/Light-skills")
OUT = ROOT / "projects" / "English.docx"
BACKUP = ROOT / "projects" / "English_backup_pre-zotero.docx"
DELIV = ROOT / "deliverable" / "English.docx"

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


def rewrite_xml(xml: str) -> str:
    out: list[str] = []
    last = 0
    unmatched = set(EN_REPLACE)
    deleted = 0
    replaced = 0
    for m in P_RE.finditer(xml):
        p = m.group(0)
        txt = para_text(p).strip()
        out.append(xml[last : m.start()])
        if any(txt.startswith(d) for d in EN_DELETE_PREFIXES):
            deleted += 1
            last = m.end()
            continue
        hit = next((k for k in EN_REPLACE if txt.startswith(k)), None)
        if hit:
            out.append(replace_inner(p, EN_REPLACE[hit]))
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


def write_docx(src_bytes: bytes, new_xml: str, dst: Path) -> None:
    zin = zipfile.ZipFile(io.BytesIO(src_bytes))
    tmp = dst.with_suffix(".tmp.docx")
    with zipfile.ZipFile(tmp, "w") as zout:
        for info in zin.infolist():
            data = (
                new_xml.encode("utf-8")
                if info.filename == "word/document.xml"
                else zin.read(info.filename)
            )
            zout.writestr(info, data)
    tmp.replace(dst)


def main() -> None:
    src = subprocess.check_output(
        ["git", "show", "a9e6101:projects/English_backup_pre-zotero.docx"]
    )
    z = zipfile.ZipFile(io.BytesIO(src))
    xml = z.read("word/document.xml").decode("utf-8")
    new_xml = rewrite_xml(xml)
    before = para_text(xml)
    after = "".join(re.findall(r"<w:t(?: [^>]*)?>([^<]*)</w:t>", new_xml))
    if "Dinamarca et al. used" in after or "Inestrosa et al. showed" in after:
        raise SystemExit("old Author et al. style still present")
    if "AChE accelerates" not in after:
        raise SystemExit("new discussion missing")
    write_docx(src, new_xml, OUT)
    BACKUP.write_bytes(OUT.read_bytes())
    DELIV.write_bytes(OUT.read_bytes())
    print("wrote", OUT, OUT.stat().st_size)
    print("backup", BACKUP, BACKUP.stat().st_size)


if __name__ == "__main__":
    main()
