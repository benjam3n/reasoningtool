---
name: question_about_guesses
description: Generate high-quality questions about identified guesses. Applies quality criteria and "why continue?" gate to prevent low-value questioning.
---

# Question About Guesses

**Input**: $ARGUMENTS (guesses from /guess_generation)

---

## Core Principle

Guesses come FIRST (from /guess_generation). Questions come SECOND (this procedure).

Questions are tools to probe guesses, not open-ended exploration.

---

## Step 1: Review Incoming Guesses

List guesses to question:
| # | Guess | Type | Confidence | Priority |
|---|-------|------|------------|----------|
| 1 | ... | ... | ... | ... |
| 2 | ... | ... | ... | ... |

---

## Step 2: Question Quality Criteria

Before generating ANY question, it must pass these criteria:

### Generativity
Does this question open new territory?

| Level | Description | Test |
|-------|-------------|------|
| HIGH | Opens multiple new lines of inquiry | "If answered, spawns 3+ follow-ups" |
| MEDIUM | Opens one clear follow-up | "If answered, spawns 1-2 follow-ups" |
| LOW | Dead end | "Answering this leads nowhere" |

**Minimum**: MEDIUM

### Specificity
Is it pointed enough to get useful answers?

| Level | Description | Test |
|-------|-------------|------|
| HIGH | Clear what counts as answer | "I can picture what answering looks like" |
| MEDIUM | Somewhat vague but addressable | "Answer would be somewhat fuzzy" |
| LOW | Too abstract to answer meaningfully | "No one could really answer this" |

**Minimum**: MEDIUM

### Depth (Direction)
Does it go UPSTREAM (toward causes) or SIDEWAYS?

| Direction | Description | Value |
|-----------|-------------|-------|
| UPSTREAM | Traces toward root causes | PROCEED |
| SIDEWAYS | Related but not causal | SKIP - distraction |
| DOWNSTREAM | Toward consequences | SKIP - wrong direction |

**Required**: UPSTREAM

### Answerability
Can this actually be answered?

| Level | Description | Test |
|-------|-------------|------|
| ANSWERABLE | Can be grounded in evidence/observation | "There's something to look at" |
| PARTIAL | Some aspects can be answered | "Parts of this are checkable" |
| UNANSWERABLE | Rhetorical, too abstract, unknowable | "No possible evidence" |

**Minimum**: PARTIAL

---

## Step 3: "Why Continue?" Gate

**Default is STOP, not CONTINUE.**

Before generating each question, explicitly answer:

```
Proposed question: "[question]"

Gate Check:
1. Is this UPSTREAM? [ YES / NO ]
   → If NO: STOP - "sideways drift"

2. Is it DIFFERENT from previous questions? [ YES / NO ]
   → If NO: STOP - "repetitive"

3. Is it ANSWERABLE? [ YES / NO / PARTIAL ]
   → If NO: MARK as GROUND/UNKNOWN, stop this branch

4. Would the answer MATTER? [ YES / NO ]
   → If NO: DEPRIORITIZE - low leverage

Decision: [ PROCEED / SKIP ]
Reason: [why]
```

---

## Step 4: Stop Criteria

**STOP generating questions when they become:**

### Repetitive
- Semantically similar to earlier question
- Answer would be same as earlier answer
- Just changing word order or synonyms

**Action**: Mark as LOOP, don't continue

### Sideways
- About a related concept, not a cause
- Answering wouldn't explain the guess
- Feels like "while we're here, what about X?"

**Action**: Note as tangent, return to main line

### Unanswerable
- Purely definitional with no empirical content
- Infinite regress that can't terminate
- Question assumes false dichotomy

**Action**: Mark as GROUND (definitional) or UNKNOWN (empirical but inaccessible)

### Low-Value
- Even if we knew, so what?
- Doesn't inform the root guess
- Curiosity-driven rather than problem-driven

**Action**: Deprioritize, explore only if nothing better

---

## Step 5: Type-Specific Questions

Match questions to guess types:

| Guess Type | Core Questions |
|------------|----------------|
| **Factual** | What's the source? How was it measured? When was it verified? |
| **Causal** | What else could cause this? Is it correlation? What's the mechanism? |
| **Predictive** | What's the base rate? What similar predictions have you made? What would falsify this? |
| **Normative** | Whose values? What if you dropped the "should"? What's the alternative? |
| **Modal** | What makes it possible/impossible? What would change that? Have you tested it? |
| **Relational** | By what measure? What's the reference point? Is the comparison fair? |
| **Intentional** | How do you know their mind? What behavior shows this? Could you be projecting? |
| **Meta** | How do you know you know? What would change your mind? Have you been wrong about this before? |

---

## Step 6: Generate Questions (With Gate)

For each high-priority guess:

```
Guess: "[guess]"
Type: [factual/causal/etc]

Question 1: [question]
├── Gate: UPSTREAM? [Y] DIFFERENT? [Y] ANSWERABLE? [Y] MATTERS? [Y]
├── Quality: Generativity [H/M/L] Specificity [H/M/L]
└── Decision: PROCEED

Question 2: [question]
├── Gate: UPSTREAM? [N] - sideways drift
└── Decision: SKIP

Question 3: [question]
├── Gate: UPSTREAM? [Y] DIFFERENT? [N] - similar to Q1
└── Decision: SKIP - repetitive

... continue until hitting stop criteria ...

STOP: [which criterion triggered]
```

---

## Step 7: After-Questioning Results Are Guesses

**Critical**: When the user answers questions, those answers are ALSO GUESSES.

Do NOT treat answers as conclusions. Mark them as:
- "Current working guess" (not "conclusion")
- "User reports [X]" (not "X is true")

The questioning loop:
1. Generate guesses
2. Question guesses
3. Get answers (which are new guesses)
4. Question new guesses
5. Repeat until hitting stop criteria

---

## Output Format

```
## Guesses Received
[List from /guess_generation]

## Questions Generated (Gated)

### For Guess: "[guess 1]"
| Question | Gate Check | Quality | Decision |
|----------|------------|---------|----------|
| ... | UPSTREAM/DIFF/ANS/MATTER | GEN/SPEC | PROCEED/SKIP |

### For Guess: "[guess 2]"
...

## Questions That Passed Gate
[Final list of questions to ask]

## Stop Criteria Triggered
[Which guesses stopped questioning and why]

## Note for Next Step
All answers to these questions are also guesses.
→ Mark as "current working guess" not "conclusion"
```

---

## Next Procedure

If questions remain:
→ Ask user the questions
→ Process answers as new guesses
→ INVOKE: /guess_generation [new claims from answers]

If questioning complete:
→ INVOKE: /araw [with current working guesses]

---

**Execute now**: Apply gate to each guess and generate questions.
