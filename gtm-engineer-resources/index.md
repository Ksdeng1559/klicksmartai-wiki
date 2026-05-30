# GTM Engineering Resources

Curated tools, platforms, and data sources that form the GTM Engineering stack — the technical infrastructure KlickSmartAI uses to build client acquisition pipelines, signal intelligence systems, and outbound workflows.

> **Positioning note:** GTM Engineering Resources are the *building blocks* KlickSmartAI assembles for clients. When building a Spectra Holdings pipeline, Explorium provides the B2B data layer; EnrichLayer handles per-profile enrichment; Bright Data handles bulk company research; Apify powers the signal detection layer. The skill is in knowing which tool goes where in the pipeline.

---

## Categories

- **[01-data-enrichment](01-data-enrichment/)** — B2B contact & company data providers, enrichment APIs
- **[02-web-intelligence](02-web-intelligence/)** — Web scraping, proxies, datasets, Crawling APIs
- **[03-signal-intelligence](03-signal-intelligence/)** — News monitoring, social listening, event detection
- **[04-outbound-automation](04-outbound-automation/)** — Email sequencing, LinkedIn automation, multichannel outreach
- **[05-engagement-infrastructure](05-engagement-infrastructure/)** — CRM, email delivery, scheduling, chat
- **[06-workflow-orchestration](06-workflow-orchestration/)** — Automation platforms, pipeline builders, integration layers

---

## Resource Master List

| Resource | Category | Status | Client Relevance |
|----------|----------|--------|-----------------|
| [Explorium AI](./01-data-enrichment/explorium-ai.md) | 01-Data Enrichment | ✅ Active | Spectra, IDF, any B2B |
| [EnrichLayer](./01-data-enrichment/enrichlayer.md) | 01-Data Enrichment | ✅ Existing | Spectra, IDC, IDF |
| [Apollo](./01-data-enrichment/apollo.md) | 01-Data Enrichment | 🔲 Catalogued | Lead lists, enrichment |
| [Clay](./01-data-enrichment/clay.md) | 01-Data Enrichment | 🔲 Catalogued | Enrichment + AI workflows |
| [Bright Data](./02-web-intelligence/bright-data.md) | 02-Web Intelligence | ✅ Existing | Bulk research, CSE |
| [Apify](./02-web-intelligence/apify.md) | 02-Web Intelligence | ✅ Active | Signal detection, CSE |
| [Scrapingdog](../entities/scrapingdog.md) | 02-Web Intelligence | ✅ Existing | Raw profile scraping |
| [Instantly.ai](./04-outbound-automation/instantly.md) | 04-Outbound Automation | 🔲 Catalogued | Email warmup + sending |
| [Phantombuster](./04-outbound-automation/phantombuster.md) | 04-Outbound Automation | 🔲 Catalogued | LinkedIn automation |
| [Mailgun](../entities/mailgun.md) | 05-Engagement Infrastructure | ✅ Existing | Transactional email |
| [n8n](./06-workflow-orchestration/n8n.md) | 06-Workflow Orchestration | 🔲 Catalogued | Self-hosted automation |
| [Claude Code + AgentSource](./06-workflow-orchestration/claude-code-gtm-automation.md) | 06-Workflow Orchestration | ✅ Active | Stack consolidation — reasoning vs. routing, 5→2 failure points |

---

## By Client Use Case

### Spectra Holdings Group (MCF county pipeline)
- **Reasoning layer:** Claude Code + AgentSource (replaces n8n + Clay + Zapier — 5→2 failure points)
- **Data layer:** Explorium (97.8% accuracy B2B data) + Bright Data (county org research)
- **Enrichment:** EnrichLayer (per-profile) + Apollo (lead lists)
- **Signal detection:** Apify (news + event crawlers) + Explorium signal engine
- **Outbound:** Klick2Client OS (LinkedIn + Email lifecycle engine)
- **Delivery:** Faith-framed advertorial + investor brief

### Insurance Direct Canada (IDC)
- **Lead research:** EnrichLayer + Bright Data
- **Enrichment:** Apollo + Clay
- **Outbound:** Klick2Client OS sequencing

### General B2B Pipeline
- **Signal → Enrich → Outbound → Convert** — full stack via GTM Engineering resources

---

*Last updated: 2026-05-29*