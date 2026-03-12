---
name: "chns - Chainable Skill Design"
description: Guides the design of skills that compose well with other skills, with clean input/output contracts and narrow scope for reliable handoffs.
output:
  format: "prose"
---

# Chainable Skill Design

**Input**: $ARGUMENTS

---

## Step 1: Define Scope Narrowly

A chainable skill does one thing well. Define it.

```
SKILL NAME: [abbreviation]
DOES: [single responsibility — one verb, one noun]
RECEIVES FROM: [what upstream skills might feed it]
FEEDS INTO: [what downstream skills might consume its output]
```

Rule: If you can't state the scope in under 10 words, it's too broad to chain cleanly.

---

## Step 2: Define Input Contract

Specify what the skill accepts — this is the interface upstream skills must match.

```
INPUT CONTRACT:
- Type: [claim / decision / list / analysis / structured data]
- Required fields: [what must be present]
- Optional fields: [what enriches but isn't needed]
- Accepts raw user input: [yes/no]
- Accepts output from: [list of compatible upstream skills]

EXAMPLE INPUT:
[a concrete example of valid input]
```

Key: If the skill accepts raw user input AND structured skill output, it works in chains and standalone.

---

## Step 3: Define Output Contract

Specify what the skill produces — this is the interface downstream skills will consume.

```
OUTPUT CONTRACT:
- Type: [claim / decision / list / analysis / structured data]
- Structure: [describe the output format]
- Guaranteed fields: [what's always present]
- Optional fields: [what's sometimes present]
- Compatible with: [list of downstream skills that can accept this]

EXAMPLE OUTPUT:
[a concrete example of the output]
```

Rule: Output must be parseable by the next skill without human reformatting.

---

## Step 4: Design the Transform

Define the steps that convert input to output.

```
TRANSFORM:
1. [Step]: [input field] → [intermediate result]
2. [Step]: [intermediate] → [intermediate result]
3. [Step]: [intermediate] → [output field]
```

Constraints:
- No step should require information not in the input contract
- No step should produce output not in the output contract
- Keep to 3-5 transformation steps maximum

---

## Step 5: Design Handoff Points

Specify where other skills can attach.

```
HANDOFF POINTS:
- BEFORE this skill: [what should be done upstream]
  Compatible skills: [list]
- AFTER this skill: [what should be done downstream]
  Compatible skills: [list]
- INSTEAD of this skill: [alternatives for the same slot]
  Compatible skills: [list]
```

---

## Step 6: Test in Chains

Verify the skill chains correctly by testing three patterns.

```
CHAIN TEST 1 (upstream):
  [Skill A] → [THIS SKILL] → does input contract match A's output? [yes/no]

CHAIN TEST 2 (downstream):
  [THIS SKILL] → [Skill B] → does output contract match B's input? [yes/no]

CHAIN TEST 3 (full chain):
  [Skill A] → [THIS SKILL] → [Skill B] → does the full chain work? [yes/no]
```

If any test fails, revise the contracts.

---

## Step 7: Document Chaining Patterns

List the most useful chains this skill participates in.

```
RECOMMENDED CHAINS:
1. [Skill A] → [THIS] → [Skill B]: [what this chain accomplishes]
2. [Skill C] → [THIS] → [Skill D]: [what this chain accomplishes]
3. [THIS] → [Skill E]: [what this chain accomplishes]
```

---

## Integration

Use with:
- `/stnl` -> Ensure the skill also works standalone
- `/wrps` -> If the skill should enhance another skill's output
- `/orcs` -> If building a router that dispatches to chainable skills
