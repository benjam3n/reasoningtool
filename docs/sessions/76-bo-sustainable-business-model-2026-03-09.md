# /bo What does a sustainable business look like around a thinking toolkit?
**Date:** 2026-03-09
**Skill:** /bo (Business Operations)

---

## Interpretation

**Interpretation 2 — Business idea to evaluate.** The user has an existing product (592 thinking skills, open-source, Claude Code plugin) and needs to assess how to build a sustainable business around it. This is a viability + growth + pricing + financial question rolled into one.

## Step 1: Classification

This spans multiple types:

| Type | Applies? | Key Question |
|------|----------|-------------|
| Starting a business | **Yes** | Is this viable as a revenue generator? |
| Revenue/sales | **Yes** | Who pays and for what? |
| Pricing | **Yes** | What to charge for a thinking toolkit? |
| Growth | **Yes** | How to scale from 0 to sustainable? |
| Financial | **Yes** | What does "sustainable" actually require? |

Primary route: **Step 2a (Viability)** with support from 2b, 2c, 2e, 2g.

---

## Step 2a: Viability Assessment

### 1. Problem: What specific problem does this solve? For whom?

**Problem:** People make bad decisions, get stuck in loops, miss angles, and produce shallow analysis — not because they're unintelligent, but because they lack structured thinking procedures. AI amplifies this: it's fluent but not rigorous unless directed.

**For whom (candidate segments):**

| Segment | Problem Intensity | Willingness to Pay |
|---------|------------------|-------------------|
| Solo knowledge workers (consultants, analysts, strategists) | High — thinking IS their product | High — tools = revenue |
| AI power users (Claude Code users, prompt engineers) | Medium-High — already investing in AI tooling | Medium — used to free/open-source |
| Founders/indie hackers | High — decisions are existential | Medium — cash-constrained |
| Students/learners | Medium — want to think better | Low — price-sensitive |
| Teams/orgs wanting decision rigor | High — bad decisions are expensive | High — budget exists |

**Sharpest problem-market fit:** Solo knowledge workers and consultants whose output quality IS their income. A thinking toolkit directly improves their deliverables.

### 2. Evidence: How do you KNOW this is a real problem?

**What exists:**
- You built 592 skills because YOU needed them — classic "scratch your own itch"
- Thinking frameworks sell: mental models books, decision journals, Second Brain, etc. are proven markets
- AI prompt engineering is a growing market — this is structured prompt engineering for thinking

**What's missing:**
- No user data yet (downloads, usage, retention)
- No validation that others find the specific skill format useful
- No evidence that people will pay vs. just use free alternatives

**Honest assessment:** The problem is real and validated by adjacent markets. The specific solution (592 markdown skills as a Claude Code plugin) is unvalidated with external users.

### 3. Solution: Why is YOUR solution better than alternatives?

**Alternatives:**
| Alternative | Weakness your toolkit addresses |
|------------|-------------------------------|
| Generic AI prompting | No structure, no procedure, inconsistent depth |
| Mental models books (Farnam Street, etc.) | Static, not applied, no AI integration |
| Consulting frameworks (McKinsey, etc.) | Expensive, not accessible, not personalized |
| Custom GPTs / prompt libraries | One-shot, not chainable, not systematic |
| Thinking courses (Coursera, etc.) | Time-intensive, theory-heavy, not applied in-workflow |

**Your differentiation:**
- **Procedural, not conceptual** — skills are step-by-step, not "here's a concept, figure it out"
- **AI-native** — designed to be executed by an LLM, not read by a human
- **Composable** — skills chain into each other (INVOKE system)
- **Comprehensive** — 592 skills covering decision-making, analysis, writing, debugging, etc.
- **In-workflow** — runs inside Claude Code where people already work

**Moat question (Step 2a.6):**
- **Weak moat:** Markdown files can be copied. Open-source means anyone can fork.
- **Potential moats:** (a) Curation quality and completeness — 592 skills is a LOT of work to replicate well. (b) Community and iteration — if you build feedback loops, the skills get better faster than a copycat. (c) Brand/trust — "the" thinking toolkit. (d) Skill interconnections — the routing and chaining system is the real IP, not individual skills.

### 4. Market: How many people have this problem and would pay?

- Claude Code users: Tens of thousands and growing rapidly
- AI power users broadly: Millions
- Knowledge workers who'd pay for thinking tools: Large but diffuse market
- **Realistic addressable market (Year 1):** 1,000-10,000 Claude Code users who care about structured thinking

### 5. Economics: Can you deliver the solution profitably?

**Cost structure (solo dev):**
- Your time (primary cost)
- Hosting/distribution: Near-zero (GitHub, static site)
- No COGS per customer for the core product (markdown files)
- Marginal cost of one more user: ~$0

