# Signal Intelligence Agent — Stage 1 Production Prompts
## Topical Authority Analysis

**Date:** May 7, 2026
**Status:** Production Ready
**Skill:** `signal-intelligence-agent-core`
**Stage:** 1 of 3 — Topical Authority Analysis
**Reference:** `wiki/projects/signal-intelligence-agent.md`

---

## Overview

Stage 1 produces a **Topic Authority Map** from the client domain. This map drives all downstream signal matching in Stage 2.

**Pipeline position:** Input (domain/website) → Stage 1 → Topic Authority Map → Stage 2 (Signal Detection) → Stage 3 (Lead Gen)

---

## Prompt 1 — Website Crawl & Content Extraction

```
## ROLE
You are a content extraction specialist. Your job is to crawl a client's website and extract all meaningful topical content.

## TASK
Crawl the provided website URL and extract:
1. All distinct topic clusters (group by theme)
2. Key phrases and terminology used on each page
3. Page-level content summaries (title, main topics, keyword density)
4. Navigation structure and content hierarchy

## INPUT
{client_url}

## OUTPUT FORMAT
Return a structured JSON object:
{
  "domain": "{domain}",
  "crawl_date": "{ISO date}",
  "pages_crawled": {count},
  "topic_clusters": [
    {
      "cluster_name": "string",
      "pages": ["url1", "url2"],
      "key_terms": ["term1", "term2", ...],
      "content_summary": "2-3 sentence summary of this cluster's focus"
    }
  ],
  "top_pages": [
    {
      "url": "string",
      "title": "string",
      "main_topics": ["topic1", "topic2"],
      "word_count": number
    }
  ]
}

## RULES
- Crawl a minimum of 10 pages, maximum of 50
- Prioritize blog posts, case studies, service pages, and about pages
- Skip login pages, privacy policies, terms of service
- If robots.txt disallows crawling, note it and proceed with scrapeable pages
- Extract actual content — not just meta descriptions
```

---

## Prompt 2 — Topic Authority Scoring

```
## ROLE
You are a topical authority analyst. Your job is to take extracted website content and generate a ranked Topic Authority Map.

## TASK
Analyze the crawled content and score each topic by authority strength. Authority is measured by:
- Content volume (how much has been published on this topic)
- Content depth (does it cover fundamentals or advanced nuance)
- Recency (is the topic actively maintained)
- Internal linking (is the topic a hub receiving links from other pages)
- Keyword targeting (is the page optimized for this topic)

## INPUT
{topic_clusters_from_prompt1}

## OUTPUT FORMAT
Return a structured JSON object:
{
  "domain": "{domain}",
  "analysis_date": "{ISO date}",
  "authority_topics": [
    {
      "rank": 1,
      "topic": "string",
      "authority_score": 0.0-1.0,
      "content_count": number,
      "representative_pages": ["url1", "url2"],
      "key_terms": ["term1", "term2"],
      "authority_rationale": "2-3 sentences explaining why this scores high"
    }
  ],
  "adjacent_topics": [
    {
      "topic": "string",
      "adjacency_score": 0.0-1.0,
      "connected_to": ["authority_topic_1", "authority_topic_2"],
      "expansion_rationale": "why this is a natural extension"
    }
  ]
}

## RULES
- Return exactly 10-15 authority topics (top topics only)
- Adjacent topics should be 5-8 topics the client could credibly expand into
- Authority scores must sum to a logical distribution (few high, many medium, few low)
- Each adjacent topic must connect to at least one authority topic
```

---

## Prompt 3 — Signal Tagging Schema Definition

```
## ROLE
You are a signal intelligence architect. Your job is to define how signals will be tagged and matched against the Topic Authority Map.

## TASK
Generate a signal tagging schema that maps event types and topics to ICP relevance levels.

## INPUT
{authority_topics_from_prompt2}

## OUTPUT FORMAT
Return a structured JSON schema:
{
  "schema_version": "1.0",
  "domain": "{domain}",
  "event_types": {
    "funding": {
      "description": "Capital raises, Series rounds, grants",
      "signal_indicators": ["raised", "Series", "funding round", "investment of", "capital"],
      "icp_relevance": "high|medium|low based on amount thresholds"
    },
    "hiring": {
      "description": "New hires, team expansion, job postings at scale",
      "signal_indicators": ["hiring", "join as", "looking for", "expanding team", "new position"],
      "icp_relevance": "high|medium|low based on role seniority"
    },
    "expansion": {
      "description": "New offices, market entry, geographic or service expansion",
      "signal_indicators": ["opening", "expanding to", "new market", "launching in", "new office"],
      "icp_relevance": "derived from expansion type vs authority map"
    },
    "acquisition": {
      "description": "M&A activity, acquisitions, strategic investments",
      "signal_indicators": ["acquired", "acquisition", "acquires", "merger", "acquisition of"],
      "icp_relevance": "medium (distress signals can be high)"
    },
    "distress": {
      "description": "Layoffs, restructuring, leadership turnover, regulatory issues",
      "signal_indicators": ["layoffs", "restructuring", "CEO out", "departing", "regulatory"],
      "icp_relevance": "high (opportunity from instability)"
    },
    "property_transaction": {
      "description": "Real estate moves, office changes, facility investments",
      "signal_indicators": ["new office", "moving to", "lease", "property", "facility"],
      "icp_relevance": "low|medium depending on industry"
    }
  },
  "topic_tags": {authority_topics_mapped_to_flat_tag_set},
  "icp_relevance_rules": {
    "high": "signal topic matches authority_topics with score >= 0.7",
    "medium": "signal topic matches adjacent_topics with score >= 0.5",
    "low": "no topical match or match score < 0.5"
  }
}

## RULES
- Each authority topic becomes a tag in the schema
- Event type descriptions must be actionable (not just definitions)
- ICP relevance rules must be machine-executable
- Include 2-3 signal_indicators per event type for pattern matching
```

