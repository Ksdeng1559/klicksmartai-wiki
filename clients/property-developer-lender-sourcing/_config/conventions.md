# Conventions

## File naming

- `kebab-case.md` for all markdown
- Date prefixes: `YYYY-MM-DD-description.md` for time-stamped artifacts
- Underscore prefix: `_template-*.md` for empty templates, `_*-index.csv` for hub files

## Folder rules

- `_config/` — voice, conventions, glossary, compliance (governance)
- `entities/` — sponsor entity record(s); one per developer
- `projects/` — per-developer sub-projects, promoted after validation
- `drafts/` — AI-generated work-in-progress; HITL-gated before promotion
- `deliverables/` — promoted client-facing outputs
- `library/` — reusable methodology + lender profiles (the playbook)

## Status values

- `draft` — initial AI generation, not validated
- `in-review` — under client or Dennis review
- `approved` — HITL-validated, source-of-truth
- `archived` — superseded; never delete, move + update STATUS.md

## Versioning

- Bump date in frontmatter on substantive edits
- Keep superseded versions in `STATUS.md` per wiki governance rules
