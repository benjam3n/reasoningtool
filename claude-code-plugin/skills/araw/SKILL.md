---
name: araw
description: Assume Right / Assume Wrong search - For every claim, explore what follows if true (AR) and what breaks if false (AW). Number every finding. Recurse until bedrock. Compile a complete registry. Derive synthesis only from the registry.
---

# ARAW - Assume Right / Assume Wrong Search

**Input**: $ARGUMENTS

---

## Core Principles

These govern everything. When procedure conflicts with principle, follow the principle.

1. **Derivation, not enumeration.** Let structure emerge from exploration. Follow surprising branches deeper. If you're checking boxes instead of following curiosity, stop and explore.

2. **No early termination.** When depth is specified (8x, 16x), meet the depth floors. These are minimums, not targets to pad toward.

3. **Both sides, equal rigor.** AR and AW get the same depth of exploration. The goal is understanding, not confirmation. If you find yourself validating everything, you are confirming, not exploring.

4. **AW must be genuinely adversarial.** The biggest failure mode is soft AW -- "well, with conditions it works." That's not AW, that's AR wearing a hat. Real AW finds reasons the claim is WRONG, alternatives that are BETTER, and conditions where the claim FAILS. If your AW doesn't make the claim uncomfortable, dig harder.

5. **Depth means tree depth, not breadth.** A session with 18 claims but 2-level trees has failed. Depth means following chains of implication 5-8 levels deep.

6. **Every finding gets tracked.** When you find an implication, a reason something is wrong, a foreclosure, or an alternative -- number it. It goes in the registry. Nothing gets lost in prose.

7. **Bedrock is not an opinion.** Bedrock means ONE of:
   - **BEDROCK-TEST**: Empirically testable -- you can run an experiment or check a fact
   - **BEDROCK-LOGIC**: Logically necessary -- follows from definitions or mathematics
   - **BEDROCK-OBSERVE**: Directly observable -- something you can directly see/measure
   - **BEDROCK-TENSION**: Contradicts another established claim in this analysis
   - "This seems right" or "probably true" is NOT bedrock. Keep recursing.

8. **Rejection is a valid and expected outcome.** If a session validates every candidate, something is wrong. Expect 20-40% of claims to be REJECTED or genuinely UNCERTAIN. If you're not rejecting anything, you're generating only safe candidates or testing them too softly.

9. **Alternatives are DERIVED, not asserted.** Don't pull alternatives from thin air. If X is wrong because of Y, the alternative is whatever Y points to. If you can't derive an alternative from the wrongness analysis, you don't have one yet.

10. **Three phases, strict separation.** Phase 1 explores (no conclusions). Phase 2 compiles (no new findings). Phase 3 synthesizes (only from the registry). Never mix phases.

---

## Quick Mode: ARAW-Lite

For low-stakes, reversible, time-sensitive decisions:

```
CLAIM: [Most important claim]
ASSUME RIGHT: What becomes possible? [2-3 sentences]
ASSUME WRONG: Best alternative? Risk? [2-3 sentences]
VERDICT: [PROCEED / RECONSIDER / NEED MORE INFO]
ACTION: [One specific next step]
```

Not saved. For quick decisions only.

---

## Step 0: Meta-ARAW (Strategy Selection)

~50 lines max. Optional for 1-2x, required for 4x+.

1. **Restate the question** -- ensure you understand the input
2. **Check evaluability** -- is this a testable claim, or a decision/request that needs claim extraction?
3. **Identify uncertainty type** -- epistemic (learn more), aleatoric (hedge), model (reframe)
4. **Discover dimensions** -- quick universalization to find what to ARAW:
   - What states could this be in? (state space)
   - What is this an instance of? (category)
   - What parameters could vary? (variation)
   - Whose view is this? (perspective)
