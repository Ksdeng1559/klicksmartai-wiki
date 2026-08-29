# Veritas — Released Deliverables Preview

Static-HTML preview of files promoted from `drafts/` → `projects/` (HITL-validated, source-of-truth).

| File | What it is | Validation |
|---|---|---|
| `seo-audit-veritasdevelopmentgroupllc-2026-08-28-client.html` | v4 SEO audit, RELEASED 2026-08-28 for David Poole + Daniel Bailey | ✅ Dennis 2026-08-28 |
| `COVER-NOTE-seo-audit-v4-2026-08-28.html` | Cover memo — 60-sec exec summary + 2 decisions | ✅ Dennis 2026-08-28 |

## Relationship to drafts-preview/

- `drafts-preview/` = working hypotheses (NOT source-of-truth)
- `projects-preview/` = HITL-validated source-of-truth (RELEASED)
- The two folders are parallel; promoting a file from `drafts/` → `projects/` also adds it to this preview.

## Regenerate

```bash
python3 build.py
```

Reads from `../projects/` (markdown), writes HTML here. Rebuilds only what the build script lists.
