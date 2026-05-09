---
name: spectra-social-intelligence
description: Gather community-level social intelligence to support Spectra Holdings MCF briefs. Uses multiple search engines to surface local news, sentiment, org landscape, faith community activity, and political context for a target county.
trigger: /spectra-social-intelligence
---

# /spectra-social-intelligence

Gather community-level social intelligence to support all Spectra Holdings MCF deliverable briefs.

## Usage

```
/spectra-social-intelligence <county>, <state> [--depth light|standard|deep]
```

**Examples:**
```
/spectra-social-intelligence Harris County, TX --depth standard
/spectra-social-intelligence King County, WA --depth deep
/spectra-social-intelligence Bexar County, TX --depth light
```

---

## What This Is

Social intelligence supplements census data with community-level qualitative intelligence. Where census tells you the numbers, social intelligence tells you the story behind them — what's being said, who's doing what, what's moving, what's stuck.

It feeds all four deliverable types:
- **Advertorial** → local faith community, churches engaged, Christian org landscape
- **Investor Brief** → political risk, regulatory environment, developer ecosystem
- **Internal Brief** → partner landscape, org landscape, community sentiment
- **County Official Briefing** → what's already in motion, who's who, community priorities

---

## Input

| Input | Required | Description |
|-------|----------|-------------|
| `county` | Yes | Full county name |
| `state` | Yes | Two-letter state code |
| `depth` | No | `light` (3 searches) / `standard` (6 searches) / `deep` (10 searches). Default: `standard` |

---

## Workflow

### Phase 1 — Search Engine Rotation

Rotate across these six engines to avoid rate limits and get diverse results:

| Engine | Best For | Notes |
|--------|----------|-------|
| **Brave Search** | Local news, community orgs, general web | `site:news <county> housing` |
| **Serper (Google)** | News, press releases, political | `county state housing crisis 2024 2025` |
| **Tavily MCP** | Deep research, cited reports, site extraction | `tavily_research` for full report; `tavily_search` for quick |
| **Parallel.ai** | Agentic deep search, content extraction, entity discovery | `parallel-cli research run --processor pro` for full dossiers |
| **Exa / Deep Search** | Academic, reports, long-form | `"<county>" housing affordability report` |
| **SerpAPI** | Local search, Google Maps categories | `<county> housing nonprofit` |

**Rotation rule:** Never call the same engine twice in a row. If one hits a rate limit, rotate immediately to the next. Never retry a credit-exhausted engine.

### Phase 2 — Intelligence Categories

For each category, run the appropriate search and web_extract key findings.

#### Category 1 — Local News (all briefs)

**Brave / Serper surface search:**
```
<county> <state> housing crisis 2024 2025
<county> <state> affordable housing news
<county> <state> eviction homelessness news
```

**Tavily deep search:**
```
tavily_search --query "<county> <state> housing crisis 2024" --search_depth advanced --topic general --max_results 10 --include_answer true
tavily_search --query "<county> <state> affordable housing policy" --search_depth advanced --topic news --time_range month --max_results 8
```

**Parallel.ai agentic research:**
```
parallel-cli research run "<county> <state> local housing news ecosystem" --processor pro --json
```

**Extract:**
- Recent headlines and key stories
- Who's being quoted — advocates, officials, developers, residents
- Trend: is housing getting better or worse in local coverage?
- Any recent policy votes, bond measures, zoning decisions
- What the local newspaper editorial board is saying

#### Category 2 — Community & Advocacy Orgs (internal brief + county official briefing)

**Search:**
```
<county> <state> housing coalition
<county> <state> affordable housing nonprofit
<county> <state> community development corporation
<county> <state> tenant rights organization
```

**Extract:**
- Active organizations — name, mission, programs
- Who's the leader, when were they founded
- What they're currently working on
- Are they faith-based? CDFI? Hybrid?
- Any recent announcements, campaigns, reports

#### Category 3 — Faith Community Landscape (advertorial + county official briefing)

**Search:**
```
<county> <state> church housing ministry
<county> <state> faith-based affordable housing
<county> <state> Christian community development
<county> <state>Habitat for Humanity churches
```

**Extract:**
- Churches actively doing housing work
- Christian community development orgs (CCDA network)
- Faith-based CDFIs or loan funds
- Denominational social ministry offices
- Local expressions of parachurch housing initiatives
-跨宗派福音联盟 or local ecumenical housing alliances

#### Category 4 — Developer & Financing Ecosystem (investor brief + internal brief)

**Search:**
```
<county> <state> housing developer affordable
<county> <state> LIHTC recent transactions
<county> <state> CDFI active financing
<county> <state> Opportunity Zone real estate
```

**Extract:**
- Active affordable housing developers in county
- Recent LIHTC award announcements
- CDFIs making loans in the county
- Opportunity Zone activity
- Any new affordable housing projects breaking ground

#### Category 5 — Political & Regulatory Environment (investor brief + county official briefing)

**Search:**
```
<county> <state> housing policy zoning 2024 2025
<county> <state> rent control ballot
<county> <state> housing authority board
<county> <state> inclusionary zoning
```

**Extract:**
- Current political climate on housing (council, county board)
- Any rent control or tenant protection measures active or proposed
- Zoning reform efforts
- Who represents the county at state level on housing
- Key champions or opponents of affordable housing

