# LeadSniper Database Schema & Field Mapping

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           LeadSniper Data Flow                               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐                   │
│  │   Frontend   │───▶│   Backend    │───▶│   Supabase   │                   │
│  │   (React)    │    │   (FastAPI)  │    │ (PostgreSQL) │                   │
│  └──────────────┘    └──────────────┘    └──────────────┘                   │
│         │                   │                   │                            │
│         │                   │                   ▼                            │
│         │                   │           ┌──────────────┐                    │
│         │                   │           │   BigQuery   │                    │
│         │                   │           │  (Analytics) │                    │
│         │                   │           └──────────────┘                    │
│         │                   │                   │                            │
│         │                   ▼                   │                            │
│         │           ┌──────────────┐            │                            │
│         │           │  Grounding   │            │                            │
│         └──────────▶│  API (Gemini)│────────────┘                           │
│                     │  + BrightData│                                         │
│                     └──────────────┘                                         │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 1. Supabase Schema (Operational Storage)

### 1.1 Core Tables

#### `leads` - Primary Lead Storage
```sql
CREATE TABLE leads (
    -- Primary Key
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    external_id VARCHAR(100) UNIQUE,  -- Frontend lead-{idx}-{timestamp}

    -- Core Business Info
    business_name VARCHAR(255) NOT NULL,
    niche VARCHAR(100) NOT NULL,
    city VARCHAR(100) NOT NULL,
    state VARCHAR(50),
    country VARCHAR(50) DEFAULT 'USA',

    -- Contact Info
    website VARCHAR(500),
    phone VARCHAR(50),
    email VARCHAR(255),

    -- Google Maps Data
    rating DECIMAL(2,1) DEFAULT 0.0,
    review_count INTEGER DEFAULT 0,
    map_link VARCHAR(500),
    place_id VARCHAR(100),  -- Google Place ID
    maps_uri VARCHAR(500),
    latitude DECIMAL(10,7),
    longitude DECIMAL(10,7),

    -- Business Intelligence
    owner_name VARCHAR(255),
    unique_angle TEXT,
    establishment_date DATE,

    -- Lead Scoring
    bucket VARCHAR(50) NOT NULL,  -- Premium, Growth, Crisis, Startup
    rescue_number INTEGER,  -- Reviews needed to reach 4.2
    lead_score INTEGER DEFAULT 0,  -- 0-100

    -- Metadata
    source VARCHAR(50) DEFAULT 'gemini_grounding',  -- gemini_grounding, brightdata, manual
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    created_by UUID REFERENCES auth.users(id),

    -- Search Index
    search_vector tsvector GENERATED ALWAYS AS (
        to_tsvector('english', business_name || ' ' || COALESCE(niche, '') || ' ' || COALESCE(city, ''))
    ) STORED
);

-- Indexes
CREATE INDEX idx_leads_business_name ON leads(business_name);
CREATE INDEX idx_leads_niche_city ON leads(niche, city);
CREATE INDEX idx_leads_bucket ON leads(bucket);
CREATE INDEX idx_leads_rating ON leads(rating);
CREATE INDEX idx_leads_place_id ON leads(place_id);
CREATE INDEX idx_leads_search ON leads USING GIN(search_vector);
CREATE INDEX idx_leads_created_at ON leads(created_at DESC);
```

#### `lead_reviews` - Review Snippets
```sql
CREATE TABLE lead_reviews (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    lead_id UUID REFERENCES leads(id) ON DELETE CASCADE,

    snippet_type VARCHAR(20) NOT NULL,  -- 'positive' or 'negative'
    content TEXT NOT NULL,
    source VARCHAR(50),  -- 'google', 'yelp', 'gemini_extract'

    created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_lead_reviews_lead_id ON lead_reviews(lead_id);
CREATE INDEX idx_lead_reviews_type ON lead_reviews(snippet_type);
```

#### `lead_emails` - Email Variants
```sql
CREATE TABLE lead_emails (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    lead_id UUID REFERENCES leads(id) ON DELETE CASCADE,

    email VARCHAR(255) NOT NULL,
    email_type VARCHAR(50),  -- 'generated', 'verified', 'scraped'
    confidence_score INTEGER DEFAULT 0,  -- 0-100
    is_verified BOOLEAN DEFAULT FALSE,
    verification_date TIMESTAMPTZ,

    created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_lead_emails_lead_id ON lead_emails(lead_id);
CREATE UNIQUE INDEX idx_lead_emails_unique ON lead_emails(lead_id, email);
```

