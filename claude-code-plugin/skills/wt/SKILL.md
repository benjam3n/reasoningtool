---
name: wt
description: Want To - AR-based goal exploration. Assume the want is right, trace what it commits you to, find what you actually want, map paths forward.
---

# WANTTO - I Want To

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

1. **Assume the want is right.** The user wants what they say they want. Take it seriously. Trace what it implies — what it commits them to, what it requires, what paths it opens, what it forecloses. This is AR applied to desires.

2. **Wants are bundled.** "I want to start a business" bundles: I want autonomy, I want income, I want to work on this specific thing, I believe a business is the way to get these, I believe I can run a business. Unbundle to find what following through actually requires.

3. **Tracing implications reveals the actual want.** The stated want is the surface. By assuming it's right and following the implications, you discover what the user is actually committed to — which may be deeper or different than what they said. "I want to quit my job" → if right → implies the job is the obstacle → implies they want what the job prevents → THAT is the actual want.

4. **Wants have prerequisites.** "I want to write a book" requires: something to say, time to write, knowledge of how to write, willingness to endure the process. These are implications of the want being right — things that must also be true.

5. **Map before routing.** Understand the full want before sending the user to another skill. A premature /foht or /ar on the wrong aspect wastes the session.

6. **Every finding gets tracked.** Number every unbundled want, implication, prerequisite, and path. Nothing gets lost in prose.

---

## Phase 1: EXPLORATION

### Step 1: State and Unbundle the Want

```
STATED WANT: [what the user said — exact words]
```

Unbundle into component claims. Number each:

```
[G1] DESIRE: [what they want to have/feel/be — the end state]
[G2] METHOD: [the approach they've assumed — the stated way to get there]
[G3] BELIEF: [why they think this method leads to this desire]
[G4] ASSUMPTION: [what must be true for this to work]
[G5] IMPLICIT WANT: [an unstated want bundled inside]
[G6] ANTI-WANT: [what they want to STOP or AVOID — often the real driver]
```

### Step 2: Trace Implications (Assume Right)

Assume the want is right. What follows?

```
[G7] If [G1 desire] is right → what must also be true? [implication]
[G8] If [G2 method] is right → what does it commit to? [commitment]
[G9] If [G3 belief] is right → what does it foreclose? [foreclosure]
[G10] If [G4 assumption] is right → what does it require? [prerequisite]
```

Follow the implication chain to find what the user is actually committed to:

```
[G11] ACTUAL WANT: [what the implication chain points to — the deeper thing]
[G12] CONFIDENCE: [high/medium/low — how clear is the chain]
[G13] The stated want serves: [what deeper want G1 is a means to]
```

### Step 3: Surface Prerequisites

For the actual want, what must be true or exist before it can be achieved?

```
[G13] PREREQUISITE: [what must exist/be true] — STATUS: [met/unmet/unknown]
[G14] PREREQUISITE: [what must exist/be true] — STATUS: [met/unmet/unknown]
[G15] PREREQUISITE: [what must exist/be true] — STATUS: [met/unmet/unknown]
[G16] BLOCKER: [what currently prevents the want] — REMOVABLE: [yes/no/unknown]
[G17] BLOCKER: [what currently prevents the want] — REMOVABLE: [yes/no/unknown]
```

### Step 4: Map the Path Space

What are the possible paths from current state to the actual want?

```
[G18] PATH: [approach 1 — brief description]
  [G19] Requires: [prerequisites — G-numbers or new]
  [G20] Gives up: [what this path forecloses]
  [G21] Risk: [main risk]

[G22] PATH: [approach 2]
  [G23] Requires: [prerequisites]
  [G24] Gives up: [foreclosures]
  [G25] Risk: [main risk]

[G26] PATH: [approach 3 — the one nobody considers]
  ...

[G27] DO-NOTHING PATH: [what happens if the user does nothing]
  [G28] Outcome: [where they end up]
  [G29] Is this acceptable? [yes/no — and to whom]
```

### Step 5: Trace Key Implications Deeper

For the most load-bearing implications, recurse:

```
IMPLICATION [G-number]: [text]
  [G30] If right → [what must also be true] — Necessary/Probable/Possible
    [G31] If THAT is right → [deeper implication]
      [G32] [→ BEDROCK or keep going]
  [G33] FORECLOSED by this: [what becomes impossible if this implication holds]
```

### Step 6: Identify the Crux

What is the single most important thing to get right?

```
[G34] CRUX: [the decision/assumption/prerequisite that changes everything]
[G35] IF CRUX GOES ONE WAY: [consequence — G-numbers]
[G36] IF CRUX GOES OTHER WAY: [consequence — G-numbers]
[G37] HOW TO RESOLVE CRUX: [what would determine which way it goes]
```

---

## Phase 2: FINDING REGISTRY

Compile EVERY finding. Nothing gets left out.

