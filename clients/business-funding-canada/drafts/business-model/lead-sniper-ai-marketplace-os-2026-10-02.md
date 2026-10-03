---
type: BusinessModel
title: "LeadSniperAI Marketplace OS — Business Model Brief"
status: verified-from-notion
generated: 2026-10-02
verified: 2026-10-02
source:
  notion_url: https://app.notion.com/p/LeadSniperAI-Marketplace-OS-3a09e94cf0a481a79a53e07966c1ac20
  notion_uuid: 3a09e94c-f0a4-81a7-9a53-e07966c1ac20
  blocks_count: 2023
  char_count: 159307
  fetched_via: NOTION_API_KEY + blocks/{uuid}/children (paged)
  sections_extracted:
    - Mission
    - Operating Model
    - Directory + Rank-and-Rent Acquisition Model
    - Core Outcomes
    - Lead Product Definition
    - Lead Tiers
    - Weekly Operating Cadence
    - Enterprise Build-Out (multi-tenant)
    - End-to-End Business Funding Lead Workflow (14 stages)
    - HighLevel AI Studio Architecture
    - GHL Refinement (Speed-to-Lead + Verification)
    - Commercial Inventory Policy (verified-and-interested-hot-prospects-only)
    - Verified Hot Prospect MVP — 60-day Implementation Plan
    - Buyer Discovery Funnel (comparison-site strategy)
    - LeadSniper Reverse Buyer Funnel
    - Buyer Acquisition Engine
    - Sept 13, 2026 Architecture Update (Tariff Vertical)
    - GoHighLevel Marketing Automation + Kanban MVP
    - Operator Study (Alex Fuller / Loan Launchpad)
    - Second-Use Lead Lifecycle and Resale Protocol
    - ChatGPT Cross-Platform AI Advertising Command Center
    - Zeely Creative Production Layer
---

# LeadSniperAI Marketplace OS — Business Model Brief

> **Canonical reference** synthesized from the LeadSniperAI Marketplace OS Notion command center. This is the source of truth for the Business Funding Canada workspace. Every workspace artifact (lead form, landing page, content article, email, lead-buyer contract) must align with the operating model described here.

> **TL;DR:** LeadSniperAI is a **multi-tenant pay-per-lead marketplace** for Canadian business-funding opportunities. It is NOT a lender. The asset (capture of private inquiry → verified hot prospect → advisor-ready opportunity) is sold to **qualified buyer organizations** (brokers, lenders, accountants, lawyers, insurers) who close and fund the deal. Pricing is a **subscription + lead credits** model. The system is **buyer-first**: do not acquire prospects until qualified buyer demand is documented in a versioned Buyer Appetite Matrix.

---

## 1. Mission

> Build LeadSniperAI Marketplace into a Canadian business-funding **lead generation, qualification, verification, scoring, distribution, and monetization operating system.**

**Front-door function:** `/funding-assessment` funnel + compact-keyword pages = entry point for Canadian business-funding inquiries. Where `www.mortgagesbydenniseng.ca` is the front door for mortgage clients into Mortgage CoPilot, the `/funding-assessment` is the entry point for business-funding into LeadSniperAI.

---

## 2. Operating Model — System of Record Map

| Layer | Owns | Authority |
|-------|------|-----------|
| **Notion** | Strategy, vertical packages, playbooks, scorecards, objectives, decisions, cadence, executive reporting | Management layer — no raw PII, no authoritative consent, no payment state |
| **Astro/React** | Public acquisition, discovery interview, buyer marketplace, operator interfaces | Frontend |
| **Supabase** (target project **LeadSniper-3.0** = `yolqrstktoqlszybwymw`) | Tenants, memberships, inventory, reservations, purchases, access grants, audit events | **CANONICAL — source of truth for transactional state** |
| **GoHighLevel (GHL)** | Prospect contacts, attribution, consent flags, SMS/email/conversations, nurture workflows, calendars, tasks, pre-sale Kanban | **System of engagement** for intake-to-Marketplace-Ready path |
| **Clerk** | Application identity, tenant membership | Identity & tenancy |
| **Stripe** | Payment execution, refunds, disputes | **Authoritative for payment state** but NOT for marketplace lead credits |
| **Atomic CRM / Supabase** | Internal analytics, relationship intelligence, outcome reporting | Optional; not the live marketing-automation authority |
| **Claude / ChatGPT agents** | Planning, intelligence, classification, implementation support | Bounded authority |
| **Private data services** | Encrypted subject & business identifiers, secure documents | Storage of sensitive records |

**Architectural decision (2026-09-13, LOCKED):** **Supabase is the authoritative Paper Lead backend.** Earlier Convex references superseded. WordPress/Divi properties used for public acquisition and SEO. Stripe Connect deferred until external suppliers must be onboarded.

**Hard rule:** Notion must NOT store raw applicant PII, authoritative consent evidence, payment state, or protected purchased-lead data.

---

## 3. The Three Entity Classes — must remain separate in Supabase + all marketplace logic

1. **Information Sources** — lender websites, government programs, underwriting guides, public databases, industry reports. Research inputs only. Never receive public placement.

2. **Public Advertisers / Directory Tenants** — businesses that pay for visible directory space, featured placement, category sponsorship, or territory occupancy. Display only when they **explicitly purchase directory occupancy or sponsorship and supply approved business name, contact details, listing info.**

3. **Lead Buyers** — approved organizations that purchase or receive qualified opportunities per buyer criteria (geography, consent, capacity, pricing, vertical rules). **A buyer does not need to be a public advertiser.**

