---
name: "platitude - Operationalize a Platitude"
description: "Convert a single platitude into concrete, testable actions, boundary conditions, and failure modes — transforming vague wisdom into executable guidance."
output:
  format: "prose"
---

# Platitude - Operationalize a Platitude

**Input**: $ARGUMENTS

---

## Core Principles

1. **Platitudes are compressed wisdom with the specifics removed.** "Move fast and break things" once meant something precise in a specific context. By the time it became a platitude, the context was stripped and the actionability was lost. This skill restores what was removed.

2. **A platitude that can't be wrong can't be useful.** "Quality matters" is unfalsifiable and therefore provides zero guidance. The operationalized version must be specific enough that someone could disagree with it or violate it. If the output is also unfalsifiable, the skill has failed.

3. **Every platitude has a boundary where it reverses.** "Move fast" is good advice until speed causes irreversible damage. "Be patient" is good advice until patience becomes avoidance. The boundary condition — where the platitude stops being true — is more useful than the platitude itself.

4. **Platitudes survive because they're partially true.** They wouldn't propagate if they were entirely wrong. The skill must identify WHAT is true about the platitude before identifying where it fails. Dismissing platitudes entirely is as lazy as accepting them uncritically.

5. **Operationalization means decision-changing.** The output must change at least one decision the user would make. If someone reads the operationalized version and acts exactly as they would have without it, the operationalization failed.

---

## Phase 1: Platitude Extraction

```
[P1] PLATITUDE: [the platitude, quoted exactly]
[P2] DOMAIN: [where this platitude is commonly invoked — business, relationships, self-help, engineering, etc.]
[P3] SURFACE_MEANING: [what someone would understand on first hearing]
[P4] EMOTIONAL_APPEAL: [why this feels true — what psychological need it satisfies]
```

---

## Phase 2: Historical Reconstruction

Trace the platitude back to useful specifics:

```
[P5] ORIGINAL_CONTEXT: [if known — where this wisdom originated and what it specifically meant]
[P6] WHAT_WAS_STRIPPED: [what specific information was lost as it became a platitude]
[P7] KERNEL_OF_TRUTH: [the genuinely useful insight buried in the platitude]
[P8] KERNEL_SCOPE: [under what specific conditions the kernel is actually true]
```

---

## Phase 3: Operationalization

Convert the platitude into concrete, testable guidance:

### Action Rules

```
[P-N] ACTION_RULE: [specific, executable rule derived from the platitude]
  WHEN: [specific conditions under which this rule applies]
  HOW: [concrete behavior — what someone would observably DO]
  TEST: [how you'd know if someone is following this rule or not]
  EXAMPLE: [concrete scenario where this rule changes a decision]
```

Generate 3-5 action rules. Each must be:
- **Specific enough to disagree with** — someone could argue the opposite
- **Observable** — you could tell if someone is doing it or not
- **Decision-changing** — it would alter at least one choice

### Metrics (if applicable)

```
[P-N] METRIC: [how you'd measure adherence to the operationalized version]
  GOOD: [what the metric looks like when the platitude is being followed well]
  BAD: [what the metric looks like when it's being followed poorly or not at all]
```

---

## Phase 4: Boundary Analysis

Where does this platitude stop being true?

```
[P-N] BOUNDARY: [condition where the platitude reverses or fails]
  TRIGGER: [what specific situation activates this boundary]
  REVERSAL: [what you should do INSTEAD past this boundary]
  SIGNAL: [how you'd know you've crossed the boundary]
```

### Counter-Platitude Test

```
[P-N] OPPOSITE: [the opposite platitude — there almost always is one]
  ALSO_TRUE: [yes/no — is the opposite platitude also partially true?]
  RECONCILIATION: [how to hold both — usually the answer is "different conditions"]
  WHEN_ORIGINAL: [conditions favoring the original platitude]
  WHEN_OPPOSITE: [conditions favoring the opposite]
```

Example: "Move fast and break things" ↔ "Measure twice, cut once." Both true — under different conditions.

---

## Phase 5: Output

```
OPERATIONALIZED PLATITUDE
=========================

PLATITUDE: [quoted]
KERNEL OF TRUTH: [what's genuinely useful about it]

ACTION RULES:
  1. WHEN [condition]: [do this specific thing]
     TEST: [how to verify]
  2. WHEN [condition]: [do this specific thing]
     TEST: [how to verify]
  3. WHEN [condition]: [do this specific thing]
     TEST: [how to verify]

BOUNDARIES (stop following this when):
  1. [boundary] — INSTEAD: [what to do]
  2. [boundary] — INSTEAD: [what to do]

COUNTER-PLATITUDE: [the opposite wisdom]
  USE ORIGINAL WHEN: [conditions]
  USE OPPOSITE WHEN: [conditions]

DECISION TEST: Before this analysis, you'd [old behavior]. After, you'd [new behavior] because [reason].

READY FOR:
- /platitudes — to analyze a set of platitudes together
- /aex — to test assumptions embedded in the platitude
- /ar [action rule] — to explore what follows if a specific rule is right
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Still vague** | Operationalized version is also unfalsifiable | Apply the disagreement test: could someone argue the opposite? |
| **Kernel dismissed** | Platitude treated as entirely worthless | Find what's true first, then find the limits |
| **No boundaries** | Platitude treated as universally true | Find the counter-platitude. Every platitude has one |
| **Academic** | Operationalization is correct but doesn't change any decisions | Each action rule must alter at least one real choice |
| **Over-literal** | Taking the metaphor at face value instead of extracting the principle | "Break things" isn't about destruction — extract the underlying principle |
| **Context-free** | No domain or situation specified | Platitudes mean different things in different domains. Specify where |
| **All action, no test** | Rules provided without verification criteria | Every rule needs an observable test for compliance |

---

## Depth Scaling

| Depth | Action Rules | Boundaries | Counter-Platitude | Historical Context |
|-------|-------------|-----------|-------------------|-------------------|
| 1x | 3 | 1 | Identified | No |
| 2x | 4 | 2 | Identified + reconciled | Brief |
| 4x | 5 | 3 | Full analysis | Traced |
| 8x | 6+ | 4+ | Full + domain variants | Full reconstruction |

Default: 2x. These are floors.

---

## Pre-Completion Checklist

- [ ] Platitude quoted exactly
- [ ] Kernel of truth identified (not dismissed)
- [ ] Action rules are specific enough to disagree with
- [ ] Each action rule has an observable test
- [ ] Boundaries identified where platitude reverses
- [ ] Counter-platitude found and reconciled
- [ ] Output would change at least one real decision
- [ ] Domain context specified

---

## Integration

- Use from: encountering vague advice, testing conventional wisdom, making aphorisms actionable
- Routes to: `/platitudes` (analyze a set), `/aex` (test embedded assumptions), `/ar` (explore action rules)
- Complementary: `/aex` (assumptions embedded in platitudes need testing)
- Differs from `/platitudes`: platitude handles ONE platitude deeply; platitudes analyzes a SET for patterns
- Differs from `/aex`: aex tests assumptions generally; platitude specifically converts wisdom into action
- Differs from `/claim`: claim tests truth value; platitude converts to actionable guidance regardless of truth
