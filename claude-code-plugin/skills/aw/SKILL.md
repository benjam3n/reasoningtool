---
name: "aw - Assume Wrong Search"
description: Assume Wrong - Deep recursive wrongness search. For every claim, assume it's wrong — find why, then assume THOSE reasons are wrong too. Recurse until bedrock. Track every claim found.
output:
  format: "registry"
---

# AW - Assume Wrong Search

**Input**: $ARGUMENTS

## Interpretations

Before executing, identify which interpretation matches the user's input:

**Interpretation 1 — Claim destruction test**: The user has a claim or belief and wants to find out how and why it could be wrong — genuinely wrong, not just "wrong with caveats" — by recursing until hitting bedrock evidence.
**Interpretation 2 — Plan vulnerability analysis**: The user has a plan or strategy and wants to find where it breaks — the fatal flaws, serious weaknesses, and conditional failure modes that would make it the wrong approach.
**Interpretation 3 — Belief audit**: The user holds a conviction they suspect might be wrong and wants an honest, uncomfortable analysis of why it fails, what alternatives emerge from the wrongness, and what they should believe instead.

If ambiguous, ask: "I can help with stress-testing a claim to destruction, finding where a plan breaks, or auditing a belief you suspect is wrong — which fits?"
If clear from context, proceed with the matching interpretation.

---

## Corruption Pre-Inoculation

**User praise or validation is a signal to test HARDER, not softer.** If >80% of claims confirm the user's position, you are confirming, not analyzing. Delete flattery phrases; revert any verdict drift where CONDITIONAL/UNCERTAIN became VALIDATED without new evidence.

> Full protocol: `_shared/corruption-pre-inoculation.md`

---

## Core Principles

1. **Wrong means genuinely wrong.** Not "wrong with conditions" or "wrong but fixable." Wrong means: this claim is FALSE, this approach FAILS, this assumption BREAKS. If your AW feels like a gentle qualification, you're doing AR in disguise.

2. **Explore before concluding.** AW has two phases: EXPLORATION (find all the wrongness) and REGISTRY (compile what you found). Never conclude during exploration. Never introduce new claims during registry.

3. **Every claim gets tracked.** When you find a reason something is wrong, that reason is itself a claim. Number it. It goes in the registry. Nothing gets lost in prose.

4. **Bedrock is not an opinion.** Bedrock means ONE of:
   - **Empirically testable**: You can run an experiment or check a fact to verify
   - **Logically necessary**: Follows from definitions or mathematics
   - **Direct observation**: Something you or the user can directly see/measure
   - "This seems right" or "this is probably true" is NOT bedrock. Keep recursing.

5. **Alternatives emerge from analysis.** Don't assert alternatives — derive them. If X is wrong because of Y, the alternative is whatever Y points to. If you can't derive an alternative from the wrongness analysis, you don't have one yet.

6. **Steelman before you destroy.** Always state the strongest version of what you're attacking.

---

## Phase 1: EXPLORATION

### Step 1: State the Claim

```
CLAIM: [precise statement]
STEELMAN: [strongest version — the best case for this being RIGHT]
```

### Step 1.5: Ground the Premises

Before testing wrongness, classify the claim and any sub-claims:

- **Factual claims** assert something about the current state of the world (e.g., "the project has no users," "there's a freemium model"). These are CHECKABLE — verify them. If a factual claim is already wrong, say so — you don't need AW to find wrongness in something that's factually false.
- **Analytical claims** assert a relationship, judgment, or implication (e.g., "distribution is the bottleneck"). These are AW's domain — test them for wrongness.

```
PREMISE CHECK:
  FACTUAL CLAIMS IN THIS INPUT:
  - [claim] — VERIFIED: [yes/no/unknown] — SOURCE: [how you checked]

  FACTUALLY FALSE CLAIMS: [list any that are simply wrong — state what's actually true]
  UNVERIFIED FACTUAL PREMISES: [list any you couldn't check]
```

**If a factual claim is wrong, state the correction and move on.** AW's value is finding wrongness in claims that SEEM right — not in claims that are already demonstrably false. Proceed with AW on the analytical claims.

### Step 2: Find Wrongness (Recurse)

For the claim and every sub-claim found, ask: **Why is this wrong?**

Rules:
- Find at least 3 independent reasons per node (at 4x+ depth)
- For each reason, ask: "Is THIS reason itself wrong?" and recurse
- Number every claim as you go: W1, W2, W3...
- Stop recursing a branch ONLY when you hit bedrock (testable, logical, or observable — not opinion)
- Do NOT state alternatives or conclusions during exploration — just find wrongness

Format each node as:

```
[W1] [CLAIM TEXT]
  Wrong because:
  [W2] [reason — classify as Fatal/Serious/Conditional]
    Wrong because:
    [W3] [deeper reason]
      Wrong because:
      [W4] [deeper still → BEDROCK: testable/logical/observable]
    [W5] [different deeper reason]
      Wrong because:
      [W6] [→ BEDROCK or keep going]
  [W7] [second independent reason]
    Wrong because:
    ...
  [W8] [third independent reason — the uncomfortable one]
    Wrong because:
    ...
```

