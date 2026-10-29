#!/usr/bin/env python3
"""Validate the repository's current documentation-only baseline.

This validator deliberately does not claim to build or test AIR itself. Add
product build, lint, security, and runtime test jobs only when their real
manifests and supported commands are present in the repository.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Sequence

REQUIRED_FILES = ("README.md", "MEC.md")
REQUIRED_README_TEXT = ("# AIR", "MEC.md")
REQUIRED_MEC_TEXT = (
    "# MASTER ENGINEERING CONTRACT (MEC)",
    "# 1. MISSION AND PRODUCT DEFINITION",
    "# 3. NON-NEGOTIABLE ENGINEERING PRINCIPLES",
)
CONFLICT_MARKERS = ("<<<<<<< ", ">>>>>>> ")


def validate_repository(root: Path) -> list[str]:
    """Return deterministic validation errors for repository documents."""
    errors: list[str] = []

    for relative_path in REQUIRED_FILES:
        path = root / relative_path
        if not path.is_file():
            errors.append(f"Required repository document is missing: {relative_path}")
            continue
        if not path.read_text(encoding="utf-8").strip():
            errors.append(f"Required repository document is empty: {relative_path}")

    markdown_files = sorted(
        path
        for path in root.rglob("*.md")
        if ".git" not in path.parts
    )
    for path in markdown_files:
        relative_path = path.relative_to(root).as_posix()
        try:
            content = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            errors.append(f"Cannot read Markdown file {relative_path}: {exc}")
            continue

        if not content.strip():
            errors.append(f"Markdown file is empty: {relative_path}")
            continue

        for line_number, line in enumerate(content.splitlines(), start=1):
            if any(line.startswith(marker) for marker in CONFLICT_MARKERS):
                errors.append(
                    f"Possible unresolved merge-conflict marker at "
                    f"{relative_path}:{line_number}"
                )
            if line.startswith("=======") and line.strip("= \t") == "":
                errors.append(
                    f"Possible unresolved merge-conflict separator at "
                    f"{relative_path}:{line_number}"
                )

    readme_path = root / "README.md"
    if readme_path.is_file():
        readme = readme_path.read_text(encoding="utf-8")
        for expected in REQUIRED_README_TEXT:
            if expected not in readme:
                errors.append(f"README.md is missing required content: {expected}")

    mec_path = root / "MEC.md"
    if mec_path.is_file():
        mec = mec_path.read_text(encoding="utf-8")
        for expected in REQUIRED_MEC_TEXT:
            if expected not in mec:
                errors.append(f"MEC.md is missing required section: {expected}")

    return errors


def main(argv: Sequence[str] | None = None) -> int:
    """CLI entry point; accepts an optional repository root for local use."""
    arguments = list(sys.argv[1:] if argv is None else argv)
    if len(arguments) > 1:
        print(
            "Usage: python3 scripts/validate_repository.py [repository-root]",
            file=sys.stderr,
        )
        return 2

    root = Path(arguments[0]).resolve() if arguments else Path(__file__).resolve().parents[1]
    errors = validate_repository(root)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"Repository validation failed with {len(errors)} error(s).", file=sys.stderr)
        return 1

    print("Repository document validation passed.")
    print(f"Validated required documents: {', '.join(REQUIRED_FILES)}")
    print("Validated Markdown files for emptiness and merge-conflict markers.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
