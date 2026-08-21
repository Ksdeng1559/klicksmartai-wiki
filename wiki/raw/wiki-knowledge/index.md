# Wiki Index

> Content catalog. Every wiki page listed under its type with a one-line summary.
> Last updated: 2026-04-16 | Total pages: 17

## Entities
- [[alexander-eng-toy-nissan-gtr]] — Alexander Eng's yellow toy Nissan GT-R die-cast collectible
- [[agency-agents]] — 147 MIT-licensed AI agents (msitarzewski), 81K stars, Finance + Legal divisions
- [[boom-automations-25-industries]] — Luke Pierce's guide: 300+ AI automation opportunities across 25 industries, $5K–$60K project range, 10 pain points + 3 discovery questions per vertical. Built from 4 years and 80+ client engagements.
- [[cc-for-everyone]] — Carl Vellotti's free Claude Code course (ccforeveryone.com), 19 modules
- [[claude-code-guide]] — Florian Bruniaux's comprehensive Claude Code guide: 24K lines, 240 templates, 271-question quiz, 15-vulnerability security DB, TDD/BDD workflows, multi-agent teams. Free & open-source.
- [[chatwoot]] — Open-source customer support platform, AI agent (Captain), omnichannel inbox, self-hosted
- [[dennis-e]] — Primary user of the Hermes Agent via Telegram, active in Vancouver BC
- [[drop-cowboy]] — Ringless voicemail + SMS platform, TCPA compliant, financial advisors vertical
- [[duckdb]] — Open-source analytical OLAP database, columnar-vectorized, embedded, MIT licensed
- [[dubb]] — Video communication platform for sales leaders — personalized video outreach, AI writing + chat, CRM, automation
- [[dubb-use-case-elite-insurance]] — Dubb case study: Elite Insurance of Merrillville — financial advisor stands out in commoditized market with personalized video
- [[dubb-use-case-kinsta]] — Use case: Video-first outreach with Dubb — Kinsta cut response time in half in week one
- [[video-email-outreach-effectiveness-research]] — Research brief: video email/outreach stats — 3x reply rates, 25-30% video reply rates vs 1-5% text
- [[sms-mms-outreach-effectiveness-research]] — Research brief: SMS/MMS stats — 98% SMS open rate, 45% response, MMS 300% higher engagement than SMS
- [[outreach-channel-comparison-battle-card]] — Battle card: full outreach channel comparison — email, video, SMS, MMS, LinkedIn stats + pitch scripts
- [[entri]] — Domain API platform: DNS, SSL, domain selling, monitoring (entri.com)
- [[gpc-development]] — New website project, GPC Development Ltd., Suite 2100-1177 W. Hastings St, Vancouver BC
- [[gpc-onboarding]] — GPC onboarding tracker (D1-PR3 checklist, discovery to launch)
- [[mailgun]] — Transactional email API service (mailgun.com/pricing/)
- [[ollama]] — Local LLM runtime with streaming, tool calling, vision, embeddings, and web search API
## Lead Enrichment & Research Stack

**Research layer** (web content + signals) + **enrichment layer** (structured profile data). Use Tavily for AI-native deep research, Exa for financial/neural, Brave for broad multi-format, Serper for Google-specific SERPs, EnrichLayer for structured professional/company profiles.

