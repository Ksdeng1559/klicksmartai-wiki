# Business Loan Marketplace — Website Wireframe (v1)

**Date:** 2026-09-14
**Site root:** mortgagesbydenniseng.ca/business-loans/
**Total pages:** 88 (from sitemap.md)
**Lender anchors:** Glasslake Funding, Triple Queens, Kingsmen Capital + BDC comparison + Swoop-style multi-lender
**Target keyword universe:** ~41,580 vol/mo across 9 tiers

---

## Design principles

1. **Comparison-site architecture, not broker-site.** Swoop dominates on "business loan" head terms with 757 indexed URLs. We compete by being the **honest multi-lender comparison site** with named anchors (BDC + Glasslake + Triple Queens + Kingsmen) and clear editorial bias disclosure.
2. **BDC as the trust anchor.** Government-backed, 100,000+ clients, $58.6B committed, 82% client satisfaction. BDC is the only lender the entire Canadian market trusts — feature them prominently on every "how to qualify" page.
3. **Honest lender positioning.** BDC = cheapest but most restrictive. Glasslake = owner-occupied specialty. Triple Queens = speed. Kingsmen = SMB accessibility. Multi-lender Swoop/online = convenience. The wireframe must show all five tiers, not just one.
4. **Mortgage-lens as differentiator.** Every commercial-lending page should have a "Mortgage Lens" section: "Before you borrow on the business, consider HELOC or refinance on the property." This is structurally impossible for credit brokers like Swoop.
5. **Lead capture at intent moments, not random CTAs.** Lead forms appear when the user is clearly choosing a product (after the rate table, before the FAQ).

---

## Site IA (information architecture)

