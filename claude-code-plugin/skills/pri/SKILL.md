---
name: "pri - Prioritization"
description: Systematically prioritizes a list of anything using weighted criteria and appropriate frameworks (Eisenhower, MoSCoW, impact-effort).
output:
  format: "prose"
---

# Prioritization

**Input**: $ARGUMENTS

---

## Step 1: List the Items

Extract everything that needs prioritizing.

```
ITEMS TO PRIORITIZE:
1. [item]
2. [item]
3. [item]
...

CONTEXT: [what are these items? tasks, features, goals, problems, etc.]
```

---

## Step 2: Define Criteria

What matters for this decision? Choose 3-5 criteria relevant to the context.

Common criteria by type:
- **Tasks**: impact, effort, urgency, dependencies
- **Features**: user value, revenue impact, build cost, strategic fit
- **Goals**: achievability, importance, time-sensitivity, resource cost
- **Problems**: severity, frequency, solvability, blast radius

```
CRITERIA:
1. [criterion] — weight: [1-3, where 3 = most important]
2. [criterion] — weight: [1-3]
3. [criterion] — weight: [1-3]
...
```

---

## Step 3: Score Each Item

Rate each item against each criterion (1-5 scale).

| Item | [Criterion 1] (w:[weight]) | [Criterion 2] (w:[weight]) | ... | Weighted Total |
|------|---------------------------|---------------------------|-----|----------------|
| [item] | [score] | [score] | ... | [calculated] |
| ... | ... | ... | ... | ... |

Weighted total = sum of (score x weight) for each criterion.

---

## Step 4: Select Framework

Choose the framework that best fits the situation:

| Situation | Framework |
|-----------|-----------|
| Tasks with deadlines | **Eisenhower** (urgent/important matrix) |
| Product features | **MoSCoW** (must/should/could/won't) |
| Resource-constrained list | **Impact-Effort** (2x2 matrix) |
| Already scored above | **Straight rank** (use weighted totals) |

Apply the chosen framework:

```
FRAMEWORK: [name]

[Framework-specific output — matrix, categories, or ranked list]
```

---

## Step 5: Ranked Output

Combine the scoring and framework into a single prioritized list.

```
PRIORITY RANKING:
1. [item] — Score: [N] — [one-line rationale]
2. [item] — Score: [N] — [one-line rationale]
3. [item] — Score: [N] — [one-line rationale]
...

RECOMMENDED CUTOFF: Do items 1-[N]. Defer or drop the rest.
RATIONALE: [Why this cutoff — resource constraint, diminishing returns, etc.]
```

---

## Step 6: Edge Cases

Check for problems in the ranking:

```
DEPENDENCY CHECK: Does any lower item need to happen before a higher one? [adjust if yes]
QUICK WINS: Any low-ranked item that takes <1 hour and unblocks others? [promote if yes]
HIDDEN COSTS: Any top item that has unstated prerequisites? [note them]
```

Adjust final ranking if needed.

---

## Integration

Use with:
- `/tri` -> When you need rapid urgency-based sorting rather than weighted analysis
- `/cba` -> When the top items need formal cost-benefit analysis
- `/dcp` -> When the #1 priority requires a decision before starting
- `/to` -> When the prioritized list needs to become an execution plan
- `/cmp` -> When two items are too close to rank and need head-to-head comparison
