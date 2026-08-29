---
title: "Veritas Development Group — Organic SEO Traffic Plan (v2)"
type: framework-execution-plan
status: DRAFT — pending David + Daniel decisions + Dennis review
created: 2026-08-28
updated: 2026-08-28 (v2: brain-aligned, governance-layered)
owner: Dennis Eng (KlickSmartAI)
client: Veritas Development Group LLC
source_framework: OpenSEO creator doctrine (5 pillars)
source_audit: VERITAS.AUDIT-V4 (2026-08-28, released)
source_score: CLIENT-SCORE-veritas-developments-2026-08-28 (released, 32/100 CONDITIONAL)
source_cover: COVER-NOTE-seo-audit-v4-2026-08-28 (released)
brain_anchor: VERITAS.BRAIN §1–20 (Notion + GitHub wiki + engagement history)

---

## ⚠ Governance binding (per VERITAS.BRAIN §7, §13–18, §18)

This plan is internal working knowledge only. No content, page, outreach, backlink, PR mention, GBP edit, or external draft produced from this plan may be published, sent, posted, or used in conversation with any investor, landowner, lender, tenant, journalist, or member of the public without:

1. Explicit human approval (per §18 agent operating policy)
2. Compliance pre-clearance against §7 hard gates (Reg D 506(b/c), RESPA §8, license fee-splitting, broker-dealer, public solicitation)
3. Evidence-tagging per §13 on every material claim (source_url_or_id, source_owner, retrieved_at, effective_date, verification_status, approved_for_external_use, expires_or_reverify_on)
4. Conflict surfacing per §14 when sources disagree

The §18 prohibitions that bind this plan:
- No publishing project information
- No quoting returns, valuations, or lender terms externally
- No representation of tenant interest as commitment
- No change of compliance status
- No advancement of project stages

Page A, Page C, and the PR pitch each have compliance annotations in the file body. Until §15 Decision Register seeds include a row for each, none of them moves out of drafts.

---

## 0. How this plan reads

This is **not** a generic 5-pillar template applied to Veritas. It is the OpenSEO creator doctrine translated through VERITAS.BRAIN §1–20 into a plan that:

- Treats the 8 winnable keywords as **credibility infrastructure for the JV fundraising funnel**, not as a direct customer-acquisition channel (Pillar 1 warning applied in reverse)
- Carries a 6th pillar — **compliance pre-clearance** — that the creator doctrine doesn't name but the brain's §7 hard gates require
- Anchors every page and outreach in §13 evidence governance and §15 Decision Register rows
- Resolves §14 conflicts when they arise (they will — BOVs are unverified, project stage is pre–Capital Ready, name collision is live)
- Stops at §18 boundaries — no publishing, no outreach, no representations

If the 5 creator pillars alone are wanted, see `wiki/processes/seo-organic-growth-playbook.md` (cross-client operating doctrine). This file is what the doctrine becomes when it has to pass the brain's compliance filter.

---

## 1. Foundation sprint is the precondition, not pillar work

Per the v4 audit and scrapling byte-level pass: `veritasdevelopmentgroupllc.com` is a JS-rendered SPA that returns "You need to enable JavaScript" to crawlers. 0 crawlable words, no H1, no internal links, no backlink footprint, no organic presence. Every Pillar 2–5 deliverable in this plan depends on this being fixed first.

**Foundation sprint scope (3-6 hrs dev, $2,500 one-time):**

| Step | Owner | Hours | Output |
|---|---|---|---|
| nginx + Cloudflare page rules: detect crawler user-agent → swap to SSR snapshot | Dev (David to assign) | 1-2 | Crawlers see HTML, humans see SPA |
| Implement SSR snapshot rendering of homepage + future page templates | Dev | 2-4 | SSR snapshot per route |
| Verify: re-run `run_site_audit` (OpenSEO) + manual `curl -A "Googlebot"` | Dennis + Dev | 0.5 | Audit shows 300+ crawlable words, H1 present, internal links visible |
| GBP claim + verify | David | 0.5 | GBP live at 210 SW Market St, Lee's Summit, MO 64063 |

**Without foundation sprint: zero pillars 2-5 register.** No point writing Pillar 4 content Google can't see.

**§18 note:** the dev team is on Veritas's side, not KlickSmartAI's. Dennis's role is to verify the sprint worked (run audit, confirm crawlable), not to execute it.

---

## 2. The 5-pillar doctrine → Veritas-specific actions

### Pillar 1 — Grounding AI in real data (creator doctrine)

