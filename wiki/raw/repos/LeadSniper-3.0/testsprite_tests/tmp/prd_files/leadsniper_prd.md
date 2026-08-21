# LeadSniper 3.0 - Product Requirements Document

## 1. Overview

LeadSniper is an AI-powered B2B lead generation and enrichment platform designed to help sales teams discover, validate, and enrich business leads at scale. The platform combines Google Maps data, AI-powered research, and multi-source enrichment to deliver high-quality leads with verified contact information.

## 2. Core Features

### 2.1 Business Search (Vertex AI Grounding)
**Purpose**: Discover businesses using AI-powered search with Google Maps grounding

**User Flow**:
1. User enters niche (e.g., "plumbers") and city (e.g., "Los Angeles")
2. Optionally selects focus mode: crisis, growth, reactivation, or any
3. System uses Gemini AI with Google Search grounding to find businesses
4. Returns leads with: business name, rating, review count, phone, website, owner name
5. Leads are automatically categorized into revenue buckets

**Acceptance Criteria**:
- Returns 10 businesses per search
- Each lead has rating, review count, and at least one contact method
- Leads are categorized into: Premium ($5K+), Growth ($2-5K), Crisis (Rescue), Startup (<$2K)
- Crisis leads include "rescue number" calculation

### 2.2 Lead Enrichment
**Purpose**: Enhance lead data with additional information from multiple sources

**Enrichment Sources**:
- Gemini AI with web grounding
- Apify web scraping
- Tavily contact intelligence

**User Flow**:
1. Select a lead to enrich
2. System performs multi-source enrichment:
   - Website analysis
   - Social profile discovery
   - Decision maker identification
   - Company intelligence gathering
3. Returns enriched lead with emails, social profiles, company insights

**Acceptance Criteria**:
- Email pattern generation based on owner name and domain
- Social profile discovery (LinkedIn, Twitter, Facebook)
- Company intelligence: competitors, hiring signals, news

### 2.3 Batch Import & Processing
**Purpose**: Import large volumes of leads from CSV files with automated enrichment

**User Flow**:
1. Upload CSV file with leads
2. Preview import with validation summary
3. Configure import options (chunk size, duplicate detection, immediate enrichment)
4. Start batch processing
5. Monitor progress via batch management UI
6. Download enriched leads

**Acceptance Criteria**:
- Support CSV files up to 1000 rows
- Validate required fields (business name)
- Detect and skip duplicates
- Process leads in configurable chunks (default: 50)
- Background processing via Celery workers
- Retry failed leads
- Cancel running batches

### 2.4 SEO Audit
**Purpose**: Analyze website SEO and provide actionable recommendations

**User Flow**:
1. Enter website URL and niche
2. System performs SEO analysis:
   - Keyword opportunities
   - Competitor analysis
   - Technical SEO issues
3. Returns audit report with recommendations

**Acceptance Criteria**:
- Identify top 5 keyword opportunities
- List competitor websites
- Provide actionable recommendations

### 2.5 Content Generation
**Purpose**: Generate personalized sales content using AI

**Content Types**:
- Personalized sales emails
- Cold call scripts
- Marketing recommendations

**User Flow**:
1. Select lead to target
2. Choose content type
3. System generates personalized content based on lead data
4. User can edit and export content

**Acceptance Criteria**:
- Emails include personalization (business name, pain points)
- Scripts include opener, value prop, and CTA
- Recommendations based on lead's industry and situation

### 2.6 Contact Intelligence (Tavily)
**Purpose**: Deep research on companies and decision makers

**Features**:
- News search: Find recent company news and press releases
- Hiring signals: Detect job postings indicating growth
- Decision makers: Find key contacts with titles and LinkedIn profiles

**Acceptance Criteria**:
- Return latest news items with dates
- Identify hiring roles and job posting links
- Find decision makers with verified LinkedIn URLs

### 2.7 Social Enrichment
**Purpose**: Find social media profiles for leads

**Platforms**:
- LinkedIn
- Twitter/X
- Facebook
- Instagram

**Acceptance Criteria**:
- Return valid profile URLs
- Identify business vs personal pages

## 3. Technical Architecture

### 3.1 Backend (Python/FastAPI)
- **Framework**: FastAPI 0.115.6
- **Background Jobs**: Celery 5.4.0 with Redis
- **Database**: Supabase (PostgreSQL)
- **AI Services**: Google Cloud AI Platform, Gemini API
- **External APIs**: Apify, Tavily

### 3.2 Frontend (React/TypeScript)
- **Framework**: React 19.2
- **Build Tool**: Vite 6.2
- **UI Components**: Custom components with Lucide icons
- **State Management**: React hooks

### 3.3 Database Schema
- **leads**: Core lead data with full-text search
- **enrichment_results**: Multi-source enrichment data
- **batch_jobs**: Batch processing state and progress
- **batch_leads**: Individual lead records within batches
- **enrichment_queue**: Background enrichment queue

## 4. API Endpoints

### Search & Discovery
- `POST /api/v1/search` - Business search with AI grounding
- `POST /api/v1/reverse-lookup` - Find business by phone or URL

### Enrichment
- `POST /api/v1/enrich` - Basic lead enrichment
- `POST /api/v1/enrich-apify` - Apify web scraping enrichment
- `POST /api/v1/enrich-tavily` - Basic Tavily enrichment
- `POST /api/v1/enrich-tavily-full` - Full contact intelligence
- `POST /api/v1/social-enrich` - Social profile discovery

### Batch Processing
- `POST /api/v1/import-batch` - Import CSV batch
- `POST /api/v1/import-batch/preview` - Preview import
- `GET /api/v1/batches` - List batch jobs
- `GET /api/v1/batch/{batch_id}` - Get batch details
- `POST /api/v1/batch/{batch_id}/retry` - Retry failed batch
- `POST /api/v1/batch/{batch_id}/cancel` - Cancel batch
- `GET /api/v1/batch/{batch_id}/errors` - Get batch errors
- `GET /api/v1/batch/{batch_id}/leads` - Get batch leads

### Intelligence
- `POST /api/v1/seo-audit` - SEO analysis
- `POST /api/v1/search-news` - Company news search
- `POST /api/v1/search-hiring` - Hiring signals search
- `POST /api/v1/search-decision-makers` - Decision maker search

### Content Generation
- `POST /api/v1/generate-email` - Generate sales email
- `POST /api/v1/generate-script` - Generate sales script
- `POST /api/v1/generate-recommendations` - Generate recommendations

### System
- `GET /` - Root endpoint
- `GET /health` - Health check
- `GET /api/v1/enrichment-queue/stats` - Queue statistics

## 5. Testing Requirements

### Unit Tests
- CSV parser validation logic
- Lead categorization algorithm
- Email pattern generation
- Batch state machine transitions

### Integration Tests
- API endpoint request/response validation
- Database operations (CRUD)
- External API integrations (mocked)

### E2E Tests
- Complete search flow
- Batch import workflow
- Lead enrichment pipeline

## 6. Non-Functional Requirements

### Performance
- Search response: <5 seconds
- Batch processing: 100 leads/minute
- API response time: <500ms (excluding enrichment)

### Reliability
- 99.9% API uptime
- Graceful degradation when external APIs fail
- Automatic retry for transient failures

### Security
- API key protection (server-side only)
- Input validation and sanitization
- CORS configuration for production
