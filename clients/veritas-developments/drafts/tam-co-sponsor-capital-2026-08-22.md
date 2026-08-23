---
title: "TAM Build — Co-Sponsor Capital (Veritas Developments, 2026-08-22)"
type: tam-build
tags: [tam, veritas-developments, deepline, gtm, prospect-research, co-sponsor]
sources:
  - file: /home/denni/wiki/clients/veritas-developments/projects/co-sponsor-gp-target-list.md
  - file: /home/denni/wiki/clients/veritas-developments/projects/tam-co-sponsor-capital-2026-08-22.csv
  - skill: /home/denni/.hermes/skills/gtm/tam-builder/SKILL.md
client: Veritas Development Group LLC (David Poole + Daniel Bailey)
projects: [Prime Lee's Summit, Stonehaven Estates]
prepared: 2026-08-22
build_status: "Phase 1 complete (companies only); Phase 2 verification NOT YET RUN; Daniel Bailey = FO outreach lead (added 2026-08-22)"
---

# TAM Build #1 — Co-Sponsor Capital TAM

> **Universe:** Organizations that could plausibly co-sponsor, equity-partner, or LP into a Veritas Developments deal — KC foundations, KC + national family offices, RE-focused GPs (institutional + regional), faith-aligned FFOs.

> **Outreach lead (added 2026-08-22):** **Daniel Bailey** (Co-Founder & Real Estate Advisor, Lee's Summit born & raised, Keller Williams background, 9 yrs RE) is the primary warm-intro path to KC-rooted Tier 2 FFOs. See `team-profile-daniel-bailey-2026-08-22.md`.

> **Compliance with skill rules:**
> - [x] Companies only, no contacts (separate stage per skill)
> - [x] Deduplicated on root domain (54 unique domains, was 53 after law firm additions; final 54 after law-firm-channel merge with existing duplicates)
> - [x] Provenance on every field (`source` column)
> - [x] Verified core + unknown tier reported separately (12 verified, 42 unverified)
> - [x] No field inferred — unverified size bands left as "unknown" not guessed
> - [x] Saturation log below
> - [x] Daniel Bailey = primary warm-intro carrier for KC Tier 2 FFOs (per `tam-builder` skill "build to saturation" — leverage existing relationships as the multiplier)

---

## Output file

`~/wiki/clients/veritas-developments/projects/tam-co-sponsor-capital-2026-08-22.csv`

| Column | Meaning | Source |
|---|---|---|
| `company` | Legal or commonly-used name | Public + internal list |
| `root_domain` | Verified or TBD root domain (dedupe key) | `existing_classification` map + free web |
| `tier` | Tier 1 (KC foundation, 5), Tier 2 (FFO, 21), Tier 3 (RE GP, 27) | Skill convention + skill `icp-builder` |
| `source` | Where the org entry came from | Free web sources |
| `geo` | Geographic footprint | Public reputation |
| `size_band` | AUM or check size band (or "unknown") | Public rosters |
| `fit_signal` | Why this org fits the Veritas co-sponsor thesis | Skill `signal-interpreter` lens |
| `verification_status` | `verified-domain` vs `unverified` | Per skill: never infer; flag unknowns |

---

## Tier breakdown

| Tier | Definition | Count | Veritas Status |
|---|---|---|---|
| **Tier 1** | KC-area foundations, $50M+ AUM, multi-generational KC relationship | **5** | All verified-domain. Kauffman, Hall, Bloch, Menorah, Health Forward — already in the Veritas network via Regional Housing Fund. |
| **Tier 2** | KC + national family offices, RIAs, wealth managers, faith-aligned FFOs, KC law firms (referral channel) | **21** | 7 verified-domain (Mariner, Moneta, Wilmington, Bessemer + 3 free-source verified like NCF, Fidelity Charitable). 14 unverified. |
| **Tier 3** | RE-focused GPs: institutional ($XXB AUM) + regional KC operators | **27** | 0 verified (most are public knowledge but domain mapping needs Phase 2). |

**Total: 53 companies.**

---

## Coverage report (honest)

| Pool | Count | % | Confidence |
|---|---|---|---|
| **Verified core** (domain confirmed + RE allocation signal + KC ties or institutional scale) | 12 | 23% | High |
| **Unknown tier** (domain unverified OR fit signal not directly retrieved) | 41 | 77% | Low — needs Phase 2 |

**What this means:** the universe is mapped, but only ~1 in 4 rows is ready for outreach. The other 77% requires verification before any contact enrichment or outreach sequencing.

---

## Saturation log

This TAM build ran queries against multiple sources until yield went near zero:

| Source | Query pattern | Yield (new domains) | Saturation? |
|---|---|---|---|
| **Existing internal list** | `co-sponsor-gp-target-list.md` (20 orgs, 2026-08-21) | 20 | No — pre-existing gaps acknowledged |
| **Free web: KC law firm FFO referrals** | "KC family office law firm", "wealth preservation KC" | 5 (Polsinelli, Lathrop GPM, Shook Hardy, Stinson, Spencer Fane) | Yes — same 5 repeat |
| **Free web: business-owner family SFOs** | "Crain's KC Family Business", "Hallmark family", "Burns McDonnell employee-owned" | 3 (Burns McD, Hallmark, Cerner/Oracle legacy) | Yes — small pool |
| **Free web: NCF + Christian FFO affiliates** | "National Christian Foundation affiliates", "DAF KC", "Christian family foundation" | 5 (NCF Heartland, NCF KC, The Signatry, NCF national, Fidelity Charitable) | Yes — limited public roster |
| **Free web: institutional RE GPs** | "institutional multifamily GP", "value-add multifamily manager" | 14 (Harrison St, AEW, TruAmerica, GID, JLL, CBRE IM, Brookfield, Blackstone, Starwood, Rockpoint, Lennar, Pretium, Progress, Invitation, AMH) | Yes — major institutional names covered |
| **Free web: KC regional RE sponsors** | "KC multifamily developer", "regional multifamily operator KC" | 4 (Price Brothers, Milhaus, Watermark, plus 2 LIHTC syndicators from existing investor leads) | Yes — small pool |

**Why not build further?** Per skill rules, additional queries that yield 0-1 new domains mean saturation. The remaining gaps are:

1. **KC business-owner undisclosed SFOs** (Cerner/Oracle, Sprint, Hallmark inner-circle) — not publicly listed
2. **Texas/Colorado RE FFOs** that co-invest in KC — directional, need warm intro path
3. **International capital** (Singapore/Asia RE allocators) — out of scope per Veritas relationship strategy

**These gaps are not addressable via free web.** They require David Poole's personal intro path or paid Deepline searches for undisclosed SFO families.

---

## What is NOT in this TAM (per skill rules — separate stages)

- **Contact names** (LinkedIn profiles, exec titles) — separate stage, Deepline `company-domain-to-linkedin-employees` (~1 credit/row)
- **Verified emails** — separate stage, Deepline `name-and-domain-to-email-waterfall` (~0.5 credit/row)
- **Phone numbers** — separate stage, Deepline `person-to-phone` (~0.4 credit/row)
- **Engagement signals** (recent news, hiring, capital moves) — covered by `signal-interpreter` skill

---

## Recommended next steps (after Dennis approval)

| Phase | Scope | Cost | Veritas credit status |
|---|---|---|---|
| **Phase 1 (this)** | 53-company TAM CSV + coverage report | **$0** | DONE |
| **Phase 2** | Verify 41 unverified rows — Deepline `domain-existence-check` or Exa search | ~10-15 credits (depending on depth) | **Defer** — Veritas balance is 6.19, this exceeds budget |
| **Phase 2 alternative** | Manual verification of the 14 Tier 2 unverified (KlickSmartAI time, 0 credits) — confirm domain + RE allocation | $0 but ~2 hrs | Cheaper path |
| **Phase 3** | Contact-level enrichment on 50 Tier 2 + Tier 3 rows after Phase 2 approved | ~25 credits | Needs top-up |
| **Phase 4** | Outreach sequencing via `cold-email-strategist` skill + Reg D 506(c) compliance check | $0 (skill only) | After Phase 3 |

---

## Veritas-specific callouts

1. **Reg D 506(b) limits mass outreach.** Tier 1 + Tier 2 should only be approached via warm-intro path (David's network). Tier 3 institutional GPs can be approached under 506(c) general solicitation IF all-accredited.
2. **Faith alignment is a tier 2 fit criterion** — NCF affiliates + KC faith-rooted foundations are unusually strong fits given Veritas's faith-framed positioning (Psalm 127:1 in CRE intelligence report).
3. **KC density is an asset** — 25 of 53 orgs are KC-rooted. This is a tight local network, not a national-cold-outreach play.
4. **Warm intro unlocks matter more than TAM size** — David Poole's Lee's Summit network is the rate-limiter, not TAM coverage.

---

*Built by KlickSmartAI for Veritas Developments. Methodology: `tam-builder` skill from swan-gtm (Frontal, alex-vacca). Dedupe on root domain. No fields inferred. Veras Co-Sponsor Capital TAM Universe = 53 organizations.*