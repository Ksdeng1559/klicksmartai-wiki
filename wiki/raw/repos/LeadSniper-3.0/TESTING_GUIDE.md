# LeadSniper 3.0 - Testing Guide

## Pre-Deployment Testing Checklist

Complete these tests before deploying to production.

---

## Local Development Testing

### 1. Environment Setup Test

```bash
# Check if .env.local exists
ls -la .env.local

# Verify Gemini API key is set
grep GEMINI_API_KEY .env.local

# Install dependencies
npm install

# Type checking
npm run type-check
```

**Expected Result:** ✅ No type errors, all dependencies installed

---

### 2. Development Server Test

```bash
# Start dev server
npm run dev
```

**Access:** http://localhost:3000

**Test Checklist:**
- [ ] Application loads without errors
- [ ] No console errors in browser DevTools
- [ ] UI renders correctly
- [ ] Dashboard displays properly

---

### 3. Core Feature Tests

#### A. Lead Search Functionality

**Test Steps:**
1. Go to "Setup / Import" tab
2. Set Niche: `Plumber`
3. Set City: `Austin, TX`
4. Set Campaign Focus: `General Audit`
5. Go back to "Finder" tab
6. Click "Find Leads"

**Expected Results:**
- [ ] Loading spinner appears
- [ ] Search completes within 30-60 seconds
- [ ] Returns 10-15 leads
- [ ] Each lead has: business name, rating, review count
- [ ] Leads categorized into buckets (Fixable Crisis, Hidden Gem, etc.)

**Error Handling Test:**
- [ ] Try without API key → Should show error
- [ ] Try with invalid city → Should fallback to simulation data

---

#### B. Lead Enrichment Test

**Test Steps:**
1. Click on any lead card
2. Wait for audit panel to load
3. Click "Enrich Contact Data"
4. Wait for social media lookup

**Expected Results:**
- [ ] Social media links populate (if available)
- [ ] Email variants generated
- [ ] Website verified
- [ ] Phone number displayed

---

#### C. SEO Audit Test

**Test Steps:**
1. Select a lead
2. Click "Run SEO Audit"
3. Wait for analysis

**Expected Results:**
- [ ] Keywords displayed with search volume
- [ ] Top competitors listed
- [ ] "Bleed Summary" generated
- [ ] Data source indicated (DataForSEO or AI estimate)

---

#### D. Email Generation Test

**Test Steps:**
1. Select a lead
2. Fill in Core Memory fields (Setup tab):
   - Offer: "We help plumbers get 10 more jobs/mo"
   - Problem: "inconsistent lead flow"
   - Guarantee: "pay on performance"
3. Click "Generate Email"

**Expected Results:**
- [ ] Email subject generated
- [ ] Email body personalized with unique angle
- [ ] Under 150 words
- [ ] Conversational tone
- [ ] Copy button works

---

#### E. Cold Call Script Test

**Test Steps:**
1. Select a lead
2. Click "Generate Cold Call Script"

**Expected Results:**
- [ ] Script sections generated: Opener, Research Hook, Qualification, Pitch, Closing
- [ ] Personalized with business details
- [ ] Copy button works

---

#### F. Growth Recommendations Test

**Test Steps:**
1. Select a lead
2. Scroll to recommendations section
3. Click "Generate Recommendations"

**Expected Results:**
- [ ] 3 recommendations generated
- [ ] Each has: title, description, impact, action type
- [ ] Tailored to business bucket

---

### 4. Import Features Test

#### A. CSV Import

**Test Data (create test.csv):**
```csv
Business Name,City,Website
Joe's Plumbing,Austin TX,https://joesplumbing.com
Quick Fix Plumbing,Austin TX,
```

**Test Steps:**
1. Go to "Setup / Import" tab
2. Upload test.csv OR paste contents
3. Click "Import & Enrich CSV"

**Expected Results:**
- [ ] Progress bar displays
- [ ] Leads enriched with reviews
- [ ] Missing data filled in where possible
- [ ] Switches to Finder tab with results

---

#### B. Reverse Contact Lookup

**Test Data:**
```
555-0123
john@example.com
```

**Test Steps:**
1. Paste contact list
2. Click "Find Businesses"

**Expected Results:**
- [ ] Progress indicator shows
- [ ] Businesses identified from contacts
- [ ] Lead cards populated

---

### 5. Export Functionality Test

**Test Steps:**
1. Generate some leads
2. Click Download icon (CSV export)

**Expected Results:**
- [ ] CSV file downloads
- [ ] Contains all lead data
- [ ] Properly formatted

---

### 6. Filter System Test

