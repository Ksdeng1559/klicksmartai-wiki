---
title: LeadSniperAI Project Status
created: 2026-10-11
updated: 2026-10-11
type: status
tags: [leadsniperai, status, handoff]
related: [ARCHITECTURE.md, MCP-TOOLS-REFERENCE.md]
---

# LeadSniperAI — Project Status (2026-10-11)

## TL;DR

LeadSniperAI's **4-layer architecture is designed and 75% built**. Discovery, Staging, and Record layers are operational. Semantic Recall (Pinecone) is wired at the MCP level but not yet integrated into the pipeline. **Next session: build the contact-embedding step + the leadsniperai KB index.**

**Repo**: the in-progress v3.1 refactor lives on branch [`hermes-lead-credit`](https://github.com/Ksdeng1559/LeadSniper-3.0/tree/hermes-lead-credit) of the LeadSniper-3.0 repo. See `scripts/leadsniper/STATUS.md` for refactor status. The README on that branch credits Hermes as the Lead AI operating layer. **Not yet merged to `main`** — review the PR before approving.

---

## What's working today

| Component | Status | Evidence |
|---|---|---|
| LeadSniper-3.0 FastAPI backend (25 endpoints) | ✓ live | `http://127.0.0.1:8000/api/v1/health` |
| LeadSniper MCP server (17 tools) | ✓ enabled | `hermes mcp list` shows ✓ enabled, all tools |
| `icp_candidate_pipeline.py` | ✓ working | end-to-end Gemini + Maps → DuckDB → Supabase |
| DuckDB per-workspace staging | ✓ working | `~/.local_tier/veritas-developments.duckdb`, `spectra-holdings.duckdb` |
| Parquet raw-response storage | ✓ working | `request_log` table stores `response_parquet` per call |
| Supabase as system of record | ✓ working | project `yolqrstktoqlszybwymw`, `client_workspaces` table live |
| `veritas-developments` workspace | ✓ live | slug resolves, signal_definitions populated |
| `spectra-holdings` workspace | ✓ live | slug resolves |
| `icp_candidate_pipeline.py --dry-run` mode | ✓ working | returns candidate list without Supabase writes |
| `signal_dashboard` view | ✓ working | queries `v_workspace_signal_dashboard` |
| `archive_no_signal` tool | ✓ working | dry_run + archive modes |
| 14 LeadSniper source docs in wiki | ✓ present | `projects/leadsniperai/*.md` (8) + `drafts/leadsniperai-*.md` (6) |

---

## What's pending (next session)

| Component | Owner | Effort |
|---|---|---|
| `leadsniperai` Pinecone index creation via MCP | Hermes | 5 min |
| Upsert 12,308 lines / 14 LeadSniper source files into Pinecone | Hermes | 10 min |
| `search-records` smoke test | Hermes | 2 min |
| Contact-embedding step in `icp_candidate_pipeline.py` (post-Supabase-sync) | TBD — design first | 1-2 hours |
| Update `README.md` "Agent Onboarding" with new LeadSniper section | Hermes | 15 min |
| Add `mcp__leadsniper__*` row to README tool table | Hermes | 5 min |
| MotherDuck enablement | NOT REQUIRED | opt-in only |
| Qdrant cleanup in PRDs (`cli-prd.md`, `marketplace-prd.md`) | Hermes | 10 min |

---

## What's blocked

| Blocker | Why | Unblock action |
|---|---|---|
| Pinecone MCP tools not loaded in current session | session needs reload after `hermes mcp add pinecone` | user: start a new chat, or `/reload-mcp` |
| `leadsniperai` Pinecone index not yet created | blocked by above | unblocks automatically next session |
| `gemini-2.5-flash` cost ceiling per pipeline run | not enforced at pipeline level | add cost gate to `run_pipeline` MCP tool |
| `veritas-developments` workspace uses default city `Kansas City` | hardcoded | parameterize or auto-derive from workspace |
| Contact-embedding model for Pinecone | need to decide on `llama-text-embed-v2` vs client-side | default to integrated inference; revisit if quality issues |

---

## Architecture decisions (locked)

| Decision | Choice | Why | Source |
|---|---|---|---|
| System of record | **Supabase** | RLS, joins, audit, real-time | user, 2026-10-11 |
| Semantic store | **Pinecone** (not Qdrant) | MCP already wired, free tier, integrated inference | user, 2026-10-11 |
| Local analytics | **DuckDB** | zero ops, fast, Parquet-native | already in use |
| Cloud DuckDB | **MotherDuck, opt-in** | not needed today | user, 2026-10-11 |
| Cross-layer format | **Parquet** | columnar, schema-on-read, universal | already in use |
| Contact embedding model | **`llama-text-embed-v2`** (Pinecone integrated) | no client-side model needed | user, 2026-10-11 |
| MCP tool prefix | `mcp__leadsniper__*` | legacy from 2026-08-22 build | server.py header |
| Pipeline promotion gate | `score >= threshold` for ≥1 opportunity type | controls Supabase write volume | icp_candidate_pipeline.py |

---

## Files this session created

| Path | Purpose |
|---|---|
| `wiki/projects/leadsniperai/MCP-TOOLS-REFERENCE.md` | 17 tools, costs, args, returns |
| `wiki/projects/leadsniperai/ARCHITECTURE.md` | 4-layer flow + integrity rules |
| `wiki/projects/leadsniperai/STATUS.md` | this file |
| `LeadSniper-3.0/scripts/leadsniper/` (branch `hermes-lead-credit`) | v3.1 refactor package, 14 modules / 3,527 LOC |
| `LeadSniper-3.0/scripts/icp_candidate_pipeline.py` (shim) | legacy bridge from old signature to new package |
| `LeadSniper-3.0/README.md` (branch `hermes-lead-credit`) | new "Lead AI Operating Layer — Hermes" section |

## Files this session referenced (read-only)

| Path | Why |
|---|---|
| `~/.hermes/mcp_servers/leadsniper/server.py` (915 lines) | source of truth for 17 tool signatures |
| `~/.hermes/mcp_servers/leadsniper/README.md` | build history, replaced broken Go CLI on 2026-08-22 |
| `LeadSniper-3.0/scripts/icp_candidate_pipeline.py` | pipeline source — DuckDB + Parquet + Supabase |
| `LeadSniper-3.0/.local_tier/veritas-developments.duckdb` | existing staging data |
| `LeadSniper-3.0/.local_tier/spectra-holdings.duckdb` | existing staging data |
| `wiki/projects/leadsniperai/*.md` (8 files) | LeadSniper source docs to embed in Pinecone |
| `wiki/drafts/leadsniperai-*.md` (6 files) | LeadSniper source docs to embed in Pinecone |
| `wiki/projects/leadsniperai/integration-api-catalog.md` | routing rules (Exa, Serper, DataForSEO, etc.) |
| `wiki/projects/leadsniperai/cli-prd.md` | Qdrant reference (to deprecate) |
| `wiki/projects/leadsniperai/marketplace-prd.md` | Qdrant reference (to deprecate) |
| `~/.hermes/config.yaml` | MCP servers block (leadsniper entry verified) |

---

## Open questions for user — RESOLVED 2026-10-11

1. **Contact-embedding trigger** — **automatic on Supabase promotion, with `dry_run` flag** (mirrors `run_pipeline`).
2. **Pinecone namespace convention** — **one namespace per workspace** (e.g. `veritas-developments`, `spectra-holdings`). Easier offboarding.
3. **Qdrant PRDs cleanup** — **update in place** with a "Qdrant deprecated 2026-10-11 in favor of Pinecone" note. `cli-prd.md` and `marketplace-prd.md` to be patched this session.
4. **MotherDuck enablement** — **skipped**, no multi-machine need today. Re-evaluate when second laptop joins the work.

---

## Re-run instructions (next session)

```bash
# 1. Reload MCP tools (or new session)
/reload-mcp

# 2. Verify tools loaded
hermes mcp list | grep leadsniper
# Expect: leadsniper ... all ... ✓ enabled
hermes mcp list | grep pinecone
# Expect: pinecone ... all ... ✓ enabled

# 3. Create leadsniperai Pinecone index (one-time)
# Via MCP: mcp__pinecone__create-index-for-model(
#   name="leadsniperai",
#   cloud="aws", region="us-east-1",
#   embed={"model": "llama-text-embed-v2", "field_map": {"text": "text"}}
# )

# 4. Upsert 14 source files (12,308 lines, ~200-400 chunks)
# Use: mcp__pinecone__upsert-records with chunks from projects/leadsniperai/*.md + drafts/leadsniperai-*.md

# 5. Smoke test
# mcp__pinecone__search-records(
#   index="leadsniperai", query="what is the LeadSniper pipeline cost ceiling?",
#   top_k=5
# )
```

---

## Sign-off

- Architecture: designed 2026-10-11
- Source docs inventoried: 14 files, 12,308 lines
- Pipeline integration: 25% (DONE) + 25% (Pinecone) + 25% (Pinecone KB) + 25% (contact-embedding step)
- Owner approval: implicit via "yes" to design question 2026-10-11
- Next checkpoint: after Pinecone KB build + smoke test (next session)
