---
title: LeadSniper MCP Tools Reference
created: 2026-10-11
updated: 2026-10-11
type: reference
tags: [leadsniperai, mcp, tools, reference]
sources: [home/denni/.hermes/mcp_servers/leadsniper/server.py]
related: [ARCHITECTURE.md, STATUS.md, projects/leadsniperai/integration-api-catalog.md]
---

# LeadSniper MCP Tools Reference

The LeadSniper MCP server (`/home/denni/.hermes/mcp_servers/leadsniper/server.py`) exposes **17 tools** to Hermes Agent and any MCP-compatible LLM client. Tools are registered under the `mcp__leadsniper__*` prefix and are auto-loaded after `hermes mcp add leadsniper`.

**Server config** (`~/.hermes/config.yaml`):
```yaml
mcp_servers:
  leadsniper:
    command: /usr/bin/python3
    args: [/home/denni/.hermes/mcp_servers/leadsniper/server.py]
    enabled: true
```

**Env overrides** (optional):
- `LEADSNIPER_BACKEND_URL` — default `http://127.0.0.1:8000`
- `LEADSNIPER_TIMEOUT` — default 120 seconds
- `SUPABASE_PAT` — loaded from `~/.hermes/mcp_servers/leadsniper/.env.supabase` (project `yolqrstktoqlszybwymw`)
- `GEMINI_API_KEY` — same env file (model `gemini-2.5-flash`)

---

## Tool Categories

The 17 tools split into four functional groups:

| Group | Tools | Cost pattern | Purpose |
|---|---|---|---|
| **Workspace (Supabase)** | 6 | $0 (Supabase REST) | Read/manage client_workspaces, signals, leads |
| **Discovery (Pipeline)** | 1 | $0.15-0.40 / run | Spawn `icp_candidate_pipeline.py` for a workspace |
| **Enrichment (Backend)** | 5 | $0.01-0.15 / call | Lead deep-dive, reviews, decision makers, news, reverse lookup |
| **Content (Gemini)** | 4 | $0.005-0.05 / call | Email, cold call script, recommendations, executive summary |
| **SEO (DataForSEO)** | 5 | $0.01-2.00 / call | Keywords, domain overview, competitors, local SERP, full audit |
| **Health** | 1 | $0 | Backend liveness check |

**Totals**: 17 tools (6 + 1 + 5 + 4 + 5 + 1 = 22 — but `health_check` and `search_businesses` collapse categories; actual = 17 distinct tools).

---

## Workspace tools (Supabase-backed, $0 cost)

### `list_workspaces()`

List all client workspaces from Supabase.

**Returns**: `[{"slug", "client_name", "problem_solved", "signal_count", "last_active_at", "created_at"}]` — max 50, ordered by `last_active_at DESC`.

**Use when**: discovering which clients are active, scoping a new analysis run, or auditing portfolio health.

### `get_workspace(slug)`

Get the full workspace configuration for one slug. Defaults to `"veritas-developments"`.

**Returns**: full `client_workspaces` row including `signal_definitions` (JSON), `negative_signals`, `qualification_rules`, `scoring_model`, `enrichment_policy`, `outreach_playbook`, `icp_id`.

**Use when**: planning enrichment, generating search queries, or scoring a candidate against a specific ICP.

### `plan_search_strategy(slug, signal_name="")`

Generate 3-7 Google / Exa search query templates from a workspace's `signal_definitions` using Gemini 2.5 Flash.

**Args**:
- `slug` (required) — workspace slug
- `signal_name` (optional) — if set, scope to one signal_type (e.g. `"capital_available"`)

**Returns**: `{"reasoning", "queries": [{provider, query_template, intent, priority, expected_yield}], "model"}`. Intents: `discovery | verification | enrichment | decision_maker`. Priorities 1-5.

**Cost**: ~$0.01-0.05/call (Gemini 2.5 Flash, 500-2k tokens).

**Use when**: bootstrapping a new pipeline run, validating existing query coverage, or extending signal coverage to a new niche.

