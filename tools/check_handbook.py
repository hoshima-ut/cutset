#!/usr/bin/env python3
"""Check local Markdown links from the Cutset documentation and its entry points."""
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
ENTRY_POINTS = {
    "README.md": "docs/README.md",
    "AGENTS.md": "docs/specs/README.md",
    "docs/CONTRIBUTING.md": "docs/development/README.md",
    "docs/SECURITY.md": "docs/security/credentials.md",
}
LINK = re.compile(r"\]\(([^ )]+)\)")
FENCE = re.compile(r"^\s*(?:```|~~~)")


def relative_targets(document):
    fenced = False
    for line in document.read_text(encoding="utf-8").splitlines():
        if FENCE.match(line):
            fenced = not fenced
        elif not fenced:
            for raw in LINK.findall(line):
                url = urlsplit(raw.strip("<>"))
                if not (url.scheme or url.netloc) and url.path:
                    yield (document.parent / unquote(url.path)).resolve()


def main():
    documents = set(DOCS.rglob("*.md")) | {ROOT / name for name in ENTRY_POINTS}
    count = 0
    for document in sorted(documents):
        relative = document.relative_to(ROOT).as_posix()
        targets = set(relative_targets(document))
        count += len(targets)
        for target in targets:
            if not target.is_relative_to(ROOT) or not target.exists():
                raise SystemExit(f"{relative}: missing or external local target {target}")
        if relative in ENTRY_POINTS and ROOT / ENTRY_POINTS[relative] not in targets:
            raise SystemExit(f"{relative}: missing link to {ENTRY_POINTS[relative]}")
    print(f"Documentation OK ({len(documents)} pages, {count} local links)")


if __name__ == "__main__":
    main()