**Public-Facing Provider Rule (2026-09-17, LOCKED):** `MortgagesByDennisEng.ca` is the **default public-facing financing provider** on financing-related directory pages. A lender/broker/source does NOT receive public placement merely because its information was used in research.

---

## 4. Operating Principle

> **Rank → Capture → Qualify → Match → Monetize → Recycle.**

Six-stage commercial loop. Stage 6 (Recycle) is **permissioned only** — see §17.

---

## 5. Three Demand-to-Revenue Pathways

The ranked directory asset may support multiple revenue streams:

### 5.1 Lead sales
- Pay-per-lead sales (exclusive or shared with disclosed seat caps)
- Territory-based lead agreements
- Subscription / quota-based lead allocations

### 5.2 Directory occupancy
- **Directory Listing** — approved name, phone, website, category visibility
- **Featured Listing** — enhanced placement within page/category
- **Category or Territory Partner** — preferred occupancy for product × geography or event × geography
- **Lead Partner** — eligibility to purchase qualified opportunities PLUS public placement
- **Exclusive Buyer / Territory Buyer** — premium routing rights subject to commercial, compliance, capacity, quality rules

### 5.3 Adjacent professional marketplace
Directory inventory extends beyond lenders:
- Commercial realtors
- Accountants / CPAs
- Commercial lawyers
- Insurance brokers
- Business brokers / M&A advisors
- Equipment vendors / lessors
- Property managers
- Developers / construction professionals
- Other approved business-service providers aligned with visitor's transaction

**Preferred design:** **transaction-led**, not merely profession-led. A page like *"Buying a Commercial Property in Vancouver"* can capture financing demand + offer sponsored placement to commercial realtor, accountant, lawyer, insurer, etc.

---

## 6. Demand-to-Revenue Flow (canonical diagram)

```
SEO / Paid / Referral Traffic
→ Commercial Information Directory
→ High-Intent Information Page
→ Qualification / Eligibility CTA
→ MortgagesByDennisEng.ca as default financing relationship
→ LeadSniper intake and verification
→ Supabase lead record and consent state
→ Buyer matching / routing
→ Exclusive, shared, specialty, or cross-professional sale
+
Optional paid directory occupancy / sponsorship revenue
```

---

## 7. Core Outcomes (8 outcomes LeadSniper must produce)

1. Generate qualified Canadian business-funding assessment submissions
2. Convert assessments into **voice-verified funding opportunities**
3. Route opportunities as **exclusive, shared, or cross-professional marketplace leads**
4. Build a **compact-keyword content engine** for Canadian business financing
6. Track marketplace revenue, buyer quality, lead quality, funding outcomes
5. Create a repeatable `/goal` and `/loop` operating cadence
6. Identify accessible real-estate equity through optional **Portfolio Real Estate Equity Review** and route to qualified commercial/residential mortgage professionals
7. Build a cross-channel campaign management system that maximizes best-performing campaigns based on business outcomes (NOT surface ad metrics)
8. Apply ChatGPT Ads best practices: conversion measurement, learning periods, optimization toward business outcomes, structured offer/intent feeds

---

## 8. Lead Product Definition — What a Saleable Voice-Verified Funding Opportunity Includes

A lead may be sold when ALL of the following are present:

- [x] Completed one-minute assessment
- [x] Completed AI discovery interview
- [x] **Verified telephone connection** (two-way)
- [x] Confirmed funding amount and purpose
- [x] Business operating history
- [x] Revenue range and financial indicators
- [x] Existing debt profile
- [x] Credit-score range
- [x] Funding timeline
- [x] Available security or owner contribution
- [x] Optional **Portfolio Real Estate Equity Review** (property type, ownership, location, occupancy, estimated value, mortgage balances, charge position, available equity estimate, owner authorization)
- [x] Recommended funding path (unsecured / business-purpose mortgage/refi / secured LOC / bridge / equity take-out / blended capital stack)
- [x] Document-readiness checklist
- [x] Applicant's stated business objective
- [x] AI-generated opportunity summary
- [x] Confidence and completeness scores
- [x] Human quality-control status
- [x] **Timestamped consent to share with approved professionals**

### Inventory exclusions (NEVER sold)

- Raw form submissions.
- Purchased or scraped contact data.
- Public business signals without confirmed funding intent.
- Invalid or unverified contact details.
- Contacts who have not responded.
- Information-only inquiries without active funding requirement.
- Prospects unwilling to speak with a broker or complete an application.
- Duplicate, fraudulent, stale, withdrawn-consent, or out-of-scope records.
- **Nurture prospects until they are reverified and meet the hot-prospect standard.**

> 🔥 **Sales rule (LOCKED):** LeadSniperAI sells **only verified, interested hot prospects**. A raw inquiry, data record, public signal, unresponsive contact, or nurture prospect is **never** offered as paid marketplace inventory.

---

## 9. Lead Tiers (immutable versions)

1. **Assessment Lead** — completed short assessment only.
2. **Voice-Verified Lead** — completed assessment + valid consent + verified contact + discovery interview.
3. **Advisor-Ready Opportunity** — human-approved briefing card + qualification score + buyer fit + next action.
4. **Application-Ready Opportunity** — core documents substantially complete + submission path confirmed.

**Versioning rule:** Every material upgrade creates a **new immutable qualification snapshot**. Previously purchased versions are NOT silently changed.

---

## 10. The 14-Stage End-to-End Workflow (canonical — see Notion §"End-to-End Business Funding Lead Workflow")

