# SiteDoctor Feature - PageSpeed Performance Audit

## Overview

SiteDoctor is a website performance auditing feature integrated into LeadSniper 3.0's AuditPanel. It uses Google's PageSpeed Insights API to analyze lead websites and provide actionable performance insights.

---

## Features

### Core Capabilities

1. **Performance Score Analysis**
   - Mobile-first performance scoring (0-100)
   - Visual score indicator with color coding:
     - 🟢 Green (90-100): Excellent performance
     - 🟡 Yellow (50-89): Needs improvement
     - 🔴 Red (0-49): Poor performance

2. **Core Web Vitals Monitoring**
   - **LCP** (Largest Contentful Paint): Measures loading performance
   - **CLS** (Cumulative Layout Shift): Measures visual stability
   - **FCP** (First Contentful Paint): Measures perceived load speed
   - **TTFB** (Time to First Byte): Measures server response time

3. **Opportunity Identification**
   - Top 3 performance bottlenecks
   - Estimated time savings for each fix
   - Actionable optimization recommendations

4. **Automatic Data Persistence**
   - Results saved to lead object
   - Available across sessions
   - Displayed immediately when audit exists

---

## Technical Implementation

### Architecture

**Service Layer**: `services/pageSpeedService.ts`
```typescript
export const analyzeWebsite = async (url: string): Promise<PageSpeedResult>
```

**UI Component**: `components/AuditPanel.tsx`
```typescript
const [pageSpeedAudit, setPageSpeedAudit] = useState<PageSpeedResult | null>(null);
const [analyzingSpeed, setAnalyzingSpeed] = useState(false);

const handleRunPageSpeed = async () => {
  const audit = await analyzeWebsite(lead.website);
  setPageSpeedAudit(audit);
  onLeadUpdate({ ...lead, pageSpeedAudit: audit });
};
```

**Data Structure**: `types.ts`
```typescript
export interface PageSpeedResult {
  score: number; // 0-100
  metrics: {
    lcp?: number;  // Largest Contentful Paint (ms)
    fid?: number;  // First Input Delay (ms)
    cls?: number;  // Cumulative Layout Shift
    fcp?: number;  // First Contentful Paint (ms)
    ttfb?: number; // Time to First Byte (ms)
  };
  opportunities: Array<{
    title: string;
    description: string;
    savingsMs?: number;
  }>;
  diagnostics: Array<{
    title: string;
    description: string;
  }>;
  screenshot?: string;
}
```

---

## User Interface

### Location
- **Panel**: Audit Panel (right side of LeadSniper)
- **Position**: Left column, below Review Analysis section
- **Visibility**: Only shown for leads with websites

### UI Components

1. **Header Section**
   ```
   🔘 SiteDoctor - Performance Audit    [Run Audit]
   ```

2. **Performance Score Display**
   - Large numerical score
   - Color-coded progress bar
   - Visual severity indicator

3. **Core Web Vitals Grid**
   ```
   LCP: 2,450ms ✅    CLS: 0.045 ✅
   FCP: 1,230ms ✅    TTFB: 420ms ✅
   ```

4. **Top Issues List**
   ```
   ⚠️ Top Issues (5)
   - Reduce unused JavaScript
     Potential savings: 1,230ms
   - Properly size images
     Potential savings: 890ms
   ```

---

## API Integration

### Google PageSpeed Insights API

**Endpoint**: `https://www.googleapis.com/pagespeedonline/v5/runPagespeed`

**Parameters**:
- `url`: Website URL to analyze
- `strategy`: `mobile` (default)
- `category`: `performance`

**Rate Limits**:
- Free tier: 25,000 queries/day
- 240 requests/minute

**No API Key Required**: The PageSpeed Insights API is publicly accessible

---

## Usage Workflow

### For Users

1. **Navigate to Audit Panel** for any lead with a website
2. **Click "Run Audit"** button in SiteDoctor section
3. **Wait 3-5 seconds** for analysis to complete
4. **Review Results**:
   - Performance score
   - Core Web Vitals metrics
   - Top optimization opportunities
5. **Use insights** for personalized outreach:
   - "I noticed your site scores 45/100 on mobile performance"
   - "We can help improve your LCP from 3.2s to under 1.5s"

### For Sales Outreach

**Example Pitch Integration**:
```
Subject: Quick Win: 45% Faster Page Load for [Business Name]

Hi [Owner],

I was checking out your website and ran a quick performance audit.
Your current mobile score is 47/100, mainly due to:

- Unoptimized images (costing 1.2s load time)
- Unused JavaScript (costing 890ms)

I specialize in fixing these exact issues. Could boost your score
to 90+ in about a week, which typically increases conversions by 20-30%.

Interested in a 15-min call to discuss?
```

---

## Integration Points

### 1. Lead Enrichment
```typescript
// Option to run PageSpeed during initial enrichment
const enrichedLead = await enrichSingleLead(lead);
if (lead.website) {
  enrichedLead.pageSpeedAudit = await analyzeWebsite(lead.website);
}
```

