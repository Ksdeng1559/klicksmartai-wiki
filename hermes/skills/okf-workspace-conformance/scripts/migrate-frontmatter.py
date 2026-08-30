#!/usr/bin/env python3
"""
OKF v0.2 frontmatter migrator (idempotent).

Walks a bundle root and ensures every .md file (except reserved filenames
and configured exceptions) has parseable YAML frontmatter with a non-empty
`type:` field.

Behavior:
  - Skip files in EXCEPTIONS set and reserved filenames (index.md, log.md).
  - Skip files already conformant (first line `---` + has top-level `type:`).
  - Detect pre-existing non-OKF frontmatter (first line `---` but no
    top-level `type:`); insert `type:` as FIRST key, preserve all other
    fields exactly.
  - Migrate files with no frontmatter: insert YAML block at top.
    Default mode emits MINIMAL block (type + title + description + status +
    tags) per upstream OKF v0.2 §11 (only `type` is required for
    conformance).
    Pass --strict to also emit okf_version / generated / verified
    (the KlickSmartAI HITL overlay).

Classification rules (path-pattern based):
  See references/okf-type-vocabulary.md. The default mapping is loaded
  from DEFAULT_RULES below; override per-bundle with --rules=path.json.

Usage:
  migrate-frontmatter.py <bundle-root> [--dry-run] [--strict]
                                                [--rules=path.json]
                                                [--exceptions=f1,f2,...]
                                                [--primary-reviewer=human:dennis]

Modes:
  default  Minimal frontmatter (type + title + description + status + tags).
           Matches upstream OKF v0.2 §11 conformance requirements exactly.
  --strict KlickSmartAI HITL overlay (adds okf_version, generated, verified).
           Use for client-facing or agent-managed bundles.

Exit codes:
  0 — success (all migrated or already conformant)
  1 — at least one file failed
  2 — usage error

Author: KlickSmartAI / 2026-08-29
Spec:   https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/main/SPEC.md
"""

from __future__ import annotations

import argparse
import datetime
import json
import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# Reserved filenames per OKF §8/§9 — never add `type:`.
RESERVED_FILENAMES = {"index.md", "log.md"}

# Default exception set — files that MUST stay non-conformant.
# Can be overridden via --exceptions=f1,f2,...
DEFAULT_EXCEPTIONS = {"CLAUDE.md"}

