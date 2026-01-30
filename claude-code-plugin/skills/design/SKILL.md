---
name: design
description: Apply universal design principles to create or improve designs. Domain-adaptive, generative, grounded in exemplars. Embeds generate → critique → iterate.
---

# Design - Principled Design Creation and Improvement

**Input**: $ARGUMENTS

---

## Core Principles

1. **Design is constrained optimization of arrangement.** Given elements, constraints, and purpose — find the arrangement that best serves that purpose. This applies to visual, physical, digital, informational, and experiential design.

2. **Purpose before aesthetics.** Every element must serve the purpose. If removing an element doesn't degrade function or signal, remove it. This is parsimony — not minimalism (a Baroque church can be parsimonious if every ornament serves awe).

3. **Exemplars before analysis.** Before designing or critiquing, identify what good looks like. Exemplars provide a perceptual anchor that prevents analysis from drifting into "analytically sound but actually bad" territory.

4. **Generate then evaluate.** Produce candidate designs before analyzing them. Labels ("make it cleaner") are less useful than artifacts (actual CSS with specific values).

5. **Trust the impression.** When the design "feels wrong" but the individual elements check out, the impression is usually right. Investigate the relationships between elements, not the elements themselves.

6. **Certainty gradient.** Design decisions range from universal neuroscience (contrast creates hierarchy) to cultural convention (logo top-left) to arbitrary choice (exact shade of grey). Invest effort from the certain end. Don't agonize over arbitrary decisions — use convention.

7. **Constraints improve quality.** They reduce the search space. Embrace them.

---

## The Design Flow

```
1. UNDERSTAND → What's the purpose? Who's the audience? What are the constraints?
2. GROUND → What does good look like? (exemplars)
3. ASSESS → Where are we now? (if improving existing design)
4. PRIORITIZE → What to work on first? (domain effort ordering)
5. GENERATE → Produce candidate designs (/generate)
6. CRITIQUE → Evaluate candidates (/critique)
7. ITERATE → Improve best candidate based on critique
8. VERIFY → Does the final design satisfy purpose?
```

Steps 5-7 may loop until satisfied.

---

## The 8 Foundational Principles

Always apply. Every domain.

| # | Principle | Test |
|---|-----------|------|
| 1 | **PARSIMONY** | Remove each element mentally. Does the design get worse? If not, remove it. |
| 2 | **HIERARCHY** | Can you tell what's most important within 3 seconds? |
| 3 | **GROUPING** | Are related things close and unrelated things separated? |
| 4 | **PURPOSE ALIGNMENT** | Does every element serve the goal? |
| 5 | **COGNITIVE COST** | How much mental effort does this require? Can it be less? |
| 6 | **RHYTHM** | Is spacing/proportion consistent and mathematical? |
| 7 | **COMPOSITION** | Is the whole more than the sum of parts? (Gestalt check) |
| 8 | **CONSTRAINT GRATITUDE** | Are constraints being used, not fought? |

---

## Domain Effort Ordering

Work from top to bottom. Top items produce the most quality per unit of effort.

### Web / App
1. Information architecture (what content, how organized)
2. Content hierarchy (what's most important per page)
3. Navigation (how users move between pages)
4. Typography (readability, scale, weight)
5. Spacing system (consistent rhythm — pick a base unit)
6. Color system (contrast, meaning, brand)
7. Interactive states (hover, focus, active, disabled)
8. Animation/transition (smooth, purposeful)
9. Decorative detail (shadows, borders, gradients)
10. Pixel-perfect polish (sub-pixel alignment)

### Physical Product
1. Function (does it work?)
2. Ergonomics (is it comfortable to use?)
3. Durability (does it last?)
4. Aesthetics (does it look/feel good?)
5. Packaging (first impression)

### Communication / Writing
1. Argument clarity (is the point clear?)
2. Logical structure (does it flow?)
3. Audience awareness (does it meet them where they are?)
4. Voice/tone (does it sound right?)
5. Visual formatting (is it scannable?)

### Sound Design
1. Clarity (can you understand it?)
2. Emotional tone (does it feel right?)
3. Volume consistency (no jarring changes)
4. Non-fatiguing (can you listen for hours?)
5. Memorability (does it stick?)

### Game Design
1. Core loop (is the basic action fun?)
2. Difficulty curve (does challenge match skill?)
3. Feedback clarity (do players know what happened?)
4. Visual coherence (does the world make sense?)
5. Polish (does it feel smooth?)

---

## The Arbitrary Decision Test

For any design decision: **"If I changed this, would the user notice and care?"**

- **YES (utility or signal)** → Design intentionally. This decision matters.
- **NO** → Use convention. Pick the most standard option. Don't waste time on this.

Convention defaults: standard grid, system fonts or proven web fonts, 4/8px spacing base, established color palette, platform-native interactions.

---

## Signaling

Every design outputs two things:
- **UTILITY**: Helps the user achieve their goal
- **SIGNAL**: Communicates something about the maker (care, quality, identity)

Signal is produced by execution quality. Pixel-perfect alignment, smooth animation, consistent spacing — these signal "we care about details." You can't fake signal cheaply (that's why it works — costly signaling).

| Context | Utility Weight | Signal Weight |
|---------|---------------|---------------|
| Developer tool | 80% | 20% |
| Consumer app | 60% | 40% |
| Luxury/brand | 20% | 80% |
| Internal tool | 90% | 10% |

---

## Working with Existing Designs

When improving an existing design:

1. **Impression first**: What's the overall feeling? Professional? Amateur? Cluttered? Clean?
2. **Exemplar comparison**: Find 3 designs you want to be compared to. What do they do that this doesn't?
3. **Foundational audit**: Run through the 8 principles. Which are violated?
4. **Priority**: Work the effort ordering top-down. Don't polish shadows before fixing hierarchy.
5. **Generate improvements**: Produce actual artifacts (specific CSS values, specific layout changes)
6. **Critique the improvements**: Do they address the issues without introducing new ones?

---

## Mathematical Quality Model

For those who want precision:

```
Design D = (Elements E, Relationships R, Hierarchy H, Spatial arrangement S, Visual properties V, Purpose P)

Quality constraints:
1. Parsimony:     ∀e ∈ E: utility(D) > utility(D \ {e})
2. Hierarchy:     visual_difference(level_n, level_n+1) > perceptual_threshold
3. Grouping:      related elements closer than unrelated
4. Rhythm:        spacing values have low entropy (mathematical system)
5. Convention:    deviation_cost < communication_gain

Objective function:
utility(D) = comprehension_speed × task_completion × signal_value − cognitive_cost − production_cost
```

---

## Pre-Completion Check

- [ ] Purpose clearly defined
- [ ] Exemplars identified
- [ ] Effort ordering followed (top-down)
- [ ] Artifacts produced (not just labels)
- [ ] Foundational principles checked
- [ ] Impression matches analysis (or divergence investigated)
