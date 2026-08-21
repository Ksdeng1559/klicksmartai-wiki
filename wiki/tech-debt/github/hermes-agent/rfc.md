# RFC — hermes-agent (NousResearch/hermes-agent)

**Audit date:** 2026-08-15 (Saturday)
**Repo:** https://github.com/NousResearch/hermes-agent
**Reference clone:** ~/wiki/tech-debt/github/hermes-agent (research/reference only — NOT the running install)
**Running install:** ~/.hermes/hermes-agent — **v0.20.1 (2026.8.13), commit `45af7a71`, "Up to date"** (updated this cycle from v0.20.0)

## 1. Git Status

- Reference clone: branch `main`, **16,059 commits behind** origin/main (April 2026 vintage — stale by design, used for reading upstream source)
- Running install commit `45af7a71` **matches origin/main HEAD** — no update available
- Reference clone working tree dirty only with audit artifacts (`rca.md`, `rfc.md` untracked)

## 2. Dependency Health

Project type: **Python (primary, uv.lock ~1MB) + Node (secondary)**.

- `package.json` deps: `@askjo/camofox-browser ^1.5.2`, `agent-browser ^0.26.0`; Node engine >=20
- `uv.lock` — reproducible Python environment; pinned
- Dependabot alerts API: 403 on free plan — **not inspectable**
- The running install is current, so dependency drift in the *reference clone* is immaterial

## 3. CI/CD Pipeline

- Last 5 runs (origin/main, 2026-08-15): 5× `action_required` (approval-gated PR runs) across CI + Docker Build/Test/Publish. No hard failures observed
- Head branches: `fix/windows-restart-loop-guard-20260815`, `contribute/wecom-appmsg-text`, `contribute/gateway-reliability-20260718` — active PR flow
- Status: **healthy**, no failing workflows

## 4. Recent Merged PRs (upstream, via search API — 2026-08-15)

```
#85600 fix: make holographic probe/related/reason use lexical anchor + HRR blend
#87063 fix(terminal): preserve lifecycle guard paths on Windows
#67481 fix(wecom): preserve quoted app message context
#66715 feat(gateway): safely inline Office attachment text
#66709 fix(media): derive cached image suffix from magic bytes
#87061 fix: update nanoid security override
#87060 Feat/engineering foundation
#68848 feat(memory): add explicit_only write mode (#68807)
```

Theme: holographic memory probe/related/reason blend, Windows lifecycle guard, WeCom message context, Office attachment inlining, media cache, nanoid security override, memory explicit_only write mode. All small surgical fixes — no breaking changes relevant to this install.

## 5. Recommended Actions for Claude Code

- [ ] **Nothing to do** — running install is at origin/main HEAD (v0.20.1, updated this cycle). Reference clone intentionally stale; refresh only if reading recent upstream source: `git -C ~/wiki/tech-debt/github/hermes-agent fetch origin && git -C ~/wiki/tech-debt/github/hermes-agent merge --ff-only origin/main`
- [ ] No dependency bumps or PR work needed this cycle

## 6. Risks / Notes

- Reference clone 16,059 commits behind is expected and harmless — do not "fix" by merging (it is not the live install)
- **Gateway restart pending:** the running gateway still executes v0.20.0 code (started 2026-08-14, before this update). It will pick up v0.20.1 on its next natural restart. Restart from an external shell: `systemctl --user restart hermes-gateway`
- `hermes skills update` this cycle: 4 skills updated (baoyu-article-illustrator, pixel-art, yuanbao, polymarket quarantined→scan SAFE→install blocked: 'creative'/'social-media'/'research' are existing skill dirs, not categories — cosmetic upstream packaging quirk, not an error). 5 user-modified bundled skills preserved (claude-design, google-workspace, hermes-agent, hermes-agent-skill-authoring, systematic-debugging)
- NOTE: `hermes skills sync` is NOT a valid subcommand — the correct command is `hermes skills update` (job instruction should be updated)
