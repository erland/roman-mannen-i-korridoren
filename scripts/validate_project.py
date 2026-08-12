#!/usr/bin/env python3
"""Snabb deterministisk validering för romanskaparprojektet.

Använder endast Python-standardbiblioteket.
Avsedd att kunna köras både lokalt och i GitHub Actions.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import unquote

CHAPTER_RE = re.compile(r"kapitel-(\d{2,})\.md$")
CHAPTER_H1_RE = re.compile(r"^#\s+Kapitel\s+(\d+)\s+[–-]\s+(.+?)\s*$")
MARKERS = ("TODO", "FIXME", "[PLACEHOLDER]")
FORBIDDEN_EXPORT_NOTES = (
    "Kort kapitelnotering:",
    "## Kapitelnotering",
    "## Efter kapitel",
    "Viktiga händelser:",
    "Nya kontinuitetspunkter:",
    "Relationsförändringar:",
    "Öppna frågor:",
)

REQUIRED_PATHS = (
    "README.md",
    "roman-bibel.md",
    "synopsis.md",
    "kapitelplan.md",
    "projektstatus.md",
    "project-index.md",
    "kapitel",
    "omslag/mannen_i_korridoren_cover_1800x2700.jpg",
    "publishing/metadata.yaml",
    "publishing/epub.css",
    "publishing/fix-epub-after-pandoc.py",
    "publishing/pdf-template.tex",
    "publishing/pdf-filter.lua",
    "scripts/build_book.py",
)

REQUIRED_METADATA = {
    "title": "Mannen i korridoren",
    "subtitle": "Ingenstans är nog långt borta",
    "author": "Erland Lindmark",
    "publisher": "Erland Lindmark",
    "language": "sv-SE",
    "cover-image": "omslag/mannen_i_korridoren_cover_1800x2700.jpg",
}


def error(errors: list[str], message: str) -> None:
    errors.append(message)
    print(f"ERROR: {message}", file=sys.stderr)


def parse_simple_yaml_scalars(path: Path) -> dict[str, str]:
    """Läs enkla top-level YAML-skalärer utan extern YAML-dependency."""
    values: dict[str, str] = {}
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if not key or key.startswith("-"):
            continue
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
            value = value[1:-1]
        values[key] = value
    return values


def validate_markdown_links(root: Path, errors: list[str]) -> None:
    link_re = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
    for md in sorted(root.rglob("*.md")):
        if any(part in {".git"} for part in md.relative_to(root).parts):
            continue
        text = md.read_text(encoding="utf-8")
        for target in link_re.findall(text):
            target = target.strip().strip("<>")
            if not target or target.startswith(("#", "http://", "https://", "mailto:")):
                continue
            if " " in target and not target.startswith(("./", "../")):
                target = target.split(" ", 1)[0]
            target = unquote(target.split("#", 1)[0].split("?", 1)[0])
            if not target:
                continue
            candidate = (md.parent / target).resolve()
            try:
                candidate.relative_to(root.resolve())
            except ValueError:
                continue
            if not candidate.exists():
                error(errors, f"Trasig intern Markdown-länk i {md.relative_to(root)}: {target}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    errors: list[str] = []

    if not root.is_dir():
        error(errors, f"Projektkatalogen finns inte: {root}")
        return 1

    for rel in REQUIRED_PATHS:
        if not (root / rel).exists():
            error(errors, f"Obligatorisk projektsökväg saknas: {rel}")

    if errors:
        return 1

    chapter_dir = root / "kapitel"
    canonical: dict[int, Path] = {}
    alternatives: list[str] = []
    for path in sorted(chapter_dir.iterdir()):
        if not path.is_file():
            continue
        match = CHAPTER_RE.fullmatch(path.name)
        if match:
            number = int(match.group(1))
            if number in canonical:
                error(errors, f"Två filer representerar kapitel {number}.")
            canonical[number] = path
        elif path.name.lower() not in {"kapitelmall.md", "kapitelnoteringar.md"} and re.search(r"kapitel.*\d", path.name, re.I):
            alternatives.append(path.name)

    if alternatives:
        error(errors, "Icke-kanoniska möjliga kapitelfiler hittades: " + ", ".join(alternatives))

    numbers = sorted(canonical)
    if not numbers:
        error(errors, "Inga kapitel hittades.")
    else:
        expected = list(range(1, numbers[-1] + 1))
        missing = sorted(set(expected) - set(numbers))
        if missing:
            error(errors, "Kapitel saknas: " + ", ".join(map(str, missing)))

    if len(numbers) != 28:
        error(errors, f"Väntade 28 kapitel, hittade {len(numbers)}.")

    for number, path in sorted(canonical.items()):
        text = path.read_text(encoding="utf-8")
        stripped = text.strip()
        if not stripped:
            error(errors, f"{path.relative_to(root)} är tom.")
            continue
        first_line = stripped.splitlines()[0].strip()
        match = CHAPTER_H1_RE.fullmatch(first_line)
        if not match:
            error(errors, f"{path.relative_to(root)} har fel H1-format; väntat '# Kapitel {number} – Kapitelrubrik'.")
        elif int(match.group(1)) != number:
            error(errors, f"{path.relative_to(root)} har kapitelnummer {match.group(1)} i H1.")
        for marker in MARKERS:
            if marker in text:
                error(errors, f"{path.relative_to(root)} innehåller arbetsmarkören {marker}.")
        # Exportkapitlen ska inte innehålla arbetsnoteringar.
        for note_marker in FORBIDDEN_EXPORT_NOTES:
            if note_marker in text:
                error(errors, f"{path.relative_to(root)} innehåller kapitelnotering/exportarbetsmaterial: {note_marker}")

    metadata = parse_simple_yaml_scalars(root / "publishing/metadata.yaml")
    for key, expected in REQUIRED_METADATA.items():
        if metadata.get(key) != expected:
            error(errors, f"publishing/metadata.yaml har fel eller saknat värde för '{key}'.")

    validate_markdown_links(root, errors)

    if errors:
        print(f"\nValidation failed: {len(errors)} error(s).", file=sys.stderr)
        return 1

    print(f"OK: projektvalidering godkänd. {len(numbers)} kapitel, Apple Books-metadata och publiceringsfiler finns.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
