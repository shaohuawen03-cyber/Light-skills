#!/usr/bin/env python3
"""Verify the project's bare-filename SHA256SUMS against source_materials/."""
from __future__ import annotations

import argparse
import hashlib
from pathlib import Path
import sys


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    root = args.project_root.resolve()
    manifest = root / "SHA256SUMS.txt"
    source_dir = root / "source_materials"
    failures = 0
    rows = 0
    for number, raw in enumerate(manifest.read_text(encoding="utf-8").splitlines(), start=1):
        if not raw.strip():
            continue
        try:
            expected, name = raw.lstrip("\ufeff").split(maxsplit=1)
        except ValueError:
            print(f"line {number}: malformed", file=sys.stderr)
            failures += 1
            continue
        name = name.lstrip("*")
        target = source_dir / name
        rows += 1
        if not target.is_file():
            print(f"MISSING  {name}")
            failures += 1
            continue
        actual = sha256(target)
        if actual.lower() == expected.lower():
            print(f"OK       {name}")
        else:
            print(f"MISMATCH {name}\n  expected {expected}\n  actual   {actual}")
            failures += 1
    print(f"verified={rows - failures} total={rows} failures={failures}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
