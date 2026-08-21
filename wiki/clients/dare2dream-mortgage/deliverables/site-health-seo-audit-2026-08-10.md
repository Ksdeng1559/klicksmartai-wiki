# dare2dreammortgagecompany.com — Site Health & SEO Audit

Audit date: 2026-08-10
Sources: `audit-issues.csv` (134 rows), 3x keyword exports (22 unique tracked keywords), live verification of homepage, robots.txt, `sitemap-xag.xml`, `sitemap-xagio-post.xml`, and one spam post.

Full visual report: https://claude.ai/code/artifact/8454ad00-2f12-4a65-a302-1de6fad2d446

---

## 0. CRITICAL — Site is compromised (fix before anything else)

Confirmed live on 2026-08-10. Of 312 posts in `sitemap-xagio-post.xml`, roughly **220 (~70%)** are gambling/casino/crypto-betting review articles in Spanish, French, German, Portuguese, Polish, Turkish, and Russian (e.g. "Vavada Bonuses and Promotions", "1win Resumen y Reputación", "Roobet Reseña y Reputación"). Most recent dated **2026-07-21**, meaning this is ongoing, not a one-time historical leftover.

The injection also reached the **homepage template itself** — it renders casino promo blocks (West Casino, Retro Casino, Rockstar Casino, Royal Valley Casino, Mad Casino, no-KYC platforms, crypto-casino payment guides) interleaved with the real mortgage broker content.

This also explains the broken-link pattern in section 1 below: 27 of the 44 broken links point to `/market-news/`, a 404 target linked from nearly every page including spam posts — almost certainly a sitewide auto-inserted link from the injection, not a content mistake.

### Action checklist
- [ ] Put site behind maintenance mode / restrict public access immediately
- [ ] Run full malware scan (Wordfence, Sucuri SiteCheck, or host-level scan)
- [ ] Diff recently modified files/plugins against last known-clean backup
- [ ] Audit WP admin users + API keys for anything unrecognized
- [ ] Rotate all passwords, secret keys, and salts regardless of scan results
- [ ] Investigate the `Xagio` SEO plugin and any outdated/unfamiliar plugin or theme for known vulns — its sitemap naming (`sitemap-xagio-*.xml`) is what's currently indexing the spam posts
- [ ] Bulk-delete the ~220 spam posts
- [ ] Strip injected casino content from the homepage/template (template-level fix, not just content deletion)
- [ ] Check Google Search Console → Security Issues for a "hacked site" manual action
- [ ] File a reconsideration request once cleanup is verified

---

## 1. Broken internal links (44 total)

All 44 resolve to one of two dead targets — fixing the target clears most of the count.

| Dead target | Linked from | Likely cause |
|---|---|---|
| `/legal/cookies-and-tracking-technologies` | 5 pages | Real page, moved/renamed |
| `/market-news/` | 27 pages | Sitewide template link, tied to the compromise (see §0) |
| `/services/ccpa`, `/intellectual-property-policy`, `/privacy_policy`, `/t-shirts`, `/users/sign_in` | 5 links from `/services/` | Leftover theme/demo boilerplate |

### Action checklist
- [ ] Confirm no real page still links `/market-news/` once spam posts are removed; if the section is gone for good, remove from nav/footer instead of redirecting to a placeholder
- [ ] Restore or relink `/legal/cookies-and-tracking-technologies`
- [ ] Remove dead `/services/` links (t-shirts, sign-in, duplicate privacy-policy path)

---

## 2. On-page issues (real mortgage pages)

| Issue | Pages |
|---|---|
| Missing H1 | `/about/`, `/careers/`, `/projects/`, `/resources/`, `/residential-financing`, `/commercial-financing/` |
| Missing meta description | Homepage, `/careers/`, `/resources/`, `/mortage-calculator/` (note: URL itself is misspelled "mortage") |
| Title too long (target 50–60 char) | 11 pages — worst: `/refinancing/` (79 char); location pages (delta-bc, nanaimo-bc, colwood-bc, saanich-bc, whistler-bc, squamish-bc, victoria-bc, campbell-river-bc) all 61–65 char |
| Meta description too long (target 160 char) | `/services/` (279 char, worst), 8 location pages, `/refinancing/`, `/residential-financing`, `/campbell-river-bc/` |
| Heading levels skip (H1 → H3) | 24 pages, incl. homepage, `/about/`, `/services/`, `/reviews/`, most location pages |
| Images missing alt text | `/services/` — 14 of 30 images |

