# Veritas — Consolidated Decision Matrix for David + Daniel

> **Purpose:** Eight draft items are queued in `drafts/VALIDATION_QUEUE.md`. Each is blocked on a David + Daniel answer. Sending one-at-a-time would force them to context-switch across 8 unrelated questions. **This doc bundles them into one decision matrix with [RECOMMENDED] answers, so David + Daniel can answer in one sitting.**
>
> **Status:** DRAFT — drafted by Hermes on 2026-08-28; awaiting Dennis signoff. **Do not send to David or Daniel until Dennis reviews.**
>
> **Approvers required:** Dennis (KlickSmartAI) reviews first → David Poole (substance) + Daniel Bailey (relationship) review next → answers committed in this file → actions queued to `projects/`.

---

## How to use this doc

1. David and Daniel scroll through the 8 rows.
2. For each row, they choose **A / B / C / D / OTHER** in the "Answer" column.
3. If a row needs a free-text answer, drop it in the "Notes" column.
4. Once all 8 are answered, this doc moves to `projects/` (per the two-approver HITL rule in `IDENTITY.md`), and the corresponding actions get queued.

Estimated time-to-complete: **15–25 minutes** if David and Daniel answer in the same sitting.

---

## Row 1 — TAM CSV (54 organizations, 3 tiers)

**Draft:** `drafts/growth-program/tam-csv-2026-08-12.csv` (54 orgs across 3 tiers — Tier 1 = top-priority, Tier 2 = warm, Tier 3 = cold)

**Question:** The Tier 3 list has some lower-fit orgs. Sosland/Crane/Ingram are not in the list but should be.

**Recommendation:** **B — Keep Tier 1+2 as drafted, delete the 11 lowest-fit Tier 3 orgs, add Sosland + Crane + Ingram to Tier 2.**

**Cost of inaction:** TAM CSV stays in `drafts/`, can't be used for outbound, blocks the growth-program pilot plan.

| Answer | Notes |
|---|---|
| A / B / C / D / OTHER | |

---

## Row 2 — KC family-office law firm channel

**Draft:** `drafts/growth-program/kc-family-office-law-firms-2026-08-12.md` — 5 firms profiled (Polsinelli, Lathrop GPM, Spencer Fane, Stinson, Shook Hardy & Bacon)

**Question:** Which of these 5 firms does David or Daniel actually know personally?

**Recommendation:** **A — Focus the warm-intro outreach on whichever 2 firms David and Daniel have a real relationship at; deprioritize the rest to Tier 3.**

**Cost of inaction:** Without warm-intro targeting, the channel becomes cold outbound, lower conversion, lower priority than TAM.

| Answer | Notes |
|---|---|
| A / B / C / D / OTHER | |

---

## Row 3 — Daniel Bailey team profile

**Draft:** `drafts/team/daniel-bailey-profile-2026-08-20.md`

**Question:** Confirm Daniel = family-office outreach lead. Which 12 verified family-foundation-organization (FFO) program officers does Daniel already know?

**Recommendation:** **A — Confirm Daniel as FFO outreach lead; have him list the 12 program officers from memory before any AI-generated names go in.**

**Cost of inaction:** If we generate names, we'll fabricate relationships. The two-approver HITL rule explicitly bans that.

| Answer | Notes |
|---|---|
| A / B / C / D / OTHER | |

---

## Row 4 — 7-touch outreach playbook

**Draft:** `drafts/growth-program/7-touch-playbook-2026-08-22.md` — T1 call, T2 email, T3 in-person dinner, T4 IRR follow-up, T5–T7 nurture

**Question:** Confirm the T1 calls happen before T2 emails (not after), the T3 dinner is at Jasper's, and the T4 IRR follow-up assumes 18% target.

**Recommendation:** **A — Confirm all three assumptions; Jasper's is good for T3 (consistent with brand positioning).**

**Cost of inaction:** Without confirmation, the playbook can't be loaded into LeadSniper as the default sequence.

| Answer | Notes |
|---|---|
| A / B / C / D / OTHER | |

---

## Row 5 — LeadSniper search-strategy alignment (2026-08-23)

**Draft:** `drafts/gtm/leadsniper-search-strategy-2026-08-23.md` — Tier 1/2/3 operator universe

**Question:** Confirm the Tier 1/2/3 universe definitions. Today's 5 RE-operator leads in the queue — keep them or archive?

