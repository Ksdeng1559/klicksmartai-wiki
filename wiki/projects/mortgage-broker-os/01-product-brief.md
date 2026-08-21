# Klick2Client OS — Mortgage Broker Vertical

## Product Brief v1.0

**Date:** May 29, 2026
**Owner:** Dennis / KlickSmartAI
**Status:** Proposal — Not yet approved

---

## Problem Statement

Residential mortgage brokers are losing on price, not winning on value.

5 distinct failure points:
1. **Aggregator leads** — sold to 5+ brokers simultaneously, brokers race to the bottom on price
2. **No differentiation** — same email templates, same pitch, same outcome
3. **Ghosting** — borrowers apply to 5 brokers, pick the fastest responder
4. **Manual follow-up** — can't scale, most brokers have no sequence at all
5. **Wrong tool** — generic CRMs don't map to the loan pipeline (Lead → Pre-qual → Application → UW → CTC → Funded)

**Result:** Brokers pay $500–$1,500/month for leads, convert at 3–5%, and leave 95% of pipeline value on the table.

---

## Solution: Mortgage OS

Klick2Client OS, deployed for the mortgage vertical as a turnkey automation system.

Not a CRM. Not a lead gen service. A **lead-to-funded pipeline automation system** that:
1. Captures intent signals before competitors do
2. Auto-differentiates broker outreach by micro-niche
3. Runs ghost-busting follow-up sequences across email + SMS
4. Scores and triages leads so brokers focus on hot prospects
5. Manages the loan stage pipeline end-to-end

---

## Product Architecture

```
[Signal Capture]          → [Enrichment]           → [Scoring]
├── Realtor/Zillow           ├── Phone + Email          ├── Intent score
├── Courthouse filings        ├── Rate sensitivity       ├── Pipeline stage
├── USDA eligibility         ├── Competitor data        ├── Urgency signals
└── Forbearance data         └── Loan type fit
        │                          │                        │
        └──────────────────────────┴────────────────────────┘
                                    ▼
                        [Klick2Client OS Core]
                        ├── Multi-niche positioning
                        ├── Ghost-busting sequences
                        ├── Lead scoring dashboard
                        └── Loan stage pipeline
                                    │
                        [Outbound Channels]
                        ├── Email (Instantly)
                        ├── SMS (Klick2Client SMS)
                        └── Voicemail drops (PhantomBuster)
```

---

## Feature Breakdown

### 1. Signal Capture Layer

**What it does:** Pulls intent signals from public data sources 2–4 weeks before competitors see the lead.

| Source | Signal | Trigger |
|--------|--------|---------|
| Realtor.com / Zillow | New listing saved, price drop | New listing in broker's county |
| Courthouse filings | Pre-foreclosure, auction notice | Address in target ZIP |
| USDA loan eligibility | Rural property eligible | Address lookup API |
| LinkedIn | Job change → likely refinancing | Title/company change |

**Automation:** Daily scrape → enrichment → CRM entry with intent score, same-day.

### 2. Micro-Niche Positioning Engine

**What it does:** On broker onboarding, they pick a micro-niche persona. All outreach language auto-personalizes.

| Micro-Niche | Persona | Outreach Hook |
|-------------|---------|---------------|
| DSCR Loans | Real estate investors | "DSCR without tax returns — 12-mo bank statements" |
| Physician Loans | Doctors with high income, thin file | "No PMI at 95% LTV for physicians" |
| Bank Statement Loans | Self-employed, 1099 income | "Bank statement loans for 1099 borrowers" |
| First-Time Buyers | FHA + down payment assistance | "First-time buyer? Here's $10K in assistance you qualify for" |
| Non-QM | Credit-challenged, complex income | "Don't fit the box? Neither do our products" |

**Automation:** Broker picks niche → CRM auto-tags → all email/SMS subject lines and body copy regenerate per niche persona.

### 3. Ghost-Busting Sequence Engine

**What it does:** Runs the full follow-up sequence automatically — email + SMS, 21-day cycle, 8 touchpoints.

| Day | Channel | Message Type |
|-----|---------|-------------|
| Day 0 | Email | Pre-qualification checklist + calendar link |
| Day 0 | SMS | "Got your info — what timeline are you targeting?" |
| Day 1 | Email | "Rates changed — here's what [niche] borrowers are locking in" |
| Day 2 | SMS | "Talking to other lenders? Here's why brokers like [name] win" |
| Day 3 | Email | Case study / testimonial from [niche] borrower |
| Day 7 | Email | Competitor rate capture: "Did another broker give you a quote?" |
| Day 10 | SMS | "Just locked a [niche] borrower at [rate] — want a comparison?" |
| Day 14 | Email | "Last message — here's how to lock in before [macro trigger]" |

