---
name: "smpl - Simple Analysis"
description: "Deliberately simple analysis for obvious questions. State the question, give the answer, add one caveat, done. Anti-overthinking skill."
---

# SMPL - Simple Analysis

**Input**: $ARGUMENTS

---

## When to Use This

Use `/smpl` when:
- The answer is obvious and more analysis would be waste
- The user needs a quick sanity check, not a deep dive
- Complexity would obscure rather than illuminate
- The question is well-defined and the answer is well-known
- Someone is overthinking something straightforward

Do NOT use when:
- The question is genuinely complex (use `/cmplx` instead)
- Multiple stakeholders disagree on the answer
- The "obvious" answer has failed before
- Significant resources depend on getting this right

---

## Step 1: State the Question

```
QUESTION: [the question in one sentence]
```

If you cannot state the question in one sentence, it is not a simple question. Stop and use a different skill.

---

## Step 2: Give the Answer

```
ANSWER: [the answer in one sentence]
```

If you cannot state the answer in one sentence, it is not a simple answer. Stop and use a different skill.

---

## Step 3: Add One Caveat

```
CAVEAT: [the single most important thing that could make this answer wrong]
```

One caveat. Not three. Not "several considerations." One. The most important one. If the caveat is more interesting than the answer, this isn't actually a simple question.

---

## Step 4: Done

```
SIMPLE ANALYSIS
===============
Q: [question]
A: [answer]
CAVEAT: [caveat]
```

That's it. Stop here. Do not add "further considerations." Do not suggest "deeper analysis." Do not hedge with additional caveats. The whole point of this skill is to stop.

---

## The Anti-Overthinking Test

Before using another skill instead of `/smpl`, ask:

1. Would a smart person with domain knowledge answer this in under 10 seconds?
2. Would 10 more minutes of analysis change the answer?
3. Is the risk of being wrong low enough to tolerate?

If yes to all three: use `/smpl`. Resist the urge to add depth.

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Oversimplifying a complex question** | The caveat is actually a dealbreaker | Escalate to `/cmplx` |
| **Adding depth anyway** | Output exceeds 5 lines | Delete everything after the caveat |
| **Multiple caveats** | More than one caveat listed | Pick the most important one, drop the rest |
| **Using smpl to avoid hard thinking** | Question is complex but you want to be done quickly | Complexity deserves complexity — use `/cmplx` |
| **False simplicity** | Answer seems simple but has a long history of failure | Check: has the "obvious" answer been tried and failed? |

---

## Integration

- Opposite of: `/cmplx` (use cmplx when smpl is insufficient)
- Use from: `/analyze` when the router detects a simple question
- Use from: `/meta` when the user needs to calibrate depth
- Escalate to: `/cmplx` if the caveat reveals genuine complexity
- Pair with: `/prvn` to quickly validate whether a need is real before investing effort
