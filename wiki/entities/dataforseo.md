---
title: DataForSEO
type: entity
category: search-api
url: https://dataforseo.com
pricing: pay-per-use
status: active
status_notes: Paid account — sales@klicksmartai.com. No free tier.
tags: [entity, dataforseo, seo, serp, keyword-research, rank-tracking, backlinks, content-analysis, mcp, python]
related: [tavily, brave-search-mcp-server, serper, exa-labs]
last_reviewed: 2026-04-19

## Summary

DataForSEO provides comprehensive SEO and search data APIs covering SERP rankings, keyword volumes, competitor analysis, backlinks, and content metrics. **69 tools** in the MCP server. Massive data breadth — best for SEO/intent intelligence use cases.

## MCP Server

- **Package:** `dataforseo-mcp-server` (npm)
- **Version:** 2.8.9
- **Transport:** STDIO (npx)
- **Install:** `npx -y dataforseo-mcp-server`
- **Tools:** 69 total. Key tools below.

## Key Tools

### SERP — Google Organic
| Tool | Description |
|------|-------------|
| `serp_organic_live_advanced` | Live Google SERP data — rank, title, URL, description, breadcrumbs |
| `serp_organic_live_standard` | Standard organic results |
| `serp_locations` | Country/location codes for targeting |

### Keyword Research
| Tool | Description |
|------|-------------|
| `kw_data_google_ads_search_volume` | Monthly search volumes + CPC + competition per keyword |
| `kw_data_google_trends_explore` | Google Trends data — subregion interests, demographics |
| `dataforseo_labs_google_keyword_ideas` | Keyword ideas from seed keyword |
| `dataforseo_labs_google_related_keywords` | Related keyword suggestions |
| `dataforseo_labs_google_keyword_overview` | Full keyword metrics (volume, difficulty, CPC, search intent) |
| `dataforseo_labs_search_intent` | Classifies keyword intent (informational, transactional, navigational, commercial) |

### Rank & Competitor Intelligence
| Tool | Description |
|------|-------------|
| `dataforseo_labs_google_ranked_keywords` | All keywords a domain ranks for |
| `dataforseo_labs_google_competitors_domain` | Organic competitors of a domain |
| `dataforseo_labs_google_serp_competitors` | Domains competing in same SERP |
| `dataforseo_labs_google_historical_rank_overview` | Historical rank tracking |
| `dataforseo_labs_google_domain_rank_overview` | Domain authority metrics |

### Backlinks
| Tool | Description |
|------|-------------|
| `backlinks_summary` | Backlink overview for domain |
| `backlinks_bulk_backlinks` | Bulk backlink data |
| `backlinks_referring_domains` | Referring domains count + metrics |

### AI Optimization (unique differentiator)
| Tool | Description |
|------|-------------|
| `ai_optimization_llm_response` | Query Claude/GPT/Gemini/Perplexity via DataForSEO infrastructure |
| `ai_opt_llm_ment_search` | Track where your brand/keyword is mentioned in AI model responses |
| `ai_optimization_keyword_data_search_volume` | LLM search volume per keyword — how often AI models cite/use this keyword |

### Content & Technologies
| Tool | Description |
|------|-------------|
| `content_analysis_search` | Citation data per keyword |
| `domain_analytics_technologies_domain_technologies` | Tech stack detection (Shopify, Wix, etc.) |
| `business_data_business_listings_search` | Google Maps business listings |
| `on_page_instant_pages` | Instant page rendering + on-page data |

## Pricing

- **Model:** Pay-per-use (no monthly subscription required)
- **SERP data:** ~$0.001–$0.005 per result
- **Keyword data:** ~$0.01–$0.05 per keyword
- **Account:** sales@klicksmartai.com (paid)

## Credentials

- **Username:** `sales@klicksmartai.com` (env: `DATAFORSEO_USERNAME`)
- **Password:** stored via `save_env_value()` (env: `DATAFORSEO_PASSWORD`)
- **Credentials saved to:** `~/.hermes/.env` via hermes_cli.config

## Wiring

- **Status:** Wired to Hermes
- **MCP server name:** `dataforseo`
- **Command:** `npx -y dataforseo-mcp-server`
- **Transport:** STDIO
- **Config file:** `~/.hermes/config.yaml` → `mcp_servers.dataforseo`

## Use Cases for KlickSmartAI

1. **HUBERT-X lead scoring** — Use `dataforseo_labs_search_intent` to classify broker search intent before outreach
2. **Keyword intelligence** — `kw_data_google_ads_search_volume` for exact monthly volumes on insurance terms
3. **Competitor gap analysis** — `dataforseo_labs_google_competitors_domain` to find broker marketing agencies
4. **AI mention tracking** — `ai_opt_llm_ment_search` to see where Insurance Direct Canada is cited in AI responses (new channel)
5. **Rank tracking** — Monitor IDC.com for target insurance keywords
6. **SERP snapshot** — `serp_organic_live_advanced` for real-time Google rankings
