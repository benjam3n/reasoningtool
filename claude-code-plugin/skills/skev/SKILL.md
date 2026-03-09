---
name: "skev - Skill Evaluation"
description: Evaluates the quality and effectiveness of a procedure, skill, or method. Tests on multiple inputs, measures efficiency, identifies failure modes, and rates overall effectiveness.
---

# Skill Evaluation

**Input**: $ARGUMENTS

---

## Step 1: State the Skill's Purpose

Define what the skill/procedure/method is supposed to accomplish.

```
SKILL: [Name or description of the skill]
STATED PURPOSE: [What it claims to do]
ACTUAL PURPOSE: [What it really does — may differ from stated]
SUCCESS CRITERIA: [What would a perfect execution look like?]
```

---

## Step 2: Test on 3+ Inputs

Run the skill against diverse inputs to see how it performs.

```
TEST 1 — [input type: easy/typical/edge case]:
  Input: [description]
  Output: [what the skill produced]
  Quality: [1-5] — [why]

TEST 2 — [input type]:
  Input: [description]
  Output: [what the skill produced]
  Quality: [1-5] — [why]

TEST 3 — [input type]:
  Input: [description]
  Output: [what the skill produced]
  Quality: [1-5] — [why]

AVERAGE QUALITY: [mean score]
VARIANCE: [How consistent is quality across inputs?]
```

---

## Step 3: Assess Efficiency

Measure the cost of using this skill relative to its output.

```
TIME/EFFORT: [How much effort does the skill require?]
COMPLEXITY: [Is the skill harder to use than it needs to be?]
OVERHEAD: [Setup, prerequisites, or context needed before the skill works]
EFFICIENCY RATIO: [Output quality / effort required]

SIMPLIFICATION POSSIBLE: [Could the same result be achieved with fewer steps?]
```

---

## Step 4: Identify Failure Modes

Find the ways this skill breaks, degrades, or misleads.

```
FAILURE MODES:
1. [Failure mode 1] — trigger: [what causes it] — severity: [HIGH/MEDIUM/LOW]
2. [Failure mode 2] — trigger: [what causes it] — severity: [HIGH/MEDIUM/LOW]
3. [Failure mode 3] — trigger: [what causes it] — severity: [HIGH/MEDIUM/LOW]

SILENT FAILURES: [Does the skill ever produce bad output that looks good?]
GRACEFUL DEGRADATION: [Does the skill fail obviously or subtly?]
```

---

## Step 5: Compare to Alternatives

Benchmark against other ways to accomplish the same thing.

```
ALTERNATIVES:
1. [Alternative 1] — strengths vs. this skill: [what] — weaknesses: [what]
2. [Alternative 2] — strengths vs. this skill: [what] — weaknesses: [what]

WHEN THIS SKILL WINS: [Scenarios where this is the best option]
WHEN ALTERNATIVES WIN: [Scenarios where something else is better]
```

---

## Step 6: Rate Overall Effectiveness

```
OVERALL RATING: [1-5]

STRENGTHS:
- [Strength 1]
- [Strength 2]

WEAKNESSES:
- [Weakness 1]
- [Weakness 2]

VERDICT: [KEEP AS-IS / IMPROVE / REPLACE / RETIRE]
IMPROVEMENT SUGGESTIONS: [If IMPROVE, what specifically should change]
```

---

## Integration

Use with:
- `/cand` -> Evaluate multiple skills as candidates for the same job
- `/ctgp` -> Check if the skill fills a gap or adds redundancy
- `/ratn` -> Build a rationale for keeping or retiring the skill