# Default classification rules. Order matters: first match wins.
# Each rule: (path_predicate_lambda, type, status, verified_default)
# path_predicate takes (relative_path: str) and returns bool.
# verified_default is a `verified[]` entry dict, or None for empty.
DEFAULT_RULES: List[Tuple] = [
    # Root-level IDENTITY.md (workspace identity card)
    (lambda p: p == "IDENTITY.md", "Client Workspace", "stable",
     {"by": "human:dennis", "at": None, "evidence": "primary reviewer per okf-bundle.md"}),
    # Root-level CONTEXT.md (engagement context)
    (lambda p: p == "CONTEXT.md", "Client Engagement", "stable",
     {"by": "human:dennis", "at": None, "evidence": "primary reviewer per okf-bundle.md"}),
    # Root-level README
    (lambda p: p == "README.md", "Reference", "stable",
     {"by": "human:dennis", "at": None, "evidence": "primary reviewer per okf-bundle.md"}),
    # Archived prefix (any depth)
    (lambda p: any(part.startswith("_archive_") or part.startswith("_archived_")
                   or "deprecated" in part.lower() or "-old." in part.lower()
                   for part in Path(p).parts),
     "Archived", "deprecated", None),
    # _config/ files
    (lambda p: any(part == "_config" for part in Path(p).parts),
     None, "stable",  # type determined by filename below
     {"by": "human:dennis", "at": None, "evidence": "primary reviewer per okf-bundle.md"}),
    # sop/ files (callable Playbook pattern)
    (lambda p: any(part == "sop" for part in Path(p).parts),
     "Playbook", "stable",
     {"by": "human:dennis", "at": None, "evidence": "SOP author per okf-bundle.md"}),
    # drafts/ content
    (lambda p: any(part == "drafts" for part in Path(p).parts)
               and not p.endswith("README.md"),
     "Reference", "draft", None),  # user can override per-vertical
    # drafts/ per-folder README
    (lambda p: any(part == "drafts" for part in Path(p).parts)
               and p.endswith("README.md"),
     "Reference", "stable",
     {"by": "human:dennis", "at": None, "evidence": "primary reviewer per okf-bundle.md"}),
    # drafts-preview/ content (mirror of drafts/)
    (lambda p: any(part == "drafts-preview" for part in Path(p).parts)
               and not p.endswith("README.md"),
     "Reference", "draft", None),
    # projects/ content
    (lambda p: any(part == "projects" for part in Path(p).parts)
               and not p.endswith("README.md"),
     "Reference", "stable",
     {"by": "human:dennis", "at": None, "evidence": "primary reviewer + client reviewer"}),
    # projects/ README
    (lambda p: any(part == "projects" for part in Path(p).parts)
               and p.endswith("README.md"),
     "Reference", "stable",
     {"by": "human:dennis", "at": None, "evidence": "primary reviewer per okf-bundle.md"}),
    # projects-preview/ content
    (lambda p: any(part == "projects-preview" for part in Path(p).parts)
               and not p.endswith("README.md"),
     "Reference", "stable",
     {"by": "human:dennis", "at": None, "evidence": "primary reviewer per okf-bundle.md"}),
    # deliverables/ content
    (lambda p: any(part == "deliverables" for part in Path(p).parts)
               and not p.endswith("README.md"),
     "Reference", "stable",
     {"by": "human:dennis", "at": None, "evidence": "primary reviewer + client reviewer"}),
    # deliverables/ README
    (lambda p: any(part == "deliverables" for part in Path(p).parts)
               and p.endswith("README.md"),
     "Reference", "stable",
     {"by": "human:dennis", "at": None, "evidence": "primary reviewer per okf-bundle.md"}),
    # skills/ files
    (lambda p: any(part == "skills" for part in Path(p).parts),
     "Reference", "stable",
     {"by": "human:dennis", "at": None, "evidence": "primary reviewer per okf-bundle.md"}),
]

# _config/ filename → type mapping (per references/okf-type-vocabulary.md)
CONFIG_TYPE_MAP = {
    "voice.md": "Reference",
    "voice-styles.md": "Reference",
    "conventions.md": "Reference",
    "deliverables.md": "Reference",
    "glossary.md": "Glossary",
    "compliance.md": "Compliance",
    "gtm-skills.md": "SkillBinding",
    "okf-bundle.md": "Reference",
}