```
mortgagesbydenniseng.ca/
└── /business-loans/                    ← cornerstone + nav root (T0)
    ├── /business-loan/                 ← T1 head term
    ├── /business-loans-canada/         ← T1 head term (CA-intent)
    ├── /small-business-loan/           ← T1 head term
    ├── /small-business-loans/          ← T1 head term
    ├── /small-business-loan-canada/    ← T1 head term
    ├── /small-business-loans-canada/   ← T1 head term
    ├── /small-business-funding/        ← T1 variant
    ├── /how-to-get-a-business-loan/    ← T1 educational
    │
    ├── /business-line-of-credit/       ← T2 pillar (general)
    ├── /unsecured-business-loans/      ← T2 pillar
    ├── /short-term-business-loans/     ← T2 pillar
    ├── /working-capital-loans/         ← T2 pillar
    ├── /long-term-business-loan/       ← T2 pillar
    │
    ├── /bdc-business-loan/             ← T3 government
    ├── /small-business-loan-bdc/       ← T3 (existing)
    ├── /bdc-vs-private-lender/         ← T3 (existing)
    ├── /bdc-vs-private-lender-decision-tree/ ← T3
    ├── /bdc-loan-requirements/         ← T3
    ├── /csbfp-alternative/             ← T3
    ├── /canada-small-business-financing-program/ ← T3 (CSBFP)
    ├── /government-grants-canada/      ← T3 (lead magnet, 1,800 vol/mo)
    │
    ├── /bridge-financing-canada/       ← T6 Triple Queens anchor
    ├── /private-mortgage-lender-canada/ ← T6
    ├── /construction-financing-canada/ ← T6 Triple Queens
    ├── /land-acquisition-financing-canada/ ← T6
    ├── /invoice-factoring-canada/      ← T6 Triple Queens
    ├── /accounts-receivable-financing-canada/ ← T6 (highest CPC)
    ├── /business-line-of-credit-canada/ ← T6 Triple Queens + multi
    ├── /mezzanine-financing-canada/    ← T6
    ├── /commercial-mortgage-broker-canada/ ← T6 Glasslake anchor
    ├── /commercial-mortgage-alberta/   ← T6 Vector 6B-2
    ├── /commercial-mortgage-bc/        ← T6 Vector 6B-2
    ├── /commercial-mortgage-ontario/   ← T6 Vector 6B-2
    ├── /gas-station-commercial-mortgage/ ← T6 Vector 6B-3
    ├── /restaurant-commercial-mortgage/ ← T6 Vector 6B-3
    ├── /auto-dealership-financing/     ← T6 Vector 6B-3
    ├── /mixed-use-property-mortgage/   ← T6 Vector 6B-3
    ├── /hotel-commercial-mortgage/     ← T6 Vector 6B-4
    ├── /commercial-mortgage-declined/  ← T6 Vector 6B emergency
    ├── /commercial-mortgage-not-renewing/ ← T6 Vector 6B emergency
    ├── /cmhc-mli-select-guide/         ← T6 Vector 6B-4
    ├── /construction-to-permanent-financing/ ← T6 Vector 6B-4
    ├── /self-employed-business-loans/  ← T6 Vector 6A
    ├── /asset-based-line-of-credit-canada/ ← T6 Kingsmen
    ├── /cra-arrears-financing-canada/  ← T6 Kingsmen
    ├── /ceba-loan-consolidation-canada/ ← T6 Kingsmen
    │
    ├── /tariff-financing-canada/       ← T5 Kingsmen anchor
    ├── /bdc-tariff-loan-vs-private-lender/ ← T5
    │
    ├── /best-business-loans-canada/    ← T4 best-X
    ├── /best-small-business-loan-canada/ ← T4
    ├── /best-business-line-of-credit-canada/ ← T4
    ├── /best-unsecured-business-loan/  ← T4
    ├── /best-business-loan-ontario/    ← T4
    ├── /best-short-term-business-loan/ ← T4
    ├── /best-business-loan-for-bad-credit/ ← T4
    │
    ├── /business-loan-for-restaurant/  ← T4 vertical
    ├── /construction-business-loan/    ← T4 vertical
    ├── /trucking-company-loans/        ← T4 vertical
    ├── /manufacturing-business-loan/   ← T4 vertical
    ├── /ecommerce-business-loan/       ← T4 vertical
    ├── /business-loan-for-self-employed/ ← T4 vertical
    ├── /business-loan-for-startups/    ← T4 vertical
    ├── /business-loan-for-real-estate-investors/ ← T4 vertical
    ├── /business-purchase-loan/        ← T4 vertical
    ├── /retail-business-loans/         ← T4 NEW Kingsmen
    ├── /salon-business-loans/          ← T4 NEW Kingsmen
    ├── /auto-repair-shop-loans/        ← T4 NEW Kingsmen
    ├── /delivery-business-loans/       ← T4 NEW Kingsmen
    ├── /medical-practice-loans/        ← T4 NEW Kingsmen
    ├── /liquor-store-business-loans/   ← T4 NEW Kingsmen
    ├── /coffee-shop-business-loans/    ← T4 NEW Kingsmen
    │
    ├── /business-loan-requirements/    ← T0 educational
    ├── /business-loan-documents-needed/ ← T0 educational
    ├── /business-loan-qualification-checklist/ ← T0 lead magnet
    ├── /credit-score-business-loan/    ← T0 educational
    ├── /how-to-qualify/                ← T0
    ├── /bad-credit-business-loans/     ← T0
    ├── /low-credit-business-loan/      ← T0
    ├── /fast-business-loan/            ← T0
    ├── /quick-business-loans/          ← T0
    │
    ├── /lenders/                       ← T8 lender directory
    ├── /lender-comparison/             ← T8 marketplace
    ├── /business-lending/              ← T8 hub
    ├── /lending-for-business/          ← T8
    ├── /loan-business-loan/            ← T8 variant
    │
    ├── /about/                         ← T8
    ├── /contact/                       ← T8
    ├── /disclosure/                    ← T8 (FSRA compliance)
    └── /privacy-policy/                ← T8
```

