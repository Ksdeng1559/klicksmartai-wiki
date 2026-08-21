# n8n

**Category:** 06-Workflow Orchestration
**Status:** 🔲 Catalogued
**URL:** https://n8n.io
**Pricing:** Cloud from €24/mo (2,500 executions); Self-hosted free (server costs ~$20–150/mo); Enterprise custom
**License:** MIT open source (self-hosted)
**Integrations:** 400+

---

## At a Glance

**"Open-source workflow automation — build anything, host anywhere, connect everything."**

n8n (pronounced "n-eight-n") is a workflow automation tool with 400+ integrations. Open source (MIT license) — can be self-hosted for free or use the cloud version. Used by developers and technical teams for complex automation pipelines. Positions as a Zapier alternative with more control and lower cost at scale.

**Key differentiator:** Open source + self-hosted = full control. Developer-friendly. Code嵌入 capability.

---

## Key Specs

| Spec | Detail |
|------|--------|
| **License** | MIT (open source, self-hosted free) |
| **Cloud pricing** | €24–800/mo (based on executions) |
| **Self-hosted cost** | ~$20–150/mo (server infrastructure only) |
| **Integrations** | 400+ |
| **Code execution** | Yes (JavaScript, Python in workflows) |
| **AI nodes** | Yes (OpenAI, Anthropic, LangChain, LlamaIndex) |
| **Use case** | Technical teams, custom pipelines, self-hosted automation |

---

## Key Features

| Feature | Description |
|---------|-------------|
| **400+ integrations** | Connect any tool in your stack |
| **Code nodes** | Run JavaScript/Python in workflows |
| **AI nodes** | LLMs, vector DBs, RAG pipelines |
| **Webhooks** | Trigger workflows from any external source |
| **Expressions** | Dynamic data transformation |
| **Sub-nodes** | Reusable workflow components |
| **Execution history** | Debug and rerun past runs |

---

## GTM Engineering Fit

### Pipeline Position
- **Workflow orchestration layer:** Connect signal detection → enrichment → outbound in custom pipelines
- **For technical teams:** Full control over automation logic without vendor lock-in
- **vs. Zapier:** More flexible (code nodes), cheaper at scale (self-hosted)
- **vs. Make:** Similar capability, n8n is open source

### Spectra Holdings Use Case
```
Apify crawler (funding signal) → webhook → n8n workflow →
EnrichLayer enrichment → Clay Waterfall → Klick2Client OS outreach
```
- Self-host on a $20/mo VPS for light pipeline automation
- Build custom signal → enrich → score → route pipelines
- Connect to Klick2Client OS via webhook triggers

### When to Self-Host vs. Cloud

| Factor | Self-Host | Cloud |
|--------|-----------|-------|
| Cost | ~$20–150/mo (server only) | €24–800/mo |
| Control | Full | Limited |
| Maintenance | You manage updates + security | Managed |
| Best for | Dev teams, custom pipelines | Non-technical teams |
| KlickSmartAI fit | ✅ Preferred for client pipelines | For quick prototyping |

---

## Complimentary Stack

| Layer | Tool | Role |
|-------|------|------|
| Signal detection | Apify | Crawl + detect |
| Workflow orchestration | n8n (self-hosted) | Connect all steps |
| Enrichment | EnrichLayer / Clay | Resolve contacts |
| Email + LinkedIn | Klick2Client OS | Outbound execution |
| AI decision layer | Hermes Agent | Orchestrate the pipeline |

---

*Source: n8n.io/pricing*