# `.local_tier/` — Tier 2 Local Mirrors

**Tier 2** in the KlickSmartAI 4-tier architecture (per `processes/lead-sniperai-cli-os.md`).
DuckDB files, gitignored, 600-chmod. Never the source of truth — Supabase (Tier 3) is.

```
.local_tier/
├── README.md                      # this file
├── clients_index.duckdb           # registry: every wiki client + its workspace state
├── clients/
│   ├── gpc-development.duckdb     # per-client empty mirror, schema pre-staged
│   └── veritas-developments.duckdb
├── scripts/                       # all scripts idempotent, re-runnable
│   ├── init_clients_index.py
│   ├── init_workspace_mirror.py
│   ├── sync_supabase_to_duckdb.py
│   └── verify_mirror.py
└── logs/                          # sync run logs (gitignored via .local_tier/)
```

## Tier rules (do not break)

| | rule |
|---|---|
| **write source** | DuckDB files are written by `init_*` scripts (from wiki) and `sync_supabase_to_duckdb.py` (from Supabase). Nothing else. |
| **read source** | Any script / agent can read. No write-back to Tier 3 from DuckDB. |
| **PASS-graded** | Tier 2 → Tier 3 sync only carries entities with `quality_gate = PASS`. Failures stay local. |
| **gitignored** | everything under `.local_tier/` is excluded from wiki git (see `~/.gitignore`). |
| **chmod 600** | every `.duckdb` file is owner-readable-only. No group/world access. |

## Schema source-of-truth

The schema in `init_workspace_mirror.py` mirrors the planned `client_workspaces` pattern
(`/home/denni/.hermes/skills/productivity/supabase/references/client-workspaces-pattern.md`)
and the Tier 3 → Tier 4 boundary rule. When Supabase schema changes, update the schema
block in `init_workspace_mirror.py` and re-run — the script is idempotent on existing tables.

## Re-running scripts

All four scripts are idempotent:

- `init_clients_index.py` — UPSERT on `slug`
- `init_workspace_mirror.py` — `CREATE TABLE IF NOT EXISTS`, no destructive ops
- `sync_supabase_to_duckdb.py` — UPSERT with `quality_gate = PASS` filter
- `verify_mirror.py` — read-only

## Verifying

```bash
python3 .local_tier/scripts/verify_mirror.py
# → table counts + integrity checks per client
```

## Adding a new client

1. Add `clients/<slug>/CLAUDE.md` + `IDENTITY.md` to the wiki (creates the wiki substrate).
2. `python3 .local_tier/scripts/init_clients_index.py --add <slug>`
3. `python3 .local_tier/scripts/init_workspace_mirror.py --add <slug>`

## Frappe wiring (Tier 4)

Phase 1 of `processes/frappe-workspace-preliminary-plan.md` will read from
`clients_index.duckdb` (the registry) and from each per-client duckdb (the mirror),
NOT directly from the wiki filesystem. This keeps the Frappe sync deterministic
and reviewable.
