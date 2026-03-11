# /abts Design an A/B test: does showing users 12 tier-1 skills vs. 5 "start here" skills lead to more engagement?
**Date:** 2026-03-09
**Skill:** /abts (A/B Test Design)

---

## Step 1: State the Hypothesis

```
OBSERVATION: The index page currently displays all 48 skills across four tiers
(12 tier-1, 15 tier-2, 17 category, 4 experimental). New users face a wall of
options. The paradox of choice suggests this suppresses actual skill usage.

HYPOTHESIS: If we reduce the initial skill display from 12 tier-1 skills to
5 curated "start here" skills, then the percentage of visitors who invoke at
least one skill will increase by 15% (relative), because fewer options reduce
decision paralysis and create a clearer entry point.

NULL HYPOTHESIS: Changing the number of initially visible skills from 12 to 5
will have no measurable effect on the skill invocation rate.

FALSIFIABLE: Yes — we measure invocation rate in both groups and compare.

ONE-SIDED OR TWO-SIDED: Two-sided. It's possible that showing fewer skills
makes the product look too thin and *reduces* engagement. We need to detect
both directions.
```

---

## Step 2: Define Control and Treatment

```
CONTROL (A): Current index page showing all tiers:
  - 12 tier-1 skills (full grid)
  - 15 tier-2 skills
  - 17 category skills
  - 4 experimental skills
  All visible on page load with section headers.

TREATMENT (B): Curated "start here" page showing 5 skills initially:
  - /claim  — "Test a Claim"
  - /decide — "Make a Decision"
  - /how    — "Find the Method"
  - /want   — "Clarify a Goal"
  - /diagnose — "Find the Cause"
  These 5 are category skills (routers) chosen because they cover the most
  common entry intents. All other skills remain accessible via a
  "See all skills" expandable section below.

CHANGE ISOLATED: No — two things change simultaneously:
1. Number of initially visible skills (12 → 5) — the primary variable
2. Skill selection shifts from tier-1 (analytical primitives) to category
   skills (intent routers) — a secondary variable

Can it be isolated?
  Partially. We could add a Treatment C to disentangle:

ADDITIONAL VARIANTS:
- Treatment C: Show 5 tier-1 skills (se, aex, cmp, ht, dcp) — same count
  as B but analytical primitives instead of routers. This isolates the
  "fewer = better" effect from the "routers > primitives" effect.

Note: Adding Treatment C increases required sample size by ~50%.

TARGETING:
- Who is eligible: New visitors only (no prior skill invocation in analytics)
- Who is excluded: Return visitors with existing sessionStorage state
  (the site already persists filter/sort state via sessionStorage per
  commit 9c10739), direct deep-links to specific skill pages
- Randomization unit: User (via persistent cookie or localStorage ID),
  not session, so returning new users see a consistent experience
```

---

## Step 3: Calculate Required Sample Size

```
PARAMETERS:
- Baseline rate: ~8% estimated invocation rate (visitors who invoke at
  least one skill after landing on index — this is an estimate that should
  be validated with actual analytics before launch)
- Minimum detectable effect (MDE): 2 percentage points absolute
  (8% → 10%, a 25% relative lift)
- Significance level (alpha): 0.05
- Power (1 - beta): 0.80

REQUIRED SAMPLE SIZE:
  Using the formula for two-proportion z-test:
  n = (Z_α/2 + Z_β)² × [p1(1-p1) + p2(1-p2)] / (p2-p1)²
  n = (1.96 + 0.84)² × [0.08×0.92 + 0.10×0.90] / (0.02)²
  n = 7.84 × [0.0736 + 0.09] / 0.0004
  n = 7.84 × 0.1636 / 0.0004
  n ≈ 3,207 per variant

  For A/B (two variants): ~6,414 total visitors
  For A/B/C (three variants): ~9,621 total visitors

CURRENT DAILY TRAFFIC: Unknown — must instrument before test.
  Estimate needed: if 50 new visitors/day → ~128 days (too long for A/B)
  If 200 new visitors/day → ~32 days (borderline acceptable for A/B)
  If 500 new visitors/day → ~13 days (comfortable)

ESTIMATED RUNTIME: Depends entirely on traffic. See reality check.

REALITY CHECK:
- [ ] Runtime is reasonable (< 4 weeks for most tests)
      → UNKNOWN. Must measure baseline traffic first. If < 100 visitors/day,
        consider increasing MDE to 3pp (reduces n to ~1,500/variant) or
        running A/B only (drop Treatment C).
- [ ] MDE is small enough to be useful
      → 2pp absolute (25% relative) is meaningful — a smaller effect probably
        isn't worth the implementation cost anyway.
- [ ] Traffic is sufficient to reach significance
      → MUST VALIDATE. This is the biggest risk for a niche developer tool.
- [ ] If any fail: Fallback plan is to run A/B only (no Treatment C),
      increase MDE to 3pp, and accept a longer runtime with sequential
      testing (using a spending function to allow valid early stopping).
```

---

## Step 4: Choose the Success Metric