```
Interest captured
→ Funding assessment (one-minute)
→ Consent and contact verification
→ Initial qualification
→ AI discovery interview
→ Intelligence and opportunity analysis
→ Human quality review
→ Advisor-ready opportunity
→ Marketplace matching and offer creation
→ Reservation or internal assignment
→ Protected lead delivery
→ Advisor contact and document collection
→ Application submission
→ Approval, decline, or nurture
→ Outcome capture and scoring improvement
```

Each stage has its own entry sources, required fields, consent requirements, system actions, exit criteria, failure routes, and primary owner. See Notion for full stage-by-stage spec.

### Workflow success criteria (thresholds)

- ≥ 80% of completed assessments receive a next-action status automatically.
- ≥ 70% of contactable qualified leads complete discovery.
- Every published opportunity has valid consent and human approval during MVP.
- No protected lead details exposed before authorized access.
- Exclusive opportunities cannot sell more than once.
- Shared opportunities cannot exceed the disclosed seat cap (MVP: **max 2 buyers**).
- Buyers receive purchased opportunities with complete audit evidence.
- Buyer contact time and outcome reporting are measurable.
- Funded, declined, nurture outcomes feed back into scoring + acquisition decisions.

---

## 11. The 60-Day MVP Sprint Plan

| Sprint | Days | Outcome |
|--------|------|---------|
| 1 — Intake & Consent | 90/60 | `/funding-assessment` + progressive save + versioned consent ledger + private inquiry + Assessment Lead snapshot + dedup |
| 2 — Verification & Discovery | 90/60 | SMS/email verification + calendar + reminder workflow + AI discovery interview schema + structured answers + transcript refs + missing-info list |
| 3 — Qualification & Human Review | 90/60 | Initial scoring + Eve intelligence mission planner + PII-free opportunity briefing card + human review queue + immutable qualification snapshots |
| 4 — Marketplace & Commerce | 90/60 | Buyer capability matching + exclusive + 2-seat shared offers + atomic reservations + Stripe test payments + scoped access grants + protected views |
| 5 — Advisor Operations & Outcomes | 90/60 | Atomic CRM sync + contact SLA tracking + document-readiness workflow + application/decision statuses + funded & declined outcomes |
| 6 — Learning Loop | 90/60 | Source/tier/buyer/funding-outcome dashboards + scoring accuracy review + Golden Market Strategy review |

---

## 12. 30-Day Buyer Validation Target (gating before campaign scale)

- [ ] Teardown 10 Canadian comparison or marketplace funnels
- [ ] Identify 100 prospective buyer organizations
- [ ] Prioritize 30 buyers across residential, commercial, private, business-finance
- [ ] Complete 15 buyer interviews
- [ ] Obtain 5 written Buyer Appetite Matrices
- [ ] Activate 3 paid design partners
- [ ] Deliver first 10 verified prospects with full disposition tracking
- [ ] Secure ≥ 1 reorder and document winning buyer profile

**Buyer qualification questions (canonical)** — apply to every prospect:

- Which provinces and borrower types can you serve?
- Business-purpose residential refi, commercial mortgages, or both?
- Property types, occupancies, charge positions, LTV ranges, deal sizes?
- Minimum credit, revenue, time-in-business, documentation rules?
- Bridge, private, conventional, alternative, or blended structures?
- How quickly will you contact an accepted prospect?
- What constitutes a valid rejection or replacement?
- Will you report application, approval, decline, funded amount, reason codes?
- Weekly capacity and acquisition cost supportable?
- Referral, lead-purchase, success-fee arrangements permitted and documented?

**Buyer-fit score (out of 100):** Funding-box fit 40 + Capacity 20 + Speed 15 + Compliance/reputation 15 + Reporting discipline 10. Tier A 75–100, Tier B 60–74, below 60 = prospecting/referral-only. **High score never overrides licensing, consent, geography, or product restrictions.**

---

## 13. Lead Product Definition — Tariff-Impacted Business Funding Opportunity (NEW VERTICAL — Sept 13, 2026)

Every saleable opportunity includes:

- Province, operating location, industry, NAICS code
- Incorporation status, years in business, annual revenue, employee count
- % revenue from U.S. exports (direct or supply-chain)
- Affected products, customers, suppliers, imported production inputs
- Estimated tariff-related cost increase, lost sales, lost contracts, cash-flow shortfall
- Requested amount, purpose of funds, required timeline
- Working capital, payroll, essential operating-cost, equipment, automation, or market-diversification need
- Historically positive cash flow and pre-tariff viability
- Availability of 2 years financial statements, interim statements, projections, payroll, invoices, customs, export-sales
- Existing government assistance / applications
- Verified decision-maker, two-way funding interest, willingness to proceed, consent to disclosure to selected partner category

### Buyer categories (tariff vertical)

- Commercial finance and business-loan brokers
- Equipment finance and leasing providers
- Factoring, receivables, purchase-order finance
- Banks, credit unions, specialized working-capital lenders
- Export finance and trade-resilience advisors
- Qualified grant and government-funding consultants
- Accountants and fractional CFOs capable of preparing resilience plans
- Commercial and residential mortgage professionals for consented property-backed opportunities

### GTM (Locked)

