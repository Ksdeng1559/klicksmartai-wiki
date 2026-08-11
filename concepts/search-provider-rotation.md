---
title: Search Provider Rotation
created: 2026-08-11
updated: 2026-08-11
type: pattern
tags: [pattern, search, provider, brave, serper, exa, tavily, parallel]
sources: []
confidence: high
---

# Search Provider Rotation

How to choose which search API for which query, and what to do when one
exhausts its quota.

## Default rotation
1. **Brave** — default for general web search.
2. **Serper** — Google SERP results. Use for Google-specific needs or when
   Brave fails.
3. **Exa** — deep semantic search; use for people research, company research,
   CDFI/investment intelligence (per Spectra workflow).
4. **Parallel.ai** — has its own dedicated skill (`parallel-ai-search`); use
   for AI-orchestrated multi-source research. ~2 keys available (rotated).
5. **Tavily** — LLM-optimized search results, useful for agent deep research.
6. **SerpApi** — Local pack / map results. 250/month hard cap, use sparingly.

## Failure handling
- **Never retry an exhausted provider.** Rotate to the next.
- If all rotated providers fail: surface the failure to the user, don't fake it.
- `wiki-query` uses `qwen2.5:3b` (local Ollama) for synthesis — separate from
  primary search.

## Sources / skills
- `~/.hermes/skills/research/tavily-*` — Tavily family (search, extract, crawl, research, map)
- `~/.hermes/skills/research/exa-*` — Exa family (company, financial, lead-gen, news, paper)
- `~/.hermes/skills/research/parallel-ai-search` — Parallel.ai CLI
- `mcp__brave_search__*` — Brave MCP
- `mcp__parallel_ai__*` — Parallel.ai MCP

## When to use which (decision tree)
- Need a list of URLs from one source → Tavily `map` or crawl
- Need one URL extracted as clean markdown → web_extract / Tavily `extract`
- Need citations for an answer → Tavily `research` or Parallel `deep research`
- Need people profiles → Exa `people-search`
- Need company intel → Exa `company-research` or `exa-company-research`
- Need Google SERPs / local pack → Serper, SerpApi (local only)
- Default / no special need → Brave

## See also
- [[Api-Keys-And-Providers]]
- [[Model-Routing]]
- [[Gtm-Enrichment-Hitl-Gate]]