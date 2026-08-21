# LeadSniper 3.0 - Stripe Payment Integration Plan

## Executive Summary

Implement dual billing model:
1. **Subscription Plans** - Monthly recurring revenue
2. **Pay-Per-Use** - Usage-based metering for lead generation

---

## Pricing Strategy

### Subscription Tiers

#### 1. **Starter Plan** - $49/month
- 100 leads per month
- Basic lead enrichment
- Email generation (AI)
- Cold call scripts
- Standard support
- **Best for:** Solo entrepreneurs, freelancers

#### 2. **Professional Plan** - $149/month
- 500 leads per month
- Advanced enrichment (DataForSEO integration)
- SEO audit reports
- Social media lookup
- Priority support
- CSV bulk import/export
- **Best for:** Small agencies, sales teams

#### 3. **Agency Plan** - $399/month
- 2,000 leads per month
- Everything in Professional
- White-label options
- API access
- Dedicated support
- Custom integrations
- **Best for:** Marketing agencies, enterprise sales

#### 4. **Enterprise Plan** - Custom Pricing
- Unlimited leads
- Custom features
- Dedicated account manager
- SLA guarantees
- On-premise deployment options

### Pay-Per-Use Pricing

**Pay As You Go** (No monthly commitment)
- $1.50 per lead searched
- $0.50 per lead enriched (social media + SEO)
- $0.20 per email generated
- $0.20 per call script generated

**Credits System:**
- Users purchase credit packs
- Credits never expire
- Volume discounts available

**Credit Packs:**
- 50 credits: $75 ($1.50 per credit)
- 200 credits: $250 ($1.25 per credit)
- 500 credits: $500 ($1.00 per credit)
- 1000 credits: $800 ($0.80 per credit)

---

## Technical Architecture

### Backend Requirements

#### 1. **Node.js/Express API Server**

```
leadsniper-backend/
├── src/
│   ├── routes/
│   │   ├── auth.ts          # User authentication
│   │   ├── subscription.ts  # Subscription management
│   │   ├── usage.ts         # Usage tracking
│   │   └── webhook.ts       # Stripe webhooks
│   ├── middleware/
│   │   ├── auth.ts          # JWT verification
│   │   ├── rateLimit.ts     # Rate limiting
│   │   └── usage.ts         # Usage metering
│   ├── services/
│   │   ├── stripe.ts        # Stripe SDK integration
│   │   ├── database.ts      # Database operations
│   │   └── metering.ts      # Usage tracking
│   └── models/
│       ├── User.ts          # User model
│       ├── Subscription.ts  # Subscription model
│       └── Usage.ts         # Usage records
```

#### 2. **Database Schema (PostgreSQL/MongoDB)**

```sql
-- Users Table
CREATE TABLE users (
    id UUID PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    stripe_customer_id VARCHAR(255),
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Subscriptions Table
CREATE TABLE subscriptions (
    id UUID PRIMARY KEY,
    user_id UUID REFERENCES users(id),
    stripe_subscription_id VARCHAR(255) UNIQUE,
    plan_id VARCHAR(50), -- 'starter', 'pro', 'agency'
    status VARCHAR(50),  -- 'active', 'canceled', 'past_due'
    current_period_start TIMESTAMP,
    current_period_end TIMESTAMP,
    leads_quota INTEGER,
    leads_used INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Usage Records Table (for pay-per-use)
CREATE TABLE usage_records (
    id UUID PRIMARY KEY,
    user_id UUID REFERENCES users(id),
    action_type VARCHAR(50), -- 'lead_search', 'enrichment', 'email_gen'
    quantity INTEGER DEFAULT 1,
    cost DECIMAL(10, 2),
    metadata JSONB,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Credits Table (for pay-per-use)
CREATE TABLE credits (
    id UUID PRIMARY KEY,
    user_id UUID REFERENCES users(id),
    credits_purchased INTEGER,
    credits_remaining INTEGER,
    stripe_payment_intent_id VARCHAR(255),
    created_at TIMESTAMP DEFAULT NOW()
);
```

---

## Implementation Phases

### Phase 1: Foundation (Week 1-2)

