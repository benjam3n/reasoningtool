---
name: "systhink - Systems Thinking"
description: Analyze feedback loops, emergent behavior, system dynamics, stocks and flows, and leverage points. See the system, not just the parts.
output:
  format: "prose"
---

# Systems Thinking

**Input**: $ARGUMENTS

---

## Interpretations

Before executing, identify which interpretation matches the user's input:

**Interpretation 1 — Understand why a system behaves the way it does**: The user sees outcomes they did not design or intend and wants to understand the structural dynamics producing them — feedback loops, delays, accumulations.
**Interpretation 2 — Find leverage points**: The user wants to change a system's behavior and needs to identify where small interventions produce large effects — and where large interventions get absorbed.
**Interpretation 3 — Anticipate emergent behavior**: The user is designing, building, or modifying a system and wants to predict unintended consequences, oscillations, or perverse incentives before they manifest.

If ambiguous, ask: "I can help with understanding why a system behaves as it does, finding leverage points to change it, or anticipating emergent behavior from a design — which fits?"
If clear from context, proceed with the matching interpretation.

---

## Core Principles

1. **Structure drives behavior.** Systems produce outcomes because of their structure — feedback loops, delays, information flows — not because of the intentions of the people in them. If you do not like the behavior, change the structure, not the actors.

2. **Stocks change slowly; flows change fast.** Stocks (accumulated quantities — trust, inventory, debt, skill) are what give systems memory and inertia. You cannot change a stock instantly. Interventions that target flows instead of stocks get faster results but often miss the deeper dynamic.

3. **Delays are invisible causes.** When cause and effect are separated in time, people misattribute outcomes. Most policy oscillations — overbuilding then cutting, overhiring then firing — result from acting on delayed feedback as if it were current.

4. **Every balancing loop has a goal; every reinforcing loop has a direction.** Balancing loops resist change — find the implicit goal they are serving (even if nobody set it deliberately). Reinforcing loops amplify — find what they are amplifying and whether that acceleration is sustainable.

5. **The system will compensate.** Interventions that push against a balancing loop will be absorbed. The system finds another way to maintain its goal. Effective intervention works WITH the system's structure, not against it.

6. **Boundaries are choices, not facts.** Every system boundary you draw includes some things and excludes others. If your model cannot explain the behavior, your boundary is probably wrong — you are excluding a critical feedback loop.

---

## Phase 1: MAP — Identify System Structure

### Step 1: Define the System and Its Boundary

```
SYSTEM: [What system is being analyzed]
OBSERVED BEHAVIOR: [What the system is producing — the phenomenon that prompted analysis]
BOUNDARY: [What is inside the system, what is outside]
TIME HORIZON: [Over what period does the behavior manifest]
```

[S1] **Boundary check**: What have you excluded that might contain a feedback loop driving the behavior? If the system behavior cannot be explained by what is inside the boundary, expand it.

### Step 2: Identify Stocks and Flows

Stocks are accumulations — things that build up or drain over time. Flows are rates of change.

```
STOCKS (what accumulates):

[S2] Stock: [name]
  Current level: [high / medium / low / unknown]
  Inflows: [what adds to this stock]
  Outflows: [what drains this stock]
  Response time: [how fast does this stock change]

[S3] Stock: [name]
  Current level: [high / medium / low / unknown]
  Inflows: [what adds to this stock]
  Outflows: [what drains this stock]
  Response time: [how fast does this stock change]

[Continue for all significant stocks]
```

Check: Are there hidden stocks? Common invisible stocks include trust, technical debt, morale, institutional knowledge, backlog, and goodwill.

### Step 3: Map Feedback Loops

For each significant behavior, trace the causal loop:

```
FEEDBACK LOOPS:

[S4] Loop: [name]
  Type: [Reinforcing (R) / Balancing (B)]
  Mechanism: [A increases → B increases → C increases → A increases (R)]
             [A increases → B increases → C decreases → A decreases (B)]
  Speed: [Fast / Medium / Slow]
  Currently: [Dominant / Active / Dormant]
  Implicit goal (if B): [what level is this loop trying to maintain?]
  Direction (if R): [what is being amplified — growth, collapse, polarization?]

[S5] Loop: [name]
  Type: [R / B]
  Mechanism: [trace the chain]
  Speed: [Fast / Medium / Slow]
  Currently: [Dominant / Active / Dormant]

[Continue for all significant loops]
```

Rules:
- Count the negative links in each loop. Odd number = balancing. Even (or zero) = reinforcing.
- A system with only reinforcing loops will grow or collapse — look for the missing balancing loop
- A system that is stuck has a dominant balancing loop — find it

### Step 4: Identify Delays

```
DELAYS:

[S6] Delay: [between what cause and what effect]
  Duration: [approximate time lag]
  Consequence: [what behavior does this delay produce — oscillation, overshoot, misattribution?]
  Visibility: [is this delay visible to actors in the system?]

[Continue for all significant delays]
```

---

## Phase 2: ANALYZE — Understand the Dynamics

### Step 5: Explain the Observed Behavior

Using the map from Phase 1, explain WHY the system produces the behavior observed:

```
BEHAVIOR EXPLANATION:

[S7] The system produces [observed behavior] because:
  1. [Loop X] drives [what] — this is currently [dominant/active/dormant]
  2. [Stock Y] is [high/low/changing] because [inflow/outflow imbalance]
  3. [Delay Z] causes actors to [misattribute/overshoot/oscillate]
  4. [Boundary issue] means [external factor] is not being accounted for

KEY DYNAMIC: [The single most important structural explanation]
```

