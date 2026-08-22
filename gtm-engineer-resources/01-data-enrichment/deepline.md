---
title: Deepline
created: 2026-08-04
updated: 2026-08-22
type: entity
tags: [technology, guide]
sources: [https://deepline.com/docs/quickstart]
---

# Deepline

GTM enrichment SDK + CLI designed for AI agents ("Designed for Agents"). Waterfall provider routing across **97+ integrations** — the first provider to return a valid, verified result wins; you pay only for the successful lookup.

**Position in stack:** contact enrichment layer (work-email discovery, verification). Fills the "Stage C: contact enrichment" gap in outbound pipelines. Named explicitly in the [[lead-sniperai-signal-cold-email-sop]] as the approved contact-waterfall provider — it must **not** define the vertical, signal meaning, qualification logic, or outreach strategy.

## Quickstart (2026-08-04)

**Install** (via coding agent or terminal):
```bash
npm install -g deepline@latest && npm exec --yes --package=deepline@latest -- deepline setup --json
```
- Requires Node.js LTS (system has Node v24 via nvm ✓)
- Agent flow: paste `Set up Deepline in this environment by following https://code.deepline.com/SKILL.md` into Claude Code/Codex/Cursor/Gemini CLI
- Setup installs the `/deepline-gtm` skill into the coding agent and starts **browser OAuth**
- If setup fails: `deepline doctor --json` to diagnose

**Use in Claude Code:**
```
/deepline-gtm Find a verified work email for Jane Smith at Stripe
/deepline-gtm Find 5 CTOs in NYC and get their verified work emails
/deepline-gtm I have a CSV with company names and domains. Find work emails for the VP of Sales at each one.
```
Add "just test on the first 2 rows" for pilot mode before full-file processing.

**CLI (advanced — verified 2026-08-04):**
```bash
# Single lookup — work email from name + domain (waterfall)
deepline plays run prebuilt/name-and-domain-to-email-waterfall \
  --input '{"first_name":"Satya","last_name":"Nadella","domain":"microsoft.com","company_name":"Microsoft"}' --watch

# Batch CSV — same play, native batch mode
deepline plays run prebuilt/name-and-domain-to-email-waterfall-batch \
  --input '{"csv":"/tmp/leads.csv"}' --watch
# CSV columns: FIRST_NAME,LAST_NAME,COMPANY_DOMAIN (+ optional COMPANY_NAME,LINKEDIN_URL)
# Export results: deepline runs export <run-id> --dataset 'result.rows' --out rows.csv

# Inspect a run (billing, providers, audit trail)
deepline runs get <run-id> --full --json
```
> Note: the docs' `deepline tools execute company_to_contact_by_role_waterfall` is **deprecated** — waterfalls now live under `deepline plays run prebuilt/...`. `deepline tools execute` is only for atomic single-provider tools.

## Key facts

- **Founded:** 2024 · NYC · $3.3M pre-seed (Lerer Hippeau, K5 Global)
- **Positioning:** "Clay alternative" — no row limits, BYOK (bring provider keys = no markup), pay-on-match, built-in PostgreSQL for enrichment data
- **Pricing:** free through August 11, 2026, metered after
- **Interfaces:** CLI (recommended for coding agents), MCP server, TypeScript SDK, REST API
- **Pre-built waterfalls:** `name_and_domain_to_email_waterfall`, `person_linkedin_to_email_waterfall`, `company_to_contact_by_role_waterfall` — do NOT chain providers manually
- **Waterfall logic:** single-provider enrichment has coverage gaps; waterfalls query multiple providers in sequence, stop at first valid hit

## Core commands

| Command | Purpose |
|---------|---------|
| `deepline tools list` | Per-tool cost list |
| `deepline tools execute <tool> --payload '{...}'` | Run a waterfall tool |
| `deepline enrich --input leads.csv --output test.csv --name "email-pilot" --rows 0:4 --with '{...}'` | Batch CSV enrichment (pilot on rows first) |
| `deepline billing balance` | Check credits |

**Pitfall:** `--with` payloads require single quotes — double quotes break under shell expansion.

## Local business contact toolkit (verified 2026-08-04)

Deepline covers local/SMB business contact discovery — live-tested on North Vancouver plumbers:

| Capability | Tool | Notes |
|-----------|------|-------|
| Google Maps business search | `openwebninja_localbusiness_search` | `query` field (NOT `keyword`), `limit`, `region`, `extract_emails_and_contacts: true` |
| Map area / nearby search | `openwebninja_localbusiness_search_in_area`, `_search_nearby` | lat/lng + zoom |
| Business details/reviews/posts/photos | `openwebninja_localbusiness_business_details`, `_reviews`, `_posts`, `_photos` | |
| Local SERP | `serper_google_maps_search` (+ batch 100), `dataforseo_serp_google_local_finder_live_advanced` | |
| **SMB owner personal contacts** | **`enformion_contact_enrich`** — personal mobile for SMB owners (restaurants, retail, local services); `enformion_person_search` (personal email+phone from name+city/state); `enformion_workplace_search` | ⭐ The gold for local outreach — but **US-only** (see pitfalls) |
| Business entity lookups | `opensosdata_bulk_lookup` (1,000/run), `openmart_search_businesses`, `icypeas_find_companies`, `forager_organization_search` | |
| Phone validation | Trestle-based phone verify/finder tools | |

**Live test result (5 plumbers, North Vancouver):** full address, phone, website, rating, review count, verified flag on all 5; `extract_emails_and_contacts` pulled `info@pinkplumbing.ca` + social profiles for Pink Plumbing, 10 phone numbers for R&B Plumbing.

**Pitfalls:**
- Search field is `query`, not `keyword` (validation error otherwise)
- Phone numbers come masked (`+160****2603`) in search output unless full contact extraction enabled
- Emails only appear when the business publishes them — use Enformion for owner personal contacts
- **Enformion is US-only**: `city_state` must be `"City, ST"` format (e.g. `"Seattle, WA"`). Canadian lookups (`"North Vancouver, BC"`) fail with `FAILED to parse addressLine2`. For Canadian SMB owners use openwebninja + website extraction instead.
- Enformion business search is separately entitled — may return `isError:true` if the profile lacks Business Search access; fall back to person-search-by-name
- Enformion flow: `enformion_business_search` (get officers + tahoeId) → `enformion_person_search` with `tahoe_id` for exact identity
- Live test (John Smith, Seattle WA): 10 persons, 6 phones (wireless + landline, all connected), 7 personal emails — full consumer skip-trace data
- `opensosdata_bulk_lookup` is US Secretary of State entities only (two-letter US state codes, no Canada)
- **Firmable** (Canada/AU/NZ business data) requires **BYOK** — bring your own API key from the Firmable dashboard; Deepline doesn't provide platform-managed access

## Canada coverage (verified 2026-08-04)

**⭐ Limadata is the Canada-capable provider.** Live-tested on Pink Plumbing Group Ltd. (`pinkplumbing.ca`, North Vancouver):

| Capability | Tool | Result |
|-----------|------|--------|
| Company enrich (CA) | `limadata_enrich_company` (domain or LinkedIn URL) | ✅ Full record: name, domain, founded 2009, 2-10 employees, email `info@pinkplumbing.ca`, tagline, description, LinkedIn (288 followers), HQ address |
| Person phone | `limadata_find_phone` (name + company or LinkedIn URL) | Works (10 credits, charged only on hit); no_result on fake names |
| Work email | `limadata_find_work_email` (name + company_domain) / `_linkedin` | Pattern + LinkedIn-based |
| Personal email | `limadata_find_personal_email` | From LinkedIn/GitHub/X/work email inputs |
| Profiles | `limadata_find_person_profiles`, `limadata_find_company_linkedin` | LinkedIn/GitHub/X resolution |
| Reverse lookup | `limadata_reverse_email_lookup` | Email → LinkedIn/GitHub/X |
| Research | `limadata_research_search`, `limadata_research_extract` | AI web research + clean markdown extraction |

**Canada local-business workflow that works:**
1. `openwebninja_localbusiness_search` (query, region=ca) → business list with phones/addresses/emails
2. `limadata_enrich_company` (domain from step 1) → full firmographic + contact enrichment
3. `limadata_find_work_email` / `find_phone` (owner name + domain) → person-level contacts
4. If the owner has a LinkedIn URL: `limadata_find_personal_email` / `find_phone` via LinkedIn

**Not Canada-capable:** Enformion (US-only), OpenSOSData (US SOS entities), Firmable (BYOK required).

## Hiring-signal toolkit (verified 2026-08-04)

Maps to the LeadSniperAI SOP's **hiring signal family** (Section 4.2: hiring + sales-pipeline development + fulfillment pressure). 75 hiring/job tools available; the verified workflow:

### ⭐ Primary: CrustData V3 Job Search (`crustdata_v3_job_search`)
"Cheap indexed hiring-signal discovery" — best cost/signal ratio, live-tested:

```bash
# Recent sales jobs in Canada (AND filter)
deepline tools execute crustdata_v3_job_search --input '{"filters":{"op":"and","conditions":[{"field":"location.country","type":"=","value":"CA"},{"field":"job_details.title","type":"(.)","value":"sales"}]},"limit":5,"sorts":[{"field":"metadata.date_added","order":"desc"}]}'

# Reposted jobs (repost = repeated posting = stronger signal)
deepline tools execute crustdata_v3_job_search --input '{"filters":{"field":"job_details.reposted_job","type":"=","value":true},"limit":20}'

# Aggregation: count jobs grouped by company (find who's hiring hardest)
# (limit:0 + aggregations [{"type":"group_by","field":"company.basic_info.company_id","agg":"count"}])
```

Filter operators: `=` `!=` `<` `<=` `>` `>=` `in` `not_in` `(.)` substring `[.]` phrase `geo_distance` — filterable fields: title, category, workplace_type, reposted, company name/domain/industries/headcount, location country/state/city, date_added/date_updated.

**Live test:** Canada + "sales" → H&M (AB), Leon's Furniture (BC/ON), The Brick (ON) with dates + source URLs.

### Supporting tools

| Tool | Strength | Input |
|------|----------|-------|
| `predictleads_discover_job_openings` | O*NET profession codes + location | `{"location":"Canada","limit":30}` (live-tested ✅) |
| `predictleads_company_job_openings` | Job openings for a specific company | company URL/domain |
| `theirstack_company_search` | "Finding companies by hiring signals" — job counts per company | `company_country_code_or`, `company_keyword_slug_or` (use company_ prefix!) |
| `theirstack_job_search` | Job postings with company/tech filters | filters object |
| `sentrion_jobs_search` / `company_jobs_search` (+`_historical`) | LinkedIn jobs, up to 6 yrs historical | location/department/keyword |
| `openwebninja_jsearch_search` / `glassdoor_job_search` | Google-for-Jobs + Glassdoor listings | query + location |
| `forager_job_search` (+`_totals`) | Job post event search | event filters |
| `apollo_organization_job_postings` | Apollo job postings per org | 1 credit/page |
| `bloomberry_search_job_postings` | Full-text keyword in job descriptions | keyword + company |
| `leadmagic_jobs_finder` | Job postings by criteria | criteria |
| `sumble_find_jobs` / `find_job_related_people` | Job listings + people related to a job (needs Sumble key) | |
| `datagma_job_change_detection`, `deepline_native.job_change` | Person-level job-change detection (billed only on confirmed move) | contact info |

### ⚠️ Native monitors (the "standing search" ideal)
`deepline_native.company_job_openings`, `company_new_hires`, `contact_job_changes` stream signals into your warehouse + trigger plays — the true automation for the SOP's continuous scanning model. **Currently gated:** "You don't have access to the Monitors feature. Contact the Deepline team to request access."

### SOP integration (hiring-signal family → Signal Report Card)
1. **Standing search** (30-day window, per SOP §8.1): `crustdata_v3_job_search` with `metadata.date_added` filter → capture role, posting date, re-post status, urgency language, source URL
2. **Pipeline-development signals** (60-day): search titles for SDR/BDR/AE/originator/partner-recruitment + `reposted_job:true`
3. **Fulfillment pressure** (60-day): openwebninja Google reviews + Glassdoor reviews via `openwebninja_glassdoor_company_jobs`/reviews
4. **Feed findings into the Signal Report Card** → human GO/HOLD/DROP (per SOP §9)

## Tool & play catalog (verified 2026-08-04)

**2,001 atomic tools** across 15 categories and 97+ providers:

| Category | Tools | Examples |
|----------|-------|----------|
| Admin | 1,109 | CRM/list management, platform admin |
| Outbound tools | 425 | Smartlead, Instantly, Lemlist, Outreach, Salesforge send/sequence ops |
| Research | 205 | DataForSEO, Gong, ad intelligence (Adyntel, Facebook/Google) |
| People enrich | 86 | Apollo, LeadMagic, DropLeads, FullEnrich person enrichment |
| Company search | 71 | Adyntel, company discovery |
| Company enrich | 61 | Apollo org enrich, Aviato |
| People search | 57 | Apollo, AI Ark people search |
| Automation | 49 | Attio, HubSpot workflow ops |
| SMB | 27 | SMB-focused tools |
| Email finder | 21 | Hunter, Findymail, Icypeas, Prospeo, LeadMagic |
| Autocomplete | 15 | Typeahead lookups |
| Email verify | 14 | LeadMagic validation, EmailGuard, Allegrow |
| Phone finder | 11 | Trestle, phone discovery |
| Monitors | 10 | Job-change, signal monitors |
| Phone verify | 2 | Trestle validation |

**Top providers:** emailbison (162), intercom (161), hubspot (114), smartlead (112), attio (104), dataforseo (99), lemlist (99), attention (98), instantly (94), emailguard (89), salesforge (84), gong (66), outreach (58)

**15 prebuilt plays** (waterfalls — the SOP-native workflows):

| Play | What it does |
|------|--------------|
| `name-and-domain-to-email-waterfall` (+ `-batch`) | **Core SOP Stage 6** — verified work email from name + domain, cascades providers |
| `person-linkedin-to-email` (+ `-batch`) | LinkedIn profile URL → verified work email |
| `person-to-linkedin` | Name + company → LinkedIn profile |
| `personal-email` (+ `-batch`) | Personal email finder |
| `personal-email-to-linkedin` (+ `-batch`) | Personal email → LinkedIn profile + identity context |
| `person-to-phone` (+ `-batch`) | Mobile phone via waterfall, Trestle-validated (activity score, carrier, line type) |
| `linkedin-post-to-engagers` | Pull reactors/commenters on a LinkedIn post |
| `engagers-to-icp-qualification` | Score/qualify LinkedIn engagers against an ICP description |
| `company-domain-to-linkedin-employees` | List employees on LinkedIn for a domain |
| `job-change-check` | Detect job changes (billed only on confirmed move) |

**Run pattern:** `deepline plays run prebuilt/<play> --input '{...}' --watch` — single JSON input or `{"csv":"path.csv"}` for batch. Output: durable row dataset + `email_source` provenance + validation flag.

## KlickSmartAI relevance

- Direct fit for the contact-enrichment stage of [[lead-sniperai-signal-cold-email-sop]] (cost-aware enrichment ladder: Stage 6 work-email waterfall, Stage 7 verification)
- Complements [[explorium-ai]] (AI web-research enrichment) — Deepline is the structured people-data waterfall (Apollo-style verified emails/phones/LinkedIn)
- Referenced in the [[swan-gtm-skills]] architecture as the contact data layer

## Docs

- Quickstart: https://deepline.com/docs/quickstart
- CLI concepts: https://deepline.com/docs/cli-concepts
- Designed for agents: https://deepline.com/docs/designed-for-agents
- Docs index (llms.txt): https://deepline.com/docs/llms.txt
- Note: `https://deepline.com/docs/getting-started` 404s — use quickstart instead

## Deepline vs LeadSniper-3.0 enrichment (added 2026-08-22)

LeadSniper-3.0's `enrich_lead` tool calls Gemini + DataForSEO to *generate* lead enrichment (reviews, owner details, email variants). Deepline is a *verification waterfall* that queries 97+ providers (Limadata, Enformion, OpenSOSData, Apollo, etc.) and returns the first hit. Different jobs.

| Need | Use | Why |
|------|-----|-----|
| Local business search (US/CA) | LeadSniper `search_businesses` (Gemini + Maps) | High recall on niche + city |
| Local business search (CA-only) | Deepline `openwebninja_localbusiness_search` + `limadata_enrich_company` | Enformion is US-only; Limadata is Canada-capable |
| Verify a *known* contact's work email | Deepline `name-and-domain-to-email-waterfall` | Multi-provider SMTP check; charged only on hit |
| Verify a *known* contact's mobile | Deepline `person-to-phone` (Trestle-validated) | Live carrier/line-type validation |
| Find decision-makers at a known company | Deepline `company-to-contact-by-role-waterfall` | Single call, multi-provider search |
| Generate business description / sentiment / emails for outreach | LeadSniper `enrich_lead` + `generate_email` | Gemini-generated content, not data lookup |
| SEO / keyword / SERP / domain overview | LeadSniper `sgi_*` (DataForSEO via backend) | Deepline has these too but LeadSniper's bundle is tighter |
| Bulk CSV enrichment (any size) | Deepline `deepline enrich --input leads.csv --output ...` | Native batch mode, BYOK economics |
| Real-time signal (hiring, job-change, news) | Deepline (CrustData, PredictLeads, monitors) | Standing search / monitors |

### Recommended hybrid workflow for one prospect (verified 2026-08-22)

```bash
# 1. Discover businesses (LeadSniper — broader recall via Gemini)
mcp__leadsniper__search_businesses niche="CDFI" city="Bellingham" state="WA" max_results=10

# 2. Verify each owner's work email (Deepline — SMTP-verified, charged only on hit)
deepline plays run prebuilt/name-and-domain-to-email-waterfall \
  --input '{"first_name":"<owner>","last_name":"<last>","domain":"<biz-domain>","company_name":"<biz>"}' --watch

# 3. Find mobile phone if email fails (Deepline — Trestle-validated)
deepline plays run prebuilt/person-to-phone \
  --input '{"first_name":"<owner>","last_name":"<last>","company_name":"<biz>"}' --watch

# 4. Generate personalized email body (LeadSniper — Gemini content)
mcp__leadsniper__generate_email lead=<enriched-lead> context="..."

# 5. Optional: company enrichment (Deepline Limadata for Canada, LeadSniper otherwise)
#    US: LeadSniper enrich_lead is fine
#    CA: deepline tools execute limadata_enrich_company --input '{"domain":"..."}'
```

### Why the split

- **LeadSniper** is best at *generating* outreach content and doing broad search via Gemini + Maps. Email "variants" are guesses (pattern + scrape), not verified.
- **Deepline** is best at *verifying* a known person/company exists and finding their verified work email/phone. Charged only when a provider returns a hit.
- Together: LeadSniper finds the leads, Deepline verifies the contact, LeadSniper writes the email. Lower cost, higher deliverability.

### Cost reference (verified 2026-08-22)

- LeadSniper `enrich_lead`: ~$0.05-0.15 per call (Gemini 2.0 Flash + DataForSEO)
- Deepline `name-and-domain-to-email-waterfall`: ~$0.02-0.08 per verified email (charged only on hit)
- Deepline `person-to-phone`: ~$0.05-0.15 per verified phone (Trestle-validated)
- Deepline `openwebninja_localbusiness_search`: ~$0.005-0.02 per 10 results

See `~/wiki/clients/leadsniper-3.0/` for the full LeadSniper endpoint catalog.
