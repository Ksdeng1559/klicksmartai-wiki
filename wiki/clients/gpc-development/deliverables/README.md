# deliverables/

**Client-ready exports — post-HITL.**

HTML, CSV, and any other client-facing artifacts land here after Dennis approves the corresponding draft in `drafts/seo/`.

## Structure

```
deliverables/
└── seo/
    ├── <phase>-<date>-<topic>.html    # client-facing
    ├── <phase>-<date>-<topic>.pdf     # (future) PDF export
    └── csv/                            # DuckDB exports
        ├── v_keyword_metrics_by_project.csv
        ├── v_audit_findings.csv
        └── ...
```

## The gate

Nothing in `deliverables/seo/` unless:
1. The matching Markdown is in `projects/seo/`
2. The HTML was rendered from the validated Markdown (not a draft)
3. CSV exports come from validated DuckDB data (after a project promotion)

## Promotion tool

The `openseo-data-export` skill handles the full promotion:
- `drafts/seo/<artifact>.md` → `projects/seo/<artifact>.md` (source of truth)
- `projects/seo/<artifact>.md` → `deliverables/seo/<artifact>.html` (client-facing)
- DuckDB views → `deliverables/seo/csv/*.csv` (data exports)
- Updates `VALIDATION_QUEUE.md` with `promoted` status + date

## Currently empty

No deliverables yet. First will be the audit quote sheet, after Dennis reviews the draft + approves CLAUDE.md.
