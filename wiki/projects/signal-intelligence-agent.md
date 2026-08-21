# Signal Intelligence Agent — Product Definition

**Status:** Active development — 2026-04-20
**Type:** Revenue Intelligence Product / Core GTM Capability
**Owner:** Dennis E. / KlickSmartAI

---

## Core Philosophy

> Not generic lead gen. **Topical authority-driven signal matching.**
>
> Analyze what a client is an authority in → find signals that match those topics → generate qualified leads based on topical match.

---

## The 3-Stage Pipeline

### Stage 1 — Topical Authority Analysis *(New)*
**Input:** Client domain / website / content
**Output:** Topic graph of client's authority zones

- Crawl client website / content library
- Extract key topics, themes, expertise areas
- Build a **Topic Authority Map** — ranked list of topics with authority scores
- Identify **adjacent topics** (topics the client could credibly expand into)

**Tools:** `firecrawl_map`, `firecrawl_scrape`, `notebooklm_mcp` (create_notebook, add_source, ask)

### Stage 2 — Signal Intelligence Agent *(Core)*
**Input:** Topic Authority Map + search engine sweep
**Output:** Scored, actionable signal opportunities

See Section below.

### Stage 3 — Lead Generation
**Input:** Scored signals
**Output:** Qualified leads ready for outreach

- Match signals to ICP
- Generate outreach content (angle, message, channel)
- Output to CRM / GHL / CSV

---

## The 5 Core Capabilities (Signal Intelligence Agent)

### 1. 🧠 Signal Detection (Multi-Engine Parallel)
**Tools:** Brave + Serper + Tavily + Exa + DataForSEO (all 5 simultaneously)
- Search across all engines for signals matching the client's topical authority zones
- Deduplicate + merge results
- Prioritize Tavily/Exa results (richer context)

### 2. 🧾 Context Extraction
**Model:** MiniMax via Ollama
**Output:**
- Who is involved
- What happened
- Where
- When
- Industry
- Event type

### 3. 🎯 Signal Classification
**Labels:**
- Event type: Funding, Hiring, Expansion, Distress, Acquisition, Property transaction
- ICP relevance: High / Medium / Low
- Topical match: [which authority topic this matches]

### 4. ⚡ Opportunity Scoring
**Output:**
- Urgency score (1–10)
- Why now (timing trigger)
- Likelihood of engagement
- Estimated deal value (optional)
- Topical authority fit score

### 5. 🚀 Action Generation
**Output:**
- Outreach angle
- First message idea
- Hook (based on signal + topical match)
- Suggested channel: LinkedIn / Email / Call

---

## Topical Authority Analysis — How It Works

### Input Sources
- Client website URL → crawl + extract all content
- Client provided topic list (manual override)
- Existing content / blog / docs

### Topic Graph Output
```json
{
  "domain": "client.com",
  "authority_topics": [
    { "topic": "AI Agents", "authority_score": 0.95, "content_count": 47 },
    { "topic": "LLM Fine-tuning", "authority_score": 0.82, "content_count": 23 },
    { "topic": "MLOps", "authority_score": 0.71, "content_count": 15 }
  ],
  "adjacent_topics": [
    { "topic": "AI Infrastructure", "score": 0.65 },
    { "topic": "Enterprise AI Adoption", "score": 0.58 }
  ]
}
```

### Signal Matching Logic
- Signals tagged by topic
- Match against authority_topics → High ICP fit
- Match against adjacent_topics → Medium ICP fit
- No match → Low ICP fit (deprioritize)

---

## Input → Output Example (Topical Authority Mode)

**Context:** Client is an authority in "AI Agents" and "LLM Fine-tuning" (based on Stage 1 analysis)

**Input Signal:**
> "AI startup Nexus Labs raises $12M Series A"

**Output:**
```json
{
  "company": "Nexus Labs",
  "event_type": "Funding",
  "summary": "Raised $12M Series A for AI agent platform",
  "matched_topic": "AI Agents",
  "authority_fit": "High",
  "why_now": "Fresh capital + AI agent focus = likely hiring, tooling, infrastructure spend in next 90 days",
  "urgency_score": 8,
  "icp_fit": "High",
  "opportunity": "Selling AI agent tools, infrastructure, or services",
  "outreach_angle": "You just raised — teams are scaling. We help AI companies operationalize their agent stack.",
  "suggested_message": "Congrats on the Series A. Most AI agent companies at your stage hit the same wall: scaling inference costs and agent orchestration. Happy to share how we're helping similar companies cut 40% on infrastructure.",
  "channel": "LinkedIn"
}
```