**What it means here:** Don't guess demand; verify with DataForSEO SERP pulls + PAA scans + competitor visibility data before any page gets written.

**Evidence already on disk (the "real data" this plan is grounded in):**

| Source | What it tells us | Cost |
|---|---|---|
| `drafts/website/serp-intelligence-2026-08-28.md` | 160 organic results + 50 competitor rows across 8 winnable entry keywords; 7 of 8 show Local Pack; 1 AI Overview on `commercial real estate loan rates` | ~290 DataForSEO credits |
| `drafts/website/serp-competitor-landscape-2026-08-30.md` | 33-keyword competitive landscape (v3; superseded by v4 SERP but kept for trend signal) | domain-only signal |
| `drafts/website/scrapling-findings-2026-08-30.md` | Byte-level pass confirms SPA render gap; crawlers see `<div id="root"></div>` + app shell | scrapling cost (negligible) |
| `drafts/seo/paa-2026-08-28-multifamily-development-process.md` | 4 PAA, 3 intent groups — "8 stages of real estate development" maps to David's 22-yr ground-up wedge | $0.018 |
| `drafts/seo/paa-2026-08-28-multifamily-co-sponsor.md` | 4 PAA, 2 intent groups — contaminated with immigration/green-card threads; reformulate seed | $0.018 |
| (PAA scans with 0 results) | `kansas city real estate developer` + `multifamily development capital partner` → deal-level RE capital buyers don't search Google PAA; route to GTM, not content | $0.036 |

**The Pillar 1 reading Veritas-specific:** The 8 winnable keywords validate that the SEO strategy can win the local commercial-construction credibility layer. They do NOT validate demand for Evermont-scale capital, multifamily tenants, or landowner-JV partners. Those audiences search on LinkedIn, family-office networks, broker-dealer referrals — different surfaces. **The creator's warning applies in reverse:** don't build a content funnel toward audiences that don't convert at the unit economics you need. SEO for Veritas bottom-funnel = credibility for institutional investor diligence calls; top-funnel = landlord/renovation leads (Track B MOU scope). Mid-funnel (Evermont-scale JV) is GTM, not content.

### Pillar 2 — Niche positioning over broad competition

**Wedge (already locked in v4 audit):** KC commercial-construction sub-market, not national.

**What the data says the wedge is:**

| Position band | Who lives there | Veritas target |
|---|---|---|
| Position 1-3 | vertexkc.com, straubconstruction.com, mccowngordon.com (KC subdomain) — entrenched premium brands | Out of scope for Year 1 |
| Position 4-13 | Diamond, MidAmerica, ARC GC, Black Oak, Centric, Dynamic, Vazquez, Rau, Rothwell — mid-tier local GCs | **6-month target position 8-10** |
| Position 14+ | kcitygeneralcontractors.com (top-2 on one term, page-2 on another), turnerconstruction.com, procore.com, facebook.com | Beatable with strong homepage |

**§13 evidence on every position claim:** the v4 audit's competitor-rows table is `Corroborated` (DataForSEO live pull + SERP-intelligence draft). Before any page publishes, re-run the SERP pull and update the position band — search rank drifts weekly. `expires_or_reverify_on: 2026-09-28`.

**What niche positioning does NOT do for Veritas:** it doesn't position Veritas as a development firm to capital partners. That positioning lives in Notion + the OKF + Loom walkthroughs David sends to Tier 1/2 contacts. SEO builds the "is this firm legit?" layer; David closes the deal.

### Pillar 3 — High-intent keywords vs. vanity metrics

**The 8 winnable keywords, classified by intent + compliance gate:**

