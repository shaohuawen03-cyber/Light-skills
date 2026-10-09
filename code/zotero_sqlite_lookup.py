#!/usr/bin/env python3
"""Read DOI -> item key from a Zotero sqlite (copied, WAL-safe). ASCII paths."""
from __future__ import annotations

import json
import os
import shutil
import sqlite3
import sys
import tempfile


def normalize_doi(raw: str) -> str:
    d = (raw or "").strip()
    for p in ("https://doi.org/", "http://doi.org/", "https://dx.doi.org/", "http://dx.doi.org/", "doi:"):
        if d.lower().startswith(p):
            d = d[len(p) :].strip()
    return d.lower().strip()


def copy_db(src: str, dst_dir: str) -> str:
    dst = os.path.join(dst_dir, "zotero.sqlite")
    shutil.copy2(src, dst)
    for extra in ("zotero.sqlite-wal", "zotero.sqlite-shm"):
        p = os.path.join(os.path.dirname(src), extra)
        if os.path.isfile(p):
            shutil.copy2(p, os.path.join(dst_dir, extra))
    return dst


def load_doi_keys(db_path: str) -> dict[str, str]:
    """DOI -> itemKey (8-char). URI host is always users/local; Word matches by key."""
    con = sqlite3.connect(db_path)
    con.row_factory = sqlite3.Row
    sql = """
    SELECT items.key AS itemKey, itemDataValues.value AS doi
    FROM items
    JOIN itemData ON itemData.itemID = items.itemID
    JOIN itemDataValues ON itemDataValues.valueID = itemData.valueID
    JOIN fieldsCombined ON fieldsCombined.fieldID = itemData.fieldID
    WHERE fieldsCombined.fieldName = 'DOI'
    """
    out: dict[str, str] = {}
    rows = con.execute(sql).fetchall()
    for r in rows:
        nd = normalize_doi(str(r["doi"] or ""))
        if nd and nd not in out:
            out[nd] = str(r["itemKey"])
    con.close()
    return out


def main() -> int:
    lib_path = sys.argv[1] if len(sys.argv) > 1 else "projects/English_Zotero_library.json"
    db_src = sys.argv[2] if len(sys.argv) > 2 else os.path.join(os.path.expanduser("~"), "Zotero", "zotero.sqlite")
    if not os.path.isfile(db_src):
        print("{}", end="")
        return 2
    with open(lib_path, encoding="utf-8") as f:
        library = json.load(f)
    tmp = tempfile.mkdtemp(prefix="zotero_sql_")
    try:
        db = copy_db(db_src, tmp)
        doi_keys = load_doi_keys(db)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    mapping = {}
    for item in library:
        ck = item.get("citation-key") or str(item.get("id"))
        nd = normalize_doi(str(item.get("DOI") or item.get("doi") or ""))
        key = doi_keys.get(nd)
        if not key:
            continue
        mapping[ck] = f"http://zotero.org/users/local/items/{key}"
    json.dump(mapping, sys.stdout, ensure_ascii=True)
    return 0 if mapping else 3


if __name__ == "__main__":
    raise SystemExit(main())
