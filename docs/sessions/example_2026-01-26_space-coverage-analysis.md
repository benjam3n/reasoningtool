# Space Coverage Analysis

This document captures the analysis that led to improvements in the guess generation system.

## Original Input

"It's not necessarily the number of guesses, it's more so the guesses have to be comprehensive in that they cover the entire space."

---

## Surface Claims Extracted

**Explicit claims:**
1. Number of guesses is not the key metric
2. Comprehensiveness is the key metric
3. Guesses should cover "the entire space"
4. Space coverage is more important than quantity

**Implicit claims:**
5. A "space" exists that can be covered
6. The space has boundaries (can be "entire")
7. Guesses map to regions of this space
8. Coverage is measurable
9. Incomplete coverage is a failure mode
10. The previous approach was focusing on quantity over coverage

**Presuppositions:**
11. Claude was generating guesses incorrectly
12. The correction is about coverage, not count
13. "Comprehensive" has a specific meaning here
14. The feedback is about improving the system

---

## Morphological Analysis

### Claim: "Guesses should cover the entire space"

| Dimension | Values Enumerated |
|-----------|-------------------|
| WHAT is "space"? | possibility space, claim space, interpretation space, outcome space, assumption space, perspective space, stakeholder space, time space, causal space, value space |
| WHAT is "cover"? | touch every region, sample uniformly, prioritize by importance, ensure no blind spots, map boundaries, identify clusters, exhaustive enumeration, strategic sampling |
| WHAT is "entire"? | literally everything, all important regions, all non-trivial regions, all that can be enumerated, all that impact the conclusion |
| WHO defines the space? | the user, the system, the problem itself, domain experts, the methodology, no one (emergent) |
| HOW is coverage measured? | by dimensions covered, by regions touched, by inversions explored, by stakeholders considered, by time horizons, by assumptions questioned |
| WHEN is coverage sufficient? | never (always more), when diminishing returns, when user satisfied, when all dimensions enumerated |
| WHY does coverage matter? | to avoid blind spots, to find non-obvious solutions, to stress-test claims, to enable selection from full option set |

### Key Combinations (guesses about meaning):

1. Space = all possible interpretations of the input, coverage = touching each interpretation
2. Space = all hidden assumptions, coverage = surfacing each one
3. Space = all dimensions of variation (SCAMPER, morphological), coverage = exploring each dimension
4. Space = all stakeholder perspectives, coverage = considering each one
5. Space = all failure modes, coverage = anticipating each one
6. Space = all causal pathways, coverage = tracing each one
7. Space = all time horizons, coverage = considering past/present/future
8. Space = belief space, coverage = exploring both assume-right and assume-wrong branches

---

## Unbundled Guesses

### From "cover the entire space":

- Guess: A bounded space exists [O: implied by "entire"]
- Guess: The space can be enumerated or characterized
- Guess: Coverage is binary (covered/not covered) rather than continuous
- Guess: All regions of the space are equally important
- Guess: Missing a region is worse than redundant coverage
- Guess: The space is knowable in advance
- Guess: The space is the same for every input
- Guess: "Entire" means literally all, not "sufficient"

### From "comprehensive":

- Guess: Comprehensive has an objective definition
- Guess: Comprehensiveness is achievable
- Guess: I know what comprehensive means in this context
- Guess: User's definition of comprehensive matches mine
- Guess: There's a checklist for comprehensiveness

### From "not necessarily the number":

- Guess: I was optimizing for number
- Guess: Number and coverage are different metrics
- Guess: High number can coexist with low coverage
- Guess: The correction is specifically about my previous response
- Guess: User observed a gap in coverage, not in quantity

---

## Inversion Guesses [O: User confirmed "all of these guesses are good"]

| Original | Inversion |
|----------|-----------|
| Cover the entire space | Cover only the important regions (sparse but targeted) |
| Comprehensiveness matters | Depth on key guesses matters more than breadth |
| Not about number | Actually IS about number, but the right kind of number |
| Space has boundaries | Space is unbounded, coverage is always partial |
| Guesses map to space | Guesses CREATE the space (not map to pre-existing) |
| Coverage is good | Over-coverage is wasteful, under-coverage is strategic |

---

## Analogy Guesses

| Domain | Analogous Problem | What They Do | Mapped Guess |
|--------|-------------------|--------------|--------------|
| Cartography | Map entire territory | Systematic survey, grid sampling | Space coverage = systematic grid over claim dimensions |
| Testing | Test coverage in software | Cover all branches, paths, conditions | Coverage = all logical branches of each claim |
| Search | Explore entire search space | BFS vs DFS, ensure all nodes visited | Coverage = guarantee no region unexplored |
| Sampling | Representative sample | Stratified sampling ensures all strata | Coverage = sample from each stratum of possibility |
| Military | Reconnaissance | Cover all terrain, identify blind spots | Coverage = no blind spots in assumption space |
| Science | Hypothesis space | Generate alternative hypotheses | Coverage = all plausible alternatives considered |

---

## SCAMPER on "Cover the Space"

