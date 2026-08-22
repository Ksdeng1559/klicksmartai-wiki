# LeadSniper-3.0 Endpoint Catalog

**Source:** `http://127.0.0.1:8000/openapi.json` (live, fetched 2026-08-22)
**Total routes:** 55
**Auth:** none (open)

---

## Health

| Method | Path | Notes |
|---|---|---|
| GET | `/health` | Top-level liveness |
| GET | `/api/v1/health` | API health check |
| GET | `/api/v1/sgi/health` | SGI subsystem health |

## Root

| Method | Path | Notes |
|---|---|---|
| GET | `/` | Root index (HTML) |
| GET | `/docs` | Swagger UI |
| GET | `/openapi.json` | OpenAPI spec |

---

## Search & discovery

| Method | Path | Summary | Payload |
|---|---|---|---|
| POST | `/api/v1/search` | Search Businesses (Gemini + Maps) | `{niche, city, state, focus, max_results}` |
| POST | `/api/v1/search-decision-makers` | Find decision makers | |
| POST | `/api/v1/search-news` | Search company news | |
| POST | `/api/v1/search-hiring` | Search hiring signals | |
| POST | `/api/v1/reverse-lookup` | Reverse lookup | |
| POST | `/api/v1/social-enrich` | Enrich social profiles | |

### `/api/v1/search` example

Request:
```json
{
  "niche": "coffee roaster",
  "city": "Bellingham",
  "state": "WA",
  "focus": "any",     // "any" | "crisis" | "growth" | "reactivation"
  "max_results": 10
}
```

Response (truncated):
```json
[
  {
    "id": "lead-0-1787383400",
    "businessName": "Camber Coffee",
    "niche": "coffee roaster",
    "city": "Bellingham",
    "rating": 4.7,
    "reviewCount": 798,
    "website": "https://www.cambercoffee.com",
    "phone": "360-656-5343",
    "mapLink": "https://www.google.com/maps/place/Camber+Coffee/...",
    "ownerName": "Andrew, David, Todd (Founders)",
    "uniqueAngle": "...",
    "emailVariants": ["andrew@cambercoffee.com"],
    "bucket": "Premium ($5K+/mo)"
  }
]
```

Note: takes ~60-90s due to Gemini + Maps grounding.

---

## Enrichment

| Method | Path | Summary |
|---|---|---|
| POST | `/api/v1/enrich` | Enrich Lead (Gemini + DataForSEO deep-dive) |
| POST | `/api/v1/enrich-apify` | Enrich Lead Apify |
| POST | `/api/v1/enrich-tavily` | Enrich Lead Tavily |
| POST | `/api/v1/enrich-tavily-full` | Enrich Lead Tavily Full |

All `enrich*` routes require a full `LeadResponse` shape as input — not just a business name.

---

## Content generation

| Method | Path | Summary |
|---|---|---|
| POST | `/api/v1/generate-email` | Generate Email |
| POST | `/api/v1/generate-recommendations` | Generate Recommendations |
| POST | `/api/v1/generate-script` | Generate Cold Call Script |
| POST | `/api/v1/executive-summary` | Generate Executive Summary |
| POST | `/api/v1/analyze-reviews` | Analyze Reviews |

---

## SEO/SGI endpoints (DataForSEO-backed)

These routes use the `SGIContext` schema:
```json
{
  "organizationId": "local-admin",
  "clientId": null,
  "domainId": null,
  "auditId": null,
  "domain": "example.com",
  "country": "US",
  "location": null,
  "language": "en",
  "locationCode": 2840,
  "nearLatitude": null,
  "nearLongitude": null,
  "nearRadiusKm": null,
  "requestedBy": "dennis"
}
```

| Method | Path | Summary |
|---|---|---|
| POST | `/api/v1/sgi/keywords` | Domain Keywords |
| POST | `/api/v1/sgi/domain-overview` | Domain Overview |
| POST | `/api/v1/sgi/competitors` | Competitors |
| POST | `/api/v1/sgi/content-gap` | Content Gap |
| POST | `/api/v1/sgi/content-plan` | Content Plan |
| POST | `/api/v1/sgi/keyword-gap` | Keyword Gap |
| POST | `/api/v1/sgi/cluster-keywords` | Cluster Keywords |
| POST | `/api/v1/sgi/backlink-gap` | Backlink Gap |
| POST | `/api/v1/sgi/cannibalization` | Cannibalization |
| POST | `/api/v1/sgi/money-keywords` | Money Keywords |
| POST | `/api/v1/sgi/research-keyword` | Research Keyword |
| POST | `/api/v1/sgi/zero-volume` | Zero Volume |
| POST | `/api/v1/sgi/local` | Local Search |
| POST | `/api/v1/sgi/drift` | Drift |
| POST | `/api/v1/sgi/voc` | Voc Questions |
| POST | `/api/v1/sgi/audit` | Audit Domain (full, slow) |
| POST | `/api/v1/sgi/audit/quick` | Audit Quick |
| POST | `/api/v1/sgi/audit/deep` | Audit Deep |
| POST | `/api/v1/sgi/audit-triage` | Audit Triage |
| POST | `/api/v1/sgi/client-history` | Client History |
| GET | `/api/v1/sgi/audit/{audit_id}` | Get Audit |
| GET | `/api/v1/sgi/opportunities/{audit_id}` | Get Opportunities |
| GET | `/api/v1/sgi/report/{audit_id}` | Get Report |
| GET | `/api/v1/sgi/signals/{audit_id}` | Get Signals |
| GET | `/api/v1/sgi/budget` | Budget |

### `/api/v1/sgi/keywords` example

Request:
```json
{"domain":"klicksmartai.com","country":"US","locationCode":2840,"language":"en","requestedBy":"dennis"}
```

Response (truncated):
```json
{
  "success": true,
  "organizationId": "local-admin",
  "data": [
    {
      "keyword": "clicksmart",
      "volume": 90,
      "difficulty": 7,
      "competition": "LOW",
      ...
    }
  ]
}
```

### `/api/v1/seo-audit` example

Request: `SGIContext` schema
Response: full audit report

---

## Batch management

| Method | Path | Summary |
|---|---|---|
| POST | `/api/v1/import-batch` | Import Batch (CSV/JSON) |
| POST | `/api/v1/import-batch/preview` | Preview Batch Import |
| POST | `/api/v1/upload-batch` | Upload Batch |
| POST | `/api/v1/batch/{batch_id}/cancel` | Cancel Batch |
| POST | `/api/v1/batch/{batch_id}/retry` | Retry Failed Leads |
| GET | `/api/v1/batches` | List Batches |
| GET | `/api/v1/batch/{batch_id}` | Get Batch Status |
| GET | `/api/v1/batch/{batch_id}/errors` | Get Batch Errors |
| GET | `/api/v1/batch/{batch_id}/leads` | Get Batch Leads |
| GET | `/api/v1/enrichment-queue/stats` | Get Enrichment Queue Stats |

---

## Complete route list (55 total)

```
GET    /
GET    /api/v1/batch/{batch_id}
GET    /api/v1/batch/{batch_id}/errors
GET    /api/v1/batch/{batch_id}/leads
GET    /api/v1/batches
GET    /api/v1/enrichment-queue/stats
GET    /api/v1/health
GET    /api/v1/sgi/audit/{audit_id}
GET    /api/v1/sgi/budget
GET    /api/v1/sgi/health
GET    /api/v1/sgi/opportunities/{audit_id}
GET    /api/v1/sgi/report/{audit_id}
GET    /api/v1/sgi/signals/{audit_id}
GET    /health
POST   /api/v1/analyze-reviews
POST   /api/v1/batch/{batch_id}/cancel
POST   /api/v1/batch/{batch_id}/retry
POST   /api/v1/enrich
POST   /api/v1/enrich-apify
POST   /api/v1/enrich-tavily
POST   /api/v1/enrich-tavily-full
POST   /api/v1/executive-summary
POST   /api/v1/generate-email
POST   /api/v1/generate-recommendations
POST   /api/v1/generate-script
POST   /api/v1/import-batch
POST   /api/v1/import-batch/preview
POST   /api/v1/reverse-lookup
POST   /api/v1/search
POST   /api/v1/search-decision-makers
POST   /api/v1/search-hiring
POST   /api/v1/search-news
POST   /api/v1/seo-audit
POST   /api/v1/sgi/audit
POST   /api/v1/sgi/audit-triage
POST   /api/v1/sgi/audit/deep
POST   /api/v1/sgi/audit/quick
POST   /api/v1/sgi/backlink-gap
POST   /api/v1/sgi/cannibalization
POST   /api/v1/sgi/client-history
POST   /api/v1/sgi/cluster-keywords
POST   /api/v1/sgi/competitors
POST   /api/v1/sgi/content-gap
POST   /api/v1/sgi/content-plan
POST   /api/v1/sgi/domain-overview
POST   /api/v1/sgi/drift
POST   /api/v1/sgi/keyword-gap
POST   /api/v1/sgi/keywords
POST   /api/v1/sgi/local
POST   /api/v1/sgi/money-keywords
POST   /api/v1/sgi/research-keyword
POST   /api/v1/sgi/voc
POST   /api/v1/sgi/zero-volume
POST   /api/v1/social-enrich
POST   /api/v1/upload-batch
```
