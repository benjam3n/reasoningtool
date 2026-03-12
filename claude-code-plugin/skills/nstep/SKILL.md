---
name: "nstep - Minimal Next Step"
description: "The absolute simplest next-step skill. What are you trying to do? What's one thing you can do in the next 5 minutes? Do that."
output:
  format: "prose"
---

# NSTEP - Minimal Next Step

**Input**: $ARGUMENTS

---

## Core Principles

1. **Action, not analysis.** This skill exists for when you need to move, not think. If you're here, you've probably already thought enough.

2. **Five minutes.** The next step must be completable in five minutes or less. If it's bigger than that, it's not a step, it's a project.

3. **Any forward motion counts.** The step doesn't need to be optimal. It doesn't need to be the most important thing. It just needs to move you closer to the goal than you are right now.

---

## The Whole Skill

**1. What are you trying to do?**

```
GOAL: [one sentence — from $ARGUMENTS]
```

**2. What's one thing you could do in the next 5 minutes that moves you forward?**

```
→ DO THIS: [one concrete action, completable in ≤5 minutes]
```

**3. Do that.**

---

## If You Can't Think of Anything

Your next step is: **describe your goal to someone, or write it down.**

That's it. Write a single paragraph about what you're trying to do and why you're stuck. The act of putting it into words will either:
- Reveal the next step (most common), or
- Give you something to show someone who can help

```
→ DO THIS: Open a blank document or message. Write "I'm trying to [goal] but I'm stuck because [reason]." Send it to someone or save it. That's your step.
```

---

## Output Format

```
NEXT STEP
=========
GOAL: [what you're trying to do]
→ DO THIS NOW: [one action, ≤5 minutes]
```

That's the entire output. No analysis. No alternatives. No context.

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Step is too big** | Takes more than 5 minutes | Make it smaller. What's the first part of that step? |
| **Step is vague** | "Work on it" or "think about it" | What specifically? Open what? Write what? Send what to whom? |
| **Gave multiple steps** | Output has more than one action | Delete all but the first one |
| **Started analyzing** | You're reading this table instead of doing the step | Stop reading. Do the step. |

---

## Integration

- If the user needs more structure: route to `/wtdn`
- If the user is stuck, not just needing a step: route to `/unstk`
- If something just happened and they need to respond: route to `/nowwt`
- If they don't know where to start at all: route to `/strt`
- Differs from `/wtdn`: wtdn diagnoses situation and gap; nstep skips all that
- Differs from `/next`: next is a sub-orchestrator that classifies and routes; nstep gives one action immediately
- This is the fastest skill in the toolkit. If it takes more than 30 seconds, something went wrong.
