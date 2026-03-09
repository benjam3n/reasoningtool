---
name: "orec - Recommendation Generation"
description: Generates actionable recommendations derived from findings. Takes a situation, analyzes it, and produces prioritized recommendations with implementation details and success metrics.
---

# Recommendation Generation

**Input**: $ARGUMENTS

---

## Step 1: State the Situation

Establish the context that the recommendations will address.

```
SITUATION: [what is happening / what prompted this]
STAKEHOLDERS: [who is affected / who will act on these recommendations]
CONSTRAINTS: [budget, time, authority, technical limits]
GOAL: [what success looks like if recommendations are followed]
```

---

## Step 2: Present Findings

Summarize the evidence base that recommendations will be derived from. Recommendations without findings are opinions.

```
FINDINGS:
1. [finding 1] — [source or evidence]
2. [finding 2] — [source or evidence]
3. [finding 3] — [source or evidence]
...
```

Rules:
- Each finding should be a factual statement, not an interpretation
- Cite the basis: data, observation, analysis, expert input, or user research
- Separate what is known from what is inferred
- Flag any findings with weak evidence

```
EVIDENCE QUALITY:
- STRONG: [findings with solid evidence]
- MODERATE: [findings with partial evidence]
- WEAK: [findings based on inference or limited data]
```

---

## Step 3: Derive Recommendations

Generate recommendations directly from the findings. Each recommendation should trace back to one or more findings.

```
RECOMMENDATIONS:
1. [recommendation 1]
   BASED ON: Finding [N], Finding [M]
   TYPE: [quick win / strategic / foundational / experimental]

2. [recommendation 2]
   BASED ON: Finding [N]
   TYPE: [quick win / strategic / foundational / experimental]

...
```

Rules:
- Every recommendation must link to at least one finding
- If a recommendation has no supporting finding, it is an opinion — flag it or remove it
- Recommendations should be specific enough to act on
- Use action verbs: "Implement X", "Reduce Y", "Migrate from A to B"

---

## Step 4: Prioritize

Rank recommendations by impact and feasibility.

| Recommendation | Impact | Effort | Priority |
|----------------|--------|--------|----------|
| [rec 1] | [H/M/L] | [H/M/L] | [rank] |
| [rec 2] | [H/M/L] | [H/M/L] | [rank] |

```
DO FIRST: [high impact, low effort — quick wins]
DO NEXT: [high impact, high effort — strategic investments]
DO LATER: [low impact, low effort — nice to have]
RECONSIDER: [low impact, high effort — may not be worth it]
```

---

## Step 5: Specify Implementation

For each top-priority recommendation, provide enough detail to act.

```
RECOMMENDATION [N]: [name]
  OWNER: [who is responsible]
  TIMELINE: [when to start, when to finish]
  DEPENDENCIES: [what must happen first]
  RESOURCES: [what is needed — people, budget, tools]
  FIRST STEP: [the concrete next action to begin]
```

---

## Step 6: State Expected Outcomes

Describe what changes if the recommendations are followed.

```
EXPECTED OUTCOMES:
- If Rec 1 is implemented: [expected result and timeframe]
- If Rec 2 is implemented: [expected result and timeframe]
- Combined effect: [what the full set of recommendations achieves together]
```

---

## Step 7: Define Success Metrics

Make it possible to measure whether the recommendations worked.

```
SUCCESS METRICS:
1. [metric 1] — current: [baseline], target: [goal], measured by: [how]
2. [metric 2] — current: [baseline], target: [goal], measured by: [how]
...

REVIEW CADENCE: [when to check progress — weekly, monthly, quarterly]
```

---

## Integration

Use with:
- `/rca` -> Perform root cause analysis before generating recommendations
- `/olst` -> Generate a comprehensive list of possible recommendations
- `/omtx` -> Compare recommendations in a matrix
- `/oprc` -> Turn a recommendation into a detailed procedure
- `/odec` -> Frame a recommendation as a formal decision
