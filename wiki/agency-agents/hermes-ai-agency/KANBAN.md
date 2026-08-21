# Hermes AI Agency — KANBAN

Active work. Format: `[ ]` todo · `[~]` in progress · `[x]` done · `[!]` blocked.

## In Progress

- `[~]` GMB URL canonicalization — 14/27 audits in place_id format. 13 still in older formats (8 CID, 4 search, 1 NULL). DataForSEO lookups needed for the remaining 13.
- `[~]` Apply opportunity scoring formula (D-2026-06-30-13) to the existing 27 audits and confirm pass threshold (70/100) is right — current top score is 53.5 (Roadhouse Projects parked), top outdated is 4.0. May need to add parked-domain override.
- `[~]` Build the Opportunity Report generator (Strengths/Problems/Estimated Lost Revenue/Score format) — design done, not yet implemented.

## Backlog (in priority order)

- `[ ]` Complete the remaining 13 GMB URL lookups (8 CID + 4 search format) via DataForSEO with city filter for better matching
- `[ ]` Add parked-domain detection (check final URL after redirect, not page title) — current code missed Hasler + Roadhouse park redirects during POC
- `[ ]` Lower pass threshold or add parked-domain override so Hasler/Roadhouse qualify (they scored 47.6 and 53.5, both below 70)
- `[ ]` Run ScrapeGraphAI on 3-5 top prospects (Hasler, Roadhouse, Best Builders) with smaller prompt + shorter timeout to get business-meaning extraction
- `[ ]` Define 2-3 verticals (Dentistry, Home Builder, Roofing) with full Claude prompts and audit templates
- `[ ]` Build the reusable `audit_gmb_prospects.py` script at `C:\Users\denni\AI-Applications\LeadSniper-3.0\scripts\` that wraps Scrapling + ScrapeGraphAI + Supabase
- `[ ]` Schedule weekly cron: Mon 09:00 — discovery + audit + persist pipeline (LS-3.0 backend on bare metal, not Docker)
- `[ ]` Build weekly digest report (tier breakdown, cost, new prospects, etc.)
- `[ ]` Continuous monitoring: nightly scan for new reviews / website changes / AI Search Score changes
- `[ ]` WebMorphasis handoff (deferred per CEO) — A/B-tier prospects waiting in Supabase
- `[ ]` Vercel backend (deferred) — current `https://lead-sniper-3-0.vercel.app/` is a stub
- `[ ]` Docker daemon (blocked on CEO starting Docker Desktop manually)
- `[ ]` Decide on first outreach copy template (CEO approval required)
- `[ ]` Decide on CRM choice (D-PENDING-03) — GoHighLevel vs HubSpot vs none-for-now
- `[ ]` Decide on outreach stack (D-PENDING-04) — Resend vs SmartLead vs Coldly

## Blocked

- `[!]` Wire `GEMINI_API_KEY` into LeadSniper-3.0 `.env` (CEO provided earlier this session but not persisted)
- `[!]` Add `gmb_url` to leads table (would mirror domain_audits.gmb_url, optional consistency improvement)

## Done Recently (2026-06-30)

- `[x]` D-2026-06-30-15: Google Maps grounding — 14/27 audits now in canonical place_id format via DataForSEO
- `[x]` D-2026-06-30-14: Added `gmb_url` top-level column to `domain_audits` (CEO ran the SQL)
- `[x]` D-2026-06-30-13: Two-scraper architecture + Opportunity Score formula in `audit_config.json` v2
- `[x]` D-2026-06-30-12: Denver exclusion rule (D-2026-06-30-12) — `audit_config.json` + lead-researcher SOUL.md + DECISIONS.md
- `[x]` 27 audits persisted in `domain_audits` (1 pre-existing Feb 2026 + 7 + 4 + 9 + 4 + 2 POC)
- `[x]` 26 of 27 audits have a GMB weblink (Vancouvervogueinteriors correctly NULL — no GMB at audit time)
- `[x]` Scrapling 0.4.8 wired as primary technical inspector (replaces urllib + Firecrawl)
- `[x]` ScrapeGraphAI 2.1.4 installed + importable (LLM calls not yet tested end-to-end)
- `[x]` DataForSEO MCP used for: domain_rank_overview, business_listings_search (Maps grounding)
- `[x]` Serper MCP used for: google_search reputation enrichment (Hasler, Ignite Digital)
- `[x]` Verified `audit_config.json` v4: 18/18 checks pass (JSON valid, structure, Supabase state matches claims, all ChIJ format valid, no Gemini redirects)
- `[x]` Two new employees (Scrapling, ScrapeGraphAI) — agents/tools, not HR
- `[x]` Updated `lead-researcher/SOUL.md` with two-scraper architecture + opportunity scoring + Denver exclusion
- `[x]` All hermes-verify-*.py temp files cleaned up

## Done (historical)

- `[x]` Wiki write reliability fixed — Python open() works (verified 2026-06-30)
- `[x]` 5 wiki governance files updated (AGENTS.md, DASHBOARD.md, KANBAN.md, DECISIONS.md, OFFER.md)
- `[x]` Agency vault moved: `C:\Users\denni\Hermes-AI-Agency\` → `~/wiki/agency-agents/hermes-ai-agency/`
- `[x]` Agency mission: "find GMB pages with no website or an outdated website"
- `[x]` GMB-Outdated Detection playbook (`okf/leadsniperai/playbooks/phase-1-gmb-outdated-detection.md`)
- `[x]` Phase 2 Continuous Discovery playbook (drafted, needs update for Scrapling primary method)
- `[x]` LeadSniper AI Run 001 + 002 reflections filed
- `[x]` LeadSniper-3.0 repo cloned + Supabase keys wired into `.env` and `backend/.env`
- `[x]` RIOS OKF subdomain `leadsniperai/` scaffolded (10 files, OKF v0.1 compliant)
- `[x]` Vercel deployment confirmed live (frontend-only stub, no backend)

## Artifact paths (quick links)

- Audit config v4: `C:\Users\denni\AI-Applications\LeadSniper-3.0\scripts\audit_config.json`
- LeadSniper-3.0 repo: `C:\Users\denni\AI-Applications\LeadSniper-3.0\`
- Scrapling source: `G:\AI-Applications\Scrapling` (0.4.8, editable)
- ScrapeGraphAI source: `G:\AI-Applications\scrapegraphai` (2.1.4)
- Supabase project: `yolqrstktoqlszybwymw` (27 audits in `domain_audits`)
- Wiki DECISIONS: `~/wiki/agency-agents/hermes-ai-agency/DECISIONS.md`
- Wiki DASHBOARD: `~/wiki/agency-agents/hermes-ai-agency/DASHBOARD.md`
- Lead-researcher SOUL: `~/wiki/agency-agents/hermes-ai-agency/employees/lead-researcher/SOUL.md`
- Playbooks: `G:\AI - Coding Projects\RIOS-CRM\RIOS\okf\leadsniperai\playbooks\`
- Output folders: `G:\AI - Coding Projects\RIOS-CRM\RIOS\okf\leadsniperai\outputs\`
- Vercel stub: `https://lead-sniper-3-0.vercel.app/` (frontend-only, no backend)
- Secrets (canonical): `~/.hermes/profiles/leadsniperai/.env` (Supabase URL + anon + service_role keys)
