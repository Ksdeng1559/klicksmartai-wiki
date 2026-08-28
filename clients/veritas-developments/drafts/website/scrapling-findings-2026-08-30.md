## Scrapling browser-render finding (2026-08-30)

**Method:** `scrapling extract fetch` (Playwright headless Chromium, network-idle, 60s timeout) on `https://veritasdevelopmentgroupllc.com/`

**Result:** HTTP 200, 13,555 bytes of rendered markdown, 397 lines.

**Key finding:** The site IS a JS-rendered SPA — raw HTML contains "You need to enable JavaScript to run this app." (line 1). But when JavaScript executes (as it does in this browser render), the page contains **substantial, complete content**: 4 divisions (Development, Construction, Site Development, Capital Advisory), leadership bios (David Poole, Mike Poole, Daniel Bailey), a 61-item portfolio, service area, financing page, and full contact details.

**Implication for the audit #8 diagnosis:**
- The "0 crawlable words" finding came from an **HTTP-only crawl** (no JS execution).
- This is NOT a thin-content site — it is a **JS-gated content site**.
- Whether Google indexes it depends on **whether Googlebot's renderer successfully executes the JS** and is allowed to crawl it.
- The fix remains the same (server-render / pre-render / ensure JS executes for Googlebot), but the severity framing changes: it's not "you have no content" — it's "you have rich content Google may not be rendering."
- **Confirm via Google Rich Results Test / Google Search Console URL inspection** (JS render test) before assuming Google can't see it.


## Additional critical finding — robots.txt + sitemap.xml both return SPA shell (2026-08-30)

**Method:** raw `curl` of `https://veritasdevelopmentgroupllc.com/robots.txt` and `/sitemap.xml`

**Result:** BOTH return HTTP 200 with the full SPA HTML `<!doctype html>...<div id="root">` shell — NOT plain-text robots or XML sitemap.

**Implication:**
- `robots.txt` serves HTML instead of `User-agent:` directives → Google receives NO crawl rules, NO sitemap reference, NO disallow directives.
- `sitemap.xml` serves HTML instead of XML → Google has NO URL inventory via sitemap; discovery depends entirely on JS rendering + internal links.
- Root cause is the same hosting misconfiguration as the JS-gate: the host is configured to serve `index.html` as a **catch-all for every route** (`/`, `/financing`, `/robots.txt`, `/sitemap.xml` all return the app shell).
- This is a **CRAWLABILITY BLOCKER**, not just an on-page issue. Even if Google's renderer executes JS on the homepage, it cannot read a robots.txt or sitemap.
- **Fix:** configure the host/static server to (a) serve a real plain-text `robots.txt` referencing the sitemap, (b) serve a real XML `sitemap.xml`, and (c) serve `index.html` only for actual app routes — or switch to server-side rendering / pre-rendering so route-requests return real HTML.
- This elevates the severity: audit #8 diagnosed "JS render gap" — now confirmed it's a full **catch-all-SPA hosting misconfiguration** affecting robots.txt + sitemap + every route.
