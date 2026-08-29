# Veritas v2 Plan Brief — for Dennis

**Audience:** Dennis Eng (KlickSmartAI).
**Source:** `wiki/clients/veritas-developments/drafts/website/framework-execution-plan-2026-08-28.md` (370 lines, 27.6 KB, DRAFT).
**Status:** Brain-aligned + governance-layered. Flips to APPROVED once the 5 approvals in §10 land.

---

## What v2 changes from v1

| | v1 (audit-only spine) | v2 (brain-aligned spine) |
|---|---|---|
| **Spine** | 5 OpenSEO creator pillars | 5 OpenSEO pillars + 6th pillar (compliance pre-clearance) |
| **Authority** | OpenSEO doctrine only | Doctrine **filtered through VERITAS.BRAIN §1-20** |
| **Reading posture** | SEO = customer acquisition | SEO = **credibility infrastructure** for JV fundraising funnel |
| **Compliance framing** | Implied / ad-hoc | §7 hard gates (Reg D 506(b/c), RESPA §8, license fee-splitting, broker-dealer) bind every page |
| **Decision gate** | Loose | **§15 Decision Register rows** must exist before anything leaves `drafts/` |
| **Precondition** | Implied | **Foundation sprint** ($2,500 + 3-6 hrs dev) explicit; without it, zero pillars 2-5 register |

---

## Foundation sprint is the actual Day 0

The site is a JS SPA that returns "enable JavaScript" to crawlers. 0 crawlable words, no H1, no internal links. Every other deliverable in this plan depends on this being fixed first.

- **Cost:** $2,500 one-time + 3-6 hrs dev time.
- **Owner:** David (assigns dev) → Dennis (verifies via OpenSEO audit + `curl -A Googlebot`).
- **Without it:** Pillar 4 content Google can't see = zero pillar 4-5. No point writing the pages.
- **Dennis role boundary:** Verify, don't execute. The dev team is on Veritas's side.

---

## The 6 pillars (brain-filtered)

