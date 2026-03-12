---
name: "stnl - Standalone Skill Design"
description: Guides the design of a skill that works independently with no dependencies on other skills. Ensures the skill is self-contained, well-scoped, and useful in isolation.
output:
  format: "prose"
---

# Standalone Skill Design

**Input**: $ARGUMENTS

---

## Step 1: Define the Skill's Purpose

State clearly what the skill does in one sentence.

```
SKILL NAME: [short lowercase abbreviation]
PURPOSE: [what it does — one sentence]
TRIGGER: [when a user would reach for this skill]
```

Gut-check: If someone used ONLY this skill and nothing else, would they get value? If no, this isn't a standalone skill.

---

## Step 2: Define Input/Output Contract

Specify exactly what goes in and what comes out.

```
INPUT:
- Required: [what the user must provide]
- Optional: [what improves results but isn't necessary]
- Format: [free text / structured / list / etc.]

OUTPUT:
- Delivers: [what the user gets back]
- Format: [how it's structured]
- Actionable: [yes/no — can the user act on the output directly?]
```

SKIP: If input is simply free text and output is analysis, state that in one line.

---

## Step 3: Ensure Self-Containment

Check that the skill embeds all necessary context.

```
DEPENDENCY CHECK:
- Requires domain knowledge?  [yes/no — if yes, embed it]
- Requires prior skill output?  [yes/no — if yes, this isn't standalone]
- Requires external data?  [yes/no — if yes, specify what]
- Requires user to know other skills?  [no — must be usable cold]
```

Rule: A standalone skill must be the first skill someone uses. No prerequisites.

---

## Step 4: Build the Steps

Design 4-7 steps that move from input to output.

For each step:
- What does it do?
- What does it produce?
- Can it be skipped? (add SKIP condition if so)

```
STEPS:
1. [Step name]: [what it does] → produces [output]
   SKIP: [condition, if any]
2. [Step name]: [what it does] → produces [output]
   ...
```

Rules:
- Each step should be completable without referencing another skill
- Steps should build on each other linearly
- The final step should produce the promised output

---

## Step 5: Test in Isolation

Verify the skill works without any context from other skills.

```
ISOLATION TEST:
- Cold start: Can a user invoke this with zero prior context? [yes/no]
- Self-explanatory: Does the skill explain its own terms? [yes/no]
- Complete: Does the user need to invoke another skill after? [no]
- Valuable: Is the output useful on its own? [yes/no]
```

If any answer is wrong, go back and fix the design.

---

## Step 6: Write the Skill File

Produce the complete SKILL.md content.

```
SKILL FILE:

---
name: "[abbreviation] - [Full Name]"
description: [one-sentence description]
---

# [Full Name]

**Input**: $ARGUMENTS

---

[Steps from Step 4, fully written out with formatting,
skip conditions, and output blocks]

---

## Integration

Use with:
- [skill 1] -> [how it connects]
- [skill 2] -> [how it connects]
```

Note: Integration section lists optional companions, not requirements.

---

## Integration

Use with:
- `/chns` -> If the skill should also work in chains, design chain points after
- `/injc` -> If the skill could double as an injectable step
- `/sp` -> Steelman the skill's prompt structure before finalizing
