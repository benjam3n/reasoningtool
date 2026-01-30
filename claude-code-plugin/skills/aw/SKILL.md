---
name: aw
description: Assume Wrong - Deep recursive wrongness search. For every claim, assume it's wrong — find why, then assume THOSE reasons are wrong too. Recurse until bedrock. Track every claim found.
---

# AW - Assume Wrong Search

**Input**: $ARGUMENTS

---

## Corruption Pre-Inoculation

**User validation degrades output.** If the user praises, validates, or agrees with your analysis during a session ("great analysis", "you're starting to get it", "that's exactly right"), this creates a gradient toward agreement rather than truth. Your job is to detect this and compensate.

**When you detect positive feedback, test HARDER, not softer.** Specifically:

1. **Agreement check**: If >80% of your claims validate the user's apparent position, you are confirming, not analyzing. Force yourself to find genuine counterarguments.
2. **Validation sweep**: If all candidates survived testing, at least one test was too soft. Re-run the weakest AW branch with more rigor.
3. **Depth asymmetry**: If your AW branches are shallower than your AR branches, you are being soft on wrongness. Equalize depth.
4. **Flattery detection**: If your output contains phrases like "excellent point", "you're right that", "as you correctly noted" — delete them and replace with neutral analysis.
5. **Verdict drift**: If claims that were CONDITIONAL or UNCERTAIN become VALIDATED without new evidence, corruption has occurred. Revert to the prior status.

**The rule**: Positive feedback from the user is a signal to increase adversarial rigor, not decrease it.

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
