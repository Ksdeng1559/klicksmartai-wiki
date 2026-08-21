---
product_id: leadsniperai
status: active
version: 2.1
last_updated: 2026-06-30
parent_offers: [leadsniperai, ai-sdr]
---

# LeadSniperAI — Product Definition

> **LeadSniperAI is a dual-purpose prospecting engine. It finds and scores local businesses for two distinct service lines: website rebuilds (via WebMorphasis) and AI SDR outreach. One discovery pipeline, two revenue streams.**

## Mission

Find local service businesses on Google Maps and qualify them for one of two offers:

### Subgoal 1: Website Rebuild (WebMorphasis)

Find businesses whose website doesn't exist or is outdated. Pitch: "Your site is costing you customers. Here's a modern one."

| Trigger | Detection | Offer |
|---|---|---|
| No website | GMB has no `website_uri` | Custom website build, $497-$1,997/mo |
| Outdated website | 6-signal scan: 2+ of [no HTTPS, no viewport, no OG, no schema, copyright stale, deprecated CMS] | Modern AI-search-ready rebuild, $497-$1,997/mo |

### Subgoal 2: AI SDR Outreach

Find businesses with proven quality but missing social proof. Pitch: "Your customers love you — but Google doesn't know that yet."

| Trigger | Detection | Offer |
|---|---|---|
| High rating, low reviews | 4.5+★ with 1-25 reviews | AI-powered review generation + lead gen, $497-$1,497/mo |

**Both subgoals use the same pipeline.** The difference is which downstream channel gets the qualified prospect.

```
                    LeadSniperAI Pipeline
                 ┌──────────────────────────┐
                 │  Discover → Crawl → Score │
                 └───────────┬──────────────┘
                             ↓
              ┌──────────────┴──────────────┐
              ↓                             ↓
   ┌────────────────────┐        ┌────────────────────┐
   │  SUBGOAL 1         │        │  SUBGOAL 2         │
   │  Website Rebuild   │        │  AI SDR Outreach   │
   │  (WebMorphasis)    │        │                    │
   │                    │        │                    │
   │  Trigger:          │        │  Trigger:          │
   │  Opp Score ≥ 70    │        │  SDR Score ≥ 50    │
   │                    │        │                    │
   │  Offer:            │        │  Offer:            │
   │  $497-$1,997/mo    │        │  $497-$1,497/mo    │
   └────────────────────┘        └────────────────────┘
```

## Architecture

LeadSniperAI has one pipeline with 7 steps. The output routes to one or both channels based on which thresholds the prospect clears.

```
Step 1: GMB Discovery (DataForSEO MCP + leads table)
Step 2: Scrapling Crawl (HTTPS, viewport, OG, schema, copyright, CMS)
Step 3: Technical Audit (phones, emails, forms, CTAs)
Step 2.5: OIL Pre-score Gate (fast signals — save tokens)
Step 4: ScrapeGraphAI Extraction (LLM — business meaning, gated by OIL)
Step 5: Opportunity Score (5-component, 0-100)
Step 6: Outreach Angle (personalized hook)
Step 7: Proposal / Rebuild Plan
```

## Scoring Systems

### Opportunity Score (Subgoal 1: Website Rebuild)
0-100, pass ≥ 70. "How strong is this prospect for a website rebuild?"

| Component | Max | What |
|---|---|---|
| GMB Strength | 25 | Rating + reviews + velocity (-3/+2) + claimed |
| Website Weakness | 25 | Missing HTTPS, OG, schema, viewport, copyright, outdated |
| AI Search Gap | 20 | Schema count, FAQ, blog, pages, local schema |
| Contactability | 15 | Phone, email, contact form, booking, hours |
| Revenue Potential | 15 | Vertical value + lead_score + website weakness |

### AI SDR Score (Subgoal 2: Outreach)
0-100. "How good is this business as an outreach candidate?"

| Component | Weight | Rationale |
|---|---|---|
| Rating | 20% | High rating = proven quality + pitch leverage |
| Review gap | 30% | 1 review = 100, 25+ = 0 (biggest lever) |
| Has phone | 15% | Must be contactable |
| Has website | 10% | Has an online presence to optimize |
| Is claimed | 10% | Actively manages their GMB |
| Is local | 15% | Real address, not a PO box |