**Automation:** Stage-triggered sequences — no manual touch until borrower responds.

### 4. Lead Scoring Dashboard

**What it does:** Recalculates intent score daily, surfaces hot leads first.

| Score Range | Broker Action | Automation |
|-------------|--------------|------------|
| 8–10 (Hot) | Call within 2 hours | "Momentum alert" → broker SMS + dashboard highlight |
| 5–7 (Warm) | Email response, set appointment | Nurture sequence continues |
| 1–4 (Cold) | No manual touch | Long-term nurture, monthly check-in |

**Signals feeding score:** Listing saved, pre-approval page visited, rate calculator used, SMS responded, competitor quote received, closing date in CRM.

**Automation:** Score recalculates nightly → broker sees updated queue each morning.

### 5. Loan Stage Pipeline

**What it does:** Replaces generic CRM with mortgage-specific stage tracking.

```
Lead → Pre-qualified → Application → Processing → UW → CTC → Funded
```

Each stage has:
- **Automated checklist** (documents needed, conditions to clear)
- **Stage-triggered sequence** (notification to borrower, deadline reminders)
- **Stage gate** (cannot advance without required data)

| Stage Transition | Trigger | Automation |
|-----------------|---------|------------|
| Lead → Pre-qualified | Pre-qual form submitted | Confirmation + next steps email |
| Pre-qual → Application | Full application received | Document checklist email |
| Application → Processing | Docs submitted to LOS | "We're on it" borrower update |
| Processing → UW | File complete | Underwriter intro email |
| UW → CTC | Conditions cleared | "Clear to close" celebration email |
| CTC → Funded | Closing confirmed | Review request + referral ask |

**Automation:** Borrower advances stages by clicking email/SMS links — no manual CRM entry, no broker chasing docs.

---

## Go-to-Market

### Target Customer Profile

**Primary:** Independent mortgage broker, 1–5 years in business, doing $5M–$20M/year volume
- Paying $500–$1,500/month for lead gen (realtor.com leads, Zillow, aggregator)
- Converting 3–5% of leads, leaving 95% on the table
- Has tried a CRM and abandoned it — "doesn't map to how loans work"

**Secondary:** Broker teams / LOAs with 2–5 loan officers sharing a pipeline

### Pricing Model

| Tier | Price | Includes |
|------|-------|---------|
| Starter | $497/mo | Signal capture + enrichment + ghost-busting sequences |
| Pro | $997/mo | Starter + lead scoring dashboard + micro-niche positioning |
| Elite | $1,997/mo | Pro + loan stage pipeline + dedicated onboarding |

**Pricing logic:** Broker currently paying $500–$1,500/month for leads with no follow-up. We're selling the system that makes those leads actually convert — 3–5% → 12–18%.

### Acquisition

1. **LinkedIn outreach** — target LO originators with "mortgage broker" in title, 1,000+ connections
2. **Facebook Groups** — r/mortgageprofessionals, Mortgage Nerds, Loan Officer Lounge
3. **Webinar funnel** — "How to double your lead conversion without more leads" → application
4. **Partner channel** — partner with wholesale lenders (Angel Oak, Carrington) to white-label to their brokers

---

## Metrics / Success KPIs

| Metric | Baseline | Target |
|--------|----------|--------|
| Lead conversion rate | 3–5% | 12–18% |
| Follow-up touchpoints per lead | 1–2 | 8–12 |
| Ghosting rate | 70%+ | <20% |
| Time to pre-qual | 3–5 days | 24 hours |
| Loan stage visibility | None | Real-time |

---

## Dependencies

- **Instantly** — email deliverability + warmup
- **PhantomBuster** — LinkedIn/voicemail automation (if prospecting)
- **EnrichLayer / Apollo** — phone/email enrichment
- **Klick2Client OS** — core orchestration layer (Claude Code + AgentSource)
- **Custom LOS integration** — Calyx, Mortech (optional, Phase 2)

---

## Next Steps

- [ ] Dennis approves scope
- [ ] Build onboarding flow (broker picks niche → CRM configures itself)
- [ ] Build ghost-busting sequence templates (7 templates × 5 niches = 35 variants)
- [ ] Build lead scoring model (20 weighted signals)
- [ ] Alpha client: find 2 mortgage brokers to test on
- [ ] Iterate based on feedback

---

**Contact:** Dennis / KlickSmartAI