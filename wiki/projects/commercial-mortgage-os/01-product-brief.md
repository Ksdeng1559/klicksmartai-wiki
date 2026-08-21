# Klick2Client OS — Commercial Mortgage Broker Vertical

## Product Brief v1.0

**Date:** May 29, 2026
**Owner:** Dennis / KlickSmartAI
**Status:** Proposal — Not yet approved

---

## Problem Statement

Commercial mortgage brokers are managing $1M–$50M+ deals across 60–180 day cycles with nothing better than spreadsheets, Outlook, and LinkedIn.

5 distinct failure points:
1. **Deal sourcing is reactive** — brokers wait for deals to come in or chase introductions, instead of systematically building a deal flow pipeline
2. **Deal tracking is fragmented** — loans live in email threads, sticky notes, and disconnected spreadsheets — stage status disappears between calls
3. **Active deal follow-up lapses** — complex deals (multi-property, preferred equity, construction) stall because no automated pipeline check-ins exist
4. **Maturity wall blind spots** — $5M–$20M loan maturities are tracked manually, if at all; brokers lose refinancing windows and borrower relationships
5. **CMBS / special servicing intelligence is inaccessible** — deals in special servicing are high-opportunity but require monitoring multiple servicers with no unified feed

**Result:** Brokers leave $100K–$500K+ in annual origination fees on the table because their pipeline system doesn't match the complexity of their deals.

---

## Solution: Commercial Mortgage OS

Klick2Client OS, deployed for the commercial mortgage vertical as a deal-to-close automation system.

Not a CRM. Not a deal board. A **commercial mortgage pipeline intelligence system** that:
1. Sources deals systematically (special servicing, maturity wall, broker network signals)
2. Tracks every deal from pitch → commitment → closing → post-closing monitoring
3. Runs check-in sequences on active deals so nothing stalls
4. Surfaces maturity and refinancing windows before competitors do
5. Monitors CMBS / special servicing pools for distressed opportunities

---

## Why This Vertical Is Higher-Value

| | Residential Broker | Commercial Broker |
|---|---|---|
| Avg loan size | $300K–$800K | $1M–$50M |
| Origination fee | 0.5–1.0% = $3K–$8K | 0.5–1.5% = $50K–$750K |
| Pipeline volume | 50–200 leads/mo | 5–30 active deals/yr |
| Follow-up problem | Volume: 100s of leads | Complexity: deals stall at UW |
| System need | Lead-to-funded automation | Deal tracking + intelligence |

**The commercial follow-up problem is not about volume — it's about deal complexity and timing.**

A stalled deal in commercial is worth $50K–$500K in lost fees. The system needs to prevent that stall, not just increase touchpoints.

---

## Product Architecture

```
[Deal Intelligence Sources]  →  [Pipeline Management]  →  [Outreach Engine]
├── CMBS Special Servicer lists   ├── Deal tracker          ├── Check-in sequences
├── Maturity wall alerts         ├── Stage gates           ├── Refinancing outreach
├── Broker network signals       ├── Document checklist     ├── Maturity alerts
├── Preferred equity deals       ├── UW condition tracking  └── CMBS opportunity alerts
└── Distressed / REO feeds       └── Post-close monitoring
         │                              │                        │
         └──────────────────────────────┴────────────────────────┘
                                         ▼
                            [Klick2Client OS Core]
                            ├── Deal scoring
                            ├── Broker + borrower tracking
                            ├── Automated check-ins
                            └── Maturity pipeline dashboard
                                         │
                             [Outbound Channels]
                             ├── Email (Instantly)
                             ├── LinkedIn (PhantomBuster)
                             └── SMS (Klick2Client SMS)
```

---

## Feature Breakdown

### 1. Deal Intelligence Layer

**What it does:** Pulls deal flow signals from sources residential CRMs can't touch.

| Source | Signal | Trigger |
|--------|--------|---------|
| CREDCO / CBRE Capital Markets | New listing, preferred equity opportunity | Deal posted in target market |
| Special Servicer websites | CMBS loans transferred to special servicing | Servicer update in target geography |
| MSCI / Trepp | Maturity wall alerts, watch list loans | Loan maturity < 12 months |
| Commercial real estate portals | New multi-family / office / industrial listing | Price > $2M, target asset class |
| Broker network intel | Deal introduction from industry network | Direct referral or warm intro |
| LinkedIn / company filings | Sponsor acquisition / portfolio sale | Company transaction signal |

**Automation:** Weekly scan → enrichment → deal entry with source attribution + urgency score.

### 2. Deal Pipeline Tracker

**What it does:** Replaces the spreadsheet / sticky note deal management system.

```
Pitch → Proposal → Application → Underwriting → Commitment → Closing → Post-Close
```

| Stage | What it tracks | Automation trigger |
|-------|---------------|-------------------|
| Pitch | Deal memo, preliminary terms, borrower brief | — |
| Proposal | Quote sent, terms outlined, exclusivity discussion | 48hr follow-up if no response |
| Application | Full package submitted, document checklist | Missing docs → borrower + guarantor alert |
| Underwriting | UW conditions, appraisal, environmental | Condition cleared → lender update |
| Commitment | Term sheet issued, legal review | Sign-off → next steps email |
| Closing | Title, insurance, entity docs | Docs due → checklist reminder |
| Post-Close | Post-closing conditions, reporting schedule | Reporting due → reminder alert |

**Key differentiator:** Commercial deals have **stage-specific document checklists** (appraisal, environmental, rent roll, operating statements, entity docs) — this system tracks them per deal.