#### `lead_socials` - Social Profiles
```sql
CREATE TABLE lead_socials (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    lead_id UUID REFERENCES leads(id) ON DELETE CASCADE,

    platform VARCHAR(50) NOT NULL,  -- instagram, facebook, linkedin, twitter
    profile_url VARCHAR(500),
    username VARCHAR(100),
    followers INTEGER,
    is_verified BOOLEAN DEFAULT FALSE,

    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_lead_socials_lead_id ON lead_socials(lead_id);
CREATE UNIQUE INDEX idx_lead_socials_platform ON lead_socials(lead_id, platform);
```

### 1.2 Enrichment Tables

#### `lead_enrichments` - BrightData/API Enrichment Data
```sql
CREATE TABLE lead_enrichments (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    lead_id UUID REFERENCES leads(id) ON DELETE CASCADE,

    -- Source Tracking
    source VARCHAR(50) NOT NULL,  -- 'brightdata_crunchbase', 'brightdata_zoominfo', 'tavily', 'apify'
    enrichment_type VARCHAR(50) NOT NULL,  -- 'company', 'contact', 'social', 'seo'

    -- Raw Data (JSONB for flexibility)
    raw_data JSONB NOT NULL,

    -- Extracted Fields (denormalized for querying)
    employee_count INTEGER,
    annual_revenue VARCHAR(50),
    funding_total VARCHAR(50),
    industry VARCHAR(100),
    tech_stack TEXT[],

    -- Quality Metrics
    confidence_score INTEGER DEFAULT 0,
    data_freshness_days INTEGER,

    created_at TIMESTAMPTZ DEFAULT NOW(),
    expires_at TIMESTAMPTZ  -- For cache invalidation
);

CREATE INDEX idx_lead_enrichments_lead_id ON lead_enrichments(lead_id);
CREATE INDEX idx_lead_enrichments_source ON lead_enrichments(source);
CREATE INDEX idx_lead_enrichments_type ON lead_enrichments(enrichment_type);
```

#### `seo_audits` - SEO Analysis Results
```sql
CREATE TABLE seo_audits (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    lead_id UUID REFERENCES leads(id) ON DELETE CASCADE,

    -- Summary
    bleed_summary TEXT,
    data_source VARCHAR(50) DEFAULT 'gemini_estimate',  -- 'gemini_estimate', 'dataforseo'

    -- Metrics
    domain_authority INTEGER,
    organic_traffic INTEGER,
    keyword_count INTEGER,

    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_seo_audits_lead_id ON seo_audits(lead_id);
```

#### `seo_keywords` - Keyword Opportunities
```sql
CREATE TABLE seo_keywords (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    seo_audit_id UUID REFERENCES seo_audits(id) ON DELETE CASCADE,

    keyword VARCHAR(255) NOT NULL,
    search_volume INTEGER,
    search_volume_display VARCHAR(20),  -- "1.2k"
    cpc DECIMAL(10,2),
    cpc_display VARCHAR(20),  -- "$5.00"
    difficulty INTEGER,  -- 0-100

    created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_seo_keywords_audit ON seo_keywords(seo_audit_id);
```

#### `seo_competitors` - Competitor Analysis
```sql
CREATE TABLE seo_competitors (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    seo_audit_id UUID REFERENCES seo_audits(id) ON DELETE CASCADE,

    name VARCHAR(255) NOT NULL,
    url VARCHAR(500),
    advantage TEXT,  -- "Winning because..."
    threat_level VARCHAR(20),  -- 'high', 'medium', 'low'

    created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_seo_competitors_audit ON seo_competitors(seo_audit_id);
```

### 1.3 Activity & Campaign Tables

