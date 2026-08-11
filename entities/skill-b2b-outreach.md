---
title: b2b-outreach-intelligence-pipeline (skill)
created: 2026-08-11
updated: 2026-08-11
type: entity
tags: [entity, skill, gtm, outreach, intelligence, b2b]
sources: []
confidence: high
---

# b2b-outreach-intelligence-pipeline (skill)

**Second-most-loaded skill (440 uses).** The umbrella skill for B2B
outreach research + intelligence assembly + draft production. Used heavily
in Spectra Holdings MCF outreach workflows.

## Trigger
Any request to research a target account, build an outreach brief, generate
a draft email for an investor / executive / partner, or assemble a sector
intelligence pack.

## Source
`~/.hermes/skills/research/b2b-outreach-intelligence-pipeline/`

## What it produces
- Account / company intelligence files (entities, contacts, signals).
- Outreach draft emails (HITL — drafts only, never auto-sent).
- Sector intelligence reports (faith / CDFI / municipal focus for Spectra).
- Lead list outputs that feed into [[Skill-Deepline]] for verified-email
  enrichment.

## Relationship to other skills
- Calls [[Skill-Tavily-Agent-Skills]] and [[Search-Provider-Rotation]]
  for discovery.
- Feeds [[Gtm-Enrichment-Hitl-Gate]] — every outreach draft is presented
  to Dennis before any send.
- Often used together with [[Entity-Spectra-Pipeline]].

## See also
- [[Entity-Spectra-Pipeline]] — Spectra-specific umbrella
- [[Search-Provider-Rotation]]
- [[Gtm-Enrichment-Hitl-Gate]]