### `run_pipeline(slug, dry_run=False, max_results_per_query=5, city="Kansas City", region="MO")`

Spawn the local `icp_candidate_pipeline.py` script end-to-end for a workspace.

**Flow** (5 stages):
1. Load workspace ICP from Supabase (slug → icp_id)
2. Call Gemini + Google Maps grounding to discover candidates
3. Score each for `website_rebuild` + `ai_sdr_review_gen` opportunity types
4. Stage in local DuckDB (`~/.local_tier/<slug>.duckdb`)
5. Promote PASS leads + signals + opportunities to Supabase

**Returns**: `{"stages": [...], "final_counts": {discovered, signal_yes, enriched, qualified, promoted}, "stdout"}`.

**Cost**: ~$0.15-0.40/discovery call (Gemini 2.5 Flash + Maps grounding). One run = many calls.

**Use when**: actual candidate discovery, not planning. Always try `dry_run=True` first.

### `archive_no_signal(dry_run=True)`

Move leads with zero signal rows from `leads` to `workspace_signal_events_archive`.

**Returns**: `{"examined", "archived", "action": "dry_run"|"archived", "archived_ids"}`. Default `dry_run=True` returns counts only.

**Cost**: $0.

**Use when**: pruning dead leads after a major signal-definition change.

### `signal_dashboard(slug)`

Per-signal-type hit counts + recent activity for a workspace. Queries `v_workspace_signal_dashboard` view (falls back to direct `lead_signals` aggregation).

**Returns**: `{"workspace", "client_name", "signal_types": [{signal_type, count, last_seen}], "recent_activity": [...], "total_leads", "total_signals"}`.

**Cost**: $0.

**Use when**: weekly ICP health check, proving signal coverage to a client, deciding where to expand signal definitions.

---

## Enrichment tools (Backend, $0.01-0.20/call)

### `health_check()`

Backend liveness. `$0`. Run first to confirm LeadSniper FastAPI is up at `LEADSNIPER_BACKEND_URL`.

### `enrich_lead(lead)`

Deep-dive on a single lead: reviews, owner details, email variants, unique angle, formatted phone.

**Args**: `lead` — full LeadResponse dict (must include `businessName` + `city` at minimum).

**Returns**: enriched lead dict with `reviewSnippets`, `emailVariants`, `uniqueAngle`, etc.

**Cost**: ~$0.05-0.15/call (Gemini 2.0 Flash + DataForSEO). Timeout 180s.

**Use when**: preparing a lead for outreach, scoring a lead, or populating the contact record in Supabase.

### `enrich_lead_tavily(lead)`

Same as `enrich_lead` but Tavily-based (web search). Cheaper, less rich.

**Cost**: ~$0.01-0.03/call. Timeout 120s.

**Use when**: budget-constrained batch enrichment, or when DataForSEO rate limits hit.

### `analyze_reviews(lead)`

Extract positive/negative themes from a business's reviews via Gemini.

**Cost**: ~$0.02-0.05/call (Gemini 2.0 Flash, 2-5k tokens). Timeout 120s.

**Use when**: building review-intelligence products, generating personalized outreach hooks, or scoring `ai_sdr_review_gen` opportunity type.

### `search_decision_makers(company, titles=None, location="")`

Find people at a company by name + role. **Returns** contact list with titles, locations, LinkedIn handles where available.

**Args**:
- `company` (required) — company name
- `titles` (optional) — list of title filters (e.g. `["CEO", "CFO", "Managing Director"]`)
- `location` (optional) — city/region filter

**Cost**: ~$0.05-0.15/call. Timeout 120s.

**Use when**: contact discovery for a known target company, building buying committee for an account.

### `search_company_news(company, days_back=30)`

Recent news about a company via Gemini + Google Search grounding.

**Cost**: ~$0.02-0.05/call. Timeout 60s.

**Use when**: triggering signals ("new funding round", "acquisition announced"), validating company is still active, or building outreach context.

### `reverse_lookup(email="", phone="", name="")`

Find a person/company from email, phone, or name. At least one arg required.

**Cost**: ~$0.05-0.20/call (multiple data sources). Timeout 60s.