```
PRIMARY METRIC: Skill invocation rate
Definition: Percentage of eligible new visitors who invoke at least one
skill (any skill, via any method) within 24 hours of first index page visit.
Direction: Higher is better.

SECONDARY METRICS (monitor but don't decide on):
1. Skills invoked per engaged user — Why: Shows whether fewer initial
   options leads to deeper exploration once the barrier is crossed, or
   whether it just moves the "try one" needle.
2. Time to first invocation — Why: Shorter time suggests lower friction.
   If B has higher invocation rate but takes longer, the mechanism may
   differ from the "choice reduction" hypothesis.
3. "See all skills" expansion rate (Treatment B only) — Why: If most
   users immediately expand, the curated view isn't serving its purpose.
4. Return visit rate (7-day) — Why: First invocation means nothing if
   users don't come back.

GUARDRAIL METRICS (must not degrade):
1. Bounce rate — Threshold: Must not increase by more than 5pp. If showing
   fewer skills makes the page look empty/unimpressive, users may leave.
2. Page error rate — Threshold: 0% increase. The variant must not
   introduce technical issues.

METRIC SENSITIVITY CHECK:
- Can this metric move in the runtime? Yes — invocation is a per-visit
  event, not a slow-moving retention metric.
- Is it measured per-user or per-session? Per-user (first 24h window),
  matching the user-level randomization unit.
```

---

## Step 5: Set Runtime and Plan for Confounders

```
RUNTIME:
- Start date: TBD (after baseline traffic measurement and instrumentation)
- End date: Must complete full weeks to avoid day-of-week effects
- Minimum runtime: 14 days, even if significance is reached early
  (developer tool usage likely has strong weekday/weekend patterns)

CONFOUNDERS TO CONTROL:
| Confounder           | Risk                                        | Mitigation                                         |
|----------------------|---------------------------------------------|----------------------------------------------------|
| Seasonality          | Dev tool usage spikes around project starts  | Run full weeks; avoid major holidays or conferences |
| Novelty effect       | Users click more because layout is "new"     | 14-day minimum dampens this; compare week 1 vs 2   |
| Network effects      | Users share specific skill links with others | Exclude deep-link arrivals from the test population |
| Multiple testing     | 4 secondary metrics inflate false positives  | Pre-register primary metric; Bonferroni on secondary|
| Sample ratio mismatch| Unequal group sizes signal a bug             | Check 50/50 split ratio daily                      |
| Bot traffic          | Crawlers inflate visitor counts              | Filter by JS execution / interaction signals       |
| SessionStorage state | Returning users get misclassified as new     | Use dedicated A/B cookie, not sessionStorage        |
| Referral source mix  | Reddit post sends spike to one variant       | Stratify randomization by referral source           |

DO NOT:
- Peek at results and stop early when "significant"
- Change the 5 selected skills mid-flight
- Ramp traffic unevenly between variants
- Count the same user twice across devices (accept this limitation)
```

---

## Step 6: Define Decision Criteria Before Running

```
DECISION FRAMEWORK:

IF primary metric is statistically significant AND positive:
-> SHIP Treatment B (or C, whichever wins).
   Verify guardrail metrics are within thresholds before full rollout.
   If both B and C beat A, compare B vs C directly.

IF primary metric is statistically significant AND negative:
-> REVERT to control. Analyze why:
   - Did bounce rate increase? (Page looked too sparse)
   - Did users expand "See all" immediately? (Curation was wrong)
   - Did Treatment C (5 tier-1) also lose? (Problem is fewer, not which)
   Write up findings for future design decisions.

IF primary metric is NOT statistically significant:
-> The test is INCONCLUSIVE, not "no effect."
   Options:
   1. If trending positive (p < 0.15), extend runtime by 50%
   2. If flat (p > 0.30), accept that skill count is not the bottleneck
      and investigate other engagement barriers (copy, UX, onboarding flow)
   3. Redesign: try a more dramatic treatment (e.g., single-skill
      onboarding wizard instead of a grid)

IF guardrail metric (bounce rate) degrades significantly:
-> REVERT regardless of primary metric result. A page that drives away
   visitors is worse even if survivors engage more.

PRACTICAL SIGNIFICANCE:
- Even if statistically significant, is the effect large enough to matter?
- Minimum practical effect: 1.5pp absolute lift in invocation rate.
  Below this, the implementation/maintenance cost of maintaining the
  curated view is not justified.

SIGN-OFF REQUIRED FROM: Project owner (Ben)
RESULTS DOCUMENTATION: Write up in reasoningtoolpersonal/prompts/ with
  /abts tag, linking to the raw data export. Update website design
  decisions log regardless of outcome.
```

---

## Pre-Test Checklist

Before this test can run, the following must exist (none of which exist today):

1. **Analytics instrumentation** — Track: page views, skill invocations, visitor identity (anonymous persistent ID), referral source
2. **Baseline measurement** — Run analytics for 2+ weeks to establish: daily new visitor count, current invocation rate, day-of-week patterns
3. **A/B framework** — Client-side variant assignment with persistent cookie, not sessionStorage (which the site already uses for filter state)
4. **The Treatment B page** — Build the 5-skill "start here" view with "See all skills" expansion
5. **Event pipeline** — Ability to join page-view events with invocation events per anonymous user within a 24-hour window

**Estimated pre-test work: 1-2 weeks of instrumentation before the test can begin.**

---

## Integration

- `/mets` — Define the invocation rate metric precisely before building instrumentation
- `/dshb` — Build a live dashboard to monitor the running experiment without peeking at p-values
- `/ht` — The underlying hypothesis ("fewer options = more usage") was partially explored in prompt #35 (`35-ht-5-10-skills-hypothesis-2026-03-09.md`); this test operationalizes that hypothesis
