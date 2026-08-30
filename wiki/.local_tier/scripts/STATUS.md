# .local_tier/scripts/ — status map

These scripts are kept on disk **for reference**. Only one is currently
active; the others are kept because they document earlier design choices
and may inform future schema decisions.

## Active (use this)

| script | role |
|---|---|
| `sync_workspace_to_supabase_and_duckdb.py` | **Current entry point.** Phase A: UPSERT `public.workspaces` row from `wiki/clients/<slug>/IDENTITY.md`. Phase B: mirror the 5 workspace-scoped CRM tables (`workspaces`, `contacts`, `organizations`, `tasks`, `touchpoints`) into per-client `.local_tier/clients/<slug>.duckdb`. Idempotent on slug. |

Usage:
```
sync_workspace_to_supabase_and_duckdb.py gpc-development veritas-developments
sync_workspace_to_supabase_and_duckdb.py --dry-run gpc-development
```

## Superseded (do NOT run)

These scripts were written against a **different Supabase project**
(`yolqrstktoqlszybwymw` / Lead Signal Service) which used a
`client_workspaces` + signal/evidence schema. They do NOT apply to
`amgknqnhiscryvcfeoyj` (Klicksmartai-RIOS), which uses a 41-table
CRM schema with `public.workspaces` as the parent table.

| script | why superseded | replacement |
|---|---|---|
| `init_clients_index.py` | Built wiki-side `clients_index.duckdb` with entity-shaped index. Useful as a reference for the wiki catalog pattern, but not used in the current sync path. | none — `clients_index.duckdb` is no longer the canonical index. Wiki workspace identity now flows directly into Supabase `public.workspaces` via the active script. |
| `init_workspace_mirror.py` | Created per-client duckdbs with custom `workspace`/`deliverable`/`approval` tables that don't match any Supabase table. | `sync_workspace_to_supabase_and_duckdb.py` — the schema is rebuilt on every run from `information_schema.columns` so it always matches the live Supabase shape. |
| `sync_supabase_to_duckdb.py` | Queried `client_workspaces` (table that doesn't exist in this project) and tried to mirror a signal-service pattern (`entity_id`/signal/evidence) into CRM-shaped duckdbs. | same — use the active script above. |
| `verify_mirror.py` | Asserted the OLD per-client schema (`workspace`, `deliverable`, `approval`, `sync_state`, `audit_log`). Would fail against the new duckdbs which use `workspace_meta`, `contact`, `organization`, `task`, `touchpoint` + `sync_state` + `audit_log`. | not yet replaced — verification is currently inline in the active script. |

## Why keep them?

- They encode decisions we **didn't end up taking** (entity_id/signal/evidence pattern vs. CRM-shaped pattern). Useful archaeology.
- They demonstrate the **two-tier sync bugs** we hit (DuckDB `BIGSERIAL` not supported, sequence-before-table ordering, touch-before-connect race, YAML title capture vs. nested-key capture, ` — ` separator direction).
- Removing them would lose the trail of how we got to the current shape. Anyone iterating on this later (Frappe Tier 4 wiring, additional clients) may want to see the rejected approach.

## Schema mapping cheat-sheet

| superseded script | thought this was the schema | actual Klicksmartai-RIOS schema |
|---|---|---|
| `init_workspace_mirror.py` | `workspace, deliverable, approval, sync_state, audit_log` (custom) | `workspace_meta, contact, organization, task, touchpoint, sync_state, audit_log` (CRM-shaped) |
| `sync_supabase_to_duckdb.py` | `client_workspaces` parent + `leads`, `lead_signals`, `lead_opportunities` | `workspaces` parent + `contacts`, `organizations`, `tasks`, `touchpoints` (workspace-scoped only) |
| `verify_mirror.py` | `workspace` table with `slug PK, name, identity_md, context_md, paths JSON` | `workspace_meta` table with full `public.workspaces` columns (`id, name, slug, plan, vertical, settings jsonb, onboarding_status, vertical_pack, created_at, updated_at`) |

## Adding more wiki clients

The active script accepts any number of slugs as positional args. To add
a third wiki client:

```
~/wiki/.local_tier/scripts/sync_workspace_to_supabase_and_duckdb.py <new-slug>
```

It will UPSERT into `public.workspaces` (creating the parent row if
absent) and mirror any existing workspace-scoped CRM rows into a fresh
`.local_tier/clients/<new-slug>.duckdb`.