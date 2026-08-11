---
title: tavily-agent-skills (skill)
created: 2026-08-11
updated: 2026-08-11
type: entity
tags: [entity, skill, tavily, search, research, deep]
sources: []
confidence: high
---

# tavily-agent-skills (skill)

**Third-most-loaded skill (283 uses).** The Tavily family — AI-optimized
search, extract, crawl, deep research, site-mapping, and answer synthesis.

## Source
`~/.hermes/skills/research/tavily-agent-skills/`

## Tools (via Tavily MCP)
- `mcp__tavily__tavily_search` — search with AI-optimized results.
- `mcp__tavily__tavily_extract` — clean markdown from specific URLs.
- `mcp__tavily__tavily_crawl` — extract content from multiple pages.
- `mcp__tavily__tavily_map` — list URLs on a site without extracting.
- `mcp__tavily__tavily_research` — comprehensive AI-powered research with
  citations.

## When to use
- Quick research where you want LLM-curated snippets.
- Citation-backed research outputs.
- Mapping the URL structure of a domain before deep crawling.
- Extracting clean markdown when web_extract isn't enough.

## When NOT to use (in Dennis's stack)
- Spectra county research — the active search rotation is
  Brave → Serper → Exa. Tavily is **deprecated for Spectra** (credits exhaust).
- Local / map pack results — use SerpApi (250/month cap).

## Failure modes
- `answer=null` response — research step fired but synthesis didn't run.
  Heartbeat sentinel pattern: write the briefing stub BEFORE the LLM step.
- Cron context: cannot use `cmd | python3` — write to file, parse separately.

## See also
- [[Search-Provider-Rotation]]
- [[Skill-B2b-Outreach]]