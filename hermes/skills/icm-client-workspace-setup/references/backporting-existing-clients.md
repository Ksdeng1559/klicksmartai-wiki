# Backporting new bindings into an existing client workspace

Use this procedure when a client (e.g. Veritas Development) has **already been scaffolded** with the basic ICM 3-layer pattern (CLAUDE.md + IDENTITY.md + CONTEXT.md + _config/{voice,conventions,glossary,compliance}.md + projects/drafts/deliverables/drafts-preview/skills) and you now need to **layer new features on top** without disrupting the legacy validated files.

## When to use this

- New `verticals` are added (per-vertical folders + `drafts/<vertical>/` ... )
- New `gtm_use_cases` are added (`_config/gtm-skills.md` generation)
- New `compliance_mode` is enabled (`_config/compliance.md` added/updated)
- `quick_mode` toggles between flat `projects/` and per-project subdirectories
- New `default_voice` is applied across all vertical READMEs

## The 4 invariants (do not violate)

1. **Never move legacy flat files** out of the parent `projects/`, `drafts/`, `deliverables/`. They are validated source-of-truth artifacts. New vertical subfolders sit alongside, never replace.
2. **Never overwrite `CLAUDE.md` silently.** It's the protected rulebook — surface the diff, wait for "yes"/"go"/"approve". (Same goes for any file the safety layer treats as an agent instruction.)
3. **Never auto-write to `projects/` or `deliverables/` from agent work.** All AI output lands in `drafts/` first; promotion goes via `VALIDATION_QUEUE.md`.
4. **Never delete empty subfolders** that already exist. The first backport often finds `drafts/landing-page/` etc. pre-populated-but-empty. Populate their READMEs from `template-readme-vertical-*.md` and move on.

## Step-by-step procedure

### Phase 0 — Inventory the existing workspace

```bash
ROOT=/home/denni/wiki/clients/<client-slug>
ls -la $ROOT/
ls -la $ROOT/_config/
# Pre-existing vertical subfolders?
find $ROOT/{drafts,drafts-preview,projects,deliverables} -maxdepth 2 -type d | sort
# Pre-existing flat files (legacy source-of-truth) at the parent level?
find $ROOT/{drafts,projects,deliverables} -maxdepth 1 -type f | sort
```

Output tells you:
- Which `_config/` files exist (5 vs 6 — do you need `compliance.md` and/or `gtm-skills.md`?)
- Which verticals are already partially scaffolded (empty subfolders)
- Which flat files are legacy source-of-truth (do not move)

### Phase 1 — Create missing dirs only

Use `mkdir -p` for any per-vertical subdir that doesn't exist yet. Do NOT `rm -rf` empty folders — they may be reserved.

```bash
ROOT=/home/denni/wiki/clients/<client-slug>
VERTICALS=(website landing-page content email video-ad ad-creative deck lead-magnet ...)
for v in "${VERTICALS[@]}"; do
  mkdir -p "$ROOT/drafts/$v" "$ROOT/drafts-preview/$v" \
           "$ROOT/projects/$v" "$ROOT/deliverables/$v"
done
```

### Phase 2 — Fill READMEs (idempotent)

For every empty vertical subfolder, copy the README template. Existing READMEs are kept; `cp` is fine for a fresh write — but `cat > README.md <<EOF` or `write_file` is fine too. Use `references/template-readme-vertical-drafts.md` and `references/template-readme-vertical-deliverables.md` from the parent skill.

For every parent folder without a README (`drafts/`, `projects/`, `deliverables/`, `drafts-preview/`, `skills/`), copy `references/template-readme-{folder}.md`.

### Phase 3 — Write / update `_config/` files

For each `_config/` file the skill would have written from scratch:

| File | Backport rule |
|------|---------------|
| `voice.md` | If it already exists with real content, **append** to it via patch — do not overwrite. |
| `conventions.md` | Append-only. |
| `glossary.md` | Append-only. |
| `compliance.md` | If doesn't exist and `compliance_mode != none`, write fresh from `references/template-compliance-securities.md`. If exists, append/extend. |
| `deliverables.md` | If doesn't exist, write fresh from `references/template-config-deliverables.md`. If exists, **merge** — preserve existing rows, add new verticals. |
| `gtm-skills.md` | If doesn't exist, write fresh from `references/template-config-gtm-skills.md`. If exists, **merge** — preserve existing use-case bindings, add new ones. |

