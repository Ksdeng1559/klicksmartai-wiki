---
name: icm-client-workspace-setup
description: "Scaffold a new client workspace in the KlickSmartAI wiki using the Interpretable Context Methodology (ICM) 3-layer pattern (Identity → Context → Config). Use when the user says 'new client', 'scaffold a client workspace', 'set up client workspace for X', or asks to instantiate the client template for a named company. Generates the full folder tree, IDENTITY.md, CONTEXT.md, CLAUDE.md (Hermes adapter), _config/ (voice/conventions/glossary/compliance), projects/, drafts/, deliverables/, drafts-preview/, skills/ — and routes any first-pass AI output to drafts/, never to projects/ or deliverables/, per the source-of-truth gate. Compatible with both Hermes Agent and Claude Code."
trigger: /icm-client-workspace-setup
author: KlickSmartAI
license: KlickSmartAI internal
version: 1.0.0
platforms: [linux, macos, wsl]
metadata:
  hermes:
    tags: [icm, workspace, scaffolding, client-onboarding, klicksmartai]
    trigger_phrases:
      - "new client workspace"
      - "scaffold a client"
      - "set up client workspace"
      - "create client folder for"
      - "init client workspace"
      - "icm template"
---

# /icm-client-workspace-setup

Scaffold a new client workspace at `/home/denni/wiki/clients/<client-slug>/` using the **Interpretable Context Methodology (ICM)** — KlickSmartAI's 3-layer workspace pattern (Identity → Context → Config) — layered on top of the wiki source-of-truth rule.

> **Glossary (binding for this skill and any conversation that uses the term):**
>
> - **ICM** = **Interpretable Context Methodology** (also called the *Interpretive Context Method* in earlier sessions). A KlickSmartAI internal name for the methodology of building a client workspace as three readable, agent-loadable layers: who the client is (Identity), what's going on with the engagement (Context), and how the workspace is configured for the verticals and compliance modes in play (Config). It is NOT an acronym of "Identity, Context, Config" — those are the *layers* the methodology organizes.
> - **Identity layer** = `IDENTITY.md` (workspace map, stage map, rules, escalation).
> - **Context layer** = `CONTEXT.md` (task routing, 5-stage pipeline, current stage).
> - **Config layer** = `_config/*.md` (voice, conventions, glossary, deliverables, GTM skills, compliance).
> - **Deliverables layer** = `drafts/` → `projects/` → `deliverables/` (source-of-truth gated).
>
> Cite "ICM" alone when you mean the methodology; cite "Identity / Context / Config" when you mean the layers.

Works for **both Hermes Agent** (auto-loads `CLAUDE.md`/`AGENTS.md`/`CONTEXT.md` on folder entry) **and Claude Code** (same progressive-discovery pattern). The folder layout is the contract; both agents see it identically.

## When to use this skill

| User says... | Use this skill? |
|--------------|-----------------|
| "Set up a new client workspace for Acme" | ✅ |
| "Scaffold the client folder for X" | ✅ |
| "I just signed a new client — Y. Build out their wiki space" | ✅ |
| "Apply the ICM template to Z Holdings" | ✅ |
| "Create the KlickSmartAI client folder structure" | ✅ |
| "Where do I put work for a new client?" | ✅ (point to this skill + the template) |
| "Just create a folder called X" (generic) | ❌ use plain `mkdir` |
| "Set up a project under existing client X" | ❌ use that client's IDENTITY.md + CONTEXT.md |

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `client_name` | ✅ | Human-readable client name (e.g. "Acme Ventures") |
| `client_slug` | ✅ | Kebab-case folder slug (e.g. `acme-ventures`) |
| `client_one_line` | ✅ | One-sentence description of the client/engagement |
| `principals` | optional | Comma-separated contacts ("David Poole (CEO), Daniel Bailey (RE)") |
| `engagement_type` | optional | e.g. "deal-loan structure + investor flywheel + CRM build" |
| `compliance_mode` | optional | One of: `none` (default), `securities` (activates Reg D / 506(b) compliance), `privacy` (PII / GDPR), `healthcare` (HIPAA). Set to `securities` if the engagement raises capital. |
| `quick_mode` | default `true` | `true` = flat `projects/` (current Veritas pattern). `false` = per-project subdirectories (Full-mode ICM, used when a pipeline recurs). |
| `verticals` | default `["landing-page","content","email","video-ad","website","deck","lead-magnet","ad-creative","image","doc","tech"]` (or a subset) | Which deliverable types this client uses. Drives the per-vertical folder convention (see `_config/deliverables.md`). If set, the skill generates `drafts/<vertical>/` + `deliverables/<vertical>/` subfolders and corresponding `projects/<vertical>/`. Default = no vertical subfolders. |
| `default_voice` | default `"default"` | One of `default` (evidence-led), `punchy` (ad/landing), `editorial` (long-form/blog), `cold-outreach` (emails). Drives the per-vertical voice inheritance in `_config/deliverables.md`. |
| `gtm_use_cases` | default `[]` | List of GTM use-cases to bind. Valid values: `signal-based-outbound`, `automated-lead-qualification`, `contact-data-enrichment`, `ai-sales-workflow-automation`, `ai-abm-targeting`, `ai-powered-cold-outreach`, `intent-based-prospecting`, `by-role_revops`, `by_role_demand-gen`, `by_role_sales`, `by_role_cro`, `by_role_ai-sdr`. Drives `_config/gtm-skills.md`. Empty = no GTM skills bound (text-only client). |

