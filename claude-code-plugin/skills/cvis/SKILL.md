---
name: "cvis - Creator Vision Analysis"
description: Analyze a project from the creator's perspective. Articulates the vision, checks whether current work serves it, identifies vision drift, and recommends corrections.
---

# Creator Vision Analysis

**Input**: $ARGUMENTS

---

## Step 1: Articulate the Vision

Extract and formalize the creator's vision, whether explicit or implicit.

```
PROJECT: [what is being analyzed]
CREATOR: [who created it / whose vision]

EXPLICIT VISION (stated):
- [stated goals, mission, purpose]

IMPLICIT VISION (inferred from choices):
- [pattern 1] suggests: [inferred goal]
- [pattern 2] suggests: [inferred goal]

CORE VISION STATEMENT:
[One clear sentence capturing what this project is trying to be]

VISION BOUNDARIES:
- This IS about: [what's in scope]
- This is NOT about: [what's deliberately excluded]
- The audience IS: [who it's for]
- The audience is NOT: [who it's not for]
```

---

## Step 2: Check Alignment

Evaluate whether current work serves the articulated vision.

```
ALIGNMENT CHECK:
| Component/Decision | Serves Vision? | How | Confidence |
|-------------------|---------------|-----|------------|
| [item 1] | YES / NO / PARTIAL | [explanation] | [HIGH/MED/LOW] |
| [item 2] | YES / NO / PARTIAL | [explanation] | [HIGH/MED/LOW] |
...

STRONGLY ALIGNED (vision amplifiers):
1. [component] — Why: [how it embodies the vision]

WEAKLY ALIGNED (technically compatible but not advancing):
1. [component] — Why: [it doesn't conflict but doesn't help either]

MISALIGNED (working against the vision):
1. [component] — Why: [how it contradicts or dilutes the vision]
```

---

## Step 3: Identify Vision Drift

Detect where the project has drifted from its original or core vision.

```
VISION DRIFT ANALYSIS:

DRIFT INDICATORS:
1. [indicator] — Original direction: [X] → Current direction: [Y]
   Drift cause: [feature creep / external pressure / lost focus / evolution]
2. [indicator] — Original direction: [X] → Current direction: [Y]
   Drift cause: [reason]

DRIFT TYPE:
- Gradual expansion: [scope growing beyond vision?]
- Audience shift: [serving different users than intended?]
- Priority inversion: [secondary goals overtaking primary?]
- Identity confusion: [trying to be too many things?]

DRIFT SEVERITY: [NONE / MINOR / MODERATE / MAJOR]
DRIFT TRAJECTORY: [getting worse / stable / self-correcting]
```

---

## Step 4: Vision Coherence

Assess whether the vision itself is clear and internally consistent.

```
VISION COHERENCE:

CLARITY: [HIGH/MED/LOW]
- Can someone new understand what this is trying to be? [Y/N — why]

INTERNAL CONSISTENCY: [HIGH/MED/LOW]
- Contradictions found:
  1. [goal A] conflicts with [goal B] because [reason]

ACHIEVABILITY: [HIGH/MED/LOW]
- Vision vs. reality gap: [description]
- Resources match ambition? [Y/N]

DISTINCTIVENESS: [HIGH/MED/LOW]
- Would someone confuse this with [alternative]? [Y/N — why]
```

---

## Step 5: Recommend Corrections

```
RECOMMENDATIONS:

VISION REFINEMENT (if the vision itself needs work):
- [suggestion for clarifying or sharpening the vision]

REALIGNMENT ACTIONS (if execution drifted from vision):
1. [action] — Fixes: [drift] — Priority: [HIGH/MED/LOW]
2. [action] — Fixes: [drift] — Priority: [HIGH/MED/LOW]

THINGS TO STOP DOING:
- [activity] — Reason: [doesn't serve vision]

THINGS TO START DOING:
- [activity] — Reason: [would serve vision]

THINGS TO KEEP DOING:
- [activity] — Reason: [strongly aligned with vision]

VISION HEALTH: [STRONG / HEALTHY / DRIFTING / AT RISK]
```

---

## Integration

Use with:
- `/ecomp` -> Check if the ecosystem matches the vision
- `/gapf` -> Find gaps between vision and current reality
- `/usnd` -> Validate that the vision addresses real user needs
