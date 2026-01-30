---
name: ge
description: "Run systematic experiments to discover and validate growth levers using hypothesis-driven testing"
---

# Growth Experiments

## Overview
Run systematic experiments to discover and validate growth levers using hypothesis-driven testing

## Steps

### Step 1: Establish experimentation foundation
Set up the infrastructure and culture for experiments:

Define primary metrics (North Star):
- What is the one metric that matters most?
- How does it tie to business value?
- Can it be measured accurately?

Secondary metrics to monitor:
- Leading indicators of primary metric
- Guardrail metrics (things that shouldn't get worse)
- Segment-level metrics

Statistical requirements:
- Minimum sample size for validity
- Confidence level required (typically 95%)
- Minimum detectable effect (MDE)
- Test duration guidelines

Sample size calculation:
Needed sample = f(baseline conversion, MDE, confidence, power)
Tools: Evan Miller calculator, Optimizely calculator

Example: To detect 10% relative lift on 5% conversion
with 95% confidence and 80% power = ~31,000 per variant

Experimentation tools:
- A/B testing platforms (Optimizely, VWO, LaunchDarkly)
- Analytics integration (GA4, Amplitude, Mixpanel)
- Statistical analysis (Python/R or built-in tools)

Documentation setup:
- Experiment tracking template
- Results repository
- Learning database

### Step 2: Generate experiment hypotheses
Build a list of testable growth ideas:

Hypothesis sources:

Quantitative data:
- Funnel analysis: Where do users drop off?
- Cohort analysis: What do successful users do differently?
- Segment analysis: Which segments perform better?
- Feature usage: What correlates with retention?

Qualitative insights:
- User interviews: What do they struggle with?
- Support tickets: Common complaints/questions
- Session recordings: Where do users get confused?
- Sales conversations: What objections come up?

Competitive intelligence:
- What do competitors do differently?
- What worked for similar businesses?
- Industry best practices

Team ideas:
- Engineering insights on technical improvements
- Sales insights on objection handling
- Support insights on user struggles
- Leadership hypotheses

Hypothesis format:
"If we [change], then [metric] will improve by [amount]
because [rationale based on evidence]."

Strong hypothesis characteristics:
- Specific and measurable
- Based on data or insights (not just guessing)
- Explains the "why" not just the "what"
- Testable within reasonable timeframe
- Connected to primary metric

Generate 20-50 hypotheses before prioritizing.

### Step 3: Prioritize using ICE framework
Rank experiments by expected value:

ICE scoring:
- Impact (1-10): How big will the improvement be?
- Confidence (1-10): How sure are we it will work?
- Ease (1-10): How easy is it to implement?

ICE Score = Impact x Confidence x Ease

Scoring guidelines:

Impact scoring:
- 10: Transforms the metric (50%+ improvement)
- 7-9: Major improvement (20-50%)
- 4-6: Moderate improvement (10-20%)
- 1-3: Small improvement (<10%)

Consider: What % of users does this affect?
How much does it change their behavior?

Confidence scoring:
- 10: Proven to work (replicated result)
- 7-9: Strong evidence (similar tests, research)
- 4-6: Reasonable hypothesis (logic + some data)
- 1-3: Educated guess (intuition only)

Consider: What evidence supports this?
Has something similar worked before?

Ease scoring:
- 10: Trivial (copy change, hours of work)
- 7-9: Easy (days of work, no dependencies)
- 4-6: Moderate (weeks, some complexity)
- 1-3: Hard (months, cross-team, technical debt)

Consider: Engineering time, design needs,
cross-functional dependencies, reversibility

Alternative frameworks:
- RICE: Reach x Impact x Confidence / Effort
- PIE: Potential x Importance x Ease

Rank all hypotheses and select top experiments.
Balance quick wins with bigger bets.

### Step 4: Design experiments rigorously
Create detailed experiment specifications:

Experiment spec template:

1. Hypothesis
"If we [change], then [metric] will improve by [amount]
because [rationale]."

2. Test design
- Control: Current experience (describe)
- Variant(s): Changed experience (describe specifically)
- Target audience: Who is included/excluded
- Allocation: % traffic to each variant

3. Success criteria
- Primary metric: What defines success
- Expected lift: Minimum meaningful improvement
- Secondary metrics: What else to monitor
- Guardrail metrics: What shouldn't get worse

4. Sample size and duration
- Required sample per variant
- Expected duration based on traffic
- Any timing considerations (seasonality, etc.)

5. Implementation details
- Technical requirements
- Design assets needed
- QA checklist
- Launch steps

6. Risk assessment
- What could go wrong?
- Reversibility plan
- Escalation criteria

Experiment types:

A/B test: Control vs single variant
- Best for: Clear hypothesis, sufficient traffic
- Simpler to analyze

A/B/n test: Multiple variants
- Best for: Testing multiple approaches
- Requires more traffic

Multivariate test: Multiple changes combined
- Best for: Understanding interactions
- Requires much more traffic

Holdback test: New feature vs no feature
- Best for: Measuring feature impact
- Used post-launch to quantify value

### Step 5: Run experiments with discipline
Execute experiments following best practices:

Pre-launch checklist:
- Tracking verified (test events firing correctly)
- Variants displaying correctly (QA all paths)
- Success metrics baseline documented
- Team aligned on success criteria
- No conflicting experiments

During experiment:

Don'ts:
- Don't peek at results too early
- Don't make changes mid-experiment
- Don't expand scope while running
- Don't run conflicting experiments
- Don't stop early on positive trend

Do's:
- Monitor for technical issues daily
- Document any anomalies observed
- Check sample balance between variants
- Verify randomization is working
- Monitor guardrail metrics

When to stop early:
- Technical issues affecting user experience
- Clear negative impact on guardrail metrics
- External events invalidating the test
- Sample ratio mismatch indicating problems

Running multiple experiments:
- Use mutual exclusion groups for conflicting tests
- Document which experiments overlap
- Consider interaction effects
- Limit simultaneous tests to avoid confusion

Experiment velocity:
- Aim for 2-4 experiments per month (starting)
- Build toward 1-2 per week with maturity
- Speed of learning > individual experiment wins

### Step 6: Analyze results objectively
Evaluate experiment outcomes rigorously:

Statistical analysis:
- Calculate confidence interval for difference
- Determine if result is statistically significant
- Check for segment-level effects
- Analyze secondary and guardrail metrics

Result categories:

Winner:
- Variant beats control with statistical significance
- Secondary metrics neutral or positive
- Guardrails not violated
Action: Implement winner, document learnings

Loser:
- Control beats variant with statistical significance
- OR guardrails violated
Action: Don't implement, document why it failed

Inconclusive:
- No statistical significance reached
- Could be: need more traffic, effect smaller than MDE
Action: Decide to extend, iterate, or abandon

Learning:
- Result (win or lose) teaches something unexpected
- Segment effects reveal new opportunities
Action: Document insights for future experiments

Analysis best practices:
- Don't cherry-pick favorable segments
- Consider novelty effects (early enthusiasm fades)
- Check for Simpson's paradox (segment vs aggregate)
- Look at full distribution, not just averages
- Consider practical significance, not just statistical

Common analysis mistakes:
- Stopping early when trend looks good
- Running until you get significance (p-hacking)
- Ignoring secondary metrics that look bad
- Not checking for segment effects
- Attributing causation without controls

### Step 7: Extract and document learnings
Capture knowledge from every experiment:

Learning documentation template:

Experiment summary:
- Hypothesis tested
- Result (win/lose/inconclusive)
- Impact on primary metric
- Impact on secondary metrics

Key learnings:
- What did we learn about user behavior?
- What did we learn about our assumptions?
- What surprised us?
- What should we test next?

Implications:
- Should we implement the change?
- What follow-up experiments does this suggest?
- Does this change our strategy?
- Who else should know this?

Learning types:

Tactical learnings:
- "Headlines with numbers get 15% more clicks"
- "Red CTAs outperform green by 8%"

Strategic learnings:
- "Users value speed over features"
- "Price sensitivity varies dramatically by segment"

Process learnings:
- "We need 3 weeks minimum for this type of test"
- "Mobile and desktop show different results"

Build institutional knowledge:
- Maintain searchable experiment repository
- Regular experiment reviews with team
- Share learnings across departments
- Update playbooks with proven tactics

### Step 8: Build continuous learning loop
Create sustainable experimentation system:

Learning loop components:

1. Generate hypotheses (ongoing)
- Regular data review sessions
- User feedback integration
- Cross-functional idea sharing
- Competitive monitoring

2. Prioritize ruthlessly
- Weekly backlog grooming
- ICE score updates based on learnings
- Balance quick wins and big bets
- Deprioritize low-learning experiments

3. Run experiments (always have tests running)
- Pipeline of ready-to-run experiments
- Clear ownership and accountability
- Experiment velocity tracking

4. Analyze and learn
- Weekly results review
- Monthly learning synthesis
- Quarterly strategy impact assessment

5. Apply learnings
- Implement winners
- Update playbooks
- Generate new hypotheses
- Share across organization

Experimentation metrics:
- Experiment velocity (tests per month)
- Win rate (% of tests that win)
- Impact (cumulative metric improvement)
- Learning rate (insights generated)

Scaling experimentation:
- Train team members on methodology
- Create self-serve testing capabilities
- Build reusable testing infrastructure
- Celebrate learning, not just winning

Maturity levels:
1. Ad hoc: Occasional tests, no system
2. Developing: Regular tests, basic process
3. Defined: Consistent methodology, tracking
4. Optimized: Sophisticated testing, high velocity
5. Innovating: Experimentation culture embedded


## When to Use
- When you have sufficient traffic for statistically valid tests
- Looking to systematically improve conversion rates
- Want to validate growth ideas before full investment
- Building culture of data-driven decision making
- When intuition differs from data on what works
- Testing new features or changes before broad rollout
- Optimizing marketing channels and messaging

## Verification
- Hypotheses are specific, measurable, and evidence-based
- Experiments have sufficient sample size for validity
- Results are analyzed with proper statistical rigor
- Learnings are documented regardless of outcome
- Experiment velocity is tracked and improving
- Winners are implemented, not just declared

---

**Input**: $ARGUMENTS

Apply this procedure to the input provided.