---
type: Project
title: "Veritas Development OS — Frappe CRM + Astro Landing Pages"
description: OKF v0.2 frontmatter — staged in drafts/ per VALIDATION_QUEUE gate (promoted to projects/ only after Dennis + David Poole sign-off).
status: planning
generated: { by: ai:hermes, at: 2026-08-29T21:05:00Z, model: minimax-m3, session: 20260829_131616_d94526 }
verified: []
okf_version: "0.2"
client: Veritas Development Group LLC
principal_contact: David Poole
co_founder: Daniel Bailey
owner: Dennis (KlickSmartAI)
---

# Veritas Development OS — Build & Deploy Job

**Purpose:** Build an Astro-based lead-generation landing page suite (v2) that posts leads into Frappe CRM (deployed on Railway), and ship everything as a verified, working stack.

**Engagement context:** This is an internal KlickSmartAI build that delivers on the **CRM build** clause of the signed Veritas Development Group LLC engagement (2026-08-11). When David signs off, this is promoted from `drafts/` → `projects/`.

---

## Status

| Phase | Owner | State |
|---|---|---|
| 0 — Prerequisites | Dennis + David | � Blocked: Frappe CRM not yet deployed; Lovable v1 repo URL not yet shared |
| 1 — Clone Lovable v1 → Astro v2 | Claude Code | ⏳ Pending; user will run Claude Code session first |
| 2 — Deploy Astro v2 to Vercel | Hermes (vercel MCP) | ⏳ Pending; triggered once GitHub URL is shared |
| 3 — Frappe integration (lead POST) | Hermes | ⏳ Blocked on Phase 0 (Frappe URL + API key/secret) |
| 4 — Custom domain (optional) | Dennis | ⏳ TBD |

---

## Architecture (locked)

```
┌─────────────────────┐  POST  ┌──────────────────┐  proxy  ┌─────────────────┐
│  Astro Static Site │───────>│  Vercel Edge     │───────>│  Frappe CRM     │
│  (Vercel-hosted)    │        │  /api/leads      │        │  /api/resource/ │
│                     │        │  (serverless)    │        │   Lead          │
│  - landing.astro    │        │                  │        │  (Railway)      │
│  - LeadForm.astro   │        │  validates,      │        │                 │
│  - api/leads.ts     │        │  forwards w/     │        │  Lead → CRM     │
│                     │        │  Frappe API key  │        │  pipeline       │
└─────────────────────┘        └──────────────────┘        └─────────────────�
```

- **Astro static** for the marketing surface (fast, SEO-friendly, cheap).
- **Vercel serverless function** at `/api/leads` — hides Frappe API key from the browser.
- **Frappe CRM** owns the data; integrates with everything else.

---

## Phase 0 — Prerequisites (BLOCKING)

| Need | Owner | Status |
|---|---|---|
| Frappe CRM deployed + accessible URL | Dennis | ⏳ Later |
| Frappe API key + secret for integration user | Dennis | ⏳ After Frappe is up |
| GitHub repo URL with Lovable v1 source | Dennis | ⏳ After Claude Code finishes |
| Vercel MCP auth | Hermes | ✅ Token at `/home/denni/.hermes/mcp-tokens/vercel.json` (verified in earlier session) |
| Railway MCP auth | Hermes | ✅ Token at `~/.hermes/.env` as `RAILWAY_API_TOKEN` (verified in this session) |
| Vercel account linked to GitHub | Dennis | Likely already; will confirm during Phase 2 |

---

## Phase 1 — Clone Lovable v1 → Astro v2 (Claude Code)

**Worktree:** `vercel-v2/astro-conversion`
**Where:** Dennis runs Claude Code locally.

### Steps for Claude Code

1. `git clone <lovable-repo-url> veritas-landing-v2`
2. `cd veritas-landing-v2`
3. Inspect `package.json` — Lovable uses Vite + shadcn by default:
   - Strip Lovable-specific build chain (remove `vite.config.ts`, `tailwind.config.*` if only used internally)
   - Keep all `src/components/*` — Astro imports React components via `@astrojs/react`
4. Scaffold Astro alongside the existing app:
   ```
   npm create astro@latest -- --template minimal --typescript strict --install
   ```
5. Migrate page structure:
   - `src/pages/index.astro` ← original `src/App.tsx` rendered to static HTML
   - Components stay as `.tsx` (React) under `src/components/`, imported with `client:load` directive for interactivity