1. **Start:** BC manufacturers and processors, $1M–$25M revenue, ≥ 3 yrs operating, measurable U.S. trade exposure.
2. **Launch BC landing-page variants:** forestry/wood, food processing, advanced manufacturing.
3. **Offer:** "Tariff Impact Funding Assessment" as prospect-facing CTA.
4. **Coverage gate:** ≥ 2 qualified buyers per vertical before scaling paid traffic.
5. **Fallback routing:** non-program candidates → equipment, working capital, factoring, PO finance, conventional commercial, property-backed.
6. **Expand to Ontario** after screening + buyer-outcome loop works; Alberta as focused industrial/agri-food campaign.

---

## 14. Federal Program Track (Tariff Vertical — locked sources)

### Program 1 — BDC Pivot to Grow

- Loan range: **C$250K – C$5M**
- **0% interest for first 12 months** under new liquidity stream
- Interest-only payments up to 36 months; amortization up to 96 months for liquidity financing
- Min annual revenue **C$1M**, generally ≥ 3 years in business
- Historically positive cash flow & pre-tariff viability
- Liquidity fit: ≥ 15% sales exported to U.S. + tariffs ≥ 5% revenue + short-term cash-flow shortfall
- Pivot WC/equipment fit: ≥ 15% U.S. sales OR revenue/costs down/up ≥ 10% due to tariffs
- Resilience/repositioning plan required for pivot & equipment streams
- Program availability through **March 31, 2028** (subject to program conditions)
- Source: https://www.bdc.ca/en/financing/pivot-grow-loan

### Program 2 — Regional Tariff Response Initiative (RTRI)

- Up to **C$2M** non-repayable liquidity assistance
- Up to **C$1M** non-repayable pivot project
- Up to **C$3M** combined non-repayable support
- Larger transformation projects may receive repayable contributions (regional rules govern)
- Activities: automation, digitization, equipment, productivity, supply-chain resilience, domestic sourcing, export development, market diversification
- Direct or indirect tariff exposure + prior viability required
- Source: https://www.canada.ca/en/department-finance/news/2026/08/support-for-canadian-workers-and-businesses-affected-by-us-tariffs.html

### Provincial opportunity map

- **BC (PacifiCan):** forestry transformation, food systems, value-added manufacturing; enhanced RTRI; up to C$2M liquidity + C$1M pivot.
- **Alberta:** hay products, metal recycling, CNC manufacturing, aerospace/defence components, oil/gas flow-control products.
- **Ontario (FedDev):** incorporated, ≥ C$1M annual revenue in 1 of last 2 fiscal years, prior viability, direct/indirect tariff exposure. Scale concentration of automotive, steel, advanced manufacturing → principal expansion market.

---

## 15. Initial Price Tests (Locked)

**Cohort A — Exclusive PPL:** one qualified buyer receives the lead for a fixed credit price.
- Initial fixed: **C$100–C$175** per exclusive verified hot prospect

**Cohort B — Hybrid:** buyer membership + lower per-lead credits + monthly capacity.
- Hybrid: **C$50–C$100** delivery fee + approved success/referral arrangement.

**Cohort C — Capped shared pilot:** ≤ 2 buyers, explicit disclosure + consent required.

**All referral and compensation structures require lender, brokerage, licensing, privacy, and province-specific compliance review before launch.**

Compare buyer first-contact time, contact rate, discovery-booking, application-start, funded rate, dispute/replacement rate, reorder rate, and contribution margin. **Do not optimize for sale price alone.** Prefer the model with the best funded outcomes, buyer retention, and consumer experience.

---

## 16. The Reverse Buyer Funnel (LOCKED governing GTM method)

> 🔁 **Buyer-first rule:** do not scale prospect acquisition until there is **verified buyer coverage** for the niche, province, funding amount, property type, risk band, and weekly volume. Buyers define their funding boxes first; LeadSniper then generates and verifies matching demand.

### Reverse funnel sequence

```
Find organizations already buying financing demand
→ identify the acquisition decision-maker
→ conduct a funding-box interview
→ verify licensing, geography, reputation, capacity, compliance
→ complete a versioned Buyer Appetite Matrix
→ agree on lead definition, price, volume, SLA, replacement policy
→ obtain paid or deposit-backed pilot commitment
→ launch matching acquisition campaigns
→ verify prospect identity, intent, viability, consent in GHL
→ route qualified opportunity through Supabase
→ track contact, application, approval, funding, buyer reorder
```

### Decision-makers to find

- Brokerage owner / principal broker / managing broker / team leader
- Commercial mortgage broker or business-finance specialist
- VP / Head of Partnerships, Business Development, Originations, Sales
- Lender BDM, regional sales manager, chief lending officer, credit leader
- MIC / mortgage-fund principal, originator, portfolio manager
- Fintech partnership manager, channel-sales leader, affiliate manager

### Five-touch buyer outreach cadence

