---
name: "cmplx - Complex Analysis"
description: "Framework for genuinely complex problems that resist simple answers. Identify sources of complexity, choose appropriate tools, decompose without oversimplifying, and synthesize."
output:
  format: "prose"
---

# CMPLX - Complex Analysis

**Input**: $ARGUMENTS

---

## Step 1: Identify Why This Is Complex

```
PROBLEM: [statement of the problem]

COMPLEXITY SOURCES (check all that apply):
  [ ] MANY VARIABLES: [list the key variables]
  [ ] FEEDBACK LOOPS: [describe circular causation]
  [ ] UNCERTAINTY: [what's unknown and how much it matters]
  [ ] CONFLICTING STAKEHOLDERS: [who wants what, and how do they clash]
  [ ] EMERGENT BEHAVIOR: [outcomes that can't be predicted from parts]
  [ ] NONLINEARITY: [small changes produce disproportionate effects]
  [ ] TIME DYNAMICS: [behavior changes depending on timescale]
  [ ] MEASUREMENT DIFFICULTY: [key factors are hard to observe]

PRIMARY COMPLEXITY: [the dominant source of complexity]
```

Name the complexity. "It's complicated" is not analysis. Identifying WHICH KIND of complicated determines which tools to use.

---

## Step 2: Choose Complexity-Handling Tools

Based on the complexity sources identified:

```
SELECTED APPROACHES:
  FOR [complexity source]: USE [approach]
    - Many variables → decomposition, sensitivity analysis
    - Feedback loops → systems mapping (/sysk), causal loop diagrams
    - Uncertainty → scenario planning, probabilistic reasoning
    - Conflicting stakeholders → multi-perspective analysis, trade-off mapping
    - Emergent behavior → simulation thinking, agent-based reasoning
    - Nonlinearity → threshold identification, regime analysis
    - Time dynamics → temporal decomposition, phase analysis
    - Measurement difficulty → proxy identification, triangulation

PRIMARY TOOL: [the main analytical approach]
SUPPORTING TOOLS: [secondary approaches]
```

---

## Step 3: Decompose Without Oversimplifying

```
DECOMPOSITION:
  PART 1: [sub-problem]
    SELF-CONTAINED: [yes | no — does it interact with other parts?]
    INTERACTIONS: [which other parts it affects and how]
  PART 2: [sub-problem]
    SELF-CONTAINED: [yes | no]
    INTERACTIONS: [cross-part effects]
  PART 3: [sub-problem]
    SELF-CONTAINED: [yes | no]
    INTERACTIONS: [cross-part effects]

INTERACTIONS MAP:
  [Part 1] ←→ [Part 2]: [how they influence each other]
  [Part 2] ←→ [Part 3]: [interaction]
  [Part 1] ←→ [Part 3]: [interaction]

DECOMPOSITION RISK: [what do you lose by analyzing parts separately?]
```

The risk of decomposition is losing interactions. Always map the interactions explicitly, and check whether analyzing parts separately would miss something critical.

---

## Step 4: Maintain Awareness of Interactions

```
CROSS-CUTTING CONCERNS:
  1. [factor that affects multiple parts]
     PARTS AFFECTED: [list]
     MECHANISM: [how it crosses boundaries]
  2. [factor]
     PARTS AFFECTED: [list]
     MECHANISM: [how]

SECOND-ORDER EFFECTS:
  IF [action on Part 1] THEN [effect on Part 2] THEN [effect on Part 3]
  IF [action on Part 2] THEN [effect on Part 1] THEN [cascade]
```

This is where complexity analysis earns its keep. Simple analysis misses these interactions. Complex analysis tracks them.

---

## Step 5: Synthesize

```
SYNTHESIS
=========
PROBLEM: [restate]
COMPLEXITY TYPE: [primary source]

ANALYSIS:
  1. [key finding from Part 1]
  2. [key finding from Part 2]
  3. [key finding from Part 3]

INTERACTIONS THAT MATTER:
  1. [critical interaction between parts]
  2. [critical interaction]

WHAT SIMPLE ANALYSIS WOULD MISS:
  [the specific insight that only emerges from tracking complexity]

RECOMMENDATIONS:
  1. [action] — ACCOUNTS FOR: [which complexity source]
  2. [action] — ACCOUNTS FOR: [which complexity source]

REMAINING UNCERTAINTY:
  [what's still unclear and how to make progress on it]

CONFIDENCE: [high | medium | low]
  WHY: [what drives the confidence level]
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Fake complexity** | Problem is actually simple | Use `/smpl` — not everything deserves this framework |
| **Decompose and forget** | Parts analyzed in isolation, interactions ignored | Step 4 exists specifically to prevent this |
| **Complexity paralysis** | Analysis never reaches conclusions | Set a stopping point — perfect analysis of complex systems is impossible |
| **Tool mismatch** | Using simple tools on complex problems | Match the tool to the complexity type from Step 2 |
| **Missing the dominant source** | All complexity sources treated equally | One source is usually primary — focus there |

---

## Integration

- Opposite of: `/smpl` (use smpl when cmplx is overkill)
- Use with: `/sysk` when feedback loops are the primary complexity source
- Use with: `/dtsk` when uncertainty can be reduced with data
- Use from: `/analyze` when the router detects genuine complexity
- Escalate to: `/certainty` when maximum rigor is required