### Action checklist
- [ ] Add homepage meta description first (highest-traffic page, currently none)
- [ ] Add H1 to the 6 pages missing one, matched to each page's title tag
- [ ] Trim the 11 over-length titles/descriptions, keyword front-loaded
- [ ] Fix heading hierarchy on the 24 flagged pages, starting with homepage + `/services/`
- [ ] Add alt text to the 14 images on `/services/`
- [ ] Fix `/mortage-calculator/` URL typo (redirect old → new, keep old as 301)

---

## 3. Keyword position & opportunity

Deduplicated from the 3 keyword exports (all three are the same 22 terms, sorted differently). Rank out of 100 — **nothing currently ranks on page 1** (rank ≤ 10). "Score" = exporting tool's on-page optimization score for the ranking URL.

| Keyword | Rank | Volume | CPC | Score | Ranking page |
|---|--:|--:|--:|--:|---|
| how much afford home | 91 | 2,400 | $1.26 | 63 | /how-much-house-can-you-afford.../ |
| what price of home can i afford | 97 | 210 | $1.15 | 63 | /how-much-house-can-you-afford.../ |
| home affordability | 96 | 50 | $10.58 | 63 | /how-much-house-can-you-afford.../ |
| what house can i afford canada | 82 | 50 | $1.11 | 32 | /how-much-house-can-you-afford.../ |
| reverse mortgage broker | 88 | 320 | $33.84 | 6 | /reverse-mortgage/ |
| reverse mortgage brokers | 90 | 320 | $33.84 | 15 | /reverse-mortgage/ |
| reverse mortgage bc | 83 | 90 | $21.63 | 13 | /reverse-mortgage/ |
| reverse mortgage vancouver | 86 | 50 | $20.01 | 8 | /reverse-mortgage/ |
| reverse mortgage british columbia | 81 | 10 | $14.23 | 6 | /reverse-mortgage/ |
| hard money lending | 72 | 260 | $14.99 | 32 | /hard-money-loan/ |
| hard money lender | 73 | 260 | $14.99 | 17 | /hard-money-loan/ |
| lending hard money | 54 | 260 | $14.99 | 5 | /hard-money-loan/ |
| hard equity lenders | 50 | 260 | $14.99 | 1 | /hard-money-loan/ |
| hard money | 75 | 70 | — | 22 | /hard-money-loan/ |
| private money lender | 68 | 210 | $16.26 | 8 | /hard-money-loan/ |
| private money lenders | 97 | 210 | $16.26 | 1 | /hard-money-loan/ |
| private money loan | 49 | 210 | $16.26 | 0 | /hard-money-loan/ |
| private money lender near me | 75 | 70 | $10.33 | 0 | /hard-money-loan/ |
| mortgage broker coquitlam | 33 | 210 | $11.11 | 1 | /mortgage-broker-coquitlam-bc/ |
| mortgage broker coquitlam bc | 33 | 210 | $11.11 | 0 | /mortgage-broker-coquitlam-bc/ |
| coquitlam mortgage broker | 34 | 210 | $11.11 | 0 | /mortgage-broker-coquitlam-bc/ |
| mortgage brokers coquitlam | 34 | 210 | $11.11 | 0 | /mortgage-broker-coquitlam-bc/ |

**Patterns:**
1. `/mortgage-broker-coquitlam-bc/` is the best-ranking page site-wide (33–34) with essentially zero optimization score — ranking on link/local signal alone, primed to move with modest on-page work.
2. Reverse mortgage terms carry the highest CPC ($20–34, strong buyer intent) but the lowest content scores (6–15) — high commercial value sitting on thin content.
3. Four Coquitlam variants all point at one URL — that's a healthy consolidated page, not cannibalization. Keep it that way.

### Action checklist
- [ ] Optimize `/mortgage-broker-coquitlam-bc/` — title, H1, body copy targeting the local term
- [ ] Rebuild `/reverse-mortgage/` with real depth — highest CPC on the site, weakest content
- [ ] Support `/how-much-house-can-you-afford.../` with backlinks/internal links — best content score (63) and top search volume (2,400/mo), push it toward page 1 rather than rewriting

---

## Priority order

1. **§0 — Contain and clean the compromise.** Today. Nothing else matters until this is done — every hour live adds more indexed spam under this domain.
2. **§1 — Clear link-rot.** This week, after cleanup (most resolves automatically once spam posts are deleted).
3. **§2 — On-page fundamentals.** Next 1–2 weeks.
4. **§3 — Content investment on already-paying intent.** Ongoing.