### 3. Deal Stalling Prevention Engine

**What it does:** Prevents the $50K–$500K loss that happens when a deal stalls in underwriting.

| Risk point | Signal | Automation |
|-----------|--------|------------|
| Docs missing at application | Checklist item not received | Borrower + guarantor SMS + email |
| UW condition overdue | Condition not cleared by date | Lender alert + borrower escalation |
| Appraisal delayed | Appraisal ordered > 30 days | Broker notification |
| Legal review stalled | LOI signed > 21 days without PSA | Internal alert |
| Rate lock expiring | Lock expires < 10 days | Borrower + broker SMS |
| Commitment not closing | Commitment > 45 days, no close date | Board review + escalation |

**Automation:** Stage gates → checklist items → automated reminders with escalation if overdue.

### 4. Maturity Wall Intelligence

**What it does:** Tracks the commercial loan maturity pipeline so brokers can proactively call borrowers before competitors do.

**Scope:** All commercial loans in broker's target market / geography (not just their own deals — their borrowers' existing loans elsewhere).

| Loan type | Opportunity | Trigger |
|-----------|-------------|---------|
| Agency (Fannie / Freddie) | Refinance before maturity | 14-month window |
| CMBS | Transfer risk, special servicer opportunity | 12-month window or special servicer flag |
| Life company | Rate reset, relet risk | 18-month window |
| Bridge loan | Exit to permanent or recap | 6-month window |
| Mezz / preferred equity | Exit or restructure | 9-month window |

**Automation:** Monthly scan of MSCI / Trepp / servicing data → maturity alert → broker outreach template pre-loaded.

### 5. CMBS Special Servicer Monitor

**What it does:** Tracks CMBS loans transferred to special servicing — high-opportunity deals where borrowers need new capital.

| Servicer | URL / Source | Frequency |
|---------|-------------|-----------|
| Oak Street / Rialto (BRSP) | servicemap.oakstreetfunding.com | Weekly |
| CWCapital | cwbserve.com | Weekly |
| RCap / LNR | lnrpartners.com | Weekly |
| Seven Hills Group | sevenhillsgroup.com | Weekly |
| Mesa West | mesawestcap.com | Weekly |
| FirstKey | firstkeyhomes.com | Weekly |

**Signal mapping:** When a loan transfers to special servicer → opportunity alert → broker can reach out to borrower with new capital solution → new deal origination.

**Automation:** Weekly scrape → deal entry with property address, loan amount, servicer contact → outreach sequence triggered.

---

## Go-to-Market

### Target Customer Profile

**Primary:** Independent commercial mortgage broker, 3–15 years in business, doing $20M–$100M+ in annual originations
- Has relationships with 3–5 lenders (agency, CMBS, life company, bridge)
- Managing 5–20 active deals at any time
- Using spreadsheets + Outlook to track deals
- Losing 1–2 deals per quarter to stalling / lost track

**Secondary:** Commercial real estate finance team at a bank or credit union (portfolio monitoring + outreach automation)

### Pricing Model

| Tier | Price | Best For |
|------|-------|---------|
| **Pipeline** | $997/mo | Deal tracking + check-in sequences |
| **Intelligence** | $1,997/mo | Pipeline + maturity wall + CMBS monitoring |
| **Enterprise** | $3,997/mo | Intelligence + multi-broker team + lender portal |

**Setup fee:** $2,497–$7,497 (based on complexity + integrations)

**Pricing logic:** Commercial broker earns 50–150 bps on $5M–$20M deals. One deal stalled in UW = $25K–$300K in lost fees. One maturity window captured = $25K–$300K in new origination. System pays for itself on 1–2 deals/year.

### Acquisition Channels

1. **Mortgage bankers conferences** — MBA Annual, CMBEX, MSFA (in-person pipeline)
2. **LinkedIn outreach** — target "Senior Loan Officer" / "Vice President — Commercial Real Estate" at mid-size independent firms
3. **Partner channel** — white-label to commercial real estate brokerages (Cresa, JLL, CBRE origination desks)
4. **Direct mail** — targeted to maturity wall targets (mailers + calls on loans maturing in 12 months)
5. **Podcast sponsorships** — Commercial Real Estate Finance podcast, GlobeSt.

---

## Dependencies

- **Instantly** — email deliverability + warmup (commercial email requires high reputation)
- **PhantomBuster** — LinkedIn outreach for broker network + borrower relationship maintenance
- **Trepp / MSCI** — maturity wall data (Phase 2 integration)
- **CREDCO** — commercial deal listings
- **Klick2Client OS** — core orchestration (Claude Code + AgentSource)

---

## Metrics / Success KPIs

| Metric | Baseline | Target |
|--------|----------|--------|
| Deals stalled in UW | 1–2/quarter | <0.5/quarter |
| Maturity window capture rate | 0–10% | 30–50% |
| Deal-to-close cycle | 90–180 days | 60–120 days (with fewer stalls) |
| Active deal visibility | Spreadsheet / email | Real-time pipeline dashboard |
| CMBS opportunity response time | Weeks | Same day |

---

## Next Steps

- [ ] Dennis approves commercial scope
- [ ] Validate with 2 commercial brokers (alpha test)
- [ ] Build CMBS special servicer monitor (5 servicers, weekly scrape)
- [ ] Build maturity wall tracking model (agency + CMBS + life company)
- [ ] Build deal check-in sequence templates (7 stage-specific variants)
- [ ] Build referral network tracking (broker + borrower relationship map)

---

**Contact:** Dennis / KlickSmartAI