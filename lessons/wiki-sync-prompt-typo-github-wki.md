---
type: LESSON
created: 2026-09-29
updated: 2026-09-29
confidence: 0.85
sources: [session cron_a54f3a299daf_20260929_200009]
related: [[wiki-graphify-sync]], [[daily-brain-closing]]
tags: [hermes, cron, wiki, git, bug, prompt-typo]
status: active
---

# Wiki-Sync Cron Prompt Contains Typo: `github-wki` (Should Be `github-wiki`)

**Lesson (2026-09-29, surfaced by Daily wiki push 20:00 cron):**

The `Daily wiki push to GitHub` cron (`a54f3a299daf`) prompt instructs the agent to `git fetch github-wki` and `git merge github-wki/master`. The actual remote name is `github-wiki`. The typo causes:

- `git fetch github-wki` → `fatal: 'github-wki' does not appear to be a git repository`
- `git merge github-wki/master` → `merge: github-wki/master - not something we can merge`

## Why this is non-blocking today

The `origin/master` path (the actual GitHub push via SSH) is **not** affected by the typo, because the prompt correctly uses `git push origin master` in a separate step. The typo only breaks the **local-mirror reconciliation** step against `~/.hermes/wiki-github-wiki`. So:

- GitHub push succeeds → canonical state stays current.
- Local mirror (`~/.hermes/wiki-github-wiki`) drifts silently from local wiki working tree, because the fetch/merge against it silently no-ops.

## Why this could become blocking

If anyone later switches the cron to push via the local-mirror-then-sync-from-local pattern (instead of direct-to-origin SSH), the typo becomes a hard failure. And the silent no-op means nobody notices the drift until someone reads from the mirror expecting canonical state.

## The fix

Either:
1. Patch the cron prompt at `~/.hermes/cron/jobs.json` to replace `github-wki` → `github-wiki`, OR
2. Rename the remote in the wiki repo from `github-wiki` → `github-wki` (matches the prompt; preserves the typo as ground truth).

Option 1 is the right fix — the remote name is the source of truth, the prompt is buggy. Do NOT silently align the world around a typo; fix the prompt.

## Rule

Before scripting `git fetch <remote>` / `git merge <remote>/<branch>` in a cron prompt, verify the remote name with `git remote -v` at the corpus root. Typos in remote names **silently no-op** rather than error visibly — the failure mode is "remote doesn't exist" not "unauthorized."

See [[wiki-graphify-sync]] for the canonical /wiki workflow. See [[daily-brain-closing]] for the routine that flagged this.
