---
name: "strt - Where to Start"
description: "For when you have a goal but genuinely don't know where to begin. Find the zero-dependency starting point and take it."
---

# STRT - Where to Start

**Input**: $ARGUMENTS

---

## Core Principles

1. **The start is the thing nothing else depends on.** Every project has tasks that require other tasks to be done first. The starting point is the task that requires nothing else. Find it.

2. **Overwhelm is a starting problem, not a planning problem.** When everything feels like too much, you don't need a better plan. You need a smaller first action.

3. **Starting wrong is better than not starting.** Any starting point that teaches you something is a valid start. Perfecting your start is a form of procrastination.

4. **Clarity comes from action, not thought.** If you can't figure out where to start by thinking about it, start anywhere and the right path will reveal itself.

---

## Step 1: What's the End State?

```
GOAL: [what "done" looks like — from $ARGUMENTS]
```

Be specific. "Launch the app" is better than "finish the project." If the user can't state the end state, the starting point is: define the end state.

## Step 2: List Everything That Seems Required

```
REQUIRED (brain dump — not ordered, not filtered):
  1. [thing]
  2. [thing]
  3. [thing]
  ...
```

Don't organize. Don't prioritize. Just list every task, requirement, or thing that needs to happen. Include vague ones. Include ones you're not sure about.

## Step 3: Find the Dependencies

For each item, ask: "Does this require any other item on the list to be done first?"

```
DEPENDENCY MAP:
  [item] ← depends on nothing
  [item] ← depends on [other item]
  [item] ← depends on [other item], [other item]
  ...
```

## Step 4: Find the Zero-Dependency Item

```
ZERO-DEPENDENCY ITEMS: [items that depend on nothing else]
```

If there are multiple, pick the one that:
- Unblocks the most other items
- Is smallest in scope
- Gives you the most information about whether your plan is right

```
→ START HERE: [the one item]
  WHY: [what it unblocks or reveals]
  FIRST ACTION: [the literal first thing to do — open a file, make a call, write a sentence]
```

## Step 5: Confirm It's Actually Doable Right Now

```
CAN YOU DO THIS RIGHT NOW?
  - Do you have what you need? [yes/no — if no, THAT is the real start]
  - Do you know how? [yes/no — if no, "learn how to [X]" is the real start]
  - Is anything stopping you? [yes/no — if yes, removing that blocker is the real start]

ACTUAL START: [confirmed first action]
```

---

## Overwhelmed Start

If the user says they're overwhelmed, or the list in Step 2 has more than 10 items, or they can't complete Step 2:

```
OVERWHELMED START
=================
Skip everything above. Do this instead:

1. What's the SMALLEST possible action related to your goal?
   Not the most important. Not the most logical. The SMALLEST.
   (Examples: open the document, write one sentence, send one message, read one page)

2. Can you do it in under 5 minutes?
   If no, make it smaller.

3. → DO THAT NOW.

You don't need to know the whole path. You need to take one step.
After that step, you'll know more about what the next step should be.
```

---

## Output Format

```
WHERE TO START
==============

GOAL: [end state]

EVERYTHING REQUIRED:
  [numbered list]

DEPENDENCIES:
  [zero-dep items marked with →]

→ START HERE: [chosen starting point]
  FIRST ACTION: [literal next physical/digital action]
  THIS UNBLOCKS: [what becomes possible after]
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Planning instead of starting** | Spent >10 min on Steps 2-3 | Switch to Overwhelmed Start |
| **No zero-dependency items** | Every item depends on another | You have a circular dependency. Break one arbitrarily |
| **Start is too big** | First action takes more than 1 hour | Break it down further. What's the first 15 minutes? |
| **"I need to research first"** | Research as starting point | Fine, but scope it: research WHAT, for HOW LONG, looking for WHAT ANSWER |
| **Can't list requirements** | Step 2 produces nothing | You don't understand the goal yet. Start: talk to someone who does, or write down what you don't know |

---

## Integration

- If user is stuck mid-project (not at the start): route to `/unstk`
- If user knows where to start but needs the next step: route to `/wtdn` or `/nstep`
- If the goal itself is unclear: route to `/gu`
- For complex project planning: route to `/de` or `/to`
- Differs from `/next`: next assumes you're mid-process; strt assumes you haven't begun
