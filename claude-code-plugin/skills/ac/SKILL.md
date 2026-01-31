---
name: "ac - Adversarial Checklist"
description: Create a checklist that catches what normal checklists miss. Each item includes adversarial branches -- what if this assumption is wrong? Chains assumption extraction, failure anticipation, assumption inversion, and steps generation.
---

# Adversarial Checklist

**Input**: $ARGUMENTS

---

## Purpose

Normal checklists say "check X" and move on. Adversarial checklists say "check X -- and if X looks fine, here's how it could STILL be wrong." They embed assumption-testing directly into the checklist format.

**What this produces**: A before-you-do-X checklist where each item has a "but what if?" branch that catches the failures normal checklists miss.

**This is a compound skill** -- it chains 4 skills in sequence.

---

## Depth Scaling

Default: 2x. Parse depth from $ARGUMENTS if specified (e.g., "/ac 4x [input]").

| Depth | Min Failure Modes | Min Adversarial Scenarios | Min Mitigation Checks | Min Red Team Passes |
|-------|------------------|--------------------------|----------------------|-------------------|
| 1x    | 5                | 2                        | 1                    | 1                 |
| 2x    | 8                | 3                        | 2                    | 1                 |
| 4x    | 12               | 5                        | 3                    | 2                 |
| 8x    | 18               | 8                        | 5                    | 3                 |
| 16x   | 25               | 12                       | 8                    | 4                 |

These are floors. Go deeper where insight is dense. Compress where it's not.

---

## The Chain

```
Step 1: /aex     -- What do people assume when doing this action?
Step 2: /fla      -- What goes wrong despite those assumptions?
Step 3: /ai      -- What if each assumption is wrong?
Step 4: /stg          -- Create the checklist with adversarial branches
```

---

## Execution Procedure

### Step 1: Extract Assumptions People Make

-> INVOKE: /aex $ARGUMENTS

When people are about to do [action], what do they assume?
- What do they take for granted?
- What do they skip checking because "it's obvious"?
- What hidden beliefs drive their preparation?

**Target**: 10-20 assumptions, ordered by how dangerous they are when wrong.

**Output**: Numbered list of assumptions with danger rating.

---

### Step 2: Anticipate Failures

-> INVOKE: /fla [action + assumptions from Step 1]

For each assumption, what goes wrong when it fails?
- What's the failure mode?
- How common is this failure?
- How bad is the outcome?
- How detectable is it before damage?

**Output**: Failure modes linked to assumptions, ranked by (frequency x severity).

---

### Step 3: Invert Critical Assumptions

-> INVOKE: /ai [top 10-15 assumptions by danger]

For each critical assumption, ask:
- What would you see if this assumption were WRONG?
- What's the earliest indicator of wrongness?
- What's the cheapest test to check?

**Output**: For each assumption, an observable check and a quick test.

---

### Step 4: Generate the Adversarial Checklist

-> INVOKE: /stg [assumptions, failures, inversions from Steps 1-3]

Create the checklist in this format:

```
BEFORE YOU [ACTION]: ADVERSARIAL CHECKLIST
==========================================

[ ] 1. CHECK: [What to verify]
       LOOKS GOOD? It could still be wrong if: [inversion]
       QUICK TEST: [How to actually verify in 2 minutes]
       IF WRONG: [What to do instead]

[ ] 2. CHECK: [Next item]
       LOOKS GOOD? It could still be wrong if: [inversion]
       QUICK TEST: [How to verify]
       IF WRONG: [What to do]

...

STOP-AND-THINK ITEMS (most commonly skipped):
[ ] [Item that feels unnecessary but catches the biggest failures]
[ ] [Item people skip because they're in a hurry]

RED FLAGS (stop everything if you see these):
- [Observable sign that something is fundamentally wrong]
- [Another red flag]
```

-> COMPLETE

---

## Output Standards

- Plain language, no jargon
- Each item is a concrete CHECK, not "consider" or "think about"
- Every CHECK has a QUICK TEST (under 2 minutes to perform)
- Every CHECK has an IF WRONG action
- Include STOP-AND-THINK items (the ones people skip)
- Include RED FLAGS (stop everything signals)
- Printable on one page when possible (two pages max)
- Validation status: "This checklist has not been validated by domain experts"

---

## What Makes This Different from Normal Checklists

| Normal Checklist | Adversarial Checklist |
|-----------------|----------------------|
| "Check that tests pass" | "Check that tests pass. Tests passing doesn't mean code works -- could be testing the wrong thing. QUICK TEST: Does any test actually exercise the changed code path?" |
| "Review the contract" | "Review the contract. Contract looking standard doesn't mean it IS standard. QUICK TEST: What's different from the last contract you signed? If nothing, check the definitions section." |
| "Confirm the meeting time" | "Confirm the meeting time. Confirmed time could still be wrong timezone. QUICK TEST: Say the time with timezone explicitly and get confirmation back." |

The adversarial branch catches failures that happen AFTER you check the item and it looks fine.

---

## Example Usage

```
/ac starting a new software project
/ac signing a lease or contract
/ac making a major purchase over $1000
/ac launching a product
/ac hiring a new employee
/ac before any important presentation
```