---

## Homepage / Cornerstone wireframe (`/business-loans/`)

The cornerstone targets **25,400 vol/mo of head terms** and serves as the navigation hub for the entire site.

```
┌─────────────────────────────────────────────────────────┐
│ HEADER                                                  │
│ - Logo (Mortgages by Dennis Eng — Business Loans)       │
│ - Phone: [dennis's direct line]                         │
│ - Nav: Loans | LOC | Unsecured | By Industry |          │
│        By Province | Lenders | Mortgage Lens | About    │
│ - [Get a 15-min call →] CTA button                      │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ HERO                                                    │
│                                                         │
│ # Business Loans in Canada: Compare 50+ Lenders         │
│ One Site. Every Option. Independent Mortgage-Broker     │
│ Advice.                                                 │
│                                                         │
│ [Compare your options →]   [Talk to a broker →]         │
│                                                         │
│ Trust signals:                                          │
│ • 100,000+ BDC clients served (BDC partner signal)      │
│ • 25+ Canadian lenders in our network                   │
│ • Licensed mortgage broker (FSRA / provincial)          │
│ • Independent — we don't lend, we match                 │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ SECTION 1 — How Much Can I Borrow? (INTERACTIVE WIDGET) │
│                                                         │
│ [Loan Amount: $50K - $5M slider]                        │
│ [Purpose: dropdown — Working capital, Equipment,        │
│  Real estate, Acquisition, Pay debt]                   │
│ [Time in business: 0-24+ months]                        │
│                                                         │
│ [See your options →]                                    │
│                                                         │
│ Output: 4 lender matches (BDC, Glasslake, Kingsmen,     │
│ Triple Queens) with their ranges, rates, and CTAs       │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ SECTION 2 — Loan Types (TILED GRID)                     │
│                                                         │
│ 6 cards, each linking to a T2 pillar:                   │
│ ┌──────────┐ ┌──────────┐ ┌──────────┐                 │
│ │ Working  │ │ Line of  │ │ Unsecured│                 │
│ │ Capital  │ │ Credit   │ │ Loans    │                 │
│ │ $660/mo  │ │ $2,680/mo│ │ $2,080/mo│                 │
│ └──────────┘ └──────────┘ └──────────┘                 │
│ ┌──────────┐ ┌──────────┐ ┌──────────┐                 │
│ │ Short    │ │ Long     │ │ Equipment│                 │
│ │ Term     │ │ Term     │ │ Loan     │                 │
│ │ $810/mo  │ │ $20/mo   │ │ $8,900/mo│                 │
│ └──────────┘ └──────────┘ └──────────┘                 │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ SECTION 3 — Who We Work With (LENDER ANCHORS)           │
│                                                         │
│ 4-column comparison:                                    │
│ ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐            │
│ │ BDC    │ │ Glass- │ │ Triple │ │ Kings- │            │
│ │        │ │ lake   │ │ Queens │ │ men    │            │
│ │ $58B   │ │ $200K- │ │ $2M+   │ │ $25K-  │            │
│ │ commit │ │ $5M    │ │ speed  │ │ $10M   │            │
│ │ Cheapest│ │ Owner- │ │ Bridge │ │ SMB    │            │
│ │ Restr- │ │ occup. │ │ ABL    │ │ ABL    │            │
│ │ ictive │ │         │ │         │ │         │            │
│ └────────┘ └────────┘ └────────┘ └────────┘            │
│                                                         │
│ + 50+ other lenders (banks, B-lenders, credit unions,   │
│   online lenders, factoring, equipment financers)       │
│                                                         │
│ Disclosure: Dennis is a licensed mortgage broker.       │
│ Commissions vary by lender. We may earn a fee on        │
│ funded loans.                                            │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ SECTION 4 — Mortgage Lens (DIFFERENTIATOR)              │
│                                                         │
│ ## Stop. Before you borrow on the business,             │
│ consider these alternatives:                            │
│                                                         │
│ ┌─────────────────────┐ ┌─────────────────────┐         │
│ │ HELOC               │ │ Refinance property  │         │
│ │ Borrow against your │ │ Pull equity out of  │         │
│ │ home equity at      │ │ your commercial     │         │
│ │ 5-7% rates          │ │ property for cash   │         │
│ │                     │ │                     │         │
│ │ [How it works →]    │ │ [How it works →]    │         │
│ └─────────────────────┘ └─────────────────────┘         │
│ ┌─────────────────────┐ ┌─────────────────────┐         │
│ │ CMHC MLI Select     │ │ Self-employed       │         │
│ │ Insured multi-res   │ │ mortgage — stated   │         │
│ │ financing at lower  │ │ income options      │         │
│ │ rates               │ │                     │         │
│ │                     │ │                     │         │
│ │ [How it works →]    │ │ [How it works →]    │         │
│ └─────────────────────┘ └─────────────────────┘         │
│                                                         │
│ These options are structurally unavailable to credit    │
│ brokers like Swoop. We can advise on them because we    │
│ are licensed mortgage brokers.                          │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ SECTION 5 — By Industry (TILED GRID)                    │
│                                                         │
│ 16 industry tiles (most popular 8 shown):               │
│ Restaurant | Construction | Trucking | Manufacturing |  │
│ E-commerce | Real Estate | Retail | Healthcare |       │
│ Salon | Auto Repair | Delivery | Medical | Liquor |     │
│ Coffee | Bars | Daycares | ...                          │
│                                                         │
│ Each tile → industry-specific landing page              │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ SECTION 6 — By Province (TILED GRID)                    │
│                                                         │
│ Ontario | British Columbia | Alberta | Quebec |         │
│ Saskatchewan | Manitoba | Nova Scotia | New Brunswick   │
│                                                         │
│ Each tile → province-specific landing page              │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ SECTION 7 — Educational Resources (TILED GRID)          │
│                                                         │
│ 6 educational pillar pages:                             │
│ • How to Qualify for a Business Loan                    │
│ • Business Loan Requirements (documents)                │
│ • Credit Score for Business Loans                       │
│ • How to Get a Business Loan (10-step guide)            │
│ • Business Loan Qualification Checklist (PDF)           │
│ • Bad Credit Business Loans                             │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ SECTION 8 — Recent Articles / Blog                      │
│                                                         │
│ 3 most recent posts from /blog/                         │
│ (also surface tariff content here when active)          │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ SECTION 9 — Lead Form (FINAL CTA)                       │
│                                                         │
│ ## Not sure where to start? Talk to a broker.           │
│                                                         │
│ [15-min call → form fields]                             │
│ Fields: name, business name, time in business,           │
│ annual revenue, loan amount, province, email, phone,    │
│ purpose (dropdown)                                       │
│ Routing: Dennis + email nurture sequence                │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ FOOTER                                                  │
│ • Lender directory (50+ names, alphabetized)            │
│ • Comparison tables index                               │
│ • By province | By industry | By purpose                │
│ • About | Contact | Disclosure | Privacy                │
│ • Mortgage broker license # (FSRA / provincial)        │
│ • Disclaimer: not tax/legal/investment advice           │
└─────────────────────────────────────────────────────────┘
```