### AI SDR Service Tiers

| Tier | Trigger | Price/mo | Service |
|---|---|---|---|
| **Reputation Builder** | 1-5 reviews | $497 | Email past customers → 25+ reviews in 90 days |
| **Lead Generator** | 6-15 reviews | $997 | Identify in-market homeowners + book estimates |
| **Full Funnel** | 16-25 reviews | $1,497 | Outbound + AI-qualified leads + monthly reporting |

### OIL Pre-Score (Token Gate)
0-100, gate ≥ 40. Pre-screens before ScrapeGraphAI.

| Component | Max |
|---|---|
| GMB Quality | 30 |
| Web Health | 15 |
| Outdated Signals | 25 (more outdated = higher) |
| Business Presence | 15 |
| Market Value | 15 |

### Lost Revenue v2
Quantifies what the business is losing. 14 verticals, 3 modes (conservative/standard/aggressive).

## How One Prospect Routes to Both Channels

A single business can qualify for both subgoals:

```
Business: Sage Family Dental
  ↓
Pipeline scores: Opp 76, SDR 66
  ↓
  ├─→ Subgoal 1: Opp ≥ 70 ✓ → WebMorphasis proposal ($997/mo Growth tier)
  └─→ Subgoal 2: SDR ≥ 50 ✓ → AI SDR outreach ($1,497/mo Full Funnel tier)
  ↓
Total agency revenue if both close: $2,494/mo
```

## Double-Play Economics

A "double-play" prospect clears both thresholds — weakest website AND strongest AI SDR profile.

| Scenario | Monthly Revenue | Prospects (of 27) |
|---|---|---|
| WebMorphasis only | $497 — $1,997 | 3 |
| AI SDR only | $497 — $1,497 | 21 |
| **Double-play (both)** | **$994 — $3,494** | **3** |

The 3 double-play prospects: Sage Family Dental, Emergency Dental of Denver, Chicago Style Smiles — all dentists with strong GMBs but weak or modern websites.

## Key Insight: AI SDR Is the Volume Play

While only 11% of audits pass the Website Rebuild threshold (Opp ≥ 70), **89% qualify for AI SDR outreach** (SDR ≥ 50). The agency's revenue floor is set by AI SDR volume, while the ceiling is raised by the double-play prospects.

| Metric | Website Rebuild | AI SDR Outreach |
|---|---|---|
| Pass rate (27 audits) | 3/27 (11%) | 24/27 (89%) |
| Price range | $497-$1,997/mo | $497-$1,497/mo |
| Selling point | "Your site is invisible" | "Your reviews don't reflect your quality" |
| Fulfillment | WebMorphasis builds site | AI SDR runs outreach campaigns |

## Current Metrics (2026-06-30)

| Metric | Value |
|---|---|
| Audits in Supabase | 27 |
| Website Rebuild targets (Opp ≥ 70) | 3 |
| AI SDR targets (SDR ≥ 50) | 24 |
| Double-play (both) | 3 |
| Total pipeline ceiling (all close) | $9,500-$19,000/mo |
| Total addressable lost revenue | $19.2M/yr |

## Tech Stack

| Layer | Tech | Version |
|---|---|---|
| Web crawler | Scrapling | 0.4.8 |
| AI extractor | ScrapeGraphAI | 2.1.4 |
| GMB discovery | DataForSEO MCP | 83 endpoints |
| Database | Supabase | yolqrstktoqlszybwymw |
| PDF | reportlab | 5.0.0 |
| LLM | DeepSeek v4 Pro | via Hermes Agent |
| Python | 3.14 | — |

## Source & Run Commands

**Repo:** `C:/Users/denni/AI-Applications/LeadSniper-3.0/scripts/`

```bash
# Full pipeline (both subgoals scored)
py -3.14 workflow.py --business "Sage Family Dental" --no-scrapegraph

# AI SDR targeting (Subgoal 2)
py -3.14 ai_sdr.py --vertical "home builder" --city "Vancouver" --persist --send
```

## Decisions

D-2026-06-30-06 through D-2026-06-30-16 cover: mission, outdated definition, Denver exclusion, two-scraper architecture, 5-component scoring, OIL, AI SDR, continuous monitoring. D-2026-06-30-16 establishes AI SDR as a co-equal subgoal alongside Website Rebuild.