#### `campaigns` - Search Campaigns
```sql
CREATE TABLE campaigns (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES auth.users(id),

    name VARCHAR(255) NOT NULL,
    niche VARCHAR(100) NOT NULL,
    city VARCHAR(100) NOT NULL,
    focus VARCHAR(50) DEFAULT 'any',  -- any, crisis, growth, reactivation

    -- Campaign Memory
    offer TEXT,
    problem TEXT,
    guarantee TEXT,
    case_study TEXT,

    -- Stats
    total_leads INTEGER DEFAULT 0,
    enriched_leads INTEGER DEFAULT 0,
    contacted_leads INTEGER DEFAULT 0,

    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_campaigns_user ON campaigns(user_id);
```

#### `lead_activities` - Activity Log
```sql
CREATE TABLE lead_activities (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    lead_id UUID REFERENCES leads(id) ON DELETE CASCADE,
    user_id UUID REFERENCES auth.users(id),

    activity_type VARCHAR(50) NOT NULL,  -- 'search', 'enrich', 'email_generated', 'script_generated', 'export'
    activity_data JSONB,

    created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_lead_activities_lead ON lead_activities(lead_id);
CREATE INDEX idx_lead_activities_user ON lead_activities(user_id);
CREATE INDEX idx_lead_activities_type ON lead_activities(activity_type);
CREATE INDEX idx_lead_activities_created ON lead_activities(created_at DESC);
```

#### `generated_content` - Emails & Scripts
```sql
CREATE TABLE generated_content (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    lead_id UUID REFERENCES leads(id) ON DELETE CASCADE,
    user_id UUID REFERENCES auth.users(id),

    content_type VARCHAR(20) NOT NULL,  -- 'email', 'script'

    -- Email Fields
    subject VARCHAR(500),
    body TEXT,

    -- Script Fields
    opener TEXT,
    research_hook TEXT,
    qualification TEXT,
    pitch TEXT,
    closing TEXT,

    -- Metadata
    prompt_context JSONB,  -- Store offer, problem, etc. used
    created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_generated_content_lead ON generated_content(lead_id);
CREATE INDEX idx_generated_content_type ON generated_content(content_type);
```

---

## 2. BigQuery Schema (Analytics)

### 2.1 Fact Tables

#### `fact_lead_searches` - Search Events
```sql
CREATE TABLE `project.leadsniper.fact_lead_searches` (
    search_id STRING NOT NULL,
    user_id STRING,

    -- Search Parameters
    niche STRING NOT NULL,
    city STRING NOT NULL,
    state STRING,
    focus STRING,  -- any, crisis, growth, reactivation

    -- Results
    leads_found INT64,
    search_duration_ms INT64,

    -- Source
    api_source STRING,  -- gemini, brightdata
    grounding_type STRING,  -- google_maps, web_search

    -- Timestamps
    searched_at TIMESTAMP NOT NULL,
    partition_date DATE NOT NULL
)
PARTITION BY partition_date
CLUSTER BY niche, city;
```

#### `fact_lead_enrichments` - Enrichment Events
```sql
CREATE TABLE `project.leadsniper.fact_lead_enrichments` (
    enrichment_id STRING NOT NULL,
    lead_id STRING NOT NULL,
    user_id STRING,

    -- Enrichment Details
    source STRING NOT NULL,  -- brightdata_crunchbase, brightdata_zoominfo, tavily, apify
    enrichment_type STRING NOT NULL,

    -- Quality
    confidence_score INT64,
    fields_enriched INT64,

    -- Performance
    api_latency_ms INT64,
    cost_credits FLOAT64,

    -- Timestamps
    enriched_at TIMESTAMP NOT NULL,
    partition_date DATE NOT NULL
)
PARTITION BY partition_date
CLUSTER BY source, enrichment_type;
```

#### `fact_content_generations` - AI Content Events
```sql
CREATE TABLE `project.leadsniper.fact_content_generations` (
    generation_id STRING NOT NULL,
    lead_id STRING NOT NULL,
    user_id STRING,

    -- Content Details
    content_type STRING NOT NULL,  -- email, script, recommendation
    token_count INT64,

    -- Quality
    generation_time_ms INT64,
    model_used STRING,  -- gemini-2.5-flash

    -- Timestamps
    generated_at TIMESTAMP NOT NULL,
    partition_date DATE NOT NULL
)
PARTITION BY partition_date
CLUSTER BY content_type;
```

### 2.2 Dimension Tables

