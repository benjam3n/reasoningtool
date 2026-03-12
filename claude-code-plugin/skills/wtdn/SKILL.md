---
name: "wtdn - What To Do Next"
description: "Simple next-step finder. No routing, no classification. State where you are, get the single most valuable next move, understand why, do it."
output:
  format: "prose"
---

# WTDN - What To Do Next

**Input**: $ARGUMENTS

---

## Core Principles

1. **Simple means simple.** This skill has no routing, no classification, no sub-orchestration. It asks a few questions and gives one answer. If the user needs complexity, they'll find it elsewhere.

2. **One move, one reason.** The output is a single action and a single reason. Not three options. Not a comparison. One thing to do and why that one.

3. **Bias toward action.** When two next moves seem equally valuable, pick the one that starts sooner and produces a visible result faster.

4. **"I don't know" is fine.** If the user can't articulate where they are, that's data. The next step is to figure out where they are.

---

## Steps

### Step 1: Where Are You Right Now?

State the current situation in one sentence based on $ARGUMENTS.

```
SITUATION: [what's happening right now — project state, problem state, or "I don't know"]
```

If the user hasn't provided enough context, ask: "Where are you right now with this? What have you done so far?"

### Step 2: What Are You Trying to Reach?

```
GOAL: [the end state or outcome they want]
```

If unclear from input, use: "What does 'done' look like?"

### Step 3: What's the Gap?

```
GAP: [the single biggest thing between SITUATION and GOAL]
```

### Step 4: What's the Single Most Valuable Next Move?

```
NEXT MOVE: [one specific action]
WHY THIS ONE: [one sentence — why this move over any other]
```

Pick the move that:
- Closes the biggest part of the gap
- Can be started immediately
- Produces a result you can see or measure

### Step 5: Do It

```
DO THIS NOW: [restate the action as a direct instruction]
TIME ESTIMATE: [how long this should take]
YOU'LL KNOW IT WORKED WHEN: [observable result]
```

---

## Quick Mode

If the user adds "quick" or wants speed, skip to three questions:

```
QUICK MODE
==========
1. Where are you? [one sentence from input]
2. What's blocking progress? [one sentence]
3. DO THIS: [one action that addresses the block]
```

No analysis. No explanation. Just the answer.

---

## Output Format

```
WHAT TO DO NEXT
===============

SITUATION: [where you are]
GOAL: [where you're headed]
GAP: [what's between]

→ NEXT MOVE: [the one thing to do]
  WHY: [one reason]
  TIME: [estimate]
  DONE WHEN: [observable result]
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Gave multiple options** | Output contains "or" or numbered alternatives | Pick one. That's the whole point |
| **Too vague** | "Work on the project" | What specific action, in what tool/place, producing what? |
| **Overthinking** | More than 2 minutes on this skill | Use Quick Mode instead |
| **User doesn't know their situation** | Can't answer Step 1 | Next move is: "Spend 5 minutes writing down what you know and don't know" |

---

## Integration

- Simpler than: `/next` (which classifies intent and routes to other skills)
- Simpler than: `/nowwt` (which handles aftermath situations)
- If user needs deeper analysis: route to `/next`
- If user is stuck, not just "what's next": route to `/unstk`
- If user just needs the absolute minimum: route to `/nstep`
