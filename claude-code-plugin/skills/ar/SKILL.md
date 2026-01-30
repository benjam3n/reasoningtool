---
name: ar
description: Assume Right - Deep recursive rightness search. For every claim, assume it's right — find what must follow, then assume THOSE implications are right too. Recurse until bedrock. Track every claim found.
---

# AR - Assume Right Search

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

1. **Right means fully right.** Not "right in some cases" — RIGHT. Push the implications as far as they go, especially when the conclusion is surprising.

2. **Explore before concluding.** AR has two phases: EXPLORATION (find all implications) and REGISTRY (compile what you found). Never conclude during exploration. Never introduce new claims during registry.

3. **Every claim gets tracked.** When you find an implication, that implication is itself a claim. Number it. It goes in the registry. Nothing gets lost in prose.

4. **Bedrock is not an opinion.** Bedrock means ONE of:
   - **Empirically testable**: You can check if this implication actually holds
   - **Logically necessary**: Follows from definitions or mathematics
   - **Direct observation**: Something you can directly see/measure
   - **Tension**: This implication contradicts something else you've established
   - "This seems like a good thing" is NOT bedrock. Keep recursing.

5. **AR is not cheerleading.** The goal isn't to validate — it's to find what you're COMMITTED to by accepting this claim. Every "yes" is also a "no" — find what gets foreclosed.

6. **Costs are implications too.** What you lose, what becomes impossible, what you must also accept — these are just as important as what opens up.

---

## Phase 1: EXPLORATION

### Step 1: State the Claim

```
CLAIM: [precise statement]
ASSUMING THIS IS: [True / Correct / The right approach / Necessary]
```

### Step 2: Find Implications (Recurse)

For the claim and every sub-claim found, ask: **If this is right, what must follow?**

Rules:
- Find at least 3 independent implications per node (at 4x+ depth)
- For each implication, ask: "If THIS is also right, what follows?" and recurse
- Number every claim as you go: R1, R2, R3...
- Stop recursing ONLY at bedrock (testable, logical, observable, or tension)
- Track what is FORECLOSED (no longer possible) at each node — these are implications too

Format each node as:

```
[R1] [CLAIM TEXT]
  If right, then:
  [R2] [implication — classify as Necessary/Probable/Possible]
    If right, then:
    [R3] [deeper implication]
      If right, then:
      [R4] [→ BEDROCK: testable/logical/observable/tension]
    [R5] [different deeper implication]
      ...
  [R6] FORECLOSED: [what becomes impossible if R1 is right]
    If this foreclosure holds:
    [R7] [consequence of foreclosure]
      ...
  [R8] [second independent implication]
    ...
  [R9] [third implication — the one nobody mentions]
    ...
```

**At each node, classify:**
- **Necessary**: MUST follow — no way around it
- **Probable**: Likely follows given reasonable assumptions
- **Possible**: Could follow under specific conditions (state them)
- **Foreclosed**: This option/belief is NO LONGER available

**Bedrock labels (the ONLY valid stopping points):**
- `BEDROCK-TEST: [specific experiment or measurement]`
- `BEDROCK-LOGIC: [logical/mathematical necessity]`
- `BEDROCK-OBSERVE: [directly observable fact]`
- `BEDROCK-TENSION: [contradicts established claim R-number]`

### Step 3: Find the Pattern

After ALL recursion is complete, look at the shape:
- **Expansive**: The claim opens up more and more possibilities — generative, high-leverage
- **Constraining**: The claim narrows options more and more — strong commitment, limited flexibility
- **Contradictory**: Following implications leads to a contradiction — the claim CANNOT be fully right
- **Convergent**: Multiple branches require the same thing — that's foundational

---

## Phase 2: CLAIM REGISTRY

After exploration is complete, compile EVERY claim found into a numbered list.

```
CLAIM REGISTRY
==============

[R1] [claim text] — TYPE: [implication/foreclosure/commitment/cost] — STRENGTH: [necessary/probable/possible]
[R2] [claim text] — TYPE: [...] — STRENGTH: [...]
...
[RN] [claim text] — TYPE: [...] — STRENGTH: [...]
```

**Type values:**
- **Implication**: Something that must/probably/possibly follows
- **Foreclosure**: Something that is no longer available
- **Commitment**: Something you must also believe or do
- **Cost**: Something you lose or must give up
- **Tension**: Contradicts another claim in the registry

**Rules for the registry:**
- Every R-numbered claim from Phase 1 appears here. No exceptions.
- Type and strength derived from the tree, not asserted.
- If a claim's strength is unclear, mark as Possible, not Necessary.

---

## Phase 3: SYNTHESIS

Derived entirely from the registry. No new claims introduced here.

```
ORIGINAL CLAIM: [X]

IMPLICATION PATTERN: [expansive / constraining / contradictory / convergent]

COMMITMENT CHAIN:
If X is right:
→ you must accept: [R-numbers of Necessary implications]
→ you probably accept: [R-numbers of Probable implications]
→ you can no longer: [R-numbers of Foreclosures]
→ you lose: [R-numbers of Costs]

WHAT THE RIGHTNESS ANALYSIS ACTUALLY FOUND:
[Numbered list of every substantive finding, referencing R-numbers]
1. [finding, from R2→R4]
2. [finding, from R6→R7]
3. ...

TENSIONS / CONTRADICTIONS:
[Any R-numbers that contradict each other. If none found, say so.]

WEAKEST LINKS:
[Which implications in the chain are Possible rather than Necessary?
 These are where the chain might break. Reference R-numbers.]

TESTABLE PREDICTIONS:
- [prediction derived from specific R-numbers]
- [prediction derived from specific R-numbers]

UNRESOLVED:
- [implications that stayed Possible — what would confirm or deny them]
```

---

## Depth Scaling

| Depth | Min Tree Levels | Min Implications per Node | Min Total Claims |
|-------|----------------|--------------------------|-----------------|
| 1x | 3 | 2 | 8 |
| 2x | 4 | 2 | 15 |
| 4x | 5 | 3 | 25 |
| 8x | 7 | 3 | 45 |
| 16x | 9 | 4 | 75 |
| 32x | 11 | 4 | 120 |

Default: 2x. These are floors.

---

## Anti-Cheerleading Checks

| Failure Mode | Signal | Fix |
|-------------|--------|-----|
| **Validation parade** | Every implication is positive | Find the foreclosures and costs. What do you LOSE? |
| **Shallow rightness** | "It works, and that's good" | Push deeper. WHY does it work? What does that commit you to? |
| **Missing foreclosures** | Only listing what opens up | Every "yes" is also a "no." Find what closes. |
| **Opinion bedrock** | Labeling "this is good" as bedrock | Not bedrock. Keep recursing until testable/logical/observable. |
| **Cherry-picked synthesis** | Synthesis mentions 3 findings but tree had 15 | Registry must include ALL claims. Synthesis references them. |
| **Narrative tree** | Tree reads as paragraphs with indent | Use numbered claims. Every node gets an R-number. |

---

## Pre-Completion Check

- [ ] Depth floors met (levels, implications per node, total claims)
- [ ] Every branch reaches bedrock (testable/logical/observable/tension)
- [ ] ALL claims from Phase 1 appear in registry (none dropped)
- [ ] Foreclosures and costs explicitly identified (not just positives)
- [ ] Synthesis introduces NO new claims — only references R-numbers
- [ ] At least one uncomfortable commitment found
- [ ] Weakest links identified with R-numbers
- [ ] **Cheerleading check**: If every finding is positive, you missed the costs. Go back.
- [ ] Testable predictions reference specific R-numbers
