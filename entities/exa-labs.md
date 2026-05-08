---
title: Exa Labs
type: entity
category: platform
url: https://exa.ai
pricing: free
status: active
wired_to: hermes
mcp_server: exa
mcp_tools: [web_search_exa, web_fetch_exa, web_search_advanced_exa]
tags: [entity, exa, search-engine, ai-search, neural-search, web-crawl, company-research, mcp, typescript, python, financial-research, academic-search, personal-site-search]
related: [brave-search-mcp-server, duckduckgo-search, mcp, company-researcher]
last_reviewed: 2026-04-19
---

# Exa Labs

**"The Search Engine for AI Applications."** Exa is a search engine built specifically for AI — neural + keyword hybrid search, live web crawling, content retrieval, and purpose-built filters for company research, news, financial data, and code.

**API:** https://dashboard.exa.ai | **Docs:** https://docs.exa.ai

---

## Products

### `exa-mcp-server` ⭐ 4,277
**MCP server** for web search and web crawling. The flagship MCP integration.

|| Tool | What it does ||
||------|-------------|
|| `web_search_exa` | Search the web, get clean ready-to-use content ||
|| `web_fetch_exa` | Get the full content of a specific webpage from a known URL ||
|| `web_search_advanced_exa` | **Advanced** — full control over filters, domains, dates, category, type, LLM output schema ||

### Search Types (via `web_search_advanced_exa`)

| Type | Speed | Best For |
|------|-------|---------|
| `auto` | ~1s | Default, general queries |
| `instant` | ~200ms | Real-time apps (chat, voice) |
| `fast` | ~450ms | Speed with minimal quality sacrifice |
| `deep-lite` | ~2–10s | Lightweight synthesized output |
| `deep` | 5–60s | Complex multi-step reasoning, structured outputs |
| `deep-reasoning` | 10–60s | Higher-reasoning for harder research |

### Category Filters

|| Category | Coverage | Use Cases ||
|----------|----------|------------|
| `company` | 50M+ companies | GTM intelligence, lead gen, competitive mapping, deal sourcing |
| `people` | 1B+ professional profiles | Recruiting, SDR prospecting, org chart mapping, AI SDR enrichment |
| `code` | Billions of GitHub repos, docs, Stack Overflow | AI coding agents, grounded code examples, API references |
| `news` | Major publications, trade press, niche outlets | Market monitoring, earnings tracking, threat intel, GTM signals |
| `research paper` | 100M+ papers | Academic research, insurance AI, actuarial science, RegTech |
| `financial report` | SEC filings, earnings calls, annual reports | Company financials, investor briefings, insurance carrier analysis |
| `personal site` | Blogs, portfolios, independent creator sites | Thought leader discovery, independent broker research |

### People Search — When to Use
- **Recruiting/talent sourcing** — search candidates by role, skill, location, employer ("senior ML engineers in Seattle with PyTorch")
- **GTM/sales prospecting** — find decision-makers and buying committees ("VP Engineering at Series B fintech")
- **Professional services** — map leadership and org charts at target accounts ("CTO at fintech startups in New York")
- **AI SDR/outbound agents** — enrich prospect lists with up-to-date titles, companies, career context

### Company Search — When to Use
- **GTM/lead generation** — build targeted company lists by industry, headcount, geography, funding ("Series A fintech in Switzerland with 50–200 employees")
- **Finance/investment** — source deals, map competitive landscapes, track funding rounds ("agtech companies that raised Series A in the US")
- **Competitive intelligence** — discover emerging players and alternatives ("companies like Stripe")
- **Consulting** — research industries and build market scans for client deliverables

### Code Search — When to Use
- **AI coding agents** — ground model outputs with real, up-to-date code examples ("how to use Vercel AI SDK streaming API")
- **Developer docs platforms** — surface working snippets from GitHub, Stack Overflow, docs sites
- **AI infrastructure/agents** — give agents reliable web context for code tasks, reduce hallucinated imports
- **Dev productivity** — find config patterns, migration guides, setup recipes ("Docker Compose for PostgreSQL and Redis")

### News Search — When to Use
- **Finance/investment** — monitor market-moving news, earnings announcements, sector developments in real time
- **Cybersecurity/threat intel** — track vulnerability disclosures, breach reports, emerging threats
- **GTM intelligence** — surface press coverage, product launches, funding announcements for target accounts
- **Consulting/enterprise research** — gather and summarize current news for client briefings

### Financial Report Search — When to Use
- **Insurance carrier analysis** — BFL Canada, Canada Life, Manulife annual reports and earnings calls
- **Investment research** — 10K reports, 10Q reports, 8K filings, earnings transcripts
- **Market intelligence** — investor presentations, analyst coverage, price targets
- **Regulatory filings** — SEC/OSC filings for Canadian and US insurance carriers