### Step 6: Identify System Archetypes

Check against common system archetypes:

| Archetype | Pattern | Signal |
|-----------|---------|--------|
| **Fixes that fail** | Quick fix creates side effects that worsen original problem | Problem keeps returning despite repeated fixes |
| **Shifting the burden** | Symptomatic solution undermines capacity for fundamental solution | Growing dependence on workaround; root capability atrophying |
| **Limits to growth** | Reinforcing loop hits a constraint that slows it | Growth that was exponential begins to plateau |
| **Tragedy of the commons** | Individual rational behavior depletes shared resource | Resource declining while each actor says "my share is small" |
| **Escalation** | Two parties each respond to the other's actions | Spending, effort, or hostility ratcheting upward |
| **Success to the successful** | Winner gets resources that ensure continued winning | Increasing inequality between two competing options |
| **Growth and underinvestment** | Growth strains capacity; instead of investing, quality drops | Demand growing, quality falling, demand eventually drops |
| **Eroding goals** | When performance gaps emerge, goals are lowered instead of performance raised | Standards quietly declining over time |

```
ARCHETYPE MATCH:

[S8] Archetype: [name]
  How it applies: [specific mapping to this system]
  Predicted trajectory: [what happens next if structure unchanged]
  Classic intervention: [what the archetype literature suggests]
```

---

## Phase 3: INTERVENE — Find Leverage Points

### Step 7: Identify Leverage Points

Rank potential interventions by leverage (Meadows' hierarchy, adapted):

| # | Level | Leverage | Question |
|---|-------|----------|----------|
| [S9] | Paradigm/mental model | HIGHEST | Is there a belief driving the system's design that could shift? |
| [S10] | System goal | VERY HIGH | What is the system optimizing for? Could the goal change? |
| [S11] | Loop structure | HIGH | Can a feedback loop be added, removed, or redirected? |
| [S12] | Information flow | MOD-HIGH | Is there information that exists but does not reach decision-makers? |
| [S13] | Rules and incentives | MODERATE | Do the rules reward the behavior you want? |
| [S14] | Stocks and flows | MOD-LOW | Can you change the rate of accumulation or depletion? |
| [S15] | Parameters | LOW | Can you adjust numbers — budgets, thresholds, targets? |

For each applicable level, provide: the specific intervention, its leverage assessment, and a concrete example in this system.

### Step 8: Evaluate Intervention Side Effects

For each proposed intervention, trace it through the system map:

```
INTERVENTION: [proposed change]

FIRST-ORDER EFFECT: [immediate intended result]
SECOND-ORDER EFFECT: [what that result causes through feedback loops]
THIRD-ORDER EFFECT: [what the second-order effect causes]
COMPENSATING RESPONSE: [how the system's balancing loops will resist this change]
DELAY RISK: [will delayed feedback make this look like it is working when it is not, or vice versa?]

NET ASSESSMENT: [After accounting for system response, will this intervention achieve its goal?]
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Linear thinking** | "If we do X, Y will happen" with no feedback consideration | Trace the causal chain back to the starting point. Does it loop? |
| **Event-level analysis** | Explaining behavior by pointing to a single event or actor | Ask: why did the structure allow this event to have this effect? |
| **Missing the balancing loop** | Confusion about why things are not changing despite effort | Find what goal the system is maintaining. What resists your push? |
| **Ignoring delays** | Surprise oscillations, overshoot, or "it worked then stopped" | Map time lags between cause and effect. Are actors seeing old data? |
| **Boundary error** | Model cannot explain the observed behavior | Expand boundary. What external loop are you missing? |
| **Leverage point inversion** | Spending maximum effort on parameter tweaks (budgets, headcount) | Move up the leverage hierarchy. Can you change goals, loops, or mental models instead? |

---

## Depth Scaling

Default: 2x. Parse depth from $ARGUMENTS if specified (e.g., "/systhink 4x [input]").

| Depth | Min Stocks | Min Feedback Loops | Min Delays | Min Leverage Points | Min Archetype Checks |
|-------|-----------|-------------------|------------|--------------------|-----------------------|
| 1x    | 2         | 2                 | 1          | 2                  | 2                     |
| 2x    | 4         | 3                 | 2          | 4                  | 4                     |
| 4x    | 6         | 5                 | 3          | 6                  | 6                     |
| 8x    | 10        | 8                 | 5          | 8                  | 8                     |

These are floors. Go deeper where insight is dense. Compress where it is not.

---

## Pre-Completion Checklist

- [ ] System boundary explicitly defined and checked for missing loops
- [ ] All significant stocks identified with inflows and outflows
- [ ] Feedback loops traced with type (R/B), speed, and dominance
- [ ] Delays mapped and their behavioral consequences stated
- [ ] Observed behavior explained by structure, not by events or actors
- [ ] At least one system archetype checked for fit
- [ ] Leverage points ranked from high to low, not just parameter-level fixes
- [ ] Intervention side effects traced through at least two orders of consequence
- [ ] Compensating responses from balancing loops anticipated

---

## Integration

- **Use from**: `/rca` (when root cause is structural, not event-level), `/fohw` (understanding how something works as a system), `/insd` (when inside-view misses structural dynamics)
- **Routes to**: `/prob` (when system behavior involves uncertain feedback), `/aex` (when assumptions about system structure need testing)
- **Differs from**: `/rca` traces backward from failure to cause; `/systhink` maps the ongoing structural dynamics that produce behavior patterns
- **Complementary**: `/fohw` (mechanistic understanding), `/insd` (revealing hidden structure), `/reframe` (changing which system you are looking at)