| Keyword | Vol/mo | KD | SERP format | Intent class | Compliance gate |
|---|---|---|---|---|---|
| `multifamily contractors` | 90 | 0 | Agency landing pages | Commercial — local | Clear |
| `kansas city corporate housing` | 260 | 1 | Niche-vertical homepages | **NONTARGET** (wrong vertical — furnished short-term rentals, not construction; v3 mis-classified) | n/a |
| `commercial general contractors kansas city` | 110 | 12 | Agency homepages + 2 directories | Commercial — local | **Primary target** |
| `top construction companies in kansas city` | 20 | 18 | Listicle (bizjournals, mccowngordon, glassdoor) | Commercial — local | PR pitch play (Pillar 5b) |
| `kc home renovations` | 390 | 18 | Agency homepages | Commercial — local | Clear |
| `commercial real estate loan rates` | 2,400 | 20 | AI Overview + bank comparisons | Vanity — **AI Overview dominates** | **GATED** — see below |
| `commercial construction kansas city` | 110 | 26 | Agency homepages | Commercial — local | Clear |
| `commercial real estate broker` | 14,800 | 0 | Forum + edu + association | Vanity — wrong audience (broker query, not developer query; Daniel Bailey's KW career is **separate from** Veritas per carve-out) | **NONTARGET for Veritas brand** |

**Compliance gates from §7 that bind keyword classification:**

- **`commercial real estate loan rates` (2,400/mo, AI Overview)** — Writing about "current commercial real estate loan rates" risks being read as Veritas offering capital/financing/lending services (Reg D general-solicitation adjacency). Educational explainer ("What determines commercial real estate loan rates in 2026") is defensible if it leads with explicit Veritas-is-not-a-lender disclaimer + KW-brokerage carve-out + "capital arranged via independent third-party providers" language. **Blocked until Daniel approves compliance framing.** See Decision #1 below.

- **`commercial real estate broker` (14,800/mo)** — Daniel Bailey is a KW broker separately from Veritas. Writing broker-query content under Veritas brand risks blurring KW-Veritas boundary and triggers license fee-splitting concerns (§7.3). **Daniel's call:** write under KW brand on a separate domain, not under Veritas. Move to NONTARGET for this plan.

- **`kansas city corporate housing` (260/mo, KD 1)** — Wrong vertical (furnished apartments, not construction). Move to NONTARGET. Daniel could consider under KW brand.

### Pillar 4 — Real questions, not AI spam

**The 90-day plan is the cap in action:** 3 new pages + GBP setup, not 30.

| Page | Target keyword(s) | Compliance | Why it works |
|---|---|---|---|
| **A. `/commercial-construction-services/`** | `commercial general contractors kansas city` (KD 12), `commercial construction kansas city` (KD 26) | Clear | All 20 organic results are agency homepages — no content-driven SERP. Single locally-optimized service page should hit top 10 in 3-6 months. |
| **B. `/kc-home-renovations-guide/`** | `kc home renovations` (KD 18, 390/mo) | Clear | kchomesolutions.com is the only real domain in top 10; Veritas's renovation service line gives credibility. Track B MOU alignment. |
| **C. `/commercial-real-estate-financing-guide/`** | `commercial real estate loan rates` (KD 20, 2,400/mo) | **GATED — Decision #1 below** | Educational explainer; explicit Veritas-is-not-a-lender; KW-brokerage carve-out; capital-arranged-via-third-party language. **No publish until Daniel approves.** |

**PAA-driven FAQ schema per page (Pillar 4 "answer real questions"):**

- Page A: 6-8 PAA-derived questions from `multifamily development process` scan (4 PAA confirmed)
- Page B: 4-6 PAA-derived questions from `kc home renovations` PAA scan (not yet pulled — budgeted in §7)
- Page C: 3-5 PAA-derived questions from `commercial real estate loan rates` PAA scan (must be pulled pre-publish to verify AI Overview hasn't absorbed them)

**The 4 PAA scans already run are the data; the 2 still needed are budgeted.** Total Pillar 4 cost: ~$0.15 in Serper.dev credits.

**Hard cap (cross-client rule from playbook):** 10 pages/quarter default. Veritas runs at 3/quarter (30%). Plenty of headroom for stonehaven content post-foundation sprint verification.

### Pillar 5a — Internal linking & on-site structure (machine-readable now)

**The structural work, not the content work:**

| Element | Status post-foundation-sprint | Tool to verify |
|---|---|---|
| H1 on every page | 1/1 currently (homepage only); all 3 new pages need H1 | OpenSEO `run_site_audit` |
| Internal links from `/` to each service page | 0 currently | OpenSEO `run_site_audit` |
| Internal links between service pages | 0 currently | OpenSEO `run_site_audit` |
| FAQ schema on every service page | 0 currently | Schema.org validator + Rich Results Test |
| City-modifier in H1/H2 (Lee's Summit, Blue Springs, Independence, Raymore) | 0 currently | Manual |
| NAP consistency (name/address/phone) across site + GBP + directories | Unverified | Manual + `whitespark` (if available) |
| Image alt text with city + project type | 0 currently | Manual |

**§13 evidence on each link:** every internal link added gets logged in a `drafts/website/link-graph-changelog-2026-MM-DD.md` file with `source_url`, `target_url`, `anchor_text`, `verification_status: Verified`. This is the audit trail when institutional investor counsel asks "what does your link structure look like?"

### Pillar 5b — Authority building & outreach automation

**Veritas-appropriate channels (NOT the creator's broken-link-replacement play):**

| Channel | Effort | Compliance gate | Decision needed |
|---|---|---|---|
| **KC Business Journal / bizjournals.com listicle pitch** | PR pitch draft (Dennis → David for approval) | §18 — no PR without human approval | **Decision #2 below** |
| **NAIOP Kansas City / Lee's Summit Chamber speaking slot** | David's existing relationships | §18 — David handles, no KlickSmartAI involvement | David to confirm availability |
| **LS Economic Development Council partner page** | Application + tier commitment | §18 — David handles | David to confirm |
| **Municipal Planning Commission / City Council meeting coverage** | Wait for Evermont approvals (when in Capital Ready stage) | §7.1 + §15 — public-solicitation concerns until MOU signed | Blocked until MOU + Reg D confirmed |
| **Broken-link outreach automation** | Out of scope — wrong audience | n/a | n/a (the creator's play doesn't fit a development-stage firm) |

**The mechanical-broken-link automation (crawl → email extract → CRM track) from the creator's doctrine doesn't apply to Veritas.** Veritas builds authority via project deliveries + PR + civic presence, not via replacing dead industry resources. The Pillar 5b spirit (other reputable sites mention you) applies; the mechanism doesn't.

---

## 3. Pillar 6 — Compliance pre-clearance (the doctrine forgot this one)

**Every page and every outreach above requires §7 + §13 + §18 clearance before execution.** The hard gates:

### 3.1 Page-level pre-clearance

| Page | §7 hard-gate check | §13 evidence-tagging required fields | §18 approval required |
|---|---|---|---|
| Page A (commercial-construction-services) | None — service description, no securities/brokerage/lending claims | service area (per writing_preferences), project portfolio (with §13 tags), team bios (with §13 tags) | Dennis approval on draft |
| Page B (kc-home-renovations-guide) | None — service description | same as A | Dennis approval |
| Page C (commercial-real-estate-financing-guide) | **§7.1 Reg D 506(b/c) — must NOT be read as Veritas offering capital/financing services.** Explicit disclaimer + KW-brokerage carve-out + "capital arranged via independent third-party providers" language required. | lender terms (none invented; if quoted, source from public Lender Matrix Pro Notion DB §11), rate claims (none made), educational-only framing | **Daniel + counsel approval** before draft begins |

### 3.2 PR pitch pre-clearance

BizJournals listicle pitch for `top construction companies in kansas city`:
- §18 — no PR mention without human approval (David reviews draft before any send)
- §1 — name collision (bizjournals lists 6+ "Veritas" firms; pitch must disambiguate with "Lee's Summit" + "David Poole" + Evermont project name)
- §13 — every project claim tagged; BOV figures (`$20.5M shovel-ready / $35M per apartment building`) are logged Draft/Unverified per §4; **must not appear in PR pitch until §15 Decision Register has a row marking them Approved**

### 3.3 §15 Decision Register — rows this plan requires before publish

| Decision/assumption | Project/phase | Owner | Status |
|---|---|---|---|
| Veritas-is-not-a-lender disclaimer language approved for Page C | Evermont / Phase 0 | Daniel Bailey | **Proposed — Decision #1** |
| BizJournals PR pitch approved for send | Veritas brand | David Poole | **Proposed — Decision #2** |
| BOV $20.5M / $35M figures verified or struck | Evermont | Daniel Bailey | Existing Draft/Unverified |
| SEO investment ($20,500 Year-1) approved | Veritas brand | David Poole | Existing MOU Track A scope |
| GBP categories + service area approved | Veritas brand | David Poole | Existing — pre-approval |
| Foundation sprint $2,500 + 3-6 hrs dev approved | Veritas brand | David Poole | **Proposed — implicit in foundation sprint scope** |

The first row and second row block Page C and the PR pitch respectively. Until those land, both stay in drafts.

---

## 4. The 30/60/90 timeline (with foundation sprint as Day 0)

### Day 0-14 — Foundation sprint (precondition)

- David approves foundation sprint ($2,500 + dev time)
- Dev executes nginx + Cloudflare + SSR snapshot
- Dennis re-runs OpenSEO audit; verifies 300+ crawlable words, H1, internal links visible
- David claims/verifies GBP

### Day 15-45 — Pillar 4 page production

- Pull `kc home renovations` PAA scan ($0.018)
- Pull `commercial real estate loan rates` PAA scan ($0.018) — needed for Page C FAQ
- Page A draft → Dennis review → David review → publish
- Page B draft → Dennis review → David review → publish
- Page C: BLOCKED on Daniel's Reg-D compliance call (Decision #1)

### Day 46-75 — Pillar 5b + Pillar 5a polish

- BizJournals PR pitch draft (Dennis) → David review → send (Decision #2)
- NAIOP / LS Chamber / LS EDC: David confirms availability, KlickSmartAI no involvement
- Internal link graph audit + add cross-links between published pages
- FAQ schema validation on all published pages
- NAP consistency check across GBP + site + Yelp + BBB

### Day 76-90 — Verification + KPI baseline

- Re-run v4-equivalent SERP pull; compare position band to baseline
- Run `get_search_console_performance` + `get_google_business_questions` once GSC + GBP scopes granted
- Document KPI baseline in `drafts/website/seo-kpi-baseline-2026-MM-DD.md`
- Schedule quarterly re-audit (per playbook 5a cadence)

### Out of scope for Year 1

- Page C (`commercial-real-estate-financing-guide`) until Daniel clears compliance
- Stonehaven content until Evermont P1 raise underway
- LinkedIn automation (Unipile reconciliation §9 — higher ban risk than generic ToS concern)
- Capital-partner content funnel (Evermont / Stonehaven investor decks live in Notion + Loom, not on Veritas's website)

---

## 5. Cost summary

| Category | Item | Cost |
|---|---|---|
| **Foundation sprint (Day 0)** | Dev time + infra | $2,500 one-time |
| **Pillar 1 data** | DataForSEO SERP pull + competitor visibility | ~290 credits (already spent v4 audit) |
| **Pillar 4 PAA scans** | 2 remaining scans | ~$0.04 |
| **Pillar 4 content** | 3 pages (or 2 if Page C blocked) | $0 (in-house writing; David + Dennis) |
| **Pillar 5b PR pitch** | BizJournals outreach | $0 (organic PR; relationship-based) |
| **Pillar 5b civic presence** | NAIOP / LS Chamber / EDC | TBD (David's existing relationships) |
| **Retained SEO** | Quarterly re-audit + content refresh | $1,500/mo (per client score bundle) |
| **Year-1 total** | Foundation + retained × 12 | **$20,500** (per client score) |
| **Year-2+ annual** | Retained only | $18,000/yr |

**Year-1 ROI at $50-75/click midpoint (per client score):** 482%-1,647% range. ROI assumes SEO drives credibility-infrastructure traffic that converts at the development-fee + JV-promote unit economics — not at the reno-contract unit economics the $25-$100/click range was sized to. **The 1,647% headline number is aspirational; the conservative band (482%) is the planning number.**

---

## 6. Decisions blocking this plan (the 2 calls to make)

### Decision #1 — Daniel Bailey: Reg-D adjacency on Page C

**Context:** `commercial real estate loan rates` is 2,400/mo, KD 20, has AI Overview. Veritas is not a direct lender. The v4 cover note flagged this in §16.3 of the released cover note. Per §7.1, no investor outreach under Veritas name until MOU signed AND Reg D exemption confirmed.

**The question:** does an educational explainer — "What determines commercial real estate loan rates in 2026: a KC developer's perspective" — with these explicit features cross the compliance line?

- Title makes no claim to offer capital/financing/lending
- Lead paragraph: "Veritas Development Group is not a licensed lender or broker-dealer. This page is educational; capital for projects Veritas is involved in is arranged via independent third-party providers with whom Veritas has no agency relationship."
- Footer disclaimer on every page in this category
- No rate tables, no rate forecasts, no "contact us for financing" CTA
- KW-brokerage carve-out language: "Lee's Summit brokerage services are offered separately by Keller Williams affiliated licensees; this page is not a solicitation of brokerage services"

**If YES:** Page C enters production in Day 15-45.
**If NO / uncomfortable:** Page C stays in drafts. Pages A + B + GBP still deliver ~80% of Year-1 SEO value per client score. Drop C3 entirely; no SEO loss.

**Why this matters for the playbook:** the framework's Pillar 4 ("real questions, not spam") and §7 hard gates pull in opposite directions here. The right answer is the one Daniel is comfortable with. Not mine to make.

### Decision #2 — David Poole: KC Business Journal PR pitch

**Context:** `top construction companies in kansas city` is KD 18, 20/mo, listicle SERP. v4 audit proposed the BizJournals pitch as a PR play (not content play). Pitch is for inclusion in an existing or upcoming KC construction listicle, not for a paid placement.

**The question:** does David want to pursue the BizJournals pitch?

**If YES:** Dennis drafts the PR pitch outline (200-300 words, project-led, name-disambiguated per §1, no BOV figures, no capital-raised claims). David reviews. David sends.
**If NO:** drop the PR pitch from the plan. No SEO loss — the listicle keyword is 20/mo; the value is brand authority, not traffic.

---

## 7. Open questions / data gaps (carried from brain + audit)

| Gap | Source | Owner | Blocks |
|---|---|---|---|
| 3 Evermont underwriting data gaps (full rent comps, signed Block & Co presale, executed shovel-ready sales contract) | §4, §8 | David + Daniel | Evermont institutional materials (not SEO directly) |
| BOV $20.5M / $35M figures verified or struck | §4 | Daniel Bailey | Any mention in PR pitch or Page C |
| Webmaster Tools + GBP scope grants for OpenSEO | §8 | David | KPI baseline + ongoing rank tracking |
| Phase 0 compliance gate confirmation (MOU signed + Reg D + RESPA) | §7, §8 | David + counsel | Any investor-adjacent content (Page C, BizJournals pitch) |
| NAIOP / LS Chamber / LS EDC relationship status | §6, §10 | David | Pillar 5b civic channels |
| 2 remaining PAA scans (`kc home renovations`, `commercial real estate loan rates`) | §3 | Dennis | Page B + C FAQ content |

---

## 8. What this plan does NOT do

- Does not generate Evermont investor materials (Notion + Loom + Frappe `Capital Mandate` DocType, not website)
- Does not replace the KV Capital Advisor compliance pre-clearance workflow (`compliance_gate.py` kill-switch)
- Does not recommend LinkedIn automation (Unipile risk §9)
- Does not produce paid placement / sponsored content (creator doctrine anti-pattern)
- Does not expand beyond 3 pages in Year 1 without explicit human approval (Pillar 4 cap)
- Does not produce any external communication without §18 human approval (sender, audience, sources, unresolved claims, required approval — all identified in every draft)

---

## 9. Files referenced (Veritas workspace + cross-workspace)

**Released (source of truth):**
- `projects/website/seo-audit-veritasdevelopmentgroupllc-2026-08-28-client.md` — v4 audit (client-facing, 25417 bytes, 303 lines)
- `projects/website/CLIENT-SCORE-veritas-developments-2026-08-28.md` — 32/100 CONDITIONAL, ROI breakdown, $20,500 Year-1
- `projects/website/COVER-NOTE-seo-audit-v4-2026-08-28.md` — keyword reclassifications + SERP format winners + 90-day plan + 2 decisions

**Drafts (evidence layer):**
- `drafts/website/serp-intelligence-2026-08-28.md` — 160 organic + 50 competitor rows
- `drafts/website/serp-competitor-landscape-2026-08-30.md` — 33-keyword v3 landscape
- `drafts/website/scrapling-findings-2026-08-30.md` — byte-level render-gap confirmation
- `drafts/website/seo-audit-veritasdevelopmentgroupllc-2026-08-28.md` — v4 audit (internal version)
- `drafts/website/serp-intelligence-2026-08-28.md` — SERP raw pulls

**Cross-workspace (OpenSEO):**
- `wiki/clients/open-seo/drafts/seo/paa-2026-08-28-multifamily-development-process.md` — 4 PAA, 3 intent groups
- `wiki/clients/open-seo/drafts/seo/paa-2026-08-28-multifamily-co-sponsor.md` — 4 PAA, 2 intent groups (reformulate)
- `wiki/processes/seo-organic-growth-playbook.md` — cross-client operating doctrine

**Brain (governance layer):**
- VERITAS.BRAIN §1-20 (Notion + GitHub wiki source)

---

## 10. Approval status

**Status:** DRAFT — pending

**Pending approvals to flip status to APPROVED:**

| Approval | Owner | Block on |
|---|---|---|
| Framework alignment with brain (Dennis) | Dennis | This file |
| Foundation sprint $2,500 + 3-6 hrs dev | David | §3.1 + §4 Day 0-14 |
| Decision #1 — Page C compliance framing | Daniel | §6 |
| Decision #2 — BizJournals PR pitch | David | §6 |
| Page A + B drafts review | Dennis + David | §4 Day 15-45 |

Once all 5 land, this plan moves from `drafts/` to `projects/website/` and the foundation sprint starts.

---

*"The doctrine tells you what to do. The brain tells you what not to do. The plan tells you when."*
