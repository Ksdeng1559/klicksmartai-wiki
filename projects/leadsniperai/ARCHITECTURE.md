---
title: LeadSniperAI Architecture — DuckDB → Parquet → Pinecone → Supabase
created: 2026-10-11
updated: 2026-10-11
type: architecture
tags: [leadsniperai, architecture, duckdb, pinecone, supabase, pipeline]
sources: [mcp_servers/leadsniper/server.py, LeadSniper-3.0/scripts/icp_candidate_pipeline.py]
related: [MCP-TOOLS-REFERENCE.md, STATUS.md, projects/leadsniperai/integration-api-catalog.md]
---

# LeadSniperAI Architecture

LeadSniperAI is a **four-layer lead-enrichment system** where each layer has a single, non-overlapping job. The pipeline discovers → stages → enriches → records, with one tool/format per stage.

```
┌─────────────────────────────────────────────────────────────────────┐
│ Layer 1: DISCOVERY (Gemini + Maps + Search)                        │
│ Tool: mcp__leadsniper__run_pipeline / search_businesses            │
│ Input: workspace.signal_definitions + city/region                  │
│ Output: candidate list (name, city, niche, source URL)             │
│ Why: this is the only expensive step; budget gate it               │
└─────────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────────┐
│ Layer 2: STAGING (DuckDB + Parquet)                                 │
│ Tool: icp_candidate_pipeline.py (local)                             │
│ Input: candidates from Layer 1                                      │
│ Output: ~/.local_tier/<slug>.duckdb + per-response .parquet files  │
│ Schema: companies, contacts, signals, opportunities, request_log   │
│ Why: cheap to query, fast to dedupe, audit-friendly                │
└─────────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────────┐
│ Layer 3: SEMANTIC RECALL (Pinecone)                                 │
│ Tool: mcp__pinecone__upsert-records / search-records               │
│ Input: contact "about + signals + role" text                       │
│ Output: vector index `leadsniperai` (per namespace per workspace)  │
│ Why: cross-contact similarity, intent recall, contact graph        │
└─────────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────────┐
│ Layer 4: SYSTEM OF RECORD (Supabase)                                │
│ Tool: mcp__supabase__* / leadsniper MCP sb_query                   │
│ Input: scored/qualified leads from Layer 2 + 3                     │
│ Output: leads, lead_signals, lead_opportunities, contacts,          │
│         companies, workspace_signal_events_archive                  │
│ Why: source of truth for billing, audit, client reporting          │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Layer 1 — Discovery (Gemini + Maps + Search)

**Tools**: `mcp__leadsniper__run_pipeline`, `plan_search_strategy`, `search_businesses` (backend route)

**Input**: workspace slug → resolved from `client_workspaces` table in Supabase → `icp_id` → `signal_definitions` JSON.

**Output**: candidate list — each candidate has `businessName`, `city`, `niche`, `sourceUrl`, `score` for `website_rebuild` + `ai_sdr_review_gen` opportunity types.

**Cost gate**: always `dry_run=True` first. Cost per discovery call: $0.15-0.40 (Gemini 2.5 Flash + Maps grounding). A 10-lead run is $1.50-4.00 just for discovery.

**Why Gemini**: grounding + Maps lets the model synthesize "plumber in Lee's Summit MO with 4.2★" without us hand-coding the local-pack parser.

---

## Layer 2 — Staging (DuckDB + Parquet)

**Tools**: `icp_candidate_pipeline.py` (called via `run_pipeline` MCP tool)

**Storage**:
- `~/.local_tier/candidates.duckdb` (global, deprecated)
- `~/.local_tier/<slug>.duckdb` (per workspace — `veritas-developments.duckdb`, `spectra-holdings.duckdb`)
- Per-API-response Parquet files: `request_params`, `response_parquet`, `fetched_at`, `byte_size` columns in the `request_log` table

**Schema** (per `icp_candidate_pipeline.py`):
- `companies` — discovered businesses
- `contacts` — people at those companies
- `signals` — evidence rows (signal_type, source_url, observed_at)
- `opportunities` — `website_rebuild` / `ai_sdr_review_gen` scored rows
- `request_log` — every external API call (params, response parquet, byte size, fetched_at)

**Why DuckDB**:
- SQL with a fast columnar engine
- Zero ops (just a file)
- Direct Parquet read/write for handoffs to other layers
- Optional MotherDuck attach for cloud persistence if multi-machine access is needed

**Why Parquet**: columnar + compressed, schema-on-read, every analytics tool reads it. The `request_log` table stores the raw API response as Parquet so we can re-process without re-paying the API.

**Why NOT Supabase here**: this is pre-scoring, noisy, and high-churn. Don't pollute the system of record with candidates that may never qualify. Stage in DuckDB until they PASS scoring.

**When to promote to Supabase**: only when `score >= threshold` for at least one opportunity type. Pipeline does this automatically via `supabase_sync.py`.

---

## Layer 3 — Semantic Recall (Pinecone)

**Tools**: `mcp__pinecone__upsert-records`, `search-records`, `cascading-search`, `rerank-documents`

**Index**: `leadsniperai` (serverless, `aws/us-east-1`, `llama-text-embed-v2`, 1024d cosine).

**Namespaces** (one per workspace or contact type — pick a convention):
- `production` — operational records
- `<workspace-slug>` — per-workspace semantic recall (e.g. `veritas-developments`, `spectra-holdings`)

**What to embed**: contact "about + signals + role" text composed at enrichment time, e.g.

```python
def build_contact_text(contact: dict) -> str:
    parts = [
        f"{contact.get('full_name', '')} — {contact.get('title', '')}",
        f"at {contact.get('company_name', '')}",
        f"({contact.get('city', '')}, {contact.get('region', '')})",
        f"Signals: {'; '.join(contact.get('signal_types', []))}",
        f"About: {contact.get('about', '')}",
    ]
    return "\n".join(p for p in parts if p and p.strip())
