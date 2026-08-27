# SEO Service Catalog & API Cost Reference

> **For agents (not clients).** Per `audit-page-gate`, never copy these figures into client-facing reports. They are the internal cost awareness for **planning**, **HITL approval**, and **budget forecasting** — not for client consumption.

Generated 2026-08-27 from a sweep of 15 OpenSEO skills. Source-of-truth: `~/.hermes/skills/*/SKILL.md` Cost sections.

## How to use this

1. User asks for SEO work → run the **Plan** phase (`seo-enrichment-planner`)
2. Pick the relevant use-case below → walk **stack layers** (Plan → Discover → Enrich → Score → Outreach)
3. Each layer returns a `Cost Estimate` block — present to user, get approval, then execute
4. After execution, log actual cost vs planned in `_config/seo-audit-log.md`

## Provider balance check (first)

The OpenSEO MCP `whoami` returns credit usage. In self-hosted mode `creditsRemaining: null` — fall back to manual dashboard checks:

| Provider | Default credit pool | Dashboard |
|---|---|---|
| DataForSEO | Variable, ~$100 = 100k credits | dataforseo.com |
| Serper.dev | Pay-as-you-go, ~$50 = 1000 calls | serper.dev |
| On-Page.ai | Per-URL subscription | api.on-page.ai |
| Rank Tracker | Per-keyword monthly | `estimate_rank_tracker_cost` MCP tool |

If credits ≈ 0 for the relevant provider, **stop** and ask user to top up.

---

## Service catalog (16 services, by skill)

### Plan (always free)

| Service | Skill | MCP tool | Cost |
|---|---|---|---|
| Project setup | `openseo-project-intake` | `whoami`, `list_projects`, `create_project`, `get_project_context`, `update_project_context` | $0 |
| Cost planning | `seo-enrichment-planner` | n/a (orchestrator only) | $0 |
| Data export | `openseo-data-export` | n/a (DuckDB only) | $0 |

### Discover (cheap first)

| Service | Skill | MCP tool | Cost |
|---|---|---|---|
| PAA + social mining | `paa-demand-mining` | `run_paa_mining`, `get_paa_scan`, `get_social_threads` | ~$0.018/scan (Serper.dev) |
| Keyword research | `keyword-research` | `research_keywords`, `save_keywords`, `list_saved_keywords`, `get_keyword_metrics` | ~96 cr/seed (DataForSEO) |
| SERP intelligence | `serp-intelligence` | `get_serp_results`, `find_serp_competitors` | ~30-50 cr/run |
| Domain research | `domain-research` | `get_domain_overview`, `get_domain_keyword_suggestions`, `get_ranked_keywords`, `get_backlinks_overview`, `get_backlinks_profile` | ~10-50 cr/domain |
| Local SEO | `local-seo` | `search_local_businesses`, `get_business_profile`, `get_local_serp_results`, `get_local_rank_grid`, `get_google_business_questions` | ~10-50 cr/query |

### Enrich

| Service | Skill | MCP tool | Cost |
|---|---|---|---|
| Content optimization | `content-optimization` | *(no MCP tools — see skill)* | Dormant (no `run_content_scan` tool exists in fork) |

### Score

| Service | Skill | MCP tool | Cost |
|---|---|---|---|
| Site audit | `site-audit` | `run_site_audit`, `get_audit_status`, `get_audit_issues`, `get_audit_pages` | ~$0.03/page (DataForSEO) |
| Rank tracking | `rank-tracking` | `create_rank_tracker`, `add_rank_tracking_keywords`, `estimate_rank_tracker_cost`, `run_rank_tracker`, `get_rank_tracker`, `remove_rank_tracking_keywords` | Per-keyword monthly (see estimate tool) |

### Outreach / Reporting

| Service | Skill | MCP tool | Cost |
|---|---|---|---|
| Analytics reporting | `analytics-reporting` | `get_search_console_performance`, `get_google_analytics_*`, `inspect_urls` | $0 (OAuth + storage cost only) |

### Cross-cutting

| Service | Skill | MCP tool | Cost |
|---|---|---|---|
| Competitor profiling | `competitor-profiling` | (composite; uses `domain-research` + `serp-intelligence`) | Sum of underlying costs |
| Client audit (gateway) | `audit-page-gate` | n/a (skill only) | $0 |
| Onboarding | `client-onboarding-sprint` | n/a (orchestrator only) | $0 |

---

## Cost reference (verified 2026-08-26/27)

### Per-tool costs

| Tool | Cost | Provider |
|---|---|---|
| `research_keywords` | ~96 credits/seed (1-5 seeds/call) | DataForSEO |
| `find_serp_competitors` | ~50 cr/run | DataForSEO |
| `get_domain_keyword_suggestions` | ~10 cr/call (free preview if cached) | DataForSEO |
| `get_serp_results` | ~30 cr/run (1-10 keywords) | DataForSEO |
| `get_local_serp_results` | ~30 cr/run | DataForSEO |
| `get_local_rank_grid` | ~50 cr/run (N×N grid) | DataForSEO |
| `search_local_businesses` | ~10 cr/query | DataForSEO |
| `get_domain_overview` | ~30 cr/domain | DataForSEO |
| `get_ranked_keywords` | ~30 cr/page | DataForSEO |
| `get_backlinks_overview` | ~30 cr/domain | DataForSEO |
| `get_backlinks_profile` | ~50 cr/domain | DataForSEO |
| `run_site_audit` | ~$0.03/page (crawled pages) | DataForSEO |
| `run_paa_mining` | ~$0.018/scan | Serper.dev |
| `get_social_threads` | ~$0.01-0.05/source | Serper.dev (multi-source) |
| `run_content_scan` | n/a (tool does not exist in fork) | On-Page.ai (intended, dormant) |