## Pre-flight

1. **Verify the wiki root:** `test -d /home/denni/wiki/clients` — bail if missing.
2. **Verify the client doesn't already exist:** `test ! -e /home/denni/wiki/clients/<client-slug>/` — if it does, prompt the user; do not clobber.
3. **Verify slug safety:** only `[a-z0-9-]`, kebab-case. Reject uppercase, spaces, underscores. If user gives "Acme Ventures", normalize to `acme-ventures`.
4. **Confirm engagement type** with the user if ambiguous (e.g. capital-raise vs. consulting). This decides `compliance_mode`.

## Workspace tree to generate

```
/home/denni/wiki/clients/<client-slug>/
├── CLAUDE.md              # Hermes + Claude Code entry-point (auto-loaded on folder entry)
├── IDENTITY.md            # ICM Layer 0 — workspace map, stage map, rules, escalation
├── CONTEXT.md             # ICM Layer 1 — task routing + 5-stage pipeline
├── README.md              # human-facing overview (mirrors IDENTITY.md)
├── _config/
│   ├── voice.md           # tone, audience, do/don't
│   ├── conventions.md     # file naming, folder rules
│   ├── deliverables.md    # vertical map + per-vertical Hermes skill binding
│   ├── gtm-skills.md      # GTM use-case → Hermes skill bindings (when gtm_use_cases set)
│   ├── glossary.md        # domain terms
│   └── compliance.md      # only if compliance_mode != 'none'
├── projects/              # validated deliverables (source of truth)
│   └── README.md
├── drafts/                # AI work in progress (pre-HITL) — gate ledger lives here
│   └── README.md
├── deliverables/          # client-ready exports (post-HITL)
│   └── README.md
├── drafts-preview/        # HTML previews of drafts/
│   └── README.md
└── skills/                # client-specific skills (optional, per-vertical adapters)
    └── README.md
```

**If `verticals` is set:** the skill ALSO creates `drafts/<vertical>/`, `drafts-preview/<vertical>/`, `projects/<vertical>/`, and `deliverables/<vertical>/` for each vertical in the list, each with its own `README.md` (use `template-readme-vertical-drafts.md` and `template-readme-vertical-deliverables.md`).

## Implementation steps

### 1. Create the folder tree

```bash
ROOT=/home/denni/wiki/clients/<client-slug>
mkdir -p "$ROOT/_config" "$ROOT/projects" "$ROOT/drafts" \
         "$ROOT/deliverables" "$ROOT/drafts-preview" "$ROOT/skills"

# If verticals set, generate per-vertical subdirectories
if [ -n "$verticals" ]; then
  for v in $verticals; do
    mkdir -p "$ROOT/drafts/$v" "$ROOT/drafts-preview/$v" \
             "$ROOT/projects/$v" "$ROOT/deliverables/$v"
  done
fi
```

### 2. Write the entry-point adapter (`CLAUDE.md`)

This is the file Hermes + Claude Code both auto-load on folder entry. Without it, neither agent picks up the ICM routing. See `references/template-CLAUDE.md` for the exact template — fill in `client_name`, `client_slug`, `compliance_mode`.

### 3. Write the layer files (`IDENTITY.md`, `CONTEXT.md`)

Use `references/template-IDENTITY.md` and `references/template-CONTEXT.md`. Fill in the placeholders from the user's input.

Key edits in CONTEXT.md:
- Default pipeline is **Quick-mode** (`01_intake → 02_research → 03_draft → 04_review → 05_publish`) — virtual stages, no physical folders.
- Only graduate to Full-mode (physical `stages/NN_*/CONTEXT.md` folders) when the user explicitly wants to encode a recurring multi-stage pipeline.

### 4. Write the human overview (`README.md`)

Same content as IDENTITY.md, slightly more compact, plus a table of any known projects. Leave blank if no projects yet.

### 5. Write the `_config/` files

| File | Default content | When to expand |
|------|-----------------|----------------|
| `voice.md` | Direct, evidence-led, no fluff. See `references/template-voice.md`. | After user provides voice direction. |
| `conventions.md` | ICM naming convention + source-of-truth gate. See `references/template-conventions.md`. | Rarely. |
| `deliverables.md` | **Vertical artifact map** — per-vertical folder, file format, default Hermes skill. Required when `verticals` is set. See `references/template-config-deliverables.md`. | Per deliverable type. |
| `gtm-skills.md` | **GTM use-case bindings** — list of bound GTM skills, role mappings, client overrides, HITL gate. Required when `gtm_use_cases` is set. Includes the **universal Deepline CLI routing rule** for enrichment: Hermes + Claude both call `deepline plays` (prebuilt workflows) only — never `deepline tools execute` directly. Providers: `Limadata` (Canada), `Enformion` / `OpenSOSData` (US-only). See `references/template-config-gtm-skills.md`. | Per client GTM profile. |
| `glossary.md` | Empty placeholder ("Add terms as they appear, with sources"). See `references/template-glossary.md`. | As research surfaces new terms. |
| `compliance.md` | **Only if `compliance_mode != 'none'`**. Reg D 506(b) / privacy / HIPAA stub. See `references/template-compliance-securities.md`. | Per regulatory mode. |

### 5b. Runtime resolution pattern (how agents consume `_config/gtm-skills.md`)

`_config/gtm-skills.md` is the **per-client binding**; `gtm-enrichment-planner` (in the GTM skills library) is the **universal orchestration**. The runtime rule:

