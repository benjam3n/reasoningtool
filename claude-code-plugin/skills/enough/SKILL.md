---
name: "enough - Sufficiency Check"
description: "Determine whether something has been examined, built, planned, or analyzed enough — or whether more work is needed, and specifically what's missing."
output:
  format: "prose"
---

# Sufficiency Check

**Input**: $ARGUMENTS

---

## Interpretations

Before executing, identify which interpretation matches the user's input:

**Interpretation 1 — Analysis sufficiency**: The user has analyzed something and wants to know if the analysis is thorough enough — or if there are gaps, blind spots, or unexamined dimensions.
**Interpretation 2 — Build sufficiency**: The user has built something (skill, product, feature) and wants to know if it's complete enough to ship — or if critical pieces are missing.
**Interpretation 3 — Planning sufficiency**: The user has a plan and wants to know if they've planned enough — or if they're over-planning and should just start.
**Interpretation 4 — Decision sufficiency**: The user is trying to decide something and wants to know if they have enough information — or if they're either overthinking or underthinking it.

If ambiguous, ask: "Are you checking whether your analysis is deep enough, your build is complete enough, your plan is thorough enough, or your decision is informed enough?"
If clear from context, proceed with the matching interpretation.

---

## Core Principles

1. **"Enough" is relative to PURPOSE.** Nothing is enough in the abstract. A summary is enough when it serves the person who reads it. An analysis is enough when it supports the decision it feeds. Always ask: enough FOR WHAT?

2. **Both under and over are failures.** Not enough = gaps that cause problems downstream. Too much = wasted effort, analysis paralysis, gold-plating, or avoiding action by hiding in process. The skill must detect both directions.

3. **Sufficiency has dimensions.** Something can be deep enough but not broad enough. Complete enough in content but not in quality. Thorough enough in analysis but missing validation. Check multiple dimensions, not just "is it done?"

4. **The cost of more must be weighed against the cost of gaps.** An extra hour of analysis is worth it if the gap would cause a week of rework. It's not worth it if the gap is cosmetic. Cost-of-gap drives the answer.

---

## Phase 1: Define the Standard

What is this thing supposed to achieve? Without a standard, "enough" is meaningless.

```
SUBJECT: [what are we checking the sufficiency of?]
PURPOSE: [what is this supposed to accomplish?]
AUDIENCE: [who consumes this? what do they need from it?]
STAKES: [what happens if it's not enough? what's the cost of gaps?]
STAKES OF OVERDOING: [what happens if we do too much? what's the cost of excess?]
```

---

## Phase 2: Dimensional Sufficiency Check

Check sufficiency along each relevant dimension:

### Breadth — Does it cover enough ground?

```
BREADTH CHECK:
  What territory SHOULD this cover? [list the expected scope]
  What territory DOES it cover? [list what's actually addressed]
  GAPS: [what's in the "should" list but not the "does" list]
  VERDICT: [sufficient / gaps exist — list them]
```

### Depth — Does it go deep enough where it matters?

```
DEPTH CHECK:
  Which parts are MOST CRITICAL to the purpose? [list]
  For each critical part:
    [part] — Current depth: [surface / moderate / thorough / exhaustive]
             Required depth: [surface / moderate / thorough / exhaustive]
             VERDICT: [sufficient / needs more depth]

  Which parts are LEAST CRITICAL? [list]
  Are any of these over-developed? [if yes, flag as over-investment]
```

### Quality — Is the work good enough?

```
QUALITY CHECK:
  Is each element internally consistent? [YES/NO — flag issues]
  Is each element accurate/correct? [YES/NO — flag issues]
  Would the audience find this clear and usable? [YES/NO — flag issues]
  Are there elements that seem done but are actually vague or hand-wavy? [list]
  VERDICT: [sufficient / quality issues exist — list them]
```

### Validation — Has it been tested or checked?

```
VALIDATION CHECK:
  Has this been tested against real cases? [YES/NO]
  Has this been reviewed by someone other than the creator? [YES/NO]
  Has anyone tried to break it or find its limits? [YES/NO]
  What would you need to see to be CONFIDENT this works? [describe]
  VERDICT: [validated / unvalidated / partially validated]
```

### Robustness — Does it handle edge cases?

```
ROBUSTNESS CHECK:
  What are the common cases? [handled? YES/NO]
  What are the edge cases? [handled? YES/NO — list unhandled]
  What would make this fail? [list scenarios]
  Which failure scenarios are acceptable? [list]
  Which are unacceptable? [list — these MUST be handled]
  VERDICT: [robust enough / fragile in these ways]
```

