---
name: "flhwijd - For Like Here What I Just Did"
description: "Analyze the user's just-finished action sequence, extract the repeatable pattern, clean it, name it, and convert it into a reusable procedure with trigger conditions."
---

# FLHWIJD - For Like Here What I Just Did

**Input**: $ARGUMENTS

---

## Core Principles

1. **Behavior contains procedure.** When someone does something well repeatedly, there's an implicit procedure. This skill makes the implicit explicit — but the procedure might need cleaning, not just recording.

2. **Separate pattern from instance.** The user did specific things in a specific order for specific reasons. Some of those specifics are essential to the pattern; others are incidental to this particular case. The skill must distinguish which is which.

3. **Name determines reuse.** A pattern without a memorable, guessable name is a pattern nobody will invoke again. The name must capture the FUNCTION, not the instance.

4. **Trigger conditions are the pattern's brain.** A procedure without "when to use this" is a tool without an instruction manual. Triggers answer: "What situation should make someone reach for this pattern?"

5. **Clean, don't just record.** The user might have done steps in suboptimal order, included unnecessary steps, or skipped steps that should be explicit. The extracted procedure should be the IDEAL version, not a verbatim log.

---

## Phase 1: Action Capture

Reconstruct what the user just did. Work backward from the most recent actions.

```
[P1] CONTEXT: [what was the user trying to accomplish?]
[P2] TRIGGER: [what prompted the action sequence?]
[P3] OUTCOME: [what was achieved?]

ACTION SEQUENCE:
[P4] Step 1: [action] — [purpose]
[P5] Step 2: [action] — [purpose]
[P6] Step 3: [action] — [purpose]
...
```

### Capture Methods

| Source | How to Extract |
|--------|---------------|
| **Conversation history** | Review the recent exchanges for actions taken |
| **User description** | User explains "what I just did" |
| **Tool call history** | Examine which tools were called in what order |
| **Output artifacts** | What was produced? Work backward from outputs to steps |

---

## Phase 2: Pattern Extraction

Separate the essential pattern from instance-specific details.

```
[P-N] ESSENTIAL STEP: [action] — WHY ESSENTIAL: [removing this breaks the pattern]
[P-N] INCIDENTAL: [action] — WHY INCIDENTAL: [specific to this instance, not the pattern]
[P-N] MISSING STEP: [action that should exist] — WHY MISSING: [user skipped it but shouldn't]
[P-N] ORDER DEPENDENCY: Step [X] must precede Step [Y] because [reason]
[P-N] ORDER FLEXIBLE: Steps [X] and [Y] can be reordered without consequence
```

### Essential vs Incidental Test

For each step, ask:
1. If I removed this step, would the outcome still be achieved? (If yes → incidental)
2. If I changed the specific content but kept the action type, would the pattern still work? (If yes → the action type is essential, the content is incidental)
3. If I did this step in a different position, would it still work? (If yes → order is flexible)

---

## Phase 3: Pattern Cleaning

Improve the extracted pattern:

```
[P-N] OPTIMIZATION: [what changed] — [why it's better]
```

| Cleaning Operation | When to Apply |
|-------------------|--------------|
| **Reorder** | Steps were done in a suboptimal sequence |
| **Remove** | Step was unnecessary (passed incidental test) |
| **Add** | A step was implicitly needed but not done |
| **Generalize** | Step was too specific to this instance |
| **Split** | One step was actually two distinct operations |
| **Merge** | Two steps were really one operation |

---

## Phase 4: Naming and Trigger Definition

```
[P-N] PATTERN_NAME: [short, memorable, function-based name]
[P-N] NAMING_RATIONALE: [why this name captures the function]
[P-N] ALTERNATIVE_NAMES: [2-3 alternatives considered and rejected]
```

### Trigger Conditions

When should someone use this pattern?

```
[P-N] TRIGGER CONDITIONS:
  SITUATION: [what state the user is in]
  SIGNAL: [what observable thing prompts this pattern]
  NOT_WHEN: [situations that look similar but should use a different approach]
```

### Scope

```
[P-N] WORKS_FOR: [what types of inputs/situations this pattern handles]
[P-N] BREAKS_WHEN: [what conditions cause this pattern to fail]
[P-N] SCALES_TO: [how far this pattern extends before needing modification]
```

---

## Phase 5: Output

```
PATTERN EXTRACTION
==================

SOURCE: [what the user just did]
CONTEXT: [what they were trying to accomplish]

PATTERN: [name]
TRIGGER: [when to use this]
NOT_WHEN: [when NOT to use this]

PROCEDURE:
1. [step] — [purpose]
2. [step] — [purpose]
3. [step] — [purpose]
...

ORDER DEPENDENCIES:
- Step [X] before Step [Y]: [reason]

OPTIMIZATIONS APPLIED:
- [what was changed from the original sequence and why]

WORKS FOR: [scope]
BREAKS WHEN: [limits]

READY FOR:
- /mts [pattern name] — to convert into a full skill
- /fmtsb — to formalize if skill-worthy
- Direct reuse as-is for ad-hoc application
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Verbatim recording** | Output is a log, not a procedure | Clean: reorder, generalize, remove incidentals |
| **Over-generalization** | Pattern is so abstract it's useless | Keep enough specificity to be actionable |
| **Under-generalization** | Pattern only works for the exact case it came from | Identify which details are incidental and generalize them |
| **Missing triggers** | No "when to use this" section | Triggers are mandatory — a pattern without triggers is unfindable |
| **Bad naming** | Name describes the instance, not the function | Name must be guessable from the PROBLEM, not the SOLUTION |
| **Skipped cleaning** | Suboptimal sequence preserved as-is | Ask: "if I were designing this from scratch, would I do it this way?" |
| **Essential step dropped** | Step removed that was actually necessary | Re-test: does removing this step break the outcome? |

---

## Depth Scaling

| Depth | Min Steps Captured | Essential/Incidental Analysis | Cleaning Operations | Trigger Detail |
|-------|-------------------|------------------------------|--------------------| --------------|
| 1x | 3 | List only | 1 | Situation only |
| 2x | 5 | With reasoning | 3 | Situation + signal + not-when |
| 4x | 8 | With reasoning + test | 5 | Full scope analysis |
| 8x | 12 | Full analysis | 8 | Full scope + scaling analysis |

Default: 2x. These are floors.

---

## Pre-Completion Checklist

- [ ] Action sequence captured with purpose for each step
- [ ] Essential vs incidental distinguished with reasoning
- [ ] Missing steps identified (not just recorded what was done)
- [ ] Order dependencies identified
- [ ] At least one cleaning operation applied (sequence is improved, not just recorded)
- [ ] Pattern named with function-based name (not instance-based)
- [ ] Trigger conditions specified (situation + signal + not-when)
- [ ] Scope and breaking conditions identified
- [ ] Output is actionable (someone could follow this procedure)

---

## Integration

- Use before: `/mts` (to convert pattern into a full skill)
- Use after: any action sequence the user wants to capture
- Complementary: `/pcex` (procedure extraction from completed goals)
- Differs from `/pcex`: pcex extracts from completed goals; flhwijd extracts from just-finished action sequences
- Differs from `/adep`: adep does breadth-first extraction from sources; flhwijd does depth-first from one sequence
