---
name: "pusr - Power User Analysis"
description: Analyze from the perspective of expert users. Identifies power user needs around efficiency, customization, and depth, finds friction points, spots missing advanced features, and assesses the learning curve.
output:
  format: "prose"
---

# Power User Analysis

**Input**: $ARGUMENTS

---

## Step 1: Identify Power User Needs

Define what expert users require from this system.

```
SYSTEM: [what is being analyzed]
POWER USER PROFILE: [who are the expert users]

CORE POWER USER NEEDS:
Efficiency:
1. [need] — Current state: [met/unmet/partial]
2. [need] — Current state: [met/unmet/partial]

Customization:
1. [need] — Current state: [met/unmet/partial]
2. [need] — Current state: [met/unmet/partial]

Depth:
1. [need] — Current state: [met/unmet/partial]
2. [need] — Current state: [met/unmet/partial]

Control:
1. [need] — Current state: [met/unmet/partial]
2. [need] — Current state: [met/unmet/partial]
```

---

## Step 2: Find Friction Points

Identify where expert users hit unnecessary resistance.

```
FRICTION POINTS:
1. [friction] — Frequency: [every time / often / sometimes]
   Impact: [time wasted / flow broken / workaround needed]
   Root cause: [designed for beginners / oversight / technical debt]

2. [friction] — Frequency: [frequency]
   Impact: [impact]
   Root cause: [cause]

SPEED BUMPS (minor annoyances that compound):
- [annoyance]: costs [time/clicks/context-switches] per occurrence

WALLS (things power users simply cannot do):
- [limitation]: forces users to [workaround or abandonment]

BEGINNER-OPTIMIZED FRICTION (helpful for novices, blocks experts):
- [feature/guard]: protects novices but slows experts — Fix: [progressive disclosure]
```

---

## Step 3: Identify Missing Advanced Features

What do power users expect that doesn't exist?

```
MISSING ADVANCED FEATURES:
1. [feature] — Why expected: [standard in domain / requested / obvious need]
   Impact of absence: [what power users can't do]
   Complexity to add: [HIGH/MED/LOW]

2. [feature] — Why expected: [reason]
   Impact of absence: [limitation]
   Complexity to add: [level]

MISSING SHORTCUTS:
- [operation] currently takes [N steps] — could be [fewer]

MISSING AUTOMATION:
- [repetitive task] that power users would want to automate

MISSING COMPOSABILITY:
- [feature A] and [feature B] can't be combined but should be
```

---

## Step 4: Assess Advanced Learning Curve

How hard is it for someone to go from competent to expert?

```
LEARNING CURVE ASSESSMENT:

NOVICE → COMPETENT: [easy / moderate / hard] — Time: [estimate]
COMPETENT → ADVANCED: [easy / moderate / hard] — Time: [estimate]
ADVANCED → EXPERT: [easy / moderate / hard] — Time: [estimate]

KNOWLEDGE CLIFFS (sudden jumps in required knowledge):
1. [cliff] — Between [level A] and [level B] — Barrier: [what's hard to learn]

HIDDEN FEATURES (powerful but undiscoverable):
1. [feature] — How to find it: [method] — Why hidden: [reason]

DOCUMENTATION GAPS FOR EXPERTS:
- [topic] lacks advanced documentation
- [topic] only covers basic usage
```

---

## Step 5: Power User Satisfaction Score

```
POWER USER SCORECARD:
| Dimension | Score (1-5) | Notes |
|-----------|------------|-------|
| Efficiency | [score] | [detail] |
| Customization | [score] | [detail] |
| Depth | [score] | [detail] |
| Control | [score] | [detail] |
| Composability | [score] | [detail] |
| Advanced docs | [score] | [detail] |

OVERALL: [score] / 5

TOP POWER USER REQUEST: [the single most impactful improvement]
QUICK WINS: [changes that would most improve expert experience with least effort]

RECOMMENDATIONS:
1. [action] — Addresses: [need] — Effort: [level]
2. [action] — Addresses: [need] — Effort: [level]
3. [action] — Addresses: [need] — Effort: [level]
```

---

## Integration

Use with:
- `/nusr` -> Compare power user needs against new user needs
- `/usnd` -> Validate power user needs with evidence
- `/cdiff` -> Check if power user features differentiate from competitors
