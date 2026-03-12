---
name: "skgap - Skill Gap Analysis"
description: "Identify thinking dimensions not adequately represented by the current skill library, recommend new skills across a sophistication/simplicity spectrum, and prioritize by user value and coverage gap severity."
output:
  format: "prose"
---

# Skill Gap Analysis

**Input**: $ARGUMENTS

---

## Core Principles

1. **Gaps are invisible from inside the system.** The skills you already have define what you think about. Missing skills represent thinking modes you don't even realize you're not doing. Gap analysis must look OUTSIDE the existing library to find what's absent — not just find weaknesses within what exists.

2. **Dimensions, not categories.** Skills exist along multiple dimensions: simple↔sophisticated, easy↔hard, general↔specific, concrete↔abstract, individual↔collaborative, fast↔slow, analytical↔creative. A category like "decision making" might have 20 sophisticated skills and zero simple ones. The gap is in the dimension, not the category.

3. **Simple skills are as valuable as sophisticated ones.** A 2-minute skill that catches one common error ("did you check the obvious thing?") may prevent more failures than a 30-minute analytical framework. The toolkit should serve users at ALL sophistication levels, not just power users.

4. **Coverage means serving ALL user states.** Users arrive in different states: confused, overwhelmed, certain, stuck, exploring, executing, recovering from error. Each state needs skills. If the toolkit has 50 exploration skills and 2 recovery-from-error skills, that's a gap.

5. **Recommended skills must be specific enough to build.** "We need more creativity skills" is not actionable. "We need a skill that takes a failed approach and generates structurally different alternatives by varying the constraint set" is buildable. Every recommendation must include enough specificity to write the SKILL.md.

---

## Phase 1: Dimension Mapping

Map the existing skill library across key dimensions:

### Sophistication Dimension

```
[G1] SOPHISTICATION_MAP:
     Simple (5-min, one technique): [skills] — COUNT: [N]
     Moderate (15-min, multi-step): [skills] — COUNT: [N]
     Sophisticated (30-min+, multi-phase): [skills] — COUNT: [N]
     Expert (requires domain knowledge): [skills] — COUNT: [N]
     GAP: [which sophistication levels are underrepresented?]
```

### Difficulty Dimension

```
[G2] DIFFICULTY_MAP:
     Easy (anyone can follow): [skills] — COUNT: [N]
     Medium (requires some thinking skill): [skills] — COUNT: [N]
     Hard (requires significant cognitive effort): [skills] — COUNT: [N]
     Expert (requires training or deep domain knowledge): [skills] — COUNT: [N]
     GAP: [which difficulty levels are underrepresented?]
```

### Generality Dimension

```
[G3] GENERALITY_MAP:
     Universal (works for any domain): [skills] — COUNT: [N]
     Broad (works for many domains): [skills] — COUNT: [N]
     Domain-specific (works for one domain): [skills] — COUNT: [N]
     Niche (very specific use case): [skills] — COUNT: [N]
     GAP: [which generality levels are underrepresented?]
```

### Speed Dimension

```
[G4] SPEED_MAP:
     Instant (< 1 min): [skills] — COUNT: [N]
     Quick (1-5 min): [skills] — COUNT: [N]
     Standard (5-20 min): [skills] — COUNT: [N]
     Deep (20-60 min): [skills] — COUNT: [N]
     Exhaustive (60+ min): [skills] — COUNT: [N]
     GAP: [which speed levels are underrepresented?]
```

### User State Dimension

```
[G5] USER_STATE_MAP:
     Exploring (no clear direction): [skills] — COUNT: [N]
     Deciding (between options): [skills] — COUNT: [N]
     Executing (knows what to do): [skills] — COUNT: [N]
     Stuck (blocked, need unblocking): [skills] — COUNT: [N]
     Recovering (something went wrong): [skills] — COUNT: [N]
     Validating (checking work): [skills] — COUNT: [N]
     Learning (building understanding): [skills] — COUNT: [N]
     Creating (generating new things): [skills] — COUNT: [N]
     GAP: [which user states are underserved?]
```

---

## Phase 2: Cross-Dimensional Analysis

The most valuable gaps are at INTERSECTIONS of dimensions:

```
[G-N] INTERSECTION_GAP:
     DIMENSIONS: [e.g., "Simple × Recovery" or "Easy × Validation"]
     EXISTING: [what skills exist at this intersection — may be zero]
     NEED: [why this intersection matters]
     SEVERITY: [critical | significant | moderate | minor]
     EXAMPLE_USE_CASE: [when a user would need a skill at this intersection]
```

### High-Value Intersections to Check

| Intersection | Why It Matters |
|-------------|----------------|
| Simple × Any user state | Quick tools everyone can use |
| Easy × Validation | Catch errors without deep expertise |
| Fast × Decision making | Quick heuristics for time-pressured choices |
| General × Recovery | Universal "something went wrong" tools |
| Sophisticated × Creation | Deep generative frameworks |
| Hard × Exploration | Rigorous methods for unknown territory |
| Specific × Common domains | Domain-expert tools for frequent use cases |

---

## Phase 3: Thinking Mode Coverage

Check whether fundamental thinking modes are represented:

```
[G-N] THINKING_MODE: [mode name]
     DEFINITION: [what this mode does]
     EXISTING_SKILLS: [which skills serve this mode]
     COVERAGE: [strong | adequate | weak | absent]
     IF_WEAK_OR_ABSENT: [what skills would fill this gap]
```

### Thinking Modes Checklist

