# KlickSmartAI.com — GTM Engineering Platform Website Spec
## Version 1.0 | Based on PRD v1.0 | May 2026

---

## 1. Concept & Vision

**KlickSmartAI.com** is the GTM Engineering Consultancy — not an AI agency, not a marketing shop, not a CRM implementation vendor. It's a **revenue systems engineering firm** that combines GTM strategy, RevOps, AI automation, CRM architecture, and local SEO into a single predictable growth system for service businesses.

The site should feel like a **consultancy that ships** — authoritative enough to sell $25K–$100K engagements, technical enough to earn trust from founders and operators, and concrete enough to show exactly what gets built.

**Personality:** Confident. Systems-minded. No fluff. The site talks like an engineer who also happens to understand revenue.

---

## 2. Design Language

### Aesthetic Direction
**"Revenue Engineering"** — dark terminal meets modern SaaS dashboard. Think: a Bloomberg terminal redesigned by a product designer. Dense with signal, clean with intent. Not cold — professional warmth.

### Color Palette
- **Primary:** `#0A1628` (deep navy — authority, depth)
- **Accent:** `#00D4AA` (electric teal — the "signal" color, growth, automation)
- **Secondary:** `#3B82F6` (clear blue — trust, system, pipeline)
- **Warning/Alert:** `#F59E0B` (amber — revenue leaks, urgency)
- **Background:** `#0F172A` (dark slate — premium dark)
- **Surface:** `#1E293B` (card backgrounds)
- **Text Primary:** `#F8FAFC`
- **Text Secondary:** `#94A3B8`
- **Border:** `#334155`

### Typography
- **Display/Hero:** Inter, 72px/56px, weight 700–800, tight letter-spacing
- **Section Headings:** Inter, 36px/28px, weight 600
- **Body:** Inter, 16px/18px, weight 400
- **Labels/Tags:** JetBrains Mono, 12px, weight 500 (for the "engineered" feel — system labels, metric tags, stage indicators)
- **Fallbacks:** system-ui, -apple-system, sans-serif

### Spatial System
- Base unit: 8px
- Section padding: 96px top/bottom (64px mobile)
- Container max-width: 1200px
- Card padding: 32px
- Grid: 12-column, 24px gutters

### Motion Philosophy
- Entrance: fade-up, 400ms ease-out, 100ms stagger between cards
- Hover: subtle scale(1.02) + border glow on cards, 200ms
- Revenue engine diagram: stage indicators pulse on hover
- Counter animations on scroll (lead numbers, %, revenue)
- No decorative motion — every animation communicates something

### Visual Assets
- **Icons:** Phosphor Icons (duotone style) — consistent stroke, techy feel
- **Diagrams:** Custom SVG pipeline diagrams (Attract → Capture → Convert → Nurture → Reactivate → Optimize)
- **No stock photos** — use abstract geometric patterns, grid backgrounds, data visualizations
- **Charts:** Minimal SVG bar/line charts for metric displays

---

## 3. Layout & Structure

### Site Architecture
```
klicksmartai.com/
├── / (Home — hero + revenue engine + services + proof + CTA)
├── /gtm-revenue-audit (Revenue Audit product page)
├── /gtm-blueprint (GTM Blueprint product page)
├── /gtm-buildout (GTM Buildout product page)
├── /fractional-gtm (Fractional GTM Engineering page)
├── /case-studies (Social proof)
├── /about (Team / company story)
└── /contact (Qualification form)
```

### Home Page Structure (Priority)

**1. Navigation Bar** (sticky, 64px height)
- Logo: "KlickSmart" wordmark + GTM badge
- Nav links: Services | How It Works | Case Studies | About | Book a Call (CTA button, teal)
- Mobile: hamburger menu

**2. Hero Section** (100vh on desktop)
- Headline: "Engineered Revenue Growth for Service Businesses"
- Subheadline: "GTM Engineering that combines strategy, automation, and CRM architecture into a single predictable growth system."
- CTA: "Get Your Revenue Audit" (primary) | "See How It Works" (secondary/anchor)
- Background: subtle animated grid + floating pipeline stage indicators
- Trust bar: "Trusted by service businesses generating $250K–$10M"

**3. Problem Section** ("The Revenue Leak" — 3-column grid)
- 8 revenue leak icons with descriptions
- Amber accent color — urgency without alarm
- Subheadline: "Most service businesses are leaking revenue from 8 predictable points."