**Recommendation:** **B — Archive today's 5 leads (they predate the tiered universe); regenerate Tier 1 from the confirmed TAM CSV (Row 1).**

**Cost of inaction:** Outbound goes out against the wrong ICP; LeadSniper credits get burned on low-fit leads.

| Answer | Notes |
|---|---|
| A / B / C / D / OTHER | |

---

## Row 6 — SEO audit v3 (2026-08-30 update)

**Draft:** `drafts/website/seo-audit-veritasdevelopmentgroupllc-2026-08-28-client.md` (v3, client-facing) + `drafts/website/scrapling-findings-2026-08-30.md` (v3.1, hosting-misconfig finding)

**Question:** The v3 audit asked "server-render / pre-render / park?" The 2026-08-30 scrape adds a 4th option: **fix hosting config only (1-2 hours)**. Which path?

**Recommendation:** **D — Fix hosting config first (1-2 hrs); re-run the audit. If Google still can't index after the fix, escalate to server-render / pre-render. Park only if the dev cost is rejected.**

**Cost of inaction:** Site stays invisible to Google. SEO priority sits behind the investor flywheel; the 1-2 hr fix is small enough to do now without derailing the flywheel.

| Answer | Notes |
|---|---|
| A / B / C / D / OTHER | |

---

## Row 7 — veritasdevelopment-wiki cleanup (5 stale files)

**Draft:** `drafts/_archive/veritasdevelopment-wiki-stale-files-2026-08-25.md` — 5 files in the client-visible repo haven't been updated since 2024

**Question:** What to do with the 5 stale files?

**Recommendation:** **B — Rename (don't delete) the 5 files to `_archive/` prefix; add a redirect README pointing to the live versions in the new `projects/` folder.**

**Cost of inaction:** Stale files stay live in the client-visible repo; David or a reviewer could mistake them for current state.

| Answer | Notes |
|---|---|
| A / B / C / D / OTHER | |

---

## Row 8 — Build-script footer leak (KlickSmartAI branding)

**Draft:** `drafts/_internal/footer-leak-2026-08-25.md` — 6 client pages in `drafts-preview/` show "Built by KlickSmartAI · 2026-08-22" in the footer

**Question:** Strip the footer branding from the 6 client pages, or leave it as portfolio attribution?

**Recommendation:** **Dennis-only decision** (does not require David or Daniel). Default: **A — Strip the footer globally from `drafts-preview/` HTML; add `<!-- KlickSmartAI branding -->` comment for internal traceability only.**

**Cost of inaction:** Client-visible HTML previews ship with KlickSmartAI branding → reads like KlickSmartAI is the developer of record.

| Answer | Notes |
|---|---|
| A / B / C / D / OTHER | |

---

## After all 8 are answered

Once David + Daniel respond, this doc:

1. **Moves from `drafts/outreach/` → `projects/`** (per HITL gate in `IDENTITY.md`).
2. **Generates a per-row action queue** that feeds the LeadSniper search strategy (Row 5), the TAM-driven outreach playbook (Row 1 + 4), the team profile (Row 3), and the SEO fix (Row 6).
3. **Updates `drafts/VALIDATION_QUEUE.md`** — closes rows 1–7, marks Row 8 (internal) as Dennis-only.

Estimated total downstream work after signoff: **8–12 hours across the team, spread over 2 weeks** (TAM list cleanup, LeadSniper regeneration, hosting fix, footer strip, outreach playbook activation).

---

## What this doc is NOT

- Not an email. No auto-send. **Drafted to Dennis first per IDENTITY.md Rule 6.**
- Not a commitment. Answers in the table are advisory until Dennis approves the send.
- Not a replacement for the individual drafts in `drafts/VALIDATION_QUEUE.md`. Those drafts stay where they are; this matrix just consolidates the questions.

---

## Source links

- `drafts/VALIDATION_QUEUE.md` (the 8 queued items consolidated here)
- `drafts/website/project-context-mirror-2026-08-28.md` (companion doc — OpenSEO project_context accuracy audit + 4-section proposal)
- `drafts/website/seo-audit-veritasdevelopmentgroupllc-2026-08-28-client.md` (v3 client-facing audit, referenced in Row 6)
- `drafts/website/scrapling-findings-2026-08-30.md` (Row 6 evidence)
- `IDENTITY.md` Rules 1–6 (source-of-truth gate + two-approver HITL + no-auto-send)