def now_iso() -> str:
    """ISO 8601 timestamp with explicit offset (OKF §5: required format)."""
    tz_offset = datetime.datetime.now().astimezone().utcoffset()
    if tz_offset is None:
        tz_str = "Z"
    else:
        total_minutes = int(tz_offset.total_seconds() // 60)
        sign = "+" if total_minutes >= 0 else "-"
        total_minutes = abs(total_minutes)
        hours, minutes = divmod(total_minutes, 60)
        tz_str = f"{sign}{hours:02d}:{minutes:02d}"
    return datetime.datetime.now().strftime(f"%Y-%m-%dT%H:%M:%S{tz_str}")


def parse_frontmatter(text: str) -> Optional[Tuple[str, str, str]]:
    """
    Parse YAML frontmatter if present.
    Returns (frontmatter_block, body, raw_after_first_fence) or None if no frontmatter.
    Bounded by first two `---` lines (the fence lines themselves are not included).
    """
    lines = text.split("\n")
    if not lines or lines[0].rstrip() != "---":
        return None
    # Find closing fence
    for i in range(1, len(lines)):
        if lines[i].rstrip() == "---":
            fm_block = "\n".join(lines[1:i])
            body = "\n".join(lines[i + 1:])
            return (fm_block, body, lines[0])
    return None  # Unclosed frontmatter — treat as no frontmatter


def has_top_level_type(fm_block: str) -> bool:
    """
    Check if frontmatter block has a top-level `type:` key.
    Important: must NOT match `report_type:` or body substrings.
    """
    for line in fm_block.split("\n"):
        stripped = line.lstrip()
        # Top-level means no indentation
        if stripped.startswith("type:"):
            # Must have a non-empty value
            val = stripped[len("type:"):].strip()
            if val:
                return True
    return False


def classify(path: str, rules: List[Tuple]) -> Tuple[str, str, Optional[Dict]]:
    """Return (type, status, verified_entry_or_none) for a relative path."""
    # Special-case _config/ filenames first
    fname = os.path.basename(path)
    if fname in CONFIG_TYPE_MAP:
        for predicate, _type, status, verified in rules:
            if predicate(path) and _type is None:
                return CONFIG_TYPE_MAP[fname], status, verified
    # Default rule matching
    for predicate, _type, status, verified in rules:
        if _type is None:
            continue  # type-only rules handled above
        if predicate(path):
            return _type, status, verified
    # Catch-all
    return "Reference", "draft", None


def build_frontmatter(type_: str, status: str, title: str, description: str,
                      verified_entry: Optional[Dict], strict: bool = False) -> str:
    """Build a YAML frontmatter block for a newly-migrated file.

    Per upstream OKF v0.2 §11, only `type` is required for conformance. By
    default this emits the MINIMAL block (type + title + description + status +
    tags). Pass strict=True to also emit okf_version / generated / verified
    (the KlickSmartAI HITL overlay).
    """
    generated_at = now_iso()
    lines = ["---"]
    if strict:
        lines.append('okf_version: "0.2"')
    lines.append(f"type: {type_}")
    lines.append(f"title: {title}")
    lines.append(f"description: {description}")
    lines.append("tags: []")
    lines.append(f"status: {status}")
    if strict:
        lines.append(f"generated:")
        lines.append(f"  by: human:dennis")
        lines.append(f"  at: {generated_at}")
        if verified_entry:
            # Fill in `at` if not set
            if verified_entry.get("at") is None:
                verified_entry = {**verified_entry, "at": generated_at}
            lines.append("verified:")
            lines.append(f"  - by: {verified_entry['by']}")
            lines.append(f"    at: {verified_entry['at']}")
            if verified_entry.get("evidence"):
                lines.append(f"    evidence: {verified_entry['evidence']}")
        else:
            lines.append("verified: []")
    lines.append("---")
    return "\n".join(lines)


def insert_type_into_existing(fm_block: str, type_: str) -> str:
    """Insert `type: <value>` as FIRST key in existing frontmatter block."""
    lines = fm_block.split("\n")
    # Skip leading blank lines if any
    insert_idx = 0
    while insert_idx < len(lines) and lines[insert_idx].strip() == "":
        insert_idx += 1
    lines.insert(insert_idx, f"type: {type_}")
    return "\n".join(lines)


def title_from_filename(path: str) -> str:
    """Derive a human-readable title from a relative path."""
    fname = os.path.basename(path)
    stem = os.path.splitext(fname)[0]
    # Convert kebab-case / snake_case to Title Case
    title = stem.replace("_", " ").replace("-", " ").strip()
    return title.title() if title else "Untitled"


def first_paragraph(body: str, max_chars: int = 150) -> str:
    """Extract first non-empty paragraph as description (truncated)."""
    for para in re.split(r"\n\s*\n", body):
        cleaned = para.strip()
        if cleaned and not cleaned.startswith("#"):
            cleaned = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", cleaned)  # strip links
            cleaned = re.sub(r"[*_`]+", "", cleaned)  # strip emphasis
            if len(cleaned) > max_chars:
                cleaned = cleaned[:max_chars - 3].rstrip() + "..."
            return cleaned
    return "(no description)"


def migrate_file(fpath: Path, rel_path: str, type_: str, status: str,
                 verified_entry: Optional[Dict], dry_run: bool,
                 strict: bool = False) -> str:
    """Migrate a single file. Returns action label."""
    text = fpath.read_text(encoding="utf-8")
    parsed = parse_frontmatter(text)

    if parsed is None:
        # No frontmatter — create new
        fm_block, body, _ = "", text, None
        action = "INSERT-NEW"
    else:
        fm_block, body, _ = parsed
        if has_top_level_type(fm_block):
            return "ALREADY-CONFORMANT"
        # Pre-existing non-OKF frontmatter — insert type
        new_fm = insert_type_into_existing(fm_block, type_)
        new_text = "---\n" + new_fm + "\n---\n" + body.lstrip("\n")
        if not dry_run:
            fpath.write_text(new_text, encoding="utf-8")
        return "INSERTED-TYPE"

    # Build new frontmatter for files with none
    title = title_from_filename(rel_path)
    description = first_paragraph(body)
    new_fm_block = build_frontmatter(type_, status, title, description,
                                      verified_entry, strict=strict)
    new_text = new_fm_block + "\n" + body.lstrip("\n")
    if not dry_run:
        fpath.write_text(new_text, encoding="utf-8")
    return action


def main() -> int:
    parser = argparse.ArgumentParser(
        description="OKF v0.2 frontmatter migrator (idempotent).")
    parser.add_argument("bundle_root", help="Absolute path to the bundle root.")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show plan without writing files.")
    parser.add_argument("--rules", default=None,
                        help="Path to JSON rules override (see references/okf-type-vocabulary.md).")
    parser.add_argument("--exceptions", default="",
                        help="Comma-separated list of filenames to skip (in addition to defaults).")
    parser.add_argument("--primary-reviewer", default="human:dennis",
                        help="Default `human:` actor for `verified[]` (default: human:dennis).")
    parser.add_argument("--strict", action="store_true",
                        help="Emit KlickSmartAI HITL overlay (okf_version + generated + verified) "
                             "on every migrated file. Default (off) emits only the MINIMAL block "
                             "(type + title + description + status + tags) per upstream OKF v0.2 §11 "
                             "where only `type` is required for conformance.")
    args = parser.parse_args()

    root = Path(args.bundle_root).resolve()
    if not root.is_dir():
        print(f"ERROR: bundle root not found: {root}", file=sys.stderr)
        return 2

    # Build exceptions set
    exceptions = set(DEFAULT_EXCEPTIONS)
    if args.exceptions:
        exceptions.update(x.strip() for x in args.exceptions.split(",") if x.strip())

    # Load rules
    rules = DEFAULT_RULES
    if args.rules:
        rules_path = Path(args.rules)
        if not rules_path.is_file():
            print(f"ERROR: rules file not found: {rules_path}", file=sys.stderr)
            return 2
        # Placeholder: JSON rules override support can be added later.
        # For now, warn and use defaults.
        print(f"WARN: JSON rules override not yet implemented; using defaults.",
              file=sys.stderr)

    # Walk
    md_files = sorted(root.rglob("*.md"))
    counts = {"ALREADY-CONFORMANT": 0, "INSERT-NEW": 0, "INSERTED-TYPE": 0,
              "EXCEPTION": 0, "RESERVED": 0}
    failures = []

    for fpath in md_files:
        rel_path = str(fpath.relative_to(root))
        fname = os.path.basename(rel_path)

        if fname in RESERVED_FILENAMES:
            counts["RESERVED"] += 1
            continue
        if fname in exceptions:
            counts["EXCEPTION"] += 1
            print(f"  [SKIP/exception] {rel_path}")
            continue

        type_, status, verified_entry = classify(rel_path, rules)

        try:
            action = migrate_file(fpath, rel_path, type_, status, verified_entry,
                                  args.dry_run, strict=args.strict)
            counts[action] = counts.get(action, 0) + 1
            label = "[DRY-RUN] " if args.dry_run else ""
            print(f"  {label}{action}: {rel_path}  →  type={type_}, status={status}")
        except Exception as e:
            failures.append((rel_path, str(e)))
            print(f"  FAILED: {rel_path}: {e}", file=sys.stderr)

    # Summary
    print()
    print("=== Migration summary ===")
    print(f"Bundle root: {root}")
    print(f"Dry-run: {args.dry_run}")
    print(f"  ALREADY-CONFORMANT: {counts['ALREADY-CONFORMANT']}")
    print(f"  INSERT-NEW:         {counts['INSERT-NEW']}")
    print(f"  INSERTED-TYPE:      {counts['INSERTED-TYPE']}")
    print(f"  EXCEPTION (skipped): {counts['EXCEPTION']}")
    print(f"  RESERVED (skipped): {counts['RESERVED']}")
    if failures:
        print(f"\nFailures: {len(failures)}")
        for rel, err in failures:
            print(f"  {rel}: {err}")
        return 1
    print()
    if args.dry_run:
        print("DRY-RUN complete. Re-run without --dry-run to apply.")
    else:
        print("Migration complete. Run scripts/check-conformance.sh to verify.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
