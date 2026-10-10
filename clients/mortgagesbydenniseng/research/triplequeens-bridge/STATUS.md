# Triple Queens — Partner Status (INACTIVE 2026-10-03)

**Status:** ⛔ INACTIVE — do not reactivate without Dennis's explicit instruction.

**Inactivation date:** 2026-10-03

**Reason for inactivation:**

1. **Website is unreachable.** `https://triplequeens.com` returns the default HostGator "Coming Soon" WordPress placeholder page. No products, no team, no contact form, no content beyond a logo screenshot uploaded in June 2025.
2. **Public broker channel is offline.** No way to onboard new broker partnerships or pull rate sheets.
3. **Dennis verbal confirmation 2026-10-03:** "They are not active at the moment. They are not available online."

**Verification (2026-10-03):**
- `curl -L https://www.triplequeens.com` → HTTP 200, 0.88s response (DNS resolves, server responds, but serves placeholder)
- Scrapling scrape → 25 lines of HostGator "Coming Soon" template + WordPress login link exposed
- Last visible real upload: logo screenshot, June 2025

**What this means for content:**

All pages that used Triple Queens as the **primary** named anchor must be re-anchored to multi-lender comparison + the closest still-active lender (typically Glasslake or Kingsmen). See the patched `verticals/business-loans-canada/sitemap.md` for the per-page reassignment.

**What is NOT affected:**

- The historical research files in this folder (`triplequeens_partner_analysis.md`, `triplequeens_industries.md`) are **preserved on disk** — they document what Triple Queens was when they were active, and remain useful if/when the company reactivates.
- The 6 citations in `verticals/business-loans-canada/executive-summary-with-citations.md` referencing the Triple Queens sitemap (accessed 2026-09-14) remain valid as historical references.

**Comeback conditions (would warrant re-activation):**

- Triple Queens republishes their product pages (or equivalent)
- Dennis confirms renewed partnership with broker-of-record access
- AND broker agreement is in writing (currently "pending" since 2026-09-14)

**Files in this folder:**

- `triplequeens_partner_analysis.md` — 12KB historical profile (active when written)
- `triplequeens_industries.md` — 6KB industry surface (13 indexed URLs)
- `processed.json` + `raw_overview.json` — DataForSEO keyword pull data (cached)
- `STATUS.md` — this file

**Do not delete this folder.** Per Dennis's standing convention, superseded research stays on disk with a STATUS.md so future agents don't accidentally re-derive.