# RIOS — Mortgage Intelligence Exchange
## Tech Stack Architecture v1.0

**Date:** May 29, 2026
**Owner:** Dennis / KlickSmartAI
**Status:** Planning — RIOS formation in progress

---

## Overview

RIOS (Residential + Commercial Mortgage Intelligence Exchange) is the tech stack foundation for the Klick2Client OS mortgage verticals.

Two verticals, one architecture:

| Layer | Residential Broker OS | Commercial Mortgage OS |
|-------|----------------------|----------------------|
| **Signal** | Realtor listings, courthouse filings, USDA eligibility | CMBS special servicers, maturity wall, broker network |
| **Enrichment** | Phone, email, intent signals, rate sensitivity | Property data, loan terms, servicer contact, sponsor intel |
| **Scoring** | Intent score (20 signals) | Deal complexity + urgency score |
| **Automation** | Ghost-busting sequences (8 touches, 21 days) | Stall prevention + maturity outreach |
| **Pipeline** | Lead → Pre-qual → App → UW → CTC → Funded | Pitch → Proposal → App → UW → Commitment → Closing |
| **Outbound** | Email (Instantly) + SMS + voicemail drops | Email (Instantly) + LinkedIn + direct mail |

---

## RIOS — System Architecture

```
                    ┌─────────────────────────────────────────┐
                    │           RIOS CORE ENGINE             │
                    │   (Claude Code + AgentSource)           │
                    └──────────────┬──────────────────────────┘
                                   │
           ┌───────────────────────┼───────────────────────┐
           │                       │                       │
    ┌──────▼──────┐        ┌──────▼──────┐        ┌──────▼──────┐
    │   SIGNAL    │        │  ENRICHMENT │        │   OUTBOUND  │
    │  LAYER      │        │   LAYER     │        │   LAYER     │
    ├─────────────┤        ├─────────────┤        ├─────────────┤
    │Web scraping │        │Phone/email  │        │Email warmup │
    │Realtor/Zill│        │intent data  │        │Instantly    │
    │Courthouse   │        │Rate sensit. │        │SMS (Twilio) │
    │USDA elig.   │        │Competitor   │        │LinkedIn     │
    │CMBS servicers│       │data         │        │Voicemail    │
    │MSCI/Trepp   │        │             │        │drops        │
    └──────┬──────┘        └──────┬──────┘        └──────┬──────┘
           │                       │                       │
           └───────────────────────┼───────────────────────┘
                                   ▼
                    ┌─────────────────────────────────────────┐
                    │        Klick2Client OS CORE             │
                    │  Lead Scoring │ Deal Tracking │ Pipeline │
                    └──────────────┬──────────────────────────┘
                                   │
               ┌───────────────────┼───────────────────┐
               │                   │                   │
        ┌──────▼──────┐    ┌──────▼──────┐    ┌──────▼──────┐
        │ RESIDENTIAL │    │  COMMERCIAL │    │  SHARED     │
        │ BROKER OS   │    │  MORTGAGE   │    │  SERVICES   │
        ├─────────────┤    ├─────────────┤    ├─────────────┤
        │Lead-to-funded│   │Deal intel + │    │Analytics    │
        │automation   │    │pipeline     │    │Reporting    │
        │Ghost-busting│    │Stall prev.  │    │CRM unify    │
        │Micro-niche  │    │Maturity     │    │API gateway  │
        │Lead scoring │    │CMBS monitor │    │Data store   │
        └─────────────┘    └─────────────┘    └─────────────┘
```

---

## RIOS — Module Breakdown

### 1. Signal Intelligence Layer

**Purpose:** Capture intent signals before competitors do.

#### Residential Signals

| Source | Signal | Frequency | API / Method |
|--------|--------|-----------|--------------|
| Realtor.com | New listing, price drop, saved properties | Daily | Web scrape (Apify/Bright Data) |
| Zillow | New listing, price reduction, views | Daily | Web scrape |
| Courthouse filings | Pre-foreclosure, auction notices | Daily | County court APIs |
| USDA eligibility | Rural property eligible for USDA loans | On-demand | USDA API |
| LinkedIn | Job title change → likely refinancing | Weekly | PhantomBuster |
| Forbearance data | Borrower exit signals | Weekly | Lender data feeds |

#### Commercial Signals