### Research — Web Content & Signals
- [[tavily]] — "Real-time search engine for AI agents & RAG." 180ms p50 (fastest), 1M+ developers, #1 on DeepResearch Bench. **5 tools** (`tavily_search`, `tavily_extract`, `tavily_crawl`, `tavily_map`, `tavily_research`). **MCP server** `tavily-mcp` ⭐1,796 (STDIO). **✅ Wired to Hermes** (v0.2.18). **Use for:** grounding LLMs, deep prospect research, anti-hallucination, RAG pipelines, bulk site crawling. **Best fit for HUBERT-X primary search.**
- [[exa-labs]] — Neural + keyword hybrid, live web crawling, company/news/tweet/financial/code/research-paper/personal-site filters. **Lead Gen skill:** subagent-driven ICP scoring, micro-verticals, structured output, CSV export via `deep_search_exa`. 4,277-star MCP server. **✅ Wired to Hermes** (`deep_search_exa` via `?tools=deep_search_exa` endpoint). **8 skills:** `exa-lead-generation`, `exa-company-research`, `exa-people-research`, `exa-code-search`, `exa-news-search`, `exa-financial-research`, `exa-research-paper-search`, `exa-personal-site-search`. **Use for:** GTM intelligence, recruiting, grounded code, news monitoring, financial/regulatory filings.
- [[brave-search-mcp-server]] — Privacy-first, 6 tool types + AI summarizer. 913 stars. **✅ Wired to Hermes** (`brave_web_search`, `brave_local_search`). API key configured. **Use for:** broad multi-format discovery, summarization, local search.
- [[serper]] — "World's fastest/cheapest Google Search API." $0.30/1K, 1-2s latency. **✅ Wired to Hermes** (`google_search`, `scrape`). Real Google SERPs. **Use for:** Google SERP intelligence, keyword research, competitive analysis, lead intent tracking. No MCP for Hermesp; direct Python/Node SDK calls.
- [[dataforseo]] — SEO/keyword data API. **69 tools**: SERP, keyword volumes, rank tracking, backlinks, AI mention tracking, tech stack. **MCP server** ⭐. **✅ Wired to Hermes** (v2.8.9). **Use for:** keyword intent classification, competitor gap analysis, AI citation tracking, rank monitoring. Paid account: sales@klicksmartai.com.

### Enrichment — Structured Profile Data
- [[enrichlayer]] — **1.2B+ professional profiles, 70M+ companies, 210M+ jobs.** 1 credit = 1 successful API call, 432K profiles/day default throughput. Python SDK (`enrichlayer-api` ⭐2, PyPI). asyncio/gevent/twisted concurrency native. **Use for:** LinkedIn URL → structured profile (job history, skills, education, company, headline). Pipeline: GMB discovery → EnrichLayer → PSQ Scoring → HUBERT-X ranker. **Best for per-lead enrichment in recruiting pipeline.**
- [[vibe-prospecting]] — **150M+ businesses, 800M+ profiles, 4,000+ data signals.** MCP server ⭐19 (Gemini CLI native, OAuth auto-auth). Plans: Free → $89 → $199 → $649/mo. **Use for:** lead list building by criteria, contact discovery (emails/phones), outreach personalization, recruiting candidate search. **Native MCP** — directly wireable to Hermes/Gemini CLI. Alternative: `mcp-explorium` ⭐21. **Complementary to EnrichLayer** — larger data network, MCP-native.
- [[scrapingdog]] — **Web scraping API with proxy rotation + headless browsers.** LinkedIn Scraper API + Profile Scraper API. 4.8★ Trustpilot (577 reviews), 1000 free credits trial. ~$0.009/profile at Enterprise tier. **Use for:** raw LinkedIn/profile page extraction when EnrichLayer doesn't have a profile. Direct REST API only (no SDK).
- [[bright-data]] — Enterprise scraping: 437+ pre-built scrapers, 150M+ residential proxy pool. ~$0.05/profile. Best for high-volume bulk scraping + pre-collected datasets. **Complement to EnrichLayer and Scrapingdog** — not a direct competitor.
- [[fetcher]] — **AI recruiting platform: inbound + outbound sourcing.** Starts $379/mo, rollover credits, Amplify plan (human sourcing). Direct **HUBERT-X competitor** — use for pricing benchmark and feature gap analysis. Study Fetcher's credit model, Amplify tier, and positioning to differentiate HUBERT-X. Self-hosted HUBERT-X advantage: unlimited candidates, no per-credit costs, full data ownership.
- [[onyx]] — Enterprise AI search & knowledge platform, 45+ permission-aware connectors, self-hostable, SOC 2 Type II, financial services secure AI
- [[motherduck]] — MCP server connecting AI assistants to DuckDB analytics, natural language SQL, sandboxed compute
- [[paperclip]] — Paperclip.ing — reference model: "human control plane for AI labor," autonomous company OS
- [[sovereign-stack]] — Manoj Saharan's Sovereign Stack: replaces GHL with Mailgun + DuckDB + Claude Code + Chatwoot + Unipile
- [[unipile]] — Unified Communication API: LinkedIn, Gmail, WhatsApp, Telegram + outreach sequences, unified inbox
- [[vidyard]] — AI-powered video selling platform — personalized video, AI avatars, Video Agent, CRM integrations, 2x response rates
- [[insurance-direct-canada-lead-research]] — Live research: term life #1 searched product in Canada, lead gen landscape (HelloSafe/InsuranceHotline/QuoteRack/BGM), lead type benchmarks ($50–$150/exclusive term, $1.25–$5/aged), final answer: Term 10 is most-searched. Strategic recs for IDC + HUBERT-X to position as AI-powered lead platform for brokers.
- [[claude-partner-network]] — Anthropic's formal partner program. $100M committed, free membership, certifications, market development funds, eligible for investment.
- [[wattbricks]] — New project, wattbricks.com — brand intel from live site + Energy Independence deck
- [[wefunder]] — Public Benefit Corporation crowdfunding platform. $1B+ raised, 4,409 founders funded, 1M+ investors. $250 median investment. API + Agents platform. Mission: 20,000 founders in all 50 states.
- [[wealth-wire-radar]] — Signal-driven intelligence platform for Canadian financial advisors (Westward Advisors)
|- [[obsidian-home-lab-documentation]] — Adam Conway's XDA guide: numbered folder structure (0-Meta → 6-Design), YAML frontmatter + Dataview for live server/service inventory tables, Excalidraw network diagrams, incident tracking. Plaintext alternative to NetBox/HomeBox.
|- [[obsidian-self-organizing-vault]] — Nolen Jonker's XDA guide: QuickAdd + Auto Note Mover + Claude for vault self-organization. Two plugins, 30-min setup, zero manual filing after.
|- [[obsidian-auto-filing-rules]] — QuickAdd commands + Auto Note Mover rules for Dennis's wiki vault. Tag triggers, template files, and frontmatter schemas for entities/concepts/raw/projects/meetings.

