# Methodology-Template Workspaces

A workspace can be a **methodology template / playbook** rather than a single client engagement. Same ICM skeleton (Identity → Context → Config), but the role of the workspace is different: it holds the **reusable procedure** that gets re-applied to many future engagements, not the artifacts of one engagement.

## When the user asks for a methodology template

| User says... | Is it a methodology template? |
|---|---|
| "Scaffold a workspace for Acme — they want SEO + outreach" | ❌ Client workspace — use the standard `icm-client-workspace-setup` flow |
| "Scaffold a workspace for our internal lender-sourcing process" | ✅ Internal playbook — methodology template |
| "Build me a template I can re-use for any future property developer lender-sourcing project" | ✅ External playbook — methodology template |
| "I want a library of capital sources we can match against any new project" | ✅ Methodology template + library |
| "Just create a folder called X" | ❌ Use plain `mkdir` — not a scaffold request |

The signal phrases that indicate a methodology template:
- "for future [X] projects / clients / engagements"
- "template / playbook / library / methodology"
- "we'll re-use this for..."
- "any time we do [X]..."
- "I want a workspace that holds the [X] process itself"

## The 3-layer ICM skeleton still applies

| Layer | Methodology-template version |
|---|---|
| `IDENTITY.md` | Describes the **methodology**, not a client. Sponsor = KlickSmartAI (or the methodology owner). |
| `CONTEXT.md` | Describes **when to enter this workspace** (not the engagement). E.g. "Enter when a new property developer engagement lands." |
| `_config/` | Holds the stable methodology rules (voice, conventions, glossary, compliance). Same as client workspace. |
| `projects/` | **Holds the per-engagement sub-folders** — each future engagement gets its own sub-folder. NOT the validated artifacts of one client. |
| `drafts/` | AI-generated work-in-progress; HITL-gated. Same as client workspace. |
| `deliverables/` | Promoted client-facing outputs. Per-engagement sub-folders (`deliverables/<engagement-slug>/`). |
| `library/` | **The reusable core** — methodology steps, lender profiles, templates, scorecards, scripts. The whole point of a methodology template is the `library/`. |
| `STATUS.md` | Tracks template version + superseded versions (per the standing rule: never auto-delete superseded scripts). |

## Library folder structure

The `library/` is the differentiator. A well-designed methodology template has:

```
library/
├── README.md              # how the library is organized
├── <methodology-folder>/  # the procedure itself
│   ├── README.md          # entry point
│   ├── 01-intake.md       # step 1 of the procedure
│   ├── 02-tam-tiering.md  # step 2
│   ├── 03-scorecard.md    # step 3
│   └── ...                # steps in order
├── <data-folder>/         # data the procedure operates on (e.g. lender profiles)
│   ├── _template-*.md     # empty templates ready to be populated
│   └── _index.csv         # CSV index with column headers
└── <domain-folder>/       # domain-specific depth (e.g. compliance routing)
```

Common `library/` subfolders by methodology type:

| Methodology | Library subfolders |
|---|---|
| Lender sourcing (RE / developer) | `lenders/` (profiles), `capital-stack/` (design templates), `methodology/` (intake → scorecard → outreach → compliance → referral → deliverables) |
| Lead generation (B2B) | `icps/` (profile templates), `channels/` (per-channel playbook), `methodology/` (intake → enrichment → outreach → deliverable) |
| Content production (any vertical) | `topics/` (research templates), `assets/` (boilerplate layouts), `methodology/` (intake → research → draft → review → publish) |

## Population policy

A methodology template is **empty by design** at scaffold time. The library entries get populated by the first engagement that validates them.

**Rules:**

1. **Validate before adding.** A library entry (e.g. lender profile, ICP template) only enters the library if it has been (a) cited from a public source, (b) verified through a deal team / engagement, or (c) confirmed by a subject matter expert.
2. **De-duplicate across roles.** If the same entity appears in multiple library entries (e.g. a law firm is both a referral channel AND a co-sponsor), use one profile with `roles:` in frontmatter.
3. **Date-stamp every entry.** `last_verified:` in frontmatter. Stale (>12 months) = needs re-verification.
4. **Reference cross-workspace data with attribution.** Borrowed data (e.g. lender matrix from another client workspace) must cite its source + the date borrowed, not be auto-ported.
5. **Status values on every entry:** `draft` (initial template) → `validated` (first engagement uses it) → `approved` (Dennis + sponsor sign-off on the pattern).

## Per-engagement sub-folder schema

When a new engagement lands (the first one triggers it; the template defines the pattern), create a sub-folder using the SAME schema the methodology defines. Example: a lender-sourcing methodology says "each new developer project gets `projects/<developer-slug>/` with `01-intake.md`, `02-capital-stack.md`, `03-tam-lender-list.md`, etc." — when the first developer signs, create that sub-folder with empty templates copied from the library.

## How to scaffold a methodology template

