# dare2dreammortgagecompany.com — §0 Compromise Remediation Runbook

Audit date: 2026-08-10 · Re-verified live: 2026-08-11 (still compromised) · Internal draft — NOT for external distribution without owner review

---

## Situation

WordPress site injected with multi-language gambling/casino/crypto-betting SEO spam. ~220 of 312 indexed posts are spam (sitemap: `sitemap-xagio-post.xml`). Homepage template itself renders casino promo blocks (West Casino, Retro Casino, Rockstar Casino, Royal Valley Casino, Mad Casino, Vavada). Injection ongoing — newest spam dated 2026-07-21, still live 2026-08-11.

---

## Phase 1 — Contain (Day 0, 2–4 hrs)

Goal: stop the bleeding. Indexing more spam every hour.

1. **Put site behind maintenance mode** (host-level, not plugin):
   - cPanel: File Manager → create `maintenance.html`, add `.htaccess` rewrite to serve it for all non-admin IPs, OR
   - Host panel: enable "Maintenance Mode" if available, OR
   - Fastest: block public access via host firewall / set account to suspend temporarily
   - Keep an IP allowlist for you + whoever remediates
2. **Kill automated spam production:**
   - Disable `wp-cron.php` via `define('DISABLE_WP_CRON', true);` in wp-config.php
   - If a queue/worker keeps posting, stop it (check host process manager, wp-cli `wp cron event list`)
3. **Freeze credentials:**
   - Change hosting panel password NOW (before scans — don't lock yourself out, but assume attacker has it)
   - Rotate DB user password, FTP/SFTP passwords

## Phase 2 — Identify entry point (Day 0–1)

1. **Full malware scan:** Wordfence CLI or Sucuri SiteCheck; host-level scan (e.g. Imunify360 if cPanel) — run all three if available; they find different things
2. **Diff against last known-clean backup:**
   - Files: `diff -rq` last-clean backup vs current `wp-content/` (or use `wp core verify-checksums`)
   - List recently modified files: `find wp-content -type f -mtime -30` — triage by mtime
   - DB: dump current DB, diff against backup dump for injected rows (options, posts)
3. **Audit WP admin users:** `wp user list` — look for unknown admins; remove immediately
4. **Audit plugins/themes:**
   - `wp plugin list` / `wp theme list` — flag anything outdated, abandoned, or unfamiliar
   - **Xagio SEO plugin is prime suspect** — its sitemap (`sitemap-xagio-*.xml`) is what's indexing the spam. Check version against known CVEs; if it's a premium/unknown plugin, treat as compromised
   - Check for rogue mu-plugins: `ls wp-content/mu-plugins/` — anything unfamiliar = backdoor
5. **Check core infection points:**
   - `wp-config.php` — base64, eval, weird includes
   - `wp-content/uploads/` — .php files should NOT exist here (classic backdoor nest)
   - `.htaccess` / nginx config — injected rewrite rules
   - Theme `functions.php` + header/footer templates — injected casino promo blocks live here (homepage template renders them)

## Phase 3 — Clean (Day 1–2)

1. **Bulk-delete spam posts** (identify by content pattern, not just count):
   ```bash
   # WP-CLI: delete posts whose slug/guid matches spam markers (casino brands, multi-language)
   wp post list --post_type=post --fields=ID,post_title --format=csv > posts.csv
   # filter to spam (Vavada, 1win, Roobet, bet365, casino, etc.) then:
   wp post delete $(cat spam-ids.txt) --force
   ```
   Alternative: SQL `DELETE FROM wp_posts WHERE post_type='post' AND post_title REGEXP 'casino|vavada|1win|bet365|roobet'` (backup first!)
2. **Strip template injection** (template-level, NOT just content):
   - Restore header.php / footer.php / functions.php / front-page template from clean backup
   - Remove injected casino blocks, no-KYC widgets, crypto-payment guides from theme
   - Grep theme for brand names: `grep -ril 'casino\|vavada\|1win' wp-content/themes/`
3. **Remove sitewide injected links** — `/market-news/` links in nav/footer/template (44 broken links, 27 from this)
4. **Clean DB thoroughly:** search `wp_options` for injected cron jobs, transients, autoload rows; remove unknown admin users

## Phase 4 — Harden & Rotate (Day 2, after clean verified)

1. Rotate ALL passwords: hosting, DB, FTP, WP admin, email account used for WP
2. Regenerate salts: `wp config shuffle-salts`
3. Delete unused plugins/themes; update everything to latest
4. Remove Xagio if it's the compromised vector (replace sitemap with Yoast/RankMath or core sitemaps)
5. Disable file editing: `define('DISABLE_FILE_EDIT', true);`
6. Add WAF + login protection: Wordfence (2FA on admin), limit login attempts, block wp-login by IP if possible
7. Security headers + disable XML-RPC if unused

## Phase 5 — Verify + recover (Day 2–3)

1. **Google Search Console → Security & Manual Actions:** check for "hacked site" manual action — if present, that's why rankings tanked
2. **Request review:** once clean, GSC → Security Issues → Request Review (Google will re-crawl)
3. **Clean indexed spam:** GSC → URL Removal for key spam URLs, or rely on 410/404s after deletion; update sitemap
4. **Confirm removal:** re-scan `sitemap-xagio-post.xml` (or replacement) — zero casino URLs; homepage renders clean
5. **Re-verify with a second scanner** (Sucuri SiteCheck is free and independent)

## Phase 6 — Monitor (ongoing)

- Schedule weekly malware scan (host or plugin)
- Alert on new admin users + plugin changes (`wp user list` in cron)
- Watch sitemap URL count — any big jump = reinfection
- Re-check GSC Security Issues weekly until clean

---

## Decision points for owner

| Question | Options |
|---|---|
| Who executes? | You (owner/host access) vs. hand to a WP security freelancer vs. host's cleanup service |
| Backup source | Need last known-clean backup — do we have one? Host may have one (JetBackup/cPanel) |
| Xagio plugin | Remove entirely vs. keep if version is current & vetted |
| Site downtime | Maintenance mode now (recommended) vs. risk more indexing |

## Estimated effort (assuming clean backup exists)

| Phase | Hours |
|---|---|
| Contain | 2–4 |
| Identify entry | 3–6 |
| Clean | 4–8 |
| Harden | 2–3 |
| Verify/recover | 2–4 |
| **Total** | **~13–25 hrs** (more without a clean backup) |
