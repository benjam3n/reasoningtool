---
name: uaua
description: UAUA Combined Exploration - Universalize, ARAW, loop, synthesize. Map possibilities with numbered findings, test rigorously with numbered claims, compile a complete registry, derive synthesis only from the registry.
---

# UAUA - Universalize -> ARAW -> Universalize -> ARAW

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

These govern everything. When procedure conflicts with principle, follow the principle.

1. **Explore until insight, not until quota.** Depth targets are floors, not ceilings. Go deeper where surprising, compress where obvious. A branch is exhausted when 3 consecutive expansions produce no new findings.

2. **Loop until stable, not once through.** When testing reveals new possibilities, loop back and map them. Stop when no genuinely new candidates appear (max 3 iterations).

3. **Generate then evaluate.** For creative/generative domains (design, writing, strategy): produce candidate artifacts before testing them. Labels like "compress the hero" are less useful than actual compressed hero code.

4. **Every finding gets tracked.** When you find a candidate, implication, wrongness reason, edge case, or alternative -- number it. It goes in the registry. Nothing gets lost in prose.

5. **Three phases, strict separation.** Exploration discovers (no conclusions). Registry compiles (no new findings). Synthesis derives (only from registry). Never mix phases.

6. **Bedrock is not an opinion.** Bedrock means ONE of:
   - **BEDROCK-TEST**: Empirically testable
   - **BEDROCK-LOGIC**: Logically necessary
   - **BEDROCK-OBSERVE**: Directly observable
   - **BEDROCK-TENSION**: Contradicts another established finding
   - "This seems right" or "probably works" is NOT bedrock. Keep recursing.

7. **Alternatives are DERIVED, not asserted.** Don't pull alternatives from thin air. If X is wrong because of Y, the alternative is whatever Y points to. Every alternative must cite the finding it derives from.

8. **AW must be genuinely adversarial.** Soft AW -- "well, with conditions it works" -- is AR wearing a hat. Real AW finds reasons the claim is WRONG and conditions where it FAILS.

9. **Rejection is a valid and expected outcome.** If a session validates every candidate, something is wrong. Expect 20-40% of candidates to be REJECTED or genuinely UNCERTAIN.

10. **Trust the impression.** When your overall feeling about something conflicts with your analytical decomposition, investigate the feeling first. The impression is data.

---

## The Flow

```
U0: GROUND (Identify exemplars -- what does good look like?)
    |
U1: MAP (Apply techniques to find the complete possibility space -- number everything)
    |
[G1: GENERATE -- for creative domains, produce candidate artifacts]
    |
A1: TEST (ARAW top candidates -- number every finding, recurse to bedrock)
    |
    <- Loop back to U1 if A1 revealed genuinely new directions (max 3 loops)
    |
U2: EDGE-CASE (Find where validated candidates break -- number everything)
    |
A2: VALIDATE (Test edge cases, produce verdicts with derivation trails)
    |
REGISTRY (Compile ALL numbered items from all phases)
    |
SYNTHESIS (Derive conclusions ONLY from registry)
```

### When to Skip Steps

- **U0**: Skip for pure logic/math, or when user supplied references
- **G1**: Skip for analytical domains (strategy, engineering, research). Use for design, writing, creative work.
- **Feedback loop**: Skip when A1 produces no surprises

---

## Phase 1: EXPLORATION

### U0: Ground in Exemplars

Before analyzing, ask: **What does good look like in this domain?**

1. Identify 3-5 best existing examples
2. Note what they share (likely fundamental) vs differ on (likely stylistic)
3. Record the felt impression -- this is your perceptual anchor throughout

---

### U1: Map the Space

Apply techniques to find candidates. **Number every finding: U1, U2, U3...**

```
[U1] EXPLICIT: [what the input directly states]
[U2] IMPLICIT: [what's assumed but not said]
[U3] PRESUPPOSED: [what must be true for the input to make sense]
[U4] BUNDLED: [separate assertions packed together]
[U5] META: [claims about the type of question or approach]
```

