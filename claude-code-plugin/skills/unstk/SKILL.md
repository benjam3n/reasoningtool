---
name: "unstk - Get Unstuck"
description: "Diagnose why you're blocked and get concrete unblocking actions based on the type of block: information gap, decision paralysis, emotional block, skill gap, or wrong approach."
output:
  format: "prose"
---

# UNSTK - Get Unstuck

**Input**: $ARGUMENTS

---

## Core Principles

1. **All blocks have a type.** "I'm stuck" feels formless, but every block falls into a small number of categories. Name the type and the solution becomes obvious.

2. **The block you report is rarely the real block.** "I can't decide" often means "I'm afraid of the consequences." "I don't know how" often means "I don't want to do it this way." Check one level deeper.

3. **Speed over perfection.** The goal is to get moving, not to find the optimal path. A mediocre unblock that happens now beats a perfect unblock you think about for another hour.

4. **Stuck longer than 30 minutes means the approach is wrong.** Not always, but often enough that it's worth treating as a rule.

---

## Step 1: State the Block

```
STUCK ON: [what you're trying to do — from $ARGUMENTS]
STUCK BECAUSE: [why you can't move forward — user's stated reason]
HOW LONG: [how long you've been stuck]
```

## Step 2: Diagnose the Block Type

Test against each type. The first one that fits is your diagnosis.

### Type A: Information Gap
**Test**: "Is there a specific fact, answer, or piece of data that, if you had it, would unblock you?"
```
DIAGNOSIS: INFORMATION GAP
MISSING: [what you need to know]
```

**Unblocking actions:**
1. Name the exact question you need answered. Search for the answer for 15 minutes max. If you don't find it, ask someone who knows.
2. If you can't name the question: write down everything you DO know. The gap will become visible.

### Type B: Decision Paralysis
**Test**: "Do you know your options but can't pick one?"
```
DIAGNOSIS: DECISION PARALYSIS
OPTIONS: [the options you're stuck between]
```

**Unblocking actions:**
1. If the decision is reversible: pick the one you can start fastest. You can switch later.
2. If the decision is irreversible: give yourself a hard deadline (15 minutes). Use that time to list pros/cons. When the timer ends, pick. The cost of not deciding is almost always higher than picking the wrong option.

### Type C: Emotional Block
**Test**: "Do you know what to do but feel unable to do it? Are you avoiding it?"
```
DIAGNOSIS: EMOTIONAL BLOCK
FEELING: [fear, anxiety, perfectionism, resentment, boredom, exhaustion]
```

**Unblocking actions:**
1. Name the emotion out loud or in writing. "I'm avoiding this because I'm afraid it won't be good enough." Naming it reduces its power.
2. Shrink the task to something so small it doesn't trigger the emotion. Not "write the report" but "open the document and write one bad sentence."

### Type D: Skill Gap
**Test**: "Do you know what needs to be done but not HOW to do it?"
```
DIAGNOSIS: SKILL GAP
NEED TO DO: [the task]
MISSING SKILL: [what you don't know how to do]
```

**Unblocking actions:**
1. Find the smallest working example of what you're trying to do. Copy it. Modify it. Learn by doing, not by studying.
2. Ask for help from someone who has the skill. Not "teach me everything" but "can you show me how to do this one thing?"

### Type E: Wrong Approach
**Test**: "Have you been trying the same general approach repeatedly without progress?"
```
DIAGNOSIS: WRONG APPROACH
CURRENT APPROACH: [what you've been trying]
EVIDENCE IT'S WRONG: [why it's not working]
```

**Unblocking actions:**
1. List three completely different ways to reach the same goal. Pick the one most unlike what you've been doing. Try that.
2. Ask: "If I couldn't do it this way at all, what would I do instead?" Do that instead.

## Step 3: Check One Level Deeper

```
STATED BLOCK: [what user said]
REAL BLOCK: [what it actually is, after testing]
MATCH: [yes/no]
```

If they don't match, re-diagnose with the real block.

## Step 4: Deliver the Unblock

```
GET UNSTUCK
===========

BLOCK TYPE: [A/B/C/D/E] — [name]
THE BLOCK: [one sentence]

→ DO THIS: [primary unblocking action]
→ OR THIS: [secondary unblocking action]

TIME BOX: [how long to spend on the unblocking action before reassessing]
```

---

## Nuclear Option

If stuck for more than 30 minutes, or if the user has already tried the standard unblocking actions:

```
NUCLEAR OPTION
==============
You've been stuck too long. Try the opposite.

- If you've been thinking: stop thinking and DO something, anything
- If you've been doing: stop doing and THINK about whether this is right
- If you've been working alone: get another person involved
- If you've been asking others: make a decision yourself
- If you've been adding: remove something instead
- If you've been going forward: go back to the last point where things worked

The opposite of what isn't working is more likely to work than
doing the same thing harder.
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Misdiagnosed block type** | Unblocking action doesn't help | Re-run Step 2 with the next type down |
| **Multiple block types** | More than one type fits | Address them in order: information gap first, then decision, then emotion |
| **Block is external** | Someone else controls the blocker | What can you do WITHOUT that person/thing? Do that instead |
| **User keeps analyzing instead of acting** | Still talking after Step 4 | "Stop. Do the action. Come back after." |
| **The block is "I don't want to do this"** | None of the types fit | That's not a block, that's a signal. Maybe the task is wrong. Consider `/reframe` |

---

## Integration

- If user isn't stuck but needs next steps: route to `/wtdn` or `/nstep`
- If user is stuck at the very beginning: route to `/strt`
- If the block is a complex problem: route to `/diagnose`
- If the block is a decision: route to `/dcp` or `/decide`
- For emotional blocks that run deep: route to `/emotion`
- Differs from `/diagnose`: diagnose is for broken systems; unstk is for blocked people