**Test Steps:**
1. Click "Smart Filters"
2. Set Max Rating: 3.5
3. Set Max Reviews: 50
4. Set Website: "Has Website"

**Expected Results:**
- [ ] Lead list filters in real-time
- [ ] "Filter Active" badge shows
- [ ] Results count updates

---

### 7. Performance Testing

```bash
# Build production version
npm run build

# Check bundle size
du -sh dist/

# Target: < 2MB total
```

**Performance Metrics:**
- [ ] Initial load: < 3s on 3G
- [ ] Time to Interactive: < 5s
- [ ] Bundle size: < 2MB
- [ ] No memory leaks (check DevTools)

---

### 8. Error Handling Tests

#### Scenario: API Key Missing
```bash
# Remove API key
echo "GEMINI_API_KEY=" > .env.local

# Reload app
```
**Expected:** Clear error message about missing API key

#### Scenario: Network Failure
1. Disconnect internet
2. Try to search leads

**Expected:** Error message with fallback to simulation data

#### Scenario: Invalid Input
1. Try empty niche/city
2. Try special characters

**Expected:** Validation messages

---

## Browser Compatibility Testing

### Desktop Browsers
- [ ] Chrome (latest)
- [ ] Firefox (latest)
- [ ] Safari (latest)
- [ ] Edge (latest)

### Mobile Browsers
- [ ] iOS Safari
- [ ] Chrome Mobile
- [ ] Samsung Internet

**Test on each:**
- [ ] Lead search works
- [ ] UI responsive
- [ ] No layout breaks
- [ ] Touch interactions work

---

## Production Build Testing

```bash
# Create production build
npm run build

# Preview production build
npm run preview

# Access at http://localhost:4173
```

**Production Checklist:**
- [ ] No console.log statements
- [ ] Source maps generated (for debugging)
- [ ] Assets cached properly
- [ ] Lazy loading works
- [ ] Code splitting active

---

## Security Testing

### API Key Protection
```bash
# Check if API key exposed in client code
grep -r "GEMINI_API_KEY" dist/

# Should NOT find it in compiled code
```

### HTTP Headers Test
```bash
# Test security headers
curl -I http://localhost:4173
```

**Expected Headers:**
- X-Frame-Options: DENY
- X-Content-Type-Options: nosniff
- X-XSS-Protection: 1; mode=block

---

## Load Testing (Optional)

```bash
# Install Apache Bench
sudo apt install apache2-utils  # Linux
brew install ab                  # Mac

# Test 100 requests, 10 concurrent
ab -n 100 -c 10 http://localhost:3000/
```

**Target Metrics:**
- Requests/sec: > 50
- Time per request: < 200ms
- Failed requests: 0

---

## Pre-Production Checklist

### Code Quality
- [ ] No TypeScript errors
- [ ] No ESLint warnings
- [ ] Code properly formatted
- [ ] Comments on complex logic

### Configuration
- [ ] Environment variables documented
- [ ] .gitignore includes sensitive files
- [ ] README updated with setup instructions
- [ ] API keys for production obtained

### Performance
- [ ] Bundle size optimized
- [ ] Images compressed
- [ ] Lazy loading implemented
- [ ] Caching strategy configured

### Security
- [ ] API keys secured
- [ ] HTTPS enabled (on deployment)
- [ ] CORS configured
- [ ] Input validation added

### Documentation
- [ ] User guide created
- [ ] API documentation complete
- [ ] Deployment instructions ready
- [ ] Troubleshooting guide available

---

## Test Results Log

**Date:** _____________

**Tester:** _____________

**Environment:** Local / Staging / Production

| Feature | Status | Notes |
|---------|--------|-------|
| Lead Search | ⬜ Pass ⬜ Fail | |
| Lead Enrichment | ⬜ Pass ⬜ Fail | |
| SEO Audit | ⬜ Pass ⬜ Fail | |
| Email Generation | ⬜ Pass ⬜ Fail | |
| Script Generation | ⬜ Pass ⬜ Fail | |
| CSV Import | ⬜ Pass ⬜ Fail | |
| Contact Lookup | ⬜ Pass ⬜ Fail | |
| Export CSV | ⬜ Pass ⬜ Fail | |
| Filters | ⬜ Pass ⬜ Fail | |

**Overall Status:** ⬜ Ready for Production ⬜ Needs Fixes

**Issues Found:**
1. ___________________________________
2. ___________________________________
3. ___________________________________

---

## Quick Test Command

```bash
# Run full test suite
npm run type-check && \
npm run build && \
echo "✅ Build successful - ready for deployment"
```

---

**Last Updated:** 2025-12-30
**Version:** 3.0.0
**Status:** Ready for Testing ✅
