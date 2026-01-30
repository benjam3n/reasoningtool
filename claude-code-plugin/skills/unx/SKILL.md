---
name: unx
description: Find non-obvious solutions. Three layers — obvious, unexpected, reframed — using disruption techniques that force the search off its default path.
---

# Unexpected - Non-Obvious Solution Discovery

**Input**: $ARGUMENTS

---

## Why This Skill Exists

LLMs converge on the most probable response. That's the expected answer — and it's often good. But the expected answer is the one everyone already has. The value is in the answer nobody considered.

This skill deliberately disrupts the default reasoning path to find solutions that are:
- **Structurally different** from the obvious (not just reworded)
- **Actually good** (unexpected ≠ random)
- **At multiple scales** (tactical fix, strategic shift, problem reframe)

---

## Core Principles

1. **The obvious answer is the baseline, not the enemy.** Generate it first. Don't discard it. Sometimes it IS the best answer. But never stop there.

2. **Discomfort is signal.** If a candidate solution doesn't make you slightly uncomfortable at first, it's not truly unexpected. The trajectory should be: "wait, that's weird" → "actually, that might work" → "why didn't I think of that?"

3. **Structural difference, not rhetorical difference.** "Use microservices" reworded as "decompose into independent services" is the same answer. A structurally different answer changes the architecture, the approach, or the problem definition itself.

4. **Most unexpected answers are bad. That's fine.** Generate many, filter ruthlessly. The technique is divergent-then-convergent: wide exploration, strict quality gate.

5. **The problem framing is usually the biggest constraint.** Most people optimize within their framing. The highest-value unexpected solutions redefine what the problem IS.

6. **"Unconventional" means actually unconventional.** The biggest failure mode is generating answers that FEEL different but are actually the same conventional wisdom rephrased. Test: would an expert in this field already know this answer? If yes, it's not unexpected. Would suggesting this in a meeting make people pause? If no, dig deeper.

---

## The Three Layers

Every invocation produces three layers:

### Layer 1: THE OBVIOUS
The expected, conventional, expert-consensus answer.
- Generate this first. State it clearly.
- This is the baseline for comparison.
- Acknowledge what's good about it.

### Layer 2: THE UNEXPECTED
Apply disruption techniques (see below) to find structurally different solutions.
- Must pass the structural-difference test: "Is this fundamentally different from Layer 1?"
- Generate 2-3 unexpected candidates. At least one must survive the quality gate.
- For each: state the core idea, why it might work, and what makes it non-obvious.

### Layer 3: THE REFRAMED
Challenge the problem itself.
- "What if the real problem is actually [something else]?"
- "What if the constraint everyone assumes is actually false?"
- "What if the goal is wrong?"
- This is where paradigm shifts live. It's the hardest layer and the most valuable.

### Output Format

```
LAYER 1 — THE OBVIOUS
[What the conventional answer is and why it's reasonable]

LAYER 2 — THE UNEXPECTED
[2-3 structurally different solutions with rationale]

LAYER 3 — THE REFRAMED
[Challenge to the problem itself — what if the question is wrong?]

STRUCTURAL DIFFERENCE CHECK:
Layer 2 differs from Layer 1 because: [specific structural difference]
Layer 3 differs from both because: [it changes the problem, not the solution]
```

---

## Disruption Techniques

Select 3-4 per invocation based on problem type. Don't apply all 10 mechanically.

### Always Apply

**1. First-Answer Rejection**
Generate the obvious answer. Acknowledge it. Then: "That's what everyone would say. What's genuinely different?"

### Core Techniques (pick 2-3)

**2. Assumption Elimination**
List every assumption in the problem statement (stated + hidden). Remove each one individually. What solutions become possible?

Example: "How to speed up our database?" → Assumptions: we need a database, speed is the bottleneck, the current architecture is correct. Remove "we need a database" → maybe the data should be computed on-the-fly, cached in memory, or restructured to not need querying.

**3. Domain Transfer**
Pick a field far from the problem domain. How do THEY solve analogous problems?

- Software problem → How does biology handle this? (Evolution = A/B testing at scale)
- Marketing problem → How does epidemiology handle this? (Viral spread models)
- Management problem → How does jazz handle this? (Improvisation within structure)