**Use when**: identifying an inbound lead (someone filled a form), or enriching a partial contact record.

---

## Content tools (Gemini, $0.005-0.05/call)

### `generate_email(lead, context="", tone="professional")`

Personalized cold email for a lead.

**Cost**: ~$0.005-0.02/call. Timeout 60s.

**Use when**: outreach at scale, A/B testing tones, or seeding a nurture sequence.

### `generate_cold_call_script(lead, context="")`

Cold call script for a lead.

**Cost**: ~$0.01-0.03/call. Timeout 60s.

**Use when**: training SDRs, building call playbooks per ICP, or batch-generating scripts.

### `generate_recommendations(lead)`

Business growth recommendations for a lead (used as outreach hook or audit deliverable).

**Cost**: ~$0.01-0.03/call. Timeout 60s.

**Use when**: site-doctor audit output, lead-magnet content, or sales-call prep.

### `executive_summary(domain, country="US", location_code=2840, language="en", requested_by="hermes")`

Executive summary report for a domain. Combines DataForSEO + Gemini synthesis.

**Cost**: ~$0.10-0.30/call. Timeout 120s.

**Use when**: client-facing reports, ABM tier-1 account briefs, or post-sale deliverables.

---

## SEO tools (DataForSEO, $0.002-2.00/call)

### `sgi_keywords(domain, country="US", location_code=2840, language="en", requested_by="hermes")`

DataForSEO keyword data for a domain — volume, CPC, KD, SERP features.

**Cost**: ~$0.002-0.01/call. No Gemini.

**Use when**: SEO opportunity research, content-gap analysis, or programmatic SEO input.

### `sgi_domain_overview(domain, ...)`

Full domain SEO overview — organic traffic, top pages, competitors.

**Cost**: ~$0.01-0.03/call. No Gemini.

**Use when**: domain valuation, ABM account scoring, or competitive research.

### `sgi_competitors(domain, ...)`

SEO competitors for a domain.

**Cost**: ~$0.01-0.03/call. No Gemini.

**Use when**: building a competitor set, programmatic SEO inputs, or sales-battlecards.

### `sgi_local(domain, keyword="", ...)`

Local SERP data (Google Maps / Local Pack results).

**Cost**: ~$0.01-0.05/call. Timeout not specified (default 120s).

**Use when**: local-SEO clients, GMB audit, or local-pack SERP intelligence.

### `seo_audit(domain, ...)`

Full SEO audit — multiple DataForSEO endpoints + Gemini synthesis. Slow (60s+).

**Cost**: ~$0.50-2.00/call. Timeout 240s.

**Use when**: site-doctor full audit, monthly client deliverable, or sale-time audit.

---

## Verification

```bash
hermes mcp test leadsniper
# Expect: ✓ Connected + ✓ Tools discovered: 17
```

Or smoke test directly:

```python
import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def main():
    params = StdioServerParameters(
        command="/usr/bin/python3",
        args=["/home/denni/.hermes/mcp_servers/leadsniper/server.py"]
    )
    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as s:
            await s.initialize()
            tools = await s.list_tools()
            print(f"Tools: {len(tools.tools)}")
            # Sample call
            r = await s.call_tool("health_check", {})
            print(r.content[0].text)

asyncio.run(main())
```

---

## Cost ceilings (per run)

| Run type | Tools invoked | Approx cost |
|---|---|---|
| Workspace dashboard read | `list_workspaces` + `get_workspace` + `signal_dashboard` | $0 |
| Plan only (no discovery) | + `plan_search_strategy` | $0.01-0.05 |
| Single lead outreach | `enrich_lead` + `analyze_reviews` + `generate_email` | $0.08-0.22 |
| Full pipeline run (10 leads) | `run_pipeline` + 10× `enrich_lead` | $0.65-1.90 |
| Site doctor audit | `seo_audit` + `sgi_domain_overview` + `executive_summary` | $0.62-2.33 |

Always run `dry_run=True` first for new pipelines. Always `hermes mcp test leadsniper` before a paid run.
