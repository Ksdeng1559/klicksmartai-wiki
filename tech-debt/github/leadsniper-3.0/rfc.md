# RFC — LeadSniper-3.0 (Ksdeng1559/LeadSniper-3.0, private)

**Audit date:** 2026-08-08 (Saturday)
**Repo:** https://github.com/Ksdeng1559/LeadSniper-3.0 (private)
**Local repo:** ~/LeadSniper-3.0 (branch main, HEAD `0e667cd` — in sync with origin)

## 1. Git Status

- Branch `main`, HEAD `0e667cd` "fix: update Gemini model to gemini-2.5-flash" (Hermes Agent commit, 2026-08-08)
- Working tree **dirty**: modified `.gitignore`, `docker-compose.yml`; untracked `.dockerignore` — uncommitted local changes present

## 2. Dependency Health

- Project type: **Node/TypeScript + Vite** (frontend), Python backend components
- Dependabot alerts API: 403 on free plan — not inspectable
- No dependency outage detected this cycle

## 3. CI/CD Pipeline — **FAILING**

Workflow `.github/workflows/deploy.yml` ("Deploy to Production"), runs on push/PR to main, matrix Node [18.x, 20.x] + lighthouse job.

**Last 5 runs: ALL FAILED — `Deploy to Production | completed | failure`**

| Run | Time | Branch | Head |
|---|---|---|---|
| 31262225100 | 2026-08-08 14:33Z | main | 0e667cd fix: update Gemini model |
| 31261410038 | 2026-08-08 14:13Z | main | ec1542a feat: Review Intelligence pipeline |
| 27068073482 | 2026-06-06 | main | 1abd01a README update |
| 26983118802 | 2026-06-04 | main | 6c65d62 AI fit scoring |
| 26983088266 | 2026-06-04 | main | e680733 failure rules |

**Failure localization (run 31262225100):**
- `build-and-deploy (18.x)` — all steps success, Vercel deploy steps **skipped** (deploy only runs on 20.x)
- `build-and-deploy (20.x)` — all build/test steps success, **`Deploy to Vercel (Production)` step FAILED**
- lighthouse job: skipped

**Root cause (probable):** deploy step (`amondnet/vercel-action@v25`) fails with `secrets.VERCEL_TOKEN` / `VERCEL_ORG_ID` / `VERCEL_PROJECT_ID` on the Node 20.x job. The 18.x job skips deploy by design (`if: github.ref == 'refs/heads/main' && matrix.node-version == '20.x'`), so **production deployments have been failing since at least 2026-06-04** (every run in the visible history). Job log endpoint requires elevated permissions (403) — exact Vercel error message not retrievable with this token.

## 4. Recent Merged PRs / Commits

No PR-based flow on this private repo — direct pushes to main. Last commits:
```
0e667cd fix: update Gemini model to gemini-2.5-flash (Hermes Agent, 2026-08-08)
ec1542a feat: add Review Intelligence pipeline (analyze-reviews endpoint) (Hermes Agent, 2026-08-08)
1abd01a Update README positioning and copyright (Dennis Eng, 2026-06-06)
6c65d62 Add AI employee fit scoring model (2026-06-04)
e680733 Add website failure rules (2026-06-04)
```

## 5. Recommended Actions for Claude Code

- [ ] **CRITICAL: Fix Vercel production deploy** — verify `VERCEL_TOKEN`, `VERCEL_ORG_ID`, `VERCEL_PROJECT_ID` secrets in repo settings; token may be expired/revoked (failing since 2026-06-04). Test locally: `npx vercel whoami` / `npx vercel pull` in ~/LeadSniper-3.0
- [ ] Check Vercel project still exists at the configured project id (`~/.vercel/project.json` present locally)
- [ ] Consider removing the Node 18.x matrix entry (deploy is 20.x-only; 18.x job runs a full redundant build+test cycle) or mirroring the deploy condition
- [ ] Commit or discard local working-tree changes (`.gitignore`, `docker-compose.yml` modified; `.dockerignore` untracked)
- [ ] After fix, re-run deploy workflow (`workflow_dispatch`) and confirm production URL updates

## 6. Risks / Notes

- Production deploy has been **silently failing for ~2 months** — the deployed app is stale (pre-June 4 at best). This is the top-priority finding this cycle
- Local `.vercel/project.json` exists — confirms Vercel CLI was configured locally at some point
- Herpes Agent itself authored the two failing commits today (Gemini model update, Review Intelligence) — the pipeline change is live in git but not in production
