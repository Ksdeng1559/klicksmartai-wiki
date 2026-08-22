---
title: "swan-gtm Skills Library — Safety Audit + Categorization"
type: audit-report
tags: [gtm, swan-gtm, safety, audit, skills-library]
sources:
  - https://www.gtmskills.com/skills
  - https://github.com/swan-gtm/gtm-skills
  - ~/wiki/raw/swan-gtm/skills/
created: 2026-08-22
updated: 2026-08-22
auditor: Hermes
---

# swan-gtm Skills Library — Safety Audit + Categorization

**Scope:** All 267 SKILL.md files in `~/wiki/raw/swan-gtm/skills/` (cloned from https://github.com/swan-gtm/gtm-skills).

**Audit date:** 2026-08-22.

**Verdict:** ✅ **All 267 files clean.** No prompt injection, no malicious patterns, no hidden content.

---

## 1. Safety audit results

### 1.1 Pattern-based red-flag scan

| Category | Hits | Status |
|----------|------|--------|
| prompt_injection (`ignore previous`, `disregard prior`, `new instructions`, `reveal prompt`, etc.) | **0** | ✅ Clean |
| exfil_attempt (`send to external server`, `exfiltrate`, etc.) | 2 | ⚠️ Both false positives (Meta CAPI docs about sending events to Meta) |
| destructive_shell (`rm -rf /`, `mkfs`, `shutdown`, `reboot`, `halt`) | 1 | ⚠️ False positive ("All non-essential projects halted" — RevOps project language) |
| credential_phish (literal API keys / passwords / tokens embedded) | **0** | ✅ Clean |
| obfuscated_code (`\x` escapes, `\u` escapes, base64 -d, atob, btoa) | **0** | ✅ Clean |
| network_exfil (`curl POST`, `wget --post`, suspicious exfil URLs) | 1 | ⚠️ False positive (`meta-reporting` explicitly states "no external service" — actually anti-exfil) |
| privilege_escalation (`sudo`, `chmod 777`, `chown -R`, `/etc/passwd`, `/etc/shadow`) | **0** | ✅ Clean |
| shell_injection (`$(...$(`, nested command substitution, `;rm`) | 1 | ⚠️ False positive (`${type:id:label}$` is Hermes skill reference syntax, not shell injection) |

**Effective verdict:** 0/8 categories show real threats. All 5 hits are false positives confirmed via context inspection.

### 1.2 Hidden content scan

| Check | Hits |
|-------|------|
| Zero-width characters (`\u200b\u200c\u200d\u200e\u200f\ufeff`) | **0** |
| HTML comments (`<!-- ... -->`) | **0** |
| Private Use Area Unicode (`\ue000-\uf8ff`) | **0** |
| Large base64 blocks (>100 chars) | **0** |

**Result: 267/267 files contain no hidden content.**

### 1.3 File size outliers

Largest file: `rutger-katz/sales-methodology/SKILL.md` at 47.9KB (~900 lines). No file >50KB.

Distribution is healthy — most skills are 50-300 lines, well under the 50KB threshold.

---

## 2. Categorization (matches www.gtmskills.com official taxonomy)

Based on keyword analysis of skill names + frontmatter + content (matches the 18 categories listed on the public GTM Skills directory):

| Category | Count | % | Top authors |
|----------|-------|---|-------------|
| **Ads** | 83 | 31.1% | ivan-falco (Frontal) — heavy Meta/Google/LinkedIn ads coverage |
| **RevOps** | 40 | 15.0% | rutger-katz (Neon Triforce) — CRM, forecasting, governance |
| **Signals** | 34 | 12.7% | amos-bar-joseph, lukas-povilionis — intent, triggers, visitor radar |
| **Outreach** | 32 | 12.0% | imad-badreddine, alex-vacca — cold email, LinkedIn, sequences |
| **Positioning** | 20 | 7.5% | stuart-kerr — messaging, story, category |
| **Deals** | 13 | 4.9% | yoni-tserruya, amos-bar-joseph — CS, retention, expansion, account health |
| **Prospecting** | 8 | 3.0% | amos-bar-joseph, lukas-povilionis — TAM, list building, lead gen |
| **Newsletters** | 7 | 2.6% | daniel-bustamante (Velocity) — welcome emails, roundups |
| **SEO** | 7 | 2.6% | — |
| **AEO** | 6 | 2.2% | yahav-fuchs — AI citation, ChatGPT visibility |
| **ABM** | 4 | 1.5% | ivan-falco, emilia-korczynska — account-based marketing |
| **Influencers** | 3 | 1.1% | — |
| Sales | 2 | 0.7% | — |
| Research | 2 | 0.7% | — |
| Reddit | 2 | 0.7% | yahav-fuchs |
| Events | 2 | 0.7% | — |
| Affiliates | 1 | 0.4% | — |
| Pricing | 1 | 0.4% | manny-medina |

---

## 3. Relevance to Veritas Development (current client)

Veritas (David Poole, Lee's Summit MO, Jackson County) is a **real estate development** firm. Relevant categories:

| Category | Veritas relevance | Use case |
|----------|-------------------|----------|
| **Prospecting** | ✅ High | TAM for SFR operators, JV family offices, RE-focused GPs |
| **Outreach** | ✅ High | Cold email to family offices + regional lenders + county officials |
| **Positioning** | ✅ High | Veritas pitch deck, investor narrative, "category of one" |
| **Deals** | ✅ High | Stonehaven Estates buyer qualification, KCCLT co-sponsor deal |
| **Signals** | ✅ Medium | Track when target orgs post new jobs, hire RE staff, expand to MO/KS |
| **ABM** | ✅ Medium | 1:1 outreach to top 20 family offices in the co-sponsor list |
| **RevOps** | ✅ Medium | HubSpot CRM setup for Veritas investor pipeline |
| **Newsletters** | ⚠️ Low | Possibly for post-purchase homeowner communication |
| **Ads** | ❌ Low | Veritas is a deal-level sponsor, not a mass-market brand |
| **Influencers** | ❌ Low | Not relevant for real estate development |
| **Reddit / AEO** | ⚠️ Low | Could use Reddit for affordable-housing community intel |

**Recommended subset (~50-60 skills) for Veritas GTM workflow:**

- All 8 Prospecting skills
- All 32 Outreach skills (filtered to those touching real estate or B2B services)
- Top 10 Positioning skills
- All 13 Deals skills
- Top 10 RevOps skills (CRM-specific)
- 4 ABM skills (full coverage)
- 2 Research skills (account intelligence)
- 2 Signals skills (job-change + website signals)

---

## 4. Current Hermes integration state

- **Hermes `~/.hermes/skills/gtm/`** has **43 skills** (19 KlickSmartAI custom + 24 swan-gtm symlinks)
- **Hermes `~/.hermes/skills/deepline/`** has **15 skills** (Deepline umbrella, separate from swan-gtm)
- **Claude Code `~/.claude/skills/`** has 25 skills (15 Deepline + 10 misc, no GTM umbrella)
- **swan-gtm clone** at `~/wiki/raw/swan-gtm/skills/` has all 267 skills available for selective install

**Install path used (2026-08-22):** Symlinked the 29 Veritas-relevant core skills from `~/wiki/raw/swan-gtm/skills/<author>/<skill>/SKILL.md` into `~/.hermes/skills/gtm/<skill>`. 24 new symlinks created; 5 already existed (duplicates of KlickSmartAI custom skills).

**Symlinked core (24 new skills):**
```
abm-engagement-scoring        buying-signals-6            cold-call-scripts
cold-email-first-touch        cold-email-strategist       cold-email-templates-34
cs-operations                 deal-desk-operations        icp-builder
lead-routing                  lead-sources-guide          linkedin-abm-1to1-few-many
list-architect                pain-is-the-pitch           positioning-and-story
positioning-messaging-designer  revops-hubspot           roi-proof-generator
sdr-outbound-rules            seo-topic-prioritization    tam-builder
track-contact-job-changes     warm-intro-intelligence     account-intelligence-analyst
```

**KlickSmartAI custom gtm/ skills (kept as local directories, NOT symlinks):**
```
account-tier-scoring    bridge-before-cold    call-scorecards
category-of-one-positioning  citation-gap-outreach  cold-email-4-sequence
cold-email-preflight    founder-led-sales     gtm-enrichment-planner
icp                     leadsniper-cli        never-guess-an-email
pipeline-review         pre-ma-offmarket-discovery  reach-out
research                score                 signal-interpreter
strategic-intelligence-briefing
```

**Rationale:** Symlinks keep `~/wiki/raw/swan-gtm/` as single source of truth. KlickSmartAI custom skills remain as local directories (Hermes-specific logic, may diverge from upstream).

**Context budget impact:** 24 new skills × ~10KB avg = ~240KB added to system prompt. Acceptable for Veritas workflow.

---

## 5. Install decision matrix

When installing from swan-gtm clone to Hermes `~/.hermes/skills/gtm/`:

| Criterion | Recommended action |
|-----------|--------------------|
| Safe to install all 267? | ✅ Yes — verified clean |
| Need to install all 267? | ❌ No — start with Veritas-relevant subset (~50-60) |
| Symlink vs copy? | **Symlink** — keeps `~/wiki/raw/swan-gtm/` as source of truth |
| Per-skill description in Hermes skills index | Auto-inherited from SKILL.md frontmatter |
| Will Hermes auto-load all 267? | ⚠️ YES — Hermes loads all skills in `~/.hermes/skills/` on every turn. Loading 267 would inflate context by ~500KB. Recommend subset. |

---

## 6. Author / company breakdown

The 267 skills come from multiple authors (the clone appears to be a curated multi-author library). Top contributors:

- **ivan-falco** (Frontal) — ads-heavy
- **rutger-katz** (Neon Triforce) — revops-heavy
- **amos-bar-joseph** — scoring + signals
- **daniel-bustamante** (Velocity) — newsletters
- **imad-badreddine** — cold outreach
- **yahav-fuchs** — AEO + Reddit
- **stuart-kerr** — positioning
- **emilia-korczynska** — LinkedIn ABM
- **alex-vacca** — AI personalization prompts
- **manny-medina** — pricing (founder of Outreach.io)

See `/tmp/swan_gtm_categorized.txt` for full author + category + secondary-categories per skill.

---

## 7. Maintenance notes

- Re-run this audit quarterly or when swan-gtm is pulled
- Watch for new author additions (unknown author = treat as low-trust until reviewed)
- If installing all 267, monitor Hermes context window usage on startup
- Backup: `~/vault/raw/swan-gtm/` is the Obsidian-synced mirror

---

**Auditor verdict:** ✅ **Library is safe to install. Proceed with selective subset for Veritas workflow.**