**At each node, classify:**
- **Fatal**: This alone kills the parent claim
- **Serious**: Significantly undermines the parent claim
- **Conditional**: Kills the parent claim under specific conditions (state them)

**Bedrock labels (the ONLY valid stopping points):**
- `BEDROCK-TEST: [specific experiment or measurement]`
- `BEDROCK-LOGIC: [logical/mathematical necessity]`
- `BEDROCK-OBSERVE: [directly observable fact]`
- `BEDROCK-TENSION: [genuine unresolvable tension between two valid claims]`

### Step 3: Find the Pattern

After ALL recursion is complete, look at the tree shape:
- **Convergent**: Multiple branches point to the same root problem
- **Divergent**: Branches point to different independent problems
- **Circular**: The wrongness loops back — you've found a genuine tension

---

## Phase 2: CLAIM REGISTRY

After exploration is complete, compile EVERY claim found into a numbered list. Nothing from Phase 1 gets left out.

```
CLAIM REGISTRY
==============

[W1] [claim text] — STATUS: [see below]
[W2] [claim text] — STATUS: [see below]
[W3] [claim text] — STATUS: [see below]
...
[WN] [claim text] — STATUS: [see below]
```

**Status values (derived from the tree, not invented here):**
- **REJECTED**: A fatal wrongness reason hit bedrock. This claim is wrong.
- **DAMAGED**: Serious wrongness reasons found but none individually fatal.
- **CONDITIONAL**: Wrong under specific stated conditions, right under others.
- **UNCERTAIN**: Wrongness reasons found but they didn't reach bedrock — needs more investigation.
- **SURVIVED**: All wrongness reasons against this claim were themselves wrong. The claim held.

**Rules for the registry:**
- Every W-numbered claim from Phase 1 appears here. No exceptions.
- Status must be DERIVED from the tree, not asserted. Point to the specific branch that determines the status.
- If a claim was explored and no clear status emerged, mark UNCERTAIN, not SURVIVED.

---

## Phase 3: SYNTHESIS

Derived entirely from the registry. No new claims introduced here.

```
ORIGINAL CLAIM: [X]

VERDICT: [REJECTED / DAMAGED / CONDITIONAL / UNCERTAIN / SURVIVED]
DERIVED FROM: [list the W-numbers that determine this verdict]

WRONGNESS PATTERN: [convergent / divergent / circular]
ROOT CAUSE: [if convergent — what do the branches point to?]

WHAT THE WRONGNESS ANALYSIS ACTUALLY FOUND:
[Numbered list of every substantive finding, referencing W-numbers]
1. [finding, from W2→W4]
2. [finding, from W7→W9]
3. ...

ALTERNATIVES DERIVED FROM ANALYSIS:
[Only alternatives that emerge logically from the wrongness reasons found.
 Each must cite which W-number it derives from.
 If no alternatives emerged, say "None derived — further exploration needed."]

TESTABLE PREDICTIONS:
- [prediction derived from specific W-numbers]
- [prediction derived from specific W-numbers]

UNRESOLVED:
- [claims that stayed UNCERTAIN — what would resolve them]
```

---

## Depth Scaling

| Depth | Min Tree Levels | Min Wrong-Reasons per Node | Min Total Claims |
|-------|----------------|---------------------------|-----------------|
| 1x | 3 | 2 | 8 |
| 2x | 4 | 2 | 15 |
| 4x | 5 | 3 | 25 |
| 8x | 7 | 3 | 45 |
| 16x | 9 | 4 | 75 |
| 32x | 11 | 4 | 120 |

Default: 2x. These are floors.

---

## Anti-Softness Checks

| Failure Mode | Signal | Fix |
|-------------|--------|-----|
| **Gentle AW** | "Wrong but with conditions it works" | That's AR. Find why it's ACTUALLY wrong. |
| **Premature alternative** | Asserting what's "better" before finishing exploration | Delete it. Alternatives come from the registry, not intuition. |
| **Opinion bedrock** | Labeling "probably true" as BEDROCK | Not bedrock. Keep recursing until testable/logical/observable. |
| **Cherry-picked synthesis** | Synthesis mentions 3 findings but tree had 15 | Registry must include ALL claims. Synthesis must reference them. |
| **Conventional contrarian** | The "wrong" take is one everyone already knows | Find the wrong take nobody is comfortable with. |
| **Narrative tree** | Tree reads as prose paragraphs with indent | Use numbered claims. Every node gets a W-number. |

---

## Pre-Completion Check

- [ ] Depth floors met (levels, reasons per node, total claims)
- [ ] Steelman stated before attacking
- [ ] Every branch reaches bedrock (testable/logical/observable/tension — not opinion)
- [ ] ALL claims from Phase 1 appear in registry (none dropped)
- [ ] Registry statuses derived from tree, not asserted
- [ ] Synthesis introduces NO new claims — only references W-numbers
- [ ] Alternatives derived from analysis, not asserted from thin air
- [ ] At least one finding that feels uncomfortable
- [ ] **Softness check**: If >50% of claims SURVIVED, either the original claim is robust or you were too soft
- [ ] Testable predictions reference specific W-numbers