| Source | Signal | Frequency | API / Method |
|--------|--------|-----------|--------------|
| CMBS Special Servicers | Loan transferred to special servicing | Weekly | Web scrape (5+ servicers) |
| MSCI / Trepp | Maturity wall alerts, watch list loans | Weekly | Data feed (Phase 2) |
| CREDCO | New deal listings, preferred equity | Weekly | API access |
| CRE fintech portals | New multifamily / office / industrial listings | Daily | Web scrape |
| Broker network | Deal introductions, warm referrals | Real-time | LinkedIn + email |
| Company filings | Sponsor acquisition / portfolio sale | Weekly | SEC EDGAR |

### 2. Enrichment Layer

**Purpose:** Transform raw signals into actionable contact + deal data.

| Data Type | Residential | Commercial |
|-----------|-------------|------------|
| Contact | Phone, email, LinkedIn, role | Contact, title, firm, lender relationships |
| Company | Brokerage, volume, CRM usage | Firm size, lender panel, deal capacity |
| Intent | Pre-approval page visited, rate calc used | Deal memo sent, UW conditions, stage |
| Rate sensitivity | Current lender, rate lock status | Existing loan terms, maturity date |
| Urgency | Closing date, listing saved | Rate lock expiry, UW deadline |

**Tools:** EnrichLayer, Apollo, Bright Data (web enrichment)

### 3. Scoring Engine

#### Residential — Lead Scoring Model

| Signal | Weight | Data Source |
|--------|--------|-------------|
| Listing saved (realtor/Zillow) | 15 | Web scrape |
| Pre-approval checklist visited | 20 | Website analytics |
| Rate calculator used | 15 | Website analytics |
| SMS responded | 20 | Klick2Client SMS |
| Competitor quote received | 15 | Follow-up sequence |
| Closing date in CRM | 10 | Broker entry |
| Job title change (LinkedIn) | 5 | PhantomBuster |

**Score thresholds:**
- Hot (8–10): Call within 2 hours — momentum alert
- Warm (5–7): Continue nurture sequence
- Cold (1–4): Long-term automation

#### Commercial — Deal Scoring Model

| Signal | Weight | Data Source |
|--------|--------|-------------|
| Loan in special servicing | 25 | CMBS monitor |
| Maturity window < 12 months | 20 | Maturity wall tracker |
| UW condition overdue | 20 | Deal tracker |
| Rate lock expiring < 10 days | 15 | Deal tracker |
| Referral from lender/partner | 10 | CRM |
| Document checklist > 50% complete | 10 | Deal tracker |

**Score thresholds:**
- Critical (15+): Immediate action — call + email today
- Active (8–14): Track closely — check-in sequence active
- Monitor (1–7): Long-term pipeline

### 4. Automation Engine — Residential

#### Ghost-Busting Sequence (21 days, 8 touchpoints)

| Day | Channel | Message Type |
|-----|---------|-------------|
| 0 | Email | Pre-qualification checklist + calendar link |
| 0 | SMS | "Got your info — what's your timeline?" |
| 1 | Email | "Rates changed — here's what borrowers are locking in" |
| 2 | SMS | "Talking to other lenders? Here's what to compare" |
| 3 | Email | Case study / testimonial from micro-niche |
| 7 | Email | "Did another broker give you a quote?" |
| 10 | SMS | "Just locked a [niche] borrower at [rate] — comparison?" |
| 14 | Email | "Last message — here's how to lock in before [trigger]" |

#### Micro-Niche Personas (5 variants)

| Persona | Outreach Hook | Email Subject Variant |
|---------|---------------|----------------------|
| DSCR Investor | "DSCR without tax returns" | "Bank statement loans for investors" |
| Physician Loans | "No PMI at 95% LTV" | "Physician loans: income verified differently" |
| Bank Statement | "12 months vs. 2 years of returns" | "1099 borrowers — bank statement loans" |
| First-Time Buyer | "$10K down payment assistance" | "First-time buyer checklist — free" |
| Non-QM | "Don't fit the box?" | "Non-QM for complex income situations" |

### 5. Automation Engine — Commercial

#### Deal Check-In Sequences

**Application Stage:**
- Day 0: Doc checklist email
- Day 3: SMS follow-up
- Day 7: Outstanding docs reminder
- Day 14: "Where are you on the rent roll?"

**Underwriting Stage:**
- Day 0: UW conditions intro email
- Day 7: Borrower check-in SMS
- Day 14: Lender status update
- Day 21: Appraisal status check
- Day 30: Full UW status summary

**Commitment / Rate Lock:**
- Day -10: Rate lock expiry alert (email + SMS)
- Day -5: Extension check-in
- Day -1: Final call to action

#### Maturity Outreach Sequence (12-month window)