| Day | Touch | Content |
|-----|-------|---------|
| 1 | Relevance | Concise intro referencing buyer's public funding specialty; ask if qualified deal flow is a current priority |
| 3 | Value | One-page Verified Hot Prospect definition + Portfolio Real Estate Equity Review sample (no PII) |
| 5 | Discovery | 15-min funding-box interview (learn appetite, don't sell) |
| 8 | Economics | Capped pilot + lead standard + SLA + replacement policy + expected application economics |
| 10 | Decision | Pilot activated / nurture / closed with reason |

### Buyer discovery opening (use verbatim)

> I operate LeadSniperAI, a Canadian marketplace for verified business-funding opportunities. We confirm the decision-maker, current funding need, preliminary viability, consent, and willingness to proceed with an application. When relevant and authorized, we also complete a preliminary Portfolio Real Estate Equity Review. Do you purchase third-party opportunities, and who manages your referral partnerships or lead-acquisition programs?

---

## 17. Second-Use Lead Lifecycle (permissioned only — LOCKED)

> Paper Lead will adopt **permissioned lead lifecycle monetization**, NOT automatic lead recycling.

### Permitted
- Same-purpose reactivation (consent + purpose remain valid)
- Customer-requested recheck
- Changed-timing requalification (callback date reached, continued interest confirmed)
- Alternative funding path (with fresh consent where purpose/disclosure changes)
- Geographic rematch (within original/fresh disclosure)
- Buyer fallback (first buyer declines / lacks capacity / misses SLA, within disclosed matching process)
- Material market-event reactivation (program change, rate/tariff development — valid consent + accurate source)

### Prohibited (HARD)
- ❌ Automatically selling the same record 3–5 times because it exists
- ❌ Adding undisclosed buyers after original match
- ❌ Buried privacy policy as blanket authorization
- ❌ Reusing for materially different purpose without renewed consent
- ❌ Recontacting suppressed, opted-out, expired-consent records
- ❌ Sending documents / financials / calculator inputs / credit data via SMS or to new buyer without necessity + authorization
- ❌ Misrepresenting market condition / program / eligibility / savings
- ❌ Counting internal transfers as additional sales
- ❌ Hiding prior distribution from buyers where exclusivity matters

### Consent gate (all must pass)
- Identity still current enough
- Original enquiry purpose + date known
- Consent status, channel, notice version, timestamp, source, expiry/review recorded
- Permitted partner category + max distribution recorded
- No global/email/SMS/calling/partner-sharing suppression
- Proposed contact within person's reasonable expectations
- New purpose / third-party disclosure / sensitive-data use → required renewed consent
- First buyer's outcome known or documented exception approved
- Data-retention rules permit continued use

**If uncertain → Consent Review, NOT automated campaign.**

### Lifecycle state model (overlay to Kanban)

- Dormant — timing known
- Reactivation eligible
- Consent review
- Reactivation in progress
- Re-engaged
- Requalified
- Second match authorized
- Second match completed
- No longer interested
- Suppressed / retention-only
- Delete/anonymize when eligible

> A lead must return to **Verified & Interested** before it can become **Marketplace Ready** again. Historical verification does not carry forward automatically.

### Pilot limits (LOCKED)
- Start with records aged **90–180 days** (operating cohorts, NOT universal legal expiry)
- One vertical, one province, ≤ 30 eligible records
- Manual approval before first reactivation send + before every second buyer disclosure
- Cap at lower of customer-authorized limit AND buyer-contract limit
- Shared-lead ceiling remains **2 buyers**
- Stop on unresolved complaint, suppression failure, unauthorized disclosure, misleading message
- Scale only when reactivation contribution is positive + customer/buyer quality indicators within approved limits

---

## 18. Working Assumptions (canonical, until counsel review supersedes)

- **Lead resale policy:** exclusive sells once; shared has small disclosed cap; each buyer org purchases once.
- **Tier upgrades:** create new offer version; prior-buyer access or credits require written commercial policy.
- **Cross-vertical distribution:** every new vertical opportunity requires separate purpose + distribution consent.
- **Buyer licensing:** credentials + permitted geography enforced per vertical before purchase.
- **AI publication:** AI recommends and drafts; **human approves** during MVP.
- **Lead-system product:** recurring service/subscription with quotas + routing rules, NOT bulk access to source records.

---

## 19. Compliance Boundaries (locked)

### Never promise
- Approval
- Grant
- Zero-percent financing
- Particular funding amount

### Always distinguish
- Non-repayable contributions vs loans vs repayable contributions
- "Program administrators and lenders make all eligibility and credit decisions"

### Always verify
- Public claims against current official program page before publishing ads/landing pages

### Always obtain
- Meaningful consent before collecting or sharing business + decision-maker info

### Always follow
- CASL, privacy, licensing, professional-referral, compensation requirements per province + buyer category

### Never use
- Government logos or language implying endorsement

### Never claim
- LeadSniper/Paper Lead is BDC, regional development agency, or Government of Canada representative

---

## 20. The Unit Economics Benchmark (Loan Launchpad case study, self-reported)

| Metric | UK Benchmark | Caveat |
|--------|--------------|--------|
| Cost per lead | £12 | Self-reported ebook |
| Avg sale price | £45 | Self-reported ebook |
| Buyers | 6 | Self-reported |
| Leads/month | 400–500 | Self-reported |
| Gross lead spread | £33/lead | — |
| Implied gross margin | 73.3% | Before labour, software, telephony, refunds, replacements, taxes, compliance |
| Monthly media spend | £4,800–£6,000 | — |
| Monthly revenue | £18,000–£22,500 | — |
| Monthly gross spread | £13,200–£16,500 | — |

> ⚠️ **Treat as benchmark hypothesis, NOT forecast for Paper Lead.** Validate with Paper Lead's own 30-lead pilot. Secondary review describes one lead sold to up to 4 buyers — that is commentary, NOT operating model. **Paper Lead will NOT use unrestricted resale** (cap at 2 buyers per shared lead).

---

## 21. Cross-Platform AI Advertising Command Center

ChatGPT = **Campaign Intelligence OS** across ChatGPT Ads, Meta, Google, YouTube.
- Optimize in priority order: **Funded revenue / contribution margin / ROAS > Cost per funded client > Cost per qualified opportunity > Application + approval rates > Assessment completion + verified-contact > CPL > CTR/CPC/CPM**
- **Champion vs Challenger** model (no campaign wins on lowest CPL alone; produce funded)

**Three coordinated acquisition engines** under one performance layer:
1. **Story Over Score** — complex mortgage situations
2. **Broki Portfolio Review** — property/equity opportunities
3. **LeadSniperAI** — business/commercial financing

### Zeely layer

- **ChatGPT** = campaign strategy, ICP, campaign hypotheses, winner analysis, cross-channel budget logic
- **Zeely** = creative production + front-end testing (static, video, UGC, variants)
- **Distribution platforms** = native to their own delivery (Meta, Google, YouTube, ChatGPT Ads)
- **Conversion engines** = Story Over Score, Broki, LeadSniperAI
- **Attribution** = GHL + Supabase (lead quality + downstream economics)

**Closed-loop advertising system:**

```
ChatGPT Campaign Brain
→ Story Over Score | Broki Portfolio Review | LeadSniperAI
→ Zeely Creative Factory
→ Creative Variants
→ ChatGPT Ads | Meta | Google | YouTube
→ GHL / Supabase
→ Qualified → Application → Funded → Revenue
→ Winner Intelligence
→ New Zeely Challenger Variants
→ Retest and Scale
```

---

## 22. Tool-First Acquisition Requirement (LOCKED)

Every Paper Lead vertical must lead with **at least one genuinely useful comparison, calculator, or eligibility tool** before asking for a sales conversation. Initial result visible without implying approval or requiring unnecessary personal info.

### Recommended business-finance tools (canonical set)

| Tool | Purpose |
|------|---------|
| **Funding-path eligibility checker** | Plausible categories from province, industry, operating history, revenue, purpose, timing, tariff exposure |
| **Repayment scenario calculator** | Payments + total repayment across user-selected amounts, terms, example rates/fees (always labelled estimates) |
| **Working-capital gap calculator** | Cash gap from receivable days, payable days, inventory, monthly operating costs |
| **Commercial property equity calculator** | Gross equity + conservative illustrative borrowing range (subject to valuation, priority, lender policy, underwriting) |
| **Tariff-impact / readiness assessment** | Quantifies reported revenue/cost exposure → routes to relevant advisory or financing pathway |
| **Transparent comparison table** | Compares funding categories by typical use, speed, security, repayment, qualification (NOT fabricated lender quotes) |

**Disclose on every tool result page:** assumptions, data date, limitations, "estimates are not approval or advice", qualified provider determines actual eligibility + terms.

---

## 23. The Refined Five-Step Canadian Assessment (canonical form fields)

1. **Funding request** — amount, use of funds, desired timing
2. **Business profile** — legal name, province, industry, legal structure, decision-maker role
3. **Operating profile** — time in business, annual/monthly revenue band, employee count
4. **Program & collateral signals** — tariff exposure, export activity, property equity / security available, document readiness
5. **Contact & consent** — email, mobile, preferred channel/time, channel-specific marketing consent, explicit consent to share with named or clearly described funding partners

---

## 24. Buyer Discovery — Public Funnels to Teardown (canonical list)

> 🎯 Strategic opportunity: comparison and marketplace sites publicly reveal the categories of organizations that buy financing demand. Their lender directories, comparison tables, advertiser disclosures, partnership pages, referral programs, application paths, and featured providers become a **buyer-discovery map**. The objective is to **identify prospective buyers**, NOT acquire or scrape competitor consumer records.

Canonical teardown targets:

- [Loans Canada](https://loanscanada.ca/) — unified application, provider matching, lender directory, partnerships, affiliate program, provider-funded comparison economics
- [Ratehub business-loan comparison](https://www.ratehub.ca/loans/best-business-loans) — education-first comparison content (rates, amounts, terms, speed, requirements, borrower type)
- [Swoop Funding Canada](https://swoopfunding.com/ca/business-loans/) — short application + matching across banks + funding providers
- [Lending Loop partner program](https://www.lendingloop.ca/) — business-funding platform with explicit partner pathway
- [nesto](https://www.nesto.ca/) — rate discovery, personalization, mortgage fulfilment, public referral-partnership model
- [WOWA](https://wowa.ca/) — lender/broker comparison, calculators, finance education
- [MCAP Commercial Mortgages](https://www.mcap.com/) and [CMLS](https://www.cmls.ca/) — commercial-mortgage product categories, institutional buyer profiles

---

## 25. The 48-Hour Market Validation Protocol (gating before any vertical scale)

For every candidate vertical, create a dated validation entry with:

- Segment hypothesis + owner
- 3–4 competitor records + evidence links
- 10–15 buyer prospects, qualification feedback, committed capacity
- Approved test budget + campaign IDs + landing-page version
- Scorecard + constraints + pass/iterate/reject decision + rationale
- Next experiment, owner, deadline

### Pass criteria (all four must hold)

1. **Communication truth:** truthful offer, valid consent, lawful partner-sharing basis
2. **Competitive evidence:** ≥ 3 credible providers actively serving or acquiring the segment
3. **Distinct angle:** LeadSniper articulates a supportable differentiation
4. **Tool viability:** credible calculator/comparison/checker concept that improves user's decision

### Buyer-side pass criteria

- ≥ 2 active buyers + 1 backup cover test segment
- Accept same qualification definition
- Commit capacity for pilot
- Verbal interest is INSUFFICIENT — pilot agreement, rate card acceptance, onboarding completed, deposit/credit commitment, or written capacity statement required

### Tool-side pass criteria

- Defensible result
- Inputs improve qualification
- ≥ 2 buyers confirm operational utility
- Test users understand "estimate, not approval"

### Tool-side fail

- Disguised form
- Unverifiable savings
- Claims guaranteed eligibility
- Fake comparison
- Collects sensitive data without necessary + disclosed purpose

### Spend gates

- Test budget benchmark from ebook: £200–£350 (record separate Canadian test budget; do NOT silently convert or imply equal economics)
- 30-lead controlled pilot only after all gates pass
- Pause sources / buyers that produce elevated opt-outs, complaints, stale opportunities, poor first-contact

---

## 26. GHL Workflow Package (canonical set LS-WF-00 through LS-WF-09)

| Workflow | Trigger |
|----------|---------|
| **LS-WF-00 Form Submitted** | Funding-assessment form submitted, inbound webhook, qualified chat, inbound call disposition, approved referral |
| **LS-WF-01 Speed to Lead** | Valid new inquiry with necessary communication consent |
| **LS-WF-02 Reply Routing** | Customer Replied on approved channel |
| **LS-WF-03 Discovery Confirmation** | Customer Booked Appointment / Appointment Status New/Confirmed |
| **LS-WF-04 No-Show Recovery** | Discovery appointment status = No-show |
| **LS-WF-05 Discovery Disposition** | Discovery appointment Showed + qualification disposition complete |
| **LS-WF-06 Documents / Verification** | Opportunity enters Documents / Verification |
| **LS-WF-07 Marketplace Publish** | Human QC approval + partner-disclosure consent |
| **LS-WF-08 Supabase Callback** | Authenticated Supabase callback |
| **LS-WF-09 Suppression / Withdrawal** | STOP/UNSUBSCRIBE / DND / consent withdrawal / complaint / manual suppression |

### Initial SMS copy (locked — use verbatim)

**SMS 1 — immediate acknowledgement:**
> Hi {{contact.first_name}}, this is {{user.first_name}} with LeadSniperAI/Paper Lead. We received your request for a business funding assessment. May I ask three brief questions here to help identify the appropriate next step? Reply STOP to opt out.

**SMS 2 — Day 1:**
> Hi {{contact.first_name}}, checking that you received your funding assessment confirmation. Is the primary need working capital, equipment, tariff relief, or another business purpose? Reply STOP to opt out.

**SMS 3 — Day 5:**
> Hi {{contact.first_name}}, should we keep your funding assessment open, schedule a short review, or close it for now? Reply 1 for review, 2 for later, or STOP to opt out.

**Appointment reminder:**
> Reminder: your business funding discovery call is scheduled for {{appointment.start_time}}. Use {{appointment.reschedule_link}} if you need another time. Reply STOP to opt out.

**No-show recovery:**
> Hi {{contact.first_name}}, we missed you for the funding review. If the need is still active, you can choose another time here: {{appointment.reschedule_link}}. Reply STOP to opt out.

**Reactivation SMS (90–180 day cohort only, with manual approval):**
> Hi {{contact.first_name}}, it's {{user.first_name}} from Paper Lead. You previously asked us about business funding. Has your timing or funding need changed? Reply YES to review your options, LATER for another time, or STOP to opt out.

---

## 27. AI Response Boundary (LOCKED)

Conversation AI may answer routine process questions, collect non-sensitive qualification facts, assist with booking. AI must **transfer to human** when contact:

- Asks whether they qualify or requests program recommendation
- Discloses financial distress, insolvency, litigation, urgent payroll risk
- Wants to upload financial documents
- Disputes consent, privacy, fees, sharing
- Asks about rates, approval likelihood, legal/tax treatment, government affiliation
- Presents complex property-equity or regulated financing situation

AI must NOT invent program criteria, promise approval, negotiate financing, collect full financial documents in chat, or continue after opt-out.

---

## 28. Messaging and Privacy Controls (LOCKED)

- Obtain channel-specific consent; retain language/version, source, timestamp
- Initial form must separately explain contact by LeadSniper/Paper Lead AND disclosure to selected categories of qualified funding partners
- Never upload purchased, scraped, or competitor-generated consumer lists into automated SMS campaign
- Use local-time business-hour send windows + frequency caps
- Include sender identity + opt-out; apply DND immediately across affected workflows
- Review HighLevel telephone provider rules before launch (carrier restrictions on financial + third-party lead-gen messaging)
- Privacy/vendor review for GHL + subprocessors, data location, retention, access, export, deletion
- Under Canadian privacy guidance, **organization remains accountable** for personal information processed by service providers; map data flows + ensure comparable protection contractually

---

## 29. Pipeline Lost Reasons (canonical taxonomy)

`Unqualified`, `Duplicate`, `Unable to Contact`, `Withdrawn`, `No Consent`, `Do Not Contact`, `Not Serviceable`, `Buyer Declined`, `Program Ineligible`, `Other Capital Route` — used as structured lost reasons rather than extra columns.

---

## 30. Tag Convention (canonical)

- Source: `src:meta`, `src:google`, `src:seo`, `src:referral`
- Vertical: `vertical:tariff`, `vertical:business-funding`, `vertical:portfolio-equity`
- Province: `province:bc`, `province:ab`, `province:on`
- Consent: `consent:sms`, `consent:email`, `consent:partner-share`
- Priority: `priority:hot`, `priority:standard`
- Control: `control:human-required`, `control:no-automation`, `control:dnd`, `control:sync-error`

---

## 31. KPI Tree

### North-star
- Qualified opportunity revenue
- Funded / successfully completed opportunities
- Buyer repeat purchase rate
- Contribution margin by source, tier, vertical

### Acquisition
- Assessment starts / completions
- Cost per consented inquiry
- Organic conversion rate
- Source-to-qualified-opportunity rate

### Qualification
- Verification completion rate
- Time to qualification
- Tier advancement rate
- Human rejection + correction rate
- Evidence freshness + completeness

### Marketplace
- Listing rate
- Time to first reservation
- Exclusive sell-through
- Shared-seat utilization
- Revenue per opportunity
- Refund, dispute, quality-complaint rate

### Buyer success
- Time to first contact
- Lead acceptance
- Outcome reporting completeness
- Repeat purchase + churn
- Revenue + funded volume by buyer

### Communication
- SMS opt-out, complaint rates
- Email bounce, unsubscribe rates
- Conversion + contribution margin by source, campaign, province, vertical

---

## 32. Weekly Operating Cadence

| Day | Cadence |
|-----|---------|
| **Monday** | Pipeline Review — new assessments, urgent timelines, next-step tasks |
| **Wednesday** | Content & SEO Review — keyword pipeline, pages in production, article owners, AI search visibility |
| **Friday** | Marketplace Review — sold leads, buyer feedback, accepted/rejected, lead quality rules |
| **Monthly** | `/loop` Review — what produced revenue, what ranked, which buyer categories performed, which lead tiers best, what to stop / improve / double down on |

---

## 33. Business Loan Comparison Site — Strategy & Research (linked page)

Notion child page "Business Loan Comparison Site — Strategy & Research" exists. Recommend opening it next for the SEO / directory inventory build. URL not exposed in this fetch — request when needed.

---

## 34. Linked child pages (canonical nav)

- LeadSniperAI Lead Pipeline (database)
- Funding Opportunities (database)
- Marketplace Buyers & Partners (database)
- Content Operating System (database)
- Product & Engineering Tasks (database)
- SOP & Knowledge Base (database)
- KPI / Loop Scorecard (database)
- Paper Lead — Lead Mission Control
- Paper Lead — Technical Architecture v1
- Business Loan Comparison Site — Strategy & Research
- Open Higgsfield — LeadSniperAI Business Funding Creative Studio
- Zeely AI Creative & Campaign Engine — Business Funding + Mortgage Cross-Sell
- LeadSniperAI Pay-Per-Lead Marketplace — 30-Day Launch Plan
- LeadSniper Search Opportunity Engine PRD — Opus + Astra + Hermes + Organic SEO Pipeline
- Financial Services Search-to-Revenue SOP — OpenSEO + Astra + Hermes + Opus

**Critical follow-ups to request from Dennis:**

1. Open each linked page and ingest canonical content (especially **Technical Architecture v1** and **30-Day Launch Plan** — these are the implementation specs)
2. Confirm or override the four named verticals (tariff, business-funding, portfolio-equity, mortgage-cross-sell)
3. Confirm or override the canonical CMS / frontend stack (Astro/React vs WordPress/Divi as public surface)
4. Confirm buyer-pilot scope (BC tariff only? or full national?)
5. Confirm CLAUDE.md is approved for the workspace

---

## 35. What this means for Business Funding Canada — workspace impact

| Workspace artifact | Required content |
|--------------------|-----------------|
| **`IDENTITY.md`** | Already reframed for PPL model; verify vertical taxonomy matches Notion's 14-stage workflow + tariff vertical + portfolio-equity vertical |
| **`_config/voice.md`** | "Transparent matching intermediary" — connecting business owners with qualified funding professionals. NOT lender/broker/approver |
| **`_config/compliance.md`** | Already covers PIPEDA + CASL + per-buyer contracts. Add explicit "no rate quote / no guaranteed approval / no lending language" rules from Notion §19 |
| **`_config/lead-buyer-buyers/`** | NEW directory — Buyer Appetite Matrix template + buyer onboarding checklist + capacity / SLA / replacement policy tracking |
| **`research/competitors/`** | Add buyer-side competitor profiles (Loans Canada, Swoop, Ratehub, Lending Loop, nesto, WOWA, MCAP, CMLS) per Notion §24 teardown list |
| **`drafts/landing-page/`** | First page should be the **Tariff Impact Funding Assessment** (BC-first) per Notion §13 GTM |
| **`drafts/calculators/`** | Build 5–6 canonical tools from §22 list, mobile-first, ≤ 2 min, result-led, PII-free |
| **`drafts/content/`** | Compact-keyword engine: tariff impact funding BC, BC forestry funding, BC manufacturing working capital, etc. |
| **`drafts/buyer-outreach/`** | Five-touch cadence emails + LinkedIn scripts per Notion §16 |
| **`drafts/ghl-build/`** | LS-WF-00 through LS-WF-09 specs, custom fields, tag convention, lost-reason taxonomy |
| **`projects/verticals/`** | BC Tariff (FIRST), then Ontario Tariff, Alberta Tariff, Portfolio Equity, Residential Mortgage Cross-Sell |

---

## 36. Acceptance gates — when this brief is "done"

- [ ] All 36 sections above reviewed by Dennis
- [ ] Notion linked pages (Technical Architecture v1, 30-Day Launch Plan, Comparison Site Strategy) ingested
- [ ] IDENTITY.md and _config/ docs updated to align with Notion §19 compliance boundaries
- [ ] CLAUDE.md approved
- [ ] First vertical (BC Tariff) selected as the build target
- [ ] First deliverable (landing page + lead form + 1 calculator) drafted into `drafts/`