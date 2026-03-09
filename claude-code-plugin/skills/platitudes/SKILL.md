---
name: "platitudes - Platitude Set Analyzer"
description: "Analyze multiple platitudes as a system, detect contradictions, reconcile conflicts by identifying context conditions, and convert the set into a coherent, actionable policy."
---

# Platitudes - Platitude Set Analyzer

**Input**: $ARGUMENTS

---

## Core Principles

1. **Platitude sets always contain contradictions.** Any collection of conventional wisdom will include pairs that directly oppose each other — "look before you leap" and "he who hesitates is lost." These aren't errors. They're signals that context determines which applies.

2. **Contradictions are information.** When two platitudes conflict, the conflict itself tells you something: there's a decision boundary between their domains of applicability. Finding that boundary is more valuable than either platitude alone.

3. **Sets reveal what individuals hide.** A single platitude can seem universally true. Put it next to three others in the same domain and the boundaries, biases, and blind spots become visible. Analysis at the set level reveals the worldview encoded in the collection.

4. **A coherent policy requires prioritization.** When two valid-in-context platitudes both apply to the same situation, one must take precedence. The policy must specify which wins and why, not just list them all.

5. **The gaps in the set matter.** What the platitude collection DOESN'T address is as revealing as what it does. If a set of management platitudes never mentions failure recovery, that's a blind spot in the worldview the set encodes.

---

## Phase 1: Set Inventory

```
[S1] PLATITUDE_SET: [list all platitudes provided or extracted from context]
[S2] SOURCE: [where the set comes from — a culture, a company, a person, a book, a domain]
[S3] SET_SIZE: [N platitudes]
[S4] DOMAIN: [what area these platitudes address — if mixed, note the spread]
```

For each platitude:
```
[S-N] PLATITUDE: [quoted]
  KERNEL: [the genuine insight — one sentence]
  DOMAIN: [where it applies]
  IMPLICIT_VALUE: [what value or priority it encodes — e.g., speed, caution, simplicity]
```

---

## Phase 2: Contradiction Detection

Compare every platitude against every other for conflicts:

```
[S-N] CONFLICT:
  A: [platitude 1]
  B: [platitude 2]
  NATURE: [direct opposition | partial tension | scope overlap | priority conflict]
  WHAT_CONFLICTS: [specifically what is contradicted]
```

### Conflict Types

| Type | Definition | Example |
|------|-----------|---------|
| **Direct opposition** | They literally recommend opposite actions | "Move fast" vs "Measure twice" |
| **Partial tension** | Mostly compatible but clash at edges | "Trust your team" vs "Verify everything" |
| **Scope overlap** | Both claim the same territory with different advice | "Focus on one thing" vs "Diversify" |
| **Priority conflict** | Both valid but can't both be #1 priority | "Quality first" vs "Ship fast" |

### Agreement Detection

Also identify reinforcing pairs:
```
[S-N] REINFORCEMENT:
  A: [platitude 1]
  B: [platitude 2]
  SHARED_VALUE: [what they both promote]
  COMBINED_BIAS: [what bias the reinforcement creates]
```

---

## Phase 3: Reconciliation

For each conflict, find the context boundary:

```
[S-N] RECONCILIATION:
  CONFLICT: [ref]
  USE_A_WHEN: [specific conditions where platitude A applies]
  USE_B_WHEN: [specific conditions where platitude B applies]
  DECISION_VARIABLE: [what changes between the two contexts — urgency, reversibility, stakes, etc.]
  BOUNDARY: [the specific threshold where you switch from A to B]
```

### Reconciliation Strategies

| Strategy | When to Use |
|----------|------------|
| **Context split** | Each applies in different, identifiable situations |
| **Temporal split** | One applies early, the other later in a process |
| **Scale split** | One for small scope, the other for large scope |
| **Phase split** | One for exploration, one for execution |
| **Stakes split** | One for reversible decisions, one for irreversible |

---

## Phase 4: Gap Analysis

```
[S-N] GAP: [what the set doesn't address]
  EXPECTED: [why you'd expect this topic to be covered]
  RISK: [what could go wrong because of this gap]
  FILL_WITH: [what principle or platitude would cover the gap]
```

