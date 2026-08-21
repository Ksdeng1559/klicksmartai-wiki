# Topical Authority Engine — Research Pipeline Plan

## Mission
Find high-search-volume, low-competition niche topics where KlickSmartAI (or any client) can become the authoritative answer — then produce evergreen content that converts.

---

## Architecture: Two-System Pipeline

```
SuperClaude (Windows)              Hermes Agent (WSL)
────────────────────              ──────────────────
Layer 0: Domain Audit
  [domain]_domain_analysis.html
  [domain]_advertorial_war_room.html
                              ├── Layers 1–4: Research funnel
                              │   (Serper + DataForSEO + Exa +
                              │    yt-dlp + Tavily + Brave)
                              └── Layer 5: Google Doc research report
                                  (merges SuperClaude output +
                                   Hermes scoring + briefs)
```

**Why two systems?**
- SuperClaude (Windows) has browser rendering + LPDomainAnalysis (rich HTML dashboards)
- Hermes (WSL) has the MCP data stack (DataForSEO, Exa, Serper, yt-dlp, Tavily, Brave)
- Each does what it's best at; outputs merge in the final Google Doc

---

## The 6-Layer Research Funnel

```
Layer 0: DOMAIN AUDIT         → baseline: what does the domain already own?
Layer 1: DEMAND SEEDING        → YouTube + Google + social signals
Layer 2: INTENT MAPPING       → PAA, related searches, forum pain points
Layer 3: COMPETITION GAP      → difficulty, thin content, backlink gaps
Layer 4: SCORING              → 6-factor matrix, threshold >= 35/60
Layer 5: BRIEF GENERATION     → angle, hooks, sub-topics, CTAs
```

### Layer 0: Domain Audit

Run FIRST for every new client. Baseline is everything.

**L0a — Backlink Profile (DataForSEO)**
```
backlinks_summary             → DR, referring domains, total links
backlinks_bulk_backlinks      → recent link acquisitions
backlinks_referring_domains   → DA distribution, toxic link signals
```

**L0b — Keyword Rankings (DataForSEO)**
```
keywords_data                → top 50 keywords domain already ranks for
rank_tracking_summary        → position changes, visibility trajectory
```

**L0c — Content Inventory (Exa deep search)**
For each top-ranking URL on the domain:
```
Exa deep_search_exa on page content
  → content depth score (1-10)
  → word count, heading structure
  → CTA presence (lead magnet / booking / contact)
  → schema markup signals
  → recency (last updated?)
  → E-E-A-T signals
```

**L0d — Technical SEO (Brave + Serper)**
```
Brave: brave_web_search "site:<domain> robots.txt"
Serper: scrape <domain>/sitemap.xml       → page count, structure
Serper: scrape <domain>                   → title, meta, H1s, internal links
```

**L0 Output — Domain Audit Report**
```
Domain: <domain>
DR: X/100 | Ref Domains: X | Total Links: X
Top Keywords (by volume): [top 10]
Top Keywords (by position): [top 10]
Content Gaps Found: [thin pages, missing topics]
Backlink Opportunities: [what competitors have that domain does not]
Technical Issues: [meta missing, sitemap absent, slow pages]
```

---

## The 5-Layer Research Funnel

```
Layer 1: RAW DEMAND
├── YouTube Trending Scraper      → yt-dlp MCP
├── Google Search Volume          → DataForSEO (search_volume)
├── Google Trends                → Tavily (news/search) + Brave
└── Social Pulse                  → Exa (social content + discussions)

          ↓  converge into Topic Seed List

Layer 2: COMPETITION ANALYSIS
├── Domain Authority / Backlinks  → Exa (company research + backlink signals)
├── Content Gap Score             → DataForSEO (keyword difficulty, CPC)
├── SERP Features                → SERP.dev (people_also_ask, related_searches)
└── Top-Ranking URL Analysis     → Exa (deep content extraction)

          ↓  filter: volume > threshold AND difficulty < threshold

Layer 3: INTENT VERIFICATION
├── What People Ask              → SERP.dev (people_also_ask)
├── People Also Ask              → SERP.dev + TAVILY (related questions)
├── Forum Pain Points           → Exa (Reddit, HN, Quora deep search)
└── Real User Gaps              → Exa (social discussions — where do people struggle?)

          ↓  score each topic: demand × intent × gap

Layer 4: TOPIC SCORING MATRIX
Each topic gets scored 1–10 on:
  • Search Volume (DataForSEO)       — raw demand
  • Competition Gap (DataForSEO)    — how underserved
  • Content Depth Gap (Exa)         — are top results thin?
  • Question Density (SERP.dev)     — how many PAA questions?
  • Social Momentum (Exa)           — growing or stagnant?
  • Monetization Signal (CPC)        — CPC = commercial intent

          ↓  topics with score ≥ 35/60 move to brief

Layer 5: CONTENT BRIEF GENERATION
For each qualified topic, output:
  • Recommended content angle (differentiated from top 3 SERP results)
  • Hook / headline variants
  • Sub-topic clusters to cover (authority silos)
  • Primary CTA + secondary CTA
  • Internal link opportunities
  • Format recommendation (video, article, tool, comparison)
```

---

## Data Sources & Tool Mapping

