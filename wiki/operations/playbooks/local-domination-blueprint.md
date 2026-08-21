# Playbook: Local Domination Blueprint (Programmatic SEO)

> **Source:** [boringmarketer/guides — LOCAL-DOMINATION-BLUEPRINT.md](https://github.com/boringmarketer/guides/blob/main/LOCAL-DOMINATION-BLUEPRINT.md)
> **Category:** Programmatic SEO / Local SEO
> **Tech Stack:** Claude Code + GitHub + Vercel
> **Estimated Run Cost:** ~$20/month
> **Cataloged:** 2026-04-30

---

## Overview

A repeatable, AI-driven framework for spinning up locally-optimized websites at scale. Uses Claude Code as the primary coding agent to generate, deploy, and optimize location-specific sites programmatically. Designed to capture local search traffic across hundreds/thousands of geographic modifiers with near-zero ongoing maintenance.

---

## The 6 Phases

### Phase 1: Foundation
- Set up GitHub repo as source of truth
- Configure Vercel for auto-deployment on push
- Establish the base site template (service pages, location pages, blog scaffolding)
- Domain strategy: subfolder vs. subdomain vs. separate domains per location

### Phase 2: Intelligence
- Build the keyword universe: service + location modifier matrix
- Scrape and analyze top-ranking local competitors
- Identify content gaps (services competitors rank for that you don't cover)
- Create the priority deployment queue based on search volume × competition

### Phase 3: Build Advantage
- Generate programmatic location pages via Claude Code
- Each location page: unique title, H1, meta description, localized content
- Avoid duplicate content penalties — Claude handles variation at scale
- Dynamic internal linking between location pages and service pages
- Deploy via git push → Vercel auto-build

### Phase 4: Conversion Optimization
- A/B test CTAs, trust signals, and social proof per location
- Add schema markup (LocalBusiness, FAQ, Review) programmatically
- Implement click-to-call, driving directions, contact forms
- Performance monitoring via Vercel Analytics / Google Search Console

### Phase 5: Growth Acceleration
- Programmatic blog content tied to local intent keywords
- "Near me" and long-tail modifier expansion
- Backlink acquisition strategy (citations, local directories, guest posts)
- Google Business Profile integration per location

### Phase 6: Domination
- Monitor rankings across entire keyword universe
- Re-optimize underperforming pages via Claude Code
- Expand to new locations / service categories
- Build topical authority clusters (hub pages → spoke location pages)
- Rinse and repeat at larger scale

---

## KlickSmartAI Service Angle

### How We'd Package This

| Component | Deliverable |
|-----------|-------------|
| Foundation Setup | GitHub + Vercel infrastructure, base template |
| Keyword Research | Full service × location matrix (e.g., 5 services × 200 cities = 1,000 pages) |
| Content Generation | 50-500 programmatic location pages (Claude Code) |
| Technical SEO | Schema markup, internal linking, sitemaps |
| Monthly Optimization | Re-optimize low performers, expand keyword coverage |

### Pricing Model (Suggested)

| Tier | Pages | One-Time Setup | Monthly Retainer |
|------|-------|---------------|-----------------|
| Starter | 50 location pages | $2,500 | $500/mo |
| Growth | 200 location pages | $5,000 | $750/mo |
| Domination | 500+ location pages | $8,000+ | $1,000+/mo |

### Ideal Client Profile
- Multi-location service business (HVAC, plumbing, roofing, dental, legal)
- Single-location business wanting to dominate a metro area (e.g., "plumber + [50 neighborhoods]")
- Franchise operations with individual location pages needed

---

## Key Insights

1. **Programmatic ≠ Spam** — Claude-generated content passes quality thresholds when given good prompts and context. The key is variation, not duplication.
2. **Speed Is the Moat** — Competitors can't match the velocity of AI-generated, human-quality location pages deployed continuously.
3. **Internal Linking Is Underrated** — The blueprint emphasizes hub-and-spoke architecture; location pages link to service pages, service pages link back. This is where most programmatic SEO fails.
4. **Cost Efficiency** — $20/month infrastructure cost (Vercel free tier + GitHub free tier) vs. traditional agency fees of $3k-10k/month.
5. **Compounding Returns** — Each new location page adds marginal traffic. At 500+ pages, the aggregate traffic curve steepens.

---

## Risk & Limitations

| Risk | Mitigation |
|------|-----------|
| Google "thin content" penalties | Claude generates substantial, varied content; avoid pure templating |
| Vercel free tier limits | 100GB bandwidth, 6,000 build minutes — sufficient for static sites |
| Client churn | Content stays live on their domain; they own the GitHub repo |
| AI content detection | Google's stance: quality matters, not origin. Focus on helpfulness. |

---

## Related Playbooks
- [First 100 Clients Playbook](../../concepts/first-100-clients-playbook.md) — complementary outbound strategy
- [Digital Marketing Subcontractors](../vendors/digital-marketing-subcontractors.md) — GEO/backlinks to layer on top

---

*For full implementation details, reference the original guide at the GitHub source link above.*