1. Read `gtm-enrichment-planner` SKILL.md for the **stack layers** (Plan → Discover → Enrich → Score → Outreach), the HITL gate format, the credit-cost estimation model, and the Deepline CLI rule (`plays` only — NEVER `tools execute`, with `Limadata`=Canada, `Enformion`/`OpenSOSData`=US, waterfall per play).
2. Read the client's `_config/gtm-skills.md` for the **bound skill names** per use-case + role, the client-specific overrides (⛔ blocked motions), and the compliance overlay (Reg D 506(b), privacy, etc.).
3. Compose the runtime plan by intersecting the two: layer ordering comes from `gtm-enrichment-planner`; skill names come from the client file.

**Worked example:** agent asked to "build a TAM list of faith-aligned investors for Jackson County MO":

- `gtm-enrichment-planner` says walk Plan → Discover → Enrich → Score → Outreach, $0 Phase 0 first.
- Veritas's `_config/gtm-skills.md` says Signal-Based Outbound binds `buying-signals-6` + `signal-interpreter`; Demand Gen paid ads are ⛔ blocked; Reg D 506(b) overlay required.
- Runtime resolves to: `buying-signals-6 → niche-signal-discovery → signal-interpreter → score → account-tier-scoring → cold-email-first-touch (post-preflight)`.

**Client-specific overrides ALWAYS win.** If the client file says a use-case is ⛔, the agent does not propose it — even if `gtm-enrichment-planner`'s default stack would include it.

### 6. Write the folder-level READMEs

Each of `projects/`, `drafts/`, `deliverables/`, `drafts-preview/`, `skills/` gets a `README.md` describing its purpose and gate. See `references/template-readme-{folder}.md` — these are the same files Veritas has on disk.

**If verticals were set:** also write a per-vertical README into each new `drafts/<vertical>/`, `deliverables/<vertical>/`, `projects/<vertical>/`, and `drafts-preview/<vertical>/` folder using:
- `references/template-readme-vertical-drafts.md` (substitute `<vertical>` and the configured skill binding)
- `references/template-readme-vertical-deliverables.md`

### 7. Verify

```bash
ROOT=/home/denni/wiki/clients/<client-slug>
test -f "$ROOT/CLAUDE.md"          && echo OK || echo MISSING CLAUDE.md
test -f "$ROOT/IDENTITY.md"        && echo OK || echo MISSING IDENTITY.md
test -f "$ROOT/CONTEXT.md"         && echo OK || echo MISSING CONTEXT.md
test -f "$ROOT/_config/voice.md"   && echo OK || echo MISSING voice.md
test -d "$ROOT/drafts"             && echo OK || echo MISSING drafts/
test -d "$ROOT/projects"           && echo OK || echo MISSING projects/
# check no AI output landed in projects/ (source-of-truth gate)
[ -z "$(find "$ROOT/projects" -type f -not -name 'README.md')" ] && echo "source-of-truth gate OK"
```

### 8. Announce

Print a short summary the user can eyeball:

```
✅ Client workspace created at /home/denni/wiki/clients/<client-slug>/
   Files:    CLAUDE.md, IDENTITY.md, CONTEXT.md, README.md
   _config:  voice.md, conventions.md, deliverables.md[, glossary.md][, compliance.md if applicable]
   folders:  projects/, drafts/, deliverables/, drafts-preview/, skills/
   verticals: [<v1>, <v2>, ...]   # if verticals provided
   Gate:     source-of-truth enforced (drafts/ → HITL → projects/ + deliverables/)
   Quick-mode: <yes/no>
```

**Vertical-aware prompt:** if `verticals` was set, also prompt:
- "Want me to seed a voice.md sample for `<vertical>` (e.g. punchy vs editorial)?"
- "Want me to wire a per-vertical VALIDATION_QUEUE.md for the first active vertical?"

Then prompt the user for next step:
- "Want to point me at a first deliverable to seed in drafts/?"
- "Want me to register this client in your CRM / Notion?"
- "Want to graduate to Full-mode ICM with a physical pipeline?"

## The source-of-truth gate (binding)

**Every AI-generated artifact for this client MUST land in `drafts/` first.** Nothing is promoted to `projects/` or `deliverables/` until the user (and, where `compliance_mode=securities`, a qualified reviewer) explicitly approves.

This is enforced:
- by reading `IDENTITY.md` + `CONTEXT.md` at session start (CLAUDE.md binds this)
- by the lack of any other writable path in the skill workflow — the workflow only writes `drafts/` on first pass

If the user requests direct write to `projects/` or `deliverables/`, refuse and explain the gate; offer to put the artifact in `drafts/` instead with a `VALIDATION_QUEUE.md` row that the user can sign off.

## Compatibility — Hermes vs Claude Code

| Aspect | Hermes Agent | Claude Code |
|--------|--------------|-------------|
| Folder entry | Auto-loads `CLAUDE.md`/`AGENTS.md`/`CONTEXT.md` via progressive discovery | Same — `CLAUDE.md` and `AGENTS.md` are auto-loaded |
| Skill entry | `skill_view(name='icm-client-workspace-setup')` or trigger `/icm-client-workspace-setup` | `/icm-client-workspace-setup` (slash command) |
| Discovery | Folder tree + progressive context files | Same |
| HITL gate | User replies "yes" / "send it" / "approve" | Same |
| Source-of-truth | Enforced via CLAUDE.md + this skill | Same (the skill runs identically) |

