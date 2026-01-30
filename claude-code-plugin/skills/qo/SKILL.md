---
name: qo
description: Find the satisfying unresolved question that opens a document and order all questions in a dependency chain. Upstream of /write.
---

# Question Ordering

**Input**: $ARGUMENTS

---

## What This Skill Does

Before writing, you need to know: what question does this document resolve, and in what order should the reader encounter sub-questions? This skill finds both.

The writing skill assumes you already have the question and the steps. This skill finds them. Pipeline: **question_ordering → high_quality_writing**.

---

## Core Principles

1. **Problems are more satisfying than solutions as openers.** A problem creates tension — the reader wants resolution. A solution closes tension — the reader has nothing to pursue. Open with the problem.

2. **Question order is a dependency chain, not chosen by interest.** Questions have prerequisites. "Why is X needed?" requires knowing what X is. "What is X?" requires having a problem X solves. Order follows dependencies.

3. **The opening problem is found by tracing backward.** Start at the target conclusion. Ask: "What must the reader know to arrive here?" Repeat until you hit universal experience. Read the chain forward for the question order.

4. **Questions not in the dependency chain are digressions.** If a question is not a prerequisite for the conclusion, it breaks momentum. Cut it.

5. **Questions and answers have separate timing.** A question can be posed (tension created) at a different point than it is answered (tension resolved). The opening problem is posed first and answered last.

---

## The Process

### Step 1: Define the Target

What should the reader believe, know, or conclude after reading?

```
TARGET CONCLUSION: [What the reader arrives at]
TARGET READER: [Who — what do they already know/believe?]
```

### Step 2: Backward Chain

Starting from the target conclusion, trace prerequisites backward. At each step ask: **"What must the reader know or feel to arrive at this?"**

```
TARGET: [conclusion]
  ← REQUIRES: [what must be known to reach this]
    ← REQUIRES: [what must be known to reach THAT]
      ← REQUIRES: [...]
        ← REQUIRES: [universal experience — no prerequisites]
```

Stop when you reach something the reader has experienced without any setup — something with no prerequisites. This is the opening problem.

### Step 3: Validate the Opening Problem

The opening problem must pass ALL four tests:

| Test | Question | Must Be |
|------|----------|---------|
| **Universal** | Has the reader experienced this without any setup? | YES |
| **Felt** | Does stating it create tension — does the reader want resolution? | YES |
| **Unsolved** | Does the reader lack a known/obvious solution? | YES |
| **Connected** | Is this what the target conclusion ultimately resolves? | YES |

If any test fails, the chain hasn't gone back far enough, or the wrong branch was taken. Try a different prerequisite path.

**Failure modes for opening problems:**
- Reader hasn't experienced it → no recognition → no tension
- Reader already has the answer → no tension → boring
- Obvious solution exists → reader dismisses ("just do X") → stops reading
- Not connected to conclusion → document is incoherent — opens one question, answers another

### Step 4: Read the Chain Forward

The backward chain, read forward, is the question order:

```
QUESTION ORDER:
1. [Opening problem — from universal experience]
2. [First sub-question — enabled by feeling the problem]
3. [Next sub-question — enabled by answering the previous]
...
N. [Target conclusion — reader arrives here]
```

Each question should be enabled by the answer to the previous one. If a question could be asked without the prior answer, it's either in the wrong position or not in the dependency chain.

### Step 5: Map Question Timing

For each question, note when it is POSED (tension created) and when it is ANSWERED (tension resolved):

```
QUESTION MAP:
| # | Question | Posed | Answered | Span | Dependencies |
|---|----------|-------|----------|------|-------------|
| 1 | [opening problem] | Opening | End | Full document | None |
| 2 | [sub-question] | After Q1 posed | Section 2 | Short | Q1 |
| 3 | [sub-question] | After Q2 answered | Section 3 | Short | Q1, Q2 |
| ... | ... | ... | ... | ... | ... |
```

**Timing principles:**
- Opening problem: posed first, answered last (maximum tension span)
- Intermediate questions: shorter spans — posed and answered within sections
- Each answer should create the next question (momentum)
- Final answer resolves all remaining tension

### Step 6: Validate the Chain

Check each question against the six ordering principles:

| Principle | Check |
|-----------|-------|
| **Dependency** | Does each question's answer require the prior answer? |
| **Recognition first** | Is the opening from universal experience (no prerequisites)? |
| **Tension before resolution** | Is every question posed before it's answered? |
| **Escalation** | Do questions get deeper/harder as they go? (Should happen naturally from dependencies) |
| **Opening lacks solution** | Does the reader genuinely not know the answer to Q1? |
| **Answers create questions** | Does each answer create the tension that drives the next question? |

If any principle is violated, reorder or remove questions.

---

## Output Format

```
QUESTION ORDERING FOR: [document title/topic]

TARGET CONCLUSION: [what the reader should arrive at]
TARGET READER: [who]

BACKWARD CHAIN:
[target]
  ← [prerequisite]
    ← [prerequisite]
      ← [opening problem — universal experience]

OPENING PROBLEM:
[Statement of the problem]
- Universal: [why the reader has experienced this]
- Felt: [why it creates tension]
- Unsolved: [why the reader lacks a solution / why obvious solutions fail]
- Connected: [how the target conclusion resolves this]

QUESTION ORDER:
1. [Q1 — opening problem]
2. [Q2 — first sub-question, enabled by Q1]
3. [Q3 — next, enabled by Q2]
...

QUESTION MAP:
| # | Question | Posed | Answered | Span | Dependencies |
|---|----------|-------|----------|------|-------------|
| 1 | ... | ... | ... | ... | ... |

VALIDATION:
- [ ] Dependency: each question requires prior answer
- [ ] Recognition first: opening from universal experience
- [ ] Tension before resolution: every question posed before answered
- [ ] Escalation: questions deepen naturally
- [ ] Opening unsolved: reader genuinely doesn't know Q1's answer
- [ ] Answers create questions: each answer drives the next

READY FOR: /write [topic]
```

---

## Pre-Completion Check

- [ ] Target conclusion and reader defined
- [ ] Backward chain reaches universal experience
- [ ] Opening problem passes all four tests (universal, felt, unsolved, connected)
- [ ] Question order follows dependency chain
- [ ] No questions outside the dependency chain (digressions removed)
- [ ] Question map includes timing (posed/answered) for each question
- [ ] All six ordering principles validated
- [ ] Output includes "READY FOR: /write"