**4. Revenue Engine Section** (full-width, the centerpiece)
- Animated 6-stage pipeline diagram (SVG)
- Attract → Capture → Convert → Nurture → Reactivate → Optimize
- Each stage: icon + description + example automation
- "This is the system we'll build for you."

**5. Services Section** (4-column card grid)
- GTM Revenue Audit
- GTM Blueprint
- GTM Buildout
- Fractional GTM Engineering
- Each card: icon, title, 3 bullets, "Learn More" link

**6. Tech Stack Section** (dark section, logo grid)
- Layer labels: Strategy | Implementation | Automation | CRM | Data | Communication | Voice | Analytics
- Tool names in JetBrains Mono: ChatGPT, Claude, Claude Code, Codex, Python, n8n, GoHighLevel, HubSpot, Supabase, Twilio, Retell AI, ElevenLabs, Looker Studio
- Subheadline: "We use best-in-class tools. We engineer them into a system."

**7. Who It's For Section** (horizontal scroll on mobile)
- 9 vertical icons: Mortgage Brokers, Insurance Advisors, Financial Planners, Realtors, HVAC, Plumbing, Landscaping, Home Services, Medical Clinics
- "We specialize in service businesses. Your vertical is our next project."

**8. Success Metrics Section** (dark card grid)
- Animated counters: 95% see ROI in 30 days | 15+ hrs/week saved | 40% avg revenue increase | 50% faster response times | 300% more qualified leads | 80% reduction in manual tasks
- Source: PRD success metrics

**9. Process Section** (numbered steps, horizontal flow)
- Step 1: GTM Revenue Audit (identify)
- Step 2: GTM Blueprint (design)
- Step 3: GTM Buildout (implement)
- Step 4: Fractional GTM (optimize)
- Timeline: 90 days to a fully operational revenue system

**10. CTA Section** (full-width teal gradient)
- "Your Revenue System Starts Here"
- Primary CTA: "Get Your Free GTM Revenue Audit"
- Secondary: "Book a 30-Minute Strategy Call"
- Trust element: "No commitment. 5-minute assessment. Custom roadmap included."

**11. Footer**
- Logo + tagline
- Services links
- Resources links
- Contact info
- Social links (LinkedIn primary)
- Legal links

---

## 4. Features & Interactions

### Navigation
- Sticky on scroll with background blur
- Active section highlighting
- Mobile hamburger with slide-in panel
- "Book a Call" always visible (top-right CTA)

### Hero Section
- Animated background grid (CSS)
- Floating stage indicator badges that pulse
- Primary CTA → opens assessment form modal or navigates to /free-audit
- Secondary CTA → smooth scroll to Revenue Engine section

### Revenue Engine Diagram
- SVG pipeline with 6 stages
- Hover on each stage: expands to show 3 example automations
- On mobile: horizontal swipe carousel
- Each stage labeled in JetBrains Mono

### Service Cards
- Hover: lift + teal border glow + arrow slides right
- Click: navigates to service detail page

### Lead Counter Animation
- Triggers on scroll into viewport
- Counts up from 0 to target value over 1.5s
- Easing: ease-out

### Tech Stack Logo Grid
- Subtle hover on each logo: tooltip with tool description
- Logos displayed in monochrome, color on hover

### Contact/CTA Form
- Fields: Name, Email, Phone (optional), Company, Revenue Range (dropdown), Primary Challenge (multi-select), Message (optional)
- Validation: required fields highlighted in amber on empty submit
- Success: confirmation message + calendar invite offer
- Error: specific field-level error messages

### Mobile Responsive
- Breakpoints: 640px (sm), 768px (md), 1024px (lg), 1280px (xl)
- Hero text scales: 72px → 48px → 36px
- Revenue engine: becomes horizontal scroll
- Service grid: 4-col → 2-col → 1-col
- Nav: full-screen overlay menu

---

## 5. Component Inventory

### Navigation Bar
- States: default (transparent bg), scrolled (blur bg + border), mobile-open
- Logo: SVG wordmark
- Links: hover = teal underline slide-in
- CTA button: teal bg, white text, hover = slight glow

### Hero Badge
- Small pill: "GTM Engineering Consultancy"
- Teal bg, dark text, JetBrains Mono font

### Revenue Leak Card
- States: default, hover (lift + amber glow)
- Icon + title + description
- Amber left border accent

