---
name: "tbd - To Be Determined"
description: "Identify unresolved decisions in any plan, document, or conversation, and convert each into an explicit determination question with type, owner, deadline, and cost of remaining unresolved."
output:
  format: "prose"
---

# TBD - To Be Determined

**Input**: $ARGUMENTS

---

## Core Principles

1. **TBD is a decision debt.** Every unresolved item blocks downstream work, creates ambiguity, or forces assumptions. The skill surfaces this debt and makes it explicit.

2. **Some TBDs are avoidance.** "TBD" is sometimes used to defer genuinely hard decisions that should be made now. Distinguishing premature decisions (legitimately TBD) from avoided decisions (should be resolved) is the key analytical move.

3. **A TBD without an owner never resolves.** Unowned decisions float indefinitely. Every TBD must have someone responsible for resolving it.

4. **A TBD without a deadline drifts.** Open-ended TBDs get resolved by accident or not at all. Even "by end of next sprint" is better than no deadline.

5. **Some TBDs should be killed.** Not every unresolved item needs a determination. Some should be cut (the question is irrelevant), some should be defaulted (pick the obvious answer), and some should be absorbed (make the design work regardless of the answer).

---

## Phase 1: TBD Identification

Scan the input for unresolved items. They appear as:

| Signal | Example |
|--------|---------|
| Explicit TBD markers | "TBD", "TODO", "to be decided", "not yet determined" |
| Questions without answers | "Which database should we use?" |
| Conditional statements | "If we decide to go with X..." |
| Vague placeholders | "[insert value]", "something like...", "approximately..." |
| Hedged commitments | "We'll probably...", "We might...", "Depending on..." |
| Missing sections | Gap in a plan where a decision should be |

```
[T1] TBD_1: [what's unresolved] — SOURCE: [where found — explicit marker, question, hedge, gap]
[T2] TBD_2: [what's unresolved] — SOURCE: [where found]
...
[T-N] TBD_COUNT: [N items found]
```

---

## Phase 2: TBD Classification

For each TBD:

```
[T-N] TBD: [description]
  TYPE: [decision | information | dependency | design | resource | scope]
  STATUS: [legitimately premature | avoidance | defaultable | killable]
  BLOCKING: [what downstream work is blocked by this TBD]
  COST_OF_DELAY: [low | medium | high — what happens if this stays TBD longer]
```

### Status Definitions

| Status | Meaning | Action |
|--------|---------|--------|
| **Legitimately premature** | Information genuinely not available yet | Set deadline; define what triggers resolution |
| **Avoidance** | Decision is hard or uncomfortable but information exists | Resolve NOW — this is costing time |
| **Defaultable** | An obvious default exists; the TBD is unnecessary | Apply default; note it can be revisited |
| **Killable** | The question is irrelevant to the goal | Remove the TBD entirely |

---

## Phase 3: Resolution Specification

For each TBD that should be resolved (not killed or defaulted):

```
[T-N] DETERMINATION QUESTION: [the specific question that needs answering]
  DECISION_TYPE: [binary (yes/no) | selection (pick from options) | value (determine a parameter) | design (create a solution)]
  OPTIONS: [known options, if any]
  INFORMATION_NEEDED: [what would resolve this]
  OWNER: [who should resolve this — person/role]
  DEADLINE: [when this must be resolved]
  RESOLUTION_METHOD: [how to decide — research, meeting, experiment, user test]
  DEFAULT_IF_MISSED: [what happens if the deadline passes without resolution]
```

---

## Phase 4: Output

```
TBD INVENTORY
=============

SOURCE: [what was scanned]
TOTAL TBDs: [N]

RESOLVE NOW (avoidance — information exists):
  1. [TBD] — QUESTION: [specific question]
     BLOCKING: [what's blocked]
     OWNER: [who] — DEADLINE: [when]
     → INVOKE: /decide [if binary/selection] or /how [if method needed]

RESOLVE SOON (legitimate — not yet answerable):
  2. [TBD] — QUESTION: [specific question]
     TRIGGERS_RESOLUTION: [what event makes this answerable]
     OWNER: [who] — DEADLINE: [when]

DEFAULT (obvious answer exists):
  3. [TBD] — DEFAULT: [the obvious answer]
     RATIONALE: [why this default is safe]
     REVISIT_IF: [what would make the default wrong]

KILL (irrelevant):
  4. [TBD] — WHY_IRRELEVANT: [reason this doesn't need resolving]

READY FOR:
- /tobd — to sequence TBDs by dependency for operational resolution
- /decide [specific TBD] — to resolve a specific decision
- /nsa [uncertain TBD] — to analyze the uncertainty
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Avoidance not detected** | All TBDs classified as "legitimately premature" | Ask: does the information exist? If yes, it's avoidance |
| **No owners** | TBDs listed without responsibility assignment | Every TBD needs an owner, even if it's "the user" |
| **No deadlines** | TBDs listed without time constraint | Every TBD needs a deadline, even if approximate |
| **Killable items kept** | Irrelevant TBDs kept on the list | If a TBD doesn't affect the goal, kill it |
| **Missing implicit TBDs** | Only explicit "TBD" markers found | Also check for hedges, conditionals, gaps, and vague placeholders |
| **No blocking analysis** | TBDs listed without downstream impact | Each TBD should show what work it blocks |

---

## Depth Scaling

| Depth | Scan Thoroughness | Classification | Resolution Detail | Blocking Analysis |
|-------|------------------|---------------|------------------|------------------|
| 1x | Explicit markers only | Type only | Question + owner | What's blocked |
| 2x | Markers + questions + hedges | Type + status | Full specification | What's blocked + cost of delay |
| 4x | All signals including gaps | Full + avoidance detection | Full + resolution method | Dependency chain impact |
| 8x | Full + cross-reference | Full + root cause of each TBD | Full + options analysis | System-wide impact map |

Default: 2x. These are floors.

---

## Pre-Completion Checklist

- [ ] All TBD signals scanned (not just explicit markers)
- [ ] Each TBD classified by type and status
- [ ] Avoidance vs legitimate premature distinguished
- [ ] Defaultable and killable TBDs identified
- [ ] Every resolve-worthy TBD has a specific question
- [ ] Every TBD has an owner and deadline
- [ ] Blocking downstream work identified for each TBD
- [ ] Cost of delay assessed

---

## Integration

- Use before: `/tobd` (to sequence TBDs for operational resolution)
- Complementary: `/decide` (to resolve specific decision TBDs)
- Complementary: `/nsa` (to analyze uncertain TBDs)
- Differs from `/tobd`: tbd identifies and classifies; tobd sequences for resolution
- Use from: project reviews, plan audits, document reviews
