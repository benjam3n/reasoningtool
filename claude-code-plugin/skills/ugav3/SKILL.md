---
name: "ugav3 - Universal Goal Analysis v3 (Decomposed Sub-Procedures)"
description: "Goal analysis with fully decomposed sub-procedures. Every analysis step is broken into atomic operations that can be followed mechanically. Consolidated into /uga but usable standalone for procedural goal decomposition."
tier: "tier4"
categories: ["Goal Processing"]
tags: ["goal", "decomposition", "procedures", "systematic"]
---

# Universal Goal Analysis v3: Fully Decomposed Sub-Procedures

**Input**: $ARGUMENTS

---

## Core Principles

1. **Every step must be atomic.** If a step says "analyze the situation," it is not decomposed. An atomic step produces exactly one output from exactly one operation. "Count the constraints" is atomic. "Understand the problem" is not.

2. **Sub-procedures are reusable.** Each decomposed procedure should work independently. If you extract the "requirement tracing" sub-procedure and run it on a different goal, it should still produce valid output.

3. **Outputs chain into inputs.** The output of Step N must be explicitly named and referenced as input to Step N+1. No implicit state. If a later step needs something from an earlier step, it must say "[uses output from Phase 2, finding E]."

4. **Ambiguity means missing decomposition.** If an executor could interpret a step two different ways and get two different outputs, the step needs further decomposition. The test: could two different people follow this and produce the same structure?

5. **Decomposition has a stopping condition.** Stop decomposing when the step produces a single, verifiable output (a number, a list, a yes/no, a ranking). If the output is a paragraph of prose, decompose further.

---

## Phase 1: Goal Registration

Register the goal with structured fields.

```
[A] RAW_INPUT: [verbatim from user]
[B] GOAL_STATEMENT: [rewrite as: "Achieve [outcome] by [deadline or 'no deadline'] using [resources or 'unspecified']"]
[C] GOAL_TYPE: [classify: achieve / prevent / maintain / discover / decide]
[D] SCOPE: [individual / team / organization / system]
```

**Sub-procedure — Goal Statement Rewrite:**
1. Identify the verb (what action?)
2. Identify the object (what changes?)
3. Identify the constraint (by when? with what?)
4. Assemble: "[verb] [object] [constraint]"
5. Verify: does the rewrite preserve the original meaning? [Y/N]

---

## Phase 2: Requirement Decomposition

**Sub-procedure — Recursive Requirement Tracing:**

```
[E] REQUIREMENTS_TREE:

Step 1: List what the goal directly requires (R1, R2, R3...)
Step 2: For each R, ask: "What does THIS require?" → list sub-requirements
Step 3: For each sub-requirement, ask: "Do I have this?" → Y/N
Step 4: If N, ask: "What would it cost to get?" → time, money, effort
Step 5: If Y, ask: "Am I sure?" → evidence?
Step 6: Stop when every leaf is either HAVE or NEED_WITH_COST

Goal
├── R1: [requirement]
│   ├── R1.1: [sub-req] — have: [Y/N] — cost: [X] — evidence: [what]
│   └── R1.2: [sub-req] — have: [Y/N] — cost: [X] — evidence: [what]
├── R2: [requirement]
│   └── R2.1: [sub-req] — have: [Y/N] — cost: [X] — evidence: [what]
└── R3: [requirement]
    ├── R3.1: [sub-req] — have: [Y/N] — cost: [X] — evidence: [what]
    └── R3.2: [sub-req] — have: [Y/N] — cost: [X] — evidence: [what]
```

---

## Phase 3: Gap Identification

**Sub-procedure — Gap Extraction:**

```
[F] GAPS:

Step 1: Collect all leaves where have = N → these are gaps
Step 2: For each gap, classify:
    - SKILL_GAP: need capability that doesn't exist yet
    - RESOURCE_GAP: need money/time/people that aren't available
    - KNOWLEDGE_GAP: need information that isn't known
    - ACCESS_GAP: need permission/connection that isn't granted
    - DEPENDENCY_GAP: need someone else to act first
Step 3: For each gap, estimate:
    - Closability: [easy / hard / uncertain / impossible]
    - Criticality: [blocking / degrading / cosmetic]
    - Timeline: [hours / days / weeks / months]

[G] GAP_SUMMARY:
    Total gaps: [N]
    Blocking gaps: [list]
    Easiest to close: [list]
    Hardest to close: [list]
```

---

## Phase 4: Strategy Assembly

**Sub-procedure — Strategy Construction:**

