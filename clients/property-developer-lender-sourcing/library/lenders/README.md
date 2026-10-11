# Lender Library

The re-usable universe of debt + equity capital sources that KlickSmartAI has profiled. Each lender gets a profile under `lenders/<slug>.md`, plus an entry in the index CSV.

## Current state (2026-10-10)

- **Empty.** No lender profiles yet.
- Reference data: `~/wiki/clients/veritas-developments/raw/notion/🏦 🏦 Veritas Capital Markets...md` contains 56 US + 28 Canadian lenders (un-mirrored). `~/wiki/clients/veritas-developments/projects/co-sponsor-gp-target-list.md` has 53 KC TAM orgs.
- When a new developer project is engaged, **pull relevant lenders from the Veritas reference data and validate**, do not auto-port.

## Population policy

- **Validate before adding.** A lender profile only enters the library if it has been (a) cited from a public source, (b) verified through a term sheet / agreement, or (c) confirmed by a deal team member.
- **De-duplicate.** If the same org appears under multiple roles (e.g. Polsinelli as both law firm and referral channel), use one profile with `roles:` in frontmatter.
- **Date-stamp.** Every profile has `last_verified:` in frontmatter. Stale = >12 months = needs re-verification.

## Schema

See `_template-lender-profile.md` for the per-profile template. Required fields:

- Name, slug, country, headquarters
- Capital type (debt / equity / both / mezz / pref / LP / co-GP)
- Loan / investment range (min, max, typical)
- Asset classes served
- Project stages served
- Geography
- Recourse (full / partial / none)
- Rate / fee range (or `TBD`)
- Sponsor experience requirement
- Broker acceptance (yes / no / preferred)
- Compliance lane (1-4 from `_config/compliance.md`)
- Source (public URL, term sheet, call notes, attribution)
- Last verified date
- Notes / open questions

## Index CSV columns

See `_lender-index.csv` for the column headers.

## How to find a lender for a deal

1. Read `../capital-stack/_stack-layer-coverage.md` to see which lender type fits which layer
2. Filter index by `country`, `geography`, `capital_type`, `asset_class`, `project_stage`
3. Score survivors against the deal's intake using `../methodology/03-scorecard.md`
4. Pull top-N profiles for shortlist