### Phase 4 — Update IDENTITY.md and CONTEXT.md (safe)

These are **not** protected. Patch freely:

- `IDENTITY.md`: add the new folder to the tree diagram, add a one-line "## Vertical artifact map" or "## GTM skill bindings" pointer at the bottom.
- `CONTEXT.md`: add a new row to the routing table for the new feature, plus a new section if it's a major addition (e.g. "## GTM skills (per `_config/gtm-skills.md`)").

### Phase 5 — Propose CLAUDE.md diff for user approval

`CLAUDE.md` is the protected rulebook. Build the diff manually:

```bash
diff <(cat $ROOT/CLAUDE.md) <(echo "ADD THIS LINE BLOCK")
```

Surface the diff to the user. **Do NOT auto-apply.** Wait for explicit "yes" / "approve" / "go".

### Phase 6 — Verify and announce

```bash
ROOT=/home/denni/wiki/clients/<client-slug>
test -f "$ROOT/CLAUDE.md"          && echo OK || echo MISSING CLAUDE.md
test -f "$ROOT/IDENTITY.md"        && echo OK || echo MISSING IDENTITY.md
test -f "$ROOT/CONTEXT.md"         && echo OK || echo MISSING CONTEXT.md
# source-of-truth gate still OK (no AI output in projects/)
find "$ROOT/projects" -type f -not -name 'README.md' | head
# legacy flat files preserved?
find "$ROOT/projects" "$ROOT/drafts" "$ROOT/deliverables" -maxdepth 1 -type f | sort
```

Then announce:

```
✅ Backport complete on <client-slug>
   _config:    [+gtm-skills.md, +deliverables.md, ...]
   verticals:  [+website, +landing-page, ...]  # 8 new subfolders × 4 parents = 32 READMEs
   legacy:     preserved (N flat files untouched)
   Pending:    CLAUDE.md diff — awaiting "yes" to apply
```

## Common pitfalls specific to backporting

- **Sibling subagent drift.** When you patch SKILL.md / templates, parallel sessions may edit the same files mid-flight. Always re-read with `read_file` before patching. (The skill's pitfall #7 captures the silent-truncation bug from duplicate user-level copies of the skill itself.)
- **`hermes config set` exit code.** Returns 2 sometimes but the file updates correctly. Always verify via `grep` on the file, not exit code. (Pitfall #7 in the parent skill.)
- **Memory budget.** When patching `_config/*.md` files, watch the memory budget if the patches are large — split into smaller patches.
- **Empty vertical subfolders from earlier runs.** May already exist with stale content (e.g. from an aborted previous attempt). `ls -la` first; decide per-folder whether to overwrite or merge.

## Worked example — Veritas Development (2026-08-22)

Phase 0 inventory:
- `_config/`: voice, conventions, glossary, compliance (4 files — no `deliverables.md`, no `gtm-skills.md`)
- Vertical subfolders: 8 × 4 = 32 (all pre-existed but empty)
- Legacy flat files at parent: ~10 in `projects/` (Prime Lee's Summit, Stonehaven, Co-Sponsor GP target list, growth-program-pilot-plan, etc.); 7 drafts in `drafts/VALIDATION_QUEUE.md`

Phase 1: 0 new dirs needed (all 32 already existed).
Phase 2: 32 per-vertical READMEs + 4 parent READMEs = 36 README writes.
Phase 3: +`deliverables.md` (Veritas-specific artifact-type map, 51 lines); +`gtm-skills.md` (Veritas-specific, 7.6KB).
Phase 4: Patches to IDENTITY.md (folder map + pointer); CONTEXT.md (routing table row + new GTM section).
Phase 5: CLAUDE.md diff surfaced, user said "yes", applied.
Phase 6: Verified.

Total time on disk: ~12 minutes from "yes, we need the client workspace to build websites..." to full GTM-wired production-ready workspace.