This is an excellent cost structure. Once built, it costs nothing to distribute.

### 6. What prevents a competitor from copying you?

See moat discussion above. The honest answer: **not much, initially.** The defensibility grows with (a) completeness, (b) quality iteration, (c) community, and (d) brand.

---

## Step 2c: Pricing — What to Charge?

### The Core Tension

Open-source creates adoption but not revenue. You need a model that preserves the open-source benefits (trust, distribution, community) while creating a revenue layer.

### Pricing Models Evaluated

| Model | How it works | Revenue potential | Risk |
|-------|-------------|-------------------|------|
| **1. Open core** | Free base skills, paid advanced/premium skills | Medium | Which skills are "premium" without feeling extractive? |
| **2. Freemium SaaS** | Free skills, paid web app with analytics/history/recommendations | High | Requires building and maintaining a SaaS product |
| **3. Paid tiers** | Free (50 skills), Pro (all 592), Team (multi-seat + custom) | Medium-High | Free tier must be genuinely useful or adoption dies |
| **4. Consulting/services** | Toolkit is free, sell custom skill development and consulting | Medium | Doesn't scale, trades time for money |
| **5. Sponsorship/patronage** | Free for all, Patreon/GitHub Sponsors for supporters | Low | Very few open-source projects sustain a person this way |
| **6. Course/education** | Free toolkit, paid "learn to think better" course using the toolkit | Medium-High | Different business (education), proven model though |
| **7. Enterprise/team licensing** | Free for individuals, paid for org-wide deployment + support | High | Requires enterprise sales capability |
| **8. Marketplace** | Platform where others contribute/sell skills | High (long-term) | Requires critical mass, complex to build |

### Recommended Pricing Architecture

**Layered approach (not either/or):**

**Layer 1 — Free & Open Source (distribution engine)**
- All 592 skills remain free and open-source
- This is your marketing, your trust-builder, your adoption mechanism
- Never gate the core value

**Layer 2 — Pro Individual ($15-25/month or $150-200/year)**
- Skill recommendation engine (which skill for this problem?)
- Usage history and personal analytics (which skills help you most?)
- Custom skill builder (create your own procedures)
- Priority skill updates and new skill early access
- Web dashboard for non-CLI users

**Layer 3 — Team/Org ($50-100/seat/month)**
- Shared skill libraries within org
- Decision audit trails
- Custom skill development for org-specific workflows
- Admin/reporting dashboard
- Onboarding and support

**Layer 4 — Services (hourly/project)**
- Custom skill development for specific domains
- Consulting on thinking processes for teams
- Workshop facilitation using the toolkit

### Price Justification (Value-Based)

A consultant billing $150/hour who makes even 10% better decisions from structured thinking gains $15/hour, or ~$2,400/month. A $25/month tool is a 96:1 ROI. This is an easy sell IF the value is demonstrated.

---

## Step 2b: Revenue — Customer Acquisition

### Who is the ideal first customer?

**Specific:** A solo consultant or freelance strategist who already uses Claude Code, charges $100+/hour, and has felt frustrated by shallow AI outputs. They would immediately see the value of structured thinking procedures because their income depends on thinking quality.

### Where are they?

1. **Claude Code community** — Discord, forums, GitHub
2. **AI/LLM Twitter/X** — power user discussions
3. **Indie hacker communities** — Indie Hackers, HN, relevant subreddits
4. **Consulting communities** — niche subreddits, Slack groups, LinkedIn

### Growth Strategy (Step 2e)

**Phase 1: Organic/Product-Led (Months 1-6)**
- Open-source distribution builds awareness at zero cost
- Content marketing: "How I make better decisions with AI" blog posts
- Community engagement in Claude Code / AI spaces
- Reddit posts demonstrating specific skills on real problems
- Goal: 500-1,000 active free users

**Phase 2: Content + Community (Months 6-12)**
- Build a small community (Discord) around structured thinking
- Regular content showing skills applied to real problems
- Guest appearances on AI/productivity podcasts
- Goal: 2,000-5,000 free users, launch Pro tier

**Phase 3: Paid Conversion (Months 9-18)**
- Launch Pro tier when you have enough free users to convert
- Target 3-5% free-to-paid conversion
- Begin exploring Team tier with early design partners
- Goal: 100-250 paying users at $20/month = $2,000-5,000/month

---

## Step 2g: Financial Reality Check

### What does "sustainable" mean for you?

| Level | Monthly Revenue | What It Requires |
|-------|----------------|-----------------|
| Survival | $3,000-4,000 | Covers basic living expenses |
| Comfortable | $6,000-8,000 | Living expenses + savings + reinvestment |
| Thriving | $15,000+ | Hire help, invest in growth, build runway |