| Day | Channel | Message |
|-----|---------|---------|
| 0 | Email | "Your loan may be approaching maturity — here's what to know" |
| 7 | Email | "Refinancing options for [property type] — [city]" |
| 14 | SMS | "Thinking about your maturity window? Happy to chat." |
| 21 | Email | Case study: "How [similar property] refinanced before maturity" |
| 30 | Call | Broker call — calendar link in email |

#### CMBS Special Servicer Alert Sequence

| Day | Channel | Message |
|-----|---------|---------|
| 0 | Email | "New CMBS opportunity — [property address], [loan amount]" |
| 0 | SMS | "CMBS alert: [loan amount] transfer — [servicer]. Outreach now?" |
| 3 | Email | "Why this CMBS loan is worth calling today" |
| 7 | SMS | "Still thinking about the [city] CMBS opportunity?" |

### 6. Pipeline Management

#### Residential — Loan Stage Pipeline

```
Lead → Pre-qualified → Application → Processing → UW → CTC → Funded
```

Each stage:
- Automated checklist (docs required)
- Stage-triggered sequence (email/SMS)
- Stage gate (cannot advance without data)

#### Commercial — Deal Stage Pipeline

```
Pitch → Proposal → Application → Underwriting → Commitment → Closing → Post-Close
```

Each stage:
- Stage-specific document checklist
- UW conditions tracker
- Deadline alerts
- Lender + borrower contact tracking

---

## Tech Stack Map

```
SIGNAL LAYER
├── Apify (web scraping — realtor, Zillow, CMBS servicers)
├── Bright Data (web data — residential listings, commercial portals)
├── PhantomBuster (LinkedIn — job changes, network signals)
└── Courthouse APIs (foreclosure filings)

ENRICHMENT LAYER
├── EnrichLayer (phone, email, B2B data — residential)
├── Apollo (contact + company data — commercial)
├── Clearbit (company enrichment)
└── LinkedIn Sales Navigator (commercial contact intel)

SCORING ENGINE
├── Klick2Client OS (custom scoring model — residential)
├── Klick2Client OS (deal scoring — commercial)
├── Google Sheets (manual score overrides)
└── Notion (deal pipeline view — commercial)

AUTOMATION ENGINE
├── Klick2Client OS (orchestration — Claude Code + AgentSource)
├── n8n (fallback workflow automation)
├── Instantly (email deliverability + warmup)
├── Twilio / Klick2Client SMS (SMS sequences)
└── PhantomBuster (LinkedIn outreach + voicemail drops)

OUTBOUND CHANNELS
├── Instantly (email — residential + commercial)
├── Twilio (SMS — residential + commercial)
├── PhantomBuster (LinkedIn InMail + connection requests)
├── Direct mail (maturity wall — commercial)
└── Voicemail drops (PhantomBuster — commercial)

DATA STORAGE
├── Google Sheets (lead pipeline — residential)
├── Notion (deal tracker — commercial)
├── Airtable (micro-niche + sequence library)
└── Hermes memory (agent state, scoring model)

ANALYTICS
├── Google Analytics (website intent signals)
├── Instantly (email engagement analytics)
├── Notion (deal close rate, stall rate)
└── Custom dashboard (lead score → loan close correlation)

AGENTS (Claude Code + AgentSource)
├── Signal Agent (scraping, monitoring, alert triggers)
├── Enrichment Agent (data enrichment, dedup, score update)
├── Sequence Agent (email/SMS triggering, A/B variant selection)
├── Scoring Agent (daily score recalculation, hot lead alerts)
├── Pipeline Agent (stage advancement, checklist tracking)
└── Reporting Agent (weekly pipeline digest, ROI metrics)
```

---

## Build Phases

### Phase 1: MVP (Weeks 1–4)
**Goal:** Get residential broker pipeline live with 2 alpha clients

- [ ] Signal agent: Realtor/Zillow scrape + daily enrichment → Google Sheets
- [ ] Enrichment agent: Phone/email/LinkedIn via EnrichLayer → CRM entry
- [ ] Ghost-busting sequence: 8-touch, email + SMS, 21 days via Instantly
- [ ] Lead scoring: 20-signal model, daily recalculation, hot lead SMS alert
- [ ] Alpha test: 2 residential brokers, 30-day conversion measurement
- [ ] Iterate: Adjust scoring weights based on real conversion data

### Phase 2: Residential Launch (Weeks 5–8)
**Goal:** Full residential broker OS with 5 paying clients

