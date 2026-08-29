---
title: SEO Organic Growth Playbook — Pillars, Execution, and Gates
created: 2026-08-28
updated: 2026-08-28
type: playbook
tags: [seo, organic-growth, content, ai-seo, geo, playbook, hitl, openseo, how-to]
sources:
  - veritas-developments:projects/website/seo-audit-veritasdevelopmentgroupllc-2026-08-28-client.md (PRIMARY — the released v4 audit)
  - veritas-developments:projects/website/CLIENT-SCORE-veritas-developments-2026-08-28.md
  - veritas-developments:projects/website/COVER-NOTE-seo-audit-v4-2026-08-28.md
  - veritas-developments:drafts/website/serp-intelligence-2026-08-28.md
  - veritas-developments:drafts/website/seo-audit-veritasdevelopmentgroupllc-2026-08-28.md (draft predecessor of v4)
  - veritas-developments:drafts/website/scrapling-findings-2026-08-30.md
  - open-seo:drafts/seo/audit-2026-08-26-example-com.md (pilot — replaced by Veritas audit)
  - open-seo:drafts/seo/paa-2026-08-28-multifamily-development-process.md (Pillar 3 case study A)
  - open-seo:drafts/seo/paa-2026-08-28-multifamily-co-sponsor.md (Pillar 3 case study B)
  - open-seo:drafts/seo/paa-2026-08-26-best-seo-tools.md
  - open-seo:_config/seo-skill-catalog.md
  - open-seo:_config/seo-skills.md
  - veritas-developments:IDENTITY.md, veritas-developments:_config/compliance.md
  - content-growth-strategies.md
  - lead-sniperai-cli-os.md (Pillar 3 verify-elsewhere routing)
related: [content-growth-strategies, seo-client-onboarding-sprint, ai-seo]
status: DRAFT — pending HITL approval
---

# SEO Organic Growth Playbook

> **Insight-first framing.** The OpenSEO creator's playbook is not a list of features — it is a set of **gates that prevent wasted spend**. Each pillar below names the failure mode it prevents, then the Hermes skill + MCP tool + cost gate that enforces it.

## Where the evidence comes from

This playbook is **anchored in the v4 Veritas Development Group audit, 2026-08-28** (RELEASED, `veritas-developments/projects/website/seo-audit-veritasdevelopmentgroupllc-2026-08-28-client.md`). That audit is the only end-to-end completed run of all 5 pillars on a real client, with live OpenSEO data, published client score (`CLIENT-SCORE-veritas-developments-2026-08-28.md`, 32/100 CONDITIONAL, 1,647% Year-1 ROI at the $75/click midpoint), and David-validated next steps. Every pillar cites the specific finding + page in that audit that proves the principle. Earlier pilot artifacts (`audit-2026-08-26-example-com.md`, the 2026-08-26 PAA scans) are retained as historical but are **not** the spine.

The 4 PAA scans I ran on Veritas-shaped seeds (2026-08-28, $0.072) live in Pillar 3 as **supporting evidence** for the demand-discovery decision tree — they cover write / reformulate / route-to-GTM outcomes in one client. They are not the primary case study; the Veritas v4 audit's 90-day content plan is.

## Scope

This playbook is the **cross-client operating doctrine** for any SEO engagement that uses OpenSEO (the 50-tool MCP server at `127.0.0.1:3005`). It is the strategic layer above `wiki/processes/seo-client-onboarding-sprint.md` (which governs the first 70 minutes) and below per-client `_config/seo-skills.md` (which governs binding).

For client-specific execution, follow the per-client skill catalog binding in `clients/<slug>/_config/seo-skills.md` and the vertical map in `open-seo/_config/seo-skills.md`.

## The principle

Most SEO failures are not technical — they are **discipline failures**. A page that ranks but does not convert. A keyword that gets traffic but no pipeline. A piece of content that is published because a calendar said so, not because a person asked. The pillars below are the disciplines that prevent those outcomes, mapped to the OpenSEO tools that produce the evidence.

## The 5 pillars

