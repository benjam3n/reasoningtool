---
name: "sysk - Systems Analysis"
description: "Analyze any system by mapping components, connections, feedback loops, leverage points, and emergent behaviors."
output:
  format: "prose"
---

# SYSK - Systems Analysis

**Input**: $ARGUMENTS

---

## Step 1: Identify Components

```
SYSTEM: [name or description of the system]
BOUNDARY: [what's inside vs outside the system]

COMPONENTS:
  1. [component] — ROLE: [what it does in the system]
  2. [component] — ROLE: [function]
  3. [component] — ROLE: [function]
  ...
```

Be explicit about the system boundary. Everything outside the boundary is environment. Everything inside is what you're analyzing.

---

## Step 2: Map Connections

For each significant connection between components:

```
CONNECTION: [component A] → [component B]
  TYPE: [information | material | energy | influence | dependency]
  DIRECTION: [one-way | bidirectional]
  STRENGTH: [strong | moderate | weak]
  WHAT FLOWS: [what specifically moves along this connection]
```

Draw the full connection map. Components without connections to anything else are either misidentified or the connection is hidden.

---

## Step 3: Find Feedback Loops

```
REINFORCING LOOP (more produces more):
  [A] increases → [B] increases → [C] increases → [A] increases
  EFFECT: [what this loop amplifies — growth or decline]
  SPEED: [fast | slow | variable]

BALANCING LOOP (maintains equilibrium):
  [A] increases → [B] increases → [A] decreases
  EFFECT: [what this loop stabilizes]
  SET POINT: [what level it maintains, if identifiable]
```

Every stable system has at least one balancing loop. Every growing or collapsing system has a dominant reinforcing loop.

---

## Step 4: Identify Leverage Points

Ranked from least to most powerful:

```
LEVERAGE POINTS:
  1. [point] — TYPE: [parameter | buffer | flow | rule | goal | paradigm]
     EFFECT OF CHANGE: [what happens if you intervene here]
     EFFORT REQUIRED: [low | medium | high]
     IMPACT EXPECTED: [low | medium | high]
  2. [point] — TYPE: [...]
     EFFECT OF CHANGE: [...]
```

The best leverage points produce large effects with small inputs. They are often counterintuitive — not where most people would intervene.

---

## Step 5: Assess Stability

```
STABILITY ASSESSMENT:
  CURRENT STATE: [stable | unstable | oscillating | transitioning]
  RESILIENCE: [high | medium | low] — can it absorb shocks and return to function?
  ADAPTABILITY: [high | medium | low] — can it change in response to new conditions?
  KEY VULNERABILITIES: [what could break the system]
  SINGLE POINTS OF FAILURE: [components whose removal collapses the system]
```

---

## Step 6: Find Bottlenecks

```
BOTTLENECK: [component or connection that constrains the whole system]
  EVIDENCE: [how you know this is the constraint]
  CURRENT THROUGHPUT: [what it handles now]
  SYSTEM DEMAND: [what the rest of the system needs from it]
  GAP: [difference between throughput and demand]
  RELIEF OPTIONS: [how to widen the bottleneck]
```

A system's overall performance is limited by its tightest bottleneck. Optimizing non-bottleneck components wastes effort.

---

## Step 7: Identify Emergent Behaviors

```
EMERGENT BEHAVIOR: [behavior that arises from interactions, not from any single component]
  PRODUCED BY: [which interactions create this]
  PREDICTABLE: [yes | no | partially]
  DESIRABLE: [yes | no | mixed]
  CONTROL MECHANISM: [how to amplify or dampen this behavior]
```

Emergence is the whole point of systems analysis. If you could understand the system by looking at parts individually, you wouldn't need this skill.

---

## Output Summary

```
SYSTEM MAP
==========
SYSTEM: [name]
COMPONENTS: [count] identified
KEY CONNECTIONS: [most important flows]
FEEDBACK LOOPS: [reinforcing and balancing]
LEVERAGE POINTS: [top 2-3 intervention points]
BOTTLENECKS: [primary constraints]
EMERGENT BEHAVIORS: [what the system produces that parts don't]
STABILITY: [assessment]
RECOMMENDATION: [where to intervene and why]
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Too many components** | List exceeds 15 items | Aggregate into subsystems |
| **Missing feedback loops** | Only linear chains found | Every stable system has loops — look harder |
| **Ignoring delays** | Assuming instant cause-effect | Add time delays to connections |
| **Boundary confusion** | Analyzing things outside the system | Redefine the boundary explicitly |
| **Static snapshot** | No sense of how the system changes over time | Add temporal dimension to each loop |

---

## Integration

- Use with: `/rlsk` to analyze relationship dynamics within the system
- Use with: `/cmplx` when the system resists simple decomposition
- Use with: `/gflr` to find missing components in the system
- Use from: `/diagnose` when the problem is systemic, not isolated
- Differs from `/rlsk`: sysk maps structural dynamics; rlsk focuses on interpersonal needs
