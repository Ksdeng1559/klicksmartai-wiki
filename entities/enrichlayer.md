---
title: EnrichLayer
type: entity
category: platform
url: https://enrichlayer.com
pricing: credit-based
status: active
tags: [entity, enrichment-api, people-data, company-data, jobs-data, linkedin, b2b-data, professional-profiles, python, asyncio, lead-enrichment]
related: [tavily, exa-labs, brave-search-mcp-server, serper, bright-data]
last_reviewed: 2026-04-19
---

# EnrichLayer

**"High-performance data enrichment for people, companies, and jobs — built for concurrency."**

EnrichLayer is a B2B enrichment API that provides structured professional profile data, company records, and job listings via a unified REST API. Designed for high-throughput pipelines — on default rate limits you can enrich up to **432,000 profiles/day**. Acts as the managed scraping + structuring layer between raw web data and your pipeline.

**API:** https://enrichlayer.com/docs | **GitHub:** https://github.com/enrichlayer/enrichlayer-api-py | **PyPI:** `enrichlayer-api`

---

## Key Stats

| Metric | Value |
|--------|-------|
| Professional profiles | 1.2B+ total (790M+ global, 245M US) |
| Company records | 70M+ |
| Job listings | 210M+ |
| Contacts | 216M+ |
| Data points per record | 60+ |
| Monthly update rate | 150M+ records refreshed |
| Default throughput | 432,000 profiles/day (rate-limited) |
| Credit model | 1 credit = 1 successful API call |
| Concurrency | asyncio, gevent, twisted — first-class citizen |

---

## Data APIs

### People API — `person.get()`

Enrich a professional profile from a LinkedIn URL or work email. Returns job history, skills, education, headline, company, and contact data.

```python
from enrichlayer_client.asyncio import EnrichLayer
enrichlayer = EnrichLayer(api_key='your-api-key')
person = enrichlayer.person.get(linkedin_profile_url='https://www.linkedin.com/in/williamhgates/')
```

**Credit cost:** 1 credit / successful request

### Company API — `company.get()`

Enrich a company from domain or name. Returns industry, size, type, location, funding, and hiring activity.

```python
company = enrichlayer.company.get(domain='example.com')
```

**Credit cost:** 1 credit / successful request

### Jobs API — `jobs.get()`

Access 210M+ current job listings. Filter by company, title, function, seniority, employment type.

### Contact API

Find verified email addresses and phone numbers for professionals worldwide.

### School API

Educational institution data — schools, universities, programs.

### Search API

Cross-data-source search with advanced filtering and matching.

---

## EnrichLayer vs Bright Data

| | EnrichLayer | Bright Data |
|--|-------------|-------------|
| **Best for** | Individual lead enrichment | High-volume bulk scraping |
| **Data model** | Structured JSON (60+ fields) | Raw scrape or dataset |
| **LinkedIn profiles** | Structured enrichment via URL | 437+ pre-built scrapers |
| **Cost** | 1 credit/profile | ~$0.05/profile |
| **Throughput** | 432K/day (default rate limit) | High volume with proxy pool |
| **Proxy network** | Not required | 150M+ residential IPs |
| **Datasets** | No pre-collected datasets | Pre-collected dataset option |
| **Python SDK** | ✅ `enrichlayer-api` (PyPI) | ❌ |
| **Concurrency** | asyncio/gevent/twisted native | ❌ |

---

## Installation

```bash
pip install 'enrichlayer-api[asyncio]'
```

```bash
# asyncio
pip install 'enrichlayer-api[asyncio]'
# gevent
pip install 'enrichlayer-api[gevent]'
# twisted
pip install 'enrichlayer-api[twisted]'
```

Authenticate via `ENRICHLAYER_API_KEY` environment variable or pass directly:

```python
enrichlayer = EnrichLayer(api_key='your-api-key')
```

Get an API key at https://enrichlayer.com/auth/register

---

## SDK / API Reference

| Resource | Method | Credit cost |
|----------|--------|-------------|
| Person | `person.get(linkedin_profile_url=...)` | 1 |
| Person bulk | `do_bulk(...)` | 1 each |
| Company | `company.get(domain=...)` | 1 |
| Jobs | `jobs.get(...)` | Varies |
| Contact | `contact.get(...)` | Varies |
| School | `school.get(...)` | Varies |

---

## For KlickSmartAI / HUBERT-X

**Integration point with existing stack:**

1. **GMB discovery → EnrichLayer:** Pass LinkedIn URLs discovered from Google Business Manager listings into EnrichLayer → get structured profile (job history, skills, company, headline)
2. **Feed into 66-Signal Scoring Engine:** Use EnrichLayer fields as signals for PSQ/lead scoring
3. **Exa complement:** Exa handles real-time activity/posts; EnrichLayer handles stable professional profile data
4. **High throughput:** 432K/day default rate limit handles pipeline-scale enrichment

**Pipeline position:**
```
GMB Discovery → EnrichLayer (profile) → PSQ Scoring Engine → HUBERT-X Candidate Ranker
                  ↓
             Exa (real-time activity/posts)
```

**Recommendation:** EnrichLayer is the cleaner fit for per-lead enrichment in the HUBERT-X recruiting pipeline. Bright Data remains relevant for bulk company research (IDC/CSE) or dataset acquisition.

---

## Sources

- https://enrichlayer.com
- https://enrichlayer.com/docs
- https://github.com/enrichlayer/enrichlayer-api-py
- https://pypi.org/project/enrichlayer-api/
