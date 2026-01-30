---
name: "pce - Procedure Engine - Comprehensive Analysis"
description: The deep analysis engine. Routes input by type, applies appropriate analysis depth, produces structured understanding and action.
---

# Procedure Engine - Comprehensive Analysis

**Input**: $ARGUMENTS

---

## Core Principles

1. **Understand before acting.** Explore the problem from multiple angles before recommending action. But don't explore forever — stop when you understand enough to act well.

2. **Route by type.** Different inputs need different treatment. A goal needs decomposition. A problem needs root cause. A decision needs comparison. Classify first.

3. **Surface the hidden.** The most important information is usually unstated — hidden assumptions, implicit constraints, presupposed beliefs. Find these before analyzing the stated content.

4. **Testable output.** Every recommendation should include how to verify it worked. Every claim should be possible to check.

5. **Action-oriented.** Analysis that doesn't lead to action is academic. End with specific, prioritized next steps.

---

## Step 1: Classify Input

What kind of thing is this?

| Type | Signal | Core Need |
|------|--------|-----------|
| **GOAL** | "I want to...", "How do I..." | Decompose and plan |
| **PROBLEM** | "Something is wrong...", "Why does..." | Diagnose and fix |
| **QUESTION** | "What is...", "Is it true that..." | Research and answer |
| **DECISION** | "Should I...", "Which option..." | Compare and choose |
| **SITUATION** | "Here's what's happening..." | Understand and respond |
| **FEELING** | "I'm frustrated/excited/confused..." | Clarify and redirect |

---

## Step 2: Surface Hidden Claims

Every input contains unstated assumptions. Find them.

- **Explicit claims**: What's directly stated
- **Implicit claims**: What's assumed but not said
- **Bundled claims**: Multiple claims packed into one statement
- **Presuppositions**: What must be true for the statement to make sense

Example: "I need to scale our database" bundles: a scaling problem exists, the database is the bottleneck, scaling the database will fix it, we have resources to scale.

**ARAW the highest-VOI hidden claim** — the one that, if wrong, changes everything.

---

## Step 3: Analyze by Type

Route to the appropriate analysis:

### GOAL
1. What's the foundational goal behind this? (trace upward)
2. What are the subgoals? (decompose downward)
3. What's the current state vs desired state?
4. What's blocking progress?
5. What's the highest-leverage next step?

→ May invoke: `/gd`, `/gjs`, `/stg`

### PROBLEM
1. What exactly is wrong? (specific symptoms)
2. When did it start? What changed?
3. What's the root cause? (ask "why" until you hit foundation)
4. What are the fix options?
5. Which fix addresses root cause, not symptoms?

→ May invoke: `/rc5w`, `/araw`, `/lpd`

### QUESTION
1. What kind of question? (factual, conceptual, evaluative)
2. What's already known?
3. What are the candidate answers?
4. What evidence supports/contradicts each?
5. What's the best current answer + confidence level?

→ May invoke: `/araw`, `/bi`, `/vbo`

### DECISION
1. What are the options? (including non-obvious ones)
2. What criteria matter? (derived from purpose)
3. How do options compare?
4. What's the recommendation?
5. How reversible is this?

→ May invoke: `/cmp`, `/evaluation_dimensions`, `/sel`

### SITUATION
1. What's happening? (neutral description)
2. What does this mean for the user's goals?
3. What options does this create?
4. What's the recommended response?

→ May invoke: `/araw`, `/grfr`, `/stg`

### FEELING
1. What's the feeling pointing at? (feelings are data about unmet needs)
2. What goal or value is threatened/served?
3. What action would address the underlying need?

→ May invoke: `/araw`, `/ve`, `/gu`

---

## Step 4: Synthesize

1. **Key findings**: What did the analysis reveal? (3-5 bullet points)
2. **Tensions**: Any unresolved conflicts between different findings?
3. **Confidence**: What are you sure about? What's uncertain?
4. **Testable predictions**: "If this analysis is correct, you should see X when Y."

---

## Step 5: Recommend Action

Specific, prioritized next steps:

1. **DO_FIRST**: [action] — [who does it] — [what it resolves]
2. **DO_NEXT**: [action] — [who] — [what it resolves]
3. **MONITOR**: [what to watch for] — [what it would mean]

Every action must be specific enough to execute without further analysis.

---

## Pre-Completion Check

- [ ] Input classified correctly
- [ ] Hidden claims surfaced and highest-VOI tested
- [ ] Analysis appropriate to type (not generic)
- [ ] Synthesis includes testable predictions
- [ ] Actions are specific and prioritized
