#!/usr/bin/env python3
"""Validate local Markdown structure without network access or dependencies."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"(?<!!)\[[^\]\n]*\]\(([^)\n]+)\)")
METHOD = re.compile(r"^## (M\d{3,})\s+", re.MULTILINE)


def without_fences(text: str) -> str:
    lines, fence = [], None
    for line in text.splitlines():
        match = re.match(r"^\s*(`{3,}|~{3,})", line)
        if match:
            marker = match.group(1)
            if fence is None:
                fence = (marker[0], len(marker))
            elif marker[0] == fence[0] and len(marker) >= fence[1]:
                fence = None
            lines.append("")
        else:
            lines.append(line if fence is None else "")
    return "\n".join(lines)


def anchors(text: str) -> set[str]:
    result = set(re.findall(r'<a\s+(?:id|name)=["\']([^"\']+)["\']', text))
    seen: dict[str, int] = {}
    for heading in re.findall(r"^#{1,6}\s+(.+?)\s*#*\s*$", text, re.MULTILINE):
        slug = re.sub(r"[^\w\- ]", "", heading.lower()).replace(" ", "-")
        count = seen.get(slug, 0)
        seen[slug] = count + 1
        result.add(slug if count == 0 else f"{slug}-{count}")
    return result


def validate(root: Path) -> tuple[list[str], dict[str, int]]:
    root = root.resolve()
    errors: list[str] = []
    documents = {p: without_fences(p.read_text(encoding="utf-8"))
                 for p in root.rglob("*.md")
                 if not any(part.startswith(".") for part in p.relative_to(root).parts)}
    anchor_map = {p: anchors(t) for p, t in documents.items()}
    for path, text in documents.items():
        for raw in LINK.findall(text):
            target = raw.strip().split(' "', 1)[0].strip("<>")
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc:
                continue
            dest = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
            if not dest.is_relative_to(root):
                errors.append(f"{path.relative_to(root)}: link escapes repository: {target}")
            elif not dest.exists():
                errors.append(f"{path.relative_to(root)}: missing target: {target}")
            elif parsed.fragment and dest.suffix == ".md":
                if unquote(parsed.fragment) not in anchor_map.get(dest, set()):
                    errors.append(f"{path.relative_to(root)}: missing anchor: {target}")
    domain_files = sorted((root / "atlas/domains").glob("*.md"))
    found: dict[str, Path] = {}
    index = documents.get(root / "atlas/index.md", "")
    if not domain_files:
        errors.append("No method-domain files found.")
    for path in domain_files:
        if f"domains/{path.name}" not in index:
            errors.append(f"Domain missing from atlas/index.md: {path.name}")
        ids = METHOD.findall(documents.get(path, ""))
        if not ids:
            errors.append(f"No method cards found: {path.name}")
        for mid in ids:
            if mid in found:
                errors.append(f"Duplicate method ID: {mid}")
            found[mid] = path
            if mid.lower() not in anchor_map[path]:
                errors.append(f"Missing stable method anchor: {mid}")
    try:
        metadata = json.loads((root / "references/provenance.json").read_text(encoding="utf-8"))
        if not isinstance(metadata.get("initial_counts"), dict):
            errors.append("provenance.json: initial_counts must be an object.")
    except (OSError, ValueError, AttributeError) as exc:
        errors.append(f"Invalid provenance.json: {exc}")
    return errors, {"markdown_files": len(documents), "domains": len(domain_files),
                    "methods": len(found)}


def main() -> int:
    errors, counts = validate(ROOT)
    if errors:
        print("Validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print("OK: " + ", ".join(f"{key}={value}" for key, value in counts.items()))
    print("Local links and anchors passed. Scientific claims and external URLs were not checked.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