```

**Record id** = `supabase.contact_id` (so we can join back).

**Metadata** = `{workspace_slug, contact_id, company_id, signal_types[], opportunity_types[], last_upserted}` — for filtering.

**Why Pinecone over Qdrant**:
- The PRDs (`cli-prd.md`, `marketplace-prd.md`) mention Qdrant; we chose **Pinecone** because (a) we just wired the MCP, (b) integrated inference means no client-side embedding model, (c) free tier covers the lead-volume range we have.

**Pinecone vs MotherDuck**:
- Pinecone = semantic similarity search (this layer)
- MotherDuck = managed DuckDB (cloud version of Layer 2)
- Use both; they don't overlap. MotherDuck would replace the local DuckDB files if you need multi-machine access.

---

## Layer 4 — System of Record (Supabase)

**Tools**: `mcp__supabase__*` (28 tools), plus the `leadsniper` MCP's `sb_query` helper.

**Project**: `yolqrstktoqlszybwymw`

**Tables**:
- `client_workspaces` — one row per client/ICP
- `icp_profiles` — reusable ICPs
- `leads` — promoted candidates (PASS scoring)
- `companies` — canonical company record
- `contacts` — people (linked to companies)
- `lead_signals` — every signal observation (joinable to leads)
- `lead_opportunities` — `website_rebuild` / `ai_sdr_review_gen` scored
- `outreach_attempts` — every email/call sent
- `workspace_signal_events_archive` — archived leads (no signal)

**Why Supabase is the system of record**:
- Row-level security for multi-tenant access
- Postgres = joins, views, RLS, audit logs
- Real-time subscriptions for UI
- Auth for the LeadSniper web app

**No autonomous writes**: per the global Hermes rule, all client-facing Supabase writes go through `mcp__leadsniper__run_pipeline` (which the user approves via `dry_run` review). Direct ad-hoc inserts are blocked at the policy level.

---

## End-to-end flow (one lead)

```
1. USER: "find 10 leads in Lee's Summit MO for Veritas"
2. HERMES: mcp__leadsniper__plan_search_strategy("veritas-developments")
3. USER: "approved"
4. HERMES: mcp__leadsniper__run_pipeline("veritas-developments",
                                         dry_run=True, city="Lee's Summit",
                                         region="MO", max_results_per_query=5)
   → returns 10 candidate records; DuckDB staged; no Supabase writes yet