#### Category 6 — Recent Developments & Momentum (all briefs)

**Search:**
```
<county> <state> housing bond measure 2024 2025
<county> <state> affordable housing grand opening
<county> <state> housing fund announcement
```

**Extract:**
- New funding sources or ballot measures
- Recent project completions or groundbreakings
- Any federal or state grants awarded in the county
- momentum indicator: is this market heating up or cooling?

#### Category 7 — Community Sentiment (advertorial + county official briefing)

**Search:**
```
"<county> housing" site:nextdoor.com OR site:reddit.com
<county> <state> housing subreddit
<county> <state> gentrification displacement
```

**Extract:**
- What residents are saying in their own words
- Displacement and gentrification concerns
- Community priorities as expressed by residents themselves
- Specific quotes that illustrate the human reality

### Phase 3 — Synthesize into Wiki

Save to: `census/<county>-<state-abbrev>-social-intelligence.md`

Follow this structure:

**Header:**
```
---
title: "<County Name, ST> — Social Intelligence Brief"
client: Spectra Holdings Group
scope: <County Name, ST>
audience: KlickSmartAI Internal | All Deliverable Types
tags: [<county>, <state>, social-intelligence, spectra-holdings]
created: [[DATE]]
updated: [[DATE]]
sources_searched: [list of engines used]
depth: [light | standard | deep]
---
```

**Sections:**
1. **News Landscape** — headlines, sentiment, who's quoted, trend
2. **Community & Advocacy Orgs** — table of active orgs with mission and status
3. **Faith Community** — churches and faith orgs active in housing
4. **Developer & Financing Ecosystem** — who's building, who's financing
5. **Political & Regulatory Environment** — current posture, key players, risk factors
6. **Recent Developments** — what's new, what's moving
7. **Community Sentiment** — resident voice, quotes, displacement concerns
8. **Intelligence Gaps** — what's missing, what needs verification, who to call

### Phase 4 — Update Graph + Push

```
cd ~/wiki && graphify update .
git add -A && git commit -m "social-intelligence: <county> county, <state>" && git push origin master
```

---

## Depth Guide

| Depth | Categories | Searches | Time |
|-------|-----------|----------|------|
| `light` | 1, 2, 5 | 3 | ~10 min |
| `standard` | 1–5 | 6 | ~20 min |
| `deep` | 1–7 | 10 | ~35 min |

Default is `standard`. Use `deep` when:
- County is a high-priority MCF target
- You have a county official meeting in the next 30 days
- The market has recent significant developments

---

## Search Query Templates

Copy and adapt these for each county:

```bash
# Brave Search — local news
brave "<county> <state> housing crisis 2024 2025" --json | jq .

# Serper — Google news + web
serper "<county> <state> affordable housing nonprofit"

# Exa — deep/ semantic
exa_search --query "<county> <state> housing affordability report study" --num-results 10

# SerpAPI local — Maps categories
serpapi "<county> <state>" --category housing_nonprofit

# Tavily — deep research with cited report
tavily_search --query "<county> <state> housing crisis affordable" --search_depth advanced --max_results 10 --include_answer true

tavily_research --query "<county> <state> community housing nonprofit ecosystem" --search_depth advanced --max_results 15

tavily_extract --urls ["https://countywebsite.gov/housing", "https://housingcoalition.org"] --query "housing programs affordability data"

# Parallel.ai — agentic deep search + extraction
~/.hermes/hermes-agent/venv/bin/parallel-cli research run "<county> <state> housing ecosystem" --processor pro --json

~/.hermes/hermes-agent/venv/bin/parallel-cli search "<county> <state> affordable housing nonprofit developer" --mode agentic --json

~/.hermes/hermes-agent/venv/bin/parallel-cli extract https://housing-org.example.com --objective "Find housing programs, affordability data, contact info" --json
```

---

## Pitfalls

- **Don't over-rely on one search engine** — rotate to avoid bias and rate limits
- **Don't skip the faith community search** — it's specifically important for advertorial framing and CDFI partner discovery
- **Local news paywalls** — try the cached version or an aggregator if the article is behind a paywall
- **Sentiment on Reddit/Nextdoor** — treat as anecdotal, use to supplement, not substitute for sourced data
- **Political data can be stale** — council and board compositions change; verify with the county website
- **Don't confuse national sentiment with local** — the national housing crisis narrative is different from what a specific county is experiencing
- **Deep search takes time** — if the user asks for deep on 3 counties simultaneously, flag that it will take longer

---

## Verification Steps

1. At least 3 search engines used
2. All assigned categories for the depth level searched
3. Key findings extracted — not just links
4. At least 5 organizations identified by name
5. Community sentiment section has at least 1 direct quote from a resident
6. Political/regulatory section identifies at least 2 key officials or bodies
7. File saved to `census/<county>-<state-abbrev>-social-intelligence.md`
8. Graph updated and pushed to GitHub
9. File linked from the corresponding census data file

---

## Related Skills

- `spectra-census-research` — quantitative foundation (run this first)
- `spectra-advertorial` — uses social intelligence for faith framing
- `spectra-investor-brief` — uses social intelligence for political risk and ecosystem analysis
- `spectra-internal-brief` — uses social intelligence for partner landscape
- `spectra-county-official-briefing` — uses social intelligence to acknowledge existing county efforts
