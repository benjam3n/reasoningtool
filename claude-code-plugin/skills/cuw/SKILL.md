---
name: "cuw - Come Up With"
description: Generate quality candidates when you need to come up with ideas, options, names, solutions, or approaches. Combines divergent generation with convergent filtering to produce genuinely useful output, not just long lists.
output:
  format: "prose"
---

# Come Up With

**Input**: $ARGUMENTS

---

## Interpretations

Before executing, identify which interpretation matches the user's input:

**Interpretation 1 — Generate options for a decision**: The user needs candidates to choose from — names, approaches, solutions, designs, strategies. Quality and distinctness matter more than quantity. They'll pick one.
**Interpretation 2 — Creative ideation**: The user wants novel ideas — inventions, concepts, angles, twists, possibilities. Originality matters. They want to be surprised.
**Interpretation 3 — Fill a gap**: The user has a specific slot to fill — a tagline, a title, a metaphor, a workaround, a way to phrase something. They know what "shape" the answer needs to be, they just can't find it.

If ambiguous, ask: "Are you choosing between options, looking for creative ideas, or trying to fill a specific gap?"
If clear from context, proceed with the matching interpretation.

---

## Core Principles

1. **Quantity is cheap; quality is the bottleneck.** Anyone can brainstorm 20 mediocre ideas. The hard part is generating candidates that are genuinely different from each other and genuinely good. Prioritize distinctness and quality over volume.

2. **Criteria before generation.** "Come up with a name" is underspecified. What makes a GOOD name for this? Establish what "good" means first — even briefly — so generation is targeted, not random.

3. **Diverge, then converge.** First generate broadly using multiple strategies. Then filter ruthlessly. Present only what survives.

4. **Name the generation strategy.** Don't just free-associate. Use identifiable strategies (analogy, inversion, combination, constraint removal, extreme cases, etc.) so you can tell when you've actually explored the space vs. just riffed on one theme.

5. **The best idea is often a synthesis.** After generating candidates, check whether combining elements from two good-but-flawed candidates produces something better than either alone.

6. **Surprise is signal.** If every candidate feels obvious, push harder. The user can generate obvious ideas themselves. Your value is in the non-obvious.

---

## Depth Scaling

Default: 2x. Parse depth from $ARGUMENTS if specified (e.g., "/cuw 4x [input]").

| Depth | Min Strategies Used | Min Candidates Generated | Min Presented (after filtering) | Min Synthesis Attempts |
|-------|--------------------|--------------------------|---------------------------------|------------------------|
| 1x    | 2                  | 8                        | 3                               | 0                      |
| 2x    | 3                  | 15                       | 5                               | 1                      |
| 4x    | 5                  | 25                       | 7                               | 2                      |
| 8x    | 7                  | 40                       | 10                              | 4                      |
| 16x   | 10                 | 60                       | 15                              | 6                      |

These are floors. Go deeper where insight is dense. Compress where it's not.

---

## Steps

### Step 1: Clarify What You're Coming Up With

State clearly:
- **The thing needed**: What kind of output? (name, idea, solution, approach, metaphor, title, design, plan, workaround, etc.)
- **The context**: What is it for? What's the situation?
- **The constraints**: What must it satisfy? Length, tone, audience, technical limits, budget, etc.

```
COMING UP WITH: [type of thing]
FOR: [context/situation]
CONSTRAINTS: [what it must satisfy]
```

### Step 2: Define "Good"

Before generating, establish criteria. What separates a great candidate from a mediocre one?

```
QUALITY CRITERIA:
1. [Criterion 1]: [what good looks like]
2. [Criterion 2]: [what good looks like]
3. [Criterion 3]: [what good looks like]

DEALBREAKERS (instant disqualification):
- [Dealbreaker 1]
- [Dealbreaker 2]
```

If the user specified criteria, use those. If not, derive criteria from the context. Keep it to 3-5 criteria — more than that and they stop being useful filters.

### Step 3: Generate Using Multiple Strategies

Use at least 3 different generation strategies to ensure you're actually exploring the space, not just riffing on one theme.

**Generation Strategy Menu** (pick strategies appropriate to the task):

| Strategy | How it works | Good for |
|----------|-------------|----------|
| **Direct** | Straightforward answers to the need | Baseline candidates |
| **Analogy** | Import from another domain | Novel approaches |
| **Inversion** | What's the opposite? What if you did the reverse? | Breaking assumptions |
| **Combination** | Merge two existing things | Hybrid solutions |
| **Constraint removal** | What if [constraint] didn't exist? Then re-add it partially | Expanding the space |
| **Constraint addition** | Add an artificial constraint and solve within it | Forcing creativity |
| **Extreme** | Push a dimension to its limit (simplest, fastest, cheapest, weirdest) | Finding boundaries |
| **User lens** | What would [specific person/persona] come up with? | Different perspectives |
| **Random entry** | Start from a random concept and force a connection | Breaking fixation |
| **Decompose & recombine** | Break the need into sub-parts, solve each, reassemble | Complex problems |
| **Negation** | List what you DON'T want, then find the opposite | Defining by exclusion |
| **Exemplar** | Find the best existing example and riff on what makes it work | Proven patterns |

For each strategy, generate candidates:

