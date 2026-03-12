---
name: "stcc - Short-Term Cluster Completion"
description: Identify partially-built clusters of work and determine what's needed to finish them. Prioritize by effort-to-complete.
output:
  format: "prose"
---

# Short-Term Cluster Completion

**Input**: $ARGUMENTS

---

## Step 1: Map Related Items

Identify clusters — groups of related work that belong together logically.

```
CLUSTER MAP:
1. [Cluster name]: [Brief description of what this group of work does together]
   - [Item A]: [exists / partial / missing]
   - [Item B]: [exists / partial / missing]
   - [Item C]: [exists / partial / missing]

2. [Cluster name]: [Brief description]
   - [Item A]: [exists / partial / missing]
   ...
```

Rules:
- A cluster is a set of things that only deliver full value when all are present
- Look for natural groupings: features, workflows, documentation sets, API surfaces
- Don't force unrelated items into clusters

---

## Step 2: Assess Completion Percentage

For each cluster, estimate how done it is.

```
COMPLETION ASSESSMENT:
1. [Cluster name]: [X]% complete
   - Done: [what's finished]
   - Partial: [what's started but incomplete]
   - Missing: [what hasn't been started]

2. [Cluster name]: [X]% complete
   ...
```

Rules:
- Be honest about percentages — 80% done often means 50% of the value is missing
- "Partial" means some work exists but it doesn't function independently
- A cluster at 95% is more valuable to finish than one at 30%

---

## Step 3: Identify Completion Requirements

For each cluster, specify exactly what's needed to reach 100%.

```
COMPLETION REQUIREMENTS:
1. [Cluster name]:
   - [ ] [Specific task 1] — effort: [hours/days]
   - [ ] [Specific task 2] — effort: [hours/days]
   - [ ] [Specific task 3] — effort: [hours/days]
   Total remaining effort: [estimate]

2. [Cluster name]:
   ...
```

Rules:
- Tasks must be specific and actionable, not vague
- "Polish the UI" is not a task; "Add error states to the login form" is
- Include only what's needed for completion, not enhancement

---

## Step 4: Prioritize by Effort-to-Complete

Rank clusters by the ratio of value delivered to effort remaining.

```
PRIORITY RANKING:
| Rank | Cluster | % Done | Effort Left | Value When Complete | Priority Score |
|------|---------|--------|-------------|---------------------|----------------|
| 1    | [name]  | [X]%   | [time]      | [HIGH/MED/LOW]      | [score]        |
| 2    | [name]  | [X]%   | [time]      | [HIGH/MED/LOW]      | [score]        |
...
```

Rules:
- Priority score = (completion % * value) / effort remaining
- High-completion + high-value + low-effort = finish first
- Low-completion + low-value + high-effort = finish last or abandon

---

## Step 5: Recommend Finishing Order

Produce a concrete plan.

```
RECOMMENDED ORDER:
1. FINISH NOW: [Cluster] — [why: nearly done, high value]
2. FINISH NEXT: [Cluster] — [why]
3. FINISH LATER: [Cluster] — [why]
4. CONSIDER ABANDONING: [Cluster] — [why: too much effort for too little value]
```

Rules:
- "Finish now" should be completable within days
- "Consider abandoning" is legitimate — sunk cost is not a reason to continue
- If two clusters share dependencies, note that and sequence accordingly

---

## Integration

Use with:
- `/immg` -> Fix urgent gaps before completing clusters
- `/de` -> Turn finishing plan into a structured delivery
- `/cba` -> If unsure whether to finish or abandon, do a cost-benefit analysis
- `/mtnw` -> After completing clusters, look for new domains to expand into