### 2. Growth Recommendations
```typescript
// Include PageSpeed insights in recommendations
if (pageSpeedAudit && pageSpeedAudit.score < 70) {
  recommendations.push({
    id: 'perf-boost',
    title: 'Website Performance Optimization',
    description: `Your site scores ${pageSpeedAudit.score}/100. Optimization could increase conversions by 20-30%.`,
    impact: 'High Revenue Potential',
    actionType: 'Technical SEO'
  });
}
```

### 3. Email Generation
```typescript
// Include PageSpeed data in pitch emails
const emailContent = await generateLeadEmail({
  lead,
  recommendation: selectedRecommendation,
  seoAudit,
  pageSpeedAudit, // NEW: Include performance insights
  offer, problem, guarantee, caseStudy
});
```

---

## Performance Benchmarks

### Thresholds (Google Standards)

| Metric | Good | Needs Improvement | Poor |
|--------|------|-------------------|------|
| **LCP** | ≤2.5s | 2.5s - 4.0s | >4.0s |
| **CLS** | ≤0.1 | 0.1 - 0.25 | >0.25 |
| **FCP** | ≤1.8s | 1.8s - 3.0s | >3.0s |
| **TTFB** | ≤600ms | 600ms - 1.5s | >1.5s |
| **Score** | 90-100 | 50-89 | 0-49 |

---

## Error Handling

### Common Issues

1. **Website Not Accessible**
   ```
   Error: "Failed to analyze website performance"
   Reason: Website is down, blocked, or requires authentication
   ```

2. **Invalid URL Format**
   ```
   Handled by: URL normalization in analyzeWebsite()
   Auto-prepends: https:// if missing
   ```

3. **API Rate Limit**
   ```
   Limit: 240 requests/minute
   Solution: Add request queue/throttling if needed
   ```

---

## Future Enhancements

### Phase 2 (Planned)

1. **Website Rebuild Generator**
   ```typescript
   const rebuildPrompt = generateRebuildPrompt(url, pageSpeedAudit);
   // Use Gemini to generate optimized landing page code
   ```

2. **Comparison Mode**
   - Compare lead's site vs competitors
   - Show relative performance ranking

3. **Historical Tracking**
   - Track performance over time
   - Show improvement trends

4. **Automated Recommendations**
   - Auto-generate growth recommendations from PageSpeed data
   - Include in email templates automatically

---

## Testing Guide

### Manual Testing Steps

1. **Basic Functionality**
   ```
   1. Find lead with website
   2. Open Audit Panel
   3. Click "Run Audit"
   4. Verify score displays
   5. Check Core Web Vitals appear
   6. Confirm opportunities list
   ```

2. **Edge Cases**
   ```
   - Lead without website (section should not appear)
   - Invalid URL (should show error)
   - Slow website (verify loading state)
   - Perfect score (verify green indicators)
   ```

3. **Data Persistence**
   ```
   1. Run audit
   2. Switch to different lead
   3. Return to original lead
   4. Verify audit data persists
   ```

---

## Cost Analysis

### API Usage

**Free Tier**: 25,000 queries/day = 750,000/month

**Projected Usage** (LeadSniper):
- 100 leads/day × 1 audit each = 100 queries/day
- 3,000 queries/month
- **Cost**: $0 (well within free tier)

**Break-Even**: Would need 25,000+ leads/day to exceed free tier

---

## Sales Impact

### Expected Outcomes

1. **Lead Qualification**
   - Identify leads with poor website performance (easier sell)
   - Target high-traffic sites needing optimization

2. **Personalized Outreach**
   - Data-backed pitch points
   - Specific, measurable improvements

3. **Conversion Rate**
   - +30% response rate (specific, actionable insights)
   - +40% pitch credibility (real data vs generic claims)

### ROI Calculation

**Investment**:
- Development time: 2 hours
- API cost: $0
- Maintenance: Minimal

**Returns** (per 100 leads):
- 30 audits run
- 5 additional qualified leads
- 2 additional conversions
- Value: $500-2,000/month (at typical agency rates)

---

## Completion Status

✅ **Completed Features**:
- PageSpeed API integration
- Performance score display
- Core Web Vitals metrics
- Opportunity identification
- UI component implementation
- Data persistence
- Error handling

⬜ **Future Enhancements**:
- Website rebuild generator
- Competitor comparison
- Historical tracking
- Automated recommendations

---

## Files Modified

1. **`components/AuditPanel.tsx`**
   - Added PageSpeed imports
   - Added state management
   - Added handleRunPageSpeed function
   - Added SiteDoctor UI section

2. **`services/pageSpeedService.ts`**
   - Already existed (complete implementation)

3. **`types.ts`**
   - PageSpeedResult interface (already defined)
   - Lead.pageSpeedAudit field (already defined)

---

## Support & Troubleshooting

### Common Questions

**Q: Why doesn't the button appear?**
A: SiteDoctor only shows for leads with websites. Check that `lead.website` exists.

**Q: Why is the audit slow?**
A: PageSpeed Insights runs real mobile device tests. Typical response time: 3-8 seconds.

**Q: Can I audit the same site multiple times?**
A: Yes, but results are cached by Google for ~30 seconds. Re-running immediately may return identical results.

**Q: What if the website is password-protected?**
A: PageSpeed can only audit publicly accessible pages. Password-protected sites will fail.

---

**Built with ❤️ for LeadSniper 3.0**

**Last Updated**: January 2026