| # | Pillar | Failure mode it prevents | Primary OpenSEO tool |
|---|--------|--------------------------|----------------------|
| 1 | Niche positioning over broad keywords | Chasing head terms you cannot win | `domain-research`, `keyword-research` |
| 2 | High-intent over vanity volume | Ranking for traffic that never converts | `keyword-research` + intent filters |
| 3 | Real demand, not guesswork | Writing what you *think* people want | `paa-demand-mining` (flagship) |
| 4 | Quality over AI bulk spam | Publishing 1,000 pages Google flags as spam | `content-optimization` (per-page HITL) |
| 5 | Structuring + authority | Pages that nobody can find, link to, or extract | `site-audit`, `get_backlinks_*` (gap) |

---

## Pillar 1 — Niche positioning over broad keywords

**Principle.** Win a specific, underserved sub-market before competing in broad categories. A niche term has small volume at first; the focused traffic compounds.

**Hermes execution.**

| Step | Tool | Cost gate |
|------|------|-----------|
| 1. Scaffold client workspace | `icm-client-workspace-setup` | free |
| 2. Intake: domain + ICP + 3-5 seed terms | `openseo-project-intake` (`create_project` + `update_project_context`) | free |
| 3. Map the niche's organic footprint | `domain-research` (`get_domain_overview`, `get_ranked_keywords`) | DataForSEO per call |
| 4. Validate sub-niche with a real keyword universe | `keyword-research` (`research_keywords`, `find_serp_competitors`) | ~96 cr per seed batch |
| 5. Lock the niche: 1 sub-market, 1 wedge term | Human decision | — |

**Hard rule.** A client engagement may not start producing content until the niche + wedge term are written into the OpenSEO project context (`update_project_context`). No context = no content.

**Evidence from the field — Veritas v4 audit (2026-08-28).** The v3 audit initially identified 33 candidate keywords; the v4 SERP intelligence pass (`drafts/website/serp-intelligence-2026-08-28.md`) re-scoped the niche to **8 winnable entry keywords in the Kansas City commercial-construction sub-market**. The repositioning was empirical, not philosophical:

- **42% of 160 organic titles name a KC-area city** (localization is the dominant signal).
- The 7 commercial-intent KC queries cluster at position 4-13 with mid-tier local GCs (Straub, Diamond, MidAmerica, ARC GC) — a **realistic 6-month target for Veritas to rank in position 8-10** below Vertex + McCownGordon.
- The 1 informational Reg-D-adjacent query (`commercial real estate loan rates`, 2,400/mo) was **separated** from the brand and routed to a compliance-gated educational page.

**The lesson.** Niche positioning is not "pick a wedge term and hope." It is the **empirical match between the client's reachable competitor set and the client's deliverable capacity**. The Veritas v3→v4 pass discarded 25 of 33 keywords that the v3 audit had over-confidently included. The audit re-run is the niche.

---

## Pillar 2 — High-intent over vanity volume

**Principle.** A keyword ranking #1 for 100k impressions and zero conversions is worse than a keyword ranking #5 for 800 impressions and 30 trial signups. Optimize for **commercial intent**, not raw volume.

**Intent taxonomy (use as filter on every keyword universe):**

| Class | Signal words | OpenSEO filter |
|-------|--------------|----------------|
| **Commercial** | `best`, `top`, `review`, `comparison`, `vs`, `alternative`, `for [use case]`, `pricing`, `cost` | Required default |
| **Transactional** | `buy`, `pricing`, `sign up`, `get`, `download` | Required default |
| **Informational** | `what is`, `how to`, `guide` | Allowed only with downstream CTA |
| **Navigational** | brand terms | Skip — you already own or don't |

**Hermes execution.**

1. `keyword-research` runs return raw keyword data. Before any content is briefed, **filter the universe**:
   - Drop informational-only clusters without a downstream CTA.
   - Drop navigational queries.
   - Cap the universe at the top 30 commercial-intent terms per sub-niche.