The folder layout is the contract; both agents see it identically. This skill mirrors the canonical version to both `~/.hermes/skills/icm-client-workspace-setup/` (via the wiki copy at `/home/denni/wiki/hermes/skills/`) and `~/.claude/skills/icm-client-workspace-setup/`.

## Post-scaffold workflow: first SEO audit + cross-reference

If the engagement is SEO-focused and OpenSEO is available (via the `mcp__openseo__*` tools), run this drill **immediately after** step 8. It establishes a baseline, surfaces the real issues, and creates the first `drafts/` artifact + queue row in one motion.

### A. The 7-call sequence (per new SEO client)

1. **`list_projects`** — check if an OpenSEO project already exists for the domain. Two workspaces (`veritas-developments/` and a new one with the same brand) → STOP, ask the user which is canonical.
2. **`create_project`** with `name` + `domain` — captures `projectId` for all later calls.
3. **`run_site_audit`** with `projectId` + `url`. Set `runLighthouse: true` only when Core Web Vitals matter (adds ~3 min). Get `auditId`.
4. **Poll `get_audit_status`** every 30–60s until `status: "completed"`. Crawl phase is fast; Lighthouse is the slow one.
5. **`get_audit_issues`** + **`get_audit_pages`** in parallel — issues are the prioritized report, pages is the full URL+title+wordCount inventory.
6. **`get_domain_overview`** + **`get_backlinks_overview`** in parallel — DataForSEO organic footprint. `hasData: false` is honest output (no data = no presence), not a tool error.
7. **Write the audit as a draft** in the client workspace: `drafts/openseo-site-audit-<domain>-<YYYY-MM-DD>.md` with frontmatter linking to `projectId` + `auditId`. Add row to `drafts/VALIDATION_QUEUE.md` (or `drafts/seo/VALIDATION_QUEUE.md` if the `seo/` vertical is active).

### B. The 6-dimension scorecard

Score each audit on the same template, so a future session can compare clients:

| Dimension | What to check |
|-----------|---------------|
| On-page SEO | H1 present? Title length 50–60? Meta 70–160? Unique per page? |
| Technical SEO | 200 status on all? Sitemap? Canonical? Indexable? Response time? |
| Content | `wordCount` per page from `get_audit_pages`. <300 words = thin. 0 across many pages = JS-render gap, not content gap. |
| Internal link graph | `internalLinkCount` from `get_audit_pages`. 0 outgoing + many orphans = broken nav in HTML. |
| Backlinks / Authority | `referringDomains` from `get_backlinks_overview`. 0 = no profile yet. |
| Local SEO (if applicable) | GBP, citations, NAP consistency — separate call (project context). |

Composite = mean of the 6 scores. **Stage 0** = composite < 20 (foundation missing — no indexable content). **Stage 1** = 20–50 (foundation built, content thin). **Stage 2** = 50–75 (rankable, link-building in progress). **Stage 3** = 75+ (compounding).

### C. The JS-render diagnostic

**Symptom across many pages:** `wordCount: 0` on every page, but unique URLs exist and `inSitemap: true` + `statusCode: 200`. All titles and meta descriptions identical. All pages missing H1. All pages have `internalLinkCount: 0`.

**Diagnosis:** content exists in React/Vue/Svelte/Next runtime, but server-renders an empty shell. The fix is one architectural change (SSR/SSG) that resolves ~95% of issues at once. **Don't recommend 25 separate fixes** — find the single render root cause.

**Verification:** `curl -s https://<domain>/ | wc -w` on the homepage. If <50 words, the diagnosis is confirmed. Compare to the rendered DOM in a browser to see the gap.

### D. Cross-reference pattern: add audit to existing workspace

If the workspace already exists for the client (most common case — Veritas already had one when we audited the LLC domain):

1. **Write the audit `.md`** to `drafts/<vertical>/` (NOT `projects/` — source-of-truth gate).
2. **Add a row to `VALIDATION_QUEUE.md`** with type=`site-audit`, validation owner = the principal, status = `⏳ Awaiting`.
3. **Add a status entry to the bottom** of the same file (date + audit_id + 1-line finding).
4. **Add a permanent record line to `IDENTITY.md`** under the corporate entity — "Web property: <domain> (Stage N SEO, see drafts/...)".
5. **Do NOT** scaffold a new workspace, even if the brand name is similar. Duplicate workspaces = duplicate source-of-truth = a future cleanup tax. Always ask before scaffold if a same-brand workspace exists.

### E. Domain-overview null pattern

`get_domain_overview` returning `organicTraffic: null, organicKeywords: null, backlinks: null, referringDomains: null, hasData: false` is **honest output, not a tool failure**. It means DataForSEO's index has no data for that domain — the site is too new, too low-authority, or deindexed. Same for `referringDomains: { totalCount: 0 }`. Report the nulls as a zero score on that dimension; do not retry, do not "fix" the call.

### F. Paid-MCP pivot — when an audit endpoint sits behind a paid wall

The first SEO audit on a new client often runs into an MCP that needs a paid signup (e.g. Localo for Google Business Profile / citation workflows, On-Page.ai for on-page optimization, BrightLocal for review monitoring, SEMrush APIs, etc.). When a 7-call sequence hits a paid gate, **do not block the audit on it** — pivot to a free, equivalent endpoint and note the deferred upgrade.

**The triage rule (binding):**