Filter: the analogy must be STRUCTURAL (same mechanism), not just SURFACE (same metaphor).

**4. Constraint Audit**
List every constraint. For each: is this physically real, or is it assumed? What if we violated it?

- "We can't change the API" → Why not? Who decided? What if we could?
- "Users expect X" → Do they? Have we tested that? What if they'd prefer Y?
- "We don't have budget for that" → Is there a version that costs nothing?

**5. Trade-off Resolution (TRIZ-style)**
Identify the core trade-off everyone accepts. Then refuse to accept it.

- "Speed vs quality" → What architecture gives BOTH? (Answer: parallel review, incremental deployment)
- "Simple vs powerful" → What interface makes power simple? (Answer: progressive disclosure)
- "Cheap vs good" → What makes good cheap? (Answer: automation, templates, reuse)

### Supplementary Techniques (use when fitting)

**6. Negation Mining**
"What's the WORST possible solution?" Then: "What's secretly useful about it?"

Often the worst solution contains an inverted insight. "Never test anything" → the kernel: maybe we're over-testing low-value paths and should test less but smarter.

**7. Role Randomization**
"How would a [randomly selected profession] approach this?"

Marine biologist, medieval historian, jazz musician, emergency room doctor, game designer, urban planner. The more distant from the problem domain, the more likely to produce genuine novelty.

**8. Provocation**
State something deliberately absurd about the problem. "PO: What if users WANTED the software to be slow?" Extract the kernel: maybe some users want deliberateness, not speed.

**9. Scale Shift**
"What if this problem was 1000x bigger? 1000x smaller?"

At 1000x: automation becomes mandatory, manual approaches collapse. What automation would you build? Can you build a small version now?

At 1/1000x: the problem might be trivial or disappear entirely. What's the minimum viable version?

**10. Temporal Displacement**
"How will this be solved in 2050? How was it solved in 1950?"

The 2050 answer reveals what's currently assumed-impossible but might not be. The 1950 answer reveals simpler approaches that were abandoned for reasons that may no longer apply.

---

## Technique Selection Guide

| Problem Type | Best Techniques |
|-------------|----------------|
| **Technical/engineering** | Constraint audit, domain transfer, trade-off resolution |
| **Strategic/business** | Assumption elimination, temporal displacement, scale shift |
| **Creative/design** | Role randomization, provocation, negation mining |
| **Interpersonal/organizational** | Role randomization, assumption elimination, negation mining |
| **Stuck/blocked** | First-answer rejection + ANY random technique (surprise is the point) |

---

## Quality Gate

Before presenting any Layer 2 or Layer 3 candidate:

1. **Structural difference**: Is this genuinely different from Layer 1, or just reworded?
2. **Feasibility**: Could this actually work? (Unlikely is fine. Impossible is not.)
3. **Addresses the need**: Does this solve the actual problem (or a valid reframing of it)?
4. **Not obvious**: Would the user have thought of this on their own? If yes, dig deeper.
5. **Actually unconventional**: Would a domain expert already know this? If yes, it's conventional wisdom in different words. The test: would suggesting this make people pause before responding?

Reject candidates that fail any of these. Generate replacements.

---

## Known-Optimal Check

Before running disruption techniques: **does this problem have a known-optimal solution?**

- "How do I sort a list?" → Don't reinvent quicksort.
- "How do I hash a password?" → Don't suggest novel cryptography.

If a well-established optimal solution exists, say so in Layer 1 and focus Layers 2-3 on whether the problem framing is right (maybe they don't need to sort; maybe they need a different data structure).

---

## Pre-Completion Check

- [ ] Layer 1 (obvious) generated and acknowledged
- [ ] Layer 2 (unexpected) has at least 1 candidate that passes quality gate
- [ ] Layer 3 (reframed) challenges the problem definition itself
- [ ] Structural difference verified between layers
- [ ] 3-4 disruption techniques applied (not all 10)
- [ ] Known-optimal check performed
- [ ] **Conventionality check**: Would a domain expert already know every Layer 2 answer? If yes, regenerate. At least one candidate should make people pause.