- [ ] Micro-niche positioning engine: 5 personas, auto-personalize copy
- [ ] Pipeline dashboard: Real-time lead score, stage, next action
- [ ] LinkedIn outreach sequence: Connection requests + InMail for broker prospecting
- [ ] Ad creative: LinkedIn + Facebook lead gen ads
- [ ] Outreach campaign: 20 residential brokers, discovery calls
- [ ] Pricing: $497–$1,997/mo tiered model
- [ ] Onboarding flow: Micro-niche selection → CRM configure → 30-day launch

### Phase 3: Commercial Intelligence (Weeks 9–14)
**Goal:** Commercial mortgage OS MVP

- [ ] CMBS special servicer monitor: 5 servicers, weekly scrape
- [ ] Deal tracker: Notion-based, Pitch → Closing stages
- [ ] Maturity wall tracker: Agency + CMBS loans, 12–18 month window
- [ ] Stall prevention engine: UW condition deadlines, rate lock alerts
- [ ] Commercial outreach sequences: Deal check-ins, maturity outreach, CMBS alerts
- [ ] Alpha test: 2 commercial brokers, 90-day stall prevention measurement
- [ ] Iterate: Adjust sequence timing based on deal cycle data

### Phase 4: Commercial Launch (Weeks 15–20)
**Goal:** Full commercial mortgage OS with 3 paying clients

- [ ] Deal scoring model: 6-signal commercial scoring engine
- [ ] Lender relationship tracker: Panel management, contact log
- [ ] CMBS opportunity alert: Same-day outreach sequence
- [ ] Multi-broker team view: Enterprise dashboard
- [ ] LinkedIn broker outreach: Targeting commercial LO / VP CRE
- [ ] Pricing: $997–$3,997/mo tiered model
- [ ] Onboarding flow: 45-day deal pipeline launch

### Phase 5: RIOS Platform (Weeks 21–26)
**Goal:** Unified platform, both verticals, API-ready

- [ ] Unified data layer: Single customer/contact view across residential + commercial
- [ ] Cross-sell engine: Residential broker → commercial opportunities
- [ ] Analytics dashboard: Conversion rates, stall rates, ROI by tier
- [ ] White-label: Brokerage portal for firm-wide deployment
- [ ] API: Third-party integrations (LMS, LOS, accounting)
- [ ] Pricing optimization: Segment by volume, tier by deal count

---

## Alpha Client Targets

### Residential (Phase 1–2)
- [ ] Broker A: DSCR investor niche, $10M/yr volume, using Excel + Lime Light
- [ ] Broker B: First-time buyer focus, $8M/yr volume, Zillow Premier Agent

### Commercial (Phase 3–4)
- [ ] Commercial Broker A: Multifamily focus, $30M/yr volume, using spreadsheet
- [ ] Commercial Broker B: Mixed asset class, $20M/yr volume, tracking in Outlook

---

## Dependencies & Vendors

| Vendor | Purpose | Cost | Priority |
|--------|---------|------|----------|
| Claude Code (AgentSource) | Orchestration engine | TBD | Critical |
| Apify | Web scraping | ~$50/mo | Critical |
| Bright Data | Web data | ~$100/mo | High |
| Instantly | Email deliverability | ~$59/mo | Critical |
| EnrichLayer | B2B data enrichment | ~$50/mo | Critical |
| Apollo | Commercial contact data | ~$49/mo | High |
| PhantomBuster | LinkedIn + social scraping | ~$56/mo | High |
| Notion | Commercial deal tracker | ~$8/user/mo | High |
| Google Sheets | Residential pipeline | Free | Critical |
| Twilio | SMS sequences | ~$0.01/text | Medium |

---

## Success Metrics

### Residential
| Metric | Baseline | Target (90 days) |
|--------|----------|------------------|
| Lead conversion rate | 3–5% | 12–18% |
| Ghosting rate | 70%+ | <20% |
| Touchpoints per lead | 1–2 | 8–12 |
| Time to pre-qual | 3–5 days | 24 hours |
| Broker NPS | — | 40+ |

### Commercial
| Metric | Baseline | Target (90 days) |
|--------|----------|------------------|
| Deal stall rate | 15–20% | 3–5% |
| Maturity window capture | 0–10% | 30–50% |
| CMBS opportunity response | Weeks | Same day |
| Pipeline visibility | Spreadsheet | Real-time dashboard |
| Broker NPS | — | 40+ |

---

## Next Steps

- [ ] Dennis approves RIOS architecture
- [ ] Prioritize Phase 1 tasks for immediate build
- [ ] Identify 2 residential alpha brokers
- [ ] Confirm Claude Code + AgentSource pricing / licensing
- [ ] Begin Phase 1 signal agent build

---

**Contact:** Dennis / KlickSmartAI