Then apply techniques (select based on domain):

**Technique 1: STATE SPACE** -- What states could this be in?
```
[U6] [alternative 1]
[U7] [alternative 2]
[U8] [the negation]
[U9] [the "do nothing" option]
[U10] [the reframe -- what if the question is wrong?]
```

**Technique 2: INSTANCE-TO-CATEGORY** -- What is this an instance of? What siblings?
```
[U11] [X] is an instance of [CATEGORY]
[U12] Sibling: [sibling 1]
[U13] Sibling: [sibling 2]
```

**Technique 3: PARAMETER VARIATION** -- What variables, what ranges?
```
[U14] Parameter: [name] -- current: [value] -- range: [min to max]
[U15] Parameter: [name] -- current: [value] -- range: [min to max]
```

**Technique 4: PERSPECTIVE ROTATION** -- Who sees this differently?
```
[U16] [stakeholder 1] sees: [their version]
[U17] [stakeholder 2] sees: [their version]
[U18] [outsider] sees: [their version]
```

**Technique 5: ASSUMPTION EXTRACTION** -- What must be true?
```
[U19] LOAD-BEARING: [assumption] -- if false: [consequence]
[U20] LOAD-BEARING: [assumption] -- if false: [consequence]
[U21] BACKGROUND: [assumption] -- probably true but worth noting
```

**Technique 6: DIMENSION DISCOVERY** -- What axes?
```
[U22] Dimension: [name] -- claim sits at: [position]
[U23] HIDDEN dimension: [name] -- not discussed but relevant
```

**Technique 7: TEMPORAL VARIATION**
```
[U24] Short-term: [what's true]
[U25] Medium-term: [what changes]
[U26] Long-term: [what changes more]
```

**Technique 8: SCALE VARIATION**
```
[U27] Individual: [true/false/different]
[U28] Team: [true/false/different]
[U29] Organization: [true/false/different]
```

**Don't apply all 8 mechanically.** Use the ones that produce findings. Skip the ones that don't. Follow surprise.

Also available for creative/design domains:
- EXEMPLAR COMPARISON, SENSORY EVALUATION, COMPOSITIONAL ANALYSIS, EMOTIONAL RESPONSE, PATTERN MATCHING

| Domain | Primary Techniques | Secondary |
|--------|-------------------|-----------|
| **Design/UX** | State space, instance-to-category, perspective, perceptual | Temporal, scale |
| **Strategy** | State space, instance-to-category, parameter variation, perspective | Temporal, scale |
| **Engineering** | State space, parameter variation, assumption extraction, scale | Perspective |
| **Writing** | Instance-to-category, perspective, dimension discovery | Temporal |

---

### G1: Generate (Creative Domains Only)

For design, writing, and other generative problems: **produce candidate artifacts, not just labels.**

Number each candidate: **G1, G2, G3...**

```
[G1] Candidate: [conventional approach] -- [concrete artifact]
[G2] Candidate: [unconventional approach] -- [concrete artifact]
[G3] Candidate: [extreme/ambitious approach] -- [concrete artifact]
```

- Generate at least 3 distinct candidates
- Artifacts should be concrete enough to evaluate (actual code, actual prose, actual layout)
- Don't evaluate yet -- that's A1's job

**Unconventional requirement:** At least one candidate must be genuinely unconventional -- not just the obvious alternative. If every candidate feels safe, you haven't explored far enough.

---

### A1: Test with ARAW

For each top candidate, build a numbered AR/AW tree. **Number every finding: F1, F2, F3...**