| Pillar | What it means for Veritas |
|---|---|
| **0 — Foundation sprint** | SSR snapshot + crawler detection; GBP claim |
| **1 — Real data grounding** | 8 winnable entry keywords verified via DataForSEO SERP + PAA + competitor pulls (already on disk, ~290 credits spent) |
| **2 — Internal-link graph** | Cross-link Pages A+B+C + GBP once published |
| **3 — NAP consistency** | GBP + site + Yelp + BBB |
| **4 — Real questions, not spam** | 3 pages (`kc home renovations`, `commercial real estate loan rates` blocked, `kansas city general contractor`), capped at 10/quarter per doctrine |
| **5a — Reputation + updates** | GBP posts, schema validation, quarterly re-audit |
| **5b — Partnership-channel links** | BizJournals PR + NAIOP / LS Chamber / LS EDC civic presence (David's existing relationships) |
| **6 — Compliance pre-clearance (NEW)** | Every page + outreach pre-cleared against §7 hard gates + §15 Decision Register row |

---

## The 8 winnable keywords

Treated as **credibility infrastructure**, not direct customer acquisition:

| Keyword | Volume/mo | KD | SERP format | Page |
|---|---|---|---|---|
| `kc home renovations` | 590 | 6 | Local Pack + organic | Page A |
| `kansas city general contractor` | 320 | 11 | Local Pack | Page B |
| `commercial real estate loan rates` | 2,400 | 20 | AI Overview | **Page C — BLOCKED on Decision #1** |
| `top construction companies in kansas city` | 20 | 18 | Listicle | PR pitch, not content (Decision #2) |
| (4 more — see §2 of plan) | | | | |

---

## The 2 pending decisions (the only thing actually blocking)

### Decision #1 — Daniel Bailey: Reg-D adjacency on Page C

**The question:** Does an educational explainer on `commercial real estate loan rates` cross the compliance line?

**Concrete features that would make it YES-safe:**
- Title makes no claim to offer capital / financing / lending.
- Lead paragraph: *"Veritas Development Group is not a licensed lender or broker-dealer. This page is educational; capital for projects Veritas is involved in is arranged via independent third-party providers with whom Veritas has no agency relationship."*
- Footer disclaimer on every page in this category.
- No rate tables, no rate forecasts, no "contact us for financing" CTA.
- KW-brokerage carve-out: *"Lee's Summit brokerage services are offered separately by Keller Williams affiliated licensees; this page is not a solicitation of brokerage services."*

**If YES:** Page C enters Day 15-45 production.
**If NO / uncomfortable:** Page C stays in drafts. Pages A + B + GBP still deliver ~80% of Year-1 SEO value per client score. Drop C3 entirely; no SEO loss.
**Not mine to make.** Daniel's call.

### Decision #2 — David Poole: KC Business Journal PR pitch

**The question:** Does David want to pursue the BizJournals inclusion in a KC construction listicle?

- `top construction companies in kansas city` is KD 18, 20/mo, listicle SERP.
- Pitch is for inclusion in an existing or upcoming listicle, **not paid placement**.
- If YES: Dennis drafts the pitch (200-300 words, project-led, name-disambiguated per §1, no BOV figures, no capital-raised claims) → David reviews → David sends.
- If NO: drop the PR pitch. No SEO loss — 20/mo is brand-authority value, not traffic.

---

## 30/60/90 (with foundation sprint as Day 0)

| Window | Deliverable | Blocked on |
|---|---|---|
| **Day 0-14** | Foundation sprint + GBP claim + audit re-run | David approves $2,500 + dev time |
| **Day 15-45** | Page A + Page B drafts → review → publish | Dennis + David review |
| **Day 15-45** | **Page C** | **Decision #1 (Daniel)** |
| **Day 46-75** | BizJournals PR pitch → review → send | **Decision #2 (David)** |
| **Day 46-75** | NAIOP / LS Chamber / LS EDC civic presence | David confirms availability |
| **Day 46-75** | Internal link graph audit + FAQ schema + NAP check | — |
| **Day 76-90** | v4-equivalent SERP re-pull + KPI baseline + quarterly re-audit schedule | GSC + GBP scopes |

**Out of scope Year 1:** Page C if blocked, Stonehaven until Evermont P1 raise underway, LinkedIn automation (Unipile risk §9), capital-partner content funnel (Evermont/Stonehaven decks live in Notion + Loom + Frappe, not the website).

---

## Cost ($20,500 Year-1 per client score)

| Category | Cost |
|---|---|
| Foundation sprint (Day 0, one-time) | $2,500 |
| Pillar 1 data (already spent v4 audit) | ~290 DataForSEO credits |
| Pillar 4 PAA scans (2 remaining) | ~$0.04 |
| Pillar 4 content (3 pages, in-house) | $0 |
| Pillar 5b PR pitch | $0 (organic PR) |
| Pillar 5b civic channels | TBD (David's existing relationships) |
| Retained SEO (quarterly re-audit + content refresh) | $1,500/mo |
| **Year-1 total** | **$20,500** |
| **Year-2+ annual** | $18,000/yr (retained only) |

**ROI band at $50-75/click midpoint:** 482% – 1,647%. **The 1,647% headline is aspirational; 482% is the planning number.** ROI assumes SEO drives credibility-infrastructure traffic that converts at development-fee + JV-promote unit economics, NOT at the reno-contract unit economics the $25-$100/click range was sized to.

---

## 5 approvals to flip status to APPROVED

| # | Approval | Owner | Block on |
|---|---|---|---|
| 1 | Framework alignment with brain | **Dennis** | This file |
| 2 | Foundation sprint $2,500 + dev time | David | §3.1 + §4 Day 0-14 |
| 3 | **Decision #1** — Page C compliance framing | **Daniel** | §6 |
| 4 | **Decision #2** — BizJournals PR pitch | **David** | §6 |
| 5 | Page A + B drafts review | Dennis + David | §4 Day 15-45 |

Once all 5 land, the file moves from `drafts/` → `projects/website/` and the foundation sprint starts.

---

## What this plan does NOT do

- Does not generate Evermont investor materials (Notion + Loom + Frappe `Capital Mandate` DocType, not website).
- Does not replace the KV Capital Advisor compliance pre-clearance workflow.
- Does not recommend LinkedIn automation.
- Does not produce paid placement / sponsored content.
- Does not expand beyond 3 pages in Year 1 without explicit human approval.
- Does not produce any external communication without §18 human approval.

---

## Open questions (carried from brain + audit)

| Gap | Owner | Blocks |
|---|---|---|
| 3 Evermont underwriting data gaps (rent comps, Block & Co presale, shovel-ready PSA) | David + Daniel | Evermont institutional materials |
| BOV $20.5M / $35M figures verified or struck | Daniel | Any mention in PR pitch or Page C |
| Webmaster Tools + GBP scope grants for OpenSEO | David | KPI baseline + ongoing rank tracking |
| Phase 0 compliance gate (MOU signed + Reg D + RESPA) | David + counsel | Any investor-adjacent content |
| NAIOP / LS Chamber / LS EDC relationship status | David | Pillar 5b civic channels |
| 2 remaining PAA scans | Dennis | Page B + C FAQ content |

---

*"The doctrine tells you what to do. The brain tells you what not to do. The plan tells you when."*
