# KommercialConnect Landing Pages — Build Index

**Built:** 2026-10-17
**Source research:** `/home/denni/wiki/clients/konstruction-comos/research/`
**Total:** 6 pages, 2,208 lines, 168 KB
**Style:** Self-contained static HTML (matches the existing Next.js dashboard dark/cyan theme)

## Pages Built

### Borrower pages (commercial financing) — `financing/`

| # | File | Target keyword | Vol | CPC | KD | Why |
|---|---|---|---|---|---|---|
| 1 | `private-lender-bc.html` | `private lender bc` | 210 | $18.99 | 0 | **#1 blue ocean** — no BC credit unions, no large lenders, mostly thin content. Single highest-value page. |
| 2 | `commercial-construction-financing-vancouver.html` | `commercial construction financing vancouver` | empty | n/a | n/a | Empty SERP, blue ocean. 18+ lender directory, 4 case studies, 3-path framework. |
| 3 | `vancouver-purpose-built-rental-loan.html` | `vancouver purpose built rental loan` | n/a | n/a | n/a | Blue ocean, no commercial lenders in SERP. 3-path framework (CMHC MLI Select / B-lender / private). |
| 4 | `apartment-construction-loan-program-bc.html` | `apartment construction loan program bc` | 260 | $13.66 | 16 | High-volume blue ocean, 1 lender (LendCity) only. CMHC ACLP guide + qualification framework. |

### Broker pages (recruiting) — `brokers/`

| # | File | Target keyword | Vol | CPC | KD | Why |
|---|---|---|---|---|---|---|
| 5 | `commercial-mortgage-broker-vancouver.html` | `commercial mortgage broker vancouver` | 20 | $10.18 | 0 | Blue ocean, 0 BC competitors. Dual-purpose: directory for borrowers + recruitment for brokers. |
| 6 | `join-as-broker.html` | (recruitment) | n/a | n/a | n/a | Direct broker recruitment landing. 4-tier fee split (70/75/80/85%), 6-feature value prop, 4-step application. |

## Each Page Includes

1. **Hero with eyebrow + 4-stat band** (vol, rate, time, cost)
2. **Definition section** (AI-Overview-citable: direct answer at the top)
3. **Decision framework** (when to use this vs. alternatives)
4. **2026 rate / cost table** (real BC market data)
5. **Curated directory** (10-24+ lenders with criteria, LTV, specialty)
6. **4-6 anonymized case studies** (real deal structures from 2025-2026)
7. **Process / how-to section** (numbered steps)
8. **FAQ** (5-8 questions, schema-marked FAQPage)
9. **Lead capture form** (matched to deal type)
10. **Cross-link footer** (other KommercialConnect pages)

## SEO Features Per Page

- **Meta tags:** title, description, keywords, canonical, OG tags
- **Schema markup:**
  - Article (headline, author, datePublished)
  - FAQPage (5-8 Q&A pairs)
  - LocalBusiness (where applicable)
- **Open Graph:** og:title, og:description, og:type, og:url
- **Canonical:** unique per page, points to `https://kommercialconnect.ca/`
- **AI-Overview-citable content:** direct definitions, scannable tables, factual answers
- **Internal linking:** every page links to 4-6 other KommercialConnect pages

## Brand Notes

**Live site brand is "Klick2Client" (Lovable)** — separate from this naming. **KonstructionComOS** is the GitHub repo brand. **KommercialConnect** is the working SEO/lead-gen brand. The pages use **KommercialConnect** as the working name per the canonical `_config/project-context.md`. When the brand is finalized, the logo + nav can be globally swapped in minutes (search/replace "KommercialConnect").

## How to Deploy

### Option A: Drop into the Lovable public site
1. Open each .html file
2. Copy the body content (everything between `<body>` and `</body>`)
3. Paste into a new Lovable page route
4. Update the nav, footer, and CTA links to use Lovable's `<Link>` components

### Option B: Add to the Next.js KonstructionComOS repo
1. Move .html files to `src/app/(marketing)/<slug>/page.tsx` and convert to JSX
2. Each page is fully self-contained: copy styles into the page module or a global CSS
3. Replace form actions with real API routes (`/api/apply`)

### Option C: Host as standalone static site
1. `cd /home/denni/wiki/clients/konstruction-comos/landing-pages`
2. Drop into a static host (Vercel, Netlify, Cloudflare Pages)
3. Point `kommercialconnect.ca` to the host
4. Wire up forms to a backend (Webhook, ConvertKit, HubSpot, etc.)

## Form Backing

Forms currently `alert()` on submit (demo). In production:
- POST to `/api/apply` with `{name, email, phone, dealType, city, loanAmount, summary}`
- Backend: send to email + CRM + Slack notification
- Per KlickSmartAI policy: drafts go to Gmail Drafts, not sent autonomously (broker outreach requires approval)
- For broker applications: separate endpoint with BCFSA verification queue

## Compliance Notes

- All pages cite BCFSA, BC Mortgage Services Act (in force 2026-10-13)
- "KommercialConnect is not a lender" disclaimer in footer
- No false claims about rates — all rates cited with "as of October 2026" qualifier
- No personal data collection beyond form submission
- CASL: form submissions imply consent to contact, with unsubscribe in all auto-replies
- Broker recruitment is selective (BCFSA registration required) — not a public offer

## What's Next

1. **Brand decision** (PRD §15): finalize the public marketing brand name
2. **Domain:** register the chosen brand domain (kommercialconnect.ca, klick2client.ca, or other)
3. **Deploy:** drop pages into Lovable or Next.js
4. **Wire forms:** connect to backend (HubSpot, webhook, ConvertKit)
5. **Submit to Google Search Console** for the new domain
6. **Add tier 2 + 3 pages** (commercial construction loan vancouver, construction loan vancouver, commercial mortgage, CMHC MLI Select, etc.)

## File Manifest

```
landing-pages/
├── README.md                                          (this file)
├── financing/
│   ├── private-lender-bc.html                         (39.9 KB, 596 lines)
│   ├── commercial-construction-financing-vancouver.html (28.4 KB, 363 lines)
│   ├── vancouver-purpose-built-rental-loan.html       (18.4 KB, 260 lines)
│   └── apartment-construction-loan-program-bc.html    (20.4 KB, 286 lines)
└── brokers/
    ├── commercial-mortgage-broker-vancouver.html      (26.4 KB, 383 lines)
    └── join-as-broker.html                            (21.3 KB, 320 lines)
```
