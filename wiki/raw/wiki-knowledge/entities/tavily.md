---
title: Tavily
type: entity
category: platform
url: https://tavily.com
pricing: freemium
status: active
wired_to: hermes
mcp_server: tavily
mcp_tools: [tavily_search, tavily_extract, tavily_crawl, tavily_map, tavily_research]
tags: [entity, tavily, search-api, rag, ai-agents, deep-research, content-extraction, web-crawl, mcp, python, javascript]
related: [brave-search-mcp-server, exa-labs, serper, openclaw]
last_reviewed: 2026-04-19
---

# Tavily

**"The real-time search engine for AI agents and RAG workflows."**

Tavily is an AI-native search API — purpose-built for grounding LLMs, RAG pipelines, and autonomous agents with fresh, accurate web context. Claims #1 position on DeepResearch Bench with their `/research` endpoint. Trusted by 1M+ developers, enterprise customers include Databricks (MCP Catalog launch partner), IBM, BCG, JetBrains, AWS, MongoDB, and Writer.

**API:** https://api.tavily.com | **Docs:** https://docs.tavily.com
**GitHub:** https://github.com/tavily-ai
**Certifications:** https://tavily.com/certification

---

## Key Stats

| Metric | Value |
|--------|-------|
| Monthly requests | 100M+ |
| Uptime SLA | 99.99% |
| p50 latency (`/search`) | **180ms** — claimed fastest in market |
| Developers | 1M+ |
| Pages crawled/extracted | Billions |

---

## Products

### Core API Endpoints

| Endpoint | Description |
|----------|-------------|
| `/search` | Real-time web search — 180ms p50, fastest in market |
| `/extract` | Extract full content from specific URLs |
| `/crawl` | Crawl and extract content from entire sites |
| `/map` | Site mapping — discover all pages on a domain |
| `/research` | Deep research — state-of-the-art, #1 on DeepResearch Bench |

### MCP Server — `tavily-mcp` ⭐ 1,796

Production-ready MCP server with real-time search, extract, map, and crawl.

**Install (Claude Code):**
```bash
claude mcp add tavily https://api.tavily.com/mcp
```

### Agent Skills — `tavily-ai/skills` ⭐ 225

CLI-based skills for Claude Code, Cursor, and other AI coding agents.

| Skill | Description |
|-------|-------------|
| `tavily-search` | Web search with domain filtering, time ranges, multiple depths |
| `tavily-extract` | Extract clean markdown/text from specific URLs (handles JS-rendered pages) |
| `tavily-crawl` | Bulk crawl entire site sections → local markdown files |
| `tavily-map` | Discover all URLs on a domain without extracting content |
| `tavily-research` | AI-powered multi-source synthesis with citations (30–120s) |
| `tavily-cli` | Workflow guide + install/auth instructions |
| `tavily-best-practices` | Production-ready integration reference |

**Install:**
```bash
npx skills add https://github.com/tavily-ai/skills
curl -fsSL https://cli.tavily.com/install.sh | bash
tvly login --api-key tvly-YOUR_KEY
```

### MCP Server — `tavily-mcp` ⭐ 1,796

Production-ready MCP server (STDIO transport) for AI agents. Distinct from CLI skills above.

**Install (Claude Code):**
```bash
claude mcp add tavily https://api.tavily.com/mcp
```

### SDKs

| Package | Stars | Language |
|---------|-------|----------|
| `tavily-python` | 1,177 | Python |
| `tavily-cookbook` | 70 | Code snippets and guides |
| `tavily-sheets` | 48 | Google Sheets + Tavily integration |
| `tavily-chat` | 72 | Conversational agent (chat + live web) |
| `market-researcher` | 36 | Market research automation tool |

---

## Pricing

Free tier: **1,000 API credits/month**, no credit card required.

| Plan | Price | Credits |
|------|-------|---------|
| Free | $0 | 1,000/month |
| Hobby | $1 | 2,000/month |
| Starter | $7 | ~14,000/month |
| Growth | $30 | ~60,000/month |
| Enterprise | Custom | Custom volume |

---

## Key Differentiators vs Other Search APIs

| | Tavily | Brave | Exa | Serper |
|--|--------|-------|-----|--------|
| **Built for AI agents** | ✅ RAG + agent-specific | ❌ | ✅ | ❌ |
| **Deep research endpoint** | ✅ #1 on benchmarks | ❌ | ❌ | ❌ |
| **180ms latency** | ✅ p50 fastest | ❌ | ❌ | 1-2s |
| **Grounding / anti-hallucination** | ✅ Core positioning | ❌ | ❌ | ❌ |
| **Enterprise trust** | ✅ IBM, Databricks, BCG, JetBrains, AWS | ❌ | ❌ | ❌ |
| **99.99% SLA** | ✅ | ❌ | ❌ | ❌ |
| **SOC 2 / security** | ✅ PII filter, prompt injection protection | ❌ | ❌ | ❌ |
| **MCP-native** | ✅ (1,796 ⭐) | ✅ | ✅ | ❌ |
| **RAG chunking/structuring** | ✅ Native output for models | ❌ | ✅ | ❌ |
| **Neural/hybrid search** | ❌ | ❌ | ✅ | ❌ |
| **Company/news/tweet filters** | ❌ | Partial | ✅ | ❌ |
| **Real Google SERPs** | ❌ | ❌ | ❌ | ✅ |

---

## OpenClaw Connection

Tavily was mentioned in the context of the OpenClaw outreach stack (Matt Ganzak framework). OpenClaw routes to Haiku/Sonnet/Opus models based on task complexity and uses a Master Router + QC agent. Tavily fits as a **search/grounding layer** within the OpenClaw orchestration — providing fresh web context to prevent hallucinations in the outbound messaging pipeline.

See: [[openclaw]], [[agency-agents/openclaw]]

---

## For KlickSmartAI / HUBERT-X

**Tavily's core value for Dennis's stack:**
1. **Grounding / anti-hallucination** — Tavily's #1 positioning is "grounding models with fresh web context." For HUBERT-X candidate research, this means summaries you can trust.
2. **Deep research** — `/research` endpoint for comprehensive prospect reports (company, market, competitive intel)
3. **Enterprise trust** — IBM, Databricks, BCG partnerships signal production-grade reliability
4. **180ms speed** — fastest in class, viable for real-time agent pipelines
5. **MCP-native** — `tavily-mcp` (1,796 stars) slots into the existing OpenClaw + Hermes orchestration

**Decision:** Tavily is the most AI/RAG-native of the four search tools. Best used as the **primary search for HUBERT-X** recruiting pipeline, especially for deep research on insurance advisor candidates. Brave/Exa/Serper remain complementary for multi-format, financial, and Google-specific use cases.

---

## Sources

- https://tavily.com
- https://api.tavily.com
- https://docs.tavily.com
- https://github.com/tavily-ai
- TechCrunch (Aug 2025): "Tavily raises $25M Series A"