### Path to Survival ($3,000/month)

**Scenario A: Pro subscriptions only**
- At $20/month: need 150 paying users
- At 4% conversion: need 3,750 free active users
- Timeline: 9-15 months of consistent effort

**Scenario B: Pro + consulting**
- 50 Pro users ($1,000/month) + 10 hours consulting at $200/hour ($2,000/month)
- More achievable in months 6-9
- Consulting validates what companies will pay for

**Scenario C: Course launch**
- A "Structured Thinking with AI" course at $200
- Need 15 sales/month = $3,000
- Could launch in months 3-6 with the toolkit as the platform

### Runway Calculation

- Current runway: $0 income, unknown savings (critical to know)
- If 12 months of savings: comfortable timeline for Phase 1-2
- If 3-6 months: need to pursue Scenario B (consulting supplement) immediately
- If < 3 months: this needs to be a side project while employed

### Unit Economics Target

- CAC (Customer Acquisition Cost): $0-5 (organic-first strategy)
- LTV (Lifetime Value) at $20/month, 12-month average retention: $240
- LTV:CAC ratio: 48:1 (excellent, if organic acquisition works)
- Gross margin: ~95% (near-zero marginal cost)

---

## BUSINESS ANALYSIS

**Question type:** Business viability + model design for a thinking toolkit product

**Key challenge:** Converting a comprehensive open-source thinking toolkit into sustainable income for a solo developer, starting from zero users and zero revenue.

### Analysis

The fundamentals are strong: near-zero marginal costs, a real problem (poor thinking), a differentiated solution (procedural AI-native skills), and a large adjacent market. The primary risks are distribution (getting noticed) and conversion (getting people to pay when the core is free).

**The sustainable business looks like this:**

1. **Free open-source core** (all skills) for distribution and trust
2. **Pro tier** ($15-25/month) for power features — recommendation, history, custom skills, web UI
3. **Consulting/services** as a revenue bridge while Pro scales
4. **Team/enterprise tier** ($50-100/seat) once product-market fit is proven with individuals
5. **Community** as a growth flywheel and retention mechanism

**The most likely failure mode** is not the business model — it's never reaching enough users because you're building in isolation. The single most important thing to do right now is get 100 people using the free toolkit and learning what they actually value.

### Key Metrics to Track

1. **Free users (weekly active)** — current: 0 — target: 500 by Month 6
2. **Retention (% using after 30 days)** — current: unknown — target: 30%+
3. **NPS / would-recommend score** — current: unknown — target: 40+
4. **Paid conversion rate** — current: N/A — target: 3-5%
5. **Monthly recurring revenue** — current: $0 — target: $3,000 by Month 12
6. **Runway (months of cash remaining)** — current: unknown — target: always > 6 months

### Next Actions

1. **Define your runway honestly.** How many months can you sustain $0 income? This determines your strategy's aggressiveness.
2. **Get the toolkit into 20 people's hands this week.** Post in Claude Code communities, AI Twitter, relevant subreddits. Measure who sticks.
3. **Build a feedback mechanism.** Even a simple "was this skill useful? Y/N" at the end of skill output. You need signal.
4. **Identify 3-5 skills that demo best.** Not all 592 — find the ones that make people say "whoa" in under 2 minutes.
5. **Start a lightweight email list or Discord.** You need a way to reach people who've shown interest.
6. **Pursue 2-3 consulting conversations.** Reach out to consultancies or teams that might pay for custom thinking procedures. This validates willingness to pay and generates bridge revenue.
7. **Sketch the Pro tier feature set.** What would make YOU pay $20/month on top of the free skills? Build that.

### Risks

1. **No users adopt** — mitigation: focus on distribution BEFORE features; lower friction (web UI, not just CLI)
2. **Users adopt but won't pay** — mitigation: validate willingness to pay early (consulting, pre-sales); ensure Pro tier is genuinely valuable, not artificially gated
3. **Someone forks and competes** — mitigation: move fast on community and brand; quality iteration is hard to replicate
4. **Solo dev burnout** — mitigation: set a clear "minimum viable effort" weekly; consulting income reduces financial pressure
5. **Market too niche** — mitigation: start niche (Claude Code power users), expand outward (any AI user, any knowledge worker)
6. **Runway runs out before revenue** — mitigation: know your number, have a "get a job" trigger point, consulting bridges the gap

### Related Procedures

- `/cd` — Customer development to validate who actually wants this
- `/pos` — Positioning the toolkit in the market
- `/fm` — Financial modeling for revenue projections
- `/prm` — Pre-mortem on business failure modes
- `/br` — Backward reasoning from revenue target to required actions
- `/to` — Task ordering for the next 90 days of execution