2. Write the filter rule into the OpenSEO project context: `keyword_intent_filter: commercial+transactional_only`.
3. The `seo-enrichment-planner` Phase 0 cost estimate must include the **filter rationale**, not just the keyword count.

**Hard rule.** No content production run begins on a keyword with intent class `informational` unless the brief explicitly documents the downstream CTA. The brief is a row in `drafts/VALIDATION_QUEUE.md` and gets HITL review.

**Evidence from the field — Veritas v4 audit (2026-08-28).** The SERP intelligence reclassified 2 of 8 keywords by intent class, **after** the live data was in:

- `kansas city corporate housing` (260/mo, KD 1) — **moved to NONTARGET** because the SERP returns furnished-apartment-rental listings, not construction. v3 had included it as a winnable term. The intent class is *navigational-vertical*, not commercial-construction.
- `commercial real estate broker` (14,800/mo, KD 0) — **moved to Daniel's KW SEO backlog**, not Veritas. v3 had it in the Veritas universe at a huge volume; the audit re-classified it because the SERP returns forum + association + educational content (Reddit, CCIM), and writing a broker-targeted page on Veritas.com would blur the Reg-D carve-out that keeps Daniel's KW brokerage separate.
- `commercial real estate loan rates` (2,400/mo, KD 20) — **retained** but compliance-gated. Educational explainer only, explicit "not a lender" disclaimer, deferred to Row 8 of `drafts/VALIDATION_QUEUE.md`.

**The lesson.** Volume alone is the wrong filter. A 14,800/month term that returns Reddit threads in the top 5 is a *forum* opportunity, not a *commercial-construction-developer* opportunity. **The SERP format, not the volume, decides the intent class.** Re-pull the SERP before the brief.