### Pipeline Stage Indicator
- States: default (dim), active (bright + pulse), hovered (expanded)
- Circle with icon + label below
- Connecting line between stages

### Service Card
- States: default, hover (lift + border glow + arrow right)
- Icon (48px) + title + 3 bullets + CTA link
- Dark surface bg with subtle border

### Tech Stack Badge
- Logo + tool name
- States: default (monochrome), hover (color + tooltip)

### Metric Counter
- Large number (Inter, 48px, bold, teal)
- Label below (secondary text)
- Animated count-up on scroll

### CTA Button
- Primary: teal bg, dark text, bold
- Secondary: transparent, teal border, teal text
- States: default, hover, active, loading, disabled

### Form Input
- States: default, focused (teal border), error (amber border + message), disabled
- Label above, helper text below
- Dark surface bg

### Footer
- 4-column grid (logo+tagline, services, resources, contact)
- Dark bg, subtle top border
- Social icons: LinkedIn primary

---

## 6. Technical Approach

### Stack
- **Next.js 14** (App Router) — for future blog/case study pages
- **TypeScript** — type safety
- **Tailwind CSS** — utility-first styling
- **Framer Motion** — page animations
- **Phosphor React** — icons
- **React Hook Form** — form handling
- **Zod** — validation
- **Resend** — email delivery
- **Vercel** — hosting + edge functions

### Architecture
```
/app
  /page.tsx (home)
  /gtm-revenue-audit/page.tsx
  /gtm-blueprint/page.tsx
  /gtm-buildout/page.tsx
  /fractional-gtm/page.tsx
  /contact/page.tsx
  /layout.tsx
  /globals.css

/components
  /navigation.tsx
  /hero.tsx
  /revenue-leaks.tsx
  /revenue-engine.tsx
  /services-grid.tsx
  /tech-stack.tsx
  /verticals.tsx
  /metrics.tsx
  /process-steps.tsx
  /cta-section.tsx
  /footer.tsx
  /ui (button, card, input, badge, etc.)

/lib
  /utils.ts
  /constants.ts
```

### Performance Targets
- LCP < 2.5s
- FID < 100ms
- CLS < 0.1
- Lighthouse Performance > 95

### SEO
- Meta tags per page
- Open Graph images
- Structured data (Organization, Service, FAQPage)
- Sitemap.xml
- robots.txt

### Analytics
- Google Analytics 4
- Google Tag Manager
- Microsoft Clarity (optional)

### Forms
- Server actions for form submission
- Zod validation on both client and server
- Resend for email notifications
- HubSpot/GoHighLevel webhook for CRM entry

---

## 7. Copy Guidelines

### Voice
- First person plural: "We engineer revenue systems"
- Specific, not vague: "AI Voice Agents that answer 24/7" not "AI-powered solutions"
- Confidence without arrogance: "We build the system. You run the business."
- No jargon without explanation

### Headlines
- Benefit-led: "Engineered Revenue Growth" not "GTM Engineering Services"
- Specific numbers when possible: "95% of clients see ROI in 30 days"
- Problem-aware: "Stop leaking revenue from 8 predictable points"

### CTAs
- Action-oriented: "Get Your Revenue Audit" not "Learn More"
- Low-friction: "Start Free" | "No Commitment" | "5 Minutes"
- Outcome-focused: "See Your Revenue Opportunity" | "Build Your 90-Day Plan"

### Avoid
- "We help businesses..." → "Service businesses generate..."
- "Cutting-edge AI" → name the tool and what it does
- "End-to-end solutions" → "We build the whole system"
- Generic claims without proof

---

## 8. Page-Specific Notes

### /gtm-revenue-audit
- Full description of the audit process
- What you get: Lead Source Analysis, CRM Audit, GBP Audit, Revenue Leak Report
- Pricing: "Starting at $2,500" or "From $2,500 — completed in 5 business days"
- Form to request audit

### /gtm-blueprint
- The 90-day roadmap deliverable
- Journey mapping, funnel architecture, KPI framework
- "From audit to blueprint in 10 business days"

### /gtm-buildout
- Implementation phase
- CRM config, AI agents, workflows, landing pages
- "We build it. We train your team. We launch."

### /fractional-gtm
- Monthly retainer model
- Ongoing optimization, strategic planning, reporting
- "Your fractional GTM engineer on retainer"

### /contact
- Qualification form (company size, revenue, primary challenge)
- Calendly embed or redirect for booking
- Response time promise: "We respond within 1 business hour"
