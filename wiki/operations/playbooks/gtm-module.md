---
title: "KlickSmartAI GTM Module — Veritas Development Playbook Index"
type: reference
tags: [gtm, deepline, veritas-developments, lead-enrichment, sales, outbound, plays]
sources:
  - https://github.com/getaero-io/gtm-eng-skills
  - https://code.deepline.com/docs
  - https://deepline.com/docs/plays
  - ~/wiki/clients/veritas-developments/README.md
created: 2026-08-22
updated: 2026-08-22
---

# KlickSmartAI GTM Module — Veritas Development Reference

**Purpose:** Encode the GTM workflow for the Veritas Development Group LLC engagement (David Poole, Lee's Summit MO) so any agent (Hermes, Claude Code, Codex) runs the same enrichment recipes.

**Active client:** Veritas Developments (NOT Spectra Holdings). Two active projects:
- **Prime Lee's Summit** — mixed-use, 5×5-story multifamily + Price Chopper + CVS + 16-store retail
- **Stonehaven Estates** — 57 single-family lots on ±23.57 acres

**County of focus:** Jackson County, MO. KCCLT partnership target. Existing deliverables in `~/wiki/clients/veritas-developments/deliverables/` (2026-08-10 package).

---

## 1. When the user asks a GTM question

**Decision rule:** if the ask involves ≥3 contacts/companies OR any paid enrichment step, **always load the `deepline-gtm` meta-skill first** (it routes to the right recipe). Then follow the meta-skill's routing — do NOT skip docs.

If `deepline-gtm` is not yet installed in your environment, install it once:
```bash
npm install -g deepline@latest --registry https://code.deepline.com/api/v2/npm/
deepline auth status  # confirms login
```

For Claude Code (separate install): paste `Install the Deepline CLI and skills using https://code.deepline.com/agent-install.txt` in a fresh session.

---

## 2. Veritas-specific target domains

| Org type | Target domain | Use |
|----------|---------------|-----|
| County officials | `jacksoncountymo.gov` | Planning, Economic Development, Public Works, Finance |
| Municipal | `cityofls.net` | Lee's Summit Planning, Community Development |
| Land trust partner | `kcclt.org` | KCCLT executive + program leads |
| Grocery anchor | `pricechopper.com` | Corporate real estate team |
| Drug store anchor | `cvs.com` | Corporate real estate team |
| SFR operators / JV | `invitationhomes.com`, `progressresidential.com`, `americanhomes4rent.com` | Acquisition leads |
| Regional lenders | `firstmidwest.com`, `commercebank.com`, `umb.com`, `usbank.com` | Construction + perm debt |

---

## 3. Standard recipes (use the deepline-gtm meta-skill for routing)

### Recipe A — County / municipal official outreach

Use `company-domain-to-linkedin-employees` then filter by title.

```bash
deepline plays run prebuilt/company-domain-to-linkedin-employees \
  --input '{"domain":"jacksoncountymo.gov","max_items":50,"profile_depth":"full"}' --watch

# Filter rows: title ∈ ["Director", "Manager", "Administrator", "Commissioner", "Officer", "VP", "President"]
# Drop titles: ["Assistant", "Specialist", "Coordinator", "Analyst", "Intern"]
```

**Estimated cost:** ~0.5 credits per call, single-page result. One full county ≈ 0.5 credits for employees.

### Recipe B — Verify contact info

```bash
# Work email
deepline plays run prebuilt/name-and-domain-to-email-waterfall \
  --input '{"first_name":"<FN>","last_name":"<LN>","domain":"<DOMAIN>","company_name":"<CO>"}'

# Phone
deepline plays run prebuilt/person-to-phone \
  --input '{"first_name":"<FN>","last_name":"<LN>","domain":"<DOMAIN>"}'
```

**Estimated cost:** 0.6 credits/email + 0.4 credits/phone = ~1.0 credits per fully-verified contact.

### Recipe C — Build TAM for a niche (lenders, SFR operators, anchors)

Use `build-tam` skill. Routes to Apollo + Crustdata + PDL with ICP filters (industry, headcount, geography, role).

**Estimated cost:** $5-15 per TAM (varies with size and ICP specificity).

### Recipe D — LinkedIn URL resolution

Use `linkedin-url-lookup` skill. Routes to multiple providers with identity validation to avoid false positives.

**Estimated cost:** ~0.3 credits per validated URL.

---

## 4. Hybrid Veritas workflow (recommended pattern)

For each target domain in §2:

1. **Discover** — `company-domain-to-linkedin-employees` (Recipe A)
2. **Filter** — keep titles at Director+
3. **Verify emails + phones** — Recipe B per person
4. **Export to CSV** — at `~/wiki/clients/veritas-developments/intelligence/<date>-<domain>-verified.csv`
5. **Generate outreach copy** — via `mcp__leadsniper__generate_email` MCP tool
6. **Write to playbook** — append the verified contacts to `~/wiki/clients/veritas-developments/projects/co-sponsor-gp-target-list.md` (existing target list)

**Always checkpoint the CSV after Step 3**, even if Step 5 is incomplete. If interrupted, the verified CSV must be on disk.

---

## 5. Working directory rules (DO NOT LOSE WORK)

**NEVER write enriched CSVs to `/tmp/`.** System `/tmp/` is wiped on reboot and you'll lose hours of paid enrichment. Always use:

```bash
WORKDIR="~/wiki/clients/veritas-developments/intelligence/"
mkdir -p "$WORKDIR"
# Then export there
```

When a Deepline run completes, the CLI prints a `play page:` URL — paste that URL + the CSV path back to the user so they can open the live spreadsheet.

---

## 6. Cost budgets (veritas-developments has 9.74 credits today, 2026-08-22)

| Workflow | Target | Estimated cost | Status |
|----------|--------|----------------|--------|
| Jackson County full outreach (Recipe A + B × 15 contacts) | Decision-makers at `jacksoncountymo.gov` + `cityofls.net` | ~16 credits (15 × ~1.0 + 0.5 employees × 2 = 16) | **Exceeds budget. Run in 2 phases: Phase 1 = 5 contacts (5 credits). Phase 2 = top-up + 10 more.** |
| KCCLT partnership (Recipe A + B × 3) | `kcclt.org` exec + program | ~3.5 credits | ✓ Affordable |
| SFR operator scoping (Recipe C, TAM) | 50 SFR companies in MO/KS | ~$5-15 (separate budget) | Ask David before running — separate pay-as-you-go cost |
| Lender research (Recipe A + B × 5) | `firstmidwest.com`, `commercebank.com`, `umb.com` construction lending | ~5.5 credits | ✓ Affordable |

**Re-up rule:** when balance <5 credits, the `deepline-credit-monitor` cron (8am daily) sends a Telegram alert to Dennis. Re-up via Deepline dashboard at https://code.deepline.com/billing.

---

## 7. Cross-agent handoff convention

When Claude Code does enrichment in its own session:

1. **Always write the CSV** to `~/wiki/clients/veritas-developments/intelligence/<task>.csv`
2. **Paste the Deepline play URL** + CSV path to the chat
3. **Drop a Honcho conclusion** in workspace `klicksmartai-wiki` summarizing what was enriched

Then next time Hermes gets a question about that client, I (Hermes) will:
- `read_file` the CSV
- OR `deepline runs get <run-id> --full --json` to pull the run output directly
- OR read the Honcho conclusion

---

## 8. Anti-patterns

❌ Don't use `/tmp/` for outputs
❌ Don't fan out without a pilot (2-3 rows first)
❌ Don't pick providers manually — let `deepline-gtm` route (waterfall + cost-aware)
❌ Don't send outreach before verifying work email
❌ Don't paste CSV rows in chat unless asked — always send file path + play URL
❌ Don't ask permission when user already sized the scope ("build me 10 verified leads at KCCLT" = approved)
❌ Don't forget to write a Honcho conclusion at the end of every session

---

## 9. Source skills (already loaded in Hermes)

- `deepline-gtm` — meta-skill, load FIRST
- `build-tam` — TAM building (Apollo + Crustdata + PDL)
- `linkedin-url-lookup` — LinkedIn URL resolution with identity validation
- `niche-signal-discovery` — won-vs-lost ICP signals
- `portfolio-prospecting` — VC portfolio → contact outreach
- `find-qualified-titles` — role holder discovery
- `clay-to-deepline` — Clay migration
- `deepline-pre-research` — pre-research package
- `deepline-monitors` — event-driven monitors
- `deepline-feedback` — bug reports to Deepline team
- `deepline-quickstart` — first-time setup walkthrough

## 10. Source docs

- https://code.deepline.com/docs/quickstart
- https://code.deepline.com/docs/plays/plays-overview
- https://deepline.com/docs/plays/company-domain-to-individual (canonical doc; play name is `company-domain-to-linkedin-employees`)
- https://code.deepline.com/docs/cli-concepts
- https://code.deepline.com/docs/designed-for-agents
- ~/wiki/gtm-engineer-resources/01-data-enrichment/deepline.md (full Deepline reference)

---

**Maintained by:** Hermes (auto-generated 2026-08-22 from getaero-io/gtm-eng-skills pattern). Update on workflow changes.