---
name: "u - Universalize"
description: Universalize - Extract the complete space of assumptions, dimensions, and alternatives from any claim. Map before you judge. Track every finding.
---

# U - Universalize

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

1. **Map before you judge.** Universalization is pure exploration — finding what EXISTS, not what's GOOD. Don't evaluate during mapping. That's AR/AW's job.

2. **Explore before concluding.** U has two phases: EXPLORATION (find everything) and REGISTRY (compile what you found). Never conclude during exploration. Never introduce new findings during registry.

3. **Every finding gets tracked.** When you find an assumption, alternative, dimension, or perspective — number it. It goes in the registry. Nothing gets lost in prose.

4. **Categories reveal siblings.** When you identify what something is an INSTANCE of, you immediately see what else is in that category. This is the most powerful technique — use it.

5. **The goal is completeness, not depth.** U produces breadth — the full space. A good U session makes you say "I didn't realize there were that many options."

6. **Unbundling is mandatory.** Every statement contains multiple claims. Find them all before applying techniques.

---

## Phase 1: EXPLORATION

### Step 1: State and Unbundle the Claim

```
INPUT: [what the user said]
CLAIM: [precise restated version]
CLAIM TYPE: [factual / strategic / design / causal / belief / assumption / decision / meta]
```

Then unbundle — single statements contain multiple claims. Number each:

```
[U1] EXPLICIT: [what's directly stated]
[U2] IMPLICIT: [what's assumed but not said]
[U3] PRESUPPOSED: [what must be true for the statement to make sense]
[U4] BUNDLED: [separate assertions packed together]
[U5] META: [claims about the type of question or how to approach it]
```

### Step 2: Apply Techniques

For each unbundled claim, apply techniques that produce findings. Number every finding.

**Technique 1: STATE SPACE** — What states could this be in?
```
[U6] [alternative 1]
[U7] [alternative 2]
[U8] [the negation]
[U9] [the "do nothing" option]
[U10] [the reframe — what if the question is wrong?]
```

**Technique 2: INSTANCE-TO-CATEGORY** — What is this an instance of? What are siblings?
```
[U11] [X] is an instance of [CATEGORY]
[U12] Sibling: [sibling 1]
[U13] Sibling: [sibling 2]
[U14] Go up a level: [CATEGORY] is an instance of [HIGHER CATEGORY]
[U15] Higher sibling: [sibling at higher level]
```

**Technique 3: PARAMETER VARIATION** — What are the variables and their ranges?
```
[U16] Parameter: [name] — current: [value] — range: [min to max]
[U17] Parameter: [name] — current: [value] — range: [min to max]
```

**Technique 4: PERSPECTIVE ROTATION** — Who sees this differently?
```
[U18] [stakeholder 1] sees: [their version]
[U19] [stakeholder 2] sees: [their version]
[U20] [outsider] sees: [their version]
[U21] [opponent] sees: [their version]
```

**Technique 5: ASSUMPTION EXTRACTION** — What must be true for this to hold?
```
[U22] LOAD-BEARING: [assumption] — if false: [consequence]
[U23] LOAD-BEARING: [assumption] — if false: [consequence]
[U24] BACKGROUND: [assumption] — probably true but worth noting
```

**Technique 6: DIMENSION DISCOVERY** — What axes does this exist on?
```
[U25] Dimension: [name] — claim sits at: [position]
[U26] Dimension: [name] — claim sits at: [position]
[U27] HIDDEN dimension: [name] — not discussed but relevant
```

**Technique 7: TEMPORAL VARIATION** — How does this change over time?
```
[U28] Short-term (days): [what's true]
[U29] Medium-term (months): [what changes]
[U30] Long-term (years): [what changes more]
```

**Technique 8: SCALE VARIATION** — At what level does this hold?
```
[U31] Individual: [true/false/different]
[U32] Team: [true/false/different]
[U33] Organization: [true/false/different]
```

**Don't apply all 8 mechanically.** Use the ones that produce findings. Skip the ones that don't.

| Claim Type | Primary Techniques | Secondary |
|-----------|-------------------|-----------|
| **Factual** | Assumption extraction, state space | Perspective |
| **Strategic** | Instance-to-category, parameter variation, perspective | Temporal, scale |
| **Design** | State space, parameter variation, dimension discovery | Perspective |
| **Causal** | Assumption extraction, perspective, temporal | Scale |
| **Decision** | State space, instance-to-category, parameter variation | All others |
| **Belief** | Assumption extraction, perspective, dimension discovery | Temporal |

---

## Phase 2: FINDING REGISTRY

After exploration, compile EVERY finding into a categorized list. Nothing from Phase 1 gets left out.

```
FINDING REGISTRY
================

UNBUNDLED CLAIMS:
[U1] [text] — TYPE: explicit
[U2] [text] — TYPE: implicit
...

ALTERNATIVES FOUND:
[U6] [text] — SOURCE: state space
[U7] [text] — SOURCE: state space
[U12] [text] — SOURCE: instance-to-category
...

ASSUMPTIONS FOUND:
[U22] [text] — LOAD-BEARING — if false: [consequence]
[U23] [text] — LOAD-BEARING — if false: [consequence]
[U24] [text] — BACKGROUND
...

DIMENSIONS FOUND:
[U25] [text]
[U26] [text]
[U27] [text] — HIDDEN
...

PERSPECTIVES FOUND:
[U18] [text]
[U19] [text]
...

TEMPORAL/SCALE VARIATIONS:
[U28-U33] [text]
...

TOTALS:
- Unbundled claims: [N]
- Alternatives: [N]
- Assumptions: [N] ([N] load-bearing)
- Dimensions: [N] ([N] hidden)
- Perspectives: [N]
```

---

## Phase 3: SYNTHESIS

Derived entirely from the registry. No new findings introduced here.

```
ORIGINAL CLAIM: [restated]

SPACE SIZE: [total unique findings from registry]

VOI RANKING (Value of Information — which findings matter most):
1. [highest-VOI finding — U-number — learning this changes the most]
2. [second highest — U-number]
3. [third — U-number]

LOAD-BEARING ASSUMPTIONS:
[List the assumptions that, if wrong, change everything — U-numbers only]

HIDDEN DIMENSIONS:
[Axes the original claim didn't mention but exists on — U-numbers only]

READY FOR:
- /ar [specific high-VOI claim from registry] — to explore what follows if true
- /aw [specific high-VOI claim from registry] — to test if it holds
- /uaua [the full analysis if warranted]
```

---

## Depth Scaling

| Depth | Min Unbundled Claims | Min Techniques | Min Total Findings |
|-------|---------------------|---------------|-------------------|
| 1x | 3 | 3 | 12 |
| 2x | 5 | 4 | 20 |
| 4x | 8 | 5 | 35 |
| 8x | 12 | 6 | 60 |
| 16x | 18 | 7 | 100 |
| 32x | 25 | 8 | 150 |

Default: 2x. These are floors.

---

## Pre-Completion Check

- [ ] Claim restated precisely and unbundled
- [ ] All unbundled claims identified (explicit, implicit, presupposed, bundled, meta)
- [ ] Techniques applied (minimum for depth level)
- [ ] ALL findings from Phase 1 appear in registry (none dropped)
- [ ] Registry includes totals
- [ ] VOI ranking provided (references U-numbers)
- [ ] Load-bearing assumptions identified (references U-numbers)
- [ ] Synthesis introduces NO new findings — only references U-numbers
- [ ] **Completeness check**: Would someone from a different domain or perspective spot something you missed? If probably yes, keep going.
- [ ] Output points to next step (/ar, /aw, or /uaua on specific high-VOI items)
