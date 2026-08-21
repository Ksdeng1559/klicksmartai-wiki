
# TestSprite AI Testing Report(MCP)

---

## 1️⃣ Document Metadata
- **Project Name:** LeadSniper-3.0
- **Date:** 2026-01-15
- **Prepared by:** TestSprite AI Team

---

## 2️⃣ Requirement Validation Summary

#### Test TC001 test_business_search_api_with_valid_niche_and_city
- **Test Code:** [TC001_test_business_search_api_with_valid_niche_and_city.py](./TC001_test_business_search_api_with_valid_niche_and_city.py)
- **Test Error:** Traceback (most recent call last):
  File "<string>", line 32, in test_business_search_api_with_valid_niche_and_city
  File "/var/task/requests/models.py", line 1024, in raise_for_status
    raise HTTPError(http_error_msg, response=self)
requests.exceptions.HTTPError: 500 Server Error: Internal Server Error for url: http://localhost:8000/api/v1/search

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/var/task/handler.py", line 258, in run_with_retry
    exec(code, exec_env)
  File "<string>", line 71, in <module>
  File "<string>", line 34, in test_business_search_api_with_valid_niche_and_city
AssertionError: Request to Business Search API failed: 500 Server Error: Internal Server Error for url: http://localhost:8000/api/v1/search

- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/0f01e6d1-cbfa-40a2-9390-f5d861c22c2d/34860e82-8edc-4c9b-b01e-4fb99dd28f1a
- **Status:** ❌ Failed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC002 test_lead_enrichment_api_aggregates_data_correctly
- **Test Code:** [TC002_test_lead_enrichment_api_aggregates_data_correctly.py](./TC002_test_lead_enrichment_api_aggregates_data_correctly.py)
- **Test Error:** Traceback (most recent call last):
  File "/var/task/handler.py", line 258, in run_with_retry
    exec(code, exec_env)
  File "<string>", line 74, in <module>
  File "<string>", line 32, in test_lead_enrichment_api_aggregates_data_correctly
AssertionError: Unexpected status code: 422

- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/0f01e6d1-cbfa-40a2-9390-f5d861c22c2d/28ed69e0-6845-4762-a93a-448de3aee3b7
- **Status:** ❌ Failed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC003 test_batch_import_api_validates_and_processes_csv
- **Test Code:** [TC003_test_batch_import_api_validates_and_processes_csv.py](./TC003_test_batch_import_api_validates_and_processes_csv.py)
- **Test Error:** Traceback (most recent call last):
  File "<string>", line 76, in test_batch_import_api_validates_and_processes_csv
AssertionError: Import request failed with status 400

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/var/task/handler.py", line 258, in run_with_retry
    exec(code, exec_env)
  File "<string>", line 138, in <module>
  File "<string>", line 81, in test_batch_import_api_validates_and_processes_csv
AssertionError: Batch import submission failed: Import request failed with status 400

- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/0f01e6d1-cbfa-40a2-9390-f5d861c22c2d/08dcc8f3-abf6-4ce0-a641-ca76d2fbd0b4
- **Status:** ❌ Failed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC004 test_batch_management_api_handles_batch_jobs
- **Test Code:** [TC004_test_batch_management_api_handles_batch_jobs.py](./TC004_test_batch_management_api_handles_batch_jobs.py)
- **Test Error:** Traceback (most recent call last):
  File "/var/task/handler.py", line 258, in run_with_retry
    exec(code, exec_env)
  File "<string>", line 84, in <module>
  File "<string>", line 26, in test_batch_management_api_handles_batch_jobs
AssertionError: Import batch failed with status 400

- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/0f01e6d1-cbfa-40a2-9390-f5d861c22c2d/8bae89fc-6529-426c-b743-509f911342d6
- **Status:** ❌ Failed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC005 test_social_enrichment_api_returns_valid_profiles
- **Test Code:** [TC005_test_social_enrichment_api_returns_valid_profiles.py](./TC005_test_social_enrichment_api_returns_valid_profiles.py)
- **Test Error:** Traceback (most recent call last):
  File "<string>", line 36, in test_social_enrichment_api_returns_valid_profiles
AssertionError: Unexpected status code: 422

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/var/task/handler.py", line 258, in run_with_retry
    exec(code, exec_env)
  File "<string>", line 70, in <module>
  File "<string>", line 68, in test_social_enrichment_api_returns_valid_profiles
AssertionError: Social Enrichment API test failed for payload {'businessName': 'Example Corp', 'website': 'https://www.example.com'}: Unexpected status code: 422

- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/0f01e6d1-cbfa-40a2-9390-f5d861c22c2d/2c51ddac-e872-4fb9-92e2-83fea3ff06d4
- **Status:** ❌ Failed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC006 test_seo_audit_api_provides_keyword_and_competitor_analysis
- **Test Code:** [TC006_test_seo_audit_api_provides_keyword_and_competitor_analysis.py](./TC006_test_seo_audit_api_provides_keyword_and_competitor_analysis.py)
- **Test Error:** Traceback (most recent call last):
  File "<string>", line 18, in test_seo_audit_api_provides_keyword_and_competitor_analysis
  File "/var/task/requests/models.py", line 1024, in raise_for_status
    raise HTTPError(http_error_msg, response=self)