1. **Hit a paid MCP wall during audit setup.** Tool returns `402`, redirects to a checkout page, or refuses without an API key bound to a paid plan.
2. **Check the partner / direct-API equivalent before signup.** Most paid MCPs wrap a public API (e.g. Localo → DataForSEO Business Data API; On-Page.ai → DataForSEO On-Page API; BrightLocal → DataForSEO Local Pack). The KlickSmartAI router already has DataForSEO endpoints wired via the OpenSEO MCP, so the pivot is usually zero-cost.
3. **Confirm with Dennis before pivoting.** Single-line ask: *"X is paid. I can pivot to Y (already wired). OK?"* He replies "yes" / "fine" / "do it" → proceed. He replies "we will get that later" / "later" → defer the upgrade, pivot to the equivalent endpoint, and add a row to `drafts/TODO-paid-mcps.md` so the upgrade isn't forgotten.
4. **Document the deferred upgrade in IDENTITY.md** under the corporate entity or web-property row: *"Local SEO scan: deferred (Localo MCP paid). Pivot endpoint: DataForSEO Local Pack via OpenSEO."*
5. **Commit the wire-up change** so future audits don't re-hit the same gate. The pattern (On-Page.ai wired via DataForSEO On-Page endpoint) is captured in commit `8761939` for reference.

**What "deferred" means operationally:** the audit uses the pivot endpoint for the trial / first-touch artifact; the paid MCP is parked in `drafts/TODO-paid-mcps.md` for future upgrade when the client signs or budget clears. Do NOT silently swap endpoints and pretend the paid MCP doesn't exist — that erases the upgrade path.

**Dennis's exact framing (verbatim, from 2026-08-27):**
> *"on page api we have a connection. that is fine you can wire it. localo mcp, is paid. we will get that later"*

Treat "we will get that later" / "parked" / "paid, defer" as the canonical user signal for paid-MCP triage. The pivot endpoint fires immediately; the paid MCP enters the parking lot with a TODO row.

**Why this matters:** the GPC and Veritas audits both hit this gate on different endpoints. Without an explicit triage rule, future agents re-discover the wall, re-ask Dennis, and burn 5–10 min per gate. The pivot also keeps the audit cost low (DataForSEO is per-call micro-cost vs. paid-MCP subscription).

## Pitfalls

1. **Don't write `CONTEXT.md` and skip `CLAUDE.md`** — Hermes won't auto-pick up ICM routing without the adapter file.
2. **Don't bake real engagement details into `_config/glossary.md`** before they exist — it should be a clean starter, not a copy of the last client's data.
3. **Don't seed `drafts/` with placeholders for the user** — that's the user's workspace. Leave it empty; the user will tell you what to draft.
4. **Don't graduate to Full-mode ICM without asking** — most clients stay Quick-mode forever. Only graduate when a recurring pipeline emerges.
5. **Watch for slug collisions** — `acme-ventures` vs `acme_ventures` vs `AcmeVentures` all normalize to the same folder; warn if you see related folders in `clients/` first.
6. **`compliance_mode=securities`** triggers Reg D 506(b) language rules; do NOT write investor-facing copy without consulting `_config/compliance.md`.
7. **Skill-name collision between `~/.hermes/skills/<name>/` and an `external_dirs` mirror causes SILENT TRUNCATION** — when the same skill name exists in both locations, `skill_view` does NOT return "Ambiguous skill name"; it loads the **shorter** copy. A 17,000-char skill at the wiki canonical can collapse to 515 chars from a stale user-level copy. The agent then runs the skill with a tiny subset of its references and silently misses the rest. **Diagnostic:** after publishing or mirroring a wiki skill, run `skill_view(name=<name>)` and compare the returned `name=... (<chars> chars)` against the file size on disk (`wc -c SKILL.md`). If chars don't match (off by >50%), you have a duplicate. **Fix:** `rm -rf ~/.hermes/skills/<name>/` — wiki `external_dirs` is the canonical home. To verify discovery still works: `hermes skills list | grep <name>`. See `references/skill-collision-diagnostic.md` for the full recovery procedure and the `_find_all_skills` semantics.
8. **`CLAUDE.md` is the protected rulebook file** — the safety layer treats edits to it as agent-instruction-file modifications and BLOCKS autonomous writes. **Do not silently edit `CLAUDE.md`.** Surface the proposed diff to Dennis and wait for explicit "yes" / "go" / "approve". `_config/*.md` and `IDENTITY.md` / `CONTEXT.md` are fine to write autonomously; `CLAUDE.md` is not.
9. **Don't auto-migrate legacy flat files into vertical subfolders** — when back-porting verticals into an existing client (e.g. Veritas), the parent `drafts/` / `projects/` / `deliverables/` may already contain validated flat files (e.g. `prime-lees-summit.md`). These are legacy source-of-truth artifacts. Leave them. The new vertical subfolders are for *future* work. State the rule explicitly in `IDENTITY.md` so the agent doesn't try to "clean up."
10. **Empty vertical subfolders may already exist** in legacy client workspaces (e.g. Veritas had them pre-scaffold as `drafts/website/`, `drafts/landing-page/` … but empty). Don't delete them; populate their READMEs from the templates and treat them as part of the layout. Use `ls <folder>/` to detect pre-existing empty subfolders before `mkdir -p`.
12. **For HTML/video deliverables, the `.md` IS the source of truth, not just the artifact spec.** Promote the `.md` to `projects/<vertical>/` alongside the rendered `.html`/`.mp4` in `deliverables/<vertical>/`. Never promote only the rendered artifact — the markdown holds the prompt, brief, and any citations.
13. **`verticals: []` is empty list, not unset** — if the user says "no verticals" they likely mean a research-only client (text deliverables at parent level). Default to no vertical subfolders unless they name a list. Don't over-scaffold.
14. **Hit a paid MCP during audit setup — pivot, don't block.** See section F above. The default is *not* to wait for the user to buy the MCP. Default is to check the equivalent endpoint already in the stack (DataForSEO via OpenSEO covers most cases), ask one-line confirmation ("X is paid, pivot to Y — OK?"), and add a TODO row for the upgrade. The Veritas Localo and On-Page.ai gates are the canonical examples (commits `769b405`, `8761939`).
15. **Don't generate `drafts-preview/<vertical>/` subfolders unless the vertical actually produces HTML** — emails and decks are HTML, but image-only deliverables (ad-creative, logo, PDF) don't need a preview folder. Either skip it or alias it to a generic `build.py` script.
16. **Don't scaffold a duplicate workspace for a same-brand or LLC-renamed client.** Before `mkdir`, search `~/wiki/clients/` for related slugs. If a workspace exists for the same company (e.g. `veritas-developments/` already covered `veritasdevelopmentgroupllc.com`), add the audit to the existing workspace as a draft + queue row + IDENTITY.md note. Do NOT create `veritas-developments-llc/`. Duplicate workspaces = duplicate source-of-truth = future cleanup tax. Always ask the user to confirm which entity is canonical.

