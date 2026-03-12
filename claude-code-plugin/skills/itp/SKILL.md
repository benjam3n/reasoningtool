---
name: "itp - In This Prompt"
description: "Decompose a prompt into its explicit requests, implicit requests, constraints, assumptions, emotional signals, and candidate skill mappings — making every part visible."
output:
  format: "prose"
---

# ITP - In This Prompt

**Input**: $ARGUMENTS

---

## Core Principles

1. **Prompts are compressed communication.** A single sentence can contain 3-5 distinct needs, 2-3 constraints, and an emotional subtext. Decompressing reveals what the user actually needs.

2. **Implicit > explicit.** What the user didn't say often matters more than what they said. Implicit assumptions, unstated constraints, and background context shape the real task.

3. **Every part has a type.** Requests, constraints, assumptions, preferences, emotions, and context are different things. Mixing them produces confused responses.

4. **Order of discovery ≠ order of importance.** The first thing in the prompt isn't necessarily the main thing. The most important element might be buried in a subordinate clause.

5. **Decomposition enables routing.** Once you can see every part of the prompt separately, you can route each part to the right skill instead of trying to handle everything with one skill.

---

## Phase 1: Surface Parse

Extract what's explicitly stated:

```
[P1] FULL_PROMPT: [quoted]
[P2] WORD_COUNT: [N]
[P3] SENTENCE_COUNT: [N]
[P4] OVERALL_INTENT: [what the prompt is broadly about — one sentence]
```

---

## Phase 2: Component Extraction

Decompose into typed components:

### Explicit Requests (what the user asked for)

```
[P-N] REQUEST: [what they want done]
  PRIORITY: [primary | secondary | tertiary]
  SPECIFICITY: [specific | moderate | vague]
```

### Constraints (what limits the solution)

```
[P-N] CONSTRAINT: [limitation stated]
  TYPE: [time | resource | scope | quality | format | audience]
  HARD/SOFT: [must respect | prefer to respect]
```

### Implicit Tasks (not stated but required)

```
[P-N] IMPLICIT: [task that wasn't stated but is implied]
  WHY_IMPLIED: [what in the prompt implies this]
  IMPORTANCE: [critical | helpful | optional]
```

### Assumptions (what the user takes for granted)

```
[P-N] ASSUMPTION: [what the user assumes is true]
  TESTABLE: [yes — how | no]
  RISK_IF_WRONG: [what breaks if this assumption is false]
```

### Emotional Signals (mood, energy, frustration)

```
[P-N] EMOTION: [detected emotion or tone]
  SIGNAL: [what words or patterns indicate this]
  IMPLICATION: [how this affects handling — e.g., frustrated user needs acknowledgment before analysis]
```

### Context (background that shapes interpretation)

```
[P-N] CONTEXT: [background information provided]
  RELEVANCE: [critical | helpful | decorative]
```

---

## Phase 3: Priority Analysis

```
[P-N] PRIORITY_ORDER:
  1. [component — P-ref] — WHY_FIRST: [why this is the most important part]
  2. [component — P-ref] — WHY_SECOND: [why]
  3. [component — P-ref] — WHY_THIRD: [why]

[P-N] MAIN_NEED: [the single most important thing the user needs — may be implicit]
[P-N] SECONDARY_NEEDS: [other needs, ordered]
```

---

## Phase 4: Skill Mapping

Map each component to candidate skills:

```
[P-N] MAPPING:
  [P-ref] REQUEST → /skill-id — [why this skill handles this component]
  [P-ref] IMPLICIT → /skill-id — [why]
  [P-ref] ASSUMPTION → /skill-id — [why — e.g., /aex to test it]
  [P-ref] EMOTION → /skill-id — [why — e.g., /emotion if frustration detected]
```

---

## Phase 5: Output

```
IN THIS PROMPT
==============

PROMPT: [quoted]
OVERALL INTENT: [one sentence]

EXPLICIT REQUESTS:
  1. [request] — PRIORITY: [level] — SKILL: /[id]
  2. [request] — PRIORITY: [level] — SKILL: /[id]

CONSTRAINTS:
  1. [constraint] — TYPE: [type] — HARD/SOFT: [level]

IMPLICIT TASKS:
  1. [task] — WHY_IMPLIED: [reason] — SKILL: /[id]

ASSUMPTIONS:
  1. [assumption] — RISK_IF_WRONG: [risk] — TEST: /[id]

EMOTIONAL SIGNALS:
  1. [emotion] — IMPLICATION: [how to handle]

MAIN NEED: [the most important thing — might not be the first thing stated]

SUGGESTED APPROACH:
  Start with: /[id] [specific invocation]
  Then: /[id] [specific invocation]
  Because: [rationale for this order]

READY FOR:
- /extract — for full skill extraction from this prompt
- /wsib — to pick the single best skill
- /fonss — to sequence skills for this prompt
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Surface only** | Only explicit requests extracted | Check for implicit tasks, assumptions, emotions |
| **Type confusion** | Constraints treated as requests or vice versa | Apply type definitions strictly |
| **Priority by position** | First sentence assumed most important | Analyze actual importance, not position |
| **Assumptions invisible** | No assumptions extracted | Every prompt assumes something. Find at least one |
| **Emotions ignored** | Analytical decomposition of an emotional prompt | Check for frustration/urgency/overwhelm signals |
| **Over-decomposition** | Simple prompt split into 15 components | Simple prompts should have simple decompositions |

---

## Depth Scaling

| Depth | Components Extracted | Implicit Tasks | Assumption Check | Emotion Check |
|-------|---------------------|---------------|-----------------|--------------|
| 1x | Requests + constraints | 1 | No | No |
| 2x | Requests + constraints + implicit | 2 | 1 assumption | Basic check |
| 4x | All types | 4 | 3 assumptions | Full check |
| 8x | All types + cross-analysis | All found | All + risk analysis | Full + implication |

Default: 2x. These are floors.

---

## Pre-Completion Checklist

- [ ] Full prompt quoted
- [ ] Explicit requests extracted with priority
- [ ] Constraints identified and typed
- [ ] At least one implicit task identified
- [ ] At least one assumption surfaced (at 2x+)
- [ ] Emotional signals checked
- [ ] Main need identified (might differ from first request)
- [ ] Skill mappings provided for key components
- [ ] Suggested approach with ordering rationale

---

## Integration

- Use from: any complex or multi-part prompt
- Routes to: `/extract` (full skill extraction), `/wsib` (best single skill), `/fonss` (skill sequencing)
- Complementary: `/extract` (itp decomposes the prompt; extract maps skills to it)
- Differs from `/extract`: extract maps skills to needs; itp decomposes the prompt into typed parts
- Differs from `/gu`: gu analyzes goals; itp analyzes prompts
