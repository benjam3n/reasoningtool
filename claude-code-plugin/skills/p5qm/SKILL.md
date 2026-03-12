---
name: "p5qm - Pick 5 Question Me"
description: "Interactive skill selection through elimination questions. Asks 3-5 discriminating questions to narrow the full library down to 5 targeted skills. Standalone implementation of the QUESTION algorithm from /pick with N=5."
tier: "tier4"
categories: ["Meta & Navigation"]
tags: ["shortcut", "pick", "discovery", "question", "interactive", "elimination"]
output:
  format: "prose"
---

# Pick 5 Question Me

**Input**: $ARGUMENTS

---

## Core Principles

1. **Questions are filters, not surveys.** Each question must eliminate at least 50% of remaining candidates. A question that eliminates 10% is not worth asking. Maximize information gain per question.

2. **Binary and multiple-choice only.** Open-ended questions produce ambiguous answers that are hard to filter on. Every question must have 2-5 discrete options, each mapping to a clear pool reduction.

3. **Three questions should suffice.** With good questions, 3 binary questions reduce the pool by 87.5%. For a library of 400+ skills, 3-4 questions narrow to a manageable candidate set. 5 questions is the maximum — after that, just pick.

4. **Implicit answers from context.** If $ARGUMENTS contains information that answers a question, skip that question and apply the filter automatically. Don't ask what you already know.

5. **Elimination, then quality ranking.** Questions eliminate; they don't rank. After elimination narrows the pool, use the USEFUL algorithm (tier + connectivity + breadth + depth) to pick the best 5 from survivors.

---

## Phase 1: Context Extraction

Before asking questions, extract any implicit answers from $ARGUMENTS.

```
[A] CONTEXT: [from $ARGUMENTS]

[B] IMPLICIT_ANSWERS:
    Step 1: Does context reveal the user's PURPOSE?
        (a) understand → analysis skills
        (b) decide → decision skills
        (c) create → creation skills
        (d) fix → diagnostic skills
        → ANSWER: [a/b/c/d/none]

    Step 2: Does context reveal the DOMAIN?
        (a) technical
        (b) business
        (c) personal
        (d) any
        → ANSWER: [a/b/c/d/none]

    Step 3: Does context reveal the SCOPE?
        (a) specific project/task
        (b) general capability building
        (c) a feeling or situation
        → ANSWER: [a/b/c/none]

    Step 4: Does context reveal the DEPTH?
        (a) quick answer
        (b) thorough analysis
        (c) deep dive
        → ANSWER: [a/b/c/none]

[C] QUESTIONS_SKIPPED: [list questions answered by context]
[D] POOL_AFTER_CONTEXT: [size after applying implicit filters]
```

---

## Phase 2: Discriminating Questions

Ask only the questions not already answered by context. Present to user.

### Question Bank (ordered by information gain)

```
[E] QUESTION_SEQUENCE:

Q1: PURPOSE (eliminates ~75%)
    "Are you trying to:
     (a) understand something
     (b) decide something
     (c) create something
     (d) fix something?"
    Filter:
        (a) → keep analysis, exploration, research skills
        (b) → keep decision, comparison, evaluation skills
        (c) → keep creation, writing, planning skills
        (d) → keep diagnostic, debugging, recovery skills

Q2: SCOPE (eliminates ~66%)
    "Is this about:
     (a) a specific project or task
     (b) a general capability you want to build
     (c) a feeling, frustration, or situation you're in?"
    Filter:
        (a) → keep execution-oriented, project-specific skills
        (b) → keep meta-skills, frameworks, general-purpose tools
        (c) → keep emotional, navigational, self-assessment skills

Q3: DEPTH (eliminates ~50%)
    "How much time do you have?
     (a) I need a quick answer
     (b) I want a thorough analysis
     (c) I want to go as deep as possible"
    Filter:
        (a) → prefer tier1, simple-output skills; exclude deep frameworks
        (b) → prefer tier1-2, moderate-depth skills
        (c) → prefer compound skills, deep frameworks, multi-step processes

Q4: DOMAIN (eliminates ~75%, but less essential)
    "What domain?
     (a) technical / engineering
     (b) business / strategy
     (c) personal / interpersonal
     (d) doesn't matter"
    Filter:
        (a-c) → keep domain-matching skills
        (d) → no filter

Q5: NOVELTY (eliminates ~50%, optional)
    "Do you want:
     (a) proven, well-known approaches
     (b) something you probably haven't tried before"
    Filter:
        (a) → prefer tier1-2, high-connectivity
        (b) → prefer tier3-4, low-connectivity, experimental
```