17. **Notion share-links are bot-gated from `web_extract`.** Three calls return stubs (593, 593, 1036 chars on different URL variants — verified 2026-08-28). Do not retry — switch to the Notion API. Check `env | grep NOTION_API_KEY` (the `ntn_…` integration token works; the older `NOTION_API_TOKEN` returns 401). Call pattern: `GET https://api.notion.com/v1/blocks/{formatted-page-uuid}/children?page_size=100` with `Authorization: Bearer $NOTION_API_KEY` + `Notion-Version: 2022-06-28`. Paginate on `next_cursor`. The Notion page ID from a share-link must be reformatted with hyphens (`3ca9e94cf0a48165b3c8dff9b439409f` → `3ca9e94c-f0a4-8165-b3c8-dff9b439409f`). Use this path to ingest the **Client Brain Standard** and any other Notion share-link the user pastes. Also applies to the canonical `brindle-guppy-146.notion.site/...` URL — same gate.

18. **CBS (Client Brain Standard) supersedes the older `_config/` pattern for new clients.** As of 2026-08-28, the canonical contract for the knowledge layer of a client workspace is `CLIENT-BRAIN.md` (router) + `context/{BRAND-VOICE,FACTS-AND-CLAIMS,COMPLIANCE,SERVICES-AND-OFFERS,SOURCES,DECISIONS}.md`. See `references/client-brain-standard.md`. For new clients, build on CBS from day one. For existing clients (`veritas-developments/`, `gpc-development/`, `open-seo/`, `veritas-development/`), do NOT bulk-migrate — let it happen on next workspace touch. Old `_config/voice.md`, `_config/glossary.md`, etc. remain valid as content sources for the new `context/*.md` files. Migration is content synthesis, not a file move.

19. **Citation discipline is enforced by the standard, not by the agent's good intentions.** Every load-bearing claim in `context/*.md` must carry `{source, owner, retrieved_at, effective_date, status: Draft|Corroborated|Verified|Counsel Approved, approved_for_external_use, expires_or_reverify_on}`. Bare assertions like "22 years of experience" with no source tag are NOT permitted in client-facing artifacts. The status field is binding: only `Verified` and `Counsel Approved` claims may be quoted externally without further review.

20. **"ICM" is the methodology, NOT an acronym of Identity / Context / Config.** The user corrected this verbatim on 2026-08-28: *"ICM stands for interpretive context method, not identity, context, config."* ICM = **Interpretable Context Methodology** (also called *Interpretive Context Method* in some earlier sessions). It is the **methodology of organizing the workspace into three layers**, not a literal abbreviation of those three layers. Failure mode: an agent that says "ICM = Identity, Context, Config" is conflating the method with its outputs and will get corrected. Correct usage:
    - "ICM workspace" ✓ (methodology applied)
    - "Identity / Context / Config layers" ✓ (the layers)
    - "ICM = Identity, Context, Config" ✗ (wrong — confuses method with output)
    - "the ICM pattern" ✓ (colloquial for the 3-layer pattern)
    Cite ICM when you mean the methodology; cite the layer names when you mean the artifacts.

## Discovery setup (wiki-scoped skills)

If this skill is being published from a wiki repo (e.g. `/home/denni/wiki/hermes/skills/`), Hermes needs to know to look there. Two pieces:

1. **Add the wiki path to `~/.hermes/config.yaml`:**
   ```yaml
   skills:
     external_dirs:
       - /home/denni/wiki/hermes/skills
   ```
   Use `hermes config set skills.external_dirs '["/home/denni/wiki/hermes/skills"]' --force` to write it.
2. **Verify discovery:**
   ```bash
   hermes skills list | grep icm-client-workspace-setup
   ```
   If empty, the loader doesn't see the wiki path. Check `~/.hermes/config.yaml` `skills.external_dirs` block.

