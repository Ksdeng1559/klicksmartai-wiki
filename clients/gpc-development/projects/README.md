# projects/

**Validated deliverables — source of truth.**

Once Dennis approves a draft from `drafts/seo/`, the Markdown source moves here. This is the canonical location for every artifact that has been reviewed and signed off.

## Gate

Nothing lands in `projects/seo/` unless:
1. A draft exists in `drafts/seo/` with the same filename
2. The corresponding `VALIDATION_QUEUE.md` row is marked `approved`
3. `openseo-data-export` was invoked to do the promotion

## Promotion tool

Use the `openseo-data-export` skill. It:
- Moves the Markdown from `drafts/seo/` → `projects/seo/`
- Renders to HTML and copies to `deliverables/seo/`
- Exports DuckDB views to CSV in `deliverables/seo/csv/`
- Updates `VALIDATION_QUEUE.md` with the promotion date
- Optionally commits + pushes to git

## Currently empty

No projects have been promoted yet. The first promotion will be the audit quote sheet, after Dennis signs off.
