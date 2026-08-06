# Source: Notion (page 3a49e94c-f0a4-8191-a554-e67a3343d08f)

## 1. Document purpose
Build an SEO-led mortgage website for **Mortgages by Dennis Eng** using a WordPress-first architecture that is familiar to operate, fast to launch, and extensible enough to support custom React and TypeScript mortgage calculators.
This document combines:
- the product requirements,
- the recommended technical architecture,
- the WordPress content model,
- calculator and lead-generation requirements,
- a phased build plan,
- and a practical learning path based on Agrici Daniel’s Claude Code and SEO tutorials.
> **Decision:** Elementor is not required. Use WordPress, Gutenberg, a custom block theme, structured content, and independently developed React/TypeScript calculator components.
## 2. Product vision
Create a high-trust BC mortgage education and lead-generation platform that helps borrowers understand financing options and converts qualified visitors into advisor-ready opportunities.
The site should become a connected system rather than a collection of blog posts:
**Search intent → helpful content → calculator or assessment → personalized result → consent-based lead capture → CRM and follow-up workflow**
## 3. Primary audiences
- Self-employed borrowers
- Borrowers considering B lenders or alternative lenders
- Property owners seeking refinancing or debt consolidation
- Construction and development financing prospects
- First-time and move-up homebuyers in British Columbia
- Mortgage renewal prospects
## 4. Business outcomes
1. Rank for high-intent mortgage queries in British Columbia.
2. Establish Dennis as a specialist in self-employed, alternative, construction, and complex mortgage financing.
3. Convert informational traffic into calculator and assessment starts.
4. Generate complete, consented, CRM-ready opportunities.
5. Build a reusable publishing and lead-generation platform.
## 5. Success metrics
### Acquisition
- Organic clicks and impressions by topic cluster
- Top-10 and top-3 keyword rankings
- Local search visibility by target city
- Indexed pages and valid structured data
### Engagement
- Article engagement rate
- Calculator start rate
- Calculator completion rate
- Internal-link click-through rate
- Return visitor rate
### Conversion
- Visitor-to-lead conversion rate
- Assessment completion rate
- Qualified-lead rate
- Booking rate
- Contact response time
- Funded-opportunity rate and estimated pipeline value
## 6. Technical architecture
```plain text
WordPress CMS
├── Gutenberg editor
├── Custom block theme
├── Custom post types and taxonomies
├── ACF or native custom fields
├── SEO plugin
└── React calculator plugin
    ├── TSX interface structure
    ├── TypeScript calculation and validation logic
    ├── CSS or Tailwind styling
    ├── Gutenberg blocks or shortcodes
    └── API submissions
             ↓
Supabase lead and event database
             ↓
Atomic CRM and n8n workflows
             ↓
Email, SMS, booking and advisor follow-up
```
### Technology responsibilities
<table header-row="true">
<tr>
<td>Layer</td>
<td>Responsibility</td>
</tr>
<tr>
<td>WordPress</td>
<td>CMS, editorial workflow, media, users and publishing</td>
</tr>
<tr>
<td>Gutenberg</td>
<td>Visual content editing and reusable page sections</td>
</tr>
<tr>
<td>Custom block theme</td>
<td>Brand design, templates, responsive layout and performance</td>
</tr>
<tr>
<td>HTML/semantic markup</td>
<td>Page and component structure</td>
</tr>
<tr>
<td>CSS or Tailwind</td>
<td>Styling and responsive presentation</td>
</tr>
<tr>
<td>React</td>
<td>Interactive calculator and assessment interfaces</td>
</tr>
<tr>
<td>TypeScript</td>
<td>Form types, mortgage logic, validation and API contracts</td>
</tr>
<tr>
<td>Supabase</td>
<td>Lead records, calculator events and result persistence</td>
</tr>
<tr>
<td>Atomic CRM</td>
<td>Advisor pipeline and lead management</td>
</tr>
<tr>
<td>n8n</td>
<td>Routing, notifications, enrichment and follow-up automation</td>
</tr>
</table>
## 7. Why Elementor is not required
Elementor is useful for rapidly producing visual layouts, but it should not be a foundational dependency because:
- Claude Code can generate and maintain the custom theme and blocks.
- Gutenberg supports reusable patterns and structured editing.
- A custom theme provides cleaner markup and better performance control.
- React calculators remain independent from the page builder.
- Structured mortgage content can be reused across pages, schema, calculators and AI responses.
Elementor may remain available on a staging or legacy site during migration, but new production templates should use Gutenberg and custom blocks.
## 8. WordPress content model
### Core post types
1. **Articles** — educational and news content
2. **Mortgage Guides** — durable pillar and supporting guides
3. **Mortgage Programs** — structured lending-program pages
4. **Locations** — city and regional mortgage pages
5. **Calculators** — landing pages and calculator configuration
6. **Case Studies** — anonymized borrower situations and outcomes
7. **FAQs** — reusable answers
8. **Glossary Terms** — mortgage definitions
9. **Authors** — credentials, biography and expertise
### Suggested taxonomies
- Borrower type
- Mortgage purpose
- Lending category
- Property type
- Location
- Funnel stage
- Topic cluster
### Structured mortgage-program fields
- Program name
- Intended borrower
- Financing purpose
- Minimum down payment or equity
- Income documentation
- Credit considerations
- Eligible property types
- Typical lender category
- Estimated fees and limitations
- Required documents
- Related calculator
- Related articles
- Call to action
- Last reviewed date
- Compliance disclaimer
## 9. Page templates
### Required templates
- Homepage
- Service page
- Mortgage-program page
- Location page
- Topic-cluster pillar page
- Supporting article
- Comparison page
- Calculator landing page
- Case study
- FAQ and glossary archive
- Author page
- Contact and booking page
### Standard SEO-page structure
1. Clear answer and value proposition
2. Eligibility or intended-user summary
3. Explanation of the mortgage problem
4. Available financing paths
5. Comparison table or decision factors
6. Required documents
7. Calculator or assessment
8. Case example
9. Relevant FAQs
10. Related internal links
11. Advisor call to action
12. Disclosures and last-reviewed date
## 10. Lead magnet roadmap
### Priority 1 — B-Lender Qualification Assessment
**Purpose:** Capture borrowers who may not fit traditional bank guidelines.
Inputs may include:
- Financing purpose
- Property location and value
- Mortgage balance or requested amount
- Down payment or equity
- Employment or business type
- Income-documentation availability
- Credit range
- Existing monthly obligations
- Timing
Output:
- Illustrative pathway category
- Strengths and possible concerns
- Suggested supporting documents
- Recommended next action
- Optional personalized-review request
### Priority 2 — Self-Employed Mortgage Assessment
Evaluate business history, reported income, gross revenue, down payment, credit range and documentation readiness. Show conventional and alternative documentation pathways without promising approval.
### Priority 3 — Affordability Calculator
Estimate mortgage amount, payment, taxes, heating, condominium fees and debt-service ratios using clearly documented assumptions.
### Priority 4 — Refinance and Debt Consolidation Calculator
Estimate available equity, potential debt consolidation and illustrative cash-flow change.
### Priority 5 — Construction Financing Assessment
Qualify land, permits, project stage, budget, borrower equity, builder experience and requested facility.
### Priority 6 — Renewal Savings Calculator
Capture maturity date, existing balance, current rate, remaining amortization and renewal contact permission.
## 11. Calculator technical requirements
### Frontend
- React components written in TSX
- TypeScript interfaces for all inputs and outputs
- Semantic HTML and accessible labels
- Responsive CSS or Tailwind design
- Keyboard navigation
- Inline validation and helpful error messages
- Progress indicator for multi-step assessments
- Result page with plain-language interpretation
### Integration
- Calculator inserted through a custom Gutenberg block or shortcode
- API endpoint protected against spam and abuse
- Lead data stored in Supabase
- CRM record created or updated
- n8n workflow triggered after valid consent
- Analytics events sent for start, step completion, result and lead submission
### Compliance and trust
- Calculations must be labelled as estimates
- No statement may imply approval or a commitment to lend
- Assumptions must be visible
- Consent must be explicit and recorded
- Sensitive information should be minimized at the initial assessment stage
- Privacy notice and contact permissions must be presented before submission
- Calculation logic must be reviewed before production release
## 12. SEO requirements
- Clean permalink structure
- XML sitemap and robots controls
- Canonical tags
- Breadcrumbs
- Organization, Person, Article, WebPage and Breadcrumb structured data where appropriate
- Local-business details represented accurately
- Unique titles and descriptions
- Semantic headings
- Responsive images and modern image formats
- Strong internal-linking system
- Author credentials and review dates
- Source citations for regulatory, lender-rule or market claims
- Core Web Vitals monitoring
- Google Search Console and GA4 integration
## 13. Claude Code operating model
Claude Code should work against a version-controlled WordPress project rather than making unmanaged production changes.
### Repository scope
```plain text
/wp-content/themes/mortgages-by-dennis/
/wp-content/plugins/dennis-mortgage-calculators/
/docs/
  PRD.md
  CONTENT-MODEL.md
  SEO-ARCHITECTURE.md
  CALCULATOR-SPECS.md
CLAUDE.md
```
### Guardrails
- Develop locally or in staging first
- Use Git branches and pull requests
- Back up the database before structural changes
- Never commit credentials
- Review generated PHP, JavaScript and schema changes
- Run accessibility and performance checks
- Require approval before deployment to production
## 14. Implementation phases
### Phase 0 — Discovery and baseline
- Inventory the existing site, pages and plugins
- Export or back up WordPress
- Capture current rankings and analytics
- Confirm branding and required legal disclosures
- Define the MVP topic clusters and lead magnets
**Exit criteria:** Approved inventory, architecture and measurement baseline.
### Phase 1 — Development environment
- Create staging WordPress environment
- Initialize Git repository
- Configure local development
- Install Claude Code
- Add a project-level `CLAUDE.md`
- Establish backup and deployment procedure
**Exit criteria:** Repeatable local/staging workflow and version-controlled custom code.
### Phase 2 — Gutenberg design system
- Build custom block theme
- Establish typography, spacing, colours and UI tokens
- Build header, footer and navigation
- Create reusable Gutenberg patterns
- Validate responsive behaviour and accessibility
**Exit criteria:** Approved design system and reusable templates.
### Phase 3 — Structured CMS
- Create custom post types and taxonomies
- Add structured fields
- Build editorial templates
- Configure roles and workflow
- Prepare migration mapping from existing pages
**Exit criteria:** Editors can create every required content type without writing code.
### Phase 4 — SEO foundation
- Configure SEO plugin
- Implement metadata and canonical rules
- Add schema and breadcrumbs
- Generate sitemap
- Establish internal-link modules
- Run technical and content audits
**Exit criteria:** Staging site passes technical SEO, accessibility and performance QA.
### Phase 5 — Content launch
Initial clusters:
1. B lenders and alternative mortgages
2. Self-employed mortgage financing
3. Construction and development financing
4. Refinance and debt consolidation
5. BC local mortgage pages
**Exit criteria:** Core commercial pages and first supporting articles are ready for publication.
### Phase 6 — B-lender assessment MVP
- Finalize question flow
- Write TypeScript data contracts
- Build React interface
- Implement result logic
- Add consent and CRM submission
- Test calculations and edge cases
**Exit criteria:** Production-ready assessment generates a CRM record and advisor alert.
### Phase 7 — Measurement and optimization
- Track rankings and conversions
- Review drop-off by assessment step
- Test calls to action
- Expand calculator and content roadmap
- Refresh claims, links and review dates
**Exit criteria:** Monthly optimization process is operating with measurable conversion data.
## 15. Practical how-to for Dennis
### Step 1 — Start with WordPress, not headless Astro
Use your existing WordPress knowledge. Build the first production version with Gutenberg and custom code. Consider Astro only after a demonstrated need for a separate frontend.
### Step 2 — Replace Elementor gradually
Do not rebuild every existing page at once. Develop the new theme, blocks and templates on staging. Migrate the highest-value pages first, then remove Elementor after all dependencies have been replaced.
### Step 3 — Install and understand Claude Code
1. Install the Claude Code CLI.
2. Open the local WordPress project folder in the terminal.
3. Start Claude Code from the repository root.
4. Give it project context through `CLAUDE.md`.
5. Ask it to inspect before changing files.
6. Make small, testable changes on branches.
### Step 4 — Install Agrici Daniel’s Claude SEO skill
Current public installation instructions list Claude Code, Python 3.10+ and Git as prerequisites. The preferred plugin approach is:
```plain text
/plugin marketplace add AgriciDaniel/claude-seo
/plugin install claude-seo@agricidaniel-claude-seo
```
Because repository instructions can change, verify the current command in the official repository before installation.
### Step 5 — Run the first SEO audit
```plain text
/seo audit https://mortgagesbydenniseng.ca
```
Then use focused commands for individual pages, schema, content, local SEO and sitemap architecture. Convert findings into prioritized GitHub or Notion tasks rather than allowing broad uncontrolled edits.
### Step 6 — Build the theme in vertical slices
A useful sequence is:
1. Header and footer
2. Homepage template
3. Article template
4. Mortgage-program template
5. Location template
6. Calculator landing-page template
7. Reusable CTA, FAQ and author blocks
For every slice, complete design, mobile behaviour, accessibility, SEO and QA before moving on.
### Step 7 — Build calculators as a plugin
Create a dedicated plugin rather than placing calculator code inside the theme. The plugin can register custom Gutenberg blocks and load React only on pages where a calculator appears.
Suggested plugin structure:
```plain text
dennis-mortgage-calculators/
├── dennis-mortgage-calculators.php
├── src/
│   ├── blocks/
│   ├── calculators/
│   ├── components/
│   ├── lib/
│   └── types/
├── build/
└── tests/
```
### Step 8 — Connect the lead workflow
After a visitor submits with consent:
1. Validate the request server-side.
2. Store the lead and calculator result.
3. Create or update the CRM record.
4. Trigger the appropriate n8n workflow.
5. Send a confirmation to the borrower.
6. Alert Dennis with a concise opportunity summary.
7. Track the response and booking outcome.
## 16. Agrici Daniel learning path
### Official creator resources
- [Agrici Daniel’s official website](https://agricidaniel.com/) — includes current video demonstrations and links to his YouTube tutorials.
- [Agrici Daniel on YouTube](https://www.youtube.com/@AgriciDaniel) — tutorials and demonstrations of his Claude Code marketing systems.
- [Claude SEO GitHub repository](https://github.com/AgriciDaniel/claude-seo) — current installation, command reference and release documentation.
- [Claude Blog GitHub repository](https://github.com/AgriciDaniel/claude-blog) — research-first blog generation and optimization workflow.
### Recommended videos
#### 1. “Claude Code Just Replaced Your Entire SEO Stack”
**Why watch:** High-level demonstration of the Claude SEO toolset and its major audit capabilities.
**Apply to this project:** Use it to understand what can be automated, then define human approval gates for changes to the mortgage site.
#### 2. “Claude Code Just Replaced Your Blog Writer”
**Why watch:** Demonstrates the Claude Blog workflow for researching, drafting and optimizing content.
**Apply to this project:** Adapt the workflow to mortgage content briefs with Canadian primary sources, broker review and compliance checks.
#### 3. Claude SEO full demo linked from the repository
**Why watch:** Shows the `/seo audit` workflow and parallel specialist analysis.
**Apply to this project:** Run the audit against staging and production, then convert the output into prioritized implementation tasks.
#### 4. Claude Blog walkthrough linked from the repository
**Why watch:** Demonstrates the blog-delivery workflow and quality gates.
**Apply to this project:** Use the quality-gate concept for evidence, internal links, author review, disclosures and publication readiness.
> Video titles and repository links should be checked at the time of use because Daniel’s channel and tools are actively updated.
## 17. Suggested Claude Code prompts
### Project inspection
```plain text
Inspect this WordPress repository without changing files. Explain the current theme, plugins, build tooling, custom post types, Elementor dependencies, SEO configuration, security risks and the safest migration path to Gutenberg.
```
### Theme plan
```plain text
Create an implementation plan for a custom WordPress block theme for a BC mortgage brokerage. Use semantic HTML, accessible Gutenberg blocks, responsive CSS, Core Web Vitals best practices and reusable templates for articles, mortgage programs, locations and calculators. Do not modify files yet.
```
### First block
```plain text
Build an accessible reusable call-to-action Gutenberg block for a mortgage advisor. Include heading, supporting text, primary action, secondary action and optional trust note. Use TypeScript for the editor component, PHP render logic where appropriate, and scoped CSS. Add tests and documentation.
```
### Calculator specification
```plain text
Before coding, create a technical specification for a Canadian B-lender qualification assessment. Separate factual inputs, illustrative calculations, decision-support messaging, compliance disclaimers, consent and CRM submission. Identify every assumption requiring broker or legal review.
```
### SEO QA
```plain text
Audit the staging site for technical SEO, semantic HTML, internal links, structured data, performance, accessibility and content quality. Do not make changes. Return findings ranked by impact, confidence, effort, dependency and validation method.
```
## 18. Dependencies and risks
<table header-row="true">
<tr>
<td>Risk</td>
<td>Mitigation</td>
</tr>
<tr>
<td>Overbuilding before launch</td>
<td>Ship one content cluster and one assessment first</td>
</tr>
<tr>
<td>AI-generated factual errors</td>
<td>Require primary sources and broker review</td>
</tr>
<tr>
<td>Mortgage calculation errors</td>
<td>Unit tests, scenario tests and professional review</td>
</tr>
<tr>
<td>Elementor remnants</td>
<td>Dependency inventory and staged migration</td>
</tr>
<tr>
<td>Plugin conflicts</td>
<td>Minimal plugin set and staging validation</td>
</tr>
<tr>
<td>Lead-data exposure</td>
<td>Data minimization, secure transport and access controls</td>
</tr>
<tr>
<td>Search-quality risk from scaled content</td>
<td>Original expertise, useful tools, evidence and editorial QA</td>
</tr>
<tr>
<td>Uncontrolled Claude Code changes</td>
<td>Git branches, code review, backups and scoped prompts</td>
</tr>
</table>
## 19. MVP definition of done
The MVP is complete when:
- WordPress is operating on a custom Gutenberg block theme.
- Elementor is not required for new pages.
- Core content types and templates are usable by an editor.
- The B-lender and self-employed topic cluster is published.
- The B-lender assessment works on desktop and mobile.
- Calculator results are clearly labelled as illustrative.
- Consented submissions reach Supabase, CRM and n8n.
- Analytics tracks the complete acquisition-to-lead funnel.
- Technical SEO, accessibility and performance checks pass.
- Backup, deployment and rollback procedures are documented.
## 20. Next build decision
Begin with a **two-week foundation sprint** covering:
1. Staging and repository setup
2. Existing-site and Elementor dependency audit
3. Gutenberg theme design tokens and shell
4. WordPress content-model specification
5. B-lender assessment question and result logic
6. Claude SEO installation and baseline audit
## References
- [Agrici Daniel — official website and current video demonstrations](https://agricidaniel.com/)
- [Agrici Daniel — YouTube channel](https://www.youtube.com/@AgriciDaniel)
- [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo)
- [Claude SEO installation guide](https://github.com/AgriciDaniel/claude-seo/blob/main/docs/INSTALLATION.md)
- [AgriciDaniel/claude-blog](https://github.com/AgriciDaniel/claude-blog)
- [WordPress.com MCP documentation](https://developer.wordpress.com/docs/mcp/)
---
**Document status:** Initial PRD and implementation guide  
**Prepared for:** Dennis Eng  
**Last updated:** July 22, 2026
