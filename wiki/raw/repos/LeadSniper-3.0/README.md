<div align="center">
<img width="1200" height="475" alt="LeadSniper 3.0 Banner" src="https://github.com/user-attachments/assets/0aa67016-6eaf-458a-adb2-6e31a0763ed6" />

# LeadSniper 3.0

### Website Revenue Infrastructure Intelligence Platform

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone)
[![Deploy to Netlify](https://www.netlify.com/img/deploy/button.svg)](https://app.netlify.com/start)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

**Identify qualified local service businesses with observable website revenue leaks, intake friction, and AI Employee fit.**

[Features](#-features) • [Quick Start](#-quick-start) • [Security](#-security--code-review-status) • [Deploy](#-deployment) • [Documentation](#-documentation)

</div>

---

## Strategic Positioning

LeadSniperAI 3.0 is a Website Revenue Infrastructure Intelligence system for local service businesses.

It converts:

```text
Google Maps / website data
→ Eligibility screening
→ Demand signal review
→ Website failure detection
→ Final qualification override
→ AI Employee fit scoring
→ CRM-ready intelligence output
```

LeadSniperAI does not assume buying intent, fabricate contact data, claim revenue loss, or guarantee outcomes. All diagnostics must be based on observable public signals only.

---

## 🚨 SECURITY & CODE REVIEW STATUS

> **⚠️ PRODUCTION READINESS: BETA (82% Complete)**
> **Last Audit**: January 15, 2026 (Updated)
> **Status**: Beta Testing - Core functionality verified, Docker deployment ready, API documentation enabled

### 🔴 Critical Issues (MUST FIX)

| Issue                    | Severity    | Status          | Location                                     |
| ------------------------ | ----------- | --------------- | -------------------------------------------- |
| **Exposed API Keys**     | 🔴 CRITICAL | ❌ UNRESOLVED   | `.env.local` committed to repo               |
| **Hardcoded API Key**    | 🔴 CRITICAL | ✅ **RESOLVED** | Migrated to Backend Proxy                    |
| **Backend Config Error** | 🔴 CRITICAL | ✅ **RESOLVED** | `backend/app/core/config.py` - optional vars |
| **Gemini None Handling** | 🔴 CRITICAL | ✅ **RESOLVED** | `backend/app/api/endpoints.py` - v3.0.3      |

| **TypeScript Build Errors** | 🔴 HIGH | ❌ UNRESOLVED | 9 errors in Dashboard & tests |
| **Zero Test Coverage** | 🔴 HIGH | ❌ UNRESOLVED | No unit tests |

### 📊 Production Readiness Scorecard

| Category      | Score | Status        |
| ------------- | ----- | ------------- |
| Security      | 7/10  | 🟢 GOOD       |
| Type Safety   | 5/10  | 🟡 NEEDS WORK |
| Test Coverage | 3/10  | 🟡 IMPROVED   |
| Code Quality  | 7/10  | 🟢 GOOD       |
| Performance   | 8/10  | 🟢 GOOD       |
| Architecture  | 9/10  | 🟢 EXCELLENT  |
| DevOps        | 7/10  | 🟢 IMPROVED   |
| Live Data     | 9/10  | 🟢 EXCELLENT  |

**Overall**: **55/80 (82%)** - 🟡 BETA READY (Core Features Working, Docker Deployed)

### 🎯 Before You Deploy - Critical Actions Required

1. **IMMEDIATE** - Rotate all API keys (Gemini & Apify were exposed)
2. ~~**IMMEDIATE** - Remove hardcoded API key from `services/apifyService.ts`~~ ✅ **COMPLETED**
3. ~~**IMMEDIATE** - Fix backend configuration~~ ✅ **COMPLETED** (Supabase/GCP vars now optional)

4. ~~**HIGH PRIORITY** - Update backend endpoints~~ ✅ **COMPLETED** (Using settings, not os.getenv)
5. **HIGH PRIORITY** - Fix TypeScript build errors (9 errors)
6. **HIGH PRIORITY** - Add basic test coverage (minimum 60%)
7. **MEDIUM** - Implement structured logging (158 console.log statements)
8. **MEDIUM** - Add CI/CD pipeline with automated testing

📖 **Full Audit Report**: See [Production Readiness Audit](#-production-readiness-audit-report) below

---

## 🎯 What is LeadSniper?

LeadSniper 3.0 combines AI research, local business data, website diagnostics, and structured scoring to help users:

- 🔍 **Discover** local service businesses by niche and location
- ✅ **Screen** businesses against eligibility and demand-signal rules
- 🧭 **Diagnose** observable website revenue infrastructure gaps
- 🤖 **Score** AI Employee fit using public signals only
- 📊 **Enrich** leads with contact data, social profiles, and business insights
- 📧 **Generate** sales-safe outreach assets where appropriate
- 📈 **Audit** SEO performance, website friction, and conversion readiness
- 💾 **Export** intelligence records to CSV for CRM workflows

Built for **agency owners**, **business consultants**, **local SEO operators**, **AI automation providers**, and **lead intelligence teams**.

---

## ✨ Features/
- ✉️ **Cold Emails**: Hyper-personalized emails under 150 words
- 📞 **Call Scripts**: Professional phone scripts with research hooks
- 🎯 **Growth Recommendations**: AI-generated strategies for each lead
- 📊 **SEO Audits**: Keyword opportunities and competitor analysis
- 🔘 **SiteDoctor**: Google PageSpeed performance audits with Core Web Vitals

### Data Management

- 📤 **CSV Import**: Bulk import businesses for enrichment
- 📥 **CSV Export**: Export leads with all data fields
- 🔄 **Reverse Lookup**: Find businesses from phone numbers or emails
- 💾 **JSON Import**: Direct DataForSEO integration

### Business Intelligence

- 🏷️ **Lead Categorization**: Automatic bucketing (Fixable Crisis, Hidden Gem, Sleeping Giant, etc.)
- 📈 **Rescue Calculator**: For low-rated businesses, calculate reviews needed to recover
- 🎨 **Campaign Memory**: Store your offer, problem statement, and case studies
- 🔄 **Progress Tracking**: Real-time enrichment progress bars

### Website Revenue Infrastructure Intelligence

- 🧭 **Eligibility Screening**: Google Maps presence, website URL, local/offline service fit, operational status
- 🚦 **Demand Signal Review**: Reviews, phone visibility, business hours, and Maps visibility
- 🧱 **Website Failure Detection**: Hero failure, missing CTA, phone-only intake, mobile friction, weak trust signals
- 🤖 **AI Employee Fit Score**: 100-point scoring model for AI receptionist, booking, intake, and review workflows
- 📋 **CRM-Ready Diagnostic Output**: Structured records for CSV, CRM, Linear, and future RIOS/Hermes workflows

### 🔬 Tavily Contact Intelligence ⭐ NEW

- 🏢 **Company Intelligence**: AI-powered company summaries and descriptions
- 📰 **News Monitoring**: Latest news with sentiment analysis (positive/negative/neutral)
- 👔 **Hiring Signals**: Active job postings with urgency indicators
- 👤 **Decision Maker Discovery**: C-level executives with LinkedIn profiles
- 🏆 **Competitive Analysis**: Competitors, market position, and advantages
- 💻 **Tech Stack Detection**: Technologies used by target companies
- 📈 **Growth Signals**: Expansion, acquisitions, hiring sprees, funding status
- ⚠️ **Risk Signals**: Layoffs, negative press, legal issues
- 📊 **Enrichment Scoring**: 0-100 quality score based on data completeness

---

## 📚 Source of Truth Documentation

LeadSniperAI 3.0 is governed by the following internal documentation:

- [`docs/linear/linear-source-of-truth.md`](docs/linear/linear-source-of-truth.md)
- [`docs/scoring/eligibility-rules.md`](docs/scoring/eligibility-rules.md)
- [`docs/scoring/website-failure-rules.md`](docs/scoring/website-failure-rules.md)
- [`docs/scoring/ai-employee-fit-score.md`](docs/scoring/ai-employee-fit-score.md)

---

## 🚀 Quick Start

### Prerequisites

- **Node.js** 18+ ([Download](https://nodejs.org))
- **Gemini API Key** ([Get Free Key](https://aistudio.google.com/app/apikey))
- **Apify API Key** ([Get Free Key](https://console.apify.com/account/integrations)) - Optional but recommended
- **Tavily API Key** ([Get Key](https://tavily.com)) - Optional for deep research

### Installation

```bash
# Clone the repository
git clone https://github.com/Deng1559/LeadSniper-3.0.git
cd LeadSniper-3.0

# Install dependencies
npm install

# Create environment file (IMPORTANT: Use .env.local, NOT .env)
cp .env.example .env.local

# Edit .env.local and add your API keys
# NEVER commit .env.local to version control!
```

### 🔒 Secure Environment Setup

#### Frontend Environment Variables

Create `.env.local` with your API keys:

```bash
# Gemini API (Required)
GEMINI_API_KEY=your_gemini_api_key_here

# Apify API (Optional - for contact verification)
VITE_APIFY_API_KEY=your_apify_key_here

# Tavily API (Optional - for deep research)
VITE_TAVILY_API_KEY=your_tavily_key_here

# Environment
VITE_APP_ENV=development
```

#### Backend Environment Variables

Create `backend/.env` for backend API:

```bash
# Required for backend
GEMINI_API_KEY=your_gemini_api_key_here
APIFY_API_KEY=your_apify_key_here
TAVILY_API_KEY=your_tavily_key_here

# Optional - only needed if using Supabase integration
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_anon_key
SUPABASE_SERVICE_ROLE_KEY=your_service_role_key

# Optional - only needed for Google Cloud features
GOOGLE_CLOUD_PROJECT=your_project_id
GOOGLE_CLOUD_LOCATION=us-central1

# Redis (Optional)
REDIS_URL=redis://localhost:6379/0
```

> **✅ Fixed in v3.0.2**: Backend now gracefully handles missing Supabase/GCP environment variables.

**🚨 SECURITY WARNING**:

- ✅ Use `.env.local` (git-ignored by default)
- ❌ NEVER commit API keys to git
- ❌ NEVER use hardcoded API keys in source code
- ❌ NEVER share `.env.local` file

### Start Development Server

```bash
# Verify TypeScript compilation (should have 0 errors)
npm run type-check

# Start development server
npm run dev
```

**Access your app at:** http://localhost:3000

### First Search

1. Go to "Setup / Import" tab
2. Set **Niche**: `Plumber` (or any service business)
3. Set **City**: `Austin, TX` (or your target city)
4. Go to "Finder" tab
5. Click **"Find Leads"**
6. Wait 30-60 seconds for AI to search and enrich leads

🎉 **You're now generating AI-powered local business intelligence!**

---

## 🌐 Deployment

> **⚠️ WARNING**: Do not deploy to production until critical security issues are resolved.
> See [Security & Code Review Status](#-security--code-review-status) above.

### Pre-Deployment Checklist

- [ ] All API keys rotated (if previously exposed)
- [ ] No hardcoded secrets in source code
- [x] ✅ Backend configuration fixed (Supabase/GCP vars made optional)
- [x] ✅ Backend endpoints updated to use settings instead of `os.getenv()`
- [x] ✅ Browser compatibility issues resolved (Apify/Tavily migrated to backend)
- [ ] TypeScript build completes with 0 errors (`npm run type-check`)
- [ ] Production build succeeds (`npm run build`)
- [ ] Environment variables configured in deployment platform
- [ ] Basic test coverage implemented (minimum 60%)
- [ ] Security headers configured in nginx/CDN
- [ ] Error monitoring setup (Sentry, LogRocket, etc.)

### Option 1: Vercel (Recommended)

**One-Click Deploy:**

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/Deng1559/LeadSniper-3.0)

**Environment Variables Required:**

```
GEMINI_API_KEY=your_key
VITE_APIFY_API_KEY=your_key
VITE_TAVILY_API_KEY=your_key
```

**Manual Deploy:**

```bash
npm install -g vercel
vercel --prod
```

---

### Option 2: Netlify

```bash
npm install -g netlify-cli
netlify deploy --prod
```

---

### Option 3: Docker ⭐ RECOMMENDED

```bash
# Build and start backend only
docker compose build backend
docker compose up -d backend

# Build and start full stack (frontend + backend)
docker compose up -d

# View logs
docker compose logs -f backend

# Stop containers
docker compose stop
```

**Access Points:**
- Backend API: http://localhost:8000
- Swagger Docs: http://localhost:8000/docs
- Health Check: http://localhost:8000/api/v1/health
- Frontend (full stack): http://localhost:8080

**Environment Variables**: Create `.env` file in project root:

```bash
GEMINI_API_KEY=your_key
APIFY_API_KEY=your_key
TAVILY_API_KEY=your_key
# Optional
SUPABASE_URL=your_url
SUPABASE_KEY=your_key
```

---

### Option 4: Traditional Hosting

```bash
# Build for production
npm run build

# Deploy the 'dist' folder to any static host
```

**📖 Full deployment guide:** [QUICK_DEPLOY.md](QUICK_DEPLOY.md)

---

## 🔧 Troubleshooting

### Backend Startup Issues

**Problem**: Backend fails to start with configuration errors

**Symptoms**:

- `ERR_CONNECTION_REFUSED` when accessing http://localhost:8000
- Backend container exits immediately
- Error messages about missing environment variables

**Solution** ✅ **FIXED in v3.0.2**:

The backend now gracefully handles missing optional environment variables. You only need:

```bash
# Minimum required variables
GEMINI_API_KEY=your_key
APIFY_API_KEY=your_key
TAVILY_API_KEY=your_key
```

Optional variables (Supabase, Google Cloud, Redis) are no longer required for local development. The backend will start successfully and provide clear error messages if you try to use features that require optional integrations.

---

## Copyright

Copyright © 2026 KlickSmartAI. All rights reserved.
