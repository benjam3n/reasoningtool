---
name: "bldk - Build"
description: Procedure for building or creating anything. Defines requirements, designs before building, builds incrementally, tests continuously, and iterates based on feedback.
output:
  format: "prose"
---

# Build

**Input**: $ARGUMENTS

---

## Step 1: Define What's Being Built

```
THING: [What you're building — product, feature, system, document, process, etc.]
FOR WHOM: [Who will use or benefit from this]
CORE NEED: [The single most important thing it must do]
```

---

## Step 2: Specify Requirements

Separate what's essential from what's optional.

```
MUST HAVE (ship-blocking):
1. [Requirement] — because [why it's essential]
2. [Requirement] — because [why it's essential]
3. [Requirement] — because [why it's essential]

SHOULD HAVE (important but not blocking):
1. [Requirement]
2. [Requirement]

NICE TO HAVE (if time permits):
1. [Requirement]

EXPLICITLY OUT OF SCOPE:
- [Thing you're choosing not to build]
- [Thing you're choosing not to build]
```

---

## Step 3: Design Before Building

```
APPROACH: [High-level description of how to build it]

KEY DECISIONS:
1. [Decision] — chose [option] because [reason]
2. [Decision] — chose [option] because [reason]

RISKS:
- [Risk 1] — mitigation: [approach]
- [Risk 2] — mitigation: [approach]

DEPENDENCIES:
- [What you need before you can start]
```

SKIP: If the thing is small enough to build in one sitting, skip to Step 4.

---

## Step 4: Build the Smallest Working Version

What is the minimum version that proves the concept works?

```
SMALLEST WORKING VERSION:
- Includes: [minimum feature set]
- Excludes: [everything else]
- Time to build: [estimate]
- How to test it: [what to check when it's done]
```

Build this first. Do not add features until this works.

---

## Step 5: Test and Iterate

After each increment, run these checks:

```
DOES IT WORK? [yes/no — if no, fix before adding anything]
DOES IT MEET THE CORE NEED? [yes/no]
WHAT DID I LEARN? [insight from building/testing]
WHAT TO BUILD NEXT? [next increment based on what I learned]
```

Repeat Step 5 for each increment until all MUST HAVE requirements are met.

---

## Step 6: Ship Decision

```
READINESS CHECK:
- All MUST HAVEs met: [yes/no]
- Tested with real use case: [yes/no]
- Known issues: [list any]
- Known issues are acceptable: [yes/no]

DECISION: SHIP / ITERATE MORE / RETHINK

IF SHIP:
- Ship as: [v1 / beta / MVP / final]
- Follow up with: [what to improve post-ship]

IF ITERATE:
- Focus on: [what needs more work]
- Timebox: [how long before re-evaluating]
```

---

## Integration

Use with:
- `/plsk` -> Evaluate the build plan before starting
- `/vldt` -> Validate at each build stage
- `/prsk` -> Analyze the finished product
- `/tmsk` -> Coordinate the build across a team