---

## Phase 3: Pool Reduction and Selection

```
[F] REDUCTION_LOG:

    Starting pool: [N] skills
    Q1 answer: [X] → Pool: [N1] skills
    Q2 answer: [X] → Pool: [N2] skills
    Q3 answer: [X] → Pool: [N3] skills
    [Q4 answer: [X] → Pool: [N4] skills — if asked]
    [Q5 answer: [X] → Pool: [N5] skills — if asked]

    Final candidate pool: [N_final] skills

[G] SELECTION:
    IF pool > 5:
        → Apply USEFUL scoring (tier + connectivity + breadth + depth)
        → Take top 5
    IF pool <= 5:
        → Return all
    IF pool = 0:
        → Loosen most recent filter; retry
```

---

## Phase 4: Output

```
ALGORITHM: QUESTION
QUESTIONS ASKED: [N]
POOL REDUCTION: [starting] → [final] skills

QUESTIONS ASKED:
  Q1: [question] → Answer: [answer] → Pool: [before] → [after]
  Q2: [question] → Answer: [answer] → Pool: [before] → [after]
  [Q3-Q5 if asked...]

SKIPPED (answered by context):
  [question] → implicit answer: [answer] → Pool: [before] → [after]

PICKED 5 SKILLS (from [final pool] candidates):
  1. /[id] — [title]
     Why this survived: [which filters it passed and why it ranks high]
     Tier: [tier] | Category: [category]

  2. /[id] — [title]
     Why this survived: [filters + ranking]
     Tier: [tier] | Category: [category]

  [continue to 5...]

IF NONE FIT:
  The elimination may have been too aggressive.
  Try: /p10diverse (broad coverage) or /p10for [describe your situation]
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Low-information questions** | Question eliminates < 25% of pool | Reorder: ask highest-elimination questions first |
| **Over-elimination** | Pool reaches 0 before 5 questions asked | Loosen most recent filter; use fewer questions |
| **Open-ended questions** | Question has no discrete options | Rewrite with 2-5 concrete choices |
| **Ignoring context** | Asking a question that $ARGUMENTS already answers | Always extract implicit answers first |
| **All questions asked** | Asking 5 questions when 3 would have sufficed | Stop asking when pool < 15 — just rank |
| **Quality ranking skipped** | Returning 5 arbitrary survivors instead of best 5 | After elimination, apply USEFUL scoring to rank |

---

## Depth Scaling

| Depth | Context Extraction | Questions | Selection |
|-------|-------------------|-----------|-----------|
| 1x | None — ask all questions | 3 questions | Take first 5 from survivors |
| 2x | Extract implicit answers, skip known | 3-4 questions with elimination logging | USEFUL scoring on survivors |
| 4x | Deep context analysis + domain inference | Adaptive questions based on pool state | USEFUL scoring + justification per pick |
| 8x | Full context modeling | Custom questions designed for maximum discrimination | Multi-criteria ranking + alternative sets |

Default: 2x. These are floors.

---

## Pre-Completion Checklist

- [ ] Context from $ARGUMENTS analyzed for implicit answers
- [ ] Each question eliminates at least 50% of remaining pool
- [ ] No more than 5 questions asked
- [ ] Pool reduction logged at each step
- [ ] Final selection uses USEFUL scoring (not arbitrary)
- [ ] Exactly 5 skills returned (or all if pool < 5)
- [ ] Each pick explains why it survived the filters

---

## Integration

- **Shortcut for**: `/pick 5 question me $ARGUMENTS`
- **Use when**: You don't know what you need and want guided discovery
- **Routes to**: The 5 picked skills; re-run with different answers for different results
- **Related**: `/p10for` (situation-based, no questions needed), `/meta` (orientation)
- **Differs from /p10for**: for infers needs from a situation description; qm asks explicitly
- **Differs from /meta**: meta provides orientation to the whole system; qm narrows to 5 specific skills
- **Differs from /p5want**: want assumes a desire is stated; qm asks questions to discover it
