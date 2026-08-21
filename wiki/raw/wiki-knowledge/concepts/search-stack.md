---
title: Search Stack
created: 2026-08-06
updated: 2026-08-06
type: concept
category: internal-infrastructure
tags: [concept, search, search-api, hermes, infrastructure, routing]
related: [entities/tavily, entities/exa-labs, entities/serper, entities/brave-search-mcp-server, entities/dataforseo]
---

# Search Stack

Hermes (KlickSmartAI) search engine inventory, capabilities, and routing. Condensed from config.yaml + verified live 2026-08-05/06.

## Native web search

- **`web_search` tool** — backend: **Brave Search** (default). Routine lookups, operator support (`site:`, `filetype:`, `-term`). Override via `search_backend`.

## MCP-connected engines (all enabled in config.yaml)

| Engine | Key | Capabilities |
|--------|-----|--------------|
| **Brave** | `brave-search` MCP | `brave_web_search`, `brave_local_search` |
| **Exa** | `exa` MCP | `deep_search_exa` — deep semantic search (CDFI/investment/deep tier) |
| **Tavily** | `tavily` MCP | `tavily_search`, `tavily_extract`, `tavily_crawl`, `tavily_map`, `tavily_research` |
| **Parallel.ai** | `parallel-ai` MCP + Python SDK + CLI | Search (turbo/basic/advanced), Extract (URL→markdown), Task (deep research), Task groups (batch), Monitor (scheduled watchlists), Entity Search + FindAll (CLI), Enrich (CLI) |
| **DataForSEO** | `dataforseo` MCP (91 tools) | SERP live (Google organic/news/YouTube), keyword data/volume/difficulty, backlinks, domain analytics, on-page, merchant, business listings — SEO/SERP tier |
| **Firecrawl** | `firecrawl` MCP | `scrape`, `crawl`, `extract`, `search`, `map` |
| **NotebookLM** | `notebooklm` MCP | research notebooks, sources, queries |
| **yt-dlp** | `yt-dlp` MCP | YouTube search, video info, playlists, subtitles |

## Skill/API-level (keys via skills)

| Engine | Role |
|--------|------|
| **Serper** (Google) | org/faith/political-angled Google results — secondary after Brave |
| **SerpApi** | local search (~250 credits) — local SEO tier |
| **Wikipedia API** | fallback when search engines credit-exhausted |
| **SearXNG** | private instance skills exist; not currently a configured server |

## Routing (order of preference)

**Brave (default) → Serper (Google/org/faith/political) → Exa (deep/CDFI/investment) → Parallel.ai (LLM-optimized excerpts + deep task research).**

- Never retry a credit-exhausted engine — rotate.
- Wikipedia API as last fallback.
- SerpApi for local, DataForSEO for SERP/keyword/backlink work.

## Parallel vs Exa/Tavily/Serper (decision 2026-08-05)

- **Parallel CAN replace Exa + Tavily for LLM-grounding research** (Search+Extract+Task = same tier, one key, one credit pool).
- **Parallel CANNOT replace Serper/SerpApi/DataForSEO** — SERP APIs return structured results (positions, local packs, ads, keyword data); Parallel returns LLM excerpts. Needed for rank tracking, local SEO audits, competitive ad extraction, keyword work.
- **Decision:** keep the rotation. Parallel stays one node, not a replacement.
- SDK v1.1.0 gotchas: `findall`/`entity_search` NOT in Python SDK (CLI/MCP only); `objective` optional (only `search_queries` required); no relevance scores, no relative time_range, no topic filter, no images.

## Related

- [[entities/tavily]] · [[entities/exa-labs]] · [[entities/serper]] · [[entities/brave-search-mcp-server]] · [[entities/dataforseo]]
- Hermes skill: `parallel-ai-search` (full migration mapping + verified SDK surface)
