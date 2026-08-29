# Tier 2 Seed SQL — Idempotent Workspace Onboarding

This directory holds **idempotent SQL seeds** for populating Supabase CRM-flavored tables from real wiki data. Re-running any seed file must produce the same final state — every row uses `uuid5` for deterministic IDs and `ON CONFLICT (id) DO UPDATE` upserts.

## Pattern

Every seed follows the same shape:

```sql
BEGIN;

INSERT INTO public.<table> (
    id, workspace_id, <columns>, metadata
) VALUES (
    '<uuid5>'::uuid, '<workspace_uuid>'::uuid, <values>, '<jsonb>'::jsonb
)
ON CONFLICT (id) DO UPDATE SET
    <every column EXCEPT id, workspace_id, created_at> = EXCLUDED.<col>;

COMMIT;
```

- `uuid5(workspace_uuid, "<table>/<slug>")` → deterministic ID, same (workspace, slug) → same UUID every run
- Whole batch in `BEGIN; ... COMMIT;` — one bad row rolls back all
- Every cell that source didn't provide → `NULL`, never fabricated
- `metadata` JSONB carries audit trail (source file path, source chat, source observation date)

## Files

| file | purpose | when to run |
|---|---|---|
| `onboarding_tasks_2026-08-29.sql` | Seed initial `public.tasks` rows for both real client workspaces (`gpc-development` 6 tasks, `veritas-developments` 8 tasks) | When a new client workspace is created and needs an initial onboarding task list |

## How to re-run a seed

```bash
# After updating any seed file:
psql "$SUPABASE_DB_URL" -f .local_tier/seeds/<file>.sql
# (or paste into dashboard SQL editor if pooler is down — see supabase skill)

# Then mirror to DuckDB:
python .local_tier/scripts/sync_workspace_to_supabase_and_duckdb.py <slug>
```

## Mirroring

After every Supabase seed/mutation, run `sync_workspace_to_supabase_and_duckdb.py <slug>` to keep the per-client DuckDB mirror in sync. Tier 2 (DuckDB) is read-only downstream of Tier 3 (Supabase) — never source of truth.

## Companion docs

- `~/wiki/processes/lead-sniperai-cli-os.md` — 4-tier architecture
- `~/.hermes/skills/productivity/supabase/references/workspace-seeding-from-wiki-content.md` — full pattern + pitfalls
- `~/.hermes/skills/productivity/supabase/references/klicksmartai-rios-schema.md` — verified schema for project `amgknqnhiscryvcfeoyj`