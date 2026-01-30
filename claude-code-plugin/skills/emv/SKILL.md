---
name: emv
description: Empirical validation step for GOSM plans - adds external reality testing beyond coherence checks
---

# Empirical Validation

**Input**: $ARGUMENTS (a plan, strategy, or set of claims to validate)

---

## Overview

**Problem**: Story coherence is necessary but insufficient for plan quality. Coherent narratives can mask poor plans (the "Hollywood problem" - heist movies have perfect coherence but real heists fail).

**Solution**: Add empirical validation step that tests plans against external reality where possible.

---

## Step 1: Identify Testable Predictions

For the plan/claims, extract testable predictions:

```
TESTABLE PREDICTIONS
====================
Plan/Claim: [the plan or claim being validated]

Predictions if this plan is CORRECT:
1. [Observable outcome 1] within [timeframe]
2. [Observable outcome 2] within [timeframe]
3. [Observable outcome 3] within [timeframe]

Predictions if this plan is WRONG:
1. [Observable failure 1] would indicate [what's wrong]
2. [Observable failure 2] would indicate [what's wrong]
3. [Observable failure 3] would indicate [what's wrong]

CRUX PREDICTIONS (would change the plan if different):
1. [Most important prediction to test]
2. [Second most important]
```

---

## Step 2: Design Minimum Viable Test

Find the smallest test that would validate or invalidate key assumptions:

```
MINIMUM VIABLE TEST
===================
Key assumption to test: [the most important uncertain element]

Test design:
- What to do: [specific action]
- Resources needed: [minimal resources]
- Time required: [estimate]
- Success indicator: [what shows assumption is correct]
- Failure indicator: [what shows assumption is wrong]
- Confidence level: [what % confidence does this test provide]

Can this test be run BEFORE full commitment? [Y/N]
If NO, why not: [reason]
Alternative smaller test: [if applicable]
```

---

## Step 3: Pre-Test vs Post-Hoc Decision

| Situation | Recommendation |
|-----------|----------------|
| Test is cheap, can run before commitment | RUN TEST FIRST |
| Test is expensive but commitment is more expensive | Consider test anyway |
| Cannot test until after commitment | Design post-commitment checkpoints |
| Plan is reversible | Act, then test via results |
| Plan is irreversible | Maximum pre-testing warranted |

```
PRE/POST DECISION
=================
Action reversibility: [REVERSIBLE / PARTIALLY / IRREVERSIBLE]
Test cost vs action cost: [TEST CHEAPER / SIMILAR / ACTION CHEAPER]
Information available pre-action: [HIGH / MEDIUM / LOW]

Recommendation: [TEST FIRST / ACT THEN TEST / SET CHECKPOINTS]
```

---

## Step 4: Run Test or Design Checkpoints

### If Testing First

```
TEST EXECUTION PLAN
===================
1. [Specific step 1]
2. [Specific step 2]
3. [Measure result]
4. [Compare to prediction]

If prediction confirmed: Proceed with plan
If prediction disconfirmed: [Revise plan OR abandon OR gather more info]
```

### If Acting Then Testing

```
CHECKPOINT DESIGN
=================
Checkpoint 1: [After what milestone?]
- What to measure: [observable]
- Expected if on track: [prediction]
- Expected if off track: [warning sign]
- Decision rule: [continue / pivot / stop]

Checkpoint 2: [After what milestone?]
- [same format]

Checkpoint 3: [After what milestone?]
- [same format]
```

---

## Step 5: Log Predictions for Tracking

For calibration over time, log predictions and outcomes:

```
PREDICTION LOG ENTRY
====================
Date: [today]
Plan/Claim: [summary]
Prediction: [specific, measurable prediction]
Confidence: [0-100%]
Timeframe: [when we'll know]
Test method: [how we'll verify]
Status: [PENDING / CONFIRMED / DISCONFIRMED / MODIFIED]
Outcome: [to be filled when known]
Lessons: [to be filled when known]
```

Save prediction logs to: `library/predictions/[date]_[topic-slug].md`

---

## Step 6: Update Plan Based on Results

After test or checkpoint:

```
POST-VALIDATION UPDATE
======================
Original plan: [summary]
Test/Checkpoint: [what was done]
Result: [what happened]

Prediction vs Reality:
| Prediction | Reality | Match? |
|------------|---------|--------|
| [pred 1] | [actual] | [Y/N] |
| [pred 2] | [actual] | [Y/N] |

If predictions matched: [Proceed with higher confidence]
If predictions didn't match:
- What this reveals: [learning]
- Plan revision needed: [changes]
- New uncertainty: [what we still don't know]
- Next test: [if applicable]
```

---

## Common Patterns

### Pattern 1: Market Test
**For**: Business plans, product ideas
**Test**: Small-scale trial, landing page, survey
**Measure**: Conversion, interest, feedback

### Pattern 2: Prototype Test
**For**: Technical plans, designs
**Test**: Build smallest working version
**Measure**: Does it function as expected?

### Pattern 3: Expert Review
**For**: Plans in specialized domains
**Test**: Get domain expert opinion
**Measure**: What objections/blindspots do they see?

### Pattern 4: Historical Analog
**For**: Situations with precedent
**Test**: Research similar past situations
**Measure**: What happened? Why?

### Pattern 5: Stress Test
**For**: Plans with assumptions about conditions
**Test**: What happens if [key assumption] is wrong?
**Measure**: Does plan still work?

---

## Integration with GOSM

This step should come AFTER:
- ARAW search (have explored the space)
- Coherence check (plan hangs together internally)
- Dual analysis (have contrarian perspective)

And BEFORE:
- Final commitment
- Resource allocation
- Step execution

```
GOSM Integration Point:
... → /vbo → /emv → Commit
```

---

## When to Skip Empirical Validation

1. **Action is trivially reversible** - Just do it and learn
2. **Time pressure is extreme** - GOSM-Lite conditions
3. **No test is possible** - Must commit without testing
4. **Cost of test exceeds cost of action** - Just act

Even when skipping, LOG the prediction for future calibration.

---

## Calibration Review (Periodic)

Review prediction logs periodically:

```
CALIBRATION REVIEW
==================
Period: [date range]
Predictions made: [count]
Predictions resolved: [count]

Accuracy by confidence level:
| Confidence | Made | Correct | Accuracy |
|------------|------|---------|----------|
| 90-100% | | | % |
| 70-89% | | | % |
| 50-69% | | | % |
| <50% | | | % |

Calibration assessment:
[ ] Well-calibrated (accuracy matches confidence)
[ ] Overconfident (accuracy < confidence)
[ ] Underconfident (accuracy > confidence)

Adjustment: [what to change in future predictions]
```

---

**Execute now**: Apply to input.