### Research Paper Search — When to Use
- **Insurance AI research** — actuarial science, underwriting automation, risk modeling papers
- **RegTech/Compliance** — regulatory technology, PIPEDA, Solvency II research
- **Academic machine learning** — ML applications in insurance, climate risk models
- **Industry whitepapers** — insurance institute reports, Canadian Underwriter articles

### Key Capabilities (from GitHub ⭐ 4,277)

- **Neural + keyword hybrid** — understands meaning AND exact matches
- **Live web crawling** — fetches fresh content, not cached
- **Full page content retrieval** — highlights (4000 char extracts) or full text
- **Structured output schema** — extract JSON via `output_schema` parameter
- **LLM summaries** — AI-generated overviews per result
- **Grounded answers with citations** — via `/answer` endpoint
- **Subpage crawling** — up to 10 subpages per domain
- **No API key required** — MCP endpoint works without auth (rate-limited)

**Install (Claude Code):**
```bash
claude mcp add --transport http exa https://mcp.exa.ai/mcp
```

**Install (npm):**
```json
{
  "mcpServers": {
    "exa": {
      "command": "npx",
      "args": ["-y", "exa-mcp-server"],
      "env": { "EXA_API_KEY": "your_api_key" }
    }
  }
}
```

---

### `company-researcher` ⭐ 1,436
Free open-source tool for instant company intelligence. Input a URL → Exa gathers comprehensive data from across the web.

**Data gathered:**
- Website content + subpages (About, FAQs, Pricing, Blog)
- LinkedIn company profile + founders' LinkedIn
- Funding details, Crunchbase, PitchBook, Tracxn, 10K reports
- News coverage, competitor analysis, Wikipedia
- Twitter/X, YouTube, TikTok, Reddit, GitHub

**Tech stack:** Next.js, TailwindCSS, TypeScript, Vercel AI SDK

---

### `exa-hallucination-detector` ⭐ 320
Free open-source tool to verify accuracy of LLM-generated content instantly.

---

### SDKs

| Package | Stars | Language |
|---------|-------|----------|
| `exa-py` | 212 | Python |
| `exa-js` | 127 | TypeScript |

---

## Core Features (vs DuckDuckGo / Brave)

| Feature | Exa | DuckDuckGo | Brave |
|---------|-----|-----------|-------|
| **Neural search** | ✅ Hybrid neural + keyword | ❌ | ❌ |
| **Live web crawling** | ✅ | ❌ | ❌ |
| **Full content retrieval** | ✅ | ❌ | ❌ |
| **Company filter** | ✅ `c=company` | ❌ | ❌ |
| **News filter** | ✅ `c=news` | ❌ | ✅ News search |
| **Tweet filter** | ✅ `c=tweet` | ❌ | ❌ |
| **Financial report filter** | ✅ `c=financial report` | ❌ | ❌ |
| **Code search** | ✅ | ❌ | ❌ |
| **Subpage crawling** | ✅ up to 10 subpages | ❌ | ❌ |
| **MCP-native** | ✅ (4,277 ⭐) | ❌ | ✅ |
| **Privacy-focused** | ✅ | ✅ | ✅ |

## Key Differentiator

Exa is **built for AI applications** — not a consumer search engine. Every result is clean, parseable, crawlable content that LLMs can use directly. The `c=` parameter categories (company, news, tweet, code, financial report, etc.) are designed for AI data extraction pipelines.

The **company researcher** tool is particularly powerful — one URL input gives you funding, LinkedIn, financials, social media, news, and competitor data from a single Exa search call.

---

## For KlickSmartAI / HUBERT-X

Relevant for:
- **HUBERT-X research phase** — Exa's company research + news/tweet filters for recruiting intelligence on insurance advisor candidates
- **WWR signal pipeline** — Exa's neural search + content retrieval for battlecard building
- **Klick2Client OS** — company research on prospects (funding, LinkedIn, news, competitors)
- **IDC presentation** — competitive intel on rival insurance agencies or talent pools
- **Alternative to Brave** — when you need full-page content retrieval rather than just URLs

---

## Exa Org Summary

| Repo | Stars | Description |
|------|-------|-------------|
| `exa-mcp-server` | 4,277 | MCP server — web search + crawl |
| `company-researcher` | 1,436 | Company intelligence tool |
| `exa-hallucination-detector` | 320 | LLM output verifier |
| `exa-deepseek-chat` | 731 | Chat app: Exa search + Deepseek R1 |
| `exa-o3mini-chat` | 42 | Chat app: Exa search + OpenAI o3-mini |
| `exa-writing-assist` | 38 | Writing + citation assistant |
| `answer-chat-app` | 28 | Chat app using Exa Answer endpoint |
| `exa-py` | 212 | Python SDK |
| `exa-js` | 127 | JavaScript SDK |

---

## Source

- https://github.com/exa-labs
- https://exa.ai
- https://docs.exa.ai