**Backend Setup:**
- [ ] Set up Express.js API server
- [ ] Configure PostgreSQL/MongoDB database
- [ ] Implement user authentication (JWT)
- [ ] Set up Stripe account and API keys

**Stripe Configuration:**
```bash
# Install Stripe SDK
npm install stripe @stripe/stripe-js

# Environment variables
STRIPE_SECRET_KEY=sk_test_...
STRIPE_PUBLISHABLE_KEY=pk_test_...
STRIPE_WEBHOOK_SECRET=whsec_...
```

**Files to Create:**
- `backend/src/config/stripe.ts` - Stripe initialization
- `backend/src/routes/auth.ts` - User registration/login
- `backend/src/middleware/auth.ts` - JWT verification

---

### Phase 2: Subscription System (Week 3-4)

**Stripe Products Setup:**

```typescript
// Create products and prices in Stripe
const products = [
  {
    name: 'Starter Plan',
    price: 4900, // $49.00
    interval: 'month',
    features: {
      leads_quota: 100,
      enrichment: 'basic',
      support: 'standard'
    }
  },
  {
    name: 'Professional Plan',
    price: 14900, // $149.00
    interval: 'month',
    features: {
      leads_quota: 500,
      enrichment: 'advanced',
      support: 'priority'
    }
  },
  {
    name: 'Agency Plan',
    price: 39900, // $399.00
    interval: 'month',
    features: {
      leads_quota: 2000,
      enrichment: 'advanced',
      support: 'dedicated'
    }
  }
];
```

**Implementation Tasks:**
- [ ] Create Stripe products and prices
- [ ] Build subscription checkout flow
- [ ] Implement subscription management API
- [ ] Handle plan upgrades/downgrades
- [ ] Quota tracking and enforcement

**API Endpoints:**
```
POST   /api/subscriptions/create-checkout
POST   /api/subscriptions/upgrade
POST   /api/subscriptions/cancel
GET    /api/subscriptions/current
GET    /api/subscriptions/usage
```

---

### Phase 3: Pay-Per-Use System (Week 5-6)

**Stripe Metering Setup:**

```typescript
// Usage-based billing configuration
const usagePrices = {
  lead_search: 150,      // $1.50 in cents
  lead_enrichment: 50,   // $0.50
  email_generation: 20,  // $0.20
  script_generation: 20  // $0.20
};
```

**Implementation Tasks:**
- [ ] Implement credit purchase flow
- [ ] Build usage tracking middleware
- [ ] Create metering service
- [ ] Implement credit balance checks
- [ ] Auto-deduction on actions

**Credit System Flow:**
```
1. User purchases credit pack
2. Credits stored in database
3. Each action checks credit balance
4. Deduct credits on successful action
5. Show low balance warnings
```

---

### Phase 4: Frontend Integration (Week 7-8)

**New Components to Build:**

```typescript
// components/pricing/
├── PricingTable.tsx       // Subscription plans display
├── CheckoutButton.tsx     // Stripe checkout trigger
├── SubscriptionCard.tsx   // Current plan display
├── UsageStats.tsx         // Usage metrics dashboard
├── CreditBalance.tsx      // Credit display/purchase
└── BillingPortal.tsx      // Manage billing
```

**User Dashboard Additions:**
- Subscription status indicator
- Usage meter (leads used / quota)
- Credit balance display
- Billing history
- Payment method management

---

### Phase 5: Webhook Handling (Week 9)

**Critical Webhooks to Handle:**

```typescript
// backend/src/routes/webhook.ts
const webhookHandlers = {
  'customer.subscription.created': handleSubscriptionCreated,
  'customer.subscription.updated': handleSubscriptionUpdated,
  'customer.subscription.deleted': handleSubscriptionCanceled,
  'invoice.payment_succeeded': handlePaymentSuccess,
  'invoice.payment_failed': handlePaymentFailed,
  'customer.updated': handleCustomerUpdated
};
```

**Webhook Implementation:**
- [ ] Set up webhook endpoint
- [ ] Verify webhook signatures
- [ ] Handle subscription lifecycle events
- [ ] Update database on webhook events
- [ ] Send email notifications

---

## User Experience Flow

### Subscription Flow