| Layer | Tool | What it provides |
|-------|------|-----------------|
| YouTube demand | yt-dlp MCP | Trending vids, view counts, engagement signals |
| Google volume + difficulty | DataForSEO MCP | Monthly search volume, CPC, difficulty |
| Google trends | Brave Search MCP | Rising queries, autocomplete |
| PAA / Related searches | Serper MCP google_search | Questions + related + knowledge graph |
| Competitor content | Exa MCP deep_search_exa | Top-ranking articles, content gaps, backlink sources |
| Social pulse | Exa MCP web_search_advanced_exa | Reddit threads, HN discussions, forum pain points |
| Real-time news | TAVILY MCP tavily_search | Breaking trends in a niche |
| Domain intel | Exa MCP (company) + DataForSEO backlinks | Client content landscape + backlink profile |

---

## Serper Integration (PAA + Related Searches)

**API:** Already wired — `SERPER_API_KEY` in config. Use the `serper` MCP server.

Key capabilities:
- `google_search` — returns `people_also_ask[]`, `related_searches[]`, organic results, knowledge graph
- `scrape` — extract full page content with markdown

Key fields captured per query:
```
query
people_also_ask[]      ← question + answer snippet
related_searches[]     ← adjacent topic terms
knowledge_graph        ← entity signals (brand, product, category)
organic_results[]      ← top 10 URLs with titles + snippets
```

---

## Social Intelligence Layer (Exa)

Use Exa's `deep_search_exa` with these query patterns:

```
Topic: "AI agents for insurance brokers"
  → "AI agents insurance brokers site:reddit.com OR site:news.ycombinator.com"
  → "insurance broker pain points AI automation site:reddit.com"
  → "what do insurance agents struggle with AI 2024 2025"
```

Extract from results:
- **Pain points** — recurring complaints, frustrations
- **Unanswered questions** — things people ask but nobody answers well
- **Tool mentions** — what are they already using?
- **Trending sentiment** — growing frustration = growing search demand

---

## Scoring Algorithm (Pseudocode)

```python
def score_topic(query, serp_data, volume_data, social_data):
    volume_score    = normalize(volume_data.monthly_searches, 0, 50000) * 10
    difficulty_score = (100 - volume_data.competition) / 100 * 10
    paa_score       = len(serp_data.people_also_ask) / 10 * 10   # cap at 10
    gap_score       = content_thinness(serp_data.top_results) * 10
    social_score    = social_momentum(social_data) * 10
    cpc_score       = normalize(volume_data.cpc, 0, 20) * 5

    total = (
        volume_score    * 0.25 +
        difficulty_score * 0.25 +
        paa_score       * 0.15 +
        gap_score       * 0.15 +
        social_score    * 0.10 +
        cpc_score       * 0.10
    )
    return round(total, 1)  # out of 10

# Topics with score >= 5.8 (35/60 weighted) → content brief
```

---

## Inputs (Client Onboarding)

When a new client/domain enters the system, capture:

```
client_name:
client_domain:
client_industry:
client_offering:
client_target_audience:
primary_kw_guess:          # what they THINK they rank for
competitor_urls[]:         # 3-5 known competitors
content_already_produced:  # URL list or "none"
budget_tier:               # solopreneur / startup / agency / enterprise
primary_goal:              # leads / sales / awareness / authority
```

This feeds the research pipeline and calibrates the competition threshold.

---

## Output: Research Report (per client) — Markdown for Claude Code

**Format:** Pure markdown. Every `- [ ]` = a standalone taskable checkbox. Every implementation brief is a complete, executable spec that Claude Code can run directly via `/blog write` or `/blog audit`.

### Structure
```
1. Executive Summary — top 3 opportunities in 1 line each
2. Opportunity Table — all scored topics with IMPLEMENT/WATCH/SKIP tags
3. Deep-Dive Briefs (top 3) — each with full task checklist
4. PAA Raw Data — by sub-intent (informational / commercial / transactional)
5. Competitive Landscape — competitor weaknesses + backlink gap actions
6. 12-Week Publishing Calendar — from LPDomainAnalysis War Room
7. Client Onboarding Summary block
```

### Output file
```
topical-authority-research-[domain]-[YYYY-MM-DD].md
```
Saved to: `~/wiki/research-pipeline/outputs/`

---

## Research Cadence

| Frequency | Action |
|-----------|--------|
| Weekly | Fresh SERP + social pulse on top 3 existing topics |
| Monthly | Full re-run of scoring matrix — catch rising trends early |
| Quarterly | Strategic review — sunset stale topics, add new verticals |

---

## Tools Already Wired In

```
yt-dlp MCP        -> YouTube trending + video research (auth: npx notebooklm-mcp-server auth)
Tavily MCP        -> Real-time search + deep research
Exa MCP           -> Deep search, company/people/news research
DataForSEO MCP    -> Search volume, keyword difficulty, CPC, backlinks
Brave Search MCP  -> Real-time web search, autocomplete
Serper MCP        -> PAA, related searches, organic results, knowledge graph
```

---

## Next Steps (when ready to build)

1. **Run LPDomainAnalysis** on Windows (SuperClaude) for first client domain
2. **Transfer HTML outputs** to Hermes context — paste key insights from the 2 HTML dashboards into the Hermes research session
3. **Run `/research-topics`** on Hermes with Layer 1-5 funnel
4. **Output** — Google Doc saved to Drive folder 1uscboXl45xn6SOrXa9Rc7FeUMa2kJthx
5. **Cron**: set up weekly pulse + monthly full run once pipeline is validated
