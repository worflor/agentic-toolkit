#!/usr/bin/env python3
"""Check the toolkit's Agent Skill metadata and local Markdown links.

A lightweight structural check, not an evaluation of skill behaviour.
Uses only the Python standard library.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent.parent
NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
FRONTMATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*(?:\n|\Z)", re.DOTALL)
LINK = re.compile(r"!?\[[^\]\n]*\]\(([^)\n]+)\)")


def skill_errors(file: Path) -> list[str]:
    errors: list[str] = []
    text = file.read_text(encoding="utf-8")
    match = FRONTMATTER.match(text)
    if match is None:
        return [f"{file}: missing or malformed YAML frontmatter"]

    lines = match.group(1).splitlines()
    values: dict[str, str] = {}
    for index, line in enumerate(lines):
        field = re.fullmatch(r"([a-z][a-z0-9-]*):\s*(.*)", line)
        if field is None:
            continue
        key, value = field.groups()
        if key in values:
            errors.append(f"{file}: duplicate frontmatter field {key}")
        if value in (">", ">-", "|", "|-"):
            continuation: list[str] = []
            for next_line in lines[index + 1 :]:
                if next_line.startswith((" ", "\t")) or not next_line.strip():
                    continuation.append(next_line.strip())
                else:
                    break
            value = " ".join(part for part in continuation if part)
        values[key] = value.strip().strip("\"'")

    name = values.get("name", "")
    description = values.get("description", "")
    if not NAME.fullmatch(name) or len(name) > 64 or name != file.parent.name:
        errors.append(f"{file}: name must match its lowercase, hyphenated directory")
    if not 1 <= len(description) <= 1024:
        errors.append(f"{file}: description must contain 1–1024 characters")
    if len(text.splitlines()) > 500:
        errors.append(f"{file}: entry point exceeds the 500-line guideline")
    return errors


def link_errors(root: Path, file: Path) -> tuple[list[str], int]:
    errors: list[str] = []
    checked = 0
    fenced = False
    for line_number, line in enumerate(file.read_text(encoding="utf-8").splitlines(), 1):
        stripped = line.lstrip()
        if stripped.startswith((chr(96) * 3, "~~~")):
            fenced = not fenced
            continue
        if fenced:
            continue

        for match in LINK.finditer(line):
            raw = match.group(1).strip()
            # Optional Markdown link title follows the destination.
            destination = raw.split(" \"", 1)[0].split(" '", 1)[0]
            destination = destination.strip("<>")
            parsed = urlsplit(destination)
            if parsed.scheme or parsed.netloc or destination.startswith("//"):
                continue
            if not parsed.path:  # In-document anchor; not a file dependency.
                continue

            checked += 1
            target = (file.parent / unquote(parsed.path)).resolve()
            if not target.is_relative_to(root.resolve()):
                errors.append(f"{file}:{line_number}: local link escapes repository: {raw}")
            elif not target.exists():
                errors.append(f"{file}:{line_number}: missing local link target: {raw}")
    return errors, checked


def validate(root: Path) -> tuple[list[str], int, int, int]:
    errors: list[str] = []
    skills = root / "skills"
    skill_dirs = sorted(path for path in skills.iterdir() if path.is_dir()) if skills.is_dir() else []
    if not skill_dirs:
        errors.append("No skill directories found")
    for folder in skill_dirs:
        entry = folder / "SKILL.md"
        if not entry.is_file():
            errors.append(f"{folder}: missing SKILL.md")
        else:
            errors.extend(skill_errors(entry))

    documents = sorted(path for path in root.rglob("*.md") if ".git" not in path.parts)
    local_links = 0
    for file in documents:
        found, count = link_errors(root, file)
        errors.extend(found)
        local_links += count

    for required in ("README.md", "AGENTS.md", "LICENSE"):
        if not (root / required).is_file():
            errors.append(f"Missing required repository file: {required}")

    return errors, len(skill_dirs), len(documents), local_links


def main() -> int:
    errors, skills, documents, links = validate(ROOT)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"Validation failed: {len(errors)} issue(s).", file=sys.stderr)
        return 1

    print(f"Validated {skills} skill(s), {documents} Markdown file(s), "
          f"and {links} local link target(s).")
    print("Structural checks passed. Skill behaviour must be evaluated separately.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
