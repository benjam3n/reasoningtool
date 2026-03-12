---
name: "obv - Obvious Check"
description: Add an obvious-things-first step to any analysis. Catches what everyone assumes someone else checked.
output:
  format: "prose"
---

# Obvious Check

**Input**: $ARGUMENTS

---

## Purpose

The most common failure mode in analysis is missing the obvious. Not because it's hard to see — because everyone assumes someone already checked it. This skill adds the "did anyone actually look?" step.

Can be applied standalone or injected into any other skill's output.

---

## Step 1: STATE THE SITUATION

What is being analyzed, decided, or planned?

```
SUBJECT: [one sentence]
```

---

## Step 2: THE OBVIOUS QUESTIONS

Answer each. If you can't answer confidently, that's a finding.

### A. Obvious Facts
1. What is the single most basic fact about this situation? Is it confirmed?
2. What would a newcomer ask first? Has that been answered?
3. What does everyone involved "know" but nobody has verified?
4. Is the problem actually what we think it is? (Have we checked?)

### B. Obvious Actions
5. What is the simplest thing that could work? Has it been tried?
6. What would cost almost nothing to try? Has it been tried?
7. Is there a standard solution that already exists? Have we looked?
8. Has someone already solved this exact problem? Have we checked?

### C. Obvious Risks
9. What is the most likely thing to go wrong? Is there a plan for it?
10. What happens if we do nothing? Is that actually bad?
11. What is the most obvious way this fails? Are we protected?
12. Is there a deadline or constraint we're ignoring?

### D. Obvious Oversights
13. Who haven't we talked to that we obviously should?
14. What information do we not have that we obviously need?
15. What assumption are we making that we haven't stated?
16. What are we optimizing for? Is that the right thing?

---

## Step 3: OBVIOUS VERDICT

```
OBVIOUS CHECK RESULTS:

Confirmed obvious:
- [things that were checked and are fine]

Unchecked obvious:
- [things nobody actually verified]

Obvious actions not taken:
- [simple things that haven't been tried]

Obvious risks unaddressed:
- [likely failure modes with no plan]

STOP SIGNAL: [YES if any unchecked obvious item could change the conclusion / NO if basics are covered]
```

If STOP SIGNAL is YES: Address the unchecked items before continuing with more sophisticated analysis.

---

## Step 4: INJECTION MODE

When used as a step within another skill, output only:

```
OBVIOUS CHECK:
- [x] [checked item — confirmed]
- [ ] [unchecked item — NEEDS ATTENTION]
- [ ] [unchecked item — NEEDS ATTENTION]

Proceed: [YES / NO — address unchecked items first]
```

---

## Integration

Use with:
- Any skill — inject as a first step before deeper analysis
- `/ogo` -> Specifically check for obvious good outcomes
- `/obo` -> Specifically check for obvious bad outcomes
- `/oba` -> Full obvious-everything scan
- `/rca` -> When the obvious cause hasn't been ruled out
