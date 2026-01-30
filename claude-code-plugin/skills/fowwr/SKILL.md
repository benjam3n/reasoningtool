---
name: fowwr
description: Figure Out What Went Wrong - Backward causal diagnosis of failures. Trace from symptom to root cause, test each candidate cause, and derive what would prevent recurrence.
---

# FOWWR - Figure Out What Went Wrong

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

1. **Symptoms are not causes.** The visible failure is where diagnosis starts, not where it ends. "The output was bad" is a symptom. "The output lacked a real unresolved question because the question was never identified" is a cause.

2. **Trace backward, not forward.** Start at the failure and ask "what caused this?" at every step. Don't start at the beginning and ask "what went wrong here?" — that's reconstruction, not diagnosis.

3. **Multiple causes are normal.** Most failures have more than one cause. A single "root cause" is sometimes real, sometimes a premature stop. Keep tracing until you find ALL contributing causes.

4. **Test causes, don't assert them.** A plausible cause is a hypothesis. Test it: if this cause were removed, would the failure still have occurred? If yes, it's not the cause (or not the only one).

5. **Every finding gets tracked.** Number every symptom, cause candidate, test result, and contributing factor. Nothing gets lost in prose.

6. **Prevention > explanation.** The goal isn't just to understand why something failed — it's to identify what would prevent it from failing the same way again. A diagnosis without prevention is an autopsy.

---

## Phase 1: EXPLORATION

### Step 1: State the Failure

```
WHAT HAPPENED: [observable outcome — what actually occurred]
WHAT WAS EXPECTED: [what should have happened instead]
GAP: [the specific difference between actual and expected]
WHEN: [when did the failure become apparent]
SEVERITY: [impact — what was lost or damaged]
```

### Step 2: Identify Symptoms

List everything that was observably wrong. These are symptoms, not causes yet.

```
[W1] SYMPTOM: [observable thing that was wrong]
[W2] SYMPTOM: [another observable thing]
[W3] SYMPTOM: [another]
[W4] FIRST NOTICED: [which symptom appeared first — this may be closest to the cause]
```

### Step 3: Trace Backward (Causal Chain)

For each symptom, ask: **"What caused this?"** Then for each cause: **"What caused THAT?"** Number everything.

```
[W5] [symptom W1] was caused by: [candidate cause]
  [W6] [W5] was caused by: [deeper cause]
    [W7] [W6] was caused by: [deeper still]
      [W8] [→ ROOT: no further cause identifiable / this is a decision or assumption]
  [W9] [W5] was ALSO caused by: [second contributing cause]
    [W10] [W9] was caused by: [deeper]
      ...
[W11] [symptom W2] was caused by: [candidate cause]
  ...
```

**At each node, classify:**
- **Direct**: This directly produced the parent — remove it and the parent doesn't happen
- **Contributing**: This made the parent more likely or worse — remove it and the parent might still happen
- **Enabling**: This didn't cause the parent but allowed it to happen — a missing safeguard

**Root labels (valid stopping points):**
- `ROOT-DECISION: [a specific decision that was made]`
- `ROOT-ASSUMPTION: [an assumption that turned out to be wrong]`
- `ROOT-MISSING: [something that should have existed but didn't — a gap]`
- `ROOT-EXTERNAL: [something outside the system's control]`
- `ROOT-UNKNOWN: [cause is unclear — needs investigation]`

### Step 4: Test Candidate Causes

For each candidate root cause, test with counterfactual:

```
[W12] CAUSE: [candidate — W-number]
  COUNTERFACTUAL: If [this cause] had not occurred, would the failure still have happened?
  [W13] ANSWER: [yes/no/partially] — EVIDENCE: [why you believe this]
  [W14] REMOVAL TEST: Could this cause have been prevented? [yes/no — how]
```

### Step 5: Find Convergence

Look at all causal chains together:

```
[W15] CONVERGENCE: Multiple chains point to: [common deeper cause — W-numbers]
[W16] INDEPENDENCE: These causes are independent: [W-numbers] — fixing one doesn't fix the other
[W17] CHAIN vs PARALLEL: [are causes sequential (A caused B caused C) or parallel (A and B independently caused C)?]
```

### Step 6: Derive Prevention

From the tested causes, derive what would prevent recurrence:

```
[W18] To prevent [W-number root cause]: [what must change]
[W19] DETECTION: How to notice this failure earlier next time: [signal to watch for]
[W20] SAFEGUARD: What check/gate would have caught this: [specific check]
```

---

## Phase 2: FINDING REGISTRY

Compile EVERY finding. Nothing gets left out.