```
FINDING REGISTRY
================

UNBUNDLED WANT:
[G1] [text] -- TYPE: desire
[G2] [text] -- TYPE: method
[G3] [text] -- TYPE: belief
[G4] [text] -- TYPE: assumption
[G5] [text] -- TYPE: implicit want
[G6] [text] -- TYPE: anti-want

IMPLICATIONS (Assume Right):
[G7] [text] -- TYPE: implication
[G8] [text] -- TYPE: commitment
[G9] [text] -- TYPE: foreclosure
[G10] [text] -- TYPE: prerequisite

ACTUAL WANT:
[G11] [text] -- CONFIDENCE: [high/medium/low]
[G12] [text]
[G13] [text] -- TYPE: deeper want

PREREQUISITES:
[G13] [text] -- STATUS: [met/unmet/unknown]
...

BLOCKERS:
[G16] [text] -- REMOVABLE: [yes/no/unknown]
...

PATHS:
[G18] [text] -- TYPE: path
  [G19-G21] [details]
[G22] [text] -- TYPE: path
  [G23-G25] [details]
[G26] [text] -- TYPE: unconventional path
[G27] [text] -- TYPE: do-nothing path

IMPLICATION CHAINS:
[G30] [text] -- FOR: [G-number] -- STRENGTH: [necessary/probable/possible]
[G31] [text] -- PARENT: G30 -- STRENGTH: [necessary/probable/possible]
[G33] [text] -- TYPE: foreclosure
...

CRUX:
[G34] [text]
[G35] [text]
[G36] [text]
[G37] [text]

TOTALS:
- Unbundled components: [N]
- Implications traced: [N]
- Foreclosures: [N]
- Prerequisites: [N] ([N] met, [N] unmet, [N] unknown)
- Blockers: [N] ([N] removable)
- Paths mapped: [N]
- Crux identified: [yes/no]
```

---

## Phase 3: SYNTHESIS

Derived entirely from the registry. No new findings.

```
USER SAID: [exact stated want]

ACTUAL WANT: [G11 — what the implication chain points to]
CONFIDENCE: [G12]
STATED ≠ ACTUAL: [yes/no — and why, with G-numbers]

CURRENT STATE:
- Prerequisites met: [G-numbers]
- Prerequisites unmet: [G-numbers]
- Active blockers: [G-numbers]

PATHS AVAILABLE:
| Path | Requires | Gives Up | Risk | Status |
|------|----------|----------|------|--------|
| [G18] | [G19] | [G20] | [G21] | viable/blocked/risky |
| [G22] | [G23] | [G24] | [G25] | viable/blocked/risky |
| [G26] | ... | ... | ... | ... |
| Do nothing [G27] | — | — | [G28] | [acceptable/unacceptable] |

CRUX: [G34]
- Resolves by: [G37]

COMMITMENT CHAIN (what the want commits you to):
[List implications that must also be true — G-numbers]

FORECLOSURES (what the want forecloses):
[List what becomes impossible — G-numbers]

FIRST ACTIONS:
1. [action] — resolves: [G-numbers] — WHO: [Claude/user]
2. [action] — resolves: [G-numbers] — WHO: [Claude/user]
3. [action] — resolves: [G-numbers] — WHO: [Claude/user]

READY FOR:
- /foht [specific sub-goal where method is unknown]
- /ar [specific implication to trace deeper]
- /aw [specific commitment to stress-test — only if confidence is low]
- /qo [if the want involves writing/communication — find the question order]
```

---

## Depth Scaling

| Depth | Min Unbundled | Min Paths | Min Assumptions Tested | Min Total Findings |
|-------|-------------|-----------|----------------------|-------------------|
| 1x | 4 | 2 | 1 | 15 |
| 2x | 6 | 3 | 2 | 28 |
| 4x | 8 | 5 | 4 | 45 |
| 8x | 12 | 7 | 6 | 75 |

Default: 2x. These are floors.

---

## Anti-Failure Checks

| Failure Mode | Signal | Fix |
|-------------|--------|-----|
| **Taking the want at face value** | Jumping straight to methods for the stated want | Trace implications first. The actual want emerges from the commitment chain. |
| **No foreclosures** | Only listing what the want opens up | Every want also forecloses. Find what becomes impossible. |
| **Skipping prerequisites** | "Here's how to do it" without checking readiness | Every want has prerequisites. Surface them. |
| **No do-nothing path** | Missing the option of not pursuing the want | Always map what happens if the user does nothing. Sometimes it's fine. |
| **No unconventional path** | Every path is the obvious approach | At least one path should reframe the problem. |
| **Crux-free** | No crux identified | If there's no crux, either the want is trivial or you haven't dug deep enough. |
| **All paths viable** | Every path looks good | Find the costs and foreclosures. Every path gives something up. |

---

## Pre-Completion Check

- [ ] Want unbundled into desire, method, belief, assumption, implicit want, anti-want
- [ ] Implications traced (assume right — what does the want commit you to?)
- [ ] Actual want identified via implication chain (distinguished from stated want)
- [ ] Foreclosures identified (what the want makes impossible)
- [ ] Prerequisites surfaced with met/unmet/unknown status
- [ ] Blockers identified with removable/not assessment
- [ ] At least [depth minimum] paths mapped including do-nothing and unconventional
- [ ] Crux identified (or explicitly stated as absent with reasoning)
- [ ] ALL findings from Phase 1 in registry (none dropped)
- [ ] Synthesis introduces NO new findings
- [ ] First actions are specific and assigned (Claude or user)
- [ ] Output routes to appropriate next skill