---

## Tier-2 pillar page wireframe (example: `/business-loans/business-line-of-credit/`)

T2 pages target 660-2,680 vol/mo clusters each. This is the template used for the 5 commercial-lending product pillars.

```
┌─────────────────────────────────────────────────────────┐
│ HEADER (same as cornerstone)                            │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ HERO                                                    │
│ # Business Line of Credit in Canada (2026 Guide)        │
│ Compare $50K-$5M LOCs from banks, B-lenders, and       │
│ private lenders. Find the right fit in 15 minutes.      │
│ [Get a 15-min call →]                                   │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ DIRECT ANSWER (snippet bait, ~80 words)                 │
│ "A business line of credit (LOC) is revolving working   │
│ capital that businesses draw as needed, paying interest │
│ only on the amount used..."                             │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ HOW IT WORKS (3-step visual)                            │
│ [Apply] → [Get approved] → [Draw as needed]             │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ LENDER COMPARISON TABLE (THE CONVERSION PIECE)          │
│                                                         │
│ | Lender | Min | Max | Rate | Speed | Best for |       │
│ |--------|-----|-----|------|-------|----------|       │
│ | Big 6 banks | 25K | 5M | Prime + 0.5-4% | 2-6 wks | Established |       │
│ | BDC | 100K | 350K | Floating base + variance | <30 days | 24+ mo in biz |       │
│ | Glasslake | 200K | 5M | TBD | 30-90 days | Owner-occupied |       │
│ | Kingsmen | 50K | 10M | TBD | 3-5 days | 1-2 yr in biz |       │
│ | Triple Queens | 2M+ | 5M+ | TBD | 5-10 days | Asset-based |       │
│ | B-lenders | 50K | 1M | Prime + 4-8% | 1-3 wks | Bank-rejected |       │
│ | Online | 10K | 500K | 8-15% | 1-3 days | Fast funding |       │
│                                                         │
│ Lead form: [Get matched →]                              │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ TYPES OF LOCs (sub-content block)                       │
│ • Operating LOC (revolving)                             │
│ • Asset-based LOC                                       │
│ • Revenue-based LOC                                     │
│ • Seasonal LOC                                          │
│ • Business credit card (small-scale)                    │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ MORTGAGE LENS (DIFFERENTIATOR)                          │
│ ## Could a HELOC be cheaper?                            │
│ If you own your home or commercial property, a HELOC   │
│ or commercial refinance could give you capital at 5-7% │
│ rates — often cheaper than any business LOC.            │
│ [Compare HELOC vs LOC →]                               │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ WHO QUALIFIES (4 paths)                                 │
│ • Bank path (24+ mo, strong revenue, collateral)        │
│ • BDC path (24+ mo, $100K+ revenue, good credit)        │
│ • Private path (Kingsmen, Glasslake — alt criteria)     │
│ • Bridge path (Triple Queens — asset-based)             │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ FAQ (10 questions, FAQPage schema)                      │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ RELATED PAGES (sidebar)                                 │
│ • T2 siblings: unsecured, short-term, working capital   │
│ • T3 government: BDC, CSBFP                             │
│ • T6 anchors: business-line-of-credit-canada, etc.      │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ LEAD FORM (bottom)                                      │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ FOOTER (same as cornerstone)                            │
└─────────────────────────────────────────────────────────┘
```