---

## Phase 3: The "More Work" Cost-Benefit

For each gap found, assess whether filling it is worth it:

```
GAP ASSESSMENT:
  [gap 1]:
    Cost of the gap: [what goes wrong if this stays unfilled]
    Cost to fill: [time/effort to address it]
    VERDICT: [must fix / should fix / can skip]

  [gap 2]:
    Cost of the gap: [what goes wrong]
    Cost to fill: [time/effort]
    VERDICT: [must fix / should fix / can skip]
  ...
```

---

## Phase 4: Over-Sufficiency Check

Is there evidence of OVERDOING?

```
OVER-SUFFICIENCY CHECK:
  Are there parts that go deeper than the purpose requires? [list]
  Are there parts that cover territory outside the scope? [list]
  Is the total volume disproportionate to the stakes? [YES/NO]
  Has more time been spent on this than the decision/output warrants? [YES/NO]
  Is continued work a form of AVOIDANCE (perfecting instead of shipping)? [YES/NO]

  Signs of overdoing:
  - [ ] Diminishing returns: each hour of work produces less improvement
  - [ ] Scope creep: the thing now covers more than originally intended
  - [ ] Perfectionism: holding to a standard higher than the purpose requires
  - [ ] Avoidance: continuing to analyze/plan because acting feels risky
  - [ ] Gold-plating: polishing parts that no one will notice or benefit from
```

---

## Phase 5: Verdict

```
SUFFICIENCY VERDICT
===================

SUBJECT: [what was checked]
PURPOSE: [what it's for]

DIMENSIONAL RESULTS:
  Breadth:    [sufficient / gaps] — [details if gaps]
  Depth:      [sufficient / needs more in X] — [details]
  Quality:    [sufficient / issues in X] — [details]
  Validation: [validated / unvalidated / partial]
  Robustness: [sufficient / fragile in X] — [details]

OVERALL: [ENOUGH / NOT ENOUGH / TOO MUCH / MIXED]

IF NOT ENOUGH:
  Must fix (blocks the purpose):
  1. [gap] — [what to do about it]
  2. ...

  Should fix (improves quality meaningfully):
  1. [gap] — [what to do about it]
  2. ...

  Can skip (nice but not load-bearing):
  1. [gap]
  2. ...

IF TOO MUCH:
  Cut or simplify:
  1. [over-developed element] — [why it's excessive]
  2. ...

IF ENOUGH:
  Ship it. Stop analyzing. The cost of further work exceeds the cost of remaining gaps.
  What you're risking by shipping: [honest assessment]
  Why that risk is acceptable: [reason]

NEXT:
  [specific action — either "fix X then ship" or "ship now" or "investigate X before deciding"]
```

---

## Depth Scaling

| Depth | Dimensions Checked | Gap Assessment | Over-Sufficiency Check |
|---|---|---|---|
| 1x | Breadth + depth only | List gaps, no cost-benefit | Skip |
| 2x | All 5 dimensions | Cost-benefit on "must fix" gaps | Basic check |
| 4x | All 5 + custom dimensions | Full cost-benefit on all gaps | Full check with avoidance detection |
| 8x | All + compare to external standards | Full + priority ordering | Full + evidence-based assessment |

Default: 2x.

---

## Failure Modes

| Failure | Signal | Fix |
|---|---|---|
| **No standard defined** | Checking "enough" without stating what it's for | Phase 1 is mandatory — "enough for WHAT?" |
| **Only checking for gaps** | Never considered whether it's overdone | Phase 4 exists for a reason — check both directions |
| **Perfectionism disguised as rigor** | Every gap is labeled "must fix" | Apply cost-benefit honestly. Most gaps are "can skip." |
| **Action avoidance** | Running /enough repeatedly instead of shipping | If you're checking sufficiency for the third time, the answer is "enough — ship it." |
| **Shallow quality check** | "Looks good" without testing | Validation dimension requires actual testing or honest admission that testing hasn't happened |
| **Binary thinking** | "It's either done or not" | Sufficiency has dimensions — something can be broad enough but not deep enough |

---

## Integration

Use with:
- `/phil` → Derive requirements FIRST, then check sufficiency against those requirements
- `/pri` → When multiple gaps exist and you need to prioritize which to fix
- `/dwt` → When you're unsure whether deeper analysis is warranted at all
- `/val` → When the sufficiency check reveals validation gaps
- `/pv` → To validate specific elements flagged as questionable
- `/ar` or `/aw` → To stress-test whether a "sufficient" verdict is actually right
