---
name: "idk - I Don't Know"
description: "Entry point for total uncertainty. When you don't know what you want, what to do, or what's happening — start here."
---

# IDK - I Don't Know

**Input**: $ARGUMENTS

---

## Core Principles

1. **Not knowing is a valid state.** It's not a failure — it's a starting position. Most useful thinking begins from "I don't know." The problem isn't not knowing. The problem is freezing because you don't know.

2. **You know more than you think.** Total blankness is rare. Usually there's one thread — a feeling, a constraint, a thing you DON'T want. That thread is enough.

3. **Narrowing beats answering.** You don't need to jump from "I don't know" to "I know exactly what to do." You just need to go from "I don't know anything" to "I don't know THIS SPECIFIC THING." That's progress.

4. **The body often knows before the mind.** If you can't articulate what you want, check what you're feeling. Anxiety points to threat. Restlessness points to stagnation. Sadness points to loss. These are data.

---

## Phase 1: Acknowledgment

```
[IDK1] STATE: "I don't know."
[IDK2] REACTION: That's OK. This is a starting point, not a dead end.
[IDK3] PRESSURE_CHECK: Is there external pressure to know right now?
  - If yes: How real is that deadline? Can you buy 24 hours?
  - If no: Good. No rush. Let's narrow it down.
```

---

## Phase 2: Narrowing the Space

What kind of "I don't know" is this?

| Type | Signals | Route |
|------|---------|-------|
| **I don't know what to DO** | Paralysis, too many options or zero options | → Phase 3A |
| **I don't know what I WANT** | Emptiness, disconnection from desire | → Phase 3B |
| **I don't know what's HAPPENING** | Confusion, things don't make sense | → Phase 3C |
| **I don't know how I FEEL** | Numbness, emotional fog | → Phase 3D |
| **I truly know NOTHING** | Complete blank | → Phase 3E |

```
[IDK4] TYPE: [do | want | happening | feel | nothing]
[IDK5] EVIDENCE: [what signals point to this type]
```

---

## Phase 3A: Don't Know What to DO

```
[IDK-A1] What's the situation you need to act in?
[IDK-A2] What are you afraid of doing wrong?
[IDK-A3] If you HAD to do something in the next hour, what would it be?
```

That gut answer in A3 — examine it. It's probably close.

→ INVOKE: `/unsure [the action from A3]`

---

## Phase 3B: Don't Know What You WANT

```
[IDK-B1] What do you NOT want? (This is always easier.)
[IDK-B2] What did you want six months ago? Does it still resonate?
[IDK-B3] When were you last excited about something? What was it?
```

Wanting is a skill that atrophies. Start with what repels you and work backwards.

→ INVOKE: `/gu [emerging want from B1-B3]`

---

## Phase 3C: Don't Know What's HAPPENING

```
[IDK-C1] What changed recently?
[IDK-C2] What were you expecting to happen that didn't?
[IDK-C3] Who else is involved, and do THEY seem to know what's happening?
```

→ INVOKE: `/cnfsd [the situation from C1-C3]`

---

## Phase 3D: Don't Know How You FEEL

```
[IDK-D1] Where in your body do you feel something? (Chest, stomach, throat, head)
[IDK-D2] Is it more like pressure, emptiness, heat, or tightness?
[IDK-D3] If you had to pick one word — even a wrong one — what would it be?
```

That "wrong" word is usually close enough to work with.

→ INVOKE: `/emotion [the word from D3]`

---

## Phase 3E: Truly Know Nothing

If you've gotten here, try this:

```
[IDK-E1] What do you NOT want? List 3 things.
[IDK-E2] What's the opposite of each?
[IDK-E3] Do any of those opposites feel like a direction?
```

If even this produces nothing:

```
[IDK-E4] When did you last feel like you DID know?
[IDK-E5] What's different now?
```

The gap between "I knew" and "I don't know" usually contains the answer.

---

## Phase 4: Output

```
I DON'T KNOW
============

STARTING STATE: [what the user said]
TYPE: [do | want | happening | feel | nothing]

THE ONE THREAD:
  [The single piece of knowledge extracted from the narrowing questions]

NEXT STEP:
  → INVOKE: /skill-id [specific arguments built from the thread]

REMINDER:
  You went from "I don't know" to "I don't know [specific thing]."
  That's real progress. The specific thing is solvable.
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Rushing to solutions** | Jumping to advice before narrowing | Stay in Phase 2 until the type is clear |
| **Accepting "nothing" too easily** | Skipping to Phase 3E without testing other types | Most people CAN narrow — push gently on A-D first |
| **Making it intellectual** | Asking analytical questions when the user is emotionally stuck | Check Phase 3D before 3A |
| **Creating more overwhelm** | Too many questions at once | One question at a time. Wait for the answer. |
| **Invalidating the state** | "You must know SOMETHING" | Never. "I don't know" is valid. Start there. |

---

## Depth Scaling

| Depth | Phases | Questions per Phase | Follow-up |
|-------|--------|-------------------|-----------|
| 1x | Narrow + one route | 1-2 | Single skill route |
| 2x | Narrow + full route | 3 | Skill route + context |
| 4x | Full exploration of all phases | 3-5 | Multiple possible routes |
| 8x | Deep inquiry across all dimensions | Full | Route + reflection + pattern analysis |

Default: 2x. These are floors.

---

## Pre-Completion Checklist

- [ ] User's "I don't know" acknowledged without judgment
- [ ] Type of uncertainty identified (do/want/happening/feel/nothing)
- [ ] At least one thread extracted from narrowing questions
- [ ] Next step is specific and invocable
- [ ] User moved from "I don't know" to "I don't know [specific thing]"

---

## Integration

- Use from: user says "I don't know", "no idea", "I'm lost", "I'm blank", total uncertainty
- Routes to: `/unsure` (action uncertainty), `/gu` (goal discovery), `/cnfsd` (confusion), `/emotion` (feelings), `/lost` (lost direction)
- Differs from `/unsure`: unsure has a direction but lacks confidence; idk has no direction at all
- Differs from `/cnfsd`: cnfsd has information that doesn't make sense; idk has no information
- Differs from `/lost`: lost had a direction and lost it; idk may never have had one
