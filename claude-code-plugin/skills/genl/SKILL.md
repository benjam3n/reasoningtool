---
name: "genl - General Analysis"
description: "Analyze at the general level — extract principles, patterns, and transferable insights rather than situation-specific answers. Find the general rule that explains the specific case."
---

# General Analysis

**Input**: $ARGUMENTS

---

## Core Principles

1. **The general explains the specific.** When someone asks "why did my project fail?", a specific answer is "you ran out of money." A general answer is "projects with unclear revenue models and 18+ month runways to profitability have a structural funding risk." The general answer explains not just this failure but a class of failures.

2. **Generalization is abstraction with verification.** Taking one case and saying "this always happens" is not generalization — it's overfitting. Real generalization requires identifying the MECHANISM that makes the pattern hold, then testing whether the mechanism is present in other cases.

3. **The right level of generality is the one that's useful.** "Everything is connected" is too general — it's true but actionless. "This specific bug is on line 47" is too specific — it doesn't help with the next bug. The right level explains the CLASS of problem while being specific enough to act on.

4. **General principles have boundary conditions.** "First-mover advantage matters" is a general principle, but it only holds when switching costs are high and network effects exist. A general principle without stated boundaries is a platitude. State where the principle applies and where it breaks down.

5. **Transfer is the test.** A properly generalized insight should be applicable to at least one DIFFERENT situation than the one it was derived from. If the "general" insight only explains the original case, it's not general — it's a specific answer in disguise.

---

## Phase 1: Specific Case Extraction

Start from the specific input.

```
[G1] SPECIFIC_CASE: [the situation, problem, or question as stated]
[G2] SPECIFIC_ANSWER: [what the specific, situational answer would be]
[G3] DOMAIN: [the domain this specific case comes from]
[G4] GENERALIZATION_GOAL: [what kind of general insight is sought — principle, pattern, framework, law]
```

---

## Phase 2: Pattern Identification

Extract the underlying pattern from the specific case.

```
[G5] FEATURES: [what features of this specific case are essential vs. accidental]
     ESSENTIAL: [features that MUST be present for the pattern to hold]
     ACCIDENTAL: [features specific to this case but not to the pattern]

[G6] MECHANISM: [the causal mechanism that makes this case work the way it does]

[G7] ABSTRACTED_PATTERN: [the specific case restated without domain-specific details]
```

### Abstraction Technique

1. **Name the actors generically**: "our team" → "a group with resource constraints"
2. **Name the mechanism**: "we ran out of money" → "resource depletion under uncertain timeline"
3. **Name the structure**: "they copied us" → "competitive imitation following observed success"
4. **Remove accidentals**: Strip details that could change without changing the outcome

---

## Phase 3: Generalization

State the general principle, pattern, or framework.

```
[G8] GENERAL_PRINCIPLE: [the principle stated in domain-independent terms]
[G9] APPLIES_WHEN: [conditions under which this principle holds]
[G10] BREAKS_WHEN: [conditions under which this principle fails — boundary conditions]
[G11] MECHANISM: [WHY this principle holds — the underlying causal structure]
```

### Generality Level Check

| Level | Description | Example | Useful? |
|-------|------------|---------|---------|
| **Too general** | True for everything | "Things can go wrong" | No — not actionable |
| **Right level** | True for a class of situations, actionable | "Resource-dependent projects with uncertain timelines need staged funding commitments" | Yes |
| **Too specific** | Only true for this case | "Your seed round should have been $2M not $1.5M" | Maybe — but not general |

---

## Phase 4: Transfer Test

Verify the generalization by applying it to different cases.

```
[G-N] TRANSFER_CASE:
     DOMAIN: [a different domain than the original]
     APPLICATION: [how the general principle applies here]
     FIT: [strong | partial | weak]
     INSIGHT: [what the principle reveals about this case]
     MODIFICATION_NEEDED: [any adjustments to the principle for this domain]
```

Generate 2-3 transfer cases. At least one should be from a VERY different domain to test true generality.

### Transfer Quality Rules

- If the principle transfers to 0 other cases → it's not general, it's specific
- If it transfers to everything → it's too general to be useful
- If it transfers to 2-3 cases with minor modifications → it's at the right level

---

## Phase 5: Output

```
GENERAL ANALYSIS
================

FROM SPECIFIC: [the original case, briefly]
GENERAL PRINCIPLE: [the principle derived]
MECHANISM: [why it holds]

APPLIES WHEN:
  - [condition 1]
  - [condition 2]

BREAKS WHEN:
  - [boundary condition 1]
  - [boundary condition 2]

TRANSFER CASES:
  1. [different domain] — [how it applies] — FIT: [level]
  2. [different domain] — [how it applies] — FIT: [level]

ACTIONABLE FORM: [the principle stated as a decision rule or heuristic]

FOR THE ORIGINAL CASE: [how the general principle applies back to the specific input]

READY FOR:
- /spcf — to apply this principle to a specific new case
- /ar — to explore what follows from the principle
- /aex — to test assumptions in the principle
- /platitude — to operationalize if the principle risks becoming vague
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Overfitting** | "General" principle only explains the original case | Apply the transfer test. If it doesn't transfer, it's not general |
| **Undergeneralized** | Principle is specific to domain when it shouldn't be | Strip domain-specific terms. Restate with generic actors and mechanisms |
| **Overgeneralized** | Principle is so broad it applies to everything | Add boundary conditions. Where does it break? |
| **No mechanism** | Principle stated without explaining WHY it holds | Identify the causal mechanism. Correlation isn't generalization |
| **No boundaries** | Principle stated without limits | Every general principle has boundary conditions. Find them |
| **Platitude output** | The "general principle" is a cliché | Apply the `/platitude` test — is it specific enough to disagree with? |
| **Transfer forcing** | Applied the principle to cases where it doesn't fit | Partial fit is fine. Forced fit is dishonest. Note where the transfer breaks |

---

## Depth Scaling

| Depth | Transfer Cases | Boundary Analysis | Mechanism Depth | Applications |
|-------|---------------|-------------------|----------------|-------------|
| 1x | 1 | Basic | Named | Original case only |
| 2x | 2-3 | Key boundaries | Explained | 2-3 applications |
| 4x | 4-5 | Full boundary map | Structural analysis | Multiple domains |
| 8x | 6+ | Full + exceptions catalog | Formal model | Comprehensive domain sweep |

Default: 2x. These are floors.

---

## Pre-Completion Checklist

- [ ] Specific case clearly stated as starting point
- [ ] Essential vs. accidental features separated
- [ ] Mechanism identified (not just correlation)
- [ ] General principle stated in domain-independent terms
- [ ] Boundary conditions specified (where it breaks)
- [ ] Transfer test passed (applies to at least 1 different domain)
- [ ] Generality level checked (not too general, not too specific)
- [ ] Actionable form provided (decision rule or heuristic)

---

## Integration

- Use from: learning from experience, finding patterns across cases, building mental models
- Routes to: `/spcf` (apply general insight to specific case), `/ar` (explore implications)
- Complementary: `/spcf` (general→specific is the natural pair)
- Differs from `/spcf`: spcf applies principles to specific cases; genl extracts principles from specific cases
- Differs from `/soph`: soph does deep structural analysis; genl abstracts to transferable principles
- Differs from `/lr`: lr researches a topic broadly; genl extracts principles from specific observations