```
[H] STRATEGY:

Step 1: Order gaps by criticality (blocking first)
Step 2: For each blocking gap:
    a. List possible approaches to close it (minimum 2)
    b. For each approach: effort [H/M/L], risk [H/M/L], speed [H/M/L]
    c. Select approach with best effort-to-risk ratio
Step 3: Sequence selected approaches into a timeline
Step 4: Identify parallel tracks (gaps that can be closed simultaneously)
Step 5: Identify serial dependencies (gap B can't close until gap A closes)

[I] EXECUTION_SEQUENCE:
    Track 1: [gap] → [approach] → [timeline]
    Track 2: [gap] → [approach] → [timeline]
    Dependencies: [Track X blocks Track Y at step Z]
```

---

## Phase 5: Validation

**Sub-procedure — Strategy Validation:**

```
[J] VALIDATION:

Step 1: For each approach in the strategy, ask:
    - What assumption does this approach rest on? [state it]
    - Is this assumption tested? [Y/N]
    - If N: what's the cost of being wrong? [state it]
Step 2: Count untested assumptions
Step 3: If untested assumptions > 3:
    → Flag strategy as HIGH UNCERTAINTY
    → Recommend testing top assumption before execution
Step 4: Verify coverage:
    - Every blocking gap has an approach? [Y/N]
    - Every approach has a timeline? [Y/N]
    - All dependencies identified? [Y/N]
```

---

## Phase 6: Report

```
UGA v3 DECOMPOSED ANALYSIS:
Goal: [goal statement from Phase 1]
Type: [goal type] | Scope: [scope]

Requirements tree: [N] requirements, [M] sub-requirements
Gaps found: [X] total, [Y] blocking

Blocking gaps:
1. [gap] — type: [type] — closability: [X] — approach: [approach]
2. [gap] — type: [type] — closability: [X] — approach: [approach]

Execution sequence:
  Track 1: [steps with timeline]
  Track 2: [steps with timeline]
  Dependencies: [what blocks what]

Uncertainty: [LOW/MEDIUM/HIGH] — untested assumptions: [N]
Top untested assumption: [what it is]
Recommended first action: [specific atomic action]
```

→ INVOKE: /uga $ARGUMENTS (for full analysis incorporating decomposed findings)

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Non-atomic steps** | Step says "analyze" or "understand" or "consider" | Decompose until output is a single verifiable artifact |
| **Implicit state** | Later step uses information not explicitly traced to earlier output | Add explicit "[uses finding X from Phase N]" |
| **Infinite decomposition** | Sub-procedures decompose past the point of usefulness | Stop when output is a number, list, Y/N, or ranking |
| **Missing gaps** | Requirement tree has no N leaves (everything assumed available) | Challenge: for each "have: Y", demand evidence |
| **Single-approach strategies** | Each gap has only one proposed approach | Require minimum 2 approaches per blocking gap |
| **Untested confidence** | Strategy proceeds despite HIGH UNCERTAINTY | Block execution until top assumption is tested |

---

## Depth Scaling

| Depth | Decomposition | Gaps | Strategy |
|-------|--------------|------|----------|
| 1x | 2 levels deep on requirement tree | List blocking gaps only | Single approach per gap |
| 2x | 3 levels deep, evidence required for "have: Y" | Classify and score all gaps | 2+ approaches per blocking gap |
| 4x | Full tree until all leaves are atomic | Gap dependency analysis | Parallel/serial timeline with contingencies |
| 8x | Full tree + cross-requirement interaction analysis | Gap interaction matrix | Multi-scenario strategy with fallbacks |

Default: 2x. These are floors.

---

## Pre-Completion Checklist

- [ ] Goal registered with type, scope, and rewritten statement
- [ ] Requirement tree decomposed to leaves with have/cost for each
- [ ] All gaps extracted, classified, and scored
- [ ] Blocking gaps each have 2+ approaches
- [ ] Execution sequence shows parallel tracks and dependencies
- [ ] Untested assumptions counted and top assumption identified
- [ ] Report includes specific first action (not vague next step)

---

## Integration

- **Consolidated into**: `/uga` (which uses v3's decomposition approach in Steps 3-5)
- **Use standalone when**: You need mechanical, reproducible goal decomposition
- **Routes to**: `/uga` (full analysis), `/gd` (goal decomposition), `/dcm` (decomposition)
- **Invoked by**: Users wanting step-by-step procedural analysis
- **Differs from /uga**: /uga runs all 17 steps; ugav3 focuses on making every step atomic and traceable
- **Differs from /gd**: /gd decomposes the goal itself; ugav3 decomposes the analysis procedure
- **Differs from /ugav2**: ugav2 focuses on questions; ugav3 focuses on procedural decomposition
