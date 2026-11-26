#!/usr/bin/env python3
"""Check that Cutset's Markdown entry points still lead to the maintained guides."""

from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
HANDBOOK = ROOT / "handbook"
ENTRY_POINTS = {
    "README.md": "README.md",
    "AGENTS.md": "README.md",
    "CONTRIBUTING.md": "README.md",
    "SECURITY.md": "secrets.md",
}
LINK = re.compile(r"\]\(([^ )]+)\)")
FENCE = re.compile(r"^\s*(?:```|~~~)")


def relative_targets(document):
    """Read inline Markdown links, excluding code examples and web URLs."""
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
    guides = set(HANDBOOK.glob("*.md"))
    roots = [ROOT / name for name in ENTRY_POINTS]
    index = HANDBOOK / "README.md"
    errors = []
    if not index.is_file():
        errors.append("Missing handbook/README.md")
    checked = 0
    for document in sorted(guides.union(roots)):
        if not document.is_file():
            errors.append(f"Missing {document.relative_to(ROOT)}")
            continue
        targets = set(relative_targets(document))
        for target in targets:
            if not target.is_relative_to(ROOT) or not target.exists():
                errors.append(f"{document.relative_to(ROOT)} has a missing or external local target: {target.name}")
        if document == index:
            for guide in sorted(guides - targets - {index}):
                errors.append(f"Handbook index omits {guide.name}")
        if document.parent == ROOT:
            required = HANDBOOK / ENTRY_POINTS[document.name]
            if required not in targets:
                errors.append(f"{document.name} must link to handbook/{required.name}")
        checked += len(targets)
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"Handbook OK ({len(guides)} guides, {checked} distinct local links across documents)")


if __name__ == "__main__":
    main()
