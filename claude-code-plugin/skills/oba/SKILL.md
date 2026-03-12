---
name: "oba - Obvious Anything"
description: Comprehensive obvious-things scan. Checks for everything obvious that might be missed — facts, actions, risks, outcomes, stakeholders, and assumptions.
output:
  format: "prose"
---

# Obvious Anything

**Input**: $ARGUMENTS

---

## Purpose

Combines all obvious-check dimensions into one comprehensive scan. Use this when you want to catch everything obvious before doing deeper analysis, or as a quality gate on any skill's output.

---

## Step 1: STATE THE SITUATION

```
SUBJECT: [one sentence description]
CONTEXT: [what analysis or decision is happening]
```

---

## Step 2: FULL OBVIOUS SCAN

### A. Obvious Facts
- What is the most basic fact here? Is it confirmed?
- What does everyone "know" that nobody has verified?
- What would a child ask about this situation?

### B. Obvious Good Outcomes
→ INVOKE: /ogo $ARGUMENTS (abbreviated — top 3 only)

### C. Obvious Bad Outcomes
→ INVOKE: /obo $ARGUMENTS (abbreviated — top 3 only)

### D. Obvious Actions
- What is the simplest thing to try? Has it been tried?
- What costs nothing to attempt?
- What standard solution already exists?

### E. Obvious Stakeholders
- Who is obviously affected that hasn't been consulted?
- Who has obvious expertise that hasn't been asked?
- Who has obvious authority or veto power?

### F. Obvious Assumptions
- What is being assumed without stating it?
- What would change if the opposite were true?
- What "goes without saying" that should be said?

### G. Obvious Timing
- Is there an obvious deadline being ignored?
- Is there an obvious "too late" point?
- Is the timing obviously wrong (too early, too late)?

### H. Obvious Precedent
- Has this exact thing been done before? What happened?
- Is there an obvious analogy nobody has mentioned?
- What does history obviously suggest?

---

## Step 3: OUTPUT

```
OBVIOUS ANYTHING SCAN:

CONFIRMED OBVIOUS (checked and fine):
- [item]
- [item]

UNCHECKED OBVIOUS (nobody verified):
- [item] — ACTION: [what to do]
- [item] — ACTION: [what to do]

IGNORED OBVIOUS (known but being minimized):
- [item] — WHY IT MATTERS: [impact]

MISSING OBVIOUS (should be present but isn't):
- [item] — RECOMMENDATION: [what to add]

OVERALL: [Everything obvious is covered / N items need attention before proceeding]
```

---

## Step 4: INJECTION INTO OTHER SKILLS

When used as a quality gate on another skill's output:

```
OBVIOUS GATE on [skill name] output:

PASSED:
- [x] Basic facts confirmed
- [x] Obvious good outcomes acknowledged
- [x] Obvious bad outcomes addressed

FAILED:
- [ ] [unchecked item] — must address before output is valid

VERDICT: [PASS / FAIL — address items before accepting output]
```

---

## Integration

Use with:
- Any skill — as a pre-check or post-check
- `/obv` -> Focused obvious check (facts, actions, risks, oversights)
- `/ogo` -> Deep dive on obvious good outcomes
- `/obo` -> Deep dive on obvious bad outcomes
- `/vbo` -> Verification before output