#### `dim_leads` - Lead Dimension (SCD Type 2)
```sql
CREATE TABLE `project.leadsniper.dim_leads` (
    lead_key INT64 NOT NULL,  -- Surrogate key
    lead_id STRING NOT NULL,  -- Natural key

    -- Business Info
    business_name STRING,
    niche STRING,
    city STRING,
    state STRING,

    -- Metrics at snapshot
    rating FLOAT64,
    review_count INT64,
    bucket STRING,
    lead_score INT64,

    -- SCD Type 2 Fields
    is_current BOOL,
    valid_from TIMESTAMP,
    valid_to TIMESTAMP,

    -- ETL
    loaded_at TIMESTAMP
);
```

#### `dim_niches` - Niche Dimension
```sql
CREATE TABLE `project.leadsniper.dim_niches` (
    niche_key INT64 NOT NULL,
    niche_name STRING NOT NULL,
    category STRING,  -- Home Services, Professional Services, etc.
    avg_deal_size FLOAT64,
    competition_level STRING,  -- low, medium, high

    loaded_at TIMESTAMP
);
```

#### `dim_locations` - Location Dimension
```sql
CREATE TABLE `project.leadsniper.dim_locations` (
    location_key INT64 NOT NULL,
    city STRING NOT NULL,
    state STRING,
    country STRING,
    region STRING,  -- West, Southwest, etc.
    population INT64,
    median_income FLOAT64,

    loaded_at TIMESTAMP
);
```

### 2.3 Aggregate Tables

#### `agg_daily_metrics` - Daily Summary
```sql
CREATE TABLE `project.leadsniper.agg_daily_metrics` (
    metric_date DATE NOT NULL,
    user_id STRING,

    -- Volumes
    searches_count INT64,
    leads_generated INT64,
    leads_enriched INT64,
    emails_generated INT64,
    scripts_generated INT64,
    exports_count INT64,

    -- Quality
    avg_lead_score FLOAT64,
    premium_leads_pct FLOAT64,
    crisis_leads_pct FLOAT64,

    -- Costs
    api_credits_used FLOAT64,
    gemini_tokens_used INT64,

    loaded_at TIMESTAMP
)
PARTITION BY metric_date;
```

#### `agg_niche_performance` - Niche Analytics
```sql
CREATE TABLE `project.leadsniper.agg_niche_performance` (
    metric_date DATE NOT NULL,
    niche STRING NOT NULL,
    city STRING,

    -- Volumes
    searches_count INT64,
    leads_found INT64,
    avg_leads_per_search FLOAT64,

    -- Quality Distribution
    premium_count INT64,
    growth_count INT64,
    crisis_count INT64,
    startup_count INT64,

    -- Rating Distribution
    avg_rating FLOAT64,
    avg_review_count FLOAT64,

    loaded_at TIMESTAMP
)
PARTITION BY metric_date
CLUSTER BY niche, city;
```

---

## 3. Field Mapping: LeadSniper → Database

### 3.1 Lead Model Mapping

| Frontend (types.ts) | Backend (Pydantic) | Supabase Column | BigQuery Column | BrightData Field |
|---------------------|-------------------|-----------------|-----------------|------------------|
| `id` | `id` | `external_id` | `lead_id` | - |
| `businessName` | `businessName` | `business_name` | `business_name` | `company_name` |
| `niche` | `niche` | `niche` | `niche` | `industry` |
| `city` | `city` | `city` | `city` | `headquarters_city` |
| `rating` | `rating` | `rating` | `rating` | `google_rating` |
| `reviewCount` | `reviewCount` | `review_count` | `review_count` | `google_reviews_count` |
| `website` | `website` | `website` | - | `website_url` |
| `phone` | `phone` | `phone` | - | `phone_number` |
| `mapLink` | `mapLink` | `map_link` | - | `google_maps_url` |
| `ownerName` | `ownerName` | `owner_name` | - | `ceo_name` / `owner` |
| `uniqueAngle` | `uniqueAngle` | `unique_angle` | - | - |
| `bucket` | `bucket` | `bucket` | `bucket` | - |
| `rescueNumber` | `rescueNumber` | `rescue_number` | - | - |

### 3.2 Grounding Metadata Mapping

