---
name: "upth - Unproceduralized Thinking"
description: Identify cognitive operations that don't have explicit procedures yet. Observes thinking processes, surfaces implicit steps and tacit knowledge, formalizes them into explicit procedures, tests, and refines.
output:
  format: "prose"
---

# Unproceduralized Thinking

**Input**: $ARGUMENTS

---

## Step 1: Observe the Thinking Process

Watch how the task or domain is actually approached, step by step.

```
DOMAIN: [what area of thinking is being examined]
TASK: [specific task or class of tasks]

OBSERVABLE STEPS (what people visibly do):
1. [step] — Seems to require: [skill/knowledge]
2. [step] — Seems to require: [skill/knowledge]
...

DECISION POINTS (where choices are made):
1. [decision] — Based on: [criteria, if visible]
2. [decision] — Based on: [criteria, if visible]
```

---

## Step 2: Identify Implicit Steps

Find the steps people take without articulating them.

```
IMPLICIT STEPS (done automatically, rarely explained):
1. [step] — Evidence it's happening: [how we know]
   Currently described as: [vague description like "use judgment" or "just know"]
2. [step] — Evidence it's happening: [how we know]
   Currently described as: [vague description]

MAGIC STEPS (described as "intuition" or "experience"):
1. [step] — What's actually happening: [hypothesis]
2. [step] — What's actually happening: [hypothesis]

GAP PHRASES (language that hides unformalized thinking):
- "It depends" → Depends on what? [specifics]
- "Use your judgment" → What criteria? [specifics]
- "You just know" → Know from what signals? [specifics]
```

---

## Step 3: Surface Tacit Knowledge

Extract the knowledge that experts have but can't easily articulate.

```
TACIT KNOWLEDGE INVENTORY:
1. [knowledge item]
   Expert has it: [YES]
   Can articulate it: [NO / PARTIALLY]
   Extraction method: [observation / probing questions / contrasting cases]

2. [knowledge item]
   Expert has it: [YES]
   Can articulate it: [NO / PARTIALLY]
   Extraction method: [method]

PATTERN RECOGNITION (experts see patterns novices miss):
- Pattern: [what they notice] → Meaning: [what it indicates]

HEURISTICS (rules of thumb used unconsciously):
- [heuristic]: used when [context]
```

---

## Step 4: Formalize Into Explicit Steps

Convert implicit knowledge into a followable procedure.

```
FORMALIZED PROCEDURE:

Step 1: [explicit action]
  - Input: [what you need]
  - Decision criteria: [how to choose]
  - Output: [what you produce]

Step 2: [explicit action]
  - Input: [from previous step]
  - Decision criteria: [how to choose]
  - Output: [what you produce]
...

DECISION TREES (for "it depends" moments):
If [condition A] → do [X]
If [condition B] → do [Y]
Otherwise → do [Z]

QUALITY CHECKS (for "you just know" moments):
- Check: [specific thing to verify]
- Good looks like: [concrete description]
- Bad looks like: [concrete description]
```

---

## Step 5: Test the Procedure

Evaluate whether the formalized procedure actually works.

```
TEST CASES:
1. [scenario] — Procedure output: [result] — Expert would do: [result] — Match? [Y/N]
2. [scenario] — Procedure output: [result] — Expert would do: [result] — Match? [Y/N]

EDGE CASES WHERE PROCEDURE FAILS:
- [case]: procedure says [X] but correct answer is [Y]
  Missing element: [what the procedure doesn't capture]

COVERAGE: [what % of cases does the procedure handle correctly?]
```

---

## Step 6: Refine

```
REFINEMENTS NEEDED:
1. [gap in procedure] → Add: [new step or criterion]
2. [gap in procedure] → Add: [new step or criterion]

REMAINING TACIT KNOWLEDGE (cannot yet be proceduralized):
- [item]: Why resistant: [explanation]

FINAL PROCEDURE QUALITY:
- Explicitness: [HIGH/MED/LOW]
- Completeness: [HIGH/MED/LOW]
- Usability by non-expert: [HIGH/MED/LOW]

RECOMMENDED USE: [who should use this procedure and when]
```

---

## Integration

Use with:
- `/gapf` -> Find gaps in the formalized procedure
- `/dxpt` -> Have a domain expert validate the procedure
- `/nusr` -> Test if newcomers can follow the procedure