| Mode | Description |
|------|------------|
| **Divergent thinking** | Generate many different options |
| **Convergent thinking** | Narrow from many to best |
| **Critical thinking** | Test and challenge claims |
| **Systems thinking** | See interconnections and feedback loops |
| **Lateral thinking** | Approach from unexpected angles |
| **Analogical thinking** | Transfer knowledge from one domain to another |
| **Counterfactual thinking** | What if things were different? |
| **Temporal thinking** | Past patterns, present state, future projection |
| **Probabilistic thinking** | Reason under uncertainty |
| **Adversarial thinking** | What would an opponent do? |
| **Empathic thinking** | See from another's perspective |
| **Metacognitive thinking** | Think about your own thinking process |
| **Reductive thinking** | Simplify complex things |
| **Constructive thinking** | Build up from components |
| **Dialectical thinking** | Synthesis from opposing views |

---

## Phase 4: Recommendations

For each gap, recommend specific skills:

```
[G-N] RECOMMENDED_SKILL:
     NAME: /[proposed abbreviation] — [full name]
     FILLS_GAP: [which gap from Phases 1-3]
     DIMENSIONS: [where it sits — sophistication, difficulty, generality, speed]
     PURPOSE: [one sentence — what it does]
     USER_ARRIVES: [what state the user is in when they need this]
     USER_LEAVES: [what state they're in after using it]
     CORE_MECHANISM: [the key technique or process — one paragraph]
     PRIORITY: [critical | high | medium | low]
     BUILD_COMPLEXITY: [simple to build | moderate | complex]
```

### Recommendation Quality Test

Each recommendation must pass:
- **Specificity**: Could you write the SKILL.md from this description? If not, it's too vague
- **Distinctness**: Is this genuinely different from existing skills? Check for overlaps
- **Need**: Can you name a specific scenario where a user needs this and nothing else serves?
- **Buildability**: Is this a coherent skill or a vague aspiration?

---

## Phase 5: Priority Matrix

```
SKILL GAP PRIORITY MATRIX
==========================

CRITICAL GAPS (create these first):
  1. /[skill] — FILLS: [gap] — COMPLEXITY: [build effort]
  2. /[skill] — FILLS: [gap] — COMPLEXITY: [build effort]

HIGH PRIORITY:
  1. /[skill] — FILLS: [gap]

MEDIUM PRIORITY:
  1. /[skill] — FILLS: [gap]

NICE TO HAVE:
  1. /[skill] — FILLS: [gap]

DIMENSION SUMMARY:
  Most underrepresented sophistication level: [level]
  Most underrepresented difficulty level: [level]
  Most underrepresented user state: [state]
  Most underrepresented thinking mode: [mode]

READY FOR:
- /cs [skill spec] — to create the recommended skills
- /mts [skill spec] — alternative creation path
- /imprt — to combine gap analysis with quality improvement
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Inside-out analysis** | Only examined existing skills for weaknesses, didn't look for absent capabilities | Start from the dimension maps and thinking modes, not from the skill list |
| **Category thinking only** | "We need more X category skills" without dimensional analysis | Map dimensions first. Gaps are at intersections, not just categories |
| **Sophistication bias** | Only recommended complex, sophisticated skills | Simple and easy skills fill gaps too. Check the simple × [state] intersections |
| **Vague recommendations** | "We need a creativity skill" | Every recommendation needs purpose, mechanism, dimensions, and user state transitions |
| **Duplicate recommendations** | Recommended a skill that effectively already exists | Check each recommendation against existing skills for overlap |
| **No priority ordering** | List of 30 gaps with no ranking | Priority = gap severity × user frequency × build complexity |
| **Ignored dimensions** | Only analyzed 1-2 dimensions instead of all relevant ones | Run all dimension maps. The most valuable gaps are often in the dimensions you didn't check |

---

## Depth Scaling

| Depth | Dimensions Mapped | Thinking Modes | Recommendations | Cross-Dimensional |
|-------|------------------|---------------|-----------------|-------------------|
| 1x | Sophistication + user state | Top 5 | 3-5 skills | No |
| 2x | All 5 core dimensions | Top 10 | 5-10 skills | Key intersections |
| 4x | All dimensions + custom | All 15 | 10-15 skills | Full intersection matrix |
| 8x | All + competitive analysis | All + emerging | 15+ skills | Full + scenario testing |

Default: 2x. These are floors.

---

## Pre-Completion Checklist

- [ ] All 5 core dimensions mapped with counts
- [ ] Cross-dimensional intersections analyzed
- [ ] Thinking modes checked for coverage
- [ ] Each recommendation is specific enough to build (passes specificity test)
- [ ] Each recommendation is distinct from existing skills (passes distinctness test)
- [ ] Recommendations span multiple sophistication and difficulty levels
- [ ] Priority matrix has clear ordering
- [ ] Simple/easy skills represented in recommendations (not just sophisticated ones)

---

## Integration

- Use from: toolkit planning, after large skill additions, periodic coverage reviews
- Routes to: `/cs` or `/mts` (to create recommended skills), `/imprt` (for holistic improvement)
- Complementary: `/imprt` (imprt finds quality issues; skgap finds missing capabilities)
- Differs from `/imprt`: imprt diagnoses the toolkit holistically including quality; skgap specifically identifies absent capabilities
- Differs from `/impss`: impss improves existing skills; skgap identifies skills that don't exist yet
- Differs from `/se`: se enumerates a known space; skgap discovers what's missing from an unknown space