### Recurring costs

| Service | Recurrence | Rate |
|---|---|---|
| Rank tracker (manual) | 0 | $0 |
| Rank tracker (daily) | 30 checks/mo | ~$0.02-0.05/keyword/mo |
| Rank tracker (weekly) | 4 checks/mo | ~$0.003-0.008/keyword/mo |
| Rank tracker (bi-weekly) | 2 checks/mo | ~$0.002-0.004/keyword/mo |

Mobile + desktop doubles the cost.

---

## Cost models by provider

| Model | Examples | Notes |
|---|---|---|
| Per-credit (DataForSEO) | research_keywords, get_serp_results, site audits | Variable cost; check balance first |
| Pay-as-you-go (Serper.dev) | PAA mining, social threads | Cheap, low-volume |
| Per-URL subscription (On-Page.ai) | content_scan (intended) | Not implemented in OpenSEO fork |
| Per-keyword monthly (Rank Tracker) | rank tracking | Recurring; always start manual |

---

## Worked cost estimates (per use-case)

### New client audit (typical)

| Phase | Tool | Calls | Est. cost |
|---|---|---|---|
| Discover | `run_paa_mining` | 1 scan | $0.018 |
| Discover | `research_keywords` | 5 seeds | ~480 cr |
| Discover | `get_serp_results` | 3 runs | ~90 cr |
| Discover | `get_domain_overview` | 5 domains | ~150 cr |
| Score | `run_site_audit` (pilot, 5 pages) | 5 pages | ~$0.15 |
| Score | `run_site_audit` (full, 100 pages) | 100 pages | ~$3.00 |
| Score | `create_rank_tracker` | 25 keywords | $0 setup + ~$0.50/mo recurring |

**Pilot cost: ~$0.30 of credits (5 pages + 1 PAA scan + 1 SERP run).**
**Full audit cost: ~$4 + 25-keyword tracker = ~$4.50 first month, ~$0.50/mo after.**

### Monthly recurring

| Component | Monthly cost |
|---|---|
| Rank tracker (25 keywords, weekly) | ~$0.50 |
| Search Console + GA reporting | $0 |
| PAA mining (4×/month) | ~$0.07 |
| **Total** | **~$0.57/mo** |

### High-volume (active engagement)

| Component | One-time | Monthly |
|---|---|---|
| 5 client audits/month | ~$22.50 | n/a |
| 20 rank trackers × 25 keywords | $0 | ~$10 |
| PAA + social mining (10×/month) | n/a | ~$0.18 |
| **Total** | ~$22.50 | ~$10.18 |

---

## BYO key model (all providers)

All OpenSEO providers are **Bring Your Own Key**:

| Provider | Env var | Source | Status |
|---|---|---|---|
| DataForSEO | `DATAFORSEO_API_KEY` | `~/.hermes/secrets/dataforseo-api-key.txt` | ✅ Wired |
| Serper.dev | `SERPER_API_KEY` | `~/.hermes/secrets/serper-api-key.txt` | ✅ Wired |
| OpenRouter | `OPENROUTER_API_KEY` | `~/.hermes/secrets/openrouter-api-key.txt` | ✅ Wired |
| On-Page.ai | `ONPAGE_API_KEY` | `~/.hermes/secrets/onpage-api-key.txt` | ⚠️ Wired (env), tools not implemented |
| Google OAuth | `GOOGLE_CLIENT_ID` + `GOOGLE_CLIENT_SECRET` + `BETTER_AUTH_SECRET` | Self-host docs | ❌ Not configured (Search Console/GA4 disabled) |

When a key is missing, MCP tools respond with "module disabled" or auth errors. **Module = $0 when disabled.**

---

## Disclosure rule (CRITICAL — per `audit-page-gate`)

**Never include the following in client-facing artifacts:**

- Cost per issue, per page, or per phase
- Tool/vendor names (DataForSEO, Serper, On-Page.ai, OpenRouter)
- API credit estimates or API provider costs
- Specific implementation sequencing or time estimates per phase
- Internal skills catalog or workflow details

**Acceptable phrasing:**

| ❌ Don't say | ✅ Do say |
|---|---|
| "We use DataForSEO at $0.03/page" | "Our audit process is data-driven and industry-validated" |
| "Estimated 480 credits" | "Our research process validates keyword data with the search engines themselves" |
| "Phase 1 fixes 110 issues in 7 days" | "We typically resolve the foundation layer in the first week" |
| "On-Page.ai score: 73/100" | "Content quality score: 73/100" (no vendor name) |

---

## Update policy

- **Re-verify quarterly** — provider pricing changes
- **Re-verify on skill edit** — any skill that changes its MCP tools should update its Cost section
- **Source of truth: each skill's `## Cost` section** — this reference doc is generated, not authoritative

**Last verified: 2026-08-27**