```
Candidate [G1 or U-number]:
  ASSUME RIGHT:
  [F1] If right: [implication] -- Necessary/Probable/Possible
    [F2] If F1 right: [deeper implication]
      [F3] [-> BEDROCK-TEST: specific test]
  [F4] FORECLOSED if right: [what becomes impossible]

  ASSUME WRONG:
  [F5] Wrong because: [reason] -- Fatal/Serious/Conditional
    [F6] If F5 holds: [deeper reason]
      [F7] [-> BEDROCK-OBSERVE: observable fact]
    [F8] Alternative derived from F5: [what F5 points toward]
  [F9] Wrong because: [second reason] -- Fatal/Serious/Conditional
    ...
```

**Classification:**
- AR: Necessary / Probable / Possible / Foreclosed
- AW: Fatal / Serious / Conditional
- Stop ONLY at bedrock: BEDROCK-TEST, BEDROCK-LOGIC, BEDROCK-OBSERVE, BEDROCK-TENSION

### Feedback Loop

After A1: did testing reveal genuinely new candidates not in U1? If yes, loop back to U1 to map the expanded space. Number new findings continuing from where you left off. Max 3 loops. Converge when no new candidates emerge.

---

### U2: Find Edge Cases

For each surviving candidate, find where it breaks. **Number everything: E1, E2, E3...**

```
[E1] Boundary: [condition where candidate breaks]
[E2] Scale failure: [what happens at 10x/100x]
[E3] Temporal limit: [when does this stop working?]
[E4] Stakeholder conflict: [who disagrees and why]
[E5] Context dependency: [where this only works in specific context]
```

Also for rejected candidates: **under what conditions would they work?**
```
[E6] Rejected [G-number] works if: [specific condition]
```

---

### A2: Validate Edge Cases

Test each edge case with quick AR/AW. **Continue numbering findings.**

```
[E1] "[boundary condition]"
  [F30] AR: [why candidate might survive this] -- Necessary/Probable/Possible
  [F31] AW: [why this edge case kills it] -- Fatal/Serious/Conditional
    [F32] [-> BEDROCK-TEST: specific test]
```

---

## Phase 2: FINDING REGISTRY

After ALL exploration is complete, compile EVERY numbered item into a categorized registry. Nothing from Phase 1 gets left out.

```
FINDING REGISTRY
================

UNBUNDLED CLAIMS:
[U1] [text] -- TYPE: explicit
[U2] [text] -- TYPE: implicit
...

CANDIDATES (from U1 mapping):
[U6] [text] -- SOURCE: state space
[U12] [text] -- SOURCE: instance-to-category
...

GENERATED ARTIFACTS (if G1 used):
[G1] [text]
[G2] [text]
...

ASSUMPTIONS:
[U19] [text] -- LOAD-BEARING -- if false: [consequence]
[U20] [text] -- LOAD-BEARING -- if false: [consequence]
[U21] [text] -- BACKGROUND
...

DIMENSIONS:
[U22] [text]
[U23] [text] -- HIDDEN
...

PERSPECTIVES:
[U16] [text]
[U17] [text]
...

AR FINDINGS:
[F1] [text] -- STRENGTH: necessary -- PARENT: [source]
[F2] [text] -- STRENGTH: probable -- PARENT: F1
...

AW FINDINGS:
[F5] [text] -- SEVERITY: fatal -- PARENT: [source]
[F9] [text] -- SEVERITY: serious -- PARENT: [source]
...

FORECLOSURES:
[F4] [text] -- PARENT: [source]
...

DERIVED ALTERNATIVES:
[F8] [text] -- DERIVED FROM: F5
...

EDGE CASES:
[E1] [text] -- TYPE: boundary
[E2] [text] -- TYPE: scale
...

BEDROCK REACHED:
[F3] BEDROCK-TEST: [text]
[F7] BEDROCK-OBSERVE: [text]
[F32] BEDROCK-TEST: [text]
...

TENSIONS:
[F-number] contradicts [F-number]: [description]
...

CANDIDATE VERDICTS:
[G1/U-number] [VALIDATED / REJECTED / DAMAGED / CONDITIONAL / UNCERTAIN]
  -- AR evidence: [F-numbers]
  -- AW evidence: [F-numbers]
  -- Edge cases: [E-numbers]
  -- Verdict derived from: [which evidence is stronger and why]
...

TOTALS:
- Unbundled claims: [N]
- Candidates mapped: [N]
- Generated artifacts: [N]
- Assumptions: [N] ([N] load-bearing)
- Dimensions: [N] ([N] hidden)
- Perspectives: [N]
- AR findings: [N] ([N] necessary, [N] probable, [N] possible)
- AW findings: [N] ([N] fatal, [N] serious, [N] conditional)
- Foreclosures: [N]
- Derived alternatives: [N]
- Edge cases: [N]
- Bedrock reached: [N]
- Tensions: [N]
- Verdicts: [N] validated, [N] rejected, [N] damaged, [N] conditional, [N] uncertain
```

