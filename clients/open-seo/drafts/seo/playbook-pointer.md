# Pointer — SEO Organic Growth Playbook

> **Why this pointer exists.** The canonical playbook lives in
> `wiki/processes/seo-organic-growth-playbook.md` (cross-client operating
> doctrine). The open-seo client workspace contains the *evidence* the
> playbook is built on, plus the per-client binding that governs how the
> playbook runs against this specific OpenSEO instance. This pointer
> describes the relationship.

## The relationship

- **Process doc (canonical):** `wiki/processes/seo-organic-growth-playbook.md` — 5 pillars + per-pillar Hermes execution + 30/60/90 cadence + stack-walk rules. Cross-client; no per-client binding.
- **Per-client binding (this client):** `wiki/clients/open-seo/_config/seo-skills.md` — which of the 50 OpenSEO tools this client gets. The vertical map (Local business / National SaaS / E-commerce / Investor-facing) lives there.
- **Per-client evidence (this client's working artifacts):** the drafts in `drafts/seo/` and `drafts/website/` — these are the **scans, audits, and SERP passes that the playbook cites as worked examples**.

The playbook is the strategy; this client's evidence is what proves the strategy works. When the playbook says "Pillar 1 — niche positioning" and cites the Veritas v4 audit, the open-seo workspace holds the PAA scans that test the demand-discovery layer; the Veritas workspace holds the audit + SERP passes that prove the broader execution. **Both layers are required.**

## Cross-workspace evidence map

| Pillar | Playbook section | Primary evidence (this client) | Primary evidence (Veritas — the worked example) |
|--------|------------------|-------------------------------|--------------------------------------------------|
| Pillar 1 (Niche) | "Niche positioning" | `paa-2026-08-26-best-seo-tools.md` (4 PAA, 2 intent clusters) — niche-vs-broad test | `veritas-developments/projects/website/seo-audit-veritasdevelopmentgroupllc-2026-08-28-client.md` — v3→v4 cut from 33 → 8 winnable keywords |
| Pillar 2 (High-intent) | "High-intent over vanity" | — | `veritas-developments/drafts/website/serp-intelligence-2026-08-28.md` — 2 of 8 keywords reclassified by intent after SERP re-pull |
| Pillar 3 (Real demand) | "Pillar 3 case study" | `paa-2026-08-28-multifamily-development-process.md` (WRITE), `paa-2026-08-28-multifamily-co-sponsor.md` (REFORMULATE), `paa-2026-08-26-best-seo-tools.md` (4 PAA) | `veritas-developments/drafts/website/serp-intelligence-2026-08-28.md` — Reg-D-adjacent term routed to compliance gate, not content |
| Pillar 4 (Quality over bulk) | "Veritas 90-day plan" | — | `veritas-developments/projects/website/seo-audit-veritasdevelopmentgroupllc-2026-08-28-client.md` lines 178-205 — **3 pages** for the entire 90-day plan |
| Pillar 5a (Internal linking) | "Internal linking + crawlable architecture" | `audit-2026-08-26-example-com.md` (1-page pilot, retained for reference) | `veritas-developments/drafts/website/scrapling-findings-2026-08-30.md` + `seo-audit-veritasdevelopmentgroupllc-2026-08-28.md` — JS-render diagnosis + Critical-tier fix order |
| Pillar 5b (Backlinks) | "Backlink outreach + authority" | — | `veritas-developments/projects/website/seo-audit-veritasdevelopmentgroupllc-2026-08-28-client.md` — PR pitch to KC Business Journal for the listicle keyword (the creator's spirit, a different form) |

## Why the Veritas v4 audit anchors the playbook

The v4 audit (RELEASED, `veritas-developments/projects/website/`) is the only end-to-end completed run of all 5 pillars on a real client, with live OpenSEO data, a published client score (32/100 CONDITIONAL, 1,647% Year-1 ROI at the $75/click midpoint), and a David-validated next-steps list. It is the **worked example** that proves each pillar's principle in a single document. When the playbook says "Pillar X works because…", the citation is the v4 audit page that demonstrates the principle, not a generic principle statement.

## What the open-seo drafts *do* contribute

The PAA scans in this workspace test the **demand-discovery layer** (Pillar 3) — the part of the pipeline that the v4 audit only touches via the SERP intelligence reclassification. The PAA scans show what happens *before* a SERP re-pull: the demand for a given seed is either real, reformulable, or on a different surface. The v4 audit shows the *next layer* down: once you have a keyword, what does the live SERP say about format winners, intent class, and gaps. Both are needed.

## Files in `open-seo/drafts/seo/`

| File | Relationship to the canonical playbook |
|---|---|
| `audit-2026-08-26-example-com.md` | Earlier 1-page pilot (Pillar 5a reference) — **superseded by the Veritas audit as the primary case** |
| `paa-2026-08-28-multifamily-development-process.md` | **Pillar 3 case study A** — Veritas seed with real demand → write |
| `paa-2026-08-28-multifamily-co-sponsor.md` | **Pillar 3 case study B** — Veritas seed with overloaded term → reformulate |
| `paa-2026-08-26-best-seo-tools.md` | Earlier Pillar 3 example (4 PAA, 2 intent clusters, 9 social threads) — retained for reference |
| The 0/0/0 PAA scans for `kansas city real estate developer` + `multifamily development capital partner` | **Pillar 3 case study C** — capital-acquisition seeds → route to GTM, not content |
| `paa-2026-08-26-credit-unions-vs-cdfi.md` | Historical PAA scan (0/0/0) — **not cited in the current playbook**; retained as data layer evidence only |

The drafts above are the empirical evidence the playbook is built on. They are not deliverables on their own; they are the worked examples the playbook references. Promote them with the same validation queue the audit uses if you want them client-facing.

*Last updated: 2026-08-28 — playbook rewritten to anchor on the Veritas v4 audit.*