**Critical:** if you also copy the skill to `~/.hermes/skills/<name>/` AND register it via `external_dirs`, you get the ambiguous-name error in pitfall #7. Pick one home.

## Verification after skill runs

After running this skill, the user should be able to:
1. `cd /home/denni/wiki/clients/<client-slug>/` and confirm all expected files exist.
2. Open the folder in the Hermes desktop app and have Hermes auto-load the routing.
3. Tell Hermes "draft <thing> for <client-slug>" and have the output land in `drafts/`.
4. See CLAUDE.md reference the right `client_name` / `client_slug` / `compliance_mode`.

## Related skills

| Skill | When |
|---|---|
| `client-onboarding-sprint` | End-to-end SEO client onboarding (this skill + OpenSEO + DuckDB mirror + gatekept audit artifacts in one 5-phase workflow). Use this when the engagement is SEO-focused and you want all artifacts in one sprint. |
| `audit-page-gate` | Gatekeeping discipline for any client-facing SEO report. Use after onboarding produces drafts to validate before sending to the client. |
| `openseo-project-intake` | Just the OpenSEO project setup (no workspace, no audit, no artifacts). Use for clients who already have a workspace but need OpenSEO configured. |
| `openseo-data-export` | Promote drafts to `projects/` + `deliverables/`. Use after Dennis signs off on drafts in `VALIDATION_QUEUE.md`. |
| `d1-to-duckdb-mirror` | The general D1 → DuckDB sync pattern (client-specific scripts live at `~/wiki/clients/<slug>/scripts/sync-<slug>-duckdb.py`). |
| `seo-enrichment-planner` | When client signs and engagement begins — gates credit spend with a HITL approval package before any paid tools fire. |
| `seo-skill-catalog` (in `_config/seo-skill-catalog.md`) | The full 12-skill SEO catalog (Plan → Discover → Enrich → Score → Outreach). Reference for picking which skill to invoke when. |

The **process doc** for this workflow lives at `~/wiki/processes/seo-client-onboarding-sprint.md` — paired with the `client-onboarding-sprint` skill. Update both together.

## References

