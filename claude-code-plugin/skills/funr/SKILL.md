---
name: "funr - Fun/Exploration Reasoning"
description: "Reason about what's interesting, playful, or worth exploring for its own sake. Follow curiosity threads, note unexpected connections, and assess what exploration reveals."
output:
  format: "prose"
---

# FUNR - Fun/Exploration Reasoning

**Input**: $ARGUMENTS

---

## Step 1: Identify What's Curious or Surprising

```
SUBJECT: [what we're exploring]

CURIOSITY HOOKS:
  1. [what's surprising or unexpected about this]
     WHY SURPRISING: [what expectation it violates]
  2. [what seems odd, unusual, or counterintuitive]
     WHY INTERESTING: [what makes this worth poking at]
  3. [what nobody seems to have asked about this]
     WHY UNASKED: [blind spot | too obvious | too weird]
```

Curiosity is a signal. When something feels surprising, that means your model of the world has a gap. The gap is where learning happens.

---

## Step 2: Follow the Thread of Interest

Pick the most interesting hook from Step 1 and pull on it:

```
THREAD: [the curiosity hook being followed]

PULL 1: [first question that arises]
  FINDING: [what you discover or hypothesize]

PULL 2: [next question that follows from the finding]
  FINDING: [what you discover]

PULL 3: [next question]
  FINDING: [what you discover]

PULL 4: [if the thread is still alive]
  FINDING: [what you discover]
```

Follow the thread until it either dead-ends or connects to something unexpected. Don't force it — if it dies, note where and why.

---

## Step 3: Explore Without Utility Pressure

```
TANGENTS WORTH NOTING:
  1. [tangent] — INTERESTING BECAUSE: [why, even if not "useful"]
  2. [tangent] — INTERESTING BECAUSE: [reason]

WHAT-IF EXPERIMENTS:
  1. What if [assumption] were reversed?
     RESULT: [what world would that create]
  2. What if [constraint] didn't exist?
     RESULT: [what becomes possible]
  3. What if [this thing] were combined with [unrelated thing]?
     RESULT: [what hybrid emerges]
```

This step is explicitly permission to think without justifying immediate utility. Not everything needs to be productive. Exploration that doesn't lead anywhere still updates your intuition.

---

## Step 4: Note Unexpected Connections

```
UNEXPECTED CONNECTIONS:
  1. [thing A] connects to [thing B] via [mechanism]
     SURPRISING BECAUSE: [why this connection wasn't obvious]
     IMPLICATIONS: [what this connection might mean]
  2. [thing A] is structurally similar to [thing C]
     SHARED STRUCTURE: [the pattern they share]
     IMPLICATIONS: [what transfers from one domain to the other]
```

The highest-value output of exploration is often an unexpected connection between previously unrelated ideas. These connections are where novel insights come from.

---

## Step 5: Assess Whether Exploration Revealed Anything

```
EXPLORATION RESULTS
===================
STARTED WITH: [original subject]
EXPLORED: [what threads were followed]

DISCOVERIES:
  1. [genuine insight or novel connection]
     VALUE: [immediately useful | stored for later | pure interest]
  2. [discovery]
     VALUE: [assessment]

DEAD ENDS:
  1. [thread that didn't lead anywhere]
     WHY IT DIED: [reason]
     STILL INTERESTING: [yes | no]

UPDATED UNDERSTANDING:
  BEFORE: [what you thought before exploring]
  AFTER: [what you think now]
  DELTA: [what changed and why]

WORTH FURTHER EXPLORATION: [yes | no]
  IF YES: [which thread to pull next]
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Forced fun** | Exploration feels mechanical | Stop following the script — what actually interests you here? |
| **Utility anxiety** | Every tangent justified by usefulness | Explicitly permit purposelessness for this skill |
| **Shallow exploration** | Many threads touched, none followed deeply | Pick one thread and follow it 4+ pulls deep |
| **No surprises** | Everything found was predictable | You're not exploring — you're confirming. Look for what violates expectations |
| **Abandoned threads** | Interesting threads dropped without noting why | Document dead ends — they're information too |

---

## Integration

- Use with: `/sysk` to explore system behaviors playfully
- Use with: `/difr` to explore what makes similar things interestingly different
- Use with: `/skcl` to explore novel skill combinations
- Use from: `/search` when open-ended exploration is the goal
- Differs from `/se`: funr follows curiosity without structure; se systematically enumerates a space
