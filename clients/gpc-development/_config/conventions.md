# Conventions — GPC Development

## File naming

| Pattern | Example |
|---|---|
| `<phase>-<YYYY-MM-DD>-<topic-slug>.md` | `audit-2026-08-26-gpc.md` |
| `<phase>-<YYYY-MM-DD>-<topic-slug>.html` | `audit-2026-08-26-gpc.html` |
| `<phase>-<YYYY-MM-DD>-<topic-slug>.csv` | `keyword-research-2026-08-26-vancouver-gc.csv` |

Phase names (from `_config/deliverables.md`):
- `audit` — site audit reports
- `audit-quote` — audit + engagement quote sheet
- `paa` — PAA demand discovery
- `keywords` — keyword research
- `serp` — SERP intelligence
- `domain` — domain research
- `content` — content optimization
- `rank-tracking-setup` — tracker setup report
- `analytics` — GA4/GSC report
- `local` — local SEO report
- `monthly-report` — recurring client deliverable
- `export-manifest` — data export manifest

## Folder rules

| Folder | Purpose | Gate |
|---|---|---|
| `drafts/seo/` | AI work in progress | First pass — no approval needed |
| `drafts-preview/seo/` | HTML previews of drafts | First pass — no approval needed |
| `drafts/seo/VALIDATION_QUEUE.md` | What's pending review | First pass — add row when draft lands |
| `projects/seo/` | Validated source-of-truth Markdown | Promoted only after Dennis approval |
| `deliverables/seo/` | Client-ready HTML exports | Promoted only after `projects/` promotion |
| `deliverables/seo/csv/` | CSV exports from DuckDB | First pass — but only from validated data |
| `_config/` | Workspace configuration | First pass — no gate |
| `skills/` | Per-client skill adapters | First pass — no gate |

## Branch / commit conventions

This workspace is in `~/wiki/clients/gpc-development/` — a git repo. Master branch = master.

Commit messages follow the pattern `seo/<phase>: <action>`:
- `seo/audit: add 110-issue audit findings`
- `seo/keywords: add vancouver-gc seed research (480 cr)`
- `seo/export: promote audit-quote to deliverables (client-ready)`

## DuckDB sync

The `openseo-duckdb-sync` cron pulls GPC project data from OpenSEO D1 into the DuckDB mirror at `.local_tier/clients/gpc-development.duckdb` every 30 minutes. Scope: project_id `34afee19-d725-4073-b43f-1b76c6275c11`.

Manual sync: `~/.hermes/scripts/sync-openseo-duckdb.py --project-id 34afee19-d725-4073-b43f-1b76c6275c11`

## Identity preservation

- **Don't strip the OpenSEO project ID** from any artifact — it's the link back to source data.
- **Don't rename client folders** — `_config/voice.md` and `_config/glossary.md` reference `gpc-development` everywhere.
- **Don't conflate** with `/home/denni/wiki/clients/open-seo/` — that's the parent tools workspace, not the GPC workspace.
