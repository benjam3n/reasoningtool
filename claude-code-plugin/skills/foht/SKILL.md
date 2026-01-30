---
name: "foht - Figure Out How To"
description: Figure Out How To - Method discovery when you know WHAT but not HOW. Systematically map the method space, test candidates, and find approaches that survive scrutiny.
---

# FOHT - Figure Out How To

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

1. **Outcome first, methods second.** Define what "done" looks like before searching for how to get there. If you can't describe the outcome, you can't evaluate methods.

2. **Map before choosing.** Find ALL plausible methods before evaluating any of them. Premature commitment to the first method that seems reasonable is the most common failure.

3. **Methods have prerequisites.** Every method assumes resources, skills, context, or prior state. Surface these. A method that requires what you don't have is not a method — it's a wish.

4. **Test methods, don't rank them.** AR/AW each method against the success criteria. A method either survives scrutiny or it doesn't. Ranking without testing is guessing.

5. **Every finding gets tracked.** Number every method, prerequisite, test result, and edge case. Nothing gets lost in prose.

6. **The unconventional method exists.** If every method you found is obvious, you haven't looked hard enough. The best method is often the one nobody considers because it reframes the problem.

---

## Phase 1: EXPLORATION

### Step 1: Define the Outcome

Before searching for HOW, define WHAT.

```
GOAL: [what the user wants to achieve — from their input]
DONE LOOKS LIKE: [concrete observable state when goal is achieved]
SUCCESS CRITERIA:
  [H1] MUST: [criterion 1 — binary, checkable]
  [H2] MUST: [criterion 2]
  [H3] MUST: [criterion 3]
  [H4] SHOULD: [criterion — valuable but not required]
CONSTRAINTS:
  [H5] [resource/time/context constraint]
  [H6] [resource/time/context constraint]
NOT THE GOAL: [what this is NOT — common misinterpretations]
```

### Step 2: Map the Method Space

Find all plausible methods. Number each. Use multiple discovery techniques:

**Direct methods** — standard approaches:
```
[H7] METHOD: [name] — [1-sentence description]
[H8] METHOD: [name] — [1-sentence description]
```

**Instance-to-category** — what is this goal an instance of? What methods work for the category?
```
[H9] [goal] is an instance of [CATEGORY]
[H10] Category method: [method that works for the category generally]
[H11] Category method: [another]
```

**Inversion** — instead of achieving the goal, what would prevent it? Remove those.
```
[H12] BLOCKER: [what prevents the goal]
[H13] REMOVAL METHOD: [how to remove that blocker]
```

**Adjacent success** — who has achieved something similar? What did they do?
```
[H14] EXEMPLAR: [who achieved similar] — METHOD: [what they did]
[H15] EXEMPLAR: [who achieved similar] — METHOD: [what they did]
```

**Reframe** — is there a way to make the goal unnecessary?
```
[H16] REFRAME: [different way of looking at it that dissolves the problem]
```

**Decomposition** — break the goal into sub-goals, find methods for each:
```
[H17] SUB-GOAL: [part 1] — METHOD: [how to achieve this part]
[H18] SUB-GOAL: [part 2] — METHOD: [how to achieve this part]
```

### Step 3: Surface Prerequisites

For each method, identify what must be true for it to work:

```
[H19] METHOD [H-number] requires: [prerequisite] — HAVE IT: [yes/no/unknown]
[H20] METHOD [H-number] requires: [prerequisite] — HAVE IT: [yes/no/unknown]
[H21] METHOD [H-number] requires: [prerequisite] — HAVE IT: [yes/no/unknown]
```

Methods with unmet prerequisites need a method for the prerequisite, or they're eliminated.

### Step 4: Test Methods (AR/AW)

For each surviving method, run a compressed AR/AW:

```
METHOD [H-number]: [name]

ASSUME RIGHT (this method works):
  [H22] If right: [what follows] — Necessary/Probable/Possible
  [H23] If right: [deeper implication]
  [H24] FORECLOSED: [what this method prevents/excludes]

ASSUME WRONG (this method fails):
  [H25] Wrong because: [reason] — Fatal/Serious/Conditional
    [H26] [deeper reason or → BEDROCK]
  [H27] Wrong because: [second reason] — Fatal/Serious/Conditional
    [H28] [deeper reason or → BEDROCK]
```

**Verdict for each method:**
- **VIABLE**: AR evidence strong, AW reasons not fatal
- **CONDITIONAL**: Works under specific conditions (state them)
- **BLOCKED**: Prerequisites unmet, no clear path to meeting them
- **ELIMINATED**: Fatal AW reason reached bedrock
- **UNCERTAIN**: Neither side reached bedrock — needs investigation

### Step 5: Find Edge Cases

For viable methods, find where they break:

```
[H29] METHOD [H-number] breaks when: [condition]
[H30] METHOD [H-number] breaks at scale: [what happens at 10x]
[H31] METHOD [H-number] has hidden cost: [cost not obvious upfront]
```

