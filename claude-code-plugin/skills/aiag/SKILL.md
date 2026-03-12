---
name: "aiag - AI Agent Analysis"
description: Analyzes suitability for AI agents. Assesses which tasks are automatable, evaluates reliability requirements, designs human oversight, and plans for failure modes.
output:
  format: "prose"
---

# AI Agent Analysis

**Input**: $ARGUMENTS

---

## Step 1: Identify the Work

Break down what needs to be done into discrete tasks.

```
DOMAIN: [Area of work]
GOAL: [What the AI agent would accomplish]

TASKS:
1. [Task] — frequency: [how often], complexity: [low/medium/high]
2. [Task] — frequency: [how often], complexity: [low/medium/high]
3. [Task] — frequency: [how often], complexity: [low/medium/high]
```

---

## Step 2: Assess Automatability

For each task, evaluate AI suitability.

```
HIGHLY AUTOMATABLE:
- [Task] — why: [structured input, clear rules, pattern-matchable]

PARTIALLY AUTOMATABLE:
- [Task] — AI does: [part], human does: [part]

NOT AUTOMATABLE (yet):
- [Task] — why: [requires judgment, novel situations, physical presence, trust]
```

Criteria for automatability: structured inputs, clear success criteria, tolerance for occasional errors, availability of training data or examples.

---

## Step 3: Evaluate Reliability Requirements

```
ERROR TOLERANCE BY TASK:
- [Task]: [high tolerance — errors are cheap to fix]
- [Task]: [low tolerance — errors cause real damage]

FAILURE CONSEQUENCES:
- If AI gets [task] wrong: [what happens]
- Worst case scenario: [describe]
- Recovery cost: [low/medium/high]
```

---

## Step 4: Design Human Oversight

```
OVERSIGHT MODEL:
- [Task]: [No oversight / spot-check / review before action / human-in-the-loop]

ESCALATION TRIGGERS:
- AI should escalate when: [condition 1]
- AI should escalate when: [condition 2]
- AI should stop when: [condition]

FEEDBACK LOOP:
- How humans correct AI: [mechanism]
- How AI improves from corrections: [mechanism]
```

---

## Step 5: Plan for Failure Modes

```
FAILURE MODES:
1. [Mode: e.g., hallucination, drift, edge case] — likelihood: [low/medium/high]
   Mitigation: [approach]
2. [Mode] — likelihood: [low/medium/high]
   Mitigation: [approach]
3. [Mode] — likelihood: [low/medium/high]
   Mitigation: [approach]

GRACEFUL DEGRADATION:
- If AI is unavailable: [fallback plan]
- If AI quality drops: [detection method and response]
```

---

## Step 6: Capability Projection

```
CURRENT STATE: [What AI can do today for this use case]
6-MONTH PROJECTION: [What's likely to improve]
LONG-TERM OUTLOOK: [What changes if AI capabilities grow significantly]

RECOMMENDED APPROACH:
1. Start with: [lowest-risk, highest-value automation]
2. Expand to: [next tier once trust is established]
3. Monitor: [key metrics to track AI performance]
```

---

## Integration

Use with:
- `/indv` -> Analyze the human roles alongside AI
- `/tmsk` -> Design human-AI team structure
- `/vldt` -> Validate the AI agent's outputs
- `/bldk` -> Build the AI agent system incrementally
