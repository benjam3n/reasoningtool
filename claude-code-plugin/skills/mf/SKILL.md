---
name: mf
description: "Analyze and optimize the customer journey from awareness to revenue using the AARRR framework"
---

# Marketing Funnel Analysis

## Overview
Analyze and optimize the customer journey from awareness to revenue using the AARRR framework

## Steps

### Step 1: Map the customer journey
Define the stages of your specific funnel:

Standard AARRR stages with typical milestones:

ACQUISITION - How users find you:
- Website visit
- Landing page view
- Content consumption
- Ad click-through

ACTIVATION - First value experience:
- Account creation
- Onboarding completion
- First key action (varies by product)
- "Aha moment" reached

RETENTION - Users come back:
- Day 1 return
- Week 1 return
- Month 1 return
- Sustained usage pattern

REVENUE - Money exchange:
- Trial to paid conversion
- First purchase
- Subscription continuation
- Upsell/expansion

REFERRAL - Users bring others:
- Invite sent
- Referral completed
- Word of mouth (harder to track)
- Public advocacy (reviews, social)

Customize stages for your specific business:
- SaaS: Focus on trial-to-paid and monthly retention
- E-commerce: Focus on cart completion and repeat purchase
- Marketplace: Track both sides of the market
- Consumer app: Focus on daily/weekly active users

Document the specific actions that define each stage transition.

### Step 2: Establish baseline metrics
Collect current performance data for each stage:

For each funnel stage, measure:
- Volume: How many users reach this stage?
- Conversion: What % move to the next stage?
- Time: How long does the transition take?
- Cohort trends: Is it improving or declining?

Key ratios to calculate:
- Acquisition rate: Visitors / Impressions
- Activation rate: Activated users / Signups
- Day 1/7/30 retention: Users returning / Activated users
- Revenue rate: Paying users / Activated users
- Referral rate: Referrals made / Active users
- Viral coefficient: New users from referrals / Existing users

Segment by:
- Traffic source (organic, paid, referral, direct)
- User type (B2B vs B2C, enterprise vs SMB)
- Geography if relevant
- Time period (look for trends)

Set up tracking if not in place:
- Implement event tracking for key actions
- Create funnel reports in analytics tool
- Build cohort analysis capability
- Set up conversion tracking by source

### Step 3: Benchmark against standards
Compare your metrics to industry benchmarks:

Typical SaaS benchmarks:
- Website visitor to signup: 2-5%
- Signup to activation: 20-40%
- Activation to paid: 2-5% (freemium), 15-25% (free trial)
- Monthly retention: 95%+ (enterprise), 90%+ (SMB)
- Annual churn: <5% (enterprise), <15% (SMB)
- Referral rate: 2-5% of users refer

E-commerce benchmarks:
- Add to cart rate: 8-15%
- Cart completion rate: 50-70%
- Repeat purchase rate: 20-40%
- Email capture rate: 1-5%

Consumer app benchmarks:
- Day 1 retention: 25-40%
- Day 7 retention: 10-20%
- Day 30 retention: 5-10%
- Viral coefficient: 0.15-0.25 (good), 0.5+ (viral)

Note: Benchmarks vary significantly by:
- Industry and product type
- Price point and sales cycle
- Target market
- Business model

Use benchmarks as directional guidance, not absolute targets.
Your best benchmark is your own historical performance.

### Step 4: Identify the leaky bucket
Find where users drop off most:

Calculate absolute drop-off at each stage:
- Stage N visitors - Stage N+1 visitors = Drop-off
- Rank stages by drop-off volume

Calculate relative drop-off:
- (Expected conversion - Actual conversion) x Volume
- This shows opportunity size, not just drop-off

Root cause analysis for biggest leaks:

Acquisition leaks:
- Wrong audience targeting
- Weak value proposition
- Poor landing page messaging
- High bounce rate signals

Activation leaks:
- Complicated signup process
- Confusing onboarding
- Time to value too long
- Users don't reach "aha moment"

Retention leaks:
- Product doesn't deliver on promise
- No habit formation
- No re-engagement triggers
- Better alternatives found

Revenue leaks:
- Price-value mismatch
- Friction in purchase process
- Free version too generous
- Wrong timing for upgrade ask

Referral leaks:
- No referral mechanism
- No incentive to share
- Product not shareable
- Customers not delighted enough

Prioritize fixing the leak with highest volume x conversion gap.

### Step 5: Diagnose specific conversion problems
Deep dive into the biggest leak:

