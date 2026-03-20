---
name: "crtv - Creativity Procedure"
description: Systematic procedure for generating novel ideas. Moves through divergent generation, combinatorial play, and convergent evaluation against the original need.
output:
  format: "prose"
---

# Creativity Procedure

**Input**: $ARGUMENTS

---

## Step 1: Define the Creative Constraint

Creativity without constraint is noise. Clarify what you're creating for.

- **The need**: What problem, gap, or opportunity does this serve?
- **The constraint**: What must be true about a good solution?
- **The domain**: What space are we working in?
- **The bar**: What already exists? What would "better" or "different" look like?

```
CREATIVE BRIEF:
- Need: [what's missing or wanted]
- Constraints: [non-negotiable requirements]
- Domain: [the space we're working in]
- Current best: [what exists now that we're trying to beat or diverge from]
```

---

## Step 2: Divergent Generation — Quantity Over Quality

Generate as many ideas as possible. No filtering. No judgment.

**Techniques** (use at least 2):

- **Free list**: Write 10+ ideas as fast as possible, no editing
- **SCAMPER**: Take something existing and Substitute / Combine / Adapt / Modify / Put to other use / Eliminate / Reverse
- **Random input**: Pick an unrelated word or concept and force a connection to the problem
- **Analogy transfer**: How do other domains solve a similar problem?
- **Constraint removal**: If you had no limits, what would you do? Then add limits back.
- **Worst idea**: What's the worst possible solution? Invert it.

```
RAW IDEAS (unfiltered):
1. [idea]
2. [idea]
3. [idea]
...
(aim for 12-20 minimum)
```

RULE: If every idea feels "reasonable," you're not being divergent enough. Include at least 3 ideas that feel absurd.

CACHED TAKE CHECK: After generating your list, look at the first 3-5 ideas. These are almost certainly the ideas anyone would think of — they're cached in the training data, not generated from the constraints. Mark them. They might still be useful, but they're not creative. If your "creative" output is the first thing that comes to mind, it's retrieval, not generation. Push past the cached layer before claiming you've been divergent.

---

## Step 3: Combinatorial Play

Take promising fragments and combine them:

- Merge idea X's mechanism with idea Y's audience
- Take the best feature of 3 different ideas into one
- Ask: "What if [idea A] but also [idea B]?"
- Identify hidden connections between seemingly unrelated ideas

```
COMBINATIONS:
- [idea X] + [idea Y] = [new hybrid idea] — interesting because [why]
- [idea A] + [idea B] + [idea C] = [synthesis] — interesting because [why]
...
```

---

## Step 4: Convergent Evaluation

Now apply judgment. Rate each surviving idea on two axes:

- **Novelty** (1-5): How different is this from what exists? (Score 1 if this is the idea anyone in the field would suggest first. That's not novel — it's the default position of the discourse.)
- **Usefulness** (1-5): How well does this actually serve the need?

```
EVALUATION:
| Idea | Novelty | Usefulness | Total | Notes |
|------|---------|------------|-------|-------|
| [idea] | [1-5] | [1-5] | [sum] | [key strength/weakness] |
...
```

The sweet spot is high on both. Novel but useless is art for art's sake. Useful but unoriginal is incremental improvement. Neither is necessarily wrong, but know which you're choosing.

---

## Step 5: Develop Top Candidates

Take the top 2-3 ideas and flesh them out:

- What would this look like in practice?
- What's the first step to test or build it?
- What could go wrong?
- What makes this better than the current best?

```
CANDIDATE 1: [name/summary]
- How it works: [brief description]
- First step: [concrete next action]
- Risk: [what could go wrong]
- Edge: [why this beats what exists]

CANDIDATE 2: [name/summary]
...
```

---

## Step 6: Test Against the Original Need

Return to the creative brief from Step 1.

```
FIT CHECK:
- Does this solve the stated need? [yes/partially/no]
- Does it respect the constraints? [yes/partially/no]
- Is it genuinely better or different from what exists? [yes/partially/no]
- Would you actually use/build/ship this? [yes/maybe/no]
```

If nothing passes the fit check, return to Step 2 with what you've learned.

---

## Step 7: Creative Output

```
BEST IDEA: [the winner]
WHY: [1-2 sentences on why this is the strongest]
RUNNER-UP: [backup option]
NEXT STEP: [concrete action to move forward]
IDEAS WORTH SAVING: [any fragments or combinations worth revisiting later]
```

---

## Integration

Use with:
- `/prcp` -> Notice more before generating ideas
- `/jdgm` -> Apply structured judgment during evaluation
- `/se` -> Systematically explore the solution space before creating
- `/ma` -> Generate more ideas using morphological analysis
- `/cda` -> Use creative destruction to challenge existing solutions