---

## Tier-3 government comparison page wireframe (example: `/business-loans/bdc-vs-private-lender/`)

T3 pages are the comparison site moat — Swoop can't publish this content because their commission model excludes lending comparisons.

```
┌─────────────────────────────────────────────────────────┐
│ HERO                                                    │
│ # BDC vs Private Lender: Which Is Right for You?       │
│ Side-by-side comparison of rates, terms, requirements,  │
│ and best use cases for Canada's two main business       │
│ funding paths.                                          │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ DIRECT ANSWER (snippet bait)                            │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ AT-A-GLANCE COMPARISON TABLE                            │
│ | Factor | BDC | Private Lender |                       │
│ |--------|-----|----------------|                       │
│ | Min time in biz | 24 months | 12 months (Kingsmen) |  │
│ | Min revenue | $100K (BDC) | None |                   │
│ | Min credit | 600 personal | No min (Kingsmen) |       │
│ | Speed | 10-30 days | 3-10 days |                     │
│ | Rate | Cheapest (floating base + variance) | Higher | │
│ | Max loan | $350K (SBL) / $5M+ (CRE) | $10M+ |        │
│ | Best for | Established, profitable | Bank-rejected |  │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ WHEN BDC MAKES SENSE (300 words)                        │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ WHEN PRIVATE LENDER MAKES SENSE (300 words)             │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ PRIVATE LENDER COMPARISON                               │
│ ┌──────────┐ ┌──────────┐ ┌──────────┐                 │
│ │ Glasslake│ │ Triple   │ │ Kingsmen │                 │
│ │ $200K-$5M│ │ Queens   │ │ $25K-    │                 │
│ │ Owner-   │ │ $2M+     │ │ $10M     │                 │
│ │ occupied │ │ Speed    │ │ SMB      │                 │
│ └──────────┘ └──────────┘ └──────────┘                 │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ DECISION TREE (visual)                                  │
│ [Are you in business 24+ months?]                      │
│    YES → [Revenue >$100K?] → YES → [Credit >600?] →     │
│          YES → BDC                                        │
│          NO → B-lender / Glasslake                       │
│    NO → Kingsmen (12+ mo) / Swoop                       │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ COST SCENARIOS (3 worked examples)                      │
│ $100K @ 5 years: BDC vs Glasslake vs Kingsmen          │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ FAQ                                                     │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ RELATED: BDC tariff loan, CSBFP, Government Grants     │
└─────────────────────────────────────────────────────────┘
```

