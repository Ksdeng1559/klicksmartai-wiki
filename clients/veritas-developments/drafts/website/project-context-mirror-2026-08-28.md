---
type: Website
title: project-context-mirror-2026-08-28.md
description: OKF v0.2 frontmatter; type/status visible to any LLM that reads the bundle.
status: draft
generated: { by: human:dennis, at: 2026-08-29T18:00:00Z }
verified: []
okf_version: "0.2"
---
# Project Context Mirror — veritasdevelopmentgroupllc.com

> **Status:** ✅ COMMITTED — `update_project_context` call executed at `2026-08-28 16:32:44 UTC`, response confirmed 4 patch ops applied
> **OpenSEO project_id:** `b5ac472f-9f18-49f8-af6d-606bd8bb00ae`
> **OpenSEO mirror URL:** http://127.0.0.1:3005/p/b5ac472f-9f18-49f8-af6d-606bd8bb00ae/settings/context
> **MCP tool:** `get_project_context` / `update_project_context` at `POST /mcp` on :3005
> **Author policy:** the wiki is the source of truth; this file is the durable mirror
> **Last verified (current OpenSEO state):** 2026-08-28 16:32 UTC — 4 sections + 2 key_pages + 2 research_log entries written by `mcp`

This file mirrors OpenSEO's `project_context` so the wiki stays authoritative even
when OpenSEO is offline or before agents have the MCP server in context. **Read
this first.** The OpenSEO copy is the AI-tool-facing one; this file is the
review/edit surface.

---

## Current OpenSEO state (after 2026-08-28 16:32 UTC update)

| Section | Filled | Author | Verdict vs. source |
|---|---|---|---|
| `business_overview` | ✅ | mcp (updated 16:32) | ✅ **now correct** — four divisions + Daniel KW carve-out |
| `current_goal` | ✅ | mcp (05:12, unchanged) | ✅ matches scrapling-findings-2026-08-30 |
| `positioning` | ✅ | mcp (05:12, unchanged) | ✅ matches site voice |
| `writing_preferences` | ✅ | mcp (05:12, unchanged) | ✅ matches site voice + compliance footer |
| `competitors` | � empty | — | ⚠️ still deferred — pending Dennis review of 5 KC firms from serp-competitor-landscape-2026-08-30 |
| `key_pages` | ✅ 2 entries | mcp (16:32) | ✅ hub + money roles assigned |
| `research_log` | ✅ 2 entries | mcp (16:32) | ✅ site audit + scrapling render captured |
| `customSections` | ❌ empty | — | ℹ️ none needed yet |

**No missing sections flagged by OpenSEO** (`"Missing sections: none"`).

---

## Accuracy audit (what's wrong + why)

### Issue 1 — business_overview says "Two divisions" but the site says FOUR  (CRITICAL)

**Current (wrong):**
> "Two divisions of scope: (1) Development & Construction — residential, commercial, multifamily and mixed-use, with in-house trades … and (2) Capital Advisory — construction/acquisition/bridge financing …"

**Correct per scrape-veritasdevelopmentgroupllc-home-2026-08-30.md (lines 177–239):**
> "Four divisions. One standard. 01 — Development. 02 — Construction. 03 — Site Development. 04 — Capital Advisory."

The `positioning` section already correctly says "four divisions working as one" — so the context is internally inconsistent. Fix business_overview to enumerate all four.

### Issue 2 — Daniel Bailey's Keller Williams carve-out is missing  (CRITICAL — Reg D adjacency)

**What's missing:** Daniel Bailey is Co-Founder & Real Estate Advisor with Veritas,
but **actively practices real estate with Keller Williams; his brokerage activities
are performed through Keller Williams, separate from his development and advisory
work with Veritas Development Group** (scrape-veritasdevelopmentgroupllc-home-2026-08-30.md line 161; mirrored in financing page footer line 113).

**Why this matters:** the Capital Advisory division offers "construction/acquisition/bridge financing and development capital" — adjacent to broker-dealer / Reg D territory. Any downstream AI content that attributes Daniel's brokerage work to Veritas, or implies Veritas is a lender, risks a misclassification. The Keller Williams carve-out must be in business_overview so every agent reading this context knows Daniel's dual-role structure.

**Recommended language** (append to business_overview): "Daniel Bailey is Co-Founder & Real Estate Advisor; his brokerage activities are performed through Keller Williams, separate from his development and advisory work with Veritas. Veritas arranges capital through third-party lenders — it is not a direct lender, broker-dealer, or investment adviser."

### Issue 3 — competitors / key_pages empty  (MINOR)