| Frontend | Backend | Supabase | BigQuery | Source |
|----------|---------|----------|----------|--------|
| `groundingMetadata.placeId` | `placeId` | `place_id` | - | Google Maps Grounding |
| `groundingMetadata.mapsUri` | `mapsUri` | `maps_uri` | - | Google Maps Grounding |
| `groundingMetadata.coordinates.latitude` | `coordinates.latitude` | `latitude` | - | Google Maps Grounding |
| `groundingMetadata.coordinates.longitude` | `coordinates.longitude` | `longitude` | - | Google Maps Grounding |

### 3.3 BrightData Enrichment Mapping

#### Crunchbase (`web_data_crunchbase_company`)
| BrightData Field | Supabase Column | BigQuery Column |
|------------------|-----------------|-----------------|
| `company_name` | `business_name` | `business_name` |
| `short_description` | `raw_data->>'description'` | - |
| `founded_on` | `establishment_date` | - |
| `num_employees_enum` | `employee_count` | `employee_count` |
| `total_funding_usd` | `funding_total` | `funding_total` |
| `last_funding_type` | `raw_data->>'last_funding_type'` | - |
| `categories` | `raw_data->>'categories'` | `categories` |
| `headquarters_city` | `city` | `city` |

#### ZoomInfo (`web_data_zoominfo_company_profile`)
| BrightData Field | Supabase Column | BigQuery Column |
|------------------|-----------------|-----------------|
| `company_name` | `business_name` | `business_name` |
| `revenue` | `annual_revenue` | `annual_revenue` |
| `employees` | `employee_count` | `employee_count` |
| `industry` | `niche` | `niche` |
| `technologies` | `tech_stack` | `tech_stack` |
| `phone` | `phone` | - |
| `website` | `website` | - |

#### Google Maps Reviews (`web_data_google_maps_reviews`)
| BrightData Field | Supabase Column | BigQuery Column |
|------------------|-----------------|-----------------|
| `review_text` | `lead_reviews.content` | - |
| `rating` | `lead_reviews.raw_data->>'rating'` | - |
| `review_date` | `lead_reviews.raw_data->>'date'` | - |
| `reviewer_name` | `lead_reviews.raw_data->>'reviewer'` | - |

### 3.4 SEO Audit Mapping

| Frontend (types.ts) | Backend | Supabase Table | Column |
|---------------------|---------|----------------|--------|
| `seoAudit.keywords[].keyword` | `KeywordOpportunity.keyword` | `seo_keywords` | `keyword` |
| `seoAudit.keywords[].volume` | `KeywordOpportunity.volume` | `seo_keywords` | `search_volume_display` |
| `seoAudit.keywords[].cpc` | `KeywordOpportunity.cpc` | `seo_keywords` | `cpc_display` |
| `seoAudit.competitors[].name` | `Competitor.name` | `seo_competitors` | `name` |
| `seoAudit.competitors[].advantage` | `Competitor.advantage` | `seo_competitors` | `advantage` |
| `seoAudit.summary` | `SeoAudit.summary` | `seo_audits` | `bleed_summary` |

---

## 4. Data Flow & ETL

### 4.1 Real-time Flow (Supabase)
```
Frontend Request → FastAPI Backend → Gemini Grounding API
                                          ↓
                                   Parse Response
                                          ↓
                                   Insert to Supabase
                                          ↓
                                   Return to Frontend
```

### 4.2 Batch Analytics Flow (BigQuery)
```
Supabase (Source) → Cloud Function (ETL) → BigQuery (Warehouse)
                          ↓
                   Transform & Aggregate
                          ↓
                   Load Fact/Dim Tables
```

### 4.3 Enrichment Flow (BrightData)
```
Lead Selected → BrightData MCP Tool → Parse Response
                      ↓
              Store in lead_enrichments
                      ↓
              Update lead record
                      ↓
              Log to BigQuery
```

---

## 5. Row-Level Security (RLS) Policies

