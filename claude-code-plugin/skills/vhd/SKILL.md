---
name: vhd
description: "Framework for deciding when to improve existing procedures (vertical) versus add new ones (horizontal)."
---

# Vertical vs Horizontal Integration Decision

**Input**: $ARGUMENTS

---

## Overview

Framework for deciding when to improve existing procedures/categories (vertical) versus when to add new procedures/categories (horizontal) in GOSM.

This applies to any system where you must choose between depth and breadth: codebases, product features, skill development, organizational capabilities.

## Steps

### Step 1: Assess Current State

**Vertical health (depth/quality of existing):**

| Factor | Score (1-5) | Evidence |
|--------|------------|---------|
| Procedure quality: Are existing procedures well-developed? | | |
| Coverage within categories: Do procedures handle their intended cases? | | |
| Integration: Do procedures work well together? | | |
| Validation: Have procedures been tested and refined? | | |
| User satisfaction: Do users find existing procedures helpful? | | |

**Horizontal health (breadth/coverage):**

| Factor | Score (1-5) | Evidence |
|--------|------------|---------|
| Domain coverage: Are all important domains represented? | | |
| Gap frequency: How often do users need something that doesn't exist? | | |
| Request patterns: What do users ask for that we can't provide? | | |
| Competitive coverage: What do alternatives offer that we don't? | | |
| Structural completeness: Is the taxonomy well-covered? | | |

### Step 2: Calculate Direction Score

**Vertical signal strength** (reasons to go deep):
- Existing procedures are frequently used but produce mediocre results → +3
- Users report confusion or errors with current procedures → +3
- Quality issues are causing trust problems → +3
- Integration between procedures is poor → +2
- Procedures have known gaps within their scope → +2

**Horizontal signal strength** (reasons to go wide):
- Users frequently need capabilities that don't exist → +3
- Entire domains are unrepresented → +3
- Low-hanging fruit: easy new procedures would add high value → +2
- Structural gaps create routing problems → +2
- New domains have emerged since last expansion → +2

### Step 3: Consider Portfolio Balance

Map current state on the depth-breadth matrix:

```
          HIGH QUALITY
              |
  "Polished    |    "Complete
   but narrow" |     system"
              |
LOW BREADTH ---+--- HIGH BREADTH
              |
  "Bare        |    "Wide but
   minimum"    |     shallow"
              |
          LOW QUALITY
```

- If "bare minimum": go horizontal (you need basics before depth)
- If "polished but narrow": go horizontal (diminishing returns on depth)
- If "wide but shallow": go vertical (breadth without depth is fragile)
- If "complete system": go vertical on weak spots or maintain

### Step 4: Apply Decision Rules

| Condition | Decision | Reasoning |
|-----------|----------|-----------|
| Vertical score > Horizontal score + 5 | Go vertical | Strong depth signal |
| Horizontal score > Vertical score + 5 | Go horizontal | Strong breadth signal |
| Scores within 5 | Check portfolio position | Tiebreaker from Step 3 |
| Both scores low | Neither — something else is wrong | Investigate root cause |
| Both scores high | Do both — but separate tracks | Parallel investment |

### Step 5: Plan the Work

**If going vertical:**
1. Rank existing procedures by: usage × quality_gap
2. Start with highest-impact improvements
3. Define "done" for each improvement (not "make it better" — specific criteria)
4. Set a stopping criterion (switch to horizontal when quality reaches threshold)

**If going horizontal:**
1. Rank gaps by: frequency_of_need × difficulty_to_create
2. Start with highest-value, lowest-effort additions
3. Define minimum viable quality for new additions (avoid creating more stubs)
4. Set a stopping criterion (switch to vertical when coverage reaches threshold)

### Step 6: Report
```
VERTICAL vs HORIZONTAL DECISION:
System: [what system is being developed]

Assessment:
- Vertical score: [N] — key signals: [top factors]
- Horizontal score: [N] — key signals: [top factors]
- Portfolio position: [which quadrant]

Decision: [VERTICAL / HORIZONTAL / BOTH]
Rationale: [why]

Work plan:
1. [specific item to improve/add]
2. [specific item]
3. [specific item]

Stopping criterion: Switch to [other direction] when [condition]
```

## When to Use
- Deciding what to work on next in library/system development
- Planning a development sprint
- Evaluating whether to improve existing or add new
- At portfolio review points to assess balance
- → INVOKE: /iterate for executing the chosen direction

## Verification
- [ ] Both vertical and horizontal health assessed with evidence
- [ ] Signal strengths scored independently
- [ ] Portfolio balance considered
- [ ] Decision follows from assessment (not predetermined)
- [ ] Work plan has specific items and stopping criteria
