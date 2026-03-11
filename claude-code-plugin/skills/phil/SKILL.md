---
name: "phil - Philosophize Requirements"
description: "Derive what a skill, system, or solution SHOULD do by examining its nature, purpose, and the problem it exists to solve — before writing any procedures."
---

# Philosophize Requirements

**Input**: $ARGUMENTS

---

## Interpretations

Before executing, identify which interpretation matches the user's input:

**Interpretation 1 — Skill requirements**: The user wants to figure out what a reasoning skill should contain — its interpretations, steps, and quality criteria — before building or improving it.
**Interpretation 2 — System requirements**: The user wants to understand what a system, product, or tool should do before designing it.
**Interpretation 3 — Solution requirements**: The user has a problem and wants to understand what a good solution would need to be — its properties, constraints, and success criteria — before generating solutions.

If ambiguous, ask: "Are you philosophizing about what a skill should do, what a system should do, or what a solution to a problem needs to be?"
If clear from context, proceed with the matching interpretation.

---

## Core Principles

1. **Requirements precede procedures.** You cannot write good steps until you know what the steps are FOR. Most bad skills are procedurally competent but requirements-wrong — they efficiently do the wrong thing.

2. **Derive, don't enumerate.** Listing requirements by brainstorming produces whatever comes to mind. DERIVING requirements from the nature of the problem produces what must be true. The difference is the difference between guessing and reasoning.

3. **Multiple derivation paths must converge.** If you derive requirements from the purpose, the user's state, the failure modes, and the domain — and they all point to the same requirements — those requirements are robust. If they diverge, the divergences reveal what you haven't understood yet.

4. **The hard part is finding what's missing.** Anyone can list obvious requirements. The value is in surfacing requirements that are invisible until you look from the right angle. Use multiple lenses specifically to find what single-lens thinking misses.

---

## Phase 1: Name What You're Philosophizing About

```
SUBJECT: [what skill, system, or solution are we examining?]
PURPOSE: [why does this thing exist? what problem does it solve?]
USER: [who uses this? what state are they in when they arrive?]
SUCCESS: [what's true when this thing works perfectly?]
FAILURE: [what's true when this thing fails?]
```

---

## Phase 2: Derive Requirements from Multiple Angles

Each angle generates candidate requirements. Requirements that appear from multiple angles are strongest.

### Angle 1: Purpose Derivation

Start from WHY this thing exists and work forward.

```
WHY does this exist?
→ [answer]
WHAT must be true for that WHY to be served?
→ [requirement 1]
→ [requirement 2]
→ [requirement 3]
WHAT would BETRAY that WHY? (things it must NOT do)
→ [anti-requirement 1]
→ [anti-requirement 2]
```

### Angle 2: User State Derivation

Start from the user's situation and work backward to what the thing must provide.

```
USER ARRIVES IN STATE: [describe their mental/emotional/practical state]
USER NEEDS TO LEAVE IN STATE: [describe the desired transformation]
THEREFORE THE THING MUST:
→ [requirement from the gap between arrival and departure]
→ [requirement]
→ [requirement]

WHAT COULD MAKE THE USER'S STATE WORSE?
→ [anti-requirement — thing that would harm the user]
→ [anti-requirement]
```

### Angle 3: Failure Mode Derivation

Start from how this thing fails and work backward to what would prevent failure.

```
THIS THING FAILS WHEN:
→ [failure mode 1] — PREVENTED BY: [requirement]
→ [failure mode 2] — PREVENTED BY: [requirement]
→ [failure mode 3] — PREVENTED BY: [requirement]
→ [failure mode 4] — PREVENTED BY: [requirement]
→ [failure mode 5] — PREVENTED BY: [requirement]

MOST COMMON FAILURE: [which one?]
MOST CATASTROPHIC FAILURE: [which one?]
```

### Angle 4: Domain Derivation

Look at how experts in this domain think about the problem.

```
DOMAIN: [what field does this problem belong to?]
HOW DO EXPERTS HANDLE THIS?
→ [practice 1] — IMPLIES REQUIREMENT: [requirement]
→ [practice 2] — IMPLIES REQUIREMENT: [requirement]
→ [practice 3] — IMPLIES REQUIREMENT: [requirement]

WHAT DO EXPERTS KNOW THAT NOVICES DON'T?
→ [insight] — IMPLIES REQUIREMENT: [requirement]
```

### Angle 5: Boundary Derivation

Define what this thing IS by defining what it IS NOT.

```
THIS IS NOT: [thing it could be confused with]
→ THEREFORE IT MUST: [requirement that distinguishes it]

THIS IS NOT: [another thing it could be confused with]
→ THEREFORE IT MUST: [distinguishing requirement]

WHERE DOES THIS END AND SOMETHING ELSE BEGIN?
→ BOUNDARY: [scope limit] — REQUIREMENT: [stay within this boundary]
```