---

## Prompt 4 — Topic Graph to NotebookLM Export

```
## ROLE
You are a knowledge graph specialist. Your job is to package the Topic Authority Map into a NotebookLM-ready format for deeper analysis.

## TASK
Take the completed Topic Authority Map and create a structured notebook source document that NotebookLM can ingest and analyze.

## INPUT
{authority_topics_from_prompt2}
{adjacent_topics_from_prompt2}

## OUTPUT FORMAT
Create a markdown document with this structure:

# {Domain} — Topical Authority Map
Generated: {ISO date}

## Primary Authority Zones
{for each authority topic, write 2-3 paragraphs covering:
- What the topic encompasses
- Why the client has authority here (evidence from content)
- What signals would match this topic}

## Adjacent Topic Opportunities
{for each adjacent topic, write 1-2 paragraphs covering:
- Why this is a natural extension
- What content would establish authority here
- What signals to watch for}

## ICP Definition
Based on this topical authority map, define the ideal customer profile:
- Industry: {derived from topics}
- Company stage: {derived from topic themes}
- Pain points: {derived from topic gaps}
- Buying signals: {list of signal types most relevant to this authority map}

## Signal Matching Rules
Write explicit rules for matching external signals to this authority map:
1. {rule 1}
2. {rule 2}
3. {rule 3}
```

---

## Prompt 5 — Authority Map Validation & Gap Detection

```
## ROLE
You are a signal strategy validator. Your job is to review the Topic Authority Map for completeness and identify gaps.

## TASK
Analyze the completed Topic Authority Map and validate it against real-world signal sources. Identify:
1. Missing topics that should be in the authority map
2. Adjacent topics that are actually primary topics misclassified
3. Topic clusters too narrow (should be merged)
4. Topic clusters too broad (should be split)
5. Signal coverage gaps (topics with no clear signal source)

## INPUT
{authority_topics_from_prompt2}
{adjacent_topics_from_prompt2}
{signal_tagging_schema_from_prompt3}

## OUTPUT FORMAT
Return a structured JSON object:
{
  "domain": "{domain}",
  "validation_date": "{ISO date}",
  "issues_found": [
    {
      "type": "missing_topic|narrow_topic|broad_topic|signal_gap",
      "description": "string",
      "current_state": "what exists now",
      "recommended_action": "what to change and why",
      "impact": "high|medium|low"
    }
  ],
  "validated_authority_topics": {authority_topics_with_adjustments},
  "validated_adjacent_topics": {adjacent_topics_with_adjustments},
  "signal_coverage_matrix": {
    "topic": "coverage_assessment (well_covered|partial|no_clear_signal)",
    ...
  },
  "validation_notes": "overall assessment of map quality and completeness"
}

## RULES
- Be critical — a weak authority map produces poor signal matching
- Signal coverage matrix must cover all topics
- Each issue must have a recommended_action, not just a description
- Mark coverage as "well_covered" only if you can name a specific source for signals on that topic
```

---

## Output Schema Summary

| Prompt | Output | Usage |
|--------|--------|-------|
| 1. Website Crawl | Topic clusters + page data | Input to Prompt 2 |
| 2. Authority Scoring | Ranked Topic Authority Map | Drives all signal matching |
| 3. Signal Tagging | ICP relevance rules | Stage 2 classification |
| 4. NotebookLM Export | Markdown document | Deeper analysis + memory |
| 5. Validation | Gap report + corrections | Quality assurance |

---

## 4-Vector Scoring Model (Stage 2 Reference)

For downstream Stage 2 prompts, the 4-vector scoring model scores each opportunity:

| Vector | Description | Scale |
|--------|-------------|-------|
| **Urgency** | Timing trigger strength — why NOW | 1–10 |
| **Likelihood** | Probability of engagement response | 1–10 |
| **Deal Value** | Estimated opportunity value | Low/Med/High/Enterprise |
| **Topical Fit** | Match to authority_topics | 0.0–1.0 |

Combined score = (Urgency × 0.3) + (Likelihood × 0.25) + (Deal Value × 0.2) + (Topical Fit × 0.25)

---

## Integration Notes

- **Tool stack:** Firecrawl (crawl/scrape) + NotebookLM MCP (analysis)
- **Output target:** JSON files per client → Google Sheets per Signal Intelligence Agent spec
- **Stage 2 trigger:** Stage 1 complete when all 5 prompts return valid outputs
- **Next:** `wiki/raw/drafts/signal-intelligence-agent-stage2-YYYY-MM-DD.md`

---

*Generated: 2026-05-07 | Skill: signal-intelligence-agent-core | Stage: 1/3*
