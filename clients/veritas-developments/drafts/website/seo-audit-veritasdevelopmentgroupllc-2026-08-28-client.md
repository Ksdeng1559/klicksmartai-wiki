---
title: "SEO Audit & Recommendations — veritasdevelopmentgroupllc.com"
type: site-audit-client
status: DRAFT — awaiting owner validation
created: 2026-08-28
client: Veritas Development Group LLC
domain: veritasdevelopmentgroupllc.com
audit_date: 2026-08-28
predecessor: (internal — kept for traceability)
---

# SEO Audit & Recommendations — veritasdevelopmentgroupllc.com

> **Bottom line: the foundation is missing.** The site is reachable and returns a healthy response. But Google can't actually read the content — the page renders through JavaScript, so the words that describe your business are invisible to search engines. Fixing this single issue clears most of what's wrong.

## At a glance

| What we checked | What we found |
|---|---|
| Domain | `veritasdevelopmentgroupllc.com` |
| Pages indexable | **1** (homepage only) |
| Site reachable | ✅ Yes — secure, fast response (69 ms) |
| Page title | 99 characters — too long, gets cut off in search results |
| Meta description | 242 characters — too long, gets cut off in search results |
| Headline (H1) | **Missing** |
| Words visible to Google | **0** |
| Links to other pages | **0** |
| XML sitemap | Not present |
| Search keywords ranking | None — site is not indexed |
| Backlinks | 0 sites linking to you |
| Google Business Profile | Not yet set up |

**Top 3 priorities:**

1. **Make the homepage content visible to search engines.** This single fix clears 3 of the 5 audit findings.
2. **Add a clear page headline (H1)** and a few hundred words describing your services and service area.
3. **Set up the basics search engines need:** XML sitemap, Google Business Profile, and a few starter pages (Services / Projects / About / Contact).

**Quick wins:** trim the page title and meta description. About 15 minutes of work, zero risk.

---

## What we found (in priority order)

### 1. The homepage content isn't visible to search engines (High priority)

- **What we saw:** Page analysis reports `wordCount: 0`. The page shows a meaningful title and meta description in the source, but the actual body content — the words describing your business — aren't in the HTML Google can read.
- **Why it matters:** **This blocks indexation entirely.** Google cannot rank what it cannot read. This single issue causes 3 of the 5 audit findings below.
- **Likely cause:** The site loads its main content through JavaScript (common with modern website builders and single-page frameworks).
- **Recommended fix:**
  1. Have your developer server-render the homepage so the headline, body copy, and navigation appear in the initial HTML response — not just after JavaScript runs.
  2. Once rendered, add **300+ words** of real content describing the company, your services, and your service area (Lee's Summit + Kansas City, MO).
  3. Re-run the audit afterward — the word count should jump from 0 to 300+, and three of the five findings below should clear automatically.

### 2. Missing page headline (H1) (High priority)

- **What we saw:** No H1 detected on `https://veritasdevelopmentgroupllc.com/`.
- **Why it matters:** The H1 is the strongest on-page signal for what a page is about. Missing H1 is a quality flag.
- **Recommended fix:** Add a single H1, front-loaded with the primary keyword. Suggested: `<h1>Real Estate Development & Construction in Lee's Summit, MO</h1>`.

### 3. No links to other pages (High priority)

- **What we saw:** Homepage has zero internal links. And because of finding #1, there are no other pages to link to anyway.
- **Why it matters:** Search engines discover pages by following links. With no links from the homepage, any future service or portfolio pages will be invisible to crawlers.
- **Recommended fix:** Add a server-rendered navigation bar (Home / Services / Projects / About / Contact). Even stub pages with short descriptions are better than nothing — they give crawlers a path to follow.

### 4. Meta description too long (Medium priority)

- **What we saw:** 242 characters. Recommended length: 70–160.
- **Why it matters:** Search engines truncate long descriptions in results. Your visible description currently cuts off mid-sentence.
- **Recommended fix:** Trim to ~150 characters. Suggested:
  > "Veritas Development Group LLC — real estate development, commercial construction, and capital advisory in Lee's Summit & Kansas City, MO. Built on integrity."

### 5. Page title too long (Medium priority)

- **What we saw:** 99 characters. Recommended length: 50–60.
- **Why it matters:** Search results truncate long titles. Important keywords get pushed off the end.
- **Recommended fix:** Trim to ~55 characters. Suggested:
  > "Veritas Development Group LLC \| Lee's Summit, MO" (47 characters)

---

## Technical health check (limited — site too thin to fully score)

| Dimension | Status | Notes |
|---|---|---|
| HTTPS (secure connection) | ✅ Yes | `https://veritasdevelopmentgroupllc.com/` returns 200 |
| Server response time | ✅ Healthy | 69 ms |
| Mobile-friendly | ⚠️ Not verified | Re-test after the homepage content fix lands |
| Page speed | ⚠️ Not run | Will test once the page is fully rendered |
| Structured data (schema) | ⚠️ Not detected | Cannot be reliably detected until the page renders. We'll re-test after the fix. |
| XML sitemap | ❌ Not present | Required |
| robots.txt | ⚠️ Not checked in this run | Verify in the next pass |

---

## Authority & local presence (Stage 1 prerequisites)

| Item | Status | Notes |
|---|---|---|
| Other sites linking to you | 0 | Site has never been linked from anywhere we can see |
| Search keywords ranking | 0 | Site is not indexed |
| Google Business Profile | Not yet set up | Required for local SEO |
| Bing Places | Not yet set up | Required for local SEO |
| Name/address/phone consistent across the web | Not yet verified | Required for local SEO |

---

## Prioritized action plan

### 🔴 Critical — do these first (they block indexation)

1. **Fix the homepage so search engines can read it.** This is the single fix that unblocks 3 of the 5 audit issues. ~2–4 hours of developer work.
2. **Add a clear headline + 300+ words** of real, keyword-rich content describing your services + service area.

### 🟠 High-impact — within 1 week of fixing the homepage

3. **Trim the page title and meta description.** Quick win — about 15 minutes. *(See recommendations #4 and #5 above.)*
4. **Add a navigation bar with stub pages** (Services / Projects / About / Contact).
5. **Create and submit an XML sitemap** to Google Search Console and Bing Webmaster Tools.

### 🟢 Quick wins — do these in parallel

6. Trim title + meta (same as #3).
7. Add Organization + LocalBusiness structured data to the homepage once it's server-rendered.
8. Set up Google Business Profile + Bing Places (about 30 minutes).

### 🔵 Long-term — after the critical fixes ship

9. Build out service-area pages (Lee's Summit, Kansas City, Jackson County MO, etc.) for local SEO.
10. Begin citation building (BBB, Missouri business directories, Kansas City real-estate associations).
11. Acquire first backlinks (press release, local press coverage, industry directories).
12. Set up monthly rank tracking + Search Console monitoring.

---

## Decision point

From the previous audit (2026-08-26), we asked:

> "Do you want to:
> 1. Coordinate with your developer to make the homepage readable to search engines, or
> 2. Build a static pre-rendered version in parallel, or
> 3. Park this audit and focus on the investor flywheel (current priority)?"

**This audit confirms the diagnosis.** The fix is the same. We're waiting on your call before taking next steps.

---

## About this audit

- **Date:** 2026-08-28
- **Pages analyzed:** 1 (homepage)
- **Method:** Automated site crawl + search-engine data
- **Status:** Draft — awaiting your validation before any next steps

This draft supersedes the earlier internal version of the audit, which is kept for traceability.