5. USER: "promote the 4 with signals"
6. HERMES: runs pipeline again with dry_run=False
   → 4 leads promoted to Supabase
7. HERMES: for each contact, builds "about + signals + role" text,
            calls mcp__pinecone__upsert-records
   → 4 records in Pinecone namespace "veritas-developments"
8. HERMES: mcp__leadsniper__enrich_lead(lead) for each → review snippets, emails
9. HERMES: mcp__leadsniper__generate_email(lead, context=signals) → outreach
10. USER: "send the emails"
11. HERMES: drafts in Gmail, waits for approval, then sends
```

Total cost per lead: ~$0.50-1.20 (Gemini + DataForSEO + Tavily). 10 leads = $5-12. 100 leads = $50-120. Gates are real.

---

## Cross-layer integrity rules

1. **Supabase is the only system of record.** DuckDB is a cache; Pinecone is a search index. Re-derivable from Supabase, but Supabase wins ties.
2. **Parquet is the only cross-layer handoff format.** Never pass a candidate row from DuckDB to Pinecone as JSON; emit Parquet, reload, embed, upsert. Same for analytics.
3. **Pinecone record id = Supabase id.** Always. So a search hit can be joined back to the canonical contact.
4. **All Gemini calls are auditable.** Every prompt + response is stored in `request_log.response_parquet`. Cost tracking comes from `byte_size + token_estimate`.
5. **MotherDuck is opt-in.** Use only when multi-machine access to the same DuckDB is needed (currently: never).
6. **No autonomous writes to Supabase.** All writes route through `run_pipeline` (which the user reviews) or approved MCP tools. Direct DDL/DML is blocked at policy level.

---

## Tool-to-layer mapping

| Layer | Tool(s) | Cost | Storage |
|---|---|---|---|
| 1. Discovery | `mcp__leadsniper__run_pipeline`, `plan_search_strategy`, `search_businesses` | $0.15-0.40/call | in-memory → DuckDB |
| 1. Discovery | `mcp__leadsniper__search_company_news`, `search_decision_makers` | $0.05-0.15/call | DuckDB |
| 2. Staging | `icp_candidate_pipeline.py` (via `run_pipeline`) | $0 | `~/.local_tier/<slug>.duckdb` + Parquet |
| 2. Staging | (optional) MotherDuck | $0 (free tier) | cloud DuckDB |
| 3. Semantic | `mcp__pinecone__upsert-records`, `search-records` | $0 (free tier ≤100K vectors) | Pinecone `leadsniperai` |
| 4. Record | `mcp__leadsniper__sb_query` (via `list_workspaces`, `get_workspace`, `signal_dashboard`, `archive_no_signal`) | $0 | Supabase |
| 4. Record | `mcp__leadsniper__enrich_*` (writes to `leads` table) | $0.01-0.20/call | Supabase |
| 4. Record | `mcp__supabase__execute_sql` (admin) | $0 | Supabase |
| All | `mcp__leadsniper__health_check` | $0 | n/a |

---

## Migration path from current state

| Today | Target | Action |
|---|---|---|
| LeadSniper MCP server exists (17 tools) | keep | already done |
| DuckDB per-workspace staging exists | keep | already done |
| Supabase as system of record | keep | already done |
| Parquet for raw API responses | keep | already done |
| Pinecone not used | **enable** | new — upsert contact records per pipeline run |
| Qdrant mentioned in PRDs | **deprecate** | remove from PRDs; Pinecone is canonical |
| MotherDuck | **opt-in only** | document but don't enable until multi-machine need |
| Contact semantic recall | **build** | add upsert step to `run_pipeline` final stage |
| Pipeline doesn't write to Pinecone | **add** | one new step in `icp_candidate_pipeline.py` post-Supabase-sync |

Next session: build the contact-embedding step in the pipeline + the `leadsniperai` Pinecone KB from the 14 source files in `/home/denni/wiki/projects/leadsniperai/` + `/home/denni/wiki/drafts/leadsniperai-*`.
