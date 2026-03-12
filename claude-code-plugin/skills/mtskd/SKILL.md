---
name: "mtskd - Meta-Skill Design"
description: "Design skills that operate on other skills — improving, validating, combining, or routing them — with cross-skill compatibility."
output:
  format: "prose"
---

# MTSKD - Meta-Skill Design

**Input**: $ARGUMENTS

---

## Step 1: Identify the Meta-Operation

```
META-OPERATION: [improve | validate | combine | route | transform | audit]
DESCRIPTION: [what this meta-skill does to other skills]
TARGET SKILLS: [which skills this operates on — "any" if universal]
```

A meta-skill's input is another skill's output (or the skill itself). Classify the operation:

| Operation | What it does | Example |
|-----------|-------------|---------|
| **Improve** | Makes a skill's output better | Refine, deepen, add rigor |
| **Validate** | Checks whether a skill was applied correctly | Audit, verify, test |
| **Combine** | Merges outputs from multiple skills | Synthesize, integrate |
| **Route** | Decides which skill to invoke | Classify, dispatch |
| **Transform** | Changes format or level of a skill's output | Summarize, expand, translate |
| **Audit** | Checks the skill design itself | Meta-analysis of the procedure |

---

## Step 2: Design the Input

```
INPUT SPECIFICATION:
  ACCEPTS: [what the meta-skill takes as input]
  FORMAT: [the expected structure — e.g., "output block from any analytical skill"]
  MINIMUM REQUIREMENTS: [what the input must contain for the meta-skill to work]
  EXAMPLE INPUT: [a concrete example of valid input]

COMPATIBILITY:
  WORKS WITH: [list of skill categories or specific skills]
  DOES NOT WORK WITH: [skills whose output format is incompatible]
  ADAPTATION NEEDED: [skills that work but need output reformatting]
```

The input is the critical design decision. Too specific means the meta-skill only works with one skill. Too generic means it can't do anything meaningful.

---

## Step 3: Design What the Meta-Operation Adds

```
VALUE ADDED:
  BEFORE META-SKILL: [what the skill output looks like without this]
  AFTER META-SKILL: [what's different after applying it]
  SPECIFIC ADDITIONS:
    1. [what it adds or changes] — WHY: [what problem this solves]
    2. [addition] — WHY: [value]
    3. [addition] — WHY: [value]

MECHANISM:
  STEP 1: [what the meta-skill does first with the input]
  STEP 2: [next operation]
  STEP 3: [next operation]
  ...
  OUTPUT: [what the meta-skill produces]
```

The meta-skill must add value that the original skill cannot add itself. If a skill could do this internally, it should — no need for a meta-skill.

---

## Step 4: Ensure Cross-Skill Compatibility

```
COMPATIBILITY TESTING:
  SKILL 1: /[skill-id]
    INPUT FROM: [what this skill outputs]
    META-SKILL APPLIES: [yes | with adaptation | no]
    ADAPTATION NEEDED: [if any]
    EXPECTED OUTPUT: [what the meta-skill produces from this skill's output]

  SKILL 2: /[skill-id]
    INPUT FROM: [output]
    META-SKILL APPLIES: [yes | with adaptation | no]
    ADAPTATION NEEDED: [if any]
    EXPECTED OUTPUT: [result]

  SKILL 3: /[skill-id]
    INPUT FROM: [output]
    META-SKILL APPLIES: [yes | with adaptation | no]
    ADAPTATION NEEDED: [if any]
    EXPECTED OUTPUT: [result]
```

Test on at least 3 different skills. If the meta-skill only works on one type, it's not really a meta-skill — it's an extension of that specific skill.

---

## Step 5: Test on 3+ Different Skills

```
TEST RESULTS:
  TEST 1: /[skill] → /[meta-skill]
    SAMPLE INPUT: [abbreviated example]
    SAMPLE OUTPUT: [abbreviated example]
    VALUE ADDED: [what improved]
    ISSUES: [any problems encountered]

  TEST 2: /[skill] → /[meta-skill]
    SAMPLE INPUT: [example]
    SAMPLE OUTPUT: [example]
    VALUE ADDED: [improvement]
    ISSUES: [problems]

  TEST 3: /[skill] → /[meta-skill]
    SAMPLE INPUT: [example]
    SAMPLE OUTPUT: [example]
    VALUE ADDED: [improvement]
    ISSUES: [problems]

CROSS-SKILL VERDICT: [works universally | works with adaptations | limited compatibility]
```

---

## Output Summary

```
META-SKILL DESIGN
=================
NAME: [proposed skill id and name]
OPERATION: [improve | validate | combine | route | transform | audit]
INPUT: [what it accepts]
OUTPUT: [what it produces]
VALUE: [one sentence on what it adds]

MECHANISM:
  1. [step]
  2. [step]
  3. [step]

COMPATIBILITY: [count] skills tested
  UNIVERSAL: [yes | no]
  WORKS WITH: [list]
  LIMITATIONS: [where it breaks]

RECOMMENDED PLACEMENT: [where in skill chains this fits]
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Not actually meta** | Operates on raw user input, not skill output | Redesign to take skill output as input |
| **Only works with one skill** | Fails compatibility testing on 2+ skills | Generalize the input specification |
| **Adds no value** | Output is not meaningfully different from input | Identify what the original skill misses that this adds |
| **Too generic** | "Improve anything" with no specific mechanism | Define the exact operations performed |
| **Circular** | Meta-skill requires its own output as input | Break the circularity with a fixed starting point |

---

## Integration

- Use with: `/skcl` to position the meta-skill within a skill cluster
- Use with: `/gflr` to find gaps that a meta-skill could fill
- Use with: `/cmpr` to verify the meta-skill design is complete
- Use from: `/create` when designing new meta-level capabilities
- Differs from `/skcl`: mtskd designs individual meta-skills; skcl designs groups of related skills
