---
title: GitHub Access Pattern
created: 2026-08-11
updated: 2026-08-11
type: pattern
tags: [pattern, github, environment, gotcha]
sources: []
confidence: high
---

# GitHub Access Pattern

How to talk to GitHub from this machine. **Don't use `gh` CLI or `.netrc` — they
don't work in this setup.**

## Auth
- **PAT** lives at `~/.hermes/github-pat.txt` (mode 600, owned by `denni`).
- **Account:** `Ksdeng1559`, free tier.
- **Use:** `Authorization: token <PAT>` header on every GitHub API call via
  curl. Not `Bearer`.

## Commands
```bash
# Read a file via the API
curl -sH "Authorization: token $(cat ~/.hermes/github-pat.txt)" \
  https://api.github.com/repos/OWNER/REPO/contents/PATH

# Issue / PR operations
curl -sH "Authorization: token $(cat ~/.hermes/github-pat.txt)" \
  -X POST https://api.github.com/repos/OWNER/REPO/issues \
  -d '{"title":"...","body":"..."}'

# GraphQL
curl -sH "Authorization: token $(cat ~/.hermes/github-pat.txt)" \
  -H "Content-Type: application/json" \
  -X POST https://api.github.com/graphql \
  -d '{"query":"..."}'
```

## What doesn't work
- `gh auth login` → produces a token that is NOT valid for Copilot API.
- `gh pr create` / `gh issue create` → not configured.
- `.netrc` → not present; git push over HTTPS will prompt.

## When this is the right answer
- Any task that needs to read/write issues, PRs, repo contents, or Actions
  via API.
- Cloning public repos via `git clone https://github.com/...` works WITHOUT a
  token (anonymous).

## See also
- [[Api-Keys-And-Providers]]
- [[Hermes-Environment-Map]]