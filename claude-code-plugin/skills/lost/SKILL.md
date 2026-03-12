---
name: "lost - Lost My Direction"
description: "For when you had a direction but lost it. Helps you find whether the goal changed, you changed, or the situation changed — and what to do next."
output:
  format: "prose"
---

# Lost - Lost My Direction

**Input**: $ARGUMENTS

---

## Core Principles

1. **Getting lost usually means you outgrew the map, not that you failed.** The direction that made sense before stopped making sense because something real changed. That's growth, not failure.

2. **There are only three reasons you lose direction.** You changed. The situation changed. Or you learned something that made the old direction invalid. Identifying which one tells you what to do next.

3. **The old goal is data, not an obligation.** You set it with the information you had. You have different information now. Honoring the old goal out of guilt or sunk cost isn't integrity — it's inertia.

4. **Feeling lost is disorienting but not dangerous.** You're between directions, not without capacity. The skills that got you to the old direction still work. You just need something to point them at.

---

## Phase 1: What Was the Direction?

```
[L1] ORIGINAL_GOAL: [What were you working toward? State it clearly.]
[L2] WHEN_SET: [When did you commit to this direction?]
[L3] WHY_IT_MATTERED: [What made this goal feel right at the time?]
[L4] HOW_FAR: [How far did you get before feeling lost?]
```

---

## Phase 2: When Did It Stop Feeling Right?

```
[L5] INFLECTION_POINT: [When did the direction start feeling off?]
[L6] SIGNAL: [What was the first sign? A feeling? An event? A realization?]
[L7] RESPONSE: [What did you do when you noticed? (Ignored it? Pushed through? Stopped?)]
```

---

## Phase 3: What Changed?

Only one of these is primary. Identify which.

| Change Type | Signals | Meaning |
|-------------|---------|---------|
| **You changed** | Different values, interests, energy, priorities than when you set the goal | You outgrew the goal. The goal was right for who you were, not who you are. |
| **The situation changed** | External factors shifted — market, relationships, resources, constraints | The goal may still be valid but the path to it needs updating. |
| **You learned something new** | New information made the old direction seem wrong, naive, or incomplete | The goal was based on incomplete understanding. Now you know more. |

```
[L8] CHANGE_TYPE: [you | situation | knowledge]
[L9] WHAT_SPECIFICALLY_CHANGED: [name it precisely]
[L10] IS_THIS_PERMANENT: [Is this change temporary/reversible, or is it the new reality?]
```

---

## Phase 4: Is the Original Goal Still Valid?

```
[L11] VALIDITY_CHECK:
  - Does the original goal still matter to you? [yes | no | partially]
  - Is the original goal still achievable? [yes | no | differently]
  - Would achieving it still produce the outcome you wanted? [yes | no | different outcome]
```

### If STILL VALID (all yes):

```
[L12-V] RECONNECTION:
  The goal is fine. You lost connection to it, not faith in it.
  What disconnected you? [fatigue | distraction | fear | a setback]

  TO RECONNECT:
  - Revisit why it mattered (L3)
  - Identify the next concrete step (not the whole path — just the next step)
  - Check: do you need rest before re-engaging, or just a restart?
```

→ INVOKE: `/gu [original goal with fresh context]`

### If NO LONGER VALID (any no):

```
[L13-N] RELEASE:
  The goal served its purpose. It got you here. It's OK to set it down.

  WHAT YOU GAINED from pursuing it (even though you're not finishing):
  1. [skill, knowledge, relationship, or clarity gained]
  2. [skill, knowledge, relationship, or clarity gained]

  WHAT'S PULLING YOU NOW:
  [Is there something emerging that feels more right? Even a whisper?]
```

If something is emerging → INVOKE: `/gu [the emerging direction]`

### If UNKNOWN:

```
[L14-U] You had a direction and it's gone, and nothing has replaced it yet.
  That's the space between maps. It's uncomfortable but it's not permanent.
```

→ INVOKE: `/idk [current state and what you've ruled out]`

---

## Phase 5: Output

```
LOST MY DIRECTION
=================

ORIGINAL GOAL: [goal]
SET WHEN: [when]
WHY IT MATTERED: [reason]

LOST DIRECTION BECAUSE: [you changed | situation changed | learned something new]
SPECIFICALLY: [what changed]

ORIGINAL GOAL STATUS: [still valid | no longer valid | unknown]

PATH FORWARD:
  [One of three:]
  a) RECONNECT: [goal is valid — here's how to re-engage]
  b) RELEASE AND REDIRECT: [goal served its purpose — here's what's emerging]
  c) SIT IN THE GAP: [nothing clear yet — here's how to be OK with that]

WHAT YOU HAVEN'T LOST:
  [Skills, knowledge, relationships, or capacities gained on the old path that carry forward regardless]

READY FOR:
- /gu [goal] — to clarify a new or reconnected goal
- /idk [state] — if no direction has emerged
- /grf [goal] — to reframe the goal with new understanding
- /emotion [feeling] — if grief or frustration about the lost direction needs processing
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Forcing reconnection** | Pushing user back to old goal when they've outgrown it | Check L11 honestly — if the goal doesn't resonate, don't force it |
| **Premature new goal** | Jumping to a new direction without processing what happened | Phase 3 and 4 must complete before Phase 5 |
| **Sunk cost pressure** | "But I've invested so much" keeping a dead goal alive | Name the sunk cost explicitly. What you gained carries forward. What you invested is spent either way. |
| **Romanticizing the old direction** | Remembering only the good parts of the old goal | Check: are you missing the goal, or missing the certainty of having one? |
| **Shame about changing** | "I should have known" or "I'm flaky" | Changing direction because of new information is rationality, not failure |
| **Skipping grief** | Moving to next goal without acknowledging loss of the old one | Letting go of a direction you cared about is a real loss. Acknowledge it. |

---

## Depth Scaling

| Depth | Phases | Analysis | Emotional Processing |
|-------|--------|----------|---------------------|
| 1x | Goal + change type + path | Light | Acknowledge only |
| 2x | Full phases | Standard | Named and addressed |
| 4x | Full + pattern analysis (is this recurring?) | Deep | Full processing |
| 8x | Full + life-direction context | Complete | Integration with identity/values |

Default: 2x. These are floors.

---

## Pre-Completion Checklist

- [ ] Original goal clearly stated
- [ ] Inflection point identified (when it stopped feeling right)
- [ ] Change type identified (you/situation/knowledge)
- [ ] Goal validity assessed honestly (not forced)
- [ ] Path forward matches the assessment (reconnect/release/gap)
- [ ] What was gained is named (nothing was wasted)
- [ ] No shame or judgment in the output

---

## Integration

- Use from: "I'm lost", "I don't know where I'm going anymore", "I had a plan but...", "I lost my way"
- Routes to: `/gu` (goal understanding), `/idk` (total uncertainty), `/grf` (goal reframing), `/emotion` (processing feelings about the loss)
- Differs from `/idk`: idk may never have had a direction; lost had one and lost it
- Differs from `/cnfsd`: cnfsd can't understand something; lost understands but can't find direction
- Differs from `/unsure`: unsure has a direction but lacks confidence; lost has lost the direction entirely