See the `references/` folder for copy-able templates:
- `template-CLAUDE.md` — Hermes + Claude Code entry-point
- `template-IDENTITY.md` — Layer 0 workspace map + rules
- `template-CONTEXT.md` — Layer 1 routing + pipeline
- `template-voice.md` — voice rules
- `template-conventions.md` — file naming + folder rules
- `template-config-deliverables.md` — **vertical artifact map** (per-vertical folder, file format, default Hermes skill binding)
- `template-config-gtm-skills.md` — **GTM use-case bindings** (per-use-case Hermes skill roster, role mappings, client overrides, HITL gate)
- `template-compliance-securities.md` — Reg D 506(b) compliance
- `template-skills.md` — client-specific skills registry (Skills table)
- `template-readme-projects.md` / `template-readme-drafts.md` / etc. — folder-level READMEs
- `template-readme-vertical-drafts.md` / `template-readme-vertical-deliverables.md` — per-vertical READMEs (when verticals are declared)
- `references/skill-collision-diagnostic.md` — recovery procedure for the silent-truncation bug when a wiki skill is also in `~/.hermes/skills/` (see pitfall #7)
- `references/backporting-existing-clients.md` — procedure for layering new verticals / GTM / compliance onto an already-scaffolded client workspace without disturbing legacy validated artifacts
- `references/client-brain-standard.md` — the **canonical contract** for the knowledge layer of a client workspace (`CLIENT-BRAIN.md` + `context/{BRAND-VOICE,FACTS-AND-CLAIMS,COMPLIANCE,SERVICES-AND-OFFERS,SOURCES,DECISIONS}.md`, 8-tier authority order, Green/Yellow/Red action taxonomy, Notion↔markdown sync). New clients built after 2026-08-28 use this pattern; existing clients migrate on next touch.

## Worked example — First client (text-only deliverables)

User: "Set up a new client workspace for Acme Ventures — they're raising capital for a Houston development."

Hermes does:
```
client_name=Acme Ventures
client_slug=acme-ventures
client_one_line=Houston real-estate developer; current engagement is capital raise for a single-asset project.
principals=Jane Doe (Founder)
engagement_type=capital raise, securities-touching
compliance_mode=securities
quick_mode=true
# verticals: omitted → text-only deliverables
```

Then runs steps 1–8 above, ending with:

```
✅ Client workspace created at /home/denni/wiki/clients/acme-ventures/
   Files:    CLAUDE.md, IDENTITY.md, CONTEXT.md, README.md
   _config:  voice.md, conventions.md, deliverables.md, glossary.md, compliance.md   ← securities mode added compliance.md
   folders:  projects/, drafts/, deliverables/, drafts-preview/, skills/
   Gate:     source-of-truth enforced (drafts/ → HITL → projects/ + deliverables/)
   Quick-mode: yes
```

Next-step prompt is offered to the user.

---

## Worked example — Veritas Development (verticals enabled, full production)

User: "Scaffold the Veritas Development workspace, full vertical mix for an active producer — Jackson County, MO developer, deal-loan, securities-touching."

Hermes does:
```
client_name=Veritas Development Group LLC
client_slug=veritas-developments
client_one_line=Jackson County, MO real-estate developer; deal-loan + investor flywheel + CRM build.
principals=David Poole (Founder & Principal), Daniel Bailey (Co-founder & RE advisor)
engagement_type=Deal-loan structure, investor flywheel (webinars), CRM build
compliance_mode=securities
quick_mode=true
verticals=website,landing-page,content,email,video-ad,ad-creative,deck,lead-magnet
default_voice=default
gtm_use_cases=signal-based-outbound,automated-lead-qualification,contact-data-enrichment,ai-powered-cold-outreach,ai-abm-targeting,intent-based-prospecting,by_role_ai-sdr
```

Then the skill creates:
- Root tree (CLAUDE.md, IDENTITY.md, CONTEXT.md, README.md)
- `_config/{voice,conventions,deliverables,gtm-skills,glossary,compliance}.md` ← `gtm-skills.md` is added because `gtm_use_cases` is non-empty
- `drafts/{website,landing-page,content,email,video-ad,ad-creative,deck,lead-magnet}/` each with `README.md`
- `drafts-preview/{website,landing-page,...,deck,lead-magnet}/` each with `README.md`
- `projects/{website,landing-page,...,deck,lead-magnet}/` each with `README.md`
- `deliverables/{website,landing-page,...,deck,lead-magnet}/` each with `README.md`

`_config/deliverables.md` includes the artifact-type map, listing every vertical with its file format, draft folder, deliverable folder, and the default Hermes skill that produces it. `_config/gtm-skills.md` includes the 7 GTM use-case bindings (each with primary + supporting skills), the role-mappings table, the client overrides table (Veritas says: signal-outbound ✅, cold-outreach ✅, enrichment ✅ via HITL gate, ABM ✅, RevOps/Sales/CRO ⏸️, Demand Gen paid ⛔), and the universal HITL gate.

When the user later says "build the Veritas lead-magnet page for the Co-Sponsor Capital TAM list":
1. Agent reads `CONTEXT.md` → routes to `drafts/lead-magnet/`.
2. `drafts/lead-magnet/` README binds → `lead-magnets` Hermes skill + `_config/deliverables.md` row for `lead-magnet`.
3. Source `.md` goes into `drafts/lead-magnet/tam-co-sponsor-capital-2026-08-22.md`.
4. Generated `.html` lands alongside.
5. `VALIDATION_QUEUE.md` (per-vertical, in the parent `drafts/`) gets a row: file, type=lead-magnet, approvers (Dennis + David for relationship facts), status=pending.
6. On approval: `.md` → `projects/lead-magnet/`, `.html` → `deliverables/lead-magnet/`.

When the user later says "Veritas needs a list of CDFIs to outreach" (GTM use-case: contact-data-enrichment + signal-based-outbound):
1. Agent reads `_config/gtm-skills.md` → finds `contact-data-enrichment` use-case → primary skills `gtm-enrichment-planner` + `find-qualified-titles` + `never-guess-an-email`.
2. Agent invokes `gtm-enrichment-planner` to draft a credit-cost + workflow estimate.
3. Present the plan to Dennis → wait for "yes / proceed."
4. On approval: agent invokes `find-qualified-titles` to source CDFI contacts, then `never-guess-an-email` for verified emails.
5. Results land in `drafts/email/cdfi-list-2026-08-22.md` (not directly in `projects/` — every GTM output is a draft first).
6. Add row to `drafts/VALIDATION_QUEUE.md`: type=email-campaign, requires David + Dennis approval.
7. Run `cold-email-4-sequence` to draft the 7-touch outreach.
8. On approval: `.md` → `projects/email/`, sequence ready in `deliverables/email/`. **Never auto-send.**

---

## Worked example — Acme SaaS (verticals + GTM, subscription client)

User: "Scaffold Acme SaaS — a B2B sales tool. They want content marketing, paid ads, and full RevOps / SDR motion."

Hermes does:
```
client_name=Acme SaaS
client_slug=acme-saas
client_one_line=B2B sales tool; ICP=mid-market RevOps teams; product launch in Q4 2026.
principals=Jane Founder (CEO), Mark CRO
engagement_type=Product launch, demand gen, RevOps build
compliance_mode=none
quick_mode=false
verticals=landing-page,content,email,ad-creative,deck,lead-magnet,doc
default_voice=punchy
gtm_use_cases=signal-based-outbound,automated-lead-qualification,contact-data-enrichment,ai-sales-workflow-automation,ai-abm-targeting,ai-powered-cold-outreach,intent-based-prospecting,by-role_revops,by_role_demand-gen,by_role_sales,by_role_cro,by_role_ai-sdr
```

The skill scaffolds:
- Full vertical folder tree (8 verticals × 4 folders)
- `_config/deliverables.md` (per-vertical skill bindings)
- `_config/gtm-skills.md` (all 12 GTM use-cases bound, all 5 role mappings active)
- `quick_mode=false` means `projects/` has **per-project subdirectories** (Full-mode ICM, for the recurring RevOps build + SDR motion)

When the user says "build Acme's first cold email sequence to RevOps leaders":
1. Agent reads `_config/gtm-skills.md` → finds `ai-powered-cold-outreach` use-case.
2. Primary skills → `cold-email-strategist` + `cold-email-4-sequence` + `reach-out`.
3. Source `.md` → `drafts/email/acme-launch-sequence-2026-08-22.md`.
4. Invoke `cold-email-4-sequence` to generate 7-touch cadence.
5. Add row to `VALIDATION_QUEUE.md`: type=email-sequence, requires Mark CRO + Dennis approval.
6. On approval: `.md` → `projects/email/`, sequence → `deliverables/email/`. No auto-send.
