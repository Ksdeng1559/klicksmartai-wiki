---
title: RIOS LeadSniperAI — Inspection & AI Website Opportunity Engine
type: prd
status: architecture-spec
version: 1.0
owner: Dennis
primary-agent: Claude Code or Hermes Agent
companion-plan: implementation-plan.md
---

# RIOS LeadSniperAI — Inspection & AI Website Opportunity Engine

> Designed for Hermes Agent

## 1. Executive Vision

The agent is not a web scraper.

It is an autonomous Business Opportunity Discovery Engine.

Instead of simply collecting leads, it identifies businesses that are likely to purchase an AI-enabled website because their current site is underperforming.

The complete workflow is:

```
Google Grounding
│
Business Discovery
│
Lead Qualification
│
Website Inspection
│
Technical Audit
│
AI Search Audit
│
Opportunity Score
│
Proposal Generation
│
Website Generation
│
CMS Generation
│
CRM
│
Outreach
```

## 2. Objectives

The system should automatically:

- Discover businesses
- Visit websites
- Crawl websites
- Inspect website quality
- Measure AI Search readiness
- Detect technical problems
- Detect conversion issues
- Estimate opportunity value
- Produce a professional audit
- Generate a replacement website
- Generate CMS
- Store knowledge in RIOS

## 3. Core Technology Stack

### Discovery
Google Grounding API · Google Maps · Google Business Profile · Exa · Tavily

**Purpose.** Find businesses matching:
- High reviews
- Active business
- Weak website
- Outdated website
- Missing website

### Website Inspection — Primary: Scrapling

**Responsibilities.** Crawl entire website · Render JavaScript · Follow links · Read HTML · Detect CMS · Extract metadata · Extract Schema · Build website map

**Outputs.** `site.json`, `pages.json`, `images.json`, `links.json`, `schema.json`, `performance.json`

### AI Extraction Layer — Optional: ScrapeGraphAI

Extract services, staff, team members, pricing, FAQs, contact info, industries, products. Used only when page layouts vary significantly.

### AI Analysis — Claude Code

Interpret findings: Is SEO weak? Is EEAT weak? Is AI Search weak? Is schema missing? Are conversion opportunities being missed?

## 4. Website Inspection Module

The crawler inspects:

- **Technical**: HTML, CSS, JavaScript, images, PDFs, sitemap, robots.txt, favicon, canonical tags, OpenGraph, Twitter cards
- **Performance**: Page speed, Core Web Vitals, mobile friendliness, lazy loading, image optimization
- **SEO**: Titles, meta descriptions, H1–H6, internal links, broken links, redirect chains, duplicate titles
- **AI Search Readiness**: JSON-LD, Organization, LocalBusiness, FAQ, Review, Article, Breadcrumb, Person schema
- **Trust**: Testimonials, Google Reviews embedded, awards, certifications, licensing, case studies, privacy policy, terms, accessibility
- **Conversion**: Phone, email, forms, Calendly, live chat, CTA buttons, lead magnets, downloads, booking systems

## 5. Opportunity Scoring Engine

Each website receives a score across:

- Website Quality
- SEO
- Technical
- Performance
- Trust
- Conversion
- AI Search
- Content
- Brand
- Accessibility
- **Overall Score** (0–100)

**Example output**: Website Score **48 / 100**

## 6. Revenue Opportunity Engine

Estimates for:
- Website rebuild
- SEO opportunity
- AI Search opportunity
- Local SEO
- Monthly maintenance
- Content generation
- CMS
- Hosting

**Example**: $4,500 website · $800 AI Search · $300/mo CMS · $500/mo SEO · **Estimated LTV $14,000**

## 7. Proposal Generator

Claude automatically generates:
- Executive Summary
- Website Audit
- SEO Audit
- AI Search Audit
- Conversion Audit
- Competitor Comparison
- Pricing
- Recommendations
- Implementation Roadmap
- **PDF Proposal**

## 8. Website Generation

Claude Code generates a Next.js website with: Tailwind · SEO · Schema · Responsive pages · Blog · Landing pages · FAQ · Location pages · AI Search optimization.

## 9. CMS Generation

Auto-creates: Blog · Pages · Services · Staff · Projects · Testimonials · FAQs · Images · Downloads · News · Resources.

## 10. Knowledge Storage

Everything discovered is stored inside RIOS: Workspace · Business · Website · Audit · Proposal · Rebuild · CRM · Communications · Follow-up.

## 11. CRM Integration

Stores: Business · Owner · Website · Email · Phone · Opportunity Score · Proposal Status · Website Status · Pipeline.

## 12. Outreach

Integrations: Resend · Unipile · SmartLead · GoHighLevel.

Capabilities: cold email · LinkedIn · follow-up · meeting booking · proposal delivery.

## 13. Claude Code Responsibilities

Plan the crawl · coordinate Scrapling and optional ScrapeGraphAI extraction · analyze findings with LLM reasoning · produce structured JSON outputs · generate audits, proposals, and replacement websites · commit generated code to Git and prepare deployments.

## 14. Hermes Agent Responsibilities

Schedule discovery jobs · monitor crawl queues and retries · manage API quotas and rate limits · dispatch parallel inspection workers · store intermediate artifacts · trigger downstream analysis and outreach · track project status and notify on failures.

## 15. Phase 2 Roadmap

- Vision-based UI analysis using screenshots
- Lighthouse and PageSpeed Insights integration
- AI citation and answer-engine visibility scoring
- Competitor benchmarking
- Google Search Console integration
- GA4 integration
- Heatmap/session replay analysis
- Continuous website monitoring with change detection
- Automated monthly client health reports
- RIOS learning engine to improve opportunity scoring from historical win/loss data

## Success Metrics

| KPI | Target |
|---|---|
| Businesses analyzed per day | 1,000+ |
| Average audit generation time | < 3 minutes |
| Crawl success rate | > 95% |
| AI audit accuracy (manual review) | > 90% |
| Proposal generation time | < 60 seconds |
| Qualified opportunity rate | > 25% |
| Website-to-meeting conversion | > 10% |
| Proposal acceptance rate | > 30% |

---

*This PRD positions the agent as an autonomous AI Website Opportunity Engine rather than a scraper, aligning with the RIOS architecture and the strategy of identifying businesses that have already demonstrated market success but are underserved by their current web presence.*