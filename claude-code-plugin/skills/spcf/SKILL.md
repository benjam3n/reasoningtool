---
name: "spcf - Specific Analysis"
description: "Apply a principle, framework, or general insight to a specific case — translating abstract knowledge into concrete, actionable guidance tailored to the exact situation, constraints, and context at hand."
output:
  format: "prose"
---

# Specific Analysis

**Input**: $ARGUMENTS

---

## Core Principles

1. **General principles don't apply themselves.** "First-mover advantage matters" is a general insight. Whether it applies to YOUR product, in YOUR market, with YOUR resources, right now — that's the specific question. The gap between general knowledge and specific application is where most advice fails.

2. **Context is everything.** The same general principle produces opposite recommendations in different contexts. "Move fast" is right for a startup in an empty market and wrong for a medical device company. Specific analysis means taking context seriously — not as a footnote, but as the primary input.

3. **Specificity means naming names.** Not "consider your resources" but "you have $50K, two engineers, and 3 months." Not "assess the competition" but "your competitor shipped this feature last Tuesday." The more specific the inputs, the more actionable the output.

4. **The value of specific analysis is that it can be wrong.** General principles are safe because they're always somewhat true. Specific recommendations are valuable because they're precise enough to be precisely wrong — and therefore precisely right when they work. Aim for precision, not safety.

5. **Adaptation is not just application.** You can't just paste a general framework onto a specific case. The specific case has features the general principle doesn't account for — constraints, quirks, history, relationships. Adaptation means modifying the general approach to fit the terrain.

---

## Phase 1: Situation Specification

Get maximally specific about the actual situation.

```
[SP1] SITUATION: [what's happening, specifically]
[SP2] ACTORS: [who is involved — named, with roles and stakes]
[SP3] CONSTRAINTS: [specific limitations — time, money, people, permissions, dependencies]
[SP4] HISTORY: [what's already happened — what's been tried, what failed, what worked]
[SP5] CONTEXT: [the broader environment — market, organization, relationships, timing]
[SP6] GOAL: [what specific outcome is needed]
[SP7] SUCCESS_CRITERIA: [how you'll know it worked — specific, measurable]
```

### Specificity Test

For each field: could this description apply to a DIFFERENT situation? If yes, it's not specific enough. Push until the description uniquely identifies THIS case.

---

## Phase 2: Applicable Principles

Identify what general knowledge applies to this specific case.

```
[SP-N] PRINCIPLE: [general insight or framework]
     SOURCE: [where this comes from — experience, theory, analogy, skill]
     APPLIES_BECAUSE: [what features of this specific case match the principle's conditions]
     DOESN'T_FULLY_FIT_BECAUSE: [what features of this case the principle doesn't account for]
     ADAPTATION_NEEDED: [how to modify the principle for this context]
```

### Application Quality Check

| Check | Question |
|-------|---------|
| **Conditions met?** | Does this specific case actually meet the principle's boundary conditions? |
| **Scale match?** | Is the principle calibrated for this scale? (Startup advice for a startup, not for a government) |
| **Time match?** | Is the principle still relevant at this point in the situation? |
| **Resource match?** | Does the principle assume resources the specific case doesn't have? |
| **Culture match?** | Does the principle assume a context that doesn't apply here? |

---

## Phase 3: Concrete Recommendations

Translate principles into specific, actionable steps for THIS case.

```
[SP-N] RECOMMENDATION: [specific action to take]
     DERIVED_FROM: [which principle, adapted how]
     WHO: [specific person or role who does this]
     WHEN: [specific timing — not "soon" but "this week" or "before the meeting on Thursday"]
     HOW: [specific method — not "reach out" but "email Sarah with the Q3 numbers and ask for a 30-min meeting"]
     COST: [specific resources required]
     RISK: [what could go wrong with THIS specific action]
     EXPECTED_RESULT: [what should happen if this works]
     IF_IT_FAILS: [specific contingency for this action]
```

### Recommendation Quality Rules

- **Named actors**: Not "the team" but "Alice and Bob"
- **Specific timelines**: Not "soon" but "by Friday"
- **Concrete actions**: Not "improve communication" but "schedule a weekly 15-min standup at 9am"
- **Measurable results**: Not "better outcomes" but "reduce churn from 5% to 3%"
- **Realistic constraints**: Recommendations must be achievable with the stated resources

---

## Phase 4: Scenario Walkthrough

Walk through the specific scenario with the recommendations applied.

```
[SP-N] SCENARIO:
     STEP_1: [what happens first — specifically]
     LIKELY_RESPONSE: [how the situation and actors respond]
     STEP_2: [what happens next]
     LIKELY_RESPONSE: [response]
     ...
     EXPECTED_OUTCOME: [where this path leads]
     RISK_POINTS: [where things could go differently]
```

### If-Then Branches

```
[SP-N] IF [specific condition occurs]:
     THEN: [specific adjusted action]
     BECAUSE: [why this contingency]
```

---

## Phase 5: Output

```
SPECIFIC ANALYSIS
=================

SITUATION: [one-paragraph summary with all key specifics]
GOAL: [specific outcome]

RECOMMENDATIONS (in order):
  1. [WHO] does [WHAT] by [WHEN]
     EXPECTED RESULT: [specific outcome]
     IF IT FAILS: [contingency]

  2. [WHO] does [WHAT] by [WHEN]
     EXPECTED RESULT: [specific outcome]
     IF IT FAILS: [contingency]

  3. [WHO] does [WHAT] by [WHEN]
     EXPECTED RESULT: [specific outcome]
     IF IT FAILS: [contingency]

KEY RISKS:
  1. [risk] — PROBABILITY: [level] — MITIGATION: [specific action]

PRINCIPLES APPLIED:
  - [principle] → adapted as [specific application] because [context]

SUCCESS LOOKS LIKE: [specific, observable success state]
REVIEW IN: [specific time] — CHECK: [what to evaluate]

READY FOR:
- /genl — to extract general lessons from this specific case later
- /hrd — for maximum rigor on the highest-stakes recommendation
- /ar — to trace what follows from these recommendations
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Generic recommendations** | "Improve your process" without naming what, who, when | Every recommendation needs named actors, specific timelines, concrete actions |
| **Principle pasted, not adapted** | Applied a framework without modifying for context | Check each principle against the specificity test. Adapt for constraints and context |
| **Missing context** | Recommendations that ignore stated constraints | Re-read the constraints. If a recommendation violates a constraint, it's not viable |
| **Unrealistic** | Recommendations requiring resources the user doesn't have | Check each recommendation against stated resources |
| **No contingency** | "Do X" with no plan for when X fails | Every recommendation needs an if-it-fails branch |
| **Vague timeline** | "Soon" or "when ready" instead of specific dates | Pin every action to a specific time or trigger event |
| **Over-specified** | So many specific steps that the user is micromanaged | 3-5 high-level recommendations with specifics, not 20 micro-steps |

---

## Depth Scaling

| Depth | Recommendations | Scenario Walkthrough | Contingencies | Principles |
|-------|----------------|---------------------|--------------|-----------|
| 1x | 2-3 | No | One per recommendation | 1-2 applied |
| 2x | 3-5 | Key path | One per recommendation | 2-3 applied and adapted |
| 4x | 5-7 | Full with branches | Multiple per recommendation | Full principle audit |
| 8x | 7+ | Full + adversarial scenarios | Complete contingency tree | All applicable + cross-domain |

Default: 2x. These are floors.

---

## Pre-Completion Checklist

- [ ] Situation described with maximum specificity (passes uniqueness test)
- [ ] Constraints explicitly stated and respected
- [ ] Principles adapted for context (not just applied generically)
- [ ] Every recommendation has WHO, WHAT, WHEN, and IF-IT-FAILS
- [ ] Recommendations are achievable with stated resources
- [ ] Timelines are specific (not "soon")
- [ ] Expected results are measurable
- [ ] Key risks identified with mitigations

---

## Integration

- Use from: applying frameworks to real situations, making advice actionable, implementing strategies
- Routes to: `/genl` (extract lessons after execution), `/hrd` (maximum rigor on key actions)
- Complementary: `/genl` (genl extracts principles; spcf applies them — natural pair)
- Differs from `/genl`: genl goes specific→general; spcf goes general→specific
- Differs from `/ezy`: ezy simplifies the path; spcf specifies it for the exact context
- Differs from `/action`: action executes a task; spcf provides the specific analytical foundation for execution
