# DCP — Real Estate Software: Build & Scope Decision Procedure

**Date**: 2026-01-31
**Input**: All things real estate — finding properties, managing properties, evaluating properties, valuing properties — and how to make the best possible software for it

---

## Step 1: Decision Dimensions (`/dd`)

### Dimension 1: Problem Domain Focus
**Why it matters**: "All things real estate" is too broad to build well. The best software solves one problem domain deeply before expanding.
- **Finding** (search, discovery, lead gen, MLS integration)
- **Evaluating** (comps, market analysis, due diligence checklists)
- **Valuing** (appraisal models, ARV, cap rate, DCF, rent estimation)
- **Managing** (tenant tracking, maintenance, rent collection, accounting)
- **Transacting** (offers, contracts, closing coordination)

### Dimension 2: User Type
**Why it matters**: Software that tries to serve everyone serves no one. Different users have fundamentally different workflows.
- Individual investor (1-10 properties)
- Portfolio investor (10-100 properties)
- Institutional investor (100+ properties)
- Real estate agent/broker
- Property manager (managing for others)
- Wholesaler
- Developer/flipper

### Dimension 3: Property Type
**Why it matters**: Residential SFR, multifamily, commercial, and land each have different data sources, valuation methods, and management needs.
- Single-family residential (SFR)
- Small multifamily (2-4 units)
- Large multifamily (5+ units)
- Commercial (retail, office, industrial)
- Land / development
- Mixed-use

### Dimension 4: Market Geography
**Why it matters**: Data availability, legal requirements, and MLS structures vary dramatically by country and even by county.
- Single metro area
- Single state
- Multi-state / national (US)
- International

### Dimension 5: Data Source Strategy
**Why it matters**: Real estate software lives or dies by its data. This is the #1 technical differentiator.
- MLS API access (requires licensing, varies by board)
- Public records / county assessor data
- Third-party aggregators (ATTOM, CoreLogic, Zillow API)
- User-submitted / manual entry
- Scraped data (legal risk)
- Proprietary data collection