Quantitative analysis:
- Segment drop-off by user characteristics
- Compare successful vs unsuccessful users
- Identify correlation patterns
- Analyze timing and sequence

Qualitative analysis:
- Session recordings of users who drop off
- User interviews with churned users
- Support ticket analysis for friction points
- Survey users who didn't convert

Common conversion killers by stage:

Acquisition problems:
- Targeting: Wrong people seeing your ads/content
- Messaging: Value proposition unclear or weak
- Channel: Wrong channels for your audience
- Competition: Others capturing the demand

Activation problems:
- Friction: Too many steps to get started
- Clarity: Users don't know what to do next
- Value delay: Too long before first value
- Technical: Bugs, performance, compatibility

Retention problems:
- Engagement: Users forget about you
- Value: Core promise not fulfilled
- Habits: No trigger for return visits
- Competition: Better alternatives found

Revenue problems:
- Timing: Asking too early or too late
- Pricing: Too high or value unclear
- Process: Purchase flow has friction
- Trust: Concerns about commitment

Document specific hypotheses to test.

### Step 6: Design optimization experiments
Create experiments to address identified problems:

For each hypothesis, design an experiment:
- Hypothesis: "If we [change], then [metric] will improve by [amount]"
- Control: Current experience
- Variant: Changed experience
- Sample size: Users needed for significance
- Duration: How long to run
- Success criteria: What constitutes a win

Experiment types by stage:

Acquisition experiments:
- A/B test landing page headlines
- Test different value propositions
- Try new acquisition channels
- Optimize ad creative and targeting

Activation experiments:
- Simplify signup flow
- Improve onboarding sequence
- Reduce time to first value
- Add progress indicators

Retention experiments:
- Trigger-based email sequences
- Push notification timing
- Feature discovery prompts
- Habit-forming product changes

Revenue experiments:
- Pricing page optimization
- Trial length variations
- Upgrade prompt timing
- Payment method options

Referral experiments:
- Referral incentive types
- Sharing mechanism placement
- Referral message optimization
- Viral loop integration

Prioritize using ICE framework:
- Impact: How big will the improvement be?
- Confidence: How sure are we it will work?
- Ease: How easy is it to implement?

### Step 7: Run and measure experiments
Execute experiments systematically:

Before launch:
- Verify tracking is in place
- Document starting metrics
- Set up test and control groups
- Communicate to relevant teams

During experiment:
- Monitor for technical issues
- Don't peek at results too early (p-hacking)
- Document anything unusual
- Maintain test integrity

After experiment:
- Calculate statistical significance
- Measure primary and secondary metrics
- Look for unexpected effects
- Document learnings

Interpreting results:
- Win: Variant better with statistical significance
- Loss: Control better with statistical significance
- Inconclusive: Not enough signal, need more data
- Learning: Even losses teach something

Common mistakes to avoid:
- Stopping too early when you see a positive trend
- Running too many variants (dilutes sample)
- Changing experiments mid-flight
- Not accounting for novelty effects
- Ignoring secondary metrics that show harm

### Step 8: Iterate and compound gains
Build on learnings to accelerate improvement:

After each experiment cycle:
- Update baseline metrics
- Recalculate opportunity sizes
- Reprioritize experiment backlog
- Apply learnings to new hypotheses

Compounding improvement:
- Small gains multiply across funnel
- 10% improvement at 5 stages = 61% overall improvement
- Focus on sustainable gains, not one-time bumps

Build optimization into culture:
- Regular experiment review meetings
- Shared learnings documentation
- Celebrate learnings, not just wins
- Track experiment velocity

Set up continuous monitoring:
- Alert when metrics drop
- Weekly funnel review
- Monthly deep dive
- Quarterly strategy review

Document institutional knowledge:
- What works in your context
- What doesn't work (avoid repeating)
- Benchmark improvements over time


## When to Use
- When you need to understand why growth is stalling
- Before investing heavily in acquisition channels
- When conversion rates seem low but you don't know where
- Starting to scale after achieving product-market fit
- When CAC (Customer Acquisition Cost) is too high
- Diagnosing why users sign up but don't convert to paying
- Setting up growth metrics and dashboards
- Prioritizing growth experiments

## Verification
- Every funnel stage has measurable conversion metrics
- Leaks are prioritized by actual opportunity size, not assumptions
- Experiments have clear hypotheses and success criteria
- Results are statistically significant before action
- Learnings are documented and applied to future experiments
- Metrics show improvement trend over time

---

**Input**: $ARGUMENTS

Apply this procedure to the input provided.