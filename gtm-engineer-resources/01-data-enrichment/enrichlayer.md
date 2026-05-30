# EnrichLayer

**Category:** 01-Data Enrichment
**Status:** ✅ Active
**Entity source:** `/wiki/entities/enrichlayer.md`

---

## At a Glance

**"High-performance data enrichment for people, companies, and jobs — built for concurrency."**

EnrichLayer is a B2B enrichment API providing structured professional profile data, company records, and job listings via a unified REST API. Designed for high-throughput pipelines — on default rate limits you can enrich up to **432,000 profiles/day**. Acts as the managed scraping + structuring layer between raw web data and your pipeline.

---

## Key Specs

| Spec | Detail |
|------|--------|
| **API type** | REST enrichment API (structured output) |
| **Rate limit** | 432K profiles/day default |
| **LinkedIn** | Profile enrichment via URL (structured) |
| **Company data** | Domain → company records |
| **Job data** | LinkedIn job postings, company hiring |
| **Async** | Yes — built for pipeline-scale concurrency |
| **Use for** | Per-lead enrichment, profile enrichment, identity resolution |

---

## GTM Engineering Fit

- **Signal → Enrich pipeline:** After Apify/Explorium detects a signal (new hire, funding, promo), EnrichLayer resolves the contact profile
- **LinkedIn enrichment:** URL → structured name, title, company, history, skills
- **Bulk enrichment:** 432K/day handles pipeline-scale scoring runs
- **vs. Bright Data:** EnrichLayer provides structured output; Bright Data provides raw scraping infrastructure

---

## Client Use Cases

| Client | Use Case |
|--------|---------|
| **Spectra Holdings** | Enrich county-level org contacts (Kulshan CLT pilot) |
| **IDC** | Agent/recruiter profile enrichment |
| **IDF** | High-volume broker enrichment |

---

*Source: `/wiki/entities/enrichlayer.md`*