#!/usr/bin/env python3
"""Maintain this repository's generated entrypoint and simple local Markdown links.

Python 3.10+, standard library only. No network, shell execution, or project scan.
Not a general Markdown validator or a portability certification tool.
"""

import argparse
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "skills" / "unwalled-garden" / "SKILL.md"
ENTRY = ROOT / "UNWALL.md"
HEADER = "<!-- Generated from skills/unwalled-garden/SKILL.md; edit that source. -->\n\n"


def expected_entry() -> str:
    source = SOURCE.read_text(encoding="utf-8")
    parts = source.split("---\n", 2)
    if len(parts) != 3 or parts[0] != "":
        raise ValueError("SKILL.md must begin with YAML frontmatter")
    frontmatter = parts[1]
    if not re.search(r"^name: unwalled-garden$", frontmatter, re.M):
        raise ValueError("SKILL.md must use the directory-matching skill name")
    match = re.search(r"^description: (.+)$", frontmatter, re.M)
    if not match or not 1 <= len(match[1]) <= 1024:
        raise ValueError("SKILL.md needs a single-line description of 1–1024 characters")
    if not parts[2].strip():
        raise ValueError("SKILL.md body cannot be empty")
    return HEADER + parts[2].lstrip("\n")


def markdown_files():
    for path in sorted(ROOT.rglob("*.md")):
        if not any(part.startswith(".") for part in path.relative_to(ROOT).parts):
            yield path


def local_link_errors(path: Path):
    # Our docs use simple inline links. Ignore fenced code, fragments, URLs,
    # and mailto links. This deliberately does not parse arbitrary Markdown.
    content = re.sub(r"```[^\n]*\n.*?```", "", path.read_text(encoding="utf-8"), flags=re.S)
    for match in re.finditer(r"\[[^\]\n]+\]\(([^)\n]+)\)", content):
        target = match[1].strip()
        if target.startswith("<") and target.endswith(">"):
            target = target[1:-1]
        parsed = urlsplit(target)
        if parsed.scheme or parsed.netloc or not parsed.path:
            continue
        destination = (path.parent / unquote(parsed.path)).resolve()
        if not destination.is_relative_to(ROOT.resolve()):
            yield f"{path.relative_to(ROOT)}: link leaves repository: {target}"
        elif not destination.exists():
            yield f"{path.relative_to(ROOT)}: missing local link target: {target}"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sync", action="store_true", help="regenerate UNWALL.md before checking")
    args = parser.parse_args()
    try:
        expected = expected_entry()
        if args.sync:
            if not ENTRY.exists() or ENTRY.read_text(encoding="utf-8") != expected:
                ENTRY.write_text(expected, encoding="utf-8")
                print("Updated UNWALL.md from the canonical skill.")
        errors = []
        if not ENTRY.exists() or ENTRY.read_text(encoding="utf-8") != expected:
            errors.append("UNWALL.md differs from SKILL.md; run python3 scripts/check.py --sync")
        paths = list(markdown_files())
        for path in paths:
            errors.extend(local_link_errors(path))
    except (OSError, ValueError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        return 1
    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        return 1
    print(f"PASS: generated entrypoint matches; simple local links checked in {len(paths)} Markdown files.")
    print("External URLs, anchor fragments, host behavior, and project portability are not verified.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
