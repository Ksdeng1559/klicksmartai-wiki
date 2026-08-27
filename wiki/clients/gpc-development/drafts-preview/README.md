# drafts-preview/

**HTML previews of drafts — same content, styled for review.**

When a skill writes a Markdown draft to `drafts/seo/`, it can also write a styled HTML preview here. This is what you open in your browser to see what the client would receive.

## Structure

```
drafts-preview/seo/
├── <phase>-<date>-<topic>.html      # preview rendered from drafts/seo/<artifact>.md
└── ...
```

## The gate

Preview HTML can be regenerated freely. Same source-of-truth gate applies: a preview here is only a preview of `drafts/seo/`. Once Dennis approves, the canonical HTML lives in `deliverables/seo/`.

## Rendering

Use `scripts/render-report.py` (auto-created by the `openseo-data-export` skill):

```bash
python3 scripts/render-report.py drafts/seo/audit-quote-2026-08-26-gpc-development.md
# Output: drafts-preview/seo/audit-quote-2026-08-26-gpc-development.html
```

The script uses python-markdown with `tables` + `fenced_code` extensions, plus a clean editorial CSS template. View in any browser to see the styled version.

## Currently

| File | Source draft |
|---|---|
| `audit-quote-2026-08-26-gpc-development.html` | (parent `clients/open-seo/drafts/seo/audit-quote-2026-08-26-gpc-development.md`) — will move here once workspace is fully active |
