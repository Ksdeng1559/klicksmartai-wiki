---
title: Entities & Projects Index
created: 2026-06-10
updated: 2026-06-10
type: summary
tags: [memory, notes, research]
sources: [https://github.com/Ksdeng1559/klicksmartai-wiki/tree/master/entities, https://github.com/Ksdeng1559/klicksmartai-wiki/tree/master/projects]
---

# Entities & Projects Index

Master index of all entity and project pages in the KlickSmartAI wiki. For full content, follow the `[[wikilinks]]` to individual pages or browse the GitHub repo.

## People

| Entity | Description |
|---|---|
| [[dennis-e]] | Dennis E. — Founder/Owner of KlickSmartAI, Vancouver BC |
| [[alexander-eng-toy-nissan-gtr]] | Alexander Eng — personal context |

## Companies & Organizations

| Entity | Description |
|---|---|
| [[ncf-national-christian-foundation]] | NCF — DAF market context, capital source for Spectra Holdings |
| [[spectra-holdings-group]] | Spectra Holdings Group — 19-division community dev holding company |
| [[insurance-direct-canada-lead-research]] | IDC — active client (insurance lead research) |
| [[insurance-direct-canada-recruitment-agent]] | IDC — recruitment agent project |
| [[wattbricks]] | WattBricks — client/prospect |
| [[wealth-wire-radar]] | Wealth Wire Radar — client/prospect |
| [[enterprise-community-loan-fund]] | Enterprise Community Loan Fund — CDFI-aligned entity |
| [[cascadia-innovation-corridor]] | Cascadia Innovation Corridor — regional context |

## AI Models & Agents

| Entity | Description |
|---|---|
| [[anthropic]] | Anthropic — Claude family provider |
| [[claude-code-guide]] | Claude Code — comprehensive guide |
| [[claude-code-local]] | Claude Code — local installation |
| [[claude-partner-network]] | Claude Partner Network |
| [[hermes-agent]] | Hermes Agent — Nous Research agent framework |
| [[grok-xai]] | Grok / xAI — model + API |
| [[ollama]] | Ollama — local model runtime |

## Search & Data APIs

| Entity | Description |
|---|---|
| [[brave-search-mcp-server]] | Brave Search MCP server |
| [[serper]] | Serper.dev — Google Search API |
| [[tavily]] | Tavily — AI search engine |
| [[exa-labs]] | Exa Labs — semantic search |
| [[dataforseo]] | DataForSEO — SEO data API |
| [[scrapingdog]] | ScrapingDog — web scraping API |
| [[fetcher]] | Fetcher — data extraction tool |
| [[enrichlayer]] | EnrichLayer — LinkedIn enrichment |
| [[bright-data]] | Bright Data — proxy/network data |
| [[unwind-ai]] | Unwind AI — workflow tool |
| [[unipile]] | Unipile — LinkedIn/email automation |
| [[chatwoot]] | Chatwoot — open-source customer support |
| [[entri]] | Entri — domain/DNS automation |
| [[awesome-llm-apps]] | Curated LLM app examples reference |

## Data & Memory Infrastructure

| Entity | Description |
|---|---|
| [[duckdb]] | DuckDB — local analytics engine |
| [[motherduck]] | MotherDuck — cloud DuckDB |
| [[obsidian-auto-filing-rules]] | Obsidian auto-filing rules |
| [[obsidian-home-lab-documentation]] | Obsidian home-lab doc patterns |
| [[obsidian-self-organizing-vault]] | Self-organizing Obsidian vault |
| [[sovereign-stack]] | Sovereign Stack — local-first stack |

## Business & Sales Tools

| Entity | Description |
|---|---|
| [[dubb]] | Dubb — video email tool |
| [[vidyard]] | Vidyard — video hosting/analytics |
| [[drop-cowboy]] | Drop Cowboy — ringless voicemail |
| [[mailgun]] | Mailgun — email API |
| [[wefunder]] | Wefunder — equity crowdfunding |
| [[paperclip]] | Paperclip — sales/marketing tool |
| [[onyx]] | Onyx — knowledge management |
| [[vibe-prospecting]] | Vibe Prospecting — sales approach |

## Real Estate & Finance

| Entity | Description |
|---|---|
| [[boom-automations-25-industries]] | Boom Automations — 25 industries playbook |
| [[cdfi-underwriting-framework]] | CDFI underwriting framework |
| [[whatcom-county-housing-developers]] | Whatcom County housing developers |
| [[gpc-development]] | GPC Development — client/prospect |
| [[gpc-onboarding]] | GPC onboarding workflow |

## Frameworks & Concepts

| Entity | Description |
|---|---|
| [[klick2client-os]] | Klick2Client OS — B2B acquisition OS |
| [[pending-exa-people-search-skill]] | Pending: Exa people search skill |
| [[agency-agents]] | Agency agents roster (also has subdir) |

---

# Projects

## Active Client Projects

| Project | Status | Description |
|---|---|---|
| [[idc-insurance-client]] | active (P1) | IDC Insurance Direct Canada — Stage 1 (Topical Authority) complete |
| [[signal-intelligence-agent]] | active dev | Signal Intelligence Agent — 3-stage pipeline, 5 search engines, MiniMax via Ollama for context extraction |
| [[klicksmartai-agent-squad-buildout]] | planning | Dennis's Personal Agent Squad — 6-agent framework (Monica=Hermes, Dwight=Research, Kelly=Social, Rachel=LinkedIn, Ross=Build, Pam=Briefing) |

## Subdirectory Projects

### commercial-mortgage-os
- `01-product-brief.md` (11.6K) — product definition
- `02-proposal.md` (6.1K)
- `03-ad-copy-outreach.md` (11.6K)
- `04-one-pager.md` (4K)

### mortgage-broker-os
- `01-product-brief.md` (9.2K)
- `02-proposal-lead-to-funded.md` (4.6K)
- `03-ad-copy-outreach-scripts.md` (9.7K)
- `04-one-pager.md` (3.7K)
- `05-linkedin-outreach.md` (7.9K)
- `README.md` (2.2K)

### klicksmartai-com-gtm-site
- `SPEC.md` (12.5K) — GTM site specification

### rios-mortgage-intelligence-exchange
- `01-architecture.md` (18.5K) — RIOS architecture

---

# Signal Intelligence Agent — Detail

**Core philosophy:** Topical authority-driven signal matching, not generic lead gen.

**3-stage pipeline:**
1. **Topical Authority Analysis** (new) — crawl client site, build Topic Authority Map with adjacent topics
   - Tools: `firecrawl_map`, `firecrawl_scrape`, `notebooklm_mcp`
2. **Signal Intelligence Agent** (core) — multi-engine search across 5 engines (Brave + Serper + Tavily + Exa + DataForSEO), dedupe/merge, prioritize Tavily/Exa for richer context
   - Context extraction model: MiniMax via Ollama
   - Outputs: who/what/where/when/industry/event-type
3. **Lead Generation** — match signals to ICP, generate outreach, output to CRM/GHL/CSV

**5 core capabilities:**
1. 🧠 Signal Detection (multi-engine parallel)
2. 🧾 Context Extraction (5W1H)
3. 🎯 Signal Classification (event type, ICP relevance, topical match)
4. ⚡ Opportunity Scoring (urgency 1-10, timing trigger, deal value, topical fit)
5. 🚀 Action Generation (outreach angle, message, channel)

---

# IDC Insurance Direct Canada — Detail

| Field | Value |
|---|---|
| Legal Name | I.D.C. Insurance Direct Canada Inc. |
| Domain | insurancedirectcanada.com |
| Founded | 1999 |
| Founder | Russ Smart |
| CEO | Binh Nguyen (ben-nguyen-canada on LinkedIn) |
| Address | 4400 Dominion St. #260, Burnaby, BC V5G 4G3 |
| Business Model | Direct-to-consumer life insurance marketplace, 30+ carriers |
| Scale | $2B+ coverage sold, 12,000+ clients, 300+ years combined advisor experience |
| Commission | Carrier-paid, no client fees |
| Service Area | All Canadian provinces |
| Status | Active client, Stage 1 (Topical Authority) complete |

**Stakeholders:** Dennis E. (KlickSmartAI), Binh Nguyen (CEO), Ben Nguyen (CEO), Russ Smart (Founder/Consultant), Kevin Panoncic (Hiring Manager)

---

# KlickSmartAI Agent Squad — Detail

Dennis's personal Chief of Staff system (the OS that runs his day, clients, and growth).

**Current friction points:**
- Too many manual handoffs between research → content → outreach
- Signal intelligence not flowing into daily workflow
- Content creation is still manual (LinkedIn posts, briefs)
- Client updates require Dennis to pull instead of being pushed
- Too much context switching between client contexts

**Squad framework (Shubham Saboo's 6-agent model):**

| Character | Original Job | Dennis's Parallel | Status |
|---|---|---|---|
| **Monica** | Chief of Staff | **Hermes** (this agent) | ✅ Live |
| **Dwight** | Research (3x/day signal sweeps) | Research Agent | 🟡 Partial |
| **Kelly** | X/Twitter social content | Social Agent | ❌ Missing |
| **Rachel** | LinkedIn thought leadership | LinkedIn Agent | ❌ Missing |
| **Ross** | Engineering/code reviews | Build Agent | ❌ Missing |
| **Pam** | Newsletter/digest | Briefing Agent | ✅ Partial (7:57 AM cron) |

---

# Related

- [[klicksmartai-wiki-architecture]] — Master repo architecture
- [[context7]] — Upstash Context7 setup
- [[klicksmartai]] — Top-level entity
- [[dennis-eng]] — Owner profile
- [[hermes-agent]] — Hermes Agent local setup
- [[klick2client-os]] — B2B acquisition OS
- [[ncf-national-christian-foundation]] — NCF profile
- [[spectra-holdings-group]] — Spectra Holdings profile