```sql
-- Enable RLS
ALTER TABLE leads ENABLE ROW LEVEL SECURITY;
ALTER TABLE campaigns ENABLE ROW LEVEL SECURITY;
ALTER TABLE lead_activities ENABLE ROW LEVEL SECURITY;

-- Policies
CREATE POLICY "Users can view own leads" ON leads
    FOR SELECT USING (auth.uid() = created_by);

CREATE POLICY "Users can insert own leads" ON leads
    FOR INSERT WITH CHECK (auth.uid() = created_by);

CREATE POLICY "Users can update own leads" ON leads
    FOR UPDATE USING (auth.uid() = created_by);

CREATE POLICY "Users can view own campaigns" ON campaigns
    FOR ALL USING (auth.uid() = user_id);
```

---

## 6. Supabase Functions

### 6.1 Lead Scoring Function
```sql
CREATE OR REPLACE FUNCTION calculate_lead_score(lead_row leads)
RETURNS INTEGER AS $$
DECLARE
    score INTEGER := 0;
BEGIN
    -- Rating component (0-30 points)
    score := score + LEAST(30, ROUND(lead_row.rating * 6));

    -- Review count component (0-25 points)
    score := score + LEAST(25, ROUND(LOG(lead_row.review_count + 1) * 5));

    -- Has website (10 points)
    IF lead_row.website IS NOT NULL AND lead_row.website != '' THEN
        score := score + 10;
    END IF;

    -- Has phone (10 points)
    IF lead_row.phone IS NOT NULL AND lead_row.phone != '' THEN
        score := score + 10;
    END IF;

    -- Has owner name (15 points)
    IF lead_row.owner_name IS NOT NULL AND lead_row.owner_name != 'Unknown' THEN
        score := score + 15;
    END IF;

    -- Bucket bonus (0-10 points)
    CASE lead_row.bucket
        WHEN 'Premium ($5K+/mo)' THEN score := score + 10;
        WHEN 'Growth ($2-5K/mo)' THEN score := score + 7;
        WHEN 'Crisis (Rescue)' THEN score := score + 5;
        ELSE score := score + 0;
    END CASE;

    RETURN LEAST(100, score);
END;
$$ LANGUAGE plpgsql;
```

### 6.2 Update Trigger
```sql
CREATE OR REPLACE FUNCTION update_lead_score()
RETURNS TRIGGER AS $$
BEGIN
    NEW.lead_score := calculate_lead_score(NEW);
    NEW.updated_at := NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_lead_score
    BEFORE INSERT OR UPDATE ON leads
    FOR EACH ROW
    EXECUTE FUNCTION update_lead_score();
```

---

## 7. Implementation Checklist

### Phase 1: Core Schema (Week 1)
- [ ] Create `leads` table with indexes
- [ ] Create `lead_reviews` table
- [ ] Create `lead_emails` table
- [ ] Create `lead_socials` table
- [ ] Set up RLS policies
- [ ] Create lead scoring function

### Phase 2: Enrichment Schema (Week 2)
- [ ] Create `lead_enrichments` table
- [ ] Create `seo_audits` table
- [ ] Create `seo_keywords` table
- [ ] Create `seo_competitors` table
- [ ] Set up BrightData field mapping

### Phase 3: Activity Tracking (Week 3)
- [ ] Create `campaigns` table
- [ ] Create `lead_activities` table
- [ ] Create `generated_content` table
- [ ] Set up activity triggers

### Phase 4: BigQuery Analytics (Week 4)
- [ ] Create fact tables
- [ ] Create dimension tables
- [ ] Create aggregate tables
- [ ] Set up ETL pipeline
- [ ] Create analytics views

---

## 8. API Integration Points

### Backend Endpoints → Supabase
| Endpoint | Operation | Table(s) |
|----------|-----------|----------|
| `POST /search` | INSERT | `leads`, `lead_reviews` |
| `POST /enrich` | UPDATE | `leads`, `lead_enrichments` |
| `POST /seo-audit` | INSERT | `seo_audits`, `seo_keywords`, `seo_competitors` |
| `POST /generate-email` | INSERT | `generated_content`, `lead_activities` |
| `POST /generate-script` | INSERT | `generated_content`, `lead_activities` |
| `POST /social-lookup` | INSERT | `lead_socials` |
| `GET /leads` | SELECT | `leads` (with joins) |
| `POST /export` | SELECT + LOG | `leads`, `lead_activities` |

---

*Document Version: 1.0*
*Last Updated: January 14, 2026*
*Author: Claude Opus 4.5*
