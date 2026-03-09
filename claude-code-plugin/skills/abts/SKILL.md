---
name: "abts - A/B Test Design"
description: Design a valid experiment with a clear hypothesis, proper controls, sufficient sample size, and pre-defined decision criteria.
---

# A/B Test Design

**Input**: $ARGUMENTS

---

## Step 1: State the Hypothesis

A good experiment starts with a falsifiable prediction.

```
OBSERVATION: [what you've noticed that prompted this test]
HYPOTHESIS: If we [change X], then [metric Y] will [increase/decrease] by [amount/percentage], because [mechanism].

NULL HYPOTHESIS: [change X] will have no measurable effect on [metric Y].

FALSIFIABLE: [yes/no — if no, rewrite until it is]
ONE-SIDED OR TWO-SIDED: [are you testing "better" or "different"?]
```

---

## Step 2: Define Control and Treatment

Specify exactly what differs between the two groups.

```
CONTROL (A): [exact description of the current experience]
TREATMENT (B): [exact description of the changed experience]

CHANGE ISOLATED: [yes/no — is there exactly ONE difference between A and B?]
If no, list all differences:
1. [difference] — Can it be isolated? [yes/no]

ADDITIONAL VARIANTS (if testing more than two):
- Treatment C: [description]
- Treatment D: [description]
Note: Each additional variant increases required sample size.

TARGETING:
- Who is eligible: [all users / segment / new users only / etc.]
- Who is excluded: [any exclusions and why]
- Randomization unit: [user / session / device / other]
```

---

## Step 3: Calculate Required Sample Size

Running a test too short or too small produces noise, not signal.

```
PARAMETERS:
- Baseline rate: [current value of the metric — e.g., 3.2% conversion]
- Minimum detectable effect (MDE): [smallest change worth detecting — e.g., 0.5% absolute]
- Significance level (alpha): [typically 0.05]
- Power (1 - beta): [typically 0.80, use 0.90 for high-stakes tests]

REQUIRED SAMPLE SIZE: [per variant]
CURRENT DAILY TRAFFIC: [eligible units per day]
ESTIMATED RUNTIME: [days needed = sample size / daily traffic]

REALITY CHECK:
- [ ] Runtime is reasonable (< 4 weeks for most tests)
- [ ] MDE is small enough to be useful
- [ ] Traffic is sufficient to reach significance
- [ ] If any fail, adjust MDE or consider alternative methods
```

---

## Step 4: Choose the Success Metric

One primary metric. Others are secondary.

```
PRIMARY METRIC: [the one metric that determines success or failure]
Definition: [exactly how it's calculated]
Direction: [higher is better / lower is better]

SECONDARY METRICS (monitor but don't decide on):
1. [metric] — Why: [what it tells you beyond the primary]
2. [metric] — Why: [what it tells you beyond the primary]

GUARDRAIL METRICS (must not degrade):
1. [metric] — Threshold: [maximum acceptable degradation]
2. [metric] — Threshold: [maximum acceptable degradation]

METRIC SENSITIVITY CHECK:
- Can this metric move in the runtime? [yes/no]
- Is it measured per-user or per-session? [match to randomization unit]
```

---

## Step 5: Set Runtime and Plan for Confounders

Protect the experiment from things that could invalidate it.

```
RUNTIME:
- Start date: [date]
- End date: [date — must complete full weeks to avoid day-of-week effects]
- Minimum runtime: [even if significance is reached early, run at least X days]

CONFOUNDERS TO CONTROL:
| Confounder | Risk | Mitigation |
|-----------|------|------------|
| Seasonality | [e.g., holiday traffic differs] | [run full weeks, avoid holidays] |
| Novelty effect | [users react to change, not improvement] | [run long enough for novelty to fade] |
| Network effects | [users influence each other] | [cluster randomization if needed] |
| Multiple testing | [checking multiple metrics inflates false positives] | [pre-register primary metric, apply corrections] |
| Sample ratio mismatch | [unequal group sizes signal a bug] | [check split ratio daily] |

DO NOT:
- Peek at results and stop early when "significant"
- Change the test mid-flight
- Ramp traffic unevenly
```

---

## Step 6: Define Decision Criteria Before Running

Decide how you'll decide before you see the data.

```
DECISION FRAMEWORK:

IF primary metric is statistically significant AND positive:
-> SHIP the treatment [with/without guardrail check]

IF primary metric is statistically significant AND negative:
-> REVERT to control. Analyze why the hypothesis was wrong.

IF primary metric is NOT statistically significant:
-> The test is INCONCLUSIVE, not "no effect."
   Options: [extend runtime / increase MDE / redesign treatment / accept uncertainty]

IF guardrail metric degrades significantly:
-> REVERT regardless of primary metric result.

PRACTICAL SIGNIFICANCE:
- Even if statistically significant, is the effect large enough to matter?
- Minimum practical effect: [the smallest effect worth shipping for]

SIGN-OFF REQUIRED FROM: [who must approve the decision]
RESULTS DOCUMENTATION: [where results will be recorded for institutional memory]
```

---

## Integration

Use with:
- `/mets` -> Select the right metrics before designing the test
- `/dshb` -> Build a monitoring dashboard for the running experiment
- `/ht` -> Test the underlying hypothesis before committing to an experiment