---

## Tier-6 anchor page wireframe (example: `/business-loans/commercial-mortgage-broker-canada/`)

T6 anchor pages are the **highest-revenue pages** — they feature a named lender and have lead forms that route directly to that lender with broker permission.

```
┌─────────────────────────────────────────────────────────┐
│ HERO                                                    │
│ # Commercial Mortgage Broker Canada:                    │
│ Owner-Occupied Lending Guide (2026)                    │
│ From $200K to $5M. Glasslake Funding + 50+ lenders.    │
│ Compare rates, terms, and qualification.               │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ DIRECT ANSWER (snippet bait, ~100 words)                │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ GLASSLAKE FEATURED PROFILE (THE ANCHOR)                 │
│ ┌─────────────────────────────────────┐                │
│ │ Glasslake Funding                   │                │
│ │ Bayview Asset Management subsidiary │                │
│ │                                     │                │
│ │ ✓ $200K - $5M                       │                │
│ │ ✓ 1-7 year terms                    │                │
│ │ ✓ Up to 80% LTV                     │                │
│ │ ✓ 30-90 day funding                 │                │
│ │ ✓ Owner-occupied specialty          │                │
│ │ ✓ Self-employed / bank-rejected OK  │                │
│ │                                     │                │
│ │ BC contact: Russell Veronelly       │                │
│ │ 587-847-5361                        │                │
│ │                                     │                │
│ │ [Apply with Glasslake →]            │                │
│ └─────────────────────────────────────┘                │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ OWNER-OCCUPIED VS INVESTMENT (sub-content)              │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ CURRENT RATE TABLE (Q3 2026)                            │
│ | Lender type | Rate range | Term | LTV max |          │
│ | CMHC-insured | 4.25-5.50% | 1-5 yr | 85% |          │
│ | Big 6 banks | 5.50-7.00% | 1-5 yr | 75% |           │
│ | BDC Commercial RE | Prime + variance | up to 25 yr | up to 100% | │
│ | Glasslake (alt lender) | 7.00-10.00% | 1-7 yr | 80% | │
│ | B-lender | 7.00-9.00% | 1-3 yr | 70% |              │
│ | Private (Trez, Romspen) | 8.00-12.00% | 1-3 yr | 70% | │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ COST COMPONENTS (rate + amortization + prepayment      │
│ penalty + lender fee + broker fee + appraisal +         │
│ legal + Phase 1 environmental)                          │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ COMMERCIAL MORTGAGE CALCULATOR (interactive)            │
│ Inputs: amount, LTV, term, amortization, rate           │
│ Outputs: monthly payment, total interest, DSCR          │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ RENEWAL SEASON BANNER (Q3-Q4 only)                      │
│ "Is your commercial mortgage renewal coming up?         │
│ Get a 2026 rate comparison."                           │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ 4 RELATED EMERGENCY/VERTICAL ANCHOR PAGES              │
│ • Commercial mortgage not renewing                      │
│ • Commercial mortgage declined                          │
│ • Gas station commercial mortgage                       │
│ • Restaurant commercial mortgage                        │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ FAQ (10+ questions)                                     │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ LEAD FORM (HIGH-VALUE — Glasslake routing)              │
│ Fields: name, business, property address, loan amount,  │
│ current lender (if renewal), purpose, urgency           │
│ Routing: Dennis (primary) + Glasslake BDM (with consent) │
└─────────────────────────────────────────────────────────┘
```