1. Use `icm-client-workspace-setup` for the standard scaffold (ID, CONTEXT, _config, projects, drafts, deliverables, drafts-preview, skills).
2. Override the layer files:
   - `IDENTITY.md` → methodology purpose, owner, what it produces
   - `CONTEXT.md` → when to enter, stage transitions for the methodology itself
3. Add `library/` with subfolders matching the methodology's reusable surface.
4. Populate `library/methodology/NN-*.md` (the procedure steps) BEFORE populating data folders — the procedure defines what data is needed.
5. Add `STATUS.md` at root tracking template version.
6. **Do NOT seed `projects/` or `drafts/` with placeholders** — the user will tell you what to draft.
7. Cite any cross-workspace references in `library/README.md` (e.g. "Reference data: `~/wiki/clients/veritas-developments/raw/notion/...` — validate before use").

## Pre-scaffold confirmation questions

Before scaffolding a methodology template, confirm with the user:

1. **Workspace location** — `~/wiki/clients/<slug>/`, `~/wiki/processes/`, or somewhere else?
2. **Slug** — kebab-case name (e.g. `property-developer-lender-sourcing`).
3. **Scope** — single methodology (e.g. "lender sourcing for property developers") or umbrella of multiple methodologies?
4. **Library content** — empty by default, or borrow from an existing client workspace (with attribution)?
5. **Per-engagement schema** — what sub-folders / files does each future engagement create?
6. **Scaffold depth** — (a) standard ICM skeleton + library folder structure only, (b) skeleton + library + first few methodology step templates, (c) full population with borrowed data.

**Default if user just says "scaffold"**: standard ICM skeleton + `library/` folder structure + `library/methodology/` with empty step templates + STATUS.md + cross-workspace reference. Library data folders (e.g. `library/lenders/`) stay empty until first engagement validates entries.

## When to graduate a methodology template

A methodology template is ready to be **promoted from template to operational** when:
1. At least one engagement has used it end-to-end
2. Library data folders have validated entries (not just templates)
3. The user confirms "this is the production version, not a template anymore"

When graduating:
- Update `STATUS.md` with the new version
- Optionally rename the workspace (drop the `-template` suffix if you used one)
- Mark the methodology steps as `validated` not `draft`

## Worked example

User: "Okay save this. Let's create a new workspace" (after working on a property developer lender-sourcing project).

User: "I believe this would be for future property developers"

User: "just template for property developers for now"

User: "scaffold for future use"

Resulting workspace: `~/wiki/clients/property-developer-lender-sourcing/`

Files written:
- Standard ICM skeleton: `IDENTITY.md`, `CONTEXT.md`, `README.md`, `STATUS.md`, `_config/{voice,conventions,glossary,compliance}.md`
- Folder READMEs: `entities/`, `projects/`, `drafts/`, `deliverables/`
- `library/lenders/`: `README.md`, `_template-lender-profile.md`, `_lender-index.csv`
- `library/capital-stack/`: `README.md`, `_capital-stack-template.md`, `_stack-layer-coverage.md`
- `library/methodology/`: `README.md`, `01-intake.md`, `02-tam-tiering.md`, `03-scorecard.md`, `04-outreach-playbook.md`, `05-compliance-routing.md`, `06-referral-channels.md`, `07-deliverables.md`

Cross-workspace reference: `~/wiki/clients/veritas-developments/raw/notion/🏦 🏦 Veritas Capital Markets...md` cited in `library/capital-stack/_stack-layer-coverage.md` as "validate before use."

Status: v0.1, empty library, ready for first engagement.

## Why this pattern is useful

A methodology template:

- **Avoids re-deriving the procedure** every time a new engagement of the same class lands
- **Captures institutional learning** — refinements from one engagement back-port to the methodology
- **Decouples methodology from clients** — borrow patterns across clients without polluting their workspaces
- **Supports compliance routing** — Lane 1-4, Reg D 506(b)/506(c), etc. defined once and re-used
- **Creates a library asset** that can be published, licensed, or sold as a service

## Pitfalls

1. **Don't auto-port cross-workspace data into the library.** Reference it with citation. Validation happens per-engagement.
2. **Don't seed `projects/` or `drafts/` with placeholder engagements.** The first real engagement will populate those.
3. **Don't write methodology step files as if they were validated.** They are templates until first engagement runs.
4. **Don't conflate "methodology template" with "client workspace" in the IDENTITY.md.** The methodology template is owned by KlickSmartAI; per-engagement sub-folders will have their own sponsor.
5. **Don't generate `library/lenders/_index.csv` with rows.** It should be column-headers-only until the first engagement populates it.
6. **Don't skip `STATUS.md` on a methodology template.** The template is versioned like code; supersede, don't delete.
7. **Don't pre-populate lender profiles / ICP templates / content layouts with synthetic data.** "No data" is a valid answer until a real engagement validates the entry.