```
[S-N] BIAS: [systematic bias across the set]
  DIRECTION: [what the set over-emphasizes]
  NEGLECTS: [what it under-emphasizes]
  CONSEQUENCE: [what decisions this bias would distort]
```

---

## Phase 5: Policy Synthesis

Convert the analyzed set into a coherent, ordered action policy:

```
[S-N] POLICY_RULE: [actionable rule derived from reconciled platitudes]
  PRIORITY: [1-N — order matters]
  SOURCE_PLATITUDES: [which platitudes contribute to this rule]
  APPLIES_WHEN: [conditions]
  OVERRIDES: [which other rules this takes precedence over, and when]
```

---

## Phase 6: Output

```
PLATITUDE SET ANALYSIS
======================

SET: [N platitudes from source]
DOMAIN: [domain]

INVENTORY:
  1. [platitude] — KERNEL: [insight] — VALUE: [encoded priority]
  2. [platitude] — KERNEL: [insight] — VALUE: [encoded priority]
  ...

CONTRADICTIONS FOUND: [N]
  1. [A] vs [B]
     USE A WHEN: [condition]
     USE B WHEN: [condition]
     SWITCH ON: [decision variable]

  2. [A] vs [B]
     ...

REINFORCEMENTS: [N]
  1. [A] + [B] → COMBINED BIAS: [what they over-emphasize together]

GAPS:
  1. [missing topic] — RISK: [consequence]

COHERENT POLICY (priority-ordered):
  1. [rule] — WHEN: [conditions]
  2. [rule] — WHEN: [conditions]
  3. [rule] — WHEN: [conditions]
  OVERRIDE RULES: [which takes precedence in conflict]

WORLDVIEW ENCODED: [one-sentence summary of the implicit worldview this set represents]

READY FOR:
- /platitude [specific] — to deep-dive one platitude from the set
- /aex — to test assumptions embedded in the policy
- /cmp [rule A] vs [rule B] — to compare competing policy rules
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **No contradictions found** | Set of 5+ platitudes with zero conflicts | Every substantial set has contradictions. Look harder at edge cases |
| **Contradictions without reconciliation** | Conflicts identified but no context boundaries given | Each conflict must specify WHEN to use each side |
| **Flat policy** | All rules at same priority, no override logic | A real policy has precedence. Force-rank and specify overrides |
| **Gaps ignored** | Only analyzes what's present, not what's missing | Gaps are as informative as contradictions. Check for blind spots |
| **Individual analysis only** | Each platitude analyzed alone, no cross-comparison | The value of this skill IS the cross-comparison. If no conflicts or reinforcements found, the analysis is incomplete |
| **Synonym grouping missed** | Treating rewordings as separate platitudes | "Work smart not hard" and "Efficiency over effort" are the same insight |
| **Policy too abstract** | Synthesized rules are themselves platitudes | Policy rules must be more specific than the platitudes they derive from |

---

## Depth Scaling

| Depth | Min Conflicts | Gap Analysis | Policy Rules | Worldview |
|-------|--------------|-------------|-------------|-----------|
| 1x | All direct | No | 3 | No |
| 2x | All direct + partial | Basic | 5 | One sentence |
| 4x | All types | Full with risks | 7 | Full analysis |
| 8x | All + second-order | Full + missing platitudes | Complete | Full + domain comparison |

Default: 2x. These are floors.

---

## Pre-Completion Checklist

- [ ] All platitudes inventoried with kernels and encoded values
- [ ] Every pair checked for contradiction
- [ ] Contradictions reconciled with specific context boundaries
- [ ] Reinforcements identified with combined bias noted
- [ ] Gaps in the set identified
- [ ] Coherent policy synthesized with priority ordering
- [ ] Override rules specified for remaining conflicts
- [ ] Policy rules are more specific than source platitudes

---

## Integration

- Use from: analyzing advice collections, company values, cultural wisdom, book takeaways
- Routes to: `/platitude` (deep-dive one), `/aex` (test assumptions), `/cmp` (compare rules)
- Complementary: `/platitude` (set analysis → individual deep-dives)
- Differs from `/platitude`: platitude operationalizes ONE; platitudes analyzes the SET for contradictions and coherence
- Differs from `/cmp`: cmp compares two options; platitudes analyzes N items as an interacting system
- Differs from `/mv`: mv validates list structure; platitudes analyzes semantic content and contradictions