---

## Tier-5 tariff page wireframe (example: `/business-loans/tariff-financing-canada/`)

T5 is event-driven — gets a traffic spike during tariff news. Lead form is Kingmen-anchored.

```
┌─────────────────────────────────────────────────────────┐
│ HERO                                                    │
│ # Tariff Financing Canada: How Importers &             │
│ Manufacturers Survive New Tariff Costs                  │
│ Working capital, term loans, and ABL to bridge tariff  │
│ gaps in 3-30 days.                                      │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ DIRECT ANSWER (snippet bait)                            │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ CURRENT CONTEXT (kept fresh — manual update monthly)    │
│ "As of [month], [tariff summary from news]..."          │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ KINGSMEN FEATURED (anchor)                              │
│ Term loans 3-5 day funding                              │
│ Asset-based LOC up to $10M for importers                │
│ [Apply via Kingsmen →]                                 │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ 4 WAYS TO FUND TARIFF GAPS                              │
│ 1. Term loan (3-5 days, Kingsmen)                       │
│ 2. Asset-based LOC (revolving, A/R-based)               │
│ 3. BDC tariff loan (if applicable — confirm)            │
│ 4. Factoring / A/R financing (Triple Queens)            │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ BDC VS PRIVATE LENDER TARIFF LOAN (comparison)          │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ FAQ                                                     │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ LEAD FORM — IMPORTER / MANUFACTURER INTAKE              │
└─────────────────────────────────────────────────────────┘
```

---

## T8 utility page wireframes

### `/business-loans/lenders/` (Lender Directory)
Alphabetized grid of 50+ lenders with logo, name, range, best for, link to dedicated page (where exists) or external site (where not). BDC, Glasslake, Triple Queens, Kingsmen featured at top.

### `/business-loans/lender-comparison/` (Marketplace)
Filterable table: amount, property type, time in business, geography, product type. JS-powered (faceted search).

### `/business-loans/about/`
Dennis's bio, brokerage (Mortgage Architects / Verico), license #, contact, regulatory disclosure.

### `/business-loans/disclosure/`
FSRA compliance, broker commission disclosure, conflict of interest statement, lender relationships list.

---

## Header navigation (final)

```
Loans      → /business-loan/ + head terms
LOC        → /business-line-of-credit/
Unsecured  → /unsecured-business-loans/
By Industry → /business-loan-for-restaurant/ (auto-tile)
By Province → /business-loans-canada/ontario/ (auto-tile)
Lenders    → /lenders/
Mortgage Lens → /self-employed-business-loans/ (HELOC + RE finance)
About      → /about/
Get a call → lead form (every page)
```

---

## Footer navigation

```
Loan types     → all 5 T2 pillars + 8 T6 product anchors
Industries     → all 17 vertical pages
Provinces      → 4-9 province pages
Government     → all 5 T3 pages
Resources      → 6 educational pages + lead magnets
About          → about, disclosure, privacy, contact
```

---