```
STRATEGY: [name]
Candidates:
- [Candidate A]: [brief rationale]
- [Candidate B]: [brief rationale]
- [Candidate C]: [brief rationale]
```

### Step 4: Filter Against Criteria

Take all candidates from Step 3 and evaluate against the criteria from Step 2.

```
FILTERING:

| Candidate | Crit 1 | Crit 2 | Crit 3 | Dealbreaker? | Verdict |
|-----------|--------|--------|--------|--------------|---------|
| [A]       | ✓      | ~      | ✓      | No           | Keep    |
| [B]       | ✓      | ✓      | ✗      | No           | Cut     |
| [C]       | ✓      | ✓      | ✓      | No           | Keep    |
...

SURVIVED: [list of candidates that passed]
CUT: [count] candidates removed
```

### Step 5: Synthesize

Look at the survivors. Can you combine elements from two good-but-different candidates to create something better?

```
SYNTHESIS ATTEMPTS:
- [Candidate A] + [Candidate C] → [New candidate]: [why this combines the best of both]
- [Element from D] + [framing from E] → [New candidate]: [rationale]
```

If a synthesis is clearly better than its parts, add it to the final list. If not, discard it — forced combinations are worse than clean originals.

### Step 6: Present Final Candidates

Present the surviving and synthesized candidates, ranked by fit to criteria.

```
================================================================
CANDIDATES: [what you're coming up with]
================================================================

1. [TOP CANDIDATE]
   Why it works: [brief rationale against criteria]
   Risk/weakness: [honest assessment]

2. [SECOND CANDIDATE]
   Why it works: [brief rationale]
   Risk/weakness: [honest assessment]

3. [THIRD CANDIDATE]
   Why it works: [brief rationale]
   Risk/weakness: [honest assessment]

[Continue for all survivors]

----------------------------------------------------------------
GENERATION STRATEGIES USED: [list]
CANDIDATES GENERATED: [total before filtering]
CANDIDATES PRESENTED: [total after filtering]
================================================================
```

For each candidate, include:
- Why it works (mapped to criteria)
- What's risky or weak about it (honest, not token)

### Step 7: Recommend (if appropriate)

If the user seems to want a recommendation, not just options:

```
RECOMMENDATION: [candidate]
BECAUSE: [1-2 sentence rationale tied to their specific context]
RUNNER-UP: [candidate] — choose this if [condition that would change the recommendation]
```

If you genuinely can't pick (multiple candidates are equally strong for different reasons), say so and explain what would tip the decision.

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Theme clustering** | All candidates are variations of the same idea | Use more generation strategies, especially inversion and analogy |
| **Criteria-free generation** | Long list with no way to evaluate quality | Stop. Define "good" first. Then regenerate |
| **Quantity over quality** | 20 ideas, none developed | Generate fewer, develop each more fully |
| **All safe/obvious** | Nothing surprising in the list | Push with extreme, inversion, or constraint strategies |
| **Ignoring constraints** | Creative ideas that can't actually work | Filter against dealbreakers before presenting |
| **Premature convergence** | Jumped to one idea without exploring the space | Go back to Step 3 and use strategies you haven't tried |
| **Everything is a synthesis** | Forced combinations that aren't better than originals | Keep originals; only present syntheses that clearly improve |

---

## Pre-Completion Checklist

- [ ] Criteria for "good" established before generating
- [ ] Multiple generation strategies used (not just one riff)
- [ ] Candidates are genuinely distinct from each other
- [ ] Filtered against criteria (not just presented raw brainstorm)
- [ ] Synthesis attempted where promising
- [ ] Each presented candidate has honest strengths AND weaknesses
- [ ] At least one candidate is non-obvious or surprising
- [ ] Recommendation given (if user wants one)

---

## After Completion

Report:
- What was generated and why these candidates rose to the top
- The candidates themselves with rationale
- What was cut and why (briefly)
- What would improve with more exploration

### Follow-Up Routing

After candidates are presented, the user may need:
- **"Develop option X further"** → INVOKE: /dd (deep dive on that option)
- **"Compare these"** → INVOKE: /cmp (structured comparison)
- **"I don't like any of these"** → Re-run with different strategies or adjusted criteria
- **"Are these any good?"** → INVOKE: /evaluate
- **"More like option 3"** → Re-run with option 3 as the seed, using combination and analogy strategies
- **"How would I do option X?"** → INVOKE: /how
- **"Which should I pick?"** → INVOKE: /decide or /dcp
- **"What am I missing?"** → INVOKE: /se (space enumeration) or /aex (assumption examination)

---

## Integration

- **Use from**: /want (user wants something, needs options), /how (exploring approaches), /search (exploring a space), /create (needs ideas before production)
- **Routes to**: /cmp (compare candidates), /decide (choose between them), /evaluate (assess quality), /dd (develop one further), /how (execute chosen option)
- **Differs from**: /se (enumerates what EXISTS; /cuw generates what COULD exist), /ma (exhaustive systematic combinations; /cuw is targeted ideation with quality filtering), /cda (imports from other domains; /cuw uses analogy as ONE of many strategies)
- **Complementary**: /aex (check assumptions in your criteria), /but (challenge your top candidate), /iaw (reframe the problem to generate differently)
