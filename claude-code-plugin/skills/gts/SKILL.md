---
name: gts
description: "The fundamental pattern for making cognitive tasks tractable: Generate possibilities, then Search using criteria."
---

# Generate-Then-Search Meta-Pattern

**Input**: $ARGUMENTS

---

## Overview

The fundamental pattern for making cognitive tasks tractable:
1. GENERATE a comprehensive space of possibilities
2. SEARCH within that space using well-defined criteria

Key insights:
- The intelligence is in the CRITERIA, not the search
- Generation can be constrained to exclude obviously bad options
- Comparison/selection is easier than generation from scratch
- Matching to criteria requires less intelligence than judgment

This pattern applies to: interpretation, prediction, communication, reasoning, creativity, understanding, and planning.

## Steps

### Step 1: Identify the Task
What cognitive task needs to be performed?

| Task Type | Generate | Search For |
|-----------|----------|-----------|
| Interpretation | Possible meanings | Most consistent with evidence |
| Prediction | Possible futures | Most likely given data |
| Communication | Possible expressions | Clearest for audience |
| Reasoning | Possible inferences | Logically valid ones |
| Creativity | Novel combinations | Valuable and feasible ones |
| Understanding | Possible models | Best fit to observations |
| Planning | Possible plans | Optimal given constraints |
| Decision | Possible options | Best according to criteria |
| Diagnosis | Possible causes | Most consistent with symptoms |
| Design | Possible solutions | Meeting requirements |

### Step 2: GENERATE — Create the Possibility Space
Rules for generation:

1. **Breadth first**: Generate MANY options before evaluating ANY
   - Premature evaluation kills the best options
   - Target: 2-3× more options than you think you need

2. **Constrained generation**: Pre-filter obviously impossible options
   - Physical impossibility → exclude
   - Violates hard constraints → exclude
   - Everything else → include, even if it seems unlikely

3. **Generation methods** (combine several):
   - Systematic enumeration (→ /se)
   - Morphological analysis (→ /ma)
   - Cross-domain analogy (→ /cda)
   - Inversion (→ /va, /im)
   - Random combination
   - Expert knowledge

4. **Quality check**: Is the space COMPREHENSIVE?
   - Have you included the obvious AND the non-obvious?
   - Have you included options from outside your domain?
   - Would someone from a different background add options you missed?

```
GENERATED SPACE:
Options: [N total]
Generation methods used: [which]
Constraint pre-filter: [what was excluded and why]
Completeness: [confident / gaps possible in: areas]
```

### Step 3: DEFINE CRITERIA — Set Search Parameters
Before searching, define what you're looking for:

1. **Must-have criteria** (non-negotiable):
   - [criterion] — how measured
   - [criterion] — how measured

2. **Ranked criteria** (in order of importance):
   - [criterion] — weight: [1-10]
   - [criterion] — weight: [1-10]

3. **Anti-criteria** (things to avoid):
   - [what to avoid] — why

**Criteria quality check:**
- Are criteria INDEPENDENT of each other? (Not measuring the same thing twice)
- Are criteria MEASURABLE? (Not "good" — specifically what makes it good)
- Are criteria RANKED? (You can't optimize everything equally)
- Do criteria reflect what you ACTUALLY want? (Not what sounds impressive)

### Step 4: SEARCH — Apply Criteria to Space
Apply criteria systematically:

**Round 1 — Must-have filter:**
Pass every option through must-have criteria. Eliminate failures.
Remaining: [N] of [N original]

**Round 2 — Ranked scoring:**
Score remaining options on ranked criteria:

| Option | Criterion 1 (wt: X) | Criterion 2 (wt: Y) | ... | Weighted Total |
|--------|---------------------|---------------------|-----|---------------|
| A | [score] | [score] | | [total] |
| B | [score] | [score] | | [total] |

**Round 3 — Top candidates:**
Take top 3-5 by weighted score for deeper evaluation.

### Step 5: EVALUATE — Deep-Dive Top Candidates
For each top candidate:
1. What are the risks specific to this option?
2. What assumptions does it depend on?
3. What would execution look like?
4. What would a critic say about this choice?

### Step 6: SELECT
Based on evaluation:
1. Which option has the best combination of score and low risk?
2. Is there a clear winner, or are top options very close?
3. If close: what tiebreaker criterion matters most?
4. → INVOKE: /sel (selection) or /dcp (decision procedure) for formal selection

### Step 7: Report
```
GENERATE-THEN-SEARCH:
Task: [what was being solved]

Generation:
- Options generated: [N]
- Methods: [which generation methods]
- Constraints: [what was pre-filtered]

Search criteria:
- Must-have: [list]
- Ranked: [top 3 criteria with weights]

Results:
- Passed must-have: [N] of [N]
- Top 3:
  1. [option] — score: [N] — key strength: [what]
  2. [option] — score: [N]
  3. [option] — score: [N]

Selected: [option]
Rationale: [why this one]
Key risk: [biggest concern with selected option]
```

## When to Use
- Any task where generating options and selecting among them is more tractable than directly constructing the answer
- When you're not sure where to start (generate broadly, then narrow)
- When quality of selection criteria matters more than quantity of options
- → INVOKE: /se (systematic enumeration) for generation
- → INVOKE: /gen (candidate generation) for diverse candidates
- → INVOKE: /sel (selection) for formal selection from candidates
- → INVOKE: /m (matching criteria) for defining search criteria

## Verification
- [ ] Generation phase completed BEFORE evaluation phase
- [ ] Multiple generation methods used
- [ ] Criteria defined BEFORE searching
- [ ] Criteria are independent, measurable, and ranked
- [ ] Must-have filter applied first, then ranked scoring
- [ ] Top candidates evaluated in depth (not just scored)