5. **Check for pitfalls** -- fish in dreams (expecting specific answer), red herring (explanation matches what you're explaining), smokescreen (confusion when approaching)

### Claim Evaluability

ARAW operates on claims (true/false). If the input is a decision, request, or conclusion, extract the underlying claims first:

"I need to quit my job" -> Claims: a problem exists, the job causes it, quitting fixes it, alternatives don't exist, what comes after is better. ARAW those.

---

## Step 1: Identify and Unbundle Claims

Parse input into claims. For each:
- State precisely
- Note type: explicit / implicit / bundled / presupposed / meta
- Rate VOI: how much would knowing this change action?

Number every claim: **C1, C2, C3...**

```
[C1] [claim text] -- TYPE: explicit -- VOI: high
[C2] [claim text] -- TYPE: implicit -- VOI: medium
[C3] [claim text] -- TYPE: bundled -- VOI: high
[C4] [claim text] -- TYPE: presupposed -- VOI: low
[C5] [claim text] -- TYPE: meta -- VOI: medium
```

**ARAW high-VOI claims first.** They determine the most.

### Unbundling

Single statements often contain multiple claims. "I need to quit my job" bundles at least 5. Find them all. Each gets its own C-number.

### Blind Spot Check

After identifying claims: what would someone from a different perspective, domain, time horizon, or scale notice that you didn't? Add those as additional C-numbered claims.

---

## Phase 1: EXPLORATION (Step 2)

### ARAW Each Claim

For each high-VOI claim, build a numbered tree. **Every AR produces sub-claims that need AW. Every AW produces alternatives that need AR.** Recurse.

Number every finding as you go: **F1, F2, F3...** (findings are distinct from claims -- claims are what you're testing, findings are what you discover).

```
[C1] "[claim text]"
  ASSUME RIGHT:
  [F1] If right: [implication] -- Necessary/Probable/Possible
    [F2] If F1 right: [deeper implication]
      [F3] If F2 right: [-> BEDROCK-TEST: specific test]
    [F4] If F1 right: [different implication]
      [F5] [-> BEDROCK-OBSERVE: observable fact]
  [F6] FORECLOSED if C1 right: [what becomes impossible]
    [F7] Consequence of F6: [what follows from that foreclosure]

  ASSUME WRONG:
  [F8] Wrong because: [reason] -- Fatal/Serious/Conditional
    [F9] If F8 holds: [deeper reason]
      [F10] [-> BEDROCK-TEST: specific test]
    [F11] Alternative derived from F8: [what F8 points toward]
      [F12] If F11 right: [implication of the alternative]
  [F13] Wrong because: [second independent reason] -- Fatal/Serious/Conditional
    ...
  [F14] Wrong because: [the uncomfortable reason] -- Fatal/Serious/Conditional
    ...
```

### Classification Labels

**AR implications:**
- **Necessary**: MUST follow -- no way around it
- **Probable**: Likely follows given reasonable assumptions
- **Possible**: Could follow under specific conditions (state them)
- **Foreclosed**: This option/belief is NO LONGER available if the claim is right

**AW reasons:**
- **Fatal**: This alone kills the claim
- **Serious**: Significantly undermines the claim
- **Conditional**: Kills the claim under specific conditions (state them)

**Bedrock labels (the ONLY valid stopping points):**
- `BEDROCK-TEST: [specific experiment or measurement]`
- `BEDROCK-LOGIC: [logical/mathematical necessity]`
- `BEDROCK-OBSERVE: [directly observable fact]`
- `BEDROCK-TENSION: [contradicts established finding F-number]`

### Multi-Valued AW

"Wrong" has multiple values. Don't just negate -- expand the state space:

```
Binary AW (limited): "NOT X"
Multi-valued AW (complete):
[F15] Alternative Y -- derived from [F-number reason]
[F16] Alternative Z -- derived from [F-number reason]
[F17] Hybrid X+Y -- derived from [F-number reason]
[F18] Reframe: wrong question entirely -- derived from [F-number reason]
[F19] X but modified -- derived from [F-number reason]
```

Every alternative MUST cite which wrongness finding it derives from.

### AW by Claim Type

| Claim Type | AW Approach | Example |
|------------|-------------|---------|
| **Factual** | Binary (true/false) | "The API is slow" -> Is it? Measure. |
| **Strategic** | State space (alternatives) | "Use microservices" -> What other architectures? |
| **Design** | State space (options) | "Add dark mode" -> What other features address this need? |
| **Causal** | Alternative causes | "X causes Y" -> What else could cause Y? |
| **Belief** | Binary + evidence | "Users prefer X" -> What's the actual evidence? |
| **Assumption** | Existence check | "This will scale" -> What if it fundamentally can't? |

### Unconventional Alternative Requirement

For each major AW, include at least one genuinely unconventional alternative -- not just the obvious opposite:

- What if the opposite of conventional wisdom is true?
- What would an outsider/novice suggest?
- What hasn't been tried, and why not?
- What would be embarrassing to suggest but might actually work?

**If every alternative feels safe and reasonable, you haven't explored far enough.**

### Depth Floors

| Depth | Min Claims (C) | Min Findings (F) | Min Tree Levels | Min CRUX |
|-------|----------------|-------------------|-----------------|----------|
| 1x | 5 | 12 | 3-4 | 2 |
| 2x | 7 | 20 | 4-5 | 3 |
| 4x | 12 | 35 | 5-6 | 5 |
| 8x | 18 | 55 | 6-8 | 8 |
| 16x | 25 | 85 | 8-10 | 12 |
| 32x | 35 | 130 | 10-12 | 16 |

These are floors. Go deeper where insight is dense. Compress where it's not.

---

## Phase 2: FINDING REGISTRY (Step 3)

After ALL exploration is complete, compile EVERY finding into a categorized registry. Nothing from Phase 1 gets left out.

```
FINDING REGISTRY
================

CLAIMS TESTED:
[C1] [text] -- TYPE: explicit -- VOI: high
[C2] [text] -- TYPE: implicit -- VOI: medium
...

AR FINDINGS (Implications):
[F1] [text] -- STRENGTH: necessary -- PARENT: C1
[F2] [text] -- STRENGTH: probable -- PARENT: F1
...

AR FINDINGS (Foreclosures):
[F6] [text] -- PARENT: C1
[F7] [text] -- PARENT: F6
...

AW FINDINGS (Wrongness Reasons):
[F8] [text] -- SEVERITY: fatal -- PARENT: C1
[F13] [text] -- SEVERITY: serious -- PARENT: C1
...

AW FINDINGS (Derived Alternatives):
[F11] [text] -- DERIVED FROM: F8
[F15] [text] -- DERIVED FROM: F13
...

BEDROCK REACHED:
[F3] BEDROCK-TEST: [text]
[F5] BEDROCK-OBSERVE: [text]
[F10] BEDROCK-TEST: [text]
...

TENSIONS:
[F-number] contradicts [F-number]: [description]
...

CLAIM VERDICTS:
[C1] [VALIDATED / REJECTED / DAMAGED / CONDITIONAL / UNCERTAIN]
  -- AR evidence: [F-numbers]
  -- AW evidence: [F-numbers]
  -- Verdict derived from: [which evidence is stronger and why]
[C2] ...

CRUX POINTS:
[CRUX-1] [precise question] -- resolves: [F-numbers] -- test: [how]
[CRUX-2] [precise question] -- resolves: [F-numbers] -- test: [how]
...

TOTALS:
- Claims tested: [N]
- Total findings: [N]
- AR findings: [N] ([N] necessary, [N] probable, [N] possible)
- AW findings: [N] ([N] fatal, [N] serious, [N] conditional)
- Foreclosures: [N]
- Derived alternatives: [N]
- Bedrock reached: [N]
- Tensions: [N]
- Verdicts: [N] validated, [N] rejected, [N] damaged, [N] conditional, [N] uncertain
- CRUX points: [N]
```

**Verdict values (derived from the tree, not asserted):**
- **VALIDATED**: AR evidence reaches bedrock, AW reasons don't reach fatal bedrock
- **REJECTED**: AW fatal reason reaches bedrock
- **DAMAGED**: Serious AW reasons found but none individually fatal at bedrock
- **CONDITIONAL**: Wrong under specific stated conditions, right under others
- **UNCERTAIN**: Neither side reached bedrock -- needs more investigation

**Rules for the registry:**
- Every C-numbered claim from Step 1 appears here. No exceptions.
- Every F-numbered finding from Phase 1 appears here. No exceptions.
- Verdicts must be DERIVED from the tree, not asserted. Point to the specific findings.
- If a verdict is unclear, mark UNCERTAIN, not VALIDATED.

---

## Phase 3: SYNTHESIS (Step 4)

Derived entirely from the registry. No new findings introduced here.

```
ORIGINAL INPUT: [restated]

OVERALL PATTERN: [expansive / constraining / contradictory / convergent / mixed]

WHAT THE ANALYSIS ACTUALLY FOUND:
[Numbered list of every substantive finding, referencing F-numbers and C-numbers]
1. [finding, from C1: F1->F3]
2. [finding, from C1: F8->F10]
3. [finding, from C2: F20->F25]
...

KEY TENSIONS:
[Any F-numbers that contradict each other. If none found, say so.]
1. [F-number] vs [F-number]: [what this tension means]
2. ...

WEAKEST LINKS:
[Which findings in the chains are Possible/Conditional rather than Necessary/Fatal?
 These are where analysis might break. Reference F-numbers.]

ALTERNATIVES DERIVED FROM ANALYSIS:
[Only alternatives that emerged from wrongness reasons. Each cites F-numbers.
 If no alternatives emerged, say "None derived -- further exploration needed."]
1. [alternative] -- derived from [F-numbers]
2. ...

TESTABLE PREDICTIONS:
- [prediction derived from specific F-numbers]
- [prediction derived from specific F-numbers]

DO_FIRST ACTIONS:
1. [action] -- WHO: [Claude/user] -- resolves: [CRUX-number or F-numbers]
2. [action] -- WHO: [Claude/user] -- resolves: [CRUX-number or F-numbers]
...

UNRESOLVED:
- [claims that stayed UNCERTAIN -- what would resolve them]
- [findings that stayed Possible -- what would confirm or deny them]
```

---

## Anti-Failure Checks

| Failure Mode | Signal | Fix |
|-------------|--------|-----|
| **Soft AW** | "Wrong but with conditions it works" | That's AR. Find why it's ACTUALLY wrong. |
| **Premature alternative** | Asserting what's "better" before finishing exploration | Delete it. Alternatives come from the registry, not intuition. |
| **Opinion bedrock** | Labeling "probably true" as BEDROCK | Not bedrock. Keep recursing until testable/logical/observable. |
| **Cherry-picked synthesis** | Synthesis mentions 5 findings but registry has 30 | Synthesis must reference ALL substantive findings from registry. |
| **Validation parade** | Every claim VALIDATED | Find the foreclosures and costs. What do you LOSE? |
| **Narrative tree** | Tree reads as prose paragraphs with indent | Use numbered findings. Every node gets an F-number. |
| **Missing foreclosures** | Only listing what opens up | Every "yes" is also a "no." Find what closes. |
| **Conventional contrarian** | The "wrong" take is one everyone already knows | Find the wrong take nobody is comfortable with. |
| **Cheerleading AR** | Every AR implication is positive | Find what you're COMMITTED to. Costs are implications too. |

---

## When ARAW Fails

If producing same findings repeatedly -> check for fish in dreams (expecting a specific answer)
If explanations don't fit -> check for red herring
If confusion when approaching -> check for smokescreen

Try: go deeper, reframe the question, or use `/space_discovery` to find what space you're missing.

---

## Saving Output

Output is NOT auto-saved. If the user wants to save, they invoke `/savefile` after the session.

---

## Pre-Completion Check

- [ ] All claims numbered (C1, C2, ...) with types and VOI
- [ ] All findings numbered (F1, F2, ...) with classification
- [ ] Depth floors met (claims, findings, tree levels, CRUX)
- [ ] AR and AW explored with equal rigor
- [ ] Every branch reaches bedrock (BEDROCK-TEST/LOGIC/OBSERVE/TENSION -- not opinion)
- [ ] ALL claims from Step 1 appear in registry (none dropped)
- [ ] ALL findings from Phase 1 appear in registry (none dropped)
- [ ] Verdicts derived from tree, not asserted
- [ ] Synthesis introduces NO new findings -- only references C-numbers and F-numbers
- [ ] Alternatives derived from analysis, not asserted from thin air (each cites F-numbers)
- [ ] At least one uncomfortable finding
- [ ] Foreclosures and costs explicitly identified (not just positives)
- [ ] Weakest links identified with F-numbers
- [ ] Testable predictions reference specific F-numbers
- [ ] **Validation bias check**: If >80% of claims VALIDATED, go back and test harder. At least 20% should be REJECTED or genuinely UNCERTAIN.
- [ ] **Unconventional check**: At least 1 AW branch explored a genuinely unconventional alternative
- [ ] **Cheerleading check**: If every AR finding is positive, you missed the costs. Go back.
- [ ] **Softness check**: If >50% of AW claims SURVIVED, either the claim is robust or you were too soft