## Lead form variants (3 types)

### A. Quick match form (header / corner)
- Fields: name, phone, email
- Routing: email to Dennis, nurture sequence triggered

### B. Product match form (mid-page on T2/T6 anchors)
- Fields: name, business name, time in business, annual revenue, loan amount, purpose (dropdown), province
- Routing: Dennis + lender-matched (with consent)

### C. Specific deal form (T6 commercial mortgage anchor)
- Fields: name, business, property address, loan amount, current lender (if renewal), purpose, urgency
- Routing: Dennis + Glasslake BDM (with consent)

---

## Critical UI elements (across all pages)

| Element | Where | Why |
|---|---|---|
| Trust badge: "Licensed mortgage broker — FSRA / provincial" | Header + footer | Compliance + differentiation vs Swoop |
| Trust badge: "Independent — we don't lend, we match" | Homepage hero | Build trust vs broker conflict of interest |
| Trust badge: "BDC partner" (only if true — confirm) | Homepage | Government signal |
| Commission disclosure | Footer of every page | FSRA requirement |
| "Last updated [date]" | Every page | E-E-A-T signal |
| Author byline (Dennis) | Every page | E-E-A-T |
| Phone number visible | Header + footer | Trust + conversion |
| FAQ accordion | Every T1/T2/T6 page | Featured snippet + UX |
| Schema: Article, FAQPage, BreadcrumbList | Every page | SEO |
| Interactive calculator | T2 LOC + T6 commercial mortgage pages | Engagement + lead qualification |
| Sidebar "Related guides" | Every T2/T6 page | Internal linking |
| "Mortgage Lens" callout | Every commercial-lending page | Differentiation |

---

## Build sequence (12-month plan from sitemap.md)

| Month | Pages | Tier | Volume target |
|---|---|---|---|
| 1-2 | 22 | T0 (13) + T1 (9) | 5,000 sessions/mo |
| 3 | 7 | T6 Vector 6B-1 (1) + T2 split (5) + T6 bridge (1) | 8K-12K sessions/mo |
| 4 | 5 | T3 (5) | 12K-16K sessions/mo |
| 5-6 | 14 | T4 Best X (7) + T4 vertical existing (4) + T6 emergency (2) + T5 tariff (1) | 15K-22K sessions/mo |
| 7 | 6 | T4 vertical Kingsmen (3) + T6 Vector 6B-3 (2) + T6 Vector 6A (1) | 18K-28K sessions/mo |
| 8-9 | 14 | T4 vertical Kingsmen remaining (4) + T6 Vector 6B-4 (3) + T6 Kingsmen special (3) + lead magnets (4) | 22K-32K sessions/mo |
| 10-12 | 5 | T6 Triple Queens adjacents (3) + T8 marketplace (2) | 28K-45K sessions/mo |

---

## Files on disk

- This document: `~/wiki/clients/business-loans-canada/wireframe.md`
- Source data: `~/wiki/clients/business-loans-canada/sitemap.md`
- Strategy: `~/wiki/clients/business-loans-canada/strategy/*.md`
- Lender analyses: `../../research/glasslake-funding/`, `../../research/triplequeens-bridge/`, `../../research/kingsmen-capital/`

---

## Open questions / decisions before build

1. **FSRA license # to display** — confirm Dennis's license number + jurisdiction (BC? ON?)
2. **BDC partner signal** — verify if Dennis has formal BDC referral agreement or just uses BDC as comparison anchor
3. **Brokerage branding** — Mortgage Architects or Verico (or both?) — confirm
4. **Email for lender routing** — separate inboxes per lender? Or all to Dennis with auto-distribute?
5. **Bilingual coverage** — Kingsmen has Quebec French. Does Dennis serve Québec? If yes, add French pages
6. **Phone number** — confirm
7. **Lead form CRM** — what tool? (HubSpot, Mailchimp, custom form-to-email?)
