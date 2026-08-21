# Hermes AI Agency — Chief of Staff NOTES

Working memory. Not a log of decisions (those go in `DECISIONS.md`). Just the live train of thought that survives between sessions.

## 2026-06-30 — agency bootstrap session

- Adopted new "Hermes AI Agency" framing per D-2026-06-30-02.
- Created vault skeleton at `~/Hermes-AI-Agency/`.
- Top-level files written: AGENTS.md, README.md, DASHBOARD.md, KANBAN.md, REGISTRY.md, DECISIONS.md, NOTES.md.
- About to hire the first 3 employees (lead-researcher, site-auditor, proposal-writer).
- LeadSniper AI subdomain in RIOS OKF vault already has the playbook + 2 run reflections — that becomes the lead-researcher's primary procedure.
- Outstanding CEO escalations: Gemini API key, pricing, CRM choice, outreach stack, run 003 direction.

## Open loops to track

- LeadSniper-3.0 TypeScript errors fixed but Gemini grounding test not run — blocked on API key.
- Schema.org absence across all 8 audited sites is the strongest consistent LeadSniper AI signal. The agency thesis ("AI-built services + Digital Employees") actually maps well onto this gap — we can sell "AI-Search-ready rebuild" specifically, not just generic "new website."
- Reputation gate (4.0+ AND 20+ reviews) is too tight for the cleaning segment. Either reframe rubric or change category.

## Things I'm being honest about

- Vancouver commercial-cleaning hypothesis didn't hold. Sites are not weak by conventional standards. The opportunity is narrower than expected — it's specifically **AI-Search readiness** (schema, structured data, content extraction for LLMs), not "weak websites" generally.
- The agency doesn't have a paying customer yet. Phase 1 has produced internal signal, not revenue.
- LeadSniper-3.0 is a partially-broken client-facing portal I inherited. I won't claim it's "production-ready" — I just made it type-check clean.

## Next session priorities (assuming CEO doesn't redirect)

1. Wait for / receive Gemini API key → finish grounding test on LeadSniper-3.0.
2. Build out service-offer internal docs (no pricing yet).
3. Draft outreach sequences (CEO review before send).
4. Decide run 003 direction (or pivot entirely).
5. Hire content-writer + sales-operations when their respective blockers clear.

## 2026-06-30 — Lead Sniper 3.0 wired to Supabase, 8-site audit successful

**Major unlock:** the 8-site batch audit on 2026-06-30 proved the Lead Sniper 3.0 + Supabase + 6-signal audit pipeline works end-to-end.

### What worked
- Connected to Supabase project `yolqrstktoqlszybwymw` with service_role key
- Discovered it's a production backend with 4.5 months of data: 375 leads, 71 battle_cards, 38+ other tables
- Used existing `domain_audits` table (no new schema needed)
- Wired keys to LeadSniper-3.0's `.env` and `backend/.env`
- Ran 6-signal audit on 8 Vancouver home builders
- Persisted 7 results to `domain_audits` (1 timed out)
- 3/7 (43%) flagged as outdated — real prospects surfaced

### Key learnings
- `domain_audits.user_id` references `auth.users.id`, NOT `profiles.id` (FK constraint)
- Use `sales@klicksmartai.com` (7ef5b581-8ae0-4046-b485-6a0caf221fd6) as the canonical owner for agency actions
- The 6-signal outdated criteria works: 43% hit rate on a real sample, vs. 0% with the old "find weak sites" framing
- 4/8 sites are fully modern (Major Homes, Glenmark, Upward Construction) — they don't need rebuilds
- 3/8 are real prospects: Roadhouse Projects (no HTTPS), Hasler Homes (no schema), Supercity Construction (Squarespace, no schema)

### Top outreach targets (from the 8-site batch)
1. **Roadhouse Projects** (http://www.roadhouseprojects.com/) — 4/6 signals, score 3.0, no HTTPS
2. **Hasler Homes** (https://haslerhomes.com/) — 3/6 signals, score 3.5, 5.0★ on GMB
3. **Supercity Construction** (https://supercityconstruction.com/) — 2/6 signals, score 4.0, Squarespace

### Next steps
1. Phase 2 Continuous Discovery playbook drafted (proposed, awaiting CEO approval)
2. Wire `GEMINI_API_KEY` into LeadSniper-3.0's `.env`
3. Get `GOOGLE_MAPS_API_KEY` for Places API
4. Run `docker compose up --build` on LeadSniper-3.0
5. Deploy to Vercel (after Docker build verified)
6. Schedule the weekly cron job

### Open questions for CEO
- Confirm "Lead Sniper 3.0" is the canonical name (CEO used 4 different names this session)
- Should chief-of-staff use `sales@klicksmartai.com` for all agency actions, or create a dedicated `chief-of-staff@agency.local` user?
- Vancouver + Home Builder for the first weekly run, or stick with the legacy Vancouver + Commercial Cleaning?
