---
name: sym
description: "Real problems exist in complex systems with many interacting parts. Comprehensive system modeling ontology."
---

# System Modeling

**Input**: $ARGUMENTS

---

## Overview

Real problems exist in complex systems with many interacting parts. This procedure provides a comprehensive ontology for modeling:
- Systems and their boundaries
- Stakeholders and their game-theoretic properties
- Environments and their characteristics
- Requirements and constraints
- Dynamics (feedback loops, equilibria, emergence)
- Epistemics (what we know vs assume)
- Failure modes and risk

Based on SEBOK (Systems Engineering Body of Knowledge) and INCOSE frameworks.

## Steps

### Step 1: Define System Boundaries
1. What is INSIDE the system? (Components, actors, processes)
2. What is OUTSIDE? (Environment, external forces)
3. What crosses the boundary? (Inputs, outputs, interfaces)
4. Where is the boundary ambiguous? (This is often where problems hide)

```
SYSTEM BOUNDARY:
Inside: [components]
Outside: [environment]
Inputs: [what enters]
Outputs: [what leaves]
Interfaces: [connection points]
Ambiguous: [unclear boundaries]
```

### Step 2: Map Components
For each major component:

| Component | Function | Inputs | Outputs | Dependencies | Failure Modes |
|-----------|----------|--------|---------|-------------|--------------|
| [name] | [what it does] | [needs] | [produces] | [depends on] | [how it breaks] |

### Step 3: Map Stakeholders
For each stakeholder:

| Stakeholder | Interest | Power | Information | Strategy |
|------------|---------|-------|------------|----------|
| [who] | [what they want] | [ability to influence] | [what they know] | [how they'll act] |

**Game-theoretic properties:**
- Are stakeholders cooperative or competitive?
- Are their interests aligned, opposed, or orthogonal?
- Can they observe each other's actions?
- Is this a one-shot or repeated interaction?
- What are each stakeholder's best alternatives (BATNA)?

### Step 4: Map Environment
External forces acting on the system:

| Force | Type | Predictability | Impact | Trend |
|-------|------|---------------|--------|-------|
| [force] | market/regulatory/technological/social/natural | H/M/L | H/M/L | [direction] |

### Step 5: Map Dynamics
How the system changes over time:

**Feedback loops:**
| Loop | Type | Components | Effect | Strength |
|------|------|-----------|--------|----------|
| [name] | reinforcing/balancing | [A→B→C→A] | [what it does] | H/M/L |

**Reinforcing loops** (positive feedback): Growth, escalation, collapse
- Example: More users → more content → more users

**Balancing loops** (negative feedback): Stability, regulation, homeostasis
- Example: More demand → higher prices → less demand

**Delays:**
Where cause and effect are separated in time:
| Action | Effect | Delay | Risk |
|--------|--------|-------|------|
| [action] | [consequence] | [time gap] | [what happens if you don't account for delay] |

**Emergent properties:**
What behaviors arise from the system that aren't properties of individual components?

### Step 6: Map Requirements and Constraints
| Requirement | Type | Source | Priority | Measurable? |
|------------|------|--------|----------|------------|
| [what must be true] | functional/performance/interface/constraint | [who requires it] | H/M/L | [how to measure] |

### Step 7: Epistemic Map
What we know vs what we assume:

| Element | Status | Confidence | How to Verify |
|---------|--------|-----------|--------------|
| [claim about system] | known/assumed/unknown | H/M/L | [method] |

### Step 8: Failure Mode Analysis
| Failure | Probability | Severity | Detection | Mitigation |
|---------|-------------|----------|-----------|-----------|
| [what could fail] | H/M/L | H/M/L | easy/hard | [prevention/response] |

### Step 9: Report
```
SYSTEM MODEL:
System: [name/description]
Boundary: [inside/outside]

Components: [N] — key: [most critical]
Stakeholders: [N] — key: [most influential]
Environment: [key forces]

Dynamics:
- Reinforcing loops: [list] — risk: [growth/collapse]
- Balancing loops: [list] — provides: [stability in what]
- Key delays: [list]
- Emergent properties: [list]

Requirements: [N total] — [N met] / [N unmet] / [N unknown]

Knowledge gaps:
1. [what we don't know but need to]

Top risks:
1. [failure mode] — probability × severity = [risk level]

Key insight: [the most important thing this model reveals]
```

## When to Use
- Analyzing complex problems
- Understanding system boundaries
- Modeling stakeholder dynamics
- Identifying failure modes
- Planning interventions in systems
- → INVOKE: /sya (systems analysis) for causal analysis
- → INVOKE: /lp (leverage points) for finding where to intervene
- → INVOKE: /de (dependency extraction) for mapping dependencies

## Verification
- [ ] System boundaries defined (inside/outside clear)
- [ ] All major components mapped with dependencies
- [ ] Stakeholders mapped with game-theoretic properties
- [ ] Feedback loops identified (reinforcing and balancing)
- [ ] Delays identified
- [ ] Epistemic status of key claims assessed
- [ ] Failure modes analyzed