**Verdict values (derived from the tree, not asserted):**
- **VALIDATED**: AR evidence reaches bedrock, AW reasons don't reach fatal bedrock, edge cases survived
- **REJECTED**: AW fatal reason reaches bedrock. Record WHY -- rejected candidates may work in other contexts.
- **DAMAGED**: Serious AW reasons found but none individually fatal at bedrock
- **CONDITIONAL**: Wrong under specific conditions, right under others (state both)
- **UNCERTAIN**: Neither side reached bedrock -- needs more investigation

**Rules for the registry:**
- Every U-numbered, G-numbered, F-numbered, and E-numbered item from Phase 1 appears here. No exceptions.
- Verdicts must be DERIVED from the tree, not asserted. Point to specific findings.
- If a verdict is unclear, mark UNCERTAIN, not VALIDATED.

---

## Phase 3: SYNTHESIS

Derived entirely from the registry. No new findings introduced here.

```
ORIGINAL INPUT: [restated]

SPACE SIZE: [total unique findings from registry]

WHAT THE ANALYSIS ACTUALLY FOUND:
[Numbered list of EVERY substantive finding, referencing item numbers]
1. [finding, from U-numbers and F-numbers]
2. [finding, from F-numbers]
3. [finding, from E-numbers and F-numbers]
...

KEY TENSIONS:
[Any items that contradict each other. Reference numbers.]
1. [item] vs [item]: [what this tension means] -- TYPE: [resource allocation / information gap / optimization frontier / commitment decision]
2. ...

VOI RANKING (Value of Information -- which findings matter most):
1. [highest-VOI finding -- item number -- learning this changes the most]
2. [second highest -- item number]
3. [third -- item number]

LOAD-BEARING ASSUMPTIONS:
[Assumptions that, if wrong, change everything -- item numbers only]

HIDDEN DIMENSIONS:
[Axes the original input didn't mention but exists on -- item numbers only]

WEAKEST LINKS:
[Which findings are Possible/Conditional rather than Necessary/Fatal?
 These are where analysis might break. Reference item numbers.]

ALTERNATIVES DERIVED FROM ANALYSIS:
[Only alternatives that emerged from wrongness reasons. Each cites F-numbers.
 If no alternatives emerged, say "None derived -- further exploration needed."]
1. [alternative] -- derived from [F-numbers]
2. ...

TESTABLE PREDICTIONS:
- [prediction derived from specific item numbers]
- [prediction derived from specific item numbers]

DO_FIRST ACTIONS:
1. [action] -- WHO: [Claude/user] -- resolves: [item numbers]
2. [action] -- WHO: [Claude/user] -- resolves: [item numbers]
...

UNRESOLVED:
- [candidates that stayed UNCERTAIN -- what would resolve them]
- [findings that stayed Possible -- what would confirm or deny them]

READY FOR:
- /ar [specific high-VOI claim] -- to go deeper on rightness
- /aw [specific high-VOI claim] -- to go deeper on wrongness
- /u [specific dimension to explore further]
```

---

## Depth Scaling

