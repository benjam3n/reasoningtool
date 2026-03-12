---
name: "nusr - New User Accessibility"
description: Analyze from the newcomer's perspective. Simulates first-use experience, identifies confusion points, assesses onboarding path, finds jargon and assumed knowledge, and recommends simplifications.
output:
  format: "prose"
---

# New User Accessibility

**Input**: $ARGUMENTS

---

## Step 1: Simulate First-Use Experience

Walk through the system as if encountering it for the first time.

```
SYSTEM: [what is being analyzed]
NEW USER PROFILE: [who is the typical newcomer]
ENTRY POINT: [how new users first encounter this]

FIRST IMPRESSIONS:
1. [what the user sees/reads first] — Clear? [Y/N] — Reaction: [likely response]
2. [next thing encountered] — Clear? [Y/N] — Reaction: [likely response]
...

FIRST TASK ATTEMPT:
- Goal: [what a new user would try to do first]
- Steps required: [actual steps]
- Steps obvious: [which steps are discoverable]
- Time to first success: [estimate]
- Likely failure points: [where they'd get stuck]
```

---

## Step 2: Identify Confusion Points

Find where new users would be lost, overwhelmed, or misled.

```
CONFUSION POINTS:
1. [point] — Type: [ambiguous / overwhelming / missing context / contradictory]
   What user thinks: [their interpretation]
   What's actually meant: [correct interpretation]
   Fix: [suggestion]

2. [point] — Type: [type]
   What user thinks: [interpretation]
   What's actually meant: [reality]
   Fix: [suggestion]

OVERWHELM POINTS (too much at once):
- [where]: [how many options/concepts presented simultaneously]

DEAD ENDS (user gets stuck with no guidance):
- [where]: [what's missing to help them proceed]
```

---

## Step 3: Assess Onboarding Path

Evaluate whether there's a clear path from "never used it" to "productive."

```
ONBOARDING PATH:
| Step | Exists? | Quality | Barrier |
|------|---------|---------|---------|
| Discover the system | [Y/N] | [rating] | [barrier] |
| Understand what it does | [Y/N] | [rating] | [barrier] |
| Try it for the first time | [Y/N] | [rating] | [barrier] |
| Complete first real task | [Y/N] | [rating] | [barrier] |
| Build a habit | [Y/N] | [rating] | [barrier] |

TIME TO VALUE: [how long until a new user gets real value]
DROP-OFF RISK: [where users are most likely to abandon]

ONBOARDING GAPS:
- Between [step A] and [step B]: [what's missing]
```

---

## Step 4: Find Jargon and Assumed Knowledge

Identify language and concepts that assume prior expertise.

```
JARGON AUDIT:
1. [term/phrase] — Assumes knowledge of: [domain/concept]
   Used where: [location]
   Plain alternative: [simpler version]

2. [term/phrase] — Assumes knowledge of: [domain/concept]
   Used where: [location]
   Plain alternative: [simpler version]

ASSUMED KNOWLEDGE:
- [concept] is assumed but never explained — Needed for: [what]
- [concept] is assumed but never explained — Needed for: [what]

ACRONYMS WITHOUT EXPANSION:
- [acronym]: [what it means] — First appears: [where]

INSIDER REFERENCES:
- [reference] assumes familiarity with [context]
```

---

## Step 5: Recommend Simplifications

```
SIMPLIFICATION RECOMMENDATIONS:

IMMEDIATE FIXES (low effort, high impact):
1. [fix] — Addresses: [confusion point] — Effort: [minimal]
2. [fix] — Addresses: [confusion point] — Effort: [minimal]

ONBOARDING IMPROVEMENTS:
1. [improvement] — Helps at: [stage] — Expected impact: [description]
2. [improvement] — Helps at: [stage] — Expected impact: [description]

CONTENT REWRITES:
1. [what to rewrite] — Currently: [problem] — Should be: [approach]

STRUCTURAL CHANGES:
1. [change] — Currently: [problem] — Proposed: [solution]

NEW USER ACCESSIBILITY SCORE:
- First impression clarity: [1-5]
- Time to first success: [1-5]
- Jargon level: [1-5, where 5 = jargon-free]
- Onboarding completeness: [1-5]
- OVERALL: [score] / 5

GOLDEN PATH: [the ideal first-five-minutes experience to design for]
```

---

## Integration

Use with:
- `/pusr` -> Balance new user simplicity against power user needs
- `/usnd` -> Discover what new users actually need vs what we assume
- `/cvis` -> Ensure simplifications don't compromise the creator's vision
