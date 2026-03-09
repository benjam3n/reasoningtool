---
name: "prvn - Proven-Need Validation"
description: "Validate that a need is real before investing by finding behavioral evidence, quantifying demand, checking existing solutions, and assessing trajectory."
---

# PRVN - Proven-Need Validation

**Input**: $ARGUMENTS

---

## Step 1: State the Claimed Need

```
CLAIMED NEED: [what someone says is needed]
CLAIMANT: [who is claiming this need exists]
BENEFICIARY: [who would benefit if the need were met]
INVESTMENT REQUIRED: [what it would cost to address this need]
```

Separate the need from the proposed solution. "We need a new CRM" is a solution. "We need to track customer interactions across channels" is a need. Validate the need, not the solution.

---

## Step 2: Find Behavioral Evidence

```
BEHAVIORAL EVIDENCE (people actually doing workarounds):
  1. [workaround observed]
     WHO: [who is doing this]
     FREQUENCY: [how often]
     PAIN: [how much effort or frustration the workaround costs]
  2. [workaround observed]
     WHO: [who]
     FREQUENCY: [how often]
     PAIN: [effort level]
  3. [workaround observed]
     WHO: [who]
     FREQUENCY: [how often]
     PAIN: [effort level]

NO WORKAROUNDS FOUND: [if nobody is working around the problem, the need may not be real]
```

Workarounds are the strongest signal of a real need. If people are building spreadsheets, using duct-tape solutions, or manually doing what software should do — the need is real. If nobody is doing workarounds, ask why not.

---

## Step 3: Quantify the Need

```
QUANTIFICATION:
  HOW MANY PEOPLE: [number affected]
  HOW OFTEN: [frequency of the need arising]
  HOW PAINFUL: [severity per occurrence — low | medium | high | critical]
  TOTAL IMPACT: [people x frequency x pain = rough magnitude]

COMPARISON:
  INVESTMENT TO ADDRESS: [cost in time, money, effort]
  VALUE IF ADDRESSED: [what's gained]
  RATIO: [is the investment justified by the value?]
```

Vague needs stay vague forever. Put numbers on it, even rough ones. "A lot of people need this" is not quantification. "About 200 users hit this 3 times per week and spend 15 minutes each time working around it" is quantification.

---

## Step 4: Check If Solutions Already Exist

```
EXISTING SOLUTIONS:
  1. [solution] — COVERAGE: [what portion of the need it addresses]
     WHY NOT SUFFICIENT: [what gap remains]
     ADOPTION: [how many people use it]
  2. [solution] — COVERAGE: [portion]
     WHY NOT SUFFICIENT: [gap]
     ADOPTION: [usage level]

IF SOLUTIONS EXIST AND ARE UNUSED:
  WHY UNUSED: [awareness | access | usability | trust | cost]
  IMPLICATION: [the problem might be adoption, not a missing solution]
```

If good solutions exist and nobody uses them, the real problem is not the missing solution — it's something else (awareness, friction, trust). Building another solution won't help.

---

## Step 5: Assess Whether the Need Is Growing or Shrinking

```
TRAJECTORY:
  DIRECTION: [growing | stable | shrinking]
  EVIDENCE: [what signals indicate the trajectory]
  DRIVERS: [what forces are pushing the need in this direction]
  TIMELINE: [how fast is the need changing]

IF GROWING:
  PROJECTED IMPACT: [what happens if unaddressed for 6/12/24 months]

IF SHRINKING:
  RISK OF INVESTMENT: [will the need disappear before the investment pays off?]

IF STABLE:
  URGENCY: [is there a timing advantage to acting now vs later?]
```

---

## Output Summary

```
NEED VALIDATION
===============
CLAIMED NEED: [restate]
VERDICT: [proven | likely real | uncertain | likely false | disproven]

EVIDENCE:
  WORKAROUNDS: [count found, strongest example]
  QUANTIFICATION: [people x frequency x pain]
  EXISTING SOLUTIONS: [what exists and why it's insufficient]
  TRAJECTORY: [growing | stable | shrinking]

RECOMMENDATION:
  [invest | investigate further | don't invest | solve differently]
  REASONING: [one-sentence justification]

IF INVESTING:
  ADDRESS: [the validated need, not the proposed solution]
  PRIORITY: [based on trajectory and magnitude]

IF NOT INVESTING:
  WHY NOT: [specific evidence against the need]
  INSTEAD: [what to do with the resources]
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Validating the solution, not the need** | Assessing whether a specific product is good | Step back — is the underlying need real? |
| **Accepting claims without evidence** | "Everyone needs this" without workarounds or data | No workarounds = no proven need |
| **Ignoring existing solutions** | Building something that already exists | Always check Step 4 before recommending investment |
| **Static assessment** | Validating need without checking trajectory | A real need that's shrinking may not justify investment |
| **Conflating desire with need** | "People want this" treated as "people need this" | Needs have workarounds and pain. Wants don't |

---

## Integration

- Use with: `/dtsk` to gather data that quantifies the need
- Use with: `/smpl` for quick validation of obviously real or false needs
- Use with: `/agsk` to analyze the argument for the need's existence
- Use from: `/viability` when testing whether an idea addresses a real need
- Differs from `/agsk`: prvn validates needs empirically; agsk analyzes argument logic