| Operation | Application |
|-----------|-------------|
| Substitute | Cover the BOUNDARIES instead of the interior |
| Substitute | Cover the STRUCTURE instead of the content |
| Combine | Cover space AND prioritize by impact |
| Adapt | Adaptive coverage - dense where important, sparse elsewhere |
| Modify | Cover the space DIMENSIONALLY (each axis) not regionally |
| Put to other use | Use coverage as a VALIDATION check, not generation method |
| Eliminate | Eliminate redundant regions, cover only distinct |
| Reverse | Start from uncovered regions, work backward |

---

## Pre-Mortem: Why "Cover the Space" Might Be Wrong

1. Perception error: I'm interpreting "space" differently than intended
2. Scope error: The "entire" space is infinite, coverage is impossible
3. Definition error: "Comprehensive" means something specific I'm missing
4. Optimization error: Covering space is a means, not the end goal
5. Framing error: The real point is something else (quality? relevance?)
6. Selection bias: Certain regions seem unimportant but aren't
7. Availability bias: I'm covering what's easy to think of, not what matters
8. False dichotomy: It's not number vs coverage, it's something else
9. Motivated reasoning: I want "coverage" to mean what I already do
10. Meta error: This feedback is about a different issue than I think

---

## Critical Guesses (High Impact × Low Confidence)

| Guess | Why Critical |
|-------|--------------|
| "Space" means all dimensions of morphological analysis | If wrong, I'm using wrong method |
| Coverage is measured by dimensions touched | If wrong, my metric is wrong |
| The gap was dimensional, not quantitative | If wrong, fix is wrong |
| User wants systematic coverage, not creative generation | If wrong, approach is wrong |
| "Entire" allows strategic sampling, not literal exhaustion | If wrong, I'll over/under do it |

---

## Type-Specific Questions

| Guess | Type | Question |
|-------|------|----------|
| A bounded space exists | Modal | What defines the boundaries? Can you characterize the space? |
| Coverage is achievable | Modal | Is 100% coverage expected, or "good enough" coverage? |
| I was optimizing for quantity | Meta | What specific gap did you observe in my previous response? |
| Space = dimensions of variation | Factual | Is morphological analysis (dimensions × values) what you mean by "space"? |
| Comprehensiveness is the goal | Normative | What would comprehensive coverage look like for the input I processed? |

---

## Synthesis: What "Cover the Space" Means

Based on analysis, the interpretations:

1. **Dimensional coverage**: For each claim, ensure ALL relevant dimensions are explored (who, what, why, how, when, where, degree, certainty, scope) - not just a few
2. **Perspective coverage**: Ensure assume-right AND assume-wrong branches are both fully explored
3. **No blind spots**: The goal is zero unexplored regions, not maximum explored regions
4. **Systematic not creative**: Use structured methods (morphological, SCAMPER) to guarantee coverage, don't rely on creative generation
5. **Quality of coverage > quantity of guesses**: 50 guesses covering 10 dimensions > 500 guesses covering 3 dimensions

---

## Derived Improvements

### 1. Adaptive Coverage Strategy
**From**: "Cover entire space" + "Cover only important regions"

Add coverage mode selector:
- EXHAUSTIVE: Use when stakes are high, cover everything
- TARGETED: Use when time-constrained, cover high-impact regions
- ADAPTIVE: Start broad, go deep where signal found
- BOUNDARY: Map the edges of the space first

### 2. Depth vs Breadth Toggle
**From**: "Comprehensiveness matters" + "Depth on key guesses matters more"

Add depth control:
- IF high_impact AND low_confidence: GO DEEP
- ELSE: STAY SHALLOW

### 3. "Right Kind of Number" Metric
**From**: "Not about number" + "Actually IS about number, but the right kind"

Define coverage metrics:
- Dimension coverage: % of morphological dimensions explored
- Perspective coverage: % of stakeholders considered
- Time coverage: past/present/future all touched
- Inversion coverage: % of claims with assume-wrong branch
- Type coverage: % of guess types (8) represented

### 4. Space Discovery Mode
**From**: "Space has boundaries" + "Space is unbounded"

Add space discovery phase BEFORE generating:
1. What dimensions COULD apply?
2. What stakeholders COULD exist?
3. What time frames COULD matter?
4. What adjacent spaces COULD connect?

### 5. Generative Space Model
**From**: "Guesses map to space" + "Guesses CREATE the space"

Reframe:
- OLD: "Cover the space"
- NEW: "Generate the space by guessing, then identify gaps"

### 6. Strategic Under-Coverage
**From**: "Coverage is good" + "Under-coverage is strategic"

Add explicit skip criteria:
- Region is well-understood
- Region is irrelevant to user's decision
- Region would require unavailable resources
- Region is downstream of more important region
- User explicitly excluded it

---

## Implementation Status

Created: 2026-01-26
Files updated:
- `/skills/guess_generation/SKILL.md` - Added coverage metrics, depth control
- `/skills/space_discovery/SKILL.md` - New skill for discovering space before guessing
- `/scripts/no_guessing_gate.py` - Excluded skill files from blocking