```
FINDING REGISTRY
================

SYMPTOMS:
[W1] [text] -- TYPE: symptom
[W2] [text] -- TYPE: symptom
...

CAUSAL CHAIN:
[W5] [text] -- TYPE: [direct/contributing/enabling] -- PARENT: W1
[W6] [text] -- TYPE: [direct/contributing/enabling] -- PARENT: W5
...

ROOT CAUSES:
[W8] [text] -- TYPE: [decision/assumption/missing/external/unknown]
...

COUNTERFACTUAL TESTS:
[W12] [text] -- TESTED: [W-number] -- RESULT: [confirmed/disconfirmed/partial]
...

CONVERGENCE:
[W15] [text] -- CHAINS: [W-numbers]
...

PREVENTION:
[W18] [text] -- PREVENTS: [W-number]
[W19] [text] -- DETECTS: [W-number]
[W20] [text] -- SAFEGUARDS: [W-number]
...

TOTALS:
- Symptoms: [N]
- Causal chain nodes: [N] ([N] direct, [N] contributing, [N] enabling)
- Root causes identified: [N] ([N] confirmed, [N] partial, [N] unconfirmed)
- Prevention measures: [N]
```

---

## Phase 3: SYNTHESIS

Derived entirely from the registry. No new findings.

```
FAILURE: [what happened — restated]
EXPECTED: [what should have happened]

CAUSAL PATTERN: [convergent / divergent / chain / parallel]

ROOT CAUSES (confirmed):
1. [root cause — W-number] — TYPE: [decision/assumption/missing/external]
   - Caused: [W-numbers of downstream effects]
   - Counterfactual: [W-number — confirmed]
   - Could have been prevented by: [W-number]

2. [root cause — W-number] — TYPE: [...]
   ...

CONTRIBUTING FACTORS (not root but made it worse):
1. [factor — W-number]
   ...

WHAT THE FAILURE ANALYSIS ACTUALLY FOUND:
[Numbered list of every substantive finding, referencing W-numbers]
1. [finding, from W5->W8]
2. [finding, from W11->W13]
...

PREVENTION PLAN:
1. [what to change — W-numbers] — prevents recurrence of: [root cause W-number]
2. [what to check — W-numbers] — detects early: [symptom W-number]
3. [what safeguard to add — W-numbers] — catches: [cause W-number]

UNRESOLVED:
- [causes that stayed ROOT-UNKNOWN — what would clarify them]
- [counterfactuals that were partial — what additional evidence needed]

READY FOR:
- /ar [specific prevention measure to validate]
- /aw [specific root cause diagnosis to stress-test]
- /foht [how to implement a specific prevention measure]
```

---

## Depth Scaling

| Depth | Min Symptoms | Min Causal Chain Depth | Min Causes Tested | Min Total Findings |
|-------|-------------|----------------------|-------------------|-------------------|
| 1x | 2 | 3 | 2 | 12 |
| 2x | 3 | 4 | 3 | 25 |
| 4x | 5 | 5 | 5 | 40 |
| 8x | 8 | 7 | 8 | 70 |

Default: 2x. These are floors.

---

## Anti-Failure Checks

| Failure Mode | Signal | Fix |
|-------------|--------|-----|
| **Symptom as cause** | "It failed because it was bad" | That's restating the symptom. Ask: WHY was it bad? |
| **Single cause tunnel** | Only one causal chain explored | Most failures have multiple contributing causes. Explore branches. |
| **Untested cause** | "The cause was probably X" | Test it. Counterfactual: if X hadn't occurred, would the failure still have happened? |
| **No prevention** | Diagnosis without actionable prevention | A diagnosis without prevention is an autopsy, not engineering. |
| **Blame assignment** | "The user/tool/process was wrong" | That's not a cause. What DECISION or ASSUMPTION led to the wrong action? |
| **Shallow root** | Stopping at "we didn't do X" | Why didn't you do X? What caused that? Keep going. |

---

## Pre-Completion Check

- [ ] Failure stated in observable terms (what happened vs what was expected)
- [ ] Symptoms listed (observable problems, not interpretations)
- [ ] Causal chains traced backward from symptoms to roots
- [ ] Each root cause classified (decision/assumption/missing/external/unknown)
- [ ] Candidate causes tested with counterfactual
- [ ] Convergence/independence of causes identified
- [ ] Prevention measures derived from confirmed causes (W-number citations)
- [ ] ALL findings from Phase 1 in registry (none dropped)
- [ ] Synthesis introduces NO new findings
- [ ] **Blame check**: If diagnosis points at a person/tool instead of a decision/assumption — go deeper
- [ ] **Depth check**: If root cause is "we didn't do X" — ask WHY you didn't do X