requests.exceptions.HTTPError: 422 Client Error: Unprocessable Content for url: http://localhost:8000/api/v1/seo-audit

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/var/task/handler.py", line 258, in run_with_retry
    exec(code, exec_env)
  File "<string>", line 43, in <module>
  File "<string>", line 37, in test_seo_audit_api_provides_keyword_and_competitor_analysis
AssertionError: Request failed: 422 Client Error: Unprocessable Content for url: http://localhost:8000/api/v1/seo-audit

- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/0f01e6d1-cbfa-40a2-9390-f5d861c22c2d/34705a72-41d6-4101-a841-7b34ca72830e
- **Status:** ❌ Failed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC007 test_content_generation_api_generates_personalized_content
- **Test Code:** [TC007_test_content_generation_api_generates_personalized_content.py](./TC007_test_content_generation_api_generates_personalized_content.py)
- **Test Error:** Traceback (most recent call last):
  File "<string>", line 43, in test_content_generation_api_generates_personalized_content
AssertionError: Email generation failed with status 422

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/var/task/handler.py", line 258, in run_with_retry
    exec(code, exec_env)
  File "<string>", line 87, in <module>
  File "<string>", line 53, in test_content_generation_api_generates_personalized_content
AssertionError: Email generation test failed: Email generation failed with status 422

- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/0f01e6d1-cbfa-40a2-9390-f5d861c22c2d/cafe76fb-af25-4b00-a2b2-894540b9622c
- **Status:** ❌ Failed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC008 test_tavily_contact_intelligence_api_returns_up_to_date_data
- **Test Code:** [TC008_test_tavily_contact_intelligence_api_returns_up_to_date_data.py](./TC008_test_tavily_contact_intelligence_api_returns_up_to_date_data.py)
- **Test Error:** Traceback (most recent call last):
  File "<string>", line 31, in test_tavily_contact_intelligence_api_returns_up_to_date_data
  File "/var/task/requests/models.py", line 1024, in raise_for_status
    raise HTTPError(http_error_msg, response=self)
requests.exceptions.HTTPError: 422 Client Error: Unprocessable Content for url: http://localhost:8000/api/v1/search-news

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/var/task/handler.py", line 258, in run_with_retry
    exec(code, exec_env)
  File "<string>", line 94, in <module>
  File "<string>", line 87, in test_tavily_contact_intelligence_api_returns_up_to_date_data
AssertionError: HTTP request failed: 422 Client Error: Unprocessable Content for url: http://localhost:8000/api/v1/search-news

- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/0f01e6d1-cbfa-40a2-9390-f5d861c22c2d/e658c629-db21-43e2-8939-a8f7f56e3348
- **Status:** ❌ Failed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC009 test_apify_enrichment_api_enriches_lead_with_requested_data
- **Test Code:** [TC009_test_apify_enrichment_api_enriches_lead_with_requested_data.py](./TC009_test_apify_enrichment_api_enriches_lead_with_requested_data.py)
- **Test Error:** Traceback (most recent call last):
  File "/var/task/handler.py", line 258, in run_with_retry
    exec(code, exec_env)
  File "<string>", line 53
    assert "emails" in enriched_lead, 
                                      ^
SyntaxError: invalid syntax

- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/0f01e6d1-cbfa-40a2-9390-f5d861c22c2d/893a0fd9-d5e4-4b7f-b6be-6d0ede5b2707
- **Status:** ❌ Failed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC010 test_reverse_lookup_api_returns_matching_leads
- **Test Code:** [TC010_test_reverse_lookup_api_returns_matching_leads.py](./TC010_test_reverse_lookup_api_returns_matching_leads.py)
- **Test Error:** Traceback (most recent call last):
  File "<string>", line 18, in test_reverse_lookup_api_returns_matching_leads
  File "/var/task/requests/models.py", line 1024, in raise_for_status
    raise HTTPError(http_error_msg, response=self)
requests.exceptions.HTTPError: 422 Client Error: Unprocessable Content for url: http://localhost:8000/api/v1/reverse-lookup

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/var/task/handler.py", line 258, in run_with_retry
    exec(code, exec_env)
  File "<string>", line 40, in <module>
  File "<string>", line 22, in test_reverse_lookup_api_returns_matching_leads
AssertionError: Request failed for phone lookup: 422 Client Error: Unprocessable Content for url: http://localhost:8000/api/v1/reverse-lookup

- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/0f01e6d1-cbfa-40a2-9390-f5d861c22c2d/b5a53631-750b-4c86-aba4-55968ce30d63
- **Status:** ❌ Failed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---


## 3️⃣ Coverage & Matching Metrics

- **0.00** of tests passed

| Requirement        | Total Tests | ✅ Passed | ❌ Failed  |
|--------------------|-------------|-----------|------------|
| ...                | ...         | ...       | ...        |
---


## 4️⃣ Key Gaps / Risks
{AI_GNERATED_KET_GAPS_AND_RISKS}
---