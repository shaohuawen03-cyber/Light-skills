#!/usr/bin/env python3
"""String-level discussion replace in deliverable/Chinese.docx. No whole-document lxml rewrite."""
from __future__ import annotations

import re
import zipfile
from html import escape
from pathlib import Path

from discussion_texts import CN_DELETE_PREFIXES, CN_REPLACE

ROOT = Path("/home/user/Light-skills")
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


def main() -> None:
    with zipfile.ZipFile(CN) as z:
        xml = z.read("word/document.xml").decode("utf-8")
        others = {i.filename: z.read(i.filename) for i in z.infolist() if i.filename != "word/document.xml"}
        infos = list(z.infolist())
    out: list[str] = []
    last = 0
    unmatched = set(CN_REPLACE)
    replaced = 0
    deleted = 0
    for m in P_RE.finditer(xml):
        p = m.group(0)
        txt = para_text(p).strip()
        out.append(xml[last : m.start()])
        if any(txt.startswith(d) for d in CN_DELETE_PREFIXES):
            deleted += 1
            last = m.end()
            continue
        hit = next((k for k in CN_REPLACE if txt.startswith(k)), None)
        if hit:
            out.append(replace_inner(p, CN_REPLACE[hit]))
            unmatched.discard(hit)
            replaced += 1
        else:
            out.append(p)
        last = m.end()
    out.append(xml[last:])
    if unmatched:
        raise SystemExit(f"unmatched: {sorted(unmatched)}")
    new_xml = "".join(out)
    after = para_text(new_xml) if False else "".join(re.findall(r"<w:t(?: [^>]*)?>([^<]*)</w:t>", new_xml))
    if "Inestrosa 等证明" in after or "Dinamarca 等用" in after:
        raise SystemExit("old Author et al. Chinese style still present")
    tmp = CN.with_suffix(".tmp.docx")
    with zipfile.ZipFile(CN, "r") as zin, zipfile.ZipFile(tmp, "w") as zout:
        for info in zin.infolist():
            data = new_xml.encode("utf-8") if info.filename == "word/document.xml" else zin.read(info.filename)
            zout.writestr(info, data)
    tmp.replace(CN)
    print(f"replaced={replaced} deleted={deleted} wrote {CN} {CN.stat().st_size}")


if __name__ == "__main__":
    main()