### Angle 6: Completeness Derivation (for skills with interpretations)

If the subject has modes, types, or interpretations — are they complete?

```
DERIVE CATEGORIES FROM:
  1. Purpose: what are all the REASONS someone would use this? → [list]
  2. Input types: what are all the INPUTS someone could bring? → [list]
  3. Operations: what are all the COGNITIVE OPERATIONS this performs? → [list]
  4. User states: what are all the STATES a user could be in? → [list]

CONVERGENCE CHECK:
  Categories that appear in 3+ derivations: [list — these are robust]
  Categories that appear in only 1: [list — these might be spurious or might be hidden gems]
  Gaps visible from one derivation but not others: [list — investigate these]
```

---

## Phase 3: Convergence Analysis

```
REQUIREMENTS CONVERGENCE MAP
=============================

STRONG REQUIREMENTS (appear from 3+ angles):
1. [requirement] — from: [angles]
2. [requirement] — from: [angles]
...

MODERATE REQUIREMENTS (appear from 2 angles):
1. [requirement] — from: [angles]
...

WEAK REQUIREMENTS (appear from 1 angle only):
1. [requirement] — from: [angle] — investigate: [why didn't other angles surface this?]
...

ANTI-REQUIREMENTS (things it must NOT do):
1. [anti-requirement] — from: [angles]
...

CONTRADICTIONS (angles disagree):
1. [angle X says A, angle Y says B] — resolution: [which is right and why]
...
```

---

## Phase 4: Requirements Specification

```
REQUIREMENTS FOR: [subject]
============================

ESSENTIAL (must have or the thing fundamentally fails):
1. [requirement] — WHY: [derived from which angles]
2. ...

IMPORTANT (significantly better with these):
1. [requirement] — WHY: [derived from which angles]
2. ...

NICE-TO-HAVE (good but not load-bearing):
1. [requirement] — WHY: [derived from which angles]
2. ...

ANTI-REQUIREMENTS (must NOT have):
1. [anti-requirement] — WHY: [what it would break]
2. ...

SCOPE BOUNDARY:
This thing does: [list]
This thing does NOT do: [list]
If the user needs [X], route to: [other skill/tool]
```

---

## Phase 5: Readiness Check

```
READINESS TO BUILD:
- [ ] Purpose is clear and non-circular
- [ ] User arrival and departure states are defined
- [ ] At least 3 derivation angles were used
- [ ] Strong requirements converge from multiple angles
- [ ] Failure modes are identified with prevention requirements
- [ ] Scope boundary is explicit (what's in vs out)
- [ ] Anti-requirements are stated (not just requirements)
- [ ] Contradictions between angles are resolved
- [ ] If interpretations exist, completeness derivation was performed

CONFIDENCE: [high / medium / low — based on convergence strength]
GAPS: [what's still uncertain]
NEXT: [build the thing / investigate gaps first / test requirements with users]
```

---

## Depth Scaling

| Depth | Angles Used | Min Requirements per Angle | Convergence Analysis |
|---|---|---|---|
| 1x | 2 (purpose + user) | 2 | List only |
| 2x | 4 (purpose + user + failure + boundary) | 3 | Convergence map |
| 4x | All 6 | 4 | Full convergence + contradiction resolution |
| 8x | All 6 + custom angles | 5 | Full + test each strong requirement for necessity |

Default: 2x.

---

## Failure Modes

| Failure | Signal | Fix |
|---|---|---|
| **Requirements by brainstorm** | Listed requirements without derivation logic | Each requirement must trace to an angle + reasoning |
| **Purpose-only derivation** | All requirements come from "what should it do" | Use failure modes and boundaries — they find different things |
| **Vague requirements** | "It should be good" or "it should be thorough" | Each requirement must be testable — how would you verify it's met? |
| **Missing anti-requirements** | Only said what it SHOULD do, never what it SHOULDN'T | Explicitly list what would make this thing harmful or useless |
| **Single-angle confidence** | "We have 10 requirements" but all from one angle | Convergence from multiple angles is what makes requirements robust |
| **Premature proceduralization** | Started writing steps before requirements are clear | Stay in requirements mode until Phase 4 is complete |

---

## Integration

Use with:
- `/cs` or `/mts` → After /phil, to create the skill based on derived requirements
- `/enough` → To check whether the requirements analysis is thorough enough
- `/ar` or `/aw` → To stress-test specific requirements
- `/se` → To enumerate the space before deriving requirements from it
- `/impss` → To improve an existing skill by re-deriving its requirements
