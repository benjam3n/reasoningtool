---
name: "ezy - Easy Mode Analysis"
description: "Break any problem into the easiest possible steps — no jargon, no prerequisites, no assumed knowledge. Designed for when the user is overwhelmed, new to the domain, or needs the simplest possible path forward."
output:
  format: "prose"
---

# Easy Mode Analysis

**Input**: $ARGUMENTS

---

## Core Principles

1. **Easy means fewer decisions, not less quality.** The goal isn't a worse analysis — it's one with fewer moving parts. Reduce the number of choices the user has to make. Reduce the cognitive load at each step. The output should be just as correct, just more accessible.

2. **If you need a prerequisite, you're not easy enough.** Every step must be followable by someone with zero domain expertise. If a step requires understanding a concept, define it in that step. If a step requires a tool, name the specific tool. "Analyze the situation" is not an easy step. "Write down the three things that bother you most about this" is an easy step.

3. **One step, one action.** Complex steps are what makes things hard. "Research the market, identify competitors, and position your product" is three steps disguised as one. Easy mode separates them and puts them in order.

4. **Overwhelm is the enemy, not ignorance.** People asking for easy mode aren't stupid — they're overloaded. The problem has too many dimensions, too many unknowns, or too much jargon. Easy mode reduces dimensions until the problem is handleable.

5. **The easy path still gets you there.** Easy mode is not a toy version. It reaches the same destination through a simpler route. If the easy path produces a significantly worse outcome, it's not easy mode — it's bad advice.

---

## Phase 1: Assess Overwhelm Source

```
[E1] PROBLEM: [what the user needs to do]
[E2] OVERWHELM_SOURCE: [what makes this feel hard — too many options? unfamiliar domain? unclear first step? emotional weight? time pressure?]
[E3] USER_KNOWS: [what they already understand — don't re-explain this]
[E4] USER_NEEDS: [the simplest possible description of what they actually need]
```

---

## Phase 2: Simplify the Problem

Reduce the problem to its minimum viable version.

```
[E5] FULL_PROBLEM: [the problem with all its complexity]
[E6] MINIMUM_PROBLEM: [the simplest version that still matters]
[E7] REMOVED: [what was stripped — and why it's safe to ignore for now]
[E8] FIRST_QUESTION: [the single most important question to answer first]
```

### Simplification Techniques

| Technique | How |
|-----------|-----|
| **Reduce options** | Instead of "choose from 20 options," narrow to 2-3 |
| **Remove conditions** | Instead of "it depends on X, Y, Z," pick the most likely scenario |
| **Sequence** | Instead of "consider all these simultaneously," order them |
| **Default** | Instead of "decide what to do about X," give a sensible default |
| **Defer** | Instead of "also handle edge case Y," note it and handle later |

---

## Phase 3: Step-by-Step Path

Generate the easiest possible steps:

```
EASY PATH
=========

STEP 1: [single, concrete action — no jargon]
  WHY: [one sentence — why this step]
  DONE_WHEN: [how to know this step is complete]

STEP 2: [single, concrete action]
  WHY: [one sentence]
  DONE_WHEN: [completion signal]

STEP 3: [single, concrete action]
  WHY: [one sentence]
  DONE_WHEN: [completion signal]

...
```

### Step Quality Rules

- **Maximum 7 steps** — if you need more, you need a simpler path
- **Each step is one action** — if it has "and" it's two steps
- **No jargon** — if a word needs defining, define it inline
- **Observable completion** — "done when" must be something you can see or check
- **No assumed tools** — if a tool is needed, name it specifically
- **Default choices included** — don't make the user choose unless they must

---

## Phase 4: If-Stuck Guide

For each step, preempt the most common place people get stuck:

```
[E-N] STEP [N] STUCK?
     MOST_COMMON_BLOCK: [what usually stops people here]
     EASY_FIX: [the simplest way past it]
     SKIP_OPTION: [can you skip this step? if so, what happens]
```

---

## Phase 5: Output

```
EASY MODE
=========

YOUR PROBLEM (simplified): [one sentence]
FIRST THING TO DO: [step 1 — the single next action]

FULL PATH:
  1. [step] — DONE WHEN: [signal]
  2. [step] — DONE WHEN: [signal]
  3. [step] — DONE WHEN: [signal]
  ...

IF YOU GET STUCK:
  Step 1: [common block → easy fix]
  Step 2: [common block → easy fix]

WHAT I SIMPLIFIED AWAY (handle later if needed):
  - [deferred complexity 1]
  - [deferred complexity 2]

READY FOR MORE DEPTH?
  → /soph for sophisticated analysis
  → /hrd for the hard version with full complexity
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Oversimplified** | Removed so much that the output is wrong or misleading | Easy means fewer decisions, not wrong decisions. Check the output is still correct |
| **Still too many steps** | More than 7 steps | Combine or defer. If you can't get below 7, the problem needs decomposing first |
| **Hidden prerequisites** | Steps that require knowledge the user doesn't have | Define every term inline. Name every tool. Assume nothing |
| **Compound steps** | Steps with "and" that are really 2-3 actions | Split every compound step |
| **No defaults** | Asking the user to make choices they can't make yet | Provide sensible defaults. "Do X (unless you have a specific reason not to)" |
| **Condescending tone** | Explaining obvious things or being patronizing | Easy mode serves overwhelmed experts too. Be direct, not simple-minded |
| **Deferred too much** | Stripped so much that the result is trivially incomplete | The easy path must still get the user to a real result |

---

## Depth Scaling

| Depth | Steps | If-Stuck Guide | Deferred Complexity | Path Options |
|-------|-------|----------------|--------------------|----|
| 1x | 3-5 | No | Listed | One path |
| 2x | 5-7 | Top blocker per step | Listed with notes | One path |
| 4x | 5-7 | Full guide | Detailed with when-to-revisit | 2 paths (easier/more complete) |
| 8x | 5-7 | Full + examples | Full with priority ordering | Multiple paths by scenario |

Default: 2x. These are floors.

---

## Pre-Completion Checklist

- [ ] Overwhelm source identified
- [ ] Problem simplified to minimum viable version
- [ ] Each step is a single, concrete action
- [ ] No jargon without inline definition
- [ ] Maximum 7 steps
- [ ] Each step has an observable completion signal
- [ ] Defaults provided where choices aren't necessary
- [ ] Deferred complexity listed (so nothing is silently lost)
- [ ] Output is still correct despite simplification

---

## Integration

- Use from: overwhelmed users, first-time encounters with a domain, "just tell me what to do"
- Routes to: `/soph` (when ready for depth), `/hrd` (full complexity version)
- Complementary: `/smpl` (simple analysis — related but /ezy focuses on step-by-step actionability)
- Differs from `/smpl`: smpl gives a simple analysis/answer; ezy gives an easy-to-follow path
- Differs from `/soph`: soph maximizes analytical depth; ezy minimizes cognitive load
- Differs from `/foht`: foht figures out how to do something; ezy makes the doing as easy as possible
