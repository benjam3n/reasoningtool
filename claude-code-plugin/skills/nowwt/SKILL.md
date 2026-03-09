---
name: "nowwt - Now What"
description: "For after something just happened — good or bad — and you need to figure out what comes next. Assess what changed, what it means, and what to do about it."
---

# NOWWT - Now What

**Input**: $ARGUMENTS

---

## Core Principles

1. **Something changed. Start there.** "Now what" always follows an event. The event changed something — your situation, your options, your constraints, your information. Identify what changed before deciding what to do.

2. **React to reality, not to feelings.** After unexpected events, the emotional response comes first. Acknowledge it, then set it aside and assess what actually changed in concrete terms.

3. **Not everything needs an immediate response.** Some changes are urgent. Some can wait. The first job is to separate what needs action NOW from what can wait.

4. **Good news and bad news both require adjustment.** Unexpected success can derail you just as easily as unexpected failure. Both require a "now what" assessment.

---

## Step 1: What Just Happened?

```
EVENT: [what happened — from $ARGUMENTS]
EXPECTED: [yes/no — did you see this coming?]
VALENCE: [positive / negative / neutral / mixed]
```

## Step 2: What Changed?

List the concrete changes this event creates:

```
WHAT CHANGED:
  GAINED: [new resources, options, information, capabilities]
  LOST: [closed options, resources spent, constraints added]
  SHIFTED: [priorities that moved, timelines that changed, relationships that altered]
  REVEALED: [things you now know that you didn't before]
```

## Step 3: What Does This Mean for Your Goals?

```
CURRENT GOAL: [what you were working toward]
IMPACT: [how the event affects this goal]
  - Goal still valid? [yes / no / needs revision]
  - Path still valid? [yes / no / needs revision]
  - Timeline still valid? [yes / no / needs revision]
```

## Step 4: What's the Most Important Response?

Based on the event type, follow the appropriate path:

### Path: Unexpected Success
Something went better than planned.
```
RISKS OF SUCCESS:
  - Overcommitting based on one win
  - Changing strategy when the current one is working
  - Ignoring what actually caused the success
→ RESPONSE: [capture what worked, secure the gain, then decide if it changes your plan]
```

### Path: Unexpected Failure
Something went wrong.
```
TRIAGE:
  - Is there damage to contain RIGHT NOW? [yes → contain it first]
  - Is the failure recoverable? [yes → recovery plan / no → adaptation plan]
  - Did you learn something that changes your approach? [what]
→ RESPONSE: [contain damage if any, extract the lesson, adjust plan]
```

### Path: Surprise Information
You learned something you didn't know.
```
INFORMATION IMPACT:
  - Does this invalidate any current assumptions? [which ones]
  - Does this open new options? [what]
  - Does this close options you were counting on? [what]
→ RESPONSE: [update your assumptions, reassess options, adjust plan]
```

### Path: External Change
Something outside your control shifted.
```
NEW CONSTRAINTS:
  - What can you no longer do? [list]
  - What can you now do that you couldn't before? [list]
  - What stays the same? [list — this is often bigger than you think]
→ RESPONSE: [adapt to new constraints, exploit new possibilities, continue what still works]
```

## Step 5: What Can Wait?

```
ACT NOW: [things that need immediate action — hours, not days]
ACT SOON: [things that need action this week]
CAN WAIT: [things to address later or that may resolve themselves]
IGNORE: [things that feel urgent but aren't actually important]
```

---

## Output Format

```
NOW WHAT
========

EVENT: [what happened]

WHAT CHANGED:
  + [gained]
  - [lost]
  ~ [shifted]
  ! [revealed]

GOAL IMPACT: [one sentence on how this affects your current goal]

→ MOST IMPORTANT RESPONSE: [the one thing to do first]
  THEN: [what comes after]

TIMING:
  NOW: [immediate actions]
  SOON: [this week]
  LATER: [can wait]
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Panic response** | All actions marked "ACT NOW" | Most things can wait. Force at least one item into CAN WAIT |
| **Ignoring emotional impact** | Jumping straight to planning after bad news | Pause. Name the feeling. Then plan |
| **Overreacting to good news** | Scrapping entire plan because one thing went well | The plan was working. The success is data, not a mandate to change everything |
| **Missing what stayed the same** | All focus on what changed | Most of your situation is unchanged. Anchor to stability |
| **No concrete actions** | "Reassess" or "think about" as outputs | What specifically are you going to do, where, and by when? |

---

## Integration

- If user needs to start something new after the event: route to `/strt`
- If user is stuck processing the event: route to `/unstk`
- If the event requires a decision: route to `/decide` or `/dcp`
- If the event is emotional: route to `/emotion`
- For simple "what's next" without a triggering event: route to `/wtdn` or `/nstep`
- Differs from `/wtdn`: wtdn is for ongoing work; nowwt is for after something happened
- Differs from `/next`: next classifies and routes; nowwt processes aftermath