| Depth | Min Candidates (U1) | Min Edge Cases (U2) | Min ARAW Levels | Min Total Findings | Min Output Lines |
|-------|---------------------|---------------------|-----------------|-------------------|------------------|
| 1x | 5 | 3 | 3 | 20 | 400 |
| 2x | 8 | 5 | 4 | 35 | 800 |
| 4x | 12 | 8 | 5 | 55 | 1600 |
| 8x | 18 | 12 | 6 | 85 | 3200 |
| 16x | 25 | 18 | 7 | 130 | 6400 |
| 32x | 35 | 25 | 8 | 200 | 12800 |

Default depth: 2x. Detect from user input ("uaua 8x" -> 8x). These are FLOORS.

---

## Phase Awareness

UAUA is not equally useful for all phases of creative work:

| Phase | UAUA Fit | What to Do |
|-------|----------|------------|
| **Strategy** ("What should we build?") | Strong | Full UAUA |
| **Ideation** ("What could it look like?") | Use G1 | Exemplar comparison + generation, light evaluation |
| **Critique** ("Is this good enough?") | Moderate | UAUA with perceptual techniques. Trust the gestalt. |
| **Polish** ("Make it perfect") | Weak | Direct iteration, not analysis |

---

## Anti-Failure Checks

| Failure Mode | Signal | Fix |
|-------------|--------|-----|
| **Soft AW** | "Wrong but with conditions it works" | That's AR. Find why it's ACTUALLY wrong. |
| **Premature alternative** | Asserting what's "better" before finishing exploration | Delete it. Alternatives come from the registry, not intuition. |
| **Opinion bedrock** | Labeling "probably true" as BEDROCK | Not bedrock. Keep recursing until testable/logical/observable. |
| **Cherry-picked synthesis** | Synthesis mentions 5 findings but registry has 40 | Synthesis must reference ALL substantive findings. |
| **Validation parade** | Every candidate VALIDATED | Find the foreclosures and costs. 20-40% should be rejected. |
| **Narrative tree** | Tree reads as prose paragraphs | Use numbered findings. Every node gets a number. |
| **Missing foreclosures** | Only listing what opens up | Every "yes" is also a "no." Find what closes. |
| **Dropped findings** | Registry has fewer items than exploration produced | Go back and add every numbered item. No exceptions. |
| **Asserted verdicts** | "VALIDATED" without citing F-numbers | Verdicts must point to specific evidence. |

---

## Saving Output

Output is NOT auto-saved. If the user wants to save, they invoke `/sf` after the session.

---

## Pre-Completion Check

Before finishing:
- [ ] All findings numbered (U, G, F, E series) throughout exploration
- [ ] Depth floors met (candidates, edge cases, ARAW levels, total findings)
- [ ] Every branch reaches bedrock (BEDROCK-TEST/LOGIC/OBSERVE/TENSION -- not opinion)
- [ ] ALL numbered items from Phase 1 appear in registry (none dropped)
- [ ] Registry includes totals
- [ ] Verdicts derived from tree with F-number citations, not asserted
- [ ] Synthesis introduces NO new findings -- only references item numbers
- [ ] Alternatives derived from analysis (each cites F-numbers), not asserted from thin air
- [ ] At least 1 genuinely novel finding per major branch
- [ ] Testable predictions reference specific item numbers
- [ ] Gestalt impression consistent with analytical conclusion
- [ ] If creative domain: artifacts generated, not just labels analyzed
- [ ] **Validation bias check**: If >80% of candidates VALIDATED, go back and test harder. At least 20% should be REJECTED or genuinely UNCERTAIN.
- [ ] **Unconventional check**: At least 1 candidate or AW branch explored a genuinely unconventional alternative
- [ ] **Cheerleading check**: If every finding is positive, you missed the costs. Go back.
- [ ] **Completeness check**: Would someone from a different domain spot something you missed? If yes, keep going.
