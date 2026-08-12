#!/usr/bin/env python3
"""Create or verify immutable annotated manuscript release tags."""
from __future__ import annotations

import argparse
from pathlib import Path
import re
import subprocess
import sys

PROJECT = Path(__file__).resolve().parents[1]
REPO = PROJECT.parents[1]
EXPECTED_BRANCH = "arena/019ff377-light-skills"
TAG_PREFIX = "porphyromonas-ad-manuscript-v"
VERSION_RE = re.compile(r"^[0-9]+\.[0-9]+\.[0-9]+$")


def git(*args: str, check: bool = True) -> str:
    process = subprocess.run(
        ["git", *args], cwd=REPO, text=True, capture_output=True, check=False
    )
    if check and process.returncode:
        detail = process.stderr.strip() or process.stdout.strip()
        raise SystemExit(f"git {' '.join(args)} failed: {detail}")
    return process.stdout.strip()


def tag_name(version: str) -> str:
    if not VERSION_RE.fullmatch(version):
        raise SystemExit("Version must use MAJOR.MINOR.PATCH, for example 3.0.0")
    return TAG_PREFIX + version


def ensure_release_preconditions(tag: str) -> None:
    branch = git("branch", "--show-current")
    if branch != EXPECTED_BRANCH:
        raise SystemExit(f"Refusing to tag branch {branch!r}; expected {EXPECTED_BRANCH!r}")
    dirty = git("status", "--porcelain")
    if dirty:
        raise SystemExit("Refusing to tag a dirty working tree; commit or discard changes first")
    exists = subprocess.run(
        ["git", "show-ref", "--verify", "--quiet", f"refs/tags/{tag}"], cwd=REPO
    ).returncode == 0
    if exists:
        raise SystemExit(f"Refusing to overwrite existing tag {tag}")


def create(args: argparse.Namespace) -> int:
    tag = tag_name(args.version)
    ensure_release_preconditions(tag)
    commit = git("rev-parse", args.commit)
    git("tag", "-a", tag, commit, "-m", args.message)
    print(f"created_tag={tag}")
    print(f"target_commit={commit}")
    if args.push:
        git("push", args.remote, f"refs/tags/{tag}")
        print(f"pushed_to={args.remote}")
    else:
        print(f"push_command=git push {args.remote} refs/tags/{tag}")
    return 0


def verify(args: argparse.Namespace) -> int:
    tag = tag_name(args.version)
    local = git("rev-list", "-n", "1", tag)
    remote_output = git("ls-remote", "--tags", args.remote, f"refs/tags/{tag}^{{}}", check=False)
    remote = remote_output.split()[0] if remote_output else ""
    print(f"tag={tag}")
    print(f"local_target={local}")
    print(f"remote_target={remote or 'NOT_FOUND'}")
    print(f"local_remote_equal={'yes' if local == remote else 'no'}")
    return 0 if local == remote else 1


def parser() -> argparse.ArgumentParser:
    main = argparse.ArgumentParser(description=__doc__)
    commands = main.add_subparsers(dest="command", required=True)
    create_cmd = commands.add_parser("create", help="create an immutable annotated tag")
    create_cmd.add_argument("--version", required=True)
    create_cmd.add_argument("--message", required=True)
    create_cmd.add_argument("--commit", default="HEAD")
    create_cmd.add_argument("--remote", default="origin")
    create_cmd.add_argument("--push", action="store_true")
    create_cmd.set_defaults(func=create)
    verify_cmd = commands.add_parser("verify", help="compare local and remote tag targets")
    verify_cmd.add_argument("--version", required=True)
    verify_cmd.add_argument("--remote", default="origin")
    verify_cmd.set_defaults(func=verify)
    return main


def main() -> int:
    args = parser().parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
