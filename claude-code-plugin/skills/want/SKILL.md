---
name: "want - Clarify a Goal"
description: Sub-orchestrator for goals and wants. Routes to WantTo analysis to trace what the want commits you to and find the actual want.
---

# Want

**Input**: $ARGUMENTS

---

## Interpretations

Before executing, identify which interpretation matches the user's input:

**Interpretation 1 — Surface want**: The user states something they want ("I want to X") and needs help uncovering whether this is the real want or a proxy for something deeper.
**Interpretation 2 — Aspirational want**: The user describes a vague aspiration ("I want to be happy", "I want financial freedom") that needs concretizing before it can be acted on.
**Interpretation 3 — Embedded decision**: The user says "I want X" but there's a hidden choice ("I want X but maybe Y") — this is actually a decision disguised as a want.

If ambiguous, ask: "I can help with tracing a specific want to its root, concretizing a vague aspiration, or untangling a hidden choice — which fits?"
If clear from context, proceed with the matching interpretation.

---

## Core Principles

1. **The stated want is never the actual want.** "I want to quit my job" means "I want what my job prevents." The first statement is the starting point, not the answer. Always go at least one layer deeper.

2. **Wants bundle desires, methods, beliefs, and assumptions.** "I want to start a startup" bundles the desire (autonomy, wealth), the method (startup specifically), the belief (this is the best path), and the assumption (I can pull it off). Unbundling reveals the real want.

3. **Every want forecloses.** Wanting X means not-wanting everything X excludes. The foreclosures are often more revealing than the want itself. Someone who wants to "move to the countryside" is also saying they don't want whatever the city represents to them.

4. **Proxy wants feel urgent but don't satisfy.** If achieving the stated want wouldn't actually resolve the underlying need, it's a proxy. Test: "If you got exactly this, would you be done?" If the answer is "well, not exactly," you have a proxy.

5. **Actionable wants have verbs; aspirational wants have adjectives.** "Launch by Q3" is actionable. "Be successful" is aspirational. Aspirational wants must be converted to actionable wants before they can be pursued.

6. **The anti-want reveals the real want.** What does the user NOT want? The thing they're running from often defines the want more precisely than the thing they're running toward.

---

## Routing Decisions

### 1. Extract the Want

What does the user want? State it in their words. "I want to X" / "I need to X" / "My goal is X" / sometimes just a noun ("career change", "startup").

### 2. Is This Actually a Goal?

- **"Should I X?"** → This is a decision. → INVOKE: /decide $ARGUMENTS
- **"X is true"** → This is a claim. → INVOKE: /claim $ARGUMENTS
- **"How do I X?"** → They already know the goal, they need the method. → INVOKE: /how $ARGUMENTS
- **"I'm frustrated about X"** → This is emotional. → INVOKE: /emotion $ARGUMENTS
- **"What about X?"** → This is an idea. → INVOKE: /viability $ARGUMENTS
- **"Analyze X"** → This is analysis. → INVOKE: /analyze $ARGUMENTS
- **"Review my X"** → This is evaluation. → INVOKE: /evaluate $ARGUMENTS
- **"I think I want X"** (tentative) → Formalize the belief. → INVOKE: /it $ARGUMENTS
- **"I want X, but Y"** (goal with obstacle) → Separate the tension. → INVOKE: /but $ARGUMENTS
- **"I'm not sure what I want"** → Classify the uncertainty. → INVOKE: /nsa $ARGUMENTS
- **"Handle this"** (vague) → INVOKE: /handle $ARGUMENTS
- **If it IS a goal/want** → continue.

### 3. Is This the Real Want or a Proxy?

The stated want is almost never the actual want. "I want to quit my job" means "I want what my job prevents." The /wt skill traces this by assuming the want is right and following implications.

Apply the proxy test: "If you got exactly this tomorrow, would you be satisfied?" If the answer would be qualified, the want is a proxy.

Always go deeper. The first stated want is the starting point, not the answer.

### 4. Is This a Goal or a Decision?

- **Single direction** ("I want X"): this is a goal. Proceed.
- **Choice embedded** ("I want X but maybe Y"): this is a decision.
  → INVOKE: /decide $ARGUMENTS

### 5. Actionable or Aspirational?

- **Actionable** ("I want to launch by Q3", "I need to hire 3 engineers"): /wt will produce paths and first actions → then /how for the method → then /action for execution.
- **Aspirational** ("I want to be happy", "I want financial freedom"): /wt will trace what this means concretely → then /want again on the concrete version.
- **Platitude-shaped** ("I want to live my best life", "I want to follow my passion"): operationalize first.
  → INVOKE: /platitude $ARGUMENTS — then /want on the operationalized version.

### 6. Goal Quality Check

Before deep analysis, check the goal itself:

| Situation | Also invoke |
|-----------|------------|
| Goal seems obviously good — check | → /obv (obvious check) |
| Goal has obvious bad outcomes | → /obo (obvious bad outcomes) |
| Goal has obvious good outcomes being missed | → /ogo (obvious good outcomes) |
| Goal involves ethical dimensions | → /eth (ethics analysis) |
| Goal might be based on self-deception | → /sdc (self-deception check) |
| User might be in wrong situation entirely | → /sid (situation identification) |
| User might have wrong mental model of what they want | → /rmm (recover from wrong mental model) |

