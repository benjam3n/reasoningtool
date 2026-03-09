---
name: "p3chain - Pick 3 Chain"
description: "Pick 3 skills that form a tight workflow chain starting from a given skill. Traces invocation links to build a connected sequence. Standalone implementation of the CHAIN algorithm from /pick with N=3."
tier: "tier4"
categories: ["Meta & Navigation"]
tags: ["shortcut", "pick", "discovery", "chain", "workflow"]
---

# Pick 3 Chain

**Input**: $ARGUMENTS

---

## Core Principles

1. **Chains are workflows, not lists.** The 3 skills must form a connected sequence where each skill's output feeds the next skill's input. A list of 3 unrelated skills is not a chain — it's a menu.

2. **Three is a complete arc.** A 3-skill chain should form a complete thinking arc: setup -> core operation -> validation (or input -> transform -> output). Each position in the chain has a role.

3. **Follow invocation links first.** The skill graph already encodes workflows through invokes/invoked_by. Start by tracing these existing links before constructing novel chains.

4. **Chains run in one direction.** The execution order must be unambiguous. Step 1 produces output that Step 2 requires. Step 2 produces output that Step 3 requires. No loops, no optional branches.

5. **The seed determines the chain.** The user provides a starting skill. The chain builds OUTWARD from that seed — either forward (what the seed invokes) or backward (what invokes the seed) or both.

---

## Phase 1: Seed Analysis

```
[A] SEED: /[skill from $ARGUMENTS]
[B] SEED_FUNCTION: [what does this skill do?]
[C] SEED_OUTPUTS: [what does it produce?]
[D] SEED_INVOKES: [skills it calls — forward chain candidates]
[E] SEED_INVOKED_BY: [skills that call it — backward chain candidates]
[F] SEED_CATEGORY: [category from skills.json]
```

Read the seed skill's SKILL.md to understand its inputs and outputs.

```
[G] SEED_INPUTS: [what does the seed skill need as input?]
[H] SEED_GAPS: [what does the seed NOT do that the user might need?]
```

---

## Phase 2: Chain Construction

Three chain strategies, tried in order of preference:

### Strategy 1: Forward Chain (seed is Step 1)

```
[I] FORWARD:
    Step 1: SEED → produces [output]
    Step 2: Which invoked skill best uses that output? → select
    Step 3: What does Step 2 produce? → Which skill best uses THAT? → select

    Chain: SEED → [step 2] → [step 3]
```

### Strategy 2: Backward Chain (seed is Step 3)

```
[J] BACKWARD:
    Step 3: SEED ← needs [input]
    Step 2: Which invoking skill produces that input? → select
    Step 1: What does Step 2 need? → Which skill produces THAT? → select

    Chain: [step 1] → [step 2] → SEED
```

### Strategy 3: Center Chain (seed is Step 2)

```
[K] CENTER:
    Step 2: SEED ← needs [input], produces [output]
    Step 1: Which skill produces what SEED needs? → select
    Step 3: Which skill uses what SEED produces? → select

    Chain: [step 1] → SEED → [step 3]
```

### Strategy Selection

```
[L] STRATEGY_SELECTION:
    IF seed has strong forward invocations → FORWARD
    IF seed has strong backward invocations → BACKWARD
    IF seed has both → CENTER
    IF seed has neither → construct novel chain based on function/category

    SELECTED: [strategy]
```

---

## Phase 3: Chain Validation

```
[M] VALIDATION:

Step 1: Does Step 1's output match Step 2's input? [Y/N — describe the connection]
Step 2: Does Step 2's output match Step 3's input? [Y/N — describe the connection]
Step 3: Is there a clear purpose for this chain? [state it in one sentence]
Step 4: Could the chain run in reverse and still make sense? [Y/N — if Y, the chain logic may be weak]
Step 5: Does each step add something the previous step couldn't do? [Y/N for each]
```

---

## Phase 4: Output

```
ALGORITHM: CHAIN
SEED: /[seed skill]
CHAIN LENGTH: 3
STRATEGY: [forward / backward / center]

CHAIN:
  Step 1: /[id] — [title]
     Role: [what it does in this chain]
     Produces: [output that feeds Step 2]
     ↓ feeds into
  Step 2: /[id] — [title]
     Role: [what it does in this chain]
     Receives: [from Step 1] | Produces: [output that feeds Step 3]
     ↓ feeds into
  Step 3: /[id] — [title]
     Role: [what it does in this chain]
     Receives: [from Step 2] | Produces: [final output]

CHAIN PURPOSE: [1-sentence: what does running this chain accomplish?]
CHAIN ARC: [setup → core → validation / input → transform → output / etc.]

ALTERNATIVE CHAINS:
  Alt 1: /[id] → /[id] → /[id] — [1-line what this chain does differently]
  Alt 2: /[id] → /[id] → /[id] — [1-line]
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Disconnected chain** | No clear output→input link between steps | Verify: what does Step N produce that Step N+1 needs? |
| **Reversible chain** | Chain works equally well backward — no directional logic | Identify which step DEPENDS on a prior step's output |
| **Redundant steps** | Two steps do the same thing at different depths | Each step must add a NEW capability |
| **Forced connections** | Chain exists only because skills share a category, not because outputs link | Links must be functional (output→input), not categorical |
| **Seed orphaned** | Seed has no invokes or invoked_by, and no natural partners | Construct based on function: what comes before/after this type of analysis? |
| **Chain too long** | Chain has implied steps between the 3 — it's really a 5-chain compressed | Each step should be directly adjacent — no skipped steps |

---

## Depth Scaling

| Depth | Seed Analysis | Chain Construction | Alternatives |
|-------|--------------|-------------------|-------------|
| 1x | Metadata only (invokes/invoked_by) | Single strategy, first valid chain | None |
| 2x | Read seed SKILL.md for inputs/outputs | Try all 3 strategies, pick best | 1-2 alternative chains |
| 4x | Read seed + connected skills | All strategies + novel chain construction | 3+ alternatives with tradeoff analysis |
| 8x | Full neighborhood analysis (seed + 2 hops) | Exhaustive chain enumeration | Ranked alternatives with use-case matching |

Default: 2x. These are floors.

---

## Pre-Completion Checklist

- [ ] Seed skill read and its inputs/outputs identified
- [ ] Chain strategy selected with rationale
- [ ] Exactly 3 skills in the chain (including seed)
- [ ] Each step's output feeds the next step's input
- [ ] Chain purpose stated in one sentence
- [ ] Each step adds a unique capability
- [ ] At least 1 alternative chain provided

---

## Integration

- **Shortcut for**: `/pick 3 chain $ARGUMENTS`
- **Use when**: You have a skill and want to know what comes before/after it
- **Routes to**: The 3 chain skills in sequence; `/to` for longer workflow design
- **Related**: `/p10complement` (broader pairing), `/de` (dependency extraction)
- **Differs from /p10complement**: complement finds 10 partners; chain finds 3 in sequence
- **Differs from /de**: de extracts dependencies from a project; chain builds a skill workflow