---

## Phase 2: FINDING REGISTRY

Compile EVERY finding. Nothing gets left out.

```
FINDING REGISTRY
================

SUCCESS CRITERIA:
[H1] [text] -- TYPE: must
[H2] [text] -- TYPE: must
[H4] [text] -- TYPE: should
...

CONSTRAINTS:
[H5] [text]
[H6] [text]

METHODS FOUND:
[H7] [text] -- SOURCE: direct
[H10] [text] -- SOURCE: category
[H13] [text] -- SOURCE: inversion
[H14] [text] -- SOURCE: exemplar
[H16] [text] -- SOURCE: reframe
...

PREREQUISITES:
[H19] [text] -- FOR: [H-number] -- MET: [yes/no/unknown]
[H20] [text] -- FOR: [H-number] -- MET: [yes/no/unknown]
...

AR FINDINGS:
[H22] [text] -- FOR: [H-number] -- STRENGTH: [necessary/probable/possible]
...

AW FINDINGS:
[H25] [text] -- FOR: [H-number] -- SEVERITY: [fatal/serious/conditional]
...

EDGE CASES:
[H29] [text] -- FOR: [H-number]
...

METHOD VERDICTS:
[H-number] [method name] -- VERDICT: [viable/conditional/blocked/eliminated/uncertain]
  -- AR evidence: [H-numbers]
  -- AW evidence: [H-numbers]
  -- Prerequisites: [met/unmet — H-numbers]
  -- Edge cases: [H-numbers]
...

TOTALS:
- Success criteria: [N]
- Methods found: [N]
- Prerequisites surfaced: [N] ([N] met, [N] unmet, [N] unknown)
- AR findings: [N]
- AW findings: [N] ([N] fatal, [N] serious, [N] conditional)
- Edge cases: [N]
- Verdicts: [N] viable, [N] conditional, [N] blocked, [N] eliminated, [N] uncertain
```

---

## Phase 3: SYNTHESIS

Derived entirely from the registry. No new findings.

```
GOAL: [restated]
DONE LOOKS LIKE: [restated]

METHODS TESTED: [N total]

VIABLE METHODS:
1. [method — H-number] — VERDICT: viable
   - What it requires: [H-numbers]
   - What it costs: [H-numbers]
   - What it forecloses: [H-numbers]
   - Breaks when: [H-numbers]

2. [method — H-number] — VERDICT: conditional
   - Works if: [conditions — H-numbers]
   - Fails if: [conditions — H-numbers]
   ...

ELIMINATED METHODS (and why):
1. [method — H-number] — eliminated because: [H-numbers]
   ...

RECOMMENDED APPROACH:
[Derived from verdicts — not asserted. If multiple viable, state conditions for choosing.]

FIRST ACTIONS:
1. [action] — resolves: [H-numbers]
2. [action] — resolves: [H-numbers]

UNRESOLVED:
- [methods that stayed uncertain — what would resolve them]
- [prerequisites that are unknown — how to check]

READY FOR:
- /ar [specific method to explore deeper]
- /aw [specific method to stress-test]
- /wt [if the goal itself needs examination]
```

---

## Depth Scaling

| Depth | Min Methods Found | Min Methods Tested | Min Prerequisites | Min Total Findings |
|-------|------------------|-------------------|------------------|-------------------|
| 1x | 4 | 3 | 3 | 15 |
| 2x | 6 | 5 | 5 | 30 |
| 4x | 10 | 8 | 8 | 50 |
| 8x | 15 | 12 | 12 | 80 |

Default: 2x. These are floors.

---

## Anti-Failure Checks

| Failure Mode | Signal | Fix |
|-------------|--------|-----|
| **First method lock-in** | Only one method explored in depth | Map at least 6 methods before testing any |
| **Methods without prerequisites** | "Just do X" with no conditions | Every method requires something. Surface it. |
| **Ranking without testing** | "Method A is best because..." without AR/AW | Test it. AR/AW each method. Verdicts from evidence. |
| **All conventional** | Every method is the obvious approach | Use inversion, reframe, category search. Find the unconventional option. |
| **Goal drift** | Methods don't connect to success criteria | Check each method against H1-H3. Does it actually achieve DONE? |
| **Missing costs** | Methods listed with only benefits | Every method forecloses something. Find it. |

---

## Pre-Completion Check

- [ ] Outcome defined with binary success criteria
- [ ] Method space mapped using multiple discovery techniques (not just direct)
- [ ] Prerequisites surfaced for each method with met/unmet status
- [ ] Each method tested with AR/AW (not just described)
- [ ] Verdicts derived from evidence (H-number citations)
- [ ] At least one unconventional method explored
- [ ] Edge cases found for viable methods
- [ ] ALL findings from Phase 1 in registry (none dropped)
- [ ] Synthesis introduces NO new findings
- [ ] Recommended approach derived from verdicts, not asserted
- [ ] First actions are specific and actionable