## Concepts
- [[about-this-wiki]] — Meta page explaining the wiki's purpose, structure, and conventions
- [[search-stack]] — Hermes search engine inventory + routing: Brave (default) → Serper → Exa → Parallel.ai; Parallel replaces Exa/Tavily for LLM-grounding but NOT SERP providers
- [[swan-gtm-gtm-skills]] — Swan's open GTM skills library (267 SKILL.md, 45 authors): RevOps, Outreach, Ads, Signals, ABM. Ingested from GitHub + Notion summary
- [[leadsniper-sgi-prd]] — LeadSniper SGI: AI domain audit + SERP intelligence + GTM recommendation app. Operating model Audit→Evidence→Opportunity→Recommendation→GTM→Execution→Measurement
- [[progressive-enrichment-architecture]] — Explorium reference: size market → resolve company → qualify account → buying committee → enrich selectively → activate. 6-stage progressive enrichment cost-control model + LeadSniperAI architecture
- [[boss-raas-v3]] — BOSS v3 Financial Services RaaS: 7-layer Revenue Conversion Machine (Signal→Enrich→Score→Act→Learn→Adapt). 4-phase build roadmap, 16-agent workforce, DuckDB feedback loop, Smartlead + LinkedIn DM execution. Source: raw/reference/BOSS-RaaS-v3-Revenue-Conversion-Machine.docx
- [[hermes-agent]] — Self-improving autonomous AI agent by Nous Research, 64K+ GitHub stars
- [[hermes-agent-setup-guide]] — Alex P.'s comprehensive VPS setup walkthrough for Hermes Agent
- [[klick2client-os]] — Klick2Client OS v1.0 product definition: 6-layer B2B LinkedIn client acquisition system. Two entry paths (warm/cold), PSQ scoring, 360-day lifecycle engine, Sales Battlecard output. Raw reference: raw/reference/Klick2Client_OS_Product_Definition_v1.0.docx
- [[ai-revenue-engine]] — AI Revenue Engine v2.0 for Local Businesses: 6-layer stack, OpenClaw orchestrator, Twilio SMS, Cal.com booking, Smartlead, 19-agent roster. Phase 1: plumbers + HVAC Vancouver. DFY → white-label. Source: raw/reference/AI_Revenue_Engine_Architecture.docx
- [[openclaw-matt-ganzak]] — Matt Ganzak's OpenClaw Agent Training Guide: Project Folders + Task Folders, 3-tier model routing, Master Router, cold outreach, QC agent. Source: raw/reference/openclaw_training_guide.md
- [[openclaw-token-calibration]] — 5-step token calibration (ScaleUP Media SPRINT): train OpenClaw to estimate task cost before running. 10-15% accuracy after 3-4 rounds. Source: raw/reference/openclaw_token_calibration_guide.md
- [[claude-code-scheduled-tasks]] — KlickSmartAI Personal Playbook: Claude Code scheduled tasks framework. 3 types (Cloud/Desktop/loop), 5 ready-to-use prompts (Morning Briefing, Competitor Watchdog, PR Reviewer, Content Calendar, Session Poller). Source: raw/reference/claude-code-scheduled-tasks.docx
- [[boss-raas]] — BOSS v3 Financial Services RaaS: 7-layer Revenue OS, signal-first waterfall, PSQ scoring, 4-phase roadmap. Companion: BOSS SIP + BOSS SIP Onboarding. Source: raw/reference/BOSS-RaaS-v3-Revenue-Conversion-Machine.docx + raw/reference/BOSS-SIP-Implementation-Plan-v1.docx
- [[boss-sip-onboarding]] — Financial Services onboarding flow for SIP + vertical engine setup. 8-step sequence, intake form, validation checklist, context directory structure.
- [[sovereign-stack]] — Manoj Saharan's Sovereign Stack: replaces GHL with Mailgun + DuckDB + Claude Code + Chatwoot + Unipile
- [[wwr-signal-pipeline]] — 9-step signal detection pipeline from search to battlecard storage
- [[wwr-relationship-manager]] — v2.0 relationship graph with BFS pathfinding and proximity scoring
- [[wwr-battlecard-format]] — ASCII battlecard format, RM brief upgrade, outreach templates
- [[client-acquisition-roadmap]] — Zero to first 5 customers: organic vs paid growth, Sabrina's success framework, lean growth mindset
- [[user-acquisition-roadmap]] — High-impact user acquisition: zero-to-one imperative, value-first outreach, community-centric growth, content-led engine, AI-SEO, paid acceleration, channel prioritisation matrix
|- [[insurance-direct-canada-recruitment-agent]] — Insurance Direct Canada 24/7 AI recruitment agent. TDD-first build via `HUBERT_X_Implementation_Playbook.md`. Track 1 (New Recruit) MVP: ~25h dev + 1.5h Dennis. Track 2 (Advisor Poach): ~15h after Track 1 stable.
- [[first-100-clients-playbook]] — Customer acquisition playbook: synthesised from Sabrina + Growth Architect + Value-First Marketing Primer — Mini-Me case study, LLM search authority, low-friction inquiry, first-hour rule, 80/20 Upwork, vibe-coded lead magnets, Book Talk viral replication, anti-fragile growth mindset
- [[wefunder-operating-system]] — Dennis Eng's core belief system. Wefunder's public benefit charter mirrors KlickSmartAI's mission: democratize access to capital/tools for ambitious builders, fight cynicism and gatekeeping, crowd-wisdom over gatekeepers. The operating system underneath HUBERT-X and Klick2Client OS.
- [[wefunder]] — Public Benefit Corporation crowdfunding platform. $1B+ raised, 4,409 founders funded, 1M+ investors. $250 median investment. API + Agents platform. Mission: 20,000 founders in all 50 states.
- [[claude-blog-skill]] — Claude Code blog writing skill. `/blog write` → research-backed, SEO + AI citation optimized articles with quality scoring and human review loop. Pending installation.

## Comparisons

## Queries

## Raw
- [[raw/drafts/website-build-onboarding-sop]] — Full SOP: discovery, deposit, content, PRD, wireframe, build, launch
- [[raw/drafts/gpc-development-prd]] — PRD: GPC Development website (8 services, pages, messaging, design direction)
- [[raw/drafts/wattbricks-energy-independence-deck]] — Energy Independence deck notes (slides 1-3)
- [[raw/drafts/ai-tools-for-financial-professionals-course-outline]] — Course outline: 30 lessons, 5 sections, $197 launch price
- [[raw/articles/claude-linkedin-prompt-library]] — John Peslar's Zevari: 18 LinkedIn workflows, 131 skills, 6 personas, DISC/ICP/Outreach frameworks, skill chains, safety system
- [[raw/reference/Klick2Client_OS_Product_Definition_v1.0.docx]] — Original product definition document from Klick2Client (source-of-truth)
- [[templates/pipeda-consent-screen]] — Standard PIPEDA consent screen for financial advisor OS deployments. GAP-19 aligned, 6-section layout, implementation checklist.