---

## Multi-Engine Signal Detection

All 5 research MCPs run in parallel for maximum signal coverage:

| Engine | Tool | Signal Type |
|--------|------|-------------|
| **Brave Search** | `brave_web_search` | Real-time news, general signals |
| **Serper.dev** | `google_search` + `scrape` | Google-ranking signals, competitor activity |
| **Tavily** | `tavily_search` + `tavily_research` | Deep research, cited sources, topic analysis |
| **Exa** | `deep_search_exa` | Financial, funding, acquisitions, people |
| **DataForSEO** | 69 tools (full SEO suite) | Market trends, keyword surges, traffic signals |

### Detection Strategy
- **Parallel sweep** — run all 5 engines simultaneously for each authority topic
- **Deduplicate** — merge results, remove duplicates by URL
- **Prioritize** — Tavily/Exa results score higher (richer context)
- **Fallback** — if one engine fails, others continue

---

## System Architecture

|| Layer | Tool |
|-------|------|
| Topical Analysis | Firecrawl (crawl, scrape) + NotebookLM MCP (topic inference) |
| Detection | Brave + Serper + Tavily + Exa + DataForSEO (parallel) |
| Processing | MiniMax via Ollama |
| Orchestration | Hermes Agent |
| Storage | Google Sheets (per-client, in Google Workspace folder) |
| Action | Google Sheets output + outreach draft for review |

---

## Vertical Applications

| Vertical | Topical Authority Example | Signal Types |
|----------|-------------------------|--------------|
| WealthWireRadar | Wealth management, HNW investing, estate planning | HNW fund flows, advisor hires, regulatory changes |
| IDC Recruitment | Insurance tech, insurance recruiting | Funding, hiring, expansion |
| Contractors | Construction, renovation, commercial build | Permits, property transactions, expansions |
| Mortgage brokers | Real estate financing, refinancing | Rate changes, property sales, builder news |

---

## Proposed Features

### Feature: Visible Reasoning Trace + Cross-Verification *(Proposed)*
**Trigger:** Comparing Grok DeepSearch's chain-of-thought transparency vs. current Stage 2 output — signal reasoning is opaque.

**Gap:** Stage 2 runs 5 engines in parallel and scores signals, but:
- No visible reasoning path (which engines found each signal, how consistent are they)
- No cross-verification scoring (did 1 engine find it vs. all 5)
- Chain-of-thought reasoning exists in MiniMax but isn't exposed as a trace

**What it does:**
- Wrap Stage 2 multi-engine sweep with MiniMax chain-of-thought reasoning
- For each signal: output the full reasoning path (sources checked, consistency score, why match)
- Cross-verification badge: `Verified by 4/5 engines` vs `Found by 1/5 engines`
- Visible trace layer before final signal score — mirrors Grok DeepSearch's transparency

**Why it matters:** Signal scores without reasoning are hard to trust. A visible trace lets users verify, refine, and build confidence in the output. Competitors (Grok DeepSearch, Perplexity) make reasoning visible — our output should too.

**Priority:** P2 — not blocking MVP, but differentiates from generic lead gen

---

## Next Steps

1. [ ] Build Topical Authority Analysis prompt + topic graph extraction logic
2. [ ] Build production-grade Signal Scoring prompt v1 (with topical match field)
3. [ ] Build ICP template system (per vertical)
4. [ ] Wire into: Python cron → Ollama MiniMax → CSV / CRM
5. [ ] Test on WealthWireRadar domain

---

## Related Projects

- WealthWireRadar — financial signals use case
- IDC Recruitment Agent — hiring signals use case
- HUBERT-X — recruiter-facing scoring interface
- Contractors (growth signals)
- Recruiters (job change signals)

---

## Next Steps

1. Build production-grade prompt + JSON schema + scoring logic
2. Wire into: Python cron job → Ollama MiniMax → CSV / CRM
3. Define ICP templates per vertical

---

## Related Projects

- WealthWireRadar — financial signals use case
- IDC Recruitment Agent — hiring signals use case
- HUBERT-X — recruiter-facing scoring interface
