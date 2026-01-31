---
name: pag
description: "Handler for goals with inherent tensions where optimizing one dimension seems to harm another."
---

# Paradox and Trade-off Goals Handler

**Input**: $ARGUMENTS

---

## Overview

Handler for goals with inherent tensions where optimizing one dimension seems to harm another. These are NOT either/or choices — they're both/and challenges. The goal is to find the non-obvious path that satisfies both constraints.

Examples: "Scale without losing quality," "Move fast AND be careful," "Grow revenue while maintaining values."

## Steps

### Step 1: Identify the Tension
1. What are the two (or more) dimensions in tension?
2. State each dimension as a goal:
   - Dimension A: [maximize/maintain X]
   - Dimension B: [maximize/maintain Y]
3. Why do these seem to conflict? What's the assumed tradeoff?

### Step 2: Map the Trade-off Space

```
        HIGH [Dimension A]
              |
  "A without B" |  "BOTH A and B"
  (common but   |  (the target)
   unsatisfying) |
              |
LOW [Dim B] ---+--- HIGH [Dimension B]
              |
  "NEITHER"    |  "B without A"
  (failure)    |  (common but
              |   unsatisfying)
              |
        LOW [Dimension A]
```

Where are you now? Where do you want to be?
The goal is the top-right quadrant: BOTH dimensions high.

### Step 3: Challenge the Trade-off
Is the trade-off actually necessary?

**False dichotomy check:**
1. Is there evidence of anyone achieving both? (If yes, it's possible)
2. Is the trade-off based on an ASSUMPTION you haven't tested?
3. Is the trade-off real at CURRENT scale but dissolves at different scale?
4. Is the trade-off real in CURRENT approach but not in alternative approaches?

**Common false trade-offs:**
| Seems like... | But actually... |
|--------------|----------------|
| Speed vs quality | Speed AND quality improve with better systems |
| Growth vs culture | Growth WITH culture requires intentional hiring |
| Innovation vs stability | Innovation IN stable areas, stability IN core |
| Freedom vs accountability | Freedom WITH accountability = ownership |

### Step 4: Find Resolution Strategies
Six ways to resolve paradox goals:

**Strategy 1: Temporal separation**
- Do A first, then B. Alternate in cycles.
- "Sprint fast, then consolidate. Sprint fast, then consolidate."

**Strategy 2: Spatial separation**
- Do A in one area, B in another.
- "Innovate in the lab, stabilize in production."

**Strategy 3: Level separation**
- Do A at one level of abstraction, B at another.
- "Be rigid on principles, flexible on tactics."

**Strategy 4: Synthesis**
- Find an approach that IS both A and B simultaneously.
- "Automated testing = moving fast AND being careful."

**Strategy 5: Reframe**
- Redefine what A or B means to dissolve the tension.
- "Quality" doesn't mean "perfection" — it means "fit for purpose."

**Strategy 6: Sequence with ratchet**
- Advance A, then lock it in. Advance B, then lock it in. Each locks enable the next.
- "Grow revenue (lock: hire). Improve culture (lock: values). Grow revenue (lock: hire)."

### Step 5: Design the Resolution

For the best resolution strategy:
1. What specific actions implement this?
2. What would success look like? (Both dimensions measured)
3. What early warning tells you one dimension is suffering?
4. What's the rebalancing mechanism when things drift?

```
RESOLUTION DESIGN:
Strategy: [which resolution type]
Dimension A actions: [how to advance A]
Dimension B actions: [how to advance B]
Integration mechanism: [how they work together]

Monitoring:
- Dimension A indicator: [what to measure]
- Dimension B indicator: [what to measure]
- Drift alarm: [when to rebalance]
```

### Step 6: Set Minimum Thresholds
Each dimension has a floor below which you will not go:

| Dimension | Floor (never below this) | Target | Current |
|-----------|------------------------|--------|---------|
| A: [name] | [minimum acceptable] | [goal] | [now] |
| B: [name] | [minimum acceptable] | [goal] | [now] |

Rule: If either dimension hits the floor, STOP advancing the other and rebalance.

### Step 7: Report
```
PARADOX GOAL RESOLUTION:
Tension: [Dimension A] vs [Dimension B]
Current state: [where you are in the trade-off space]

Trade-off validity: [real / false / contextual]
Resolution strategy: [temporal/spatial/level/synthesis/reframe/ratchet]

Plan:
[specific actions that advance both dimensions]

Monitoring:
- A indicator: [metric] — floor: [minimum] — target: [goal]
- B indicator: [metric] — floor: [minimum] — target: [goal]
- Rebalance trigger: [when to course-correct]

Key insight: [what makes both achievable]
```

## When to Use
- Goal contains "but", "while", "without losing", "and also"
- Two dimensions that seem to trade off
- Feeling forced to choose between things you want
- Standard optimization sacrifices something important
- → INVOKE: /tnt (tension navigation tactics) for specific tactics
- → INVOKE: /vcd (value conflict decomposition) for deep conflict analysis

## Verification
- [ ] Both dimensions explicitly named
- [ ] Trade-off challenged (not assumed necessary)
- [ ] Resolution strategy selected from the six types
- [ ] Both dimensions have measurable indicators
- [ ] Minimum thresholds set for each dimension
- [ ] Rebalancing mechanism defined