```
1. User signs up (free trial or paid)
   ↓
2. Select plan on pricing page
   ↓
3. Redirect to Stripe Checkout
   ↓
4. Complete payment
   ↓
5. Webhook activates subscription
   ↓
6. Redirect to dashboard (quota active)
   ↓
7. User generates leads (quota tracked)
   ↓
8. Warning at 80% quota usage
   ↓
9. Hard limit at 100% (prompt to upgrade)
```

### Pay-Per-Use Flow

```
1. User signs up
   ↓
2. Purchase credit pack
   ↓
3. Credits added to account
   ↓
4. Each action deducts credits
   ↓
5. Low balance warning (< 10 credits)
   ↓
6. Prompt to purchase more credits
```

---

## Security Considerations

### Payment Security
- [ ] Never store credit card details (Stripe handles)
- [ ] Use Stripe Elements for PCI compliance
- [ ] Implement webhook signature verification
- [ ] Secure API endpoints with authentication
- [ ] Rate limiting on payment endpoints

### Data Protection
- [ ] Encrypt sensitive user data
- [ ] GDPR compliance for EU customers
- [ ] Secure database connections
- [ ] Regular security audits
- [ ] PCI DSS compliance

---

## Testing Strategy

### Test Modes
```env
# Development
STRIPE_SECRET_KEY=sk_test_...
STRIPE_PUBLISHABLE_KEY=pk_test_...

# Production
STRIPE_SECRET_KEY=sk_live_...
STRIPE_PUBLISHABLE_KEY=pk_live_...
```

### Test Scenarios
- [ ] Successful subscription purchase
- [ ] Failed payment handling
- [ ] Plan upgrade/downgrade
- [ ] Subscription cancellation
- [ ] Credit purchase and deduction
- [ ] Webhook event handling
- [ ] Quota enforcement
- [ ] Refund processing

**Test Cards:**
- Success: `4242 4242 4242 4242`
- Decline: `4000 0000 0000 0002`
- 3D Secure: `4000 0027 6000 3184`

---

## Cost Analysis

### Development Costs
- Backend development: 40-60 hours
- Frontend integration: 20-30 hours
- Testing & QA: 15-20 hours
- **Total:** 75-110 hours (~2-3 weeks)

### Stripe Fees
- **Standard:** 2.9% + $0.30 per transaction
- **Subscriptions:** Same as above
- **Metered billing:** 0.8% on metered amount (min $0.01)

**Example Revenue:**
- $149/month subscription = $144.68 after fees
- $100 credit purchase = $97.10 after fees

---

## Launch Checklist

### Pre-Launch
- [ ] Complete development and testing
- [ ] Set up production Stripe account
- [ ] Configure live API keys
- [ ] Test all webhook events
- [ ] Set up monitoring and alerts
- [ ] Create billing documentation
- [ ] Prepare customer support materials

### Launch
- [ ] Switch to live Stripe keys
- [ ] Enable payment processing
- [ ] Monitor first transactions closely
- [ ] Be ready for support requests
- [ ] Track key metrics

### Post-Launch
- [ ] Monitor churn rate
- [ ] Analyze conversion rates
- [ ] Gather user feedback
- [ ] Optimize pricing
- [ ] Add requested features

---

## Metrics to Track

### Business Metrics
- Monthly Recurring Revenue (MRR)
- Customer Acquisition Cost (CAC)
- Customer Lifetime Value (LTV)
- Churn rate
- Conversion rate (free → paid)

### Technical Metrics
- Payment success rate
- Webhook delivery success
- API response times
- Error rates
- Quota utilization

---

## Next Steps

**Immediate Actions:**
1. Create Stripe account
2. Set up test products and prices
3. Build backend authentication system
4. Design subscription UI mockups
5. Set up development database

**Timeline:**
- Week 1-2: Foundation + Auth
- Week 3-4: Subscription system
- Week 5-6: Pay-per-use system
- Week 7-8: Frontend integration
- Week 9: Testing & launch preparation
- Week 10: Soft launch + monitoring

---

**Status:** Planning Complete ✅
**Ready to Implement:** Yes
**Estimated Timeline:** 10 weeks
**Investment Required:** Development + Stripe fees
