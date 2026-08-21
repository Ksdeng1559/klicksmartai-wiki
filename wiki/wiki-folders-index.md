---
title: Wiki Folders Index
created: 2026-06-10
updated: 2026-06-10
type: summary
tags: [memory, notes, research]
sources: [https://github.com/Ksdeng1559/klicksmartai-wiki]
---

# Wiki Folders Index

Complete inventory of all folders in the KlickSmartAI wiki, grouped by purpose. Individual files indexed at [[entities-and-projects-index]].

## clients/ — Client Context

Top-level client roster (4 active + 2 historical).

| Client | Folder | Key Files |
|---|---|---|
| **IDC Insurance** | `idc-insurance/` | authority-map.md (10K), business-dna-report.md (6.7K), individual-owned-insurance-asset.md (6K) |
| **Breakthrough Management** | `breakthrough-mgmt/` | README.md (8K), 8 working files (problem-definition 20K, gtm-strategy 16K, grant-eligibility 15K, no-fee-directory 14K, urban-mining-gilbert-interview 9K, field-observations 10K, urban-mining-field-validation 11K) + carbon-credits-initiative/ + urban-mining/ subdirs |
| **Spectra Holdings** | `spectra-holdings/` | overview.md (10K), master-credit-facility-cdfi-strategy.md (15K), deliverables/, projects/ subdirs |
| **WattBricks** | `wattbricks/` | authority-map.md (4.7K), implementation-plan.md (8.4K), topical-authority-plan.md (14K) |
| Byron Chard | (single file) | byron-chard.md (1.3K) |
| Tiyo Energy | (single file) | tiyo-energy.md (1.7K) |
| Insurance Direct Canada | (single file) | insurance-direct-canada.md (1.3K) |

### Breakthrough Management — Grant Funding Focus
Carbon credits, methane, circular economy, urban mining, AI-MRV, infrastructure.
Supports: Non-dilutive capital, SBIR/STTR, EPA/DOE/USDA/EDA screening, APEX/SBDC prep, partner outreach, concept papers, public-private infrastructure funding.

### Spectra Holdings Group — Detail
- **HQ:** Fort Myers, Florida
- **Mission:** Redevelop rural and underserved communities
- **Pillars:** Health, Housing, Economics, Education
- **Flagship Tech:** ICF construction (28-45 days post-permit) + Revvo Central APU (up to 93% electricity reduction)
- **Pipeline:** 20,000+ homes, 10+ US states, 5-year horizon
- **Subsidiary:** Revvo Technology & Energy, Inc.
- **SPE:** Arrowhead Crossings District, LLC (Arrowhead Pointe)

## concepts/ — Conceptual Knowledge (13 files)

| File | Size | Topic |
|---|---|---|
| about-this-wiki.md | 1.2K | Meta: structure, conventions, sources |
| capital-stack-recoverable-grants.md | 22.5K | **Largest concept** - recoverable grant capital stack strategy |
| claude-blog-skill.md | 3.9K | Claude blog generation skill |
| client-acquisition-roadmap.md | 5K | Sabrina's Growth Strategy 101 - zero to first 5 |
| first-100-clients-playbook.md | 12.8K | Cold prospect to loyal customer - test flywheel, secure First Five |
| hermes-agent-setup-guide.md | 2.5K | Self-hosting on VPS (Hostinger KVM 2, $20/mo) |
| insurance-direct-canada-recruitment-agent.md | 3K | IDC recruitment |
| linkedin-lead-enrichment.md | 6.9K | LinkedIn enrichment playbook |
| user-acquisition-roadmap.md | 0B | (empty) |
| wefunder-operating-system.md | 4.5K | Wefunder as Dennis's core operating system + belief mirror |
| wwr-battlecard-format.md | 4.1K | Wealth Wire Radar battlecard format |
| wwr-relationship-manager.md | 6.4K | WWR relationship management |
| wwr-signal-pipeline.md | 4.3K | **9-step pipeline** with 5-engine search fan-out |

### Key concept: First 100 Clients Playbook
- **Core premise:** Show value before asking. Prove before pitch.
- **Psychological barrier:** Founders avoid warm network (fear of judgment)
- **Testimonial flywheel:** High-touch delivery → case study → embed landing pages → refine pitch
- **Pro tip:** Secure the First Five. 5 successful deliveries + 5 testimonials = moral authority to enter cold market.

### Key concept: WWR Signal Pipeline (9 steps)
```
HERMES AGENT (daily 6AM PT cron)
├── wwr_search ─────→ tri_engine_search.py ✅ (Serper + Tavily + Brave fan-out)
├── signal_parser ──→ signal_parser.py ✅ (entity, province, signal_type, signal_date, etc.)
├── wwr_classify ───→ signal_classifier.py ✅ (composite score, tier, clusters)
├── wwr_map_pv ──────→ preliminary_viewpoint_mapper.py ✅ (18-field PV profile, ICP gate)
├── wwr_resolve_identity → Phase 2 (Exa.ai)
```

## reference/ — Reference Material (2 files)

| File | Size | Topic |
|---|---|---|
| hermes-dev-to-prod-implementation-plan.md | 11.9K | Hermes dev → prod implementation |
| mga-advisor-retirement-crisis-problem-definition.md | 3.9K | MGA advisor retirement crisis |

## architecture/agents/ — Architecture (1 file)

`division_based_architecture.md` (1.9K) — Division-Based Agent Architecture
- **Core philosophy:** Shift from Generalist Agent → Division-Based Pipeline
- **Outbound OS example:** Intelligence (Wealth Scout) → Strategy (Persona Architect) → Execution (Copywriter) → Quality (QA Auditor)
- **Design principles:** Atomic Responsibility, Hand-off Protocol, Context Isolation
- **Variations:** Content Engine, Recruitment (Hubert-X), Client Onboarding

## spectra/ — Spectra Context

| Subdir | Key Files |
|---|---|
| `capital-stack/` | capital-stack-recoverable-grants.md (22.5K - same as concepts/) |
| `whatcom-county/` | housing-community-sentiment-report.md (6.5K) |

## hermes/ — Hermes Directives (3 files + 6 skills)

| File | Size | Topic |
|---|---|---|
| directives.md | 1.7K | Two-layer memory, multi-LLM shared knowledge, daily 8PM PST cron, Obsidian vault ID `1b9c01d85dcfdeb7` |
| memory-architecture.md | 0.8K | Ephemeral vs permanent, upgrade triggers |
| skills/ | (dir) | 6 Spectra skills (see entities-and-projects-index) |

## operations/ — Operations (2 subdirs)

| Subdir | Key Files |
|---|---|
| `playbooks/` | local-domination-blueprint.md (5.2K) |
| `vendors/` | digital-marketing-subcontractors.md (2.3K) |

## ops/outreach/ — Outbound Operations

| File | Size | Topic |
|---|---|---|
| agent_specs_outbound_os.md | 5.5K | Outbound OS agent specs |
| cold_email_os.md | 5.5K | Cold email OS |
| `case_studies/` | (subdir) | TBD |
| `production/` | (subdir) | TBD |
| `reports/` | (subdir) | TBD |

## queries/ — Research Queries (1 file)

`wwr-gap19-decision-brief.md` (5.3K) — WWR gap analysis decision brief

## Other Production Folders

| Folder | Purpose | Notes |
|---|---|---|
| `processes/` | Repeatable workflows and SOPs | TBD |
| `gtm/` | Approved go-to-market assets | Empty/not indexed yet |
| `recruitment/` | Approved hiring workflows | TBD |
| `tech-debt/` | Known issues to address | TBD |
| `strategic/` | Strategic planning docs | TBD |
| `templates/` | Document templates | TBD |
| `notes/` | General notes | TBD |
| `morning-briefings/` | Daily briefing templates | TBD |
| `census/` | Census data | TBD |
| `clips/` | Clipped content | TBD |
| `commercial-relationships/` | Business relationships | TBD |
| `drafts/` | Work-in-progress docs | TBD |
| `raw/` | Source material and drafts | Immutable |
| `graphify-out/` | Generated graph output only | Output dir |
| `sbir/` | SBIR grant material | TBD |
| `rios/` | RIOS project | TBD |
| `grantfunding/` | Grant funding knowledge | TBD |
| `GrantFundingAI/` | Grant funding AI project | TBD |
| `gtm-engineer-resources/` | GTM engineering resources | TBD |
| `wiki/` | Sub-wikis | TBD |
| `SpectraHoldings/` | Spectra content (alt casing) | TBD |
| `Spectraholdings/` | Spectra content (alt casing) | TBD |
| `_meta/` | Metadata (hook logs) | TBD |

---

# Related Wiki Structure Pages

- [[klicksmartai-wiki-architecture]] — Master repo architecture, branch governance, sync sequence
- [[entities-and-projects-index]] — Master entity & project index
- [[context7]] — Upstash Context7 setup for future installs
- [[klick2client-os]] — B2B acquisition OS framework
- [[hermes-agent]] — Local Hermes Agent setup

# Related Project Folders

- `clients/idc-insurance/` — Active client, $2B+ coverage sold
- `clients/breakthrough-mgmt/` — Grant funding package
- `clients/spectra-holdings/` — CDFI capital strategy
- `clients/wattbricks/` — Topical authority plan
- `concepts/` — Strategic playbooks and frameworks
- `reference/` — Implementation plans

---

# Last Updated

2026-06-10 — Initial inventory from github.com/Ksdeng1559/klicksmartai-wiki
