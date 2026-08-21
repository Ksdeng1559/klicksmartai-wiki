---
title: Serper
type: entity
category: platform
url: https://serper.dev
pricing: paid
status: active
wired_to: hermes
mcp_server: serper
mcp_tools: [google_search, scrape]
tags: [entity, serper, google-search-api, serp-api, search-api, python, node-js, crewai, langchain]
related: [brave-search-mcp-server, exa-labs, duckduckgo-search]
last_reviewed: 2026-04-19
---

# Serper

**"The world's fastest and cheapest Google Search API."**

Serper is a Google Search API — delivers real Google search results (SERP data: titles, URLs, snippets, knowledge panels) at high speed and low cost. Not a consumer search engine — an API that proxies Google search for developers and AI applications.

**API Playground:** https://serper.dev/playground
**Status:** Live (green indicator on site)
**Free tier:** 2,500 queries free

---

## Pricing

| Plan | Price | Notes |
|------|-------|-------|
| Free | 2,500 queries | One-time, no card required |
| Pay-as-you-go | **$0.30 / 1,000 queries** | Unstructured |
| Volume | Custom | Contact for bulk pricing |

**Speed claim:** Results in **1–2 seconds**

---

## What It Returns

Serper returns **Google SERP data only** — no crawling, no full-page content:

- Organic search results (title, URL, snippet)
- Knowledge panels
- "People also ask" results
- Related searches
- Image results
- News results
- Ad results

---

## Integrations

Native integrations with the AI agent stack:
- **Haystack** (open-source NLP framework)
- **Jan AI** (local ChatGPT alternative)
- **CrewAI** (multi-agent orchestration)
- **LangChain** (LLM app framework)

---

## Comparison: Serper vs Brave vs Exa

| | Serper | Brave | Exa |
|--|--------|-------|-----|
| **What** | Google SERP data | Privacy search engine + API | Neural search + content retrieval |
| **Content** | Titles, URLs, snippets | Full search results | Full crawlable content |
| **Google results** | ✅ Real Google | ❌ Brave own index | ❌ Exa own index |
| **Speed** | 1-2 seconds | Medium | Medium |
| **Price** | $0.30/1K | Free (with API key) | Paid tiered |
| **MCP server** | ❌ | ✅ | ✅ |
| **Neural/hybrid search** | ❌ | ❌ | ✅ |
| **Full page content** | ❌ | ❌ | ✅ |
| **Company/news/tweet filters** | ❌ | Partial | ✅ |
| **Best for** | Ranking tracking, SEO, Google-dependent AI apps | Privacy-first search, multi-type search | AI content pipelines, deep research |

---

## For KlickSmartAI / HUBERT-X

**Use Serper when you need:**
- Real Google search results (not an alternative index)
- Fast, cheap SERP data for ranking checks or competitive Google analysis
- Integration with CrewAI/LangChain agent pipelines

**Use Brave/Exa when you need:**
- Full-page content retrieval (Exa)
- Multi-type search: images, video, news (Brave)
- Neural/hybrid search (Exa)
- MCP-native tool (Brave or Exa)

Serper fills the niche of **lightweight, fast, Google-specific** search at low cost.

---

## Source

- https://serper.dev
- https://serper.dev/playground