**Counter-example (from the OpenSEO creator's brief).** Ranking for "backlink checker" generates hundreds of thousands of impressions and almost no customers. The fix is **not** to rank better for "backlink checker" — it is to *not target it* and target "ahrefs alternative for agencies" instead.

---

## Pillar 3 — Real demand, not guesswork

**Principle.** Every piece of content answers a question a real person asked. The source is `paa-demand-mining` (OpenSEO's flagship use-case), not what an LLM thinks people might want.

**Hermes execution.**

| Step | Tool | Output |
|------|------|--------|
| 1. Pick a seed from the keyword universe (Pillar 2) | — | 1 seed |
| 2. Run PAA + social mining | `paa-demand-mining` (`run_paa_mining`) | PAA questions + intent clusters + social threads + pain points |
| 3. Read the structured report | `get_paa_scan` | Angle surfaces |
| 4. Pick 1-3 angle surfaces (not all 4) | Human decision | Brief row in `drafts/` |
| 5. Write the piece, with citations to the PAA source | `content-optimization` (if page exists) or direct write | Published page |

**Cost gate.** PAA scans are cheap (~$0.018 via Serper.dev) but the **writing** is the expensive step. Gate the writing, not the scan. Scan freely; write with approval.

### Pillar 3 case study — three Veritas-shaped seeds, three verdicts (US, 2026-08-28, $0.072)

To test the demand-discovery layer against Veritas-shaped language, I ran 4 PAA scans at $0.018 each. The results span the full Pillar 3 decision tree — write, reformulate, and verify-elsewhere — all on one client, for a quarter of a dollar.

**Scan A: `multifamily development process` — `b5caf62e-f015-49bc-b2c6-85ea2269dc5e`.**
- 4 PAA questions, 3 intent groups (`what_is` + `other` + `problem`).
- 24 demand-signal phrases, 2 pain points. Top PAA: "What are the 8 stages of real estate development?", "What is a multifamily development?", "Do developers usually own the land?", "Is multifamily real estate in trouble?"
- Pain point: *"build five luxury townhomes. It's very difficult to determine value because there are no [comparables]."*
- **Verdict: WRITE.** All four PAA questions map directly to Veritas's wedge (David's 22-year ground-up track record, Lee's Summit mixed-use, vertically-integrated trades). Draft brief: "The 8 stages of multifamily development: a Lee's Summit ground-up case study."
- Full report: `open-seo/drafts/seo/paa-2026-08-28-multifamily-development-process.md`

**Scan B: `multifamily co-sponsor` — `629dec18-cd74-4ac3-b4ae-be965dbe4cc4`.**
- 4 PAA questions, 2 intent groups (`comparison` + `what_is`).
- 20 phrases, 0 pain points. The real problem: the top PAA question ("sponsor vs co-sponsor") returns **immigration-law Reddit threads and Quora brand-sponsorship answers** as the dominant social signal. Question #4 is literally "What is a co-sponsor for a green card application?"
- **Verdict: REFORMULATE.** Real demand exists in RE for the co-sponsor concept, but the term is overloaded. Write the article only after re-seeding with cleaner terms: `co-GP vs LP real estate syndication`, `multifamily joint venture equity partner`, or `multifamily development equity partner`. Run a fresh PAA scan on each before committing any page.
- Full report: `open-seo/drafts/seo/paa-2026-08-28-multifamily-co-sponsor.md`

**Scan C: `kansas city real estate developer` and `multifamily development capital partner`.**
- 0 PAA questions each. 0 intent groups. 0 social threads.
- **Verdict: VERIFY-ELSEWHERE.** The deal-level real estate capital buyer (family offices, RE-focused GPs) does not search Google PAA for capital partners. They search differently — direct outreach, LinkedIn, family-office networks, broker-dealer referrals. The PAA-empty result does **not** mean the demand doesn't exist; it means the demand sits on a different surface. Route to GTM Revenue Hunt (`wiki/processes/lead-sniperai-cli-os.md`) instead of content marketing.
- **Operational rule:** any PAA-empty result for a capital-acquisition seed → archive the content idea, escalate the demand to the GTM signal-based outbound motion. Don't keep scanning reformulations to try to manufacture organic PAA; that's the wrong surface.

### Pillar 3 tie-in to the Veritas v4 audit

The v4 audit already operationalized this rule without calling it Pillar 3: the **Reg-D-adjacent** keyword (`commercial real estate loan rates`) was retained only as a *compliance-gated educational explainer* with an explicit "Veritas is not a lender" disclaimer, because writing a direct content play there would put Veritas in front of capital-acquisition searchers (a *wrong surface* for a content page) and would also risk a Reg-D general-solicitation issue (a *compliance* problem). The PAA scans above show the same dynamic: when the search intent doesn't match the surface, the right move is to **route the demand elsewhere**, not to manufacture content.

**This is Pillar 3 in practice.** Three scans, three different strategic verdicts (write / reformulate / route to GTM), all on a single client, for $0.054. The PAA scan is the **first evidence** that decides which way each demand goes — and the cost of being wrong without it is measured in pages nobody reads.

---

## Pillar 4 — Quality over AI bulk spam

**Principle.** Mass AI-generated content is flagged by Google as spam over time. The strategy is fewer, more valuable pages — each one with a clear answer to a real question (Pillar 3), targeting commercial intent (Pillar 2), in a defensible niche (Pillar 1).

**Hermes execution (the production cap).**

| Production rate | Status | Action |
|-----------------|--------|--------|
| ≤ 10 pages / quarter / client | Allowed by default | Standard HITL row per page in `drafts/VALIDATION_QUEUE.md` |
| 11–30 pages / quarter | Requires justification | Extra row: `wiki/clients/<slug>/drafts/ai-content-bulk-justification.md` signed by Dennis |
| 30+ pages / quarter | Rejected | Reframe the goal — bulk AI production is the wrong tool |

**Per-page gate (every page, every client):**

1. Row in `drafts/VALIDATION_QUEUE.md` with:
   - Target keyword + intent class (from Pillar 2)
   - Source PAA scan ID (from Pillar 3)
   - Niche + sub-niche (from Pillar 1)
   - Estimated word count + unique data/source count
2. `content-optimization` scan before publication (`run_content_scan` → review score). If `ONPAGE_API_KEY` is missing, the skill reports **module dormant** and the page is blocked from publishing until manual review.
3. Publish, then `inspect_urls` via Search Console to confirm indexing.

**Why a hard cap.** The cap is the gate that enforces Pillar 4. Without it, "quality over volume" is a slogan. With it, every production run either fits the default or escalates a written justification. The justification file is itself an audit trail — you can see *why* 25 pages were produced in Q3 and decide next quarter if the rationale held.

**Evidence from the field — Veritas v4 audit (2026-08-28).** The v4 90-day content plan is **3 new pages, plus GBP setup, plus an optional PR pitch**. That is the entire production run for the next 90 days on a real client with a $20,500 Year-1 budget:

| Page | Target keyword | KD | Volume | Decision rule |
|------|---------------|----|----|----------------|
| `/commercial-construction-services/` | `commercial general contractors kansas city` + `commercial construction kansas city` | 12 / 26 | 110 / 110 | **All 20 organic results are agency homepages** — single well-built locally-optimized service page hits top 10 in 3-6 months |
| `/kc-home-renovations-guide/` | `kc home renovations` | 18 | 390 | **Only one real domain in top 10** (kchomesolutions.com) — informational guide, no compliance gate |
| `/commercial-real-estate-financing-guide/` | `commercial real estate loan rates` | 20 | 2,400 | **AI Overview present + Reg-D adjacent** — compliance-gated, deferred until David approves disclaimer framing |

The dropped 5th and 6th page candidates (`multifamily contractors` guide, `top construction companies in kansas city` listicle) are held for **month 4-6** as the data warrants, not pre-emptively drafted. That's the cap in action: 3 pages is enough; the rest waits for the data.

**The "no auto-spend" tie-in.** The production cap mirrors the HITL spend cap in the OpenSEO skill catalog: every action that costs money (rank tracker, site audit, PAA scan beyond a threshold) gets the same `assumptions + cost + cap + approval` treatment. The production cap is the **content-side version of the same discipline**.

---

## Pillar 5 — Structuring and authority

**Principle.** Two pages with the same content rank differently based on (a) how Google crawls their internal link graph and (b) how many reputable sites link to them. Both are measurable and both can be improved systematically.

### 5a. Internal linking + crawlable architecture (in scope today)

**Hermes execution.**

| Step | Tool | Output |
|------|------|--------|
| 1. Crawl the site | `site-audit` (`run_site_audit`) | Audit ID |
| 2. Read the issue report | `get_audit_issues` | Prioritized issues |
| 3. Identify orphan pages + thin content | `get_audit_pages` | Per-page data |
| 4. Decide the hub-spoke graph | Human decision | Internal link map |
| 5. Update pages + re-audit quarterly | `run_site_audit` | Verified improvement |

**Evidence from the field — Veritas v4 audit (2026-08-28).** The v4 audit found that **3 of 5 audit issues collapse into a single root cause**: the homepage is JS-rendered, the real content lives in a SPA shell, and Google cannot read it. The audit's Critical-tier action list is the canonical Pillar 5a template for a foundation-missing client:

1. **Server-render / pre-render the homepage.** This single fix unblocks 3 of 5 audit issues (`thin-content` → 0, `missing-h1` → adds H1, `no-outgoing-links` → can now add internal nav). ~2-4 hours of dev work.
2. **Add H1 + 300+ words** of real, keyword-rich content describing services + service area.
3. Trim title to ~55 chars + meta to ~150 chars. (15 min, zero risk.)
4. Add server-rendered internal nav with stub pages (Services / Projects / About / Contact). Even stubs beat zero.
5. Create + submit XML sitemap to GSC + Bing Webmaster Tools.
6. Add Organization + LocalBusiness schema to the homepage once it's server-rendered.
7. Set up Google Business Profile + Bing Places (30 min).
8. (Long-term) Build out service-area pages (Lee's Summit, Kansas City, Jackson County MO, etc.) for local SEO.

The **scrapling pass** on `veritasdevelopmentgroupllc.com` (2026-08-30) confirmed the audit's diagnosis at the byte level: a 200 OK response but content injected via JavaScript, noindex confirmation, and `localStorage`-driven nav. The audit's structural recommendations are not generic — they are the specific fix for **JS-rendered SPA hosting**, which is the most common Pillar 5a failure mode for React/Next/Vue sites.

The v1 audit on `example.com` (2026-08-26, ~$0.30) is a simpler case study: 2 warnings, both Pillar 5a, the 1-2-3-week template (meta → re-audit → full audit). Retained for reference, **not** the primary Pillar 5a case.

### 5b. Backlink outreach + authority (mixed: PR angle, build gap)

**The OpenSEO creator's playbook is explicit:** backlinks are won by analyzing competitor backlink profiles, finding dead/broken resources, and offering replacement content. The process is labor-intensive but heavily automatable: crawl pages, extract emails, track follow-ups.

**Current OpenSEO tool surface (verified 2026-08-28 against `127.0.0.1:3005`):**

- ✅ `get_backlinks_overview` — total backlinks, referring domains, DR/UR
- ✅ `get_backlinks_profile` — bounded page of detailed backlink rows
- ✅ `find_serp_competitors` — who competes in SERPs
- ❌ **No broken-link finder, no email extractor, no outreach tracker.**

**The gap.** The OpenSEO tool surface tells you *what* links exist. It does not yet (a) find broken resources to replace, (b) extract contact emails from those resources, or (c) track multi-step outreach. These three capabilities are the difference between "we know our backlink profile" and "we systematically earn new backlinks."

**Evidence from the field — Veritas v4 audit (2026-08-28).** The v4 audit's Pillar 5b play is **PR, not broken-link outreach**. For the `top construction companies in kansas city` keyword (KD 18, listicle SERP dominated by bizjournals + glassdoor), the recommended action is a PR pitch to the **Kansas City Business Journal** for inclusion in a "Top Construction Companies" feature. This is a Pillar 5b play in the *creator's spirit* (other reputable sites linking to Veritas) but in a *different form* than broken-link outreach — appropriate for a development-stage firm with a 22-year track record but no SEO link footprint. David must approve (Decision 2 in the cover note).

**Two options for the gap (when the broken-link outreach is needed for other clients):**

| Option | What it is | Cost | When to choose |
|--------|------------|------|----------------|
| **Manual** | Operator runs Ahrefs/Semrush broken-link report, exports CSVs, sends outreach by hand. Hermes is the ledger. | Operator time only | Client budget < $2k/mo SEO; < 5 outreach touches/month |
| **Build the module** | Add `find_broken_links`, `extract_emails`, `track_outreach` to OpenSEO. Hermes orchestrates the full loop. | 1-2 dev weeks + a third-party email-finding API | Client budget > $2k/mo SEO OR an active client engagement needs > 20 outreach touches/month |

**Recommendation for the open-seo engagement:** keep this gap **explicit and visible** in this playbook until a paying client engagement actually needs the loop. Speculative module work has its own papercut cost — see `content-growth-strategies.md` governance rule #2 ("commercial purpose before volume").

---

## Stack-walk rules (the discipline layer)

These apply to every pillar and every engagement.

1. **Always start at Layer 1 (`seo-enrichment-planner`).** No Discover/Enrich/Score/Outreach skill runs without the cost estimate + scope agreed. Same as GTM.
2. **HITL gates between pillars.** Each pillar transition (Pillar 1 → 2, 2 → 3, 3 → 4, 4 → 5) requires a written summary in the OpenSEO project context (`update_project_context`) before the next layer's spend begins.
3. **Cost plan with a range, not a point.** "5-8 cr" not "6 cr". Include a spend cap explicitly. Pattern from `seo-enrichment-planner`:
   ```
   ## Assumptions
   - <3-5 bullets>
   ## Cost Estimate
   <markdown table>
   ## Spend Cap
   - max spend: <cap>
   ## Approval Question
   Approve full run? (yes / no / adjust)
   ```
4. **Discover before Enrich.** A keyword universe that starts with `content-optimization` scans wastes money on pages for keywords you haven't qualified (Pillar 2 + 3) yet.
5. **Module dormancy is honest.** If `ONPAGE_API_KEY` is empty, `content-optimization` reports "module dormant" — the UI hides the sidebar item, the MCP tool returns `{error: "module disabled"}`. No silent failure. Same for GSC/GA4 (`analytics-reporting` partial status) and rank tracker when balances are exhausted.
6. **Verify the tool, not the doc.** This playbook references 50 OpenSEO tools. Before running an engagement, confirm via `whoami` + `tools/list` that the surface matches the catalog. We did this 2026-08-28 — the 50 tools were live, the server was `self-hosted`, scopes were `none` (GSC/GA4 gated as expected).
7. **Audit → SERP → Brief is the only path to a page.** The Veritas v4 audit is the worked example. v3 had 33 candidate keywords; v4 re-scoped to 8 winnable, then reclassified 2 of 8 by intent, then gated 1 of 8 for compliance. **The audit passes are the discipline; the content count is the output.**

---

## The 30/60/90 cadence

| Period | Focus | Pillar |
|--------|-------|--------|
| **Days 1-30** | Pick the niche. Run `domain-research` on 3-5 competitors. Lock the wedge term. | Pillar 1 |
| **Days 31-60** | Build the keyword universe. Filter to commercial intent. Run the SERP intelligence pass on the top 8-10 seeds. Decide the 3-5 winnable pages. | Pillar 2 + 3 |
| **Days 61-90** | Publish the first 3-5 pages with `content-optimization` scans. Run `site-audit`. Plan the next 3-5. | Pillar 4 + 5 |

If by Day 60 you have not produced 3-5 content briefs, **stop and re-examine Pillar 1** — the niche is probably wrong, not the velocity.

**Veritas real-world timeline (v4 plan, 2026-08-28):**
- Day 0 (now): cover note + audit + client score delivered. Awaiting David's Decision 1 (Reg-D adjacency on the financing guide) and Decision 2 (PR listicle yes/no).
- Day 1-7: foundation sprint — server-render the homepage, add H1 + 300 words, trim title + meta, add internal nav, submit sitemap, set up GBP + Bing Places. **Foundation sprint is the precondition for the content plan.**
- Day 8-30: Page A (`/commercial-construction-services/`) drafted + published; Page D (`/kc-home-renovations-guide/`) drafted + published; GBP categories + service area + reviews seeded; weekly Google Posts begin.
- Day 31-60: Page C (`/commercial-real-estate-financing-guide/`) drafted only if Decision 1 = clean; otherwise drop. Begin monthly SERP re-pulls; first rank tracker run on Tier-1 keywords.
- Day 61-90: top-5 organic target for Tier-1 keywords; citation building begins; first backlink acquisition (organic + PR); month-3 SERP re-pull.

---

## What this playbook is NOT

- **Not a list of OpenSEO features.** That's the docs and the skill catalog (`_config/seo-skill-catalog.md`).
- **Not a replacement for `seo-audit` skill** in `~/.hermes/skills/`. The audit skill is one tool; this playbook is the strategy that decides when to use it.
- **Not a per-client binding.** Per-client binding lives in `clients/<slug>/_config/seo-skills.md`. The vertical map (Local business / National SaaS / E-commerce / Investor-facing) in `open-seo/_config/seo-skills.md` lines 49-56 is the source of truth for which skills each client gets.
- **Not a commitment to bulk AI content.** Pillar 4 is explicitly anti-bulk. The 10-page/quarter default is the gate.
- **Not a finished answer to Pillar 5b.** The broken-link outreach loop is a known gap with two options (manual or build). A real client engagement should trigger the decision, not this playbook.

---

## Files

**Primary evidence (the v4 Veritas audit + its supporting docs):**
- `wiki/clients/veritas-developments/projects/website/seo-audit-veritasdevelopmentgroupllc-2026-08-28-client.md` — the RELEASED v4 audit
- `wiki/clients/veritas-developments/projects/website/CLIENT-SCORE-veritas-developments-2026-08-28.md` — the RELEASED client score (32/100, CONDITIONAL → PROCEED after foundation sprint)
- `wiki/clients/veritas-developments/projects/website/COVER-NOTE-seo-audit-v4-2026-08-28.md` — the cover note with the 2 decisions for David + Daniel
- `wiki/clients/veritas-developments/drafts/website/serp-intelligence-2026-08-28.md` — 160 organic results + 50 competitor rows (Pillar 1 + 2 + 5a source)
- `wiki/clients/veritas-developments/drafts/website/scrapling-findings-2026-08-30.md` — byte-level confirmation of the JS-render diagnosis (Pillar 5a evidence)
- `wiki/clients/veritas-developments/drafts/website/seo-audit-veritasdevelopmentgroupllc-2026-08-28.md` — the draft predecessor of v4

**Pillar 3 case-study drafts (4 PAA scans, Veritas-shaped, $0.072):**
- `wiki/clients/open-seo/drafts/seo/paa-2026-08-28-multifamily-development-process.md` — verdict: WRITE
- `wiki/clients/open-seo/drafts/seo/paa-2026-08-28-multifamily-co-sponsor.md` — verdict: REFORMULATE
- `wiki/clients/open-seo/drafts/seo/paa-2026-08-26-best-seo-tools.md` — earlier 4-PAA example, retained
- `wiki/clients/open-seo/drafts/seo/audit-2026-08-26-example-com.md` — earlier 1-page pilot, retained for reference but **not** the primary Pillar 5a case (Veritas audit is)

**Process-layer cross-references:**
- This doc: `wiki/processes/seo-organic-growth-playbook.md`
- Onboarding sprint (the 70-minute first-touch): `wiki/processes/seo-client-onboarding-sprint.md`
- 1:many demand-generation parent: `wiki/processes/content-growth-strategies.md`
- GTM signal-based outbound (Pillar 3 verify-elsewhere routing): `wiki/processes/lead-sniperai-cli-os.md`
- AI search (AEO/GEO) layer: `~/.hermes/skills/ai-seo/SKILL.md`
- OpenSEO skill catalog: `wiki/clients/open-seo/_config/seo-skill-catalog.md`
- OpenSEO per-client binding: `wiki/clients/open-seo/_config/seo-skills.md`
- OpenSEO pointer for this playbook: `wiki/clients/open-seo/drafts/seo/playbook-pointer.md`

---

## Governance

1. **Evidence before content.** No PAA scan, no Pillar 3 brief. No SERP re-pull, no Pillar 2 page. The Veritas v4 audit is the worked example of audit-before-content.
2. **Commercial purpose before volume.** The 10-page/quarter cap is the gate. The Veritas v4 plan produced 3 pages, not 30.
3. **One core question, one piece of content.** Maximize answer density per page; do not let PAA scans produce 4 different articles when 1 is what readers need.
4. **HITL for sensitive material.** Reputation, financial, legal claims (real estate disclosures, accredited-investor verification, joint-venture structuring, Reg-D-adjacent capital content) require David + Daniel's explicit review. Default to the existing per-client `_config/voice.md` and `_config/compliance.md` (Veritas's compliance file is the Reg D 506(b/c) screening rule).
5. **Measure downstream outcomes.** Engagement is useful; pipeline and revenue determine success. The Veritas client score ($20,500 Year-1 spend → $358K midpoint recoverable traffic value) is the framing.
6. **Store learning.** Winning patterns (e.g. "PAA scan for `best X` returns 4+ questions → write 1 page" or "JS-render root cause → server-render first, then audit re-runs") become institutional knowledge. Update this playbook when a new pattern is verified twice.

---

*Drafted 2026-08-28 from the OpenSEO creator's playbook + the 50-tool OpenSEO MCP surface + the released v4 Veritas audit (the primary spine) + 4 supporting PAA scans (Pillar 3) + the scrapling byte-level confirmation (Pillar 5a). Pending Dennis's review and promotion from `drafts/` to `projects/`.*