`competitors=[]` and `key_pages=[]` are technically OK (OpenSEO calls them out as
"curated shortlists, 100 max each"), but seeding them with the actual crawlable
inventory gives every downstream agent a starting point:

- **key_pages** (seed from scrape-2026-08-30): `https://veritasdevelopmentgroupllc.com/` (home), `https://veritasdevelopmentgroupllc.com/financing` (only 2 pages where HTTP-only crawl + scrapling render both return real content)
- **competitors** (seed from serp-competitor-landscape-2026-08-30.md): the 5 KC commercial-construction + development firms profiled in that doc — names TBD pending Dennis review

### Issue 4 — business_overview missing phone / email / funding email  (MINOR)

scrape-veritasdevelopmentgroupllc-home-2026-08-30.md (lines 345, 377) carries:
- `816-405-6181`
- `info@veritasdevelopmentgroupllc.com`
- `funding@veritasdevelopmentgroupllc.com`

Not strictly needed in business_overview (it's positioning, not a contact sheet),
but the funding email is the one that matters for lead-routing in any AI agent.

---

## Committed payload (sent 2026-08-28 16:32 UTC, response confirmed)

The `update_project_context` MCP call was executed via `POST http://127.0.0.1:3005/mcp` with 4 patch ops. Response: `"Updated project context (4 change(s))."` — every section, key_page, and research_log entry echoed back with new `updatedAt` timestamp matching the call.

### Final `updates[]` (as sent — op names conformed to `src/types/schemas/projectContext.ts`)

- `[{section: "business_overview", content: <1,587 chars>}]` — corrected copy (four divisions + Daniel KW carve-out)
- `[{addKeyPages: [{url: "https://veritasdevelopmentgroupllc.com", role: "hub", topic: ..., notes: ...}, {url: ".../financing", role: "money", topic: ..., notes: ...}]}]`
- `[{appendResearchLog: {summary: "..."}}]` × 2 — site audit + scrapling render

**Schema correction note:** my draft payload used `append_key_page` / `append_research_log` / `upsert_section` — the actual schema is `{section, content}` for sections, `{addKeyPages: [...]}` for key pages, and `{appendResearchLog: {summary}}` for research log. The `keyPage` shape has no `label` field — `topic` and `notes` cover it. The research log entry has no `researchType`/`source`/`costCredits` — those are encoded in the `summary` string.

### IDs returned by the server

| Entity | ID | Updated |
|---|---|---|
| business_overview | (inline section) | `2026-08-28T16:32:44.371Z` |
| key_page: `/` | `6e564c2c-d233-4ae4-8a11-8fa03dc838a2` | `2026-08-28T16:32:44.374Z` |
| key_page: `/financing` | `6e73372c-af36-43a9-9d47-69b4a4d6d9eb` | `2026-08-28T16:32:44.374Z` |
| research_log: scrapling | `c8d81e26-a424-41f0-ae0e-a13f93553c9b` | entry date `2026-08-28` |
| research_log: site audit | `6cfbadda-7515-4a20-bb74-1d8b6c85bbb8` | entry date `2026-08-28` |

(Keep these IDs — `removeResearchLog` and `removeKeyPages` take IDs, not URLs.)

`current_goal`, `positioning`, and `writing_preferences` were **NOT touched** in the update — they're already accurate, and re-writing them would have reset their `updatedAt` timestamps for no reason.

`competitors` is still deferred — pending Dennis review of the 5 KC competitors from `serp-competitor-landscape-2026-08-30.md`.

---

## Source links

- OpenSEO settings page: http://127.0.0.1:3005/p/b5ac472f-9f18-49f8-af6d-606bd8bb00ae/settings/context
- MCP tool definition: `/home/denni/repos/open-seo/src/server/mcp/tools/project-context.ts`
- MCP route: `POST /mcp` on `127.0.0.1:3005` (Streamable HTTP / JSON-RPC 2.0)
- v3 client audit: `drafts/website/seo-audit-veritasdevelopmentgroupllc-2026-08-28-client.md`
- v3 internal audit: `drafts/website/seo-audit-veritasdevelopmentgroupllc-2026-08-28.md`
- Scrapling findings: `drafts/website/scrapling-findings-2026-08-30.md`
- Home scrape: `drafts/website/scrape-veritasdevelopmentgroupllc-home-2026-08-30.md`
- Financing scrape: `drafts/website/scrape-veritasdevelopmentgroupllc-financing-2026-08-30.md`
- SERP landscape: `drafts/website/serp-competitor-landscape-2026-08-30.md`