### Dimension 6: Competitive Positioning
**Why it matters**: The market has strong incumbents. Your angle determines everything about what to build.
- Better UX on existing workflow (Zillow-killer)
- Novel analysis not available elsewhere (new valuation model)
- Integration hub (connect fragmented tools)
- Vertical niche (e.g., mobile home parks only)
- Automation play (eliminate manual steps)
- Data advantage (access data others don't have)

### Dimension 7: Revenue Model
**Why it matters**: Determines feature gating, pricing, data costs you can absorb, and growth strategy.
- SaaS subscription (per user or per property)
- Transaction-based (per deal closed)
- Freemium with premium analytics
- Marketplace / lead generation fees
- Data licensing
- White-label for brokerages

### Dimension 8: Technical Architecture
**Why it matters**: Wrong architecture early means rewrite later. Must match scale ambitions.
- Monolith (fast to ship, harder to scale)
- Microservices (slower to ship, scales independently)
- Serverless (low ops cost, cold start issues for heavy computation)
- Hybrid (monolith + specific services for heavy compute like valuations)

### Dimension 9: Build vs. Buy vs. Integrate
**Why it matters**: For each capability, you must decide whether to build from scratch, buy/license, or integrate an existing service.
- Core differentiator → build
- Commodity feature → buy/integrate
- Regulated/compliance feature → buy (liability transfer)

### Dimension 10: Regulatory & Compliance Scope
**Why it matters**: Real estate is heavily regulated. Fair Housing, data privacy, licensing requirements, and financial regulations all constrain what you can build and how.
- Fair Housing Act compliance (advertising, screening)
- State-specific landlord-tenant law
- Financial data regulations (if handling payments)
- Data privacy (CCPA, state laws)
- MLS rules and restrictions on data display

### Dimension 11: Moat Strategy
**Why it matters**: Without a defensible advantage, you're building a feature that Zillow/Redfin/AppFolio will copy.
- Network effects (marketplace, user-generated data)
- Data compounding (more users → better models)
- Switching costs (deep workflow integration)
- Proprietary algorithms (valuation IP)
- Regulatory moat (licensed access others can't get)

### Dimension 12: Stage of Development
**Why it matters**: What you build first determines whether you survive to build the rest.
- Validation (landing page + manual backend)
- MVP (one domain, one user type, one geography)
- Growth (expanding domains/users/geographies)
- Scale (platform/ecosystem play)

---

## Step 2: Option Space Map (`/se`)

| Dimension | Values | Interactions |
|---|---|---|
| **Domain Focus** | Find / Evaluate / Value / Manage / Transact | If Manage → need Property Type. If Value → need Data Source. |
| **User Type** | Individual investor / Portfolio / Institutional / Agent / PM / Wholesaler / Developer | Institutional → needs API + bulk ops. Individual → needs simplicity. |
| **Property Type** | SFR / Small MF / Large MF / Commercial / Land / Mixed | Commercial → different valuation (NOI-based). SFR → comp-based. |
| **Geography** | Metro / State / National / International | National → must handle 600+ MLS boards. Metro → can hand-curate data. |
| **Data Source** | MLS / Public records / Aggregators / Manual / Scraped / Proprietary | MLS requires board-by-board licensing ($$$). Public records = free but messy. |
| **Positioning** | Better UX / Novel analysis / Integration hub / Vertical niche / Automation / Data advantage | Vertical niche = fastest to defensibility. Better UX = hardest. |
| **Revenue** | SaaS / Transaction / Freemium / Marketplace / Data licensing / White-label | Transaction = aligned but lumpy. SaaS = predictable but must prove daily value. |
| **Architecture** | Monolith / Microservices / Serverless / Hybrid | MVP → Monolith. Scale → Hybrid. Never start with microservices. |
| **Build/Buy** | Build core / Buy commodity / Integrate regulated | Valuation models = build. Payments = buy (Stripe). Background checks = integrate. |
| **Compliance** | Fair Housing / Landlord-tenant / Financial / Privacy / MLS rules | If managing → landlord-tenant is critical. If advertising → Fair Housing is critical. |
| **Moat** | Network / Data compound / Switching cost / Algorithm / Regulatory | Data compounding = strongest long-term. Switching costs = fastest to establish. |
| **Stage** | Validation / MVP / Growth / Scale | MUST go in order. Skipping validation is the #1 startup death cause. |

### Critical Interaction Rules
- If **User = Individual investor** AND **Domain = Find + Value**, you're competing with BiggerPockets + Zillow. Need a novel angle.
- If **Geography = National** AND **Data = MLS**, budget $50K-200K/year for data licensing alone.
- If **Domain = Manage** AND **Property = Commercial**, you're competing with Yardi/MRI — massive incumbents.
- If **Stage = Validation**, your **Architecture** choice doesn't matter. Use whatever ships fastest.

---

## Step 3: Hidden Assumptions (`/aex`)

**A1: "More features = better software"**
Reality: The graveyard of real estate startups is full of products that tried to do everything. The best software each started with ONE thing done exceptionally well.

**A2: "I need MLS data to compete"**
Reality: MLS data is expensive, restricted, and comes with display rules that limit your UX. Many successful products use public records + user-contributed data instead.

**A3: "The technology is the hard part"**
Reality: The hard parts are (1) data acquisition and quality, (2) distribution/user acquisition, and (3) regulatory compliance. The code is the easy part.

**A4: "I should build a platform from day one"**
Reality: Platforms emerge from successful point solutions. Build one tool that one user type loves, then expand.

**A5: "Real estate professionals will adopt new software easily"**
Reality: Real estate is one of the most technologically conservative industries. Adoption requires either 10x improvement on a pain point or integration with existing workflows.

**A6: "My valuation model will be more accurate than Zillow's Zestimate"**
Reality: Zillow has billions of data points and hundreds of ML engineers. Compete on *specificity* (better for a niche) or *transparency* (show your work, let users adjust inputs).

**A7: "I can build this as a solo developer"**
Reality: The data pipeline alone for real estate data is a full-time job. You need at minimum: one person on data, one on product/frontend, one on distribution.

**A8: "SaaS subscription is the obvious revenue model"**
Reality: Most individual investors won't pay monthly for software they use sporadically. Transaction-based or per-deal pricing often converts better.

**A9: "The US market is one market"**
Reality: Real estate is hyper-local. Laws, data formats, market dynamics, and terminology vary by state and even county.

**A10: "AI/ML will be my differentiator"**
Reality: AI is a feature, not a product. If your only differentiator is "we use AI," you'll be copied in months.

---

## Step 4: The Decision Procedure (`/stg`)

```
REAL ESTATE SOFTWARE SCOPING & BUILD PROCEDURE
===============================================

WHO THIS IS FOR: Anyone deciding what real estate software to build.
WHAT YOU'LL GET: A specific, defensible product scope with clear build priorities.
TIME NEEDED: 2-4 hours to work through. Do not rush.

═══════════════════════════════════════════════
STEP 0: WHAT TYPE OF BUILDER ARE YOU?
═══════════════════════════════════════════════

Answer this question: How many people will work on this full-time
for the first 6 months?

  → 1 person           → You are a SOLO BUILDER.    Go to SECTION A.
  → 2-5 people         → You are a SMALL TEAM.      Go to SECTION B.
  → 6-20 people        → You are a FUNDED STARTUP.  Go to SECTION C.
  → 20+ or enterprise  → You are a COMPANY.         Go to SECTION D.

═══════════════════════════════════════════════
SECTION A: SOLO BUILDER
═══════════════════════════════════════════════

Step A1: Pick ONE domain from this list. Circle it.
  □ Finding properties (search, alerts, lead generation)
  □ Evaluating deals (analysis, comps, due diligence)
  □ Valuing properties (automated estimates, rent projections)
  □ Managing properties (tenants, maintenance, accounting)
  □ Transacting (offers, contracts, closing)

  RULE: You MUST pick exactly one. If you circled more than one,
  cross out all but the one where you have the most personal
  experience or frustration.

Step A2: Pick ONE user type. This is your first customer.
  □ Individual investor buying 1-10 properties
  □ Real estate agent/broker
  □ Property manager
  □ Wholesaler
  □ House flipper

  RULE: Pick the user type you either ARE or have direct access to
  10+ people who are this type. If neither, STOP — you need to
  go talk to real estate professionals before building anything.

Step A3: Pick ONE property type.
  □ Single-family homes
  □ Small multifamily (2-4 units)
  □ Large multifamily (5+ units)
  □ Commercial

  RULE: Pick what your user type from A2 most commonly works with.

Step A4: Pick ONE metro area to start.
  Write it here: _______________

  RULE: Pick a metro where you live or have direct connections.
  You will need to manually verify your data against this market.

Step A5: VALIDATION CHECK (Do not skip)
  Before writing any code, do ALL of the following:
  □ Interview 10 people who match your user type (A2)
  □ Ask each: "What is the most painful part of [domain from A1]?"
  □ Ask each: "What tools do you currently use? What do you hate?"
  □ Ask each: "Would you pay $X/month for [your idea]?"
  □ Write down the 3 most common pain points

  WHERE TO FIND INTERVIEWEES: BiggerPockets forums, local real
  estate investor meetups (meetup.com), Facebook groups for
  "[your metro] real estate investors," LinkedIn search, local
  REIA meetings.

  HOW TO ASK: "I'm building software for [user type] and I'd love
  15 minutes to understand your workflow. No pitch, just questions."
  Offer a $10 coffee gift card.

  RED FLAG: If you can't find 10 people to talk to, you don't
  understand your market well enough to build for it.

  CHECKPOINT: Did at least 5 of 10 people describe the SAME pain?
    → YES: Proceed to A6.
    → NO: Go back to A1 and pick a different domain, or refine
      your user type. Repeat A5.

Step A6: Define your ONE killer feature.
  Complete this sentence:
  "[User type] currently does [painful task] using [current tool].
  My software will [specific improvement] by [how]."

  RULE: The improvement must be measurable. Not "better" or
  "easier" — it must be "50% faster" or "eliminates 3 manual
  steps" or "catches errors that cost $X."

Step A7: Data source decision.
  For your domain + geography, what data do you need?
  For EACH data need, check ONE source:

  | Data needed          | Public records | Third-party API | User enters | I collect |
  |----------------------|----------------|-----------------|-------------|-----------|
  | Property details     | □              | □               | □           | □         |
  | Sale history         | □              | □               | □           | □         |
  | Rental comps         | □              | □               | □           | □         |
  | Owner information    | □              | □               | □           | □         |
  | Market trends        | □              | □               | □           | □         |
  | [Your specific need] | □              | □               | □           | □         |

  RULE: For MVP, prefer "User enters" or "Public records."
  Third-party APIs cost money and add complexity.
  "I collect" means you scrape or manually gather — do this
  ONLY if it's your core differentiator.

Step A8: Technology choice.
  → Use whatever language/framework you know best.
  → Build a monolith. Not microservices. Not serverless.
  → Use PostgreSQL for your database (it has PostGIS for
    geographic queries, which you WILL need).
  → Ship a web app first. Not mobile.

  RULE: If you spent more than 1 day choosing your tech stack,
  you are procrastinating. Pick and move.

Step A9: Build sequence.
  Build in this EXACT order:
  1. Data model for properties in your metro (A4)
  2. Manual data entry for 20 real properties
  3. Your ONE killer feature (A6) working on those 20 properties
  4. User accounts and authentication
  5. Your data pipeline (A7) for automated ingestion
  6. Basic UI polish
  7. Payment/subscription

  CHECKPOINT: After step 3, show it to 5 of your interviewees.
    → 3+ say "I want to use this now": Continue to step 4.
    → Fewer than 3: Your killer feature isn't killer. Go back to
      A5 and re-interview.

Step A10: Revenue model for solo builder.
  Match your domain:
  → Finding: Per-lead or per-deal pricing
  → Evaluating: Per-report pricing ($5-25/report)
  → Valuing: Freemium (basic free, detailed paid)
  → Managing: Per-unit/month ($5-15/unit)
  → Transacting: Per-transaction fee

→ Go to SECTION E (Common Steps).

═══════════════════════════════════════════════
SECTION B: SMALL TEAM (2-5 people)
═══════════════════════════════════════════════

Step B1: Complete Steps A1 through A6 from Section A.
  RULE: Even with more people, start with ONE domain, ONE user,
  ONE property type, ONE metro. More people = faster execution,
  NOT wider scope.

Step B2: Assign roles.
  You need exactly these roles covered (one person can cover
  multiple):
  □ Data person — owns data pipeline, quality, sourcing
  □ Product person — owns UX, user interviews, feature decisions
  □ Engineering person — owns architecture, code quality, shipping
  □ Distribution person — owns user acquisition, marketing, sales

  MISSING A ROLE? If nobody owns distribution, you will build
  something nobody finds. This is the most commonly missing role.

Step B3: Data source decision (expanded from A7).
  With a team, you can handle more complexity:
  □ Public records + county assessor scraping (assign to data person)
  □ Third-party API (budget: $500-2000/month for ATTOM or similar)
  □ MLS access (ONLY if you have a licensed broker on team or as
    advisor who can get you IDX/RETS access)

  RULE: Get your data pipeline producing clean, reliable data for
  your ONE metro before expanding to a second metro.

Step B4: Architecture decision.
  → Start monolith (same as solo).
  → BUT: design your data layer to be extractable.
  → Use a job queue (Redis/Sidekiq, Celery, BullMQ) for data
    ingestion from day 1.
  → Set up CI/CD from day 1.

Step B5: 90-Day milestone plan.
  Days 1-30:   Validation (A5) + data pipeline for 1 metro
  Days 31-60:  Killer feature (A6) working with real data
  Days 61-90:  10 paying users in your target metro

  CHECKPOINT at Day 90: Do you have 10 paying users?
    → YES: Proceed to growth. Consider expanding to adjacent metro
      or adding second domain.
    → NO: Diagnose. Is it the product (people try but don't pay)?
      Or distribution (people don't find it)? Fix that before
      adding features.

Step B6: Revenue model for small team.
  Same as A10, but add:
  → Consider annual billing with discount (improves cash flow)
  → Consider a free tier with usage limits (improves distribution)
  → RULE: Price 2x what feels comfortable. You can always discount.

→ Go to SECTION E (Common Steps).

═══════════════════════════════════════════════
SECTION C: FUNDED STARTUP (6-20 people)
═══════════════════════════════════════════════

Step C1: Complete Steps A1-A6, then B2-B3.

Step C2: Competitive positioning decision.
  With funding, you need a defensible position. Pick ONE:
  □ Vertical niche — serve one property type or user type better
    than anyone
  □ Data advantage — acquire or generate data that competitors
    can't easily replicate
  □ Integration hub — become the glue between fragmented tools
  □ Automation — eliminate manual steps that currently require
    humans

  RULE: "Better UX" alone is NOT a viable position at this stage.
  You need a structural advantage.

Step C3: Moat-building plan.
  Based on C2, your moat strategy is:

  | Position         | Primary moat        | How to build it                     |
  |------------------|---------------------|-------------------------------------|
  | Vertical niche   | Switching costs     | Deep workflow integration, custom    |
  |                  |                     | data fields, industry partnerships   |
  | Data advantage   | Data compounding    | Every user action improves models,   |
  |                  |                     | proprietary data collection          |
  | Integration hub  | Network effects     | Two-sided: tools want your users,    |
  |                  |                     | users want your tool connections      |
  | Automation       | Proprietary algo    | Invest in ML/AI for specific tasks,  |
  |                  |                     | build training data flywheel          |

Step C4: Architecture for scale.
  → Monolith for application layer
  → Separate services for: (1) data ingestion pipeline,
    (2) computation/valuation engine, (3) search/matching
  → PostgreSQL + PostGIS for primary data
  → Elasticsearch or similar for search
  → Data warehouse (BigQuery/Snowflake) for analytics
  → Event bus (Kafka/SQS) between services

Step C5: Compliance checklist.
  Before launching, verify ALL that apply:
  □ Fair Housing: Does any feature filter by race, religion,
    familial status, disability, or proxies thereof? → REMOVE IT
  □ Data display: If using MLS data, have you complied with ALL
    display rules for your board? → GET LEGAL REVIEW
  □ Privacy: Are you storing personal data? → IMPLEMENT data
    deletion, privacy policy, opt-out mechanisms
  □ Financial: Are you handling money? → USE a licensed payment
    processor, do not hold funds yourself
  □ Licensing: Does your product give "advice"? → ADD disclaimers,
    consult attorney about broker/appraiser licensing requirements

Step C6: Hiring priorities.
  Hire in this order (after founding team):
  1. Data engineer (your product IS your data)
  2. Designer (real estate professionals judge by appearance)
  3. Sales/BD (for partnerships, MLS access, enterprise deals)
  4. ML engineer (only AFTER you have clean data + clear use case)
  5. Mobile developer (only AFTER web product has traction)

→ Go to SECTION E (Common Steps).

═══════════════════════════════════════════════
SECTION D: COMPANY (20+ people / enterprise)
═══════════════════════════════════════════════

Step D1: Platform strategy.
  At this scale, you're building a platform. Choose your
  expansion model:
  □ Horizontal: Same user type, add domains
  □ Vertical: Same domain, add user types
  □ Geographic: Same product, add markets

  RULE: Expand on ONE axis at a time. Never two simultaneously.

Step D2: Build-vs-buy matrix.

  | Capability           | Build if...           | Buy/integrate if...        |
  |----------------------|-----------------------|----------------------------|
  | Property search      | It's your core product| You're a PM tool           |
  | Valuation models     | Data advantage play   | Not your differentiator    |
  | Payment processing   | Never build this      | Always (Stripe/Dwolla)     |
  | Background checks    | Never build this      | Always (TransUnion/etc)    |
  | Document generation  | High volume           | Low volume                 |
  | Accounting           | PM is your core       | Otherwise integrate QB     |
  | CRM                  | Agent-focused product | Otherwise integrate        |
  | Marketing/listings   | Distribution play     | Otherwise use Syndication  |
  | Maintenance mgmt     | PM is your core       | Otherwise integrate        |

Step D3: API-first architecture.
  → Every feature must have an API before it has a UI
  → This enables: white-labeling, partnerships, integrations,
    mobile apps, third-party developers
  → Publish API documentation from day 1 of each feature

Step D4: Multi-market data strategy.
  → Build a data normalization layer that maps every source to
    a canonical schema
  → Create a "market launch playbook" that documents exactly
    what's needed to add a new metro
  → Target: add a new metro in < 2 weeks once playbook exists

→ Go to SECTION E (Common Steps).

═══════════════════════════════════════════════
SECTION E: COMMON STEPS (All builders)
═══════════════════════════════════════════════

Step E1: Name your product.
  Requirements:
  □ .com domain available (or reasonable alternative)
  □ Not confusingly similar to existing real estate tools
  □ Easy to spell over the phone
  □ Doesn't include "real estate" or "property" (too generic)

Step E2: Define your launch metrics.

  | Domain    | Key metric                        |
  |-----------|-----------------------------------|
  | Finding   | # of qualified leads generated    |
  | Evaluating| # of analyses completed           |
  | Valuing   | Accuracy vs. actual sale price    |
  | Managing  | # of units under management       |
  | Transacting| # of deals closed through platform|

Step E3: User feedback loop.
  Set up BEFORE launching:
  □ In-app feedback widget
  □ Weekly call with 2-3 active users
  □ Usage analytics (what features are used, what's ignored)
  □ Churn interviews (when someone cancels, ask why)

Step E4: "Best of the best" quality checklist.
  □ DATA FRESHNESS: Updates within 24 hours of public record changes
  □ SPEED: Search < 1 second. Analysis < 5 seconds.
  □ ACCURACY TRANSPARENCY: Show confidence intervals, data sources.
    Let users override.
  □ MOBILE-READY: Every critical workflow works on a phone.
  □ OFFLINE CAPABILITY: Key data downloadable/cached.
  □ EXPORT: Every analysis exportable as professional PDF.
  □ MAPS: Every property view includes a map with comps, schools,
    transit, flood zones.
  □ PHOTOS: Display property photos prominently.
  □ CALCULATIONS SHOWN: Show formula, inputs, let users adjust.
  □ MULTI-SCENARIO: "What-if" scenarios for price, rent, expenses,
    vacancy, appreciation.

Step E5: What NOT to build.
  ✗ Social features (forums, messaging)
  ✗ News/blog/content
  ✗ Generic CRM
  ✗ Full accounting system
  ✗ Mortgage calculator
  ✗ "AI chatbot" for real estate questions
```

---

## Step 5: Failure Modes (`/fla`)

### FAILURE MODE 1: "Boiling the Ocean"
**Recognize**: 3+ months building, can't describe product in one sentence.
**Fix**: Stop. Go back to A6. One sentence. One killer feature.

### FAILURE MODE 2: "Data Quicksand"
**Recognize**: 60%+ time on data pipeline, no user-facing features.
**Fix**: Ship with manual data entry for 20 properties. Automate AFTER validation.

### FAILURE MODE 3: "Building for Yourself"
**Recognize**: Haven't talked to 10 target users, or interviews were friends.
**Fix**: Go back to A5. Interview strangers. Ask about their problems, not your solution.

### FAILURE MODE 4: "Tech Stack Paralysis"
**Recognize**: Changed frameworks twice without shipping.
**Fix**: Use the boring default (Rails/Django/Next.js + PostgreSQL + Mapbox). Ship today.

### FAILURE MODE 5: "Feature Creep Disguised as User Requests"
**Recognize**: Every interview adds a feature. Roadmap has 50 items.
**Fix**: Only build features 5+ of first 20 users independently request.

### FAILURE MODE 6: "Competing on Valuation Accuracy"
**Recognize**: Building an AVM and comparing to Zestimate.
**Fix**: Compete on niche accuracy, transparency, or user control instead.

### FAILURE MODE 7: "Ignoring Compliance"
**Recognize**: Filtering by demographics, displaying MLS data without IDX compliance.
**Fix**: Get a real estate attorney review ($2K-5K) before launch.

### FAILURE MODE 8: "Premature Geographic Expansion"
**Recognize**: 50 users in first metro, adding second city.
**Fix**: Get to 500 paying users in one metro first.

---

## Step 6: Validation (`/pv`)

All steps verified as executable by non-experts. All paths terminate at either Section E (completion) or a retry loop with clear exit conditions. No dead ends or infinite loops.

---

## COMMON MISTAKES

1. Building "Zillow but better" — Zillow has 10,000 employees. Find a niche.
2. Starting with MLS data — expensive, restricted, unnecessary for MVP.
3. Skipping validation — talk to users in week 1.
4. Multi-geography from day 1 — master one metro first.
5. Building mobile first — web is faster to iterate.
6. Underpricing — RE professionals make $50K-500K/year. Don't charge $5/month.
7. No distribution plan — "build it and they will come" doesn't work.
8. Over-engineering architecture — microservices for 0 users is procrastination.

---

## WHEN TO OVERRIDE

- Deep domain expertise + existing relationships suggest different approach
- Building for a regulated niche (1031 exchanges, opportunity zones)
- You have a proprietary data source nobody else has
- Adding RE features to an existing successful product
- Signed contract from a large client specifying requirements

---

## WORKED EXAMPLES

### Example 1: Solo developer, former landlord
- A1: Managing → A2: Individual investor → A3: Small MF → A4: Cleveland, OH
- A5: 7/10 landlords said maintenance tracking is biggest headache
- A6: "Reduce maintenance response time by 80% via tenant portal with photo submissions and auto-routing to vendors"
- Built Rails + PostgreSQL. Launched in 8 weeks. 15 paying users at $12/unit/month within 3 months.

### Example 2: Small team targeting wholesalers
- A1: Finding → A2: Wholesaler → A3: SFR → A4: Phoenix, AZ
- A5: 8/10 said finding motivated sellers before competitors is #1 challenge
- A6: "Surface pre-foreclosure and probate properties 48 hours before competitors via county recorder feeds + ML scoring"
- County data pipeline: 6 weeks. MVP at Day 45. 10 paying users ($99/month) at Day 80.

### Example 3: Funded startup, integration hub
- C2: Integration hub connecting MLS + CRM + analysis + PM
- Moat: Network effects from each integration
- Launched with 3 integrations. 200 users Year 1. Raised Series A.

---

**Validation status**: This procedure has not been validated by domain experts.