### 7. Scope and Limits

- **User is expanding scope** ("and also I want Y and Z..."): → INVOKE: /iagca to compress.
- **User wants to know their current limits**: → INVOKE: /awtlytrn $ARGUMENTS
- **User keeps finding more wants** ("and also..."): → INVOKE: /ycshikfmif to structure the expansion.
- **Goal has "etc" or implied scope**: → INVOKE: /etc or /aso to expand explicitly.

### 8. Depth and Mode Selection

| Situation | Mode |
|-----------|------|
| User wants simplest framing | → /ezy (easy mode) |
| User wants maximum rigor | → /hrd (hard mode) or /certainty |
| User wants general principle | → /genl (what general pattern does this want follow?) |
| User wants specific application | → /spcf (apply known goal framework to this case) |

---

## Execute

→ INVOKE: /wt $ARGUMENTS

The /wt skill uses AR-forward mode: assume the want is right, trace what it commits you to, unbundle the want into desire/method/belief/assumption/implicit want/anti-want, find the actual want, map paths, identify the crux.

### Supplementary Analysis (invoke when relevant)

| Situation | Also invoke |
|-----------|------------|
| Goal involves future predictions | → /fut (future analysis) |
| Best-case outcome matters | → /utp (utopia analysis) |
| Worst-case outcome matters | → /dys (dystopia analysis) |
| Good outcome maximization | → /gop (good outcome analysis) |
| Goal involves safety | → /saf (safety analysis) |
| Need to trace implications of the goal | → /sycs (so you can see) |
| Goal can be reframed productively | → /iaw (in another way) |
| Goal has unresolved sub-decisions | → /tbd (to be determined) |
| Need to differentiate between similar goals | → /difr (differentiation reasoning) |
| Goal has a narrative structure | → /story |
| Convert knowledge of goal to action | → /kta (knowledge to action) |
| Want has adjacent implied tasks | → /ata (and then also) |

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Accepting the surface want** | Analysis proceeds on stated want without going deeper | Apply proxy test, trace anti-want, unbundle |
| **Infinite regression** | "But what do you REALLY want?" repeated endlessly | Stop when the want is both actionable and resonates — when the user says "yes, that's it" |
| **Method-as-want confusion** | User says they want a specific method (startup, MBA, move) | Separate the desire from the method — what does the method achieve? |
| **Aspirational stall** | Vague want never converts to actionable form | Force concreteness: "What would this look like on a Tuesday afternoon?" |
| **Foreclosure blindness** | Only exploring what the want opens, not what it closes | Explicitly map what each path gives up |
| **Anti-want avoidance** | Focusing only on what they want toward, not what they want away from | Ask: "What are you trying to get away from?" |

---

## Depth Scaling

| Depth | Scope | Minimum Output |
|-------|-------|----------------|
| **1x** | Surface unbundling — desire vs method vs assumption | 1 unbundling, proxy test, stated vs actual want |
| **2x** | Full unbundling + anti-want + foreclosures | Full unbundle, 2+ paths mapped, crux identified |
| **4x** | Multi-layer tracing + path comparison + prerequisites | 3+ layers deep, paths compared with tradeoffs, prerequisite audit |
| **8x** | Complete want archaeology + timeline + dependency mapping | Full want chain, all foreclosures mapped, prerequisite dependencies, first 3 actions specified |

---

## Pre-Completion Checklist

- [ ] Stated want captured in user's words
- [ ] Want unbundled into desire / method / belief / assumption
- [ ] Anti-want identified (what they're running from)
- [ ] Proxy test applied (would getting this satisfy them?)
- [ ] Actual want stated (if different from surface want)
- [ ] Foreclosures mapped (what each path gives up)
- [ ] At least one actionable path identified
- [ ] Crux identified (the one thing that determines which path)
- [ ] Prerequisites assessed (met / unmet)

---

## After Completion

Report:
- Stated want vs actual want (if different)
- The unbundling (desire / method / belief / assumption / anti-want)
- What the want commits you to
- What the want forecloses
- Prerequisites (met / unmet)
- Paths available
- Crux point
- Recommended first action

### Follow-Up Routing

After goal is clarified, the user may need:
- **"How do I get there?"** → INVOKE: /how $ARGUMENTS
- **"Should I actually pursue this?"** → INVOKE: /decide
- **"What could go wrong?"** → INVOKE: /fla or /dys
- **"What are the implications?"** → INVOKE: /sycs
- **"What else should I consider?"** → INVOKE: /ata
- **"What's left to figure out?"** → INVOKE: /tbd
- **"What skill should I run next?"** → INVOKE: /next or /fonss
- **"Convert this to action"** → INVOKE: /kta

---

## Integration

- **Use from**: /emotion (when feeling points to a goal), /decide (when criteria need clarifying via underlying want), /search (when exploration reveals a goal)
- **Routes to**: /wt (primary — want tracing), /how (after want is clear — find the method), /decide (if embedded choice found), /action (when ready to execute)
- **Differs from**: /how (want asks "what do I actually want?", how asks "how do I get it?"), /decide (want is single-direction, decide is choice between options)
- **Complementary**: /aex (surface assumptions in the want), /fla (anticipate failure of chosen path), /gd (goal decomposition after want is clear)
