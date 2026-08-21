# RFC — graphify (Graphify-Labs/graphify, formerly safishamsi/graphify)

**Audit date:** 2026-08-15 (Saturday)
**Repo:** https://github.com/Graphify-Labs/graphify (safishamsi/graphify redirects here; repo id 1200597263)
**Local clone:** ~/wiki/tech-debt/github/graphify
**Current branch:** v6 (upstream default is now **v8**)
**Local HEAD:** `8a6306f` — make .graphifyignore hermetic (closes #643)
**Remote HEAD (origin/v8):** `7281f27` — chore: bump to 0.9.43
**Local installed binary:** `~/.local/bin/graphify` → **v0.5.0** (graphifyy-0.5.0.dist-info, python3.12 site-packages)

## 1. Git Status

- Branch `v6`, **63 commits behind** origin/v6, **1,195 commits behind** origin/v8
- Local tag level: **v0.6.0**; upstream released through **v0.9.43** (2026-08-15) — 37 release versions ahead
- Working tree dirty only with audit artifacts (`rca.md`, `rfc.md` untracked)

## 2. Dependency Health

Project type: **Python** (setuptools, requires-python >=3.10). Runtime deps: `networkx`, `tree-sitter>=0.23.0`, ~20 language grammar bindings, optional `mcp` extra.

| Package | Constraint | Latest on PyPI | Note |
|---|---|---|---|
| networkx | unpinned | 3.6.1 | fine |
| tree-sitter | >=0.23.0 | 0.26.0 | compatible range |
| mcp (optional) | unpinned | 2.0.0 | v2 is a major; only if mcp extra used |

- **Local install is v0.5.0** — 43 release versions behind upstream (v0.9.43). This is a **security-relevant gap** (see below).
- Dependabot alerts API: 403 on free plan — **not inspectable**, rely on release notes
- **Security-relevant merged fix (June):** #1357 Harden HTML output against U+2028 XSS + crash-on-adversarial-input — local v0.5.0 predates this hardening. **Upgrade is a security-relevant action.**
- **New this cycle:** PR #2755 "Bump pypdf floor past six DoS advisories" — pypdf DoS advisories patched upstream; local v0.5.0 predates this too.

## 3. CI/CD Pipeline

- Workflow: `.github/workflows/ci.yml` — `push` + `pull_request` on branches v1–v4/main, matrix Python 3.10/3.12, `pip install -e ".[mcp,pdf,watch]"`, pytest
- Last 5 runs (2026-08-15): 4× `action_required` (approval-gated PR runs), 1× `success` (`fix/js-external-import-shadow`). **One green run this cycle** — CI is functional when approved.
- The CI workflow triggers on `main`/v1–v4, **not v8** — the active default branch has no CI coverage in the fetched workflow

## 4. Recent Merged PRs (upstream, via search API — 2026-08-15)

```
#2762 Fix SSRF guard rejecting private proxies
#2705 fix: extract nested JS function declarations (#2653)
#2758 fix: an import from outside the corpus must shadow indirect_call resolution
#2754 feat: add Jenkinsfile pipeline extractor
#2755 Bump pypdf floor past six DoS advisories
#2753 fix(install): honor CLAUDE_CONFIG_DIR in always-on CLAUDE.md registration (#2694)
#2744 feat(depth): add `graphify depth` iterative sliding-window build mode
#666 feat: support custom file extensions via GRAPHIFY_EXTENSION_ALIASES
```

Theme: SSRF guard fix, JS function extraction, Jenkinsfile extractor, pypdf DoS bump, depth build mode, custom extensions. Active, healthy upstream.

## 5. Recommended Actions for Claude Code

- [ ] **Upgrade local graphify install from v0.5.0 → v0.9.43** (security: XSS hardening, pypdf DoS bump, 43 releases of fixes). `pip install --upgrade "graphify @ git+https://github.com/Graphify-Labs/graphify.git@v0.9.43"` then `graphify update .` in ~/wiki
- [ ] **Decide branch policy**: local clone sits on v6 (63 behind); upstream default is v8 (1,195 behind). If the clone is used for anything but reference, fast-forward to v8
- [ ] **Re-run `graphify update .`** in ~/wiki after upgrade to refresh `graphify-out/` (wiki AGENTS.md depends on GRAPH_REPORT.md)
- [ ] Confirm `v6` is not a required production branch before abandoning it
- [ ] No draft PR warranted — this is a vendored reference clone, not a fork with push access

## 6. Risks / Notes

- **Repo moved organizations** — any tooling pointing at `safishamsi/graphify` still resolves (redirect) but should be updated to `Graphify-Labs/graphify`
- Local wiki `~/wiki/graphify-out/` exists with GRAPH_REPORT.md, `_polluted_backup`, cache — verify regeneration after upgrade
- CI approval-gated (`action_required`) on most runs — one green run this cycle confirms tests pass on the current head
- Local install (v0.5.0) is **43 releases behind** — the largest dependency gap in this audit