6. Add lead form: `src/components/LeadForm.tsx` + `src/pages/api/leads.ts`
7. Style: port Tailwind classes 1:1 (Astro supports Tailwind natively via `@astrojs/tailwind`)
8. Build: `npm run build` → confirm `dist/` is generated
9. Push to new branch: `git push origin vercel-v2/astro-conversion`

**Deliverable from this phase:** GitHub repo URL + branch name. Dennis pastes both back to Hermes.

---

## Phase 2 — Deploy to Vercel (Hermes via vercel MCP)

Triggered once Dennis hands me the GitHub URL.

1. `mcp__vercel__whoami` — confirm Vercel auth
2. `mcp__vercel__list_projects` — check no name collision
3. `mcp__vercel__create_git_project` with repo + branch
4. Wire placeholder env vars:
   - `FRAPPE_API_URL`
   - `FRAPPE_API_KEY`
   - `FRAPPE_API_SECRET`
5. Trigger first deploy
6. Confirm preview URL renders

**Deliverable:** `https://veritas-landing-v2.vercel.app` (or auto-generated name) is live.

---

## Phase 3 — Frappe Integration (after Frappe is up)

1. Dennis creates a Frappe API user (or uses Administrator) → generates API key + secret
2. Dennis pastes URL + key + secret back to Hermes
3. Hermes updates Vercel env vars via `mcp__vercel__update_project` (or `mcp__vercel__add_env`)
4. Smoke test: submit form → confirm new Lead doctype in Frappe
5. Confirm Lead appears in CRM pipeline

---

## Phase 4 — Custom Domain (optional)

If Dennis provides a domain:
1. `mcp__vercel__buy_domain` OR add DNS records at the registrar (depending on ownership)
2. Verify + issue TLS

---

## Risks / Gotchas

| Risk | Mitigation |
|---|---|
| Lovable uses Supabase auth — won't port cleanly | Strip auth in v2 (landing page = no login); Supabase stays internal to Lovable v1 |
| Lovable React components have client-only state that breaks Astro SSR | Wrap interactive bits in `<Component client:load />` directive; static parts render at build time |
| Frappe `/api/resource/Lead` expects specific JSON shape | Match the Lead doctype schema (`{ "lead_name", "email_id", "company_name", ... }`); confirm against live Frappe instance |
| Astro serverless functions on Vercel have 10s default timeout | Lead POST is a single Frappe call, ~200ms typically. Fine. |
| Conflating "Veritas Development OS" (this project) with "Veritas Development Group LLC" (David's real-estate firm) in the wiki | This file lives under `clients/veritas-developments/drafts/` — parent IS the client; this project IS a deliverable for that client. Clear once promoted. |
| Validation gate skipped if promoted directly | Per OKF rules, must remain in `drafts/` until Dennis + David Poole approve |

---

## Handoff Notes

- **Railway:** ERPNext template at `railway.com/deploy/erpnext` deploys 5 services (ERPNext + MariaDB + 2× Redis). Manual `railway-setup.sh` must run inside the ERPNext container post-deploy. HTTP port must be set to 80 manually.
- **Vercel:** Astro + `@astrojs/react` + `@astrojs/tailwind` is the locked stack. No Next.js unless David asks for SSR.
- **Frappe:** v14+ on Frappe Framework. Lead doctype is built-in — no custom schema work needed.

---

## Promotion Checklist (drafts/ → projects/)

- [ ] Dennis reviews this JOB.md
- [ ] David Poole reviews this JOB.md (or summary)
- [ ] Daniel Bailey looped in if relationship-impacting (he's co-founder/RE advisor)
- [ ] Phase 0 prerequisites cleared (Frappe up, Lovable repo URL shared)
- [ ] Phase 1 completed by Claude Code
- [ ] Phase 2 deployed to Vercel (Hermes)
- [ ] Phase 3 lead POST verified end-to-end
- [ ] File moved: `mv drafts/veritas-development-os/ projects/veritas-development-os/`
- [ ] Entry added to `drafts/VALIDATION_QUEUE.md` with sign-off timestamps

---

**Next action:** Dennis to share the GitHub URL of the Lovable v1 project (or run Claude Code first per plan) and the Frappe deployment URL when ready. Hermes triggers Phase 2 + Phase 3.
