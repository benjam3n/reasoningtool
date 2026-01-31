---
date: 2026-01-29 21:00
topic: How to build a skill that finds unexpected/non-obvious solutions
depth: 4x
claims: 14
crux_points: 6
status: MIXED
---

# UAUA 4x: Building an "Unexpected Solutions" Skill

Input: The system gives what's expected, not what's unexpected but better. How to make a skill that finds non-obvious solutions through sophisticated prompt techniques?

---

## U0: EXEMPLAR GROUNDING

### What produces unexpected solutions in practice?

1. **Lateral Thinking (de Bono)** — Deliberately disrupts default reasoning patterns. Uses provocation ("PO: cars should have square wheels") to force the brain off its rails. The provocation isn't the answer — it's the lever that pries open a new search space.

2. **TRIZ (Altshuller)** — Analyzed 40,000 patents and found that inventive solutions follow 40 recurring patterns. The insight: what seems "creative" is actually pattern transfer from a solved problem in another domain. Contradiction matrices force you to find solutions that resolve trade-offs rather than accept them.

3. **Oblique Strategies (Eno/Schmidt)** — Cards with prompts like "Honor thy error as a hidden intention" or "What would your closest friend do?" These work because they inject a random perturbation into an otherwise deterministic reasoning process.

4. **Evolutionary Algorithms** — Mutation + selection. Most mutations are bad, but the ones that aren't are genuinely novel. The key: you need MANY candidates to find the rare good mutation.

5. **How LLMs Actually Work** — LLMs sample from a probability distribution. The most probable token is the "expected" answer. Lower-probability tokens are unexpected but potentially better. Temperature increases diversity but decreases coherence. The challenge: how to access the non-obvious parts of the distribution without sacrificing quality.

### Shared Pattern

All five exemplars share one mechanism: **FORCE THE SYSTEM OFF ITS DEFAULT PATH.** The default path is the most probable, most expected, most median response. Unexpected solutions live in the tails of the distribution, and you need deliberate techniques to get there.

### Felt Impression

This skill needs to feel like a JOLT — not a gradual exploration but a deliberate disruption of normal reasoning. It should be uncomfortable to use, because comfort = expected = median.

---

## U1: SPACE MAPPING

**1. STATE SPACE — Why does the LLM give expected answers?**
- Training objective: predict the most likely next token → median response
- RLHF: reward "helpful, harmless, honest" → safe, conventional, agreeable
- Instruction following: "do what the user asked" → literal interpretation
- Context anchoring: the prompt frames the solution space → solutions near the prompt's implied space
- Knowledge compression: training data is averaged → outputs reflect the average, not the outliers

**2. INSTANCE-TO-CATEGORY — What kind of problem is "finding unexpected solutions"?**
- It's an instance of: EXPLORATION-EXPLOITATION trade-off
- In exploitation mode: use what you know → expected answer
- In exploration mode: try something new → unexpected answer
- LLMs are heavily exploitation-biased by design
- Siblings: brainstorming, creative ideation, scientific discovery, mutation in evolution

**3. PARAMETER VARIATION — What parameters control "expectedness"?**
- The FRAMING of the question (narrow frame → narrow answers)
- The ASSUMPTIONS in the question (more assumptions → more constrained answers)
- The DOMAIN implied (staying in one domain → domain-typical answers)
- The LEVEL OF ABSTRACTION (concrete → concrete answers; abstract → more room for surprise)
- The CONSTRAINTS stated (more constraints → fewer options → but sometimes constraint-violating solutions are best)

**4. ROLE REVERSAL — What if we designed prompts TO PRODUCE unexpected answers?**
- Force the LLM to argue against its first instinct
- Ask it to generate what an expert in an UNRELATED field would suggest
- Give it a constraint that makes the obvious answer impossible
- Ask for the answer it would be embarrassed to suggest
- Ask it to assume its first answer is wrong and find something genuinely different

**5. CAUSAL REVERSAL — What if unexpectedness is the wrong goal?**
- Maybe the goal isn't "unexpected" but "better"
- Some expected answers ARE the best answer
- The problem isn't that answers are expected; it's that the SEARCH terminates too early
- [NOVEL] The real problem: premature convergence on the first plausible answer, not expectedness per se

**6. BOUNDARY DISSOLUTION — What techniques from other fields force non-obvious thinking?**
- TRIZ contradiction matrices: "What if you could have BOTH X and NOT-X?"
- Random input (Oblique Strategies): inject an unrelated concept and find connections
- Constraint removal: "What if [strongest constraint] didn't exist?"
- Constraint addition: "What if you also had to [absurd requirement]?"
- Role assumption: "How would a [random profession] solve this?"
- Time travel: "What will the 2050 solution look like? What will the 1950 solution look like?"
- Scale shift: "What if this was 1000x bigger? 1000x smaller?"
- Negation: "What's the WORST possible solution? Now, what's good about it?"

**7. PERSPECTIVE ROTATION — Whose unexpected is unexpected?**
- Unexpected to the user (who has domain expertise and sees the obvious)
- Unexpected to the LLM (which converges on median training data)
- Unexpected to the field (which has established best practices)
- [NOVEL] The most valuable unexpected solutions are those unexpected to the FIELD — they represent genuine novelty, not just personal blind spots

**8. SCALE VARIATION — At what scale do unexpected solutions matter?**
- Tactical: unexpected approach to a specific problem (small but valuable)
- Strategic: unexpected framing of the problem itself (medium, often more valuable)
- Paradigmatic: unexpected assumptions about what the problem IS (rare, highest value)
- [NOVEL] The skill should operate at ALL three scales, not just tactical

**13. EXEMPLAR COMPARISON — What do breakthrough solutions share?**
- They reframe the problem (Ford: "faster horse" → "personal transportation")
- They violate a constraint everyone assumed was real ("you can't have a phone without buttons")
- They transfer a solution from another domain (Velcro from burrs, PageRank from citation networks)
- They resolve a trade-off instead of accepting it ("you can have speed AND quality")

**14. SENSORY EVALUATION — What does an unexpected-but-good solution feel like?**
- Initial reaction: "Wait, that's weird"
- Second reaction: "Actually, that might work"
- Third reaction: "Why didn't I think of that?"
- The trajectory is: discomfort → consideration → insight
- [NOVEL] If the solution doesn't make you uncomfortable first, it's not truly unexpected

### CANDIDATES for A1

1. **Constraint violation technique** — Systematically remove or invert each stated constraint
2. **Domain transfer technique** — Map the problem to 3 unrelated domains, import their solutions
3. **Provocation technique** — Generate deliberately absurd solutions, extract the useful kernel
4. **Negation technique** — Find the worst solution, then analyze what's secretly good about it
5. **Assumption elimination** — List all assumptions, systematically delete each one
6. **Scale disruption** — Solve at 1000x scale, then import back
7. **Temporal displacement** — Solve from future/past perspective
8. **Adversarial prompt chaining** — Use multiple prompt stages that force the LLM off its default path
9. **Role randomization** — Solve as a randomly selected profession/discipline
10. **Trade-off resolution** — Instead of choosing between X and Y, find a solution that gives both
11. **First-answer rejection** — Generate the obvious answer, explicitly forbid it, then generate again
12. **Meta-unexpected** — Don't just find unexpected solutions; find unexpected PROBLEM FRAMINGS

[T:result] U1 produced 14 universalizations, 12 candidates

---

## A1: CANDIDATE TESTING

### CANDIDATE 1: Constraint Violation

**AR: Removing constraints opens new solution spaces**
├── Every constraint eliminates solutions. Some eliminated solutions are better than anything in the constrained space.
│   ├── AR: iPhone violated "phones need buttons" → opened touch-screen space
│   │   ├── AR: This works because constraints are often ASSUMED, not actually required
│   │   │   ├── AW: Some constraints are real (physics, resources, time)
│   │   │   │   └── AR: The technique asks "IS this constraint real?" which is valuable even for real ones
│   │   │   │       └── [LEVEL 5] Constraint violation is really CONSTRAINT AUDITING — checking which are real
│   │   │   └── AW: Removing all constraints gives useless answers ("just be omniscient")
│   │   │       └── AR: Remove ONE at a time, not all. Each removal opens a specific new space.
│   │   └── AW: Users already know their constraints and chose them deliberately
│   │       └── AR: Users know their STATED constraints. They often don't realize which are assumed.
│   │           └── [CRUX 1: Are assumed constraints the primary source of unexplored solution spaces?]

**VERDICT: VALIDATED** — Core technique. Systematic one-at-a-time constraint removal.

### CANDIDATE 2: Domain Transfer

**AR: Most "creative" solutions are imports from other domains**
├── TRIZ found this from analyzing 40,000 patents
│   ├── AR: The solution already exists — just in a field you haven't looked at
│   │   ├── AR: LLMs are uniquely good at this — they've seen ALL domains in training
│   │   │   ├── The LLM KNOWS the cross-domain solution. It just doesn't offer it because the prompt doesn't ask.
│   │   │   │   └── [NOVEL] Domain transfer may be the highest-leverage LLM technique — the knowledge exists but the default prompt doesn't activate it
│   │   │   └── AW: The LLM might produce superficial analogies ("marketing is like warfare!")
│   │   │       └── AR: Filter for STRUCTURAL analogies (same mechanism) not SURFACE analogies (same metaphor)
│   │   │           └── [LEVEL 5] The technique needs a filter: structural match required, not just metaphor
│   │   └── AW: Finding the right source domain is the hard part
│   │       └── AR: Use RANDOM domain selection to avoid the LLM's default domain associations
│   │           └── [CRUX 2: Is random domain selection better than deliberate domain selection for finding unexpected transfers?]

**VERDICT: VALIDATED** — Powerful technique, especially for LLMs. Needs structural filter.

### CANDIDATE 8: Adversarial Prompt Chaining

**AR: Multiple stages can force genuinely different thinking**
├── Stage 1: Generate the obvious answer
│   Stage 2: "That's the expected answer. Now generate something the user WON'T have considered"
│   Stage 3: "Your second answer is still within the normal range. What if the problem itself is wrong?"
│   ├── AR: Each stage pushes further from the median
│   │   ├── AR: This exploits the LLM's instruction-following — it WILL try to obey "don't give the obvious answer"
│   │   │   ├── AW: It might just give a slightly different obvious answer
│   │   │   │   └── AR: The third stage (reframe the problem) is the key — that's where paradigm shifts live
│   │   │   │       └── [LEVEL 5] Three-stage chain: obvious → different → reframed. The reframing is the high-value output.
│   │   │   └── AW: This is complicated to implement in a single skill invocation
│   │   │       └── AR: The skill can instruct the LLM to do all three stages internally
│   │   └── AW: The LLM might perform the rejection superficially
│   │       └── AR: The specificity of "what would the user NOT have considered" helps
│   │           └── [CRUX 3: Does explicit first-answer-rejection produce genuinely different second answers?]

**VERDICT: VALIDATED** — The three-stage chain (obvious → different → reframed) is the most promising structural technique.

### CANDIDATE 5: Assumption Elimination

**AR: Hidden assumptions are the biggest constraint on solution spaces**
├── Every problem statement contains assumptions about what the problem IS
│   ├── AR: "How do I make my website look better?" assumes: the website should exist, looking better is the goal, visual appearance is the lever
│   │   ├── AR: Eliminating "visual appearance is the lever" might reveal: content quality, information architecture, or load speed matter more
│   │   │   └── This is a BETTER solution that the original framing excluded
│   │   │       └── [NOVEL] Assumption elimination is constraint violation applied to the PROBLEM FRAMING, not just the solution space
│   │   └── AW: Users stated those assumptions for a reason
│   │       └── AR: Check if the reason is valid. Often it's not.

**VERDICT: VALIDATED** — Subsumes constraint violation at a higher level (problem framing).

### CANDIDATE 11: First-Answer Rejection

**AR: Explicitly rejecting the first answer forces exploration**
├── "What's the obvious answer? [answer]. Now that's off the table. What else?"
│   ├── AR: This is the simplest possible technique and it measurably works
│   │   ├── Studies show people generate more creative solutions after being told "that's not the answer"
│   │   │   └── AR: The LLM equivalent: generate, reject, regenerate
│   │   │       └── But: each regeneration might converge back to the same space
│   │   │           └── [CRUX 4: How many rejection rounds before diminishing returns?]
│   │   └── AW: Sometimes the first answer IS the best answer
│   │       └── AR: The skill should present ALL answers (first + alternatives) and let the user pick
│   │           └── [NOVEL] Don't discard the obvious answer. Present it alongside the unexpected ones. Let the user decide.

**VERDICT: VALIDATED** — Simple, effective, core technique.

### CANDIDATE 10: Trade-off Resolution

**AR: Instead of choosing between X and Y, find a solution that gives both**
├── TRIZ calls this "resolving contradictions" — it's the highest-value inventive pattern
│   ├── AR: Most people accept trade-offs as given. The best solutions dissolve them.
│   │   ├── "You can have speed OR quality" → Git: you can have BOTH (fast branching + rigorous merging)
│   │   │   └── AR: Identifying the trade-off explicitly, then asking "what if both?" is a powerful framing
│   │   │       └── [CRUX 5: Can most perceived trade-offs be dissolved, or are some genuinely real?]
│   │   └── AW: Some trade-offs are physically real (speed vs thoroughness, cost vs quality)
│   │       └── AR: Even real trade-offs can be shifted — you can change the frontier, even if you can't eliminate it

**VERDICT: VALIDATED** — High-value technique. State the trade-off, then search for dissolution.

### Remaining Candidates (abbreviated)

**CANDIDATE 3: Provocation** — VALIDATED. Generate absurd solutions, extract the kernel. De Bono's PO technique. Works but needs restraint.

**CANDIDATE 4: Negation** — VALIDATED. "What's the worst solution? What's good about it?" Often reveals hidden value in rejected approaches.

**CANDIDATE 6: Scale Disruption** — VALIDATED WITH CONDITIONS. Useful for some problems, irrelevant for others. Include but don't mandate.

**CANDIDATE 7: Temporal Displacement** — VALIDATED WITH CONDITIONS. "What will the 2050 solution be?" works for technology/strategy. Less useful for immediate practical problems.

**CANDIDATE 9: Role Randomization** — VALIDATED. "How would a marine biologist solve this software problem?" Forces cross-domain transfer from a specific discipline.

**CANDIDATE 12: Meta-Unexpected** — VALIDATED. Finding unexpected PROBLEM FRAMINGS. This is the highest-value technique but hardest to execute. Include as the capstone.

[T:result] A1: 10 validated, 0 rejected, 2 with conditions

---

## U2: EDGE CASES

**EC1: "Unexpected" becomes a new expected pattern.** If the skill always uses the same techniques (reject first answer, transfer domains, remove constraints), the outputs become predictable. Fix: randomize which techniques are applied each time.

**EC2: Unexpected ≠ good.** Most unexpected answers are unexpected because they're bad. Fix: ALL unexpected candidates must pass a quality gate before being presented.

**EC3: User wants practical, gets wacky.** If every answer is "reframe the entire problem," users who need tactical solutions get frustrated. Fix: operate at all three scales (tactical, strategic, paradigmatic) and present options at each.

**EC4: The LLM fakes unexpectedness.** It might produce answers that SOUND creative but are actually just rephrased obvious answers. Fix: the quality gate should check: "Is this structurally different from the obvious answer, or just rhetorically different?"

**EC5: Some problems have well-known optimal solutions.** "How do I sort a list?" → Quicksort. The unexpected skill shouldn't try to reinvent quicksort. Fix: the skill should first check if the problem has a known-optimal solution.

**EC6: Interaction between unexpected skill and other skills.** If UAUA calls /unexpected as part of its generation step, the unexpected skill shouldn't call UAUA back. Fix: this is a leaf skill — it produces candidates but doesn't invoke other analytical skills.

**EC7: The "embarrassment test" is underspecified.** "What would you be embarrassed to suggest?" — the LLM might refuse or hedge. Fix: frame it as "what option would a conventional thinker dismiss but might actually work?"

**EC8: Technique fatigue.** Using all 10+ techniques on every problem is exhausting and mostly waste. Fix: select 3-4 techniques per invocation based on problem type.

[T:result] U2 found 8 edge cases

---

## A2: FINAL VALIDATION

**EC1 (randomize techniques):** MATTERS — build in technique selection, not fixed sequence.
**EC2 (unexpected ≠ good):** MATTERS — quality gate essential. Present obvious + unexpected + reframed, all quality-checked.
**EC3 (user wants practical):** MATTERS — three scales: tactical, strategic, paradigmatic.
**EC4 (fake unexpectedness):** MATTERS — structural difference test, not just rhetorical.
**EC5 (known-optimal exists):** MATTERS — check first. Don't reinvent quicksort.
**EC8 (technique fatigue):** MATTERS — select 3-4 per run.

### FINAL STATUS

| # | Technique | Final Status |
|---|-----------|-------------|
| 1 | Constraint violation/audit | VALIDATED (core technique) |
| 2 | Domain transfer (random + structural filter) | VALIDATED (core technique) |
| 3 | Provocation (absurd → kernel) | VALIDATED (supplementary) |
| 4 | Negation (worst → what's good about it) | VALIDATED (supplementary) |
| 5 | Assumption elimination | VALIDATED (core — problem-level constraint violation) |
| 6 | Scale disruption | WITH CONDITIONS (use when scale-relevant) |
| 7 | Temporal displacement | WITH CONDITIONS (use for tech/strategy) |
| 8 | Three-stage adversarial chain | VALIDATED (structural backbone of the skill) |
| 9 | Role randomization | VALIDATED (supplementary) |
| 10 | Trade-off resolution | VALIDATED (core technique) |
| 11 | First-answer rejection | VALIDATED (simplest technique, always use) |
| 12 | Meta-unexpected (reframe the problem) | VALIDATED (capstone technique) |

---

## SYNTHESIS

### The Architecture

The skill should have a THREE-LAYER structure:

**Layer 1: The Obvious** — Generate the expected, conventional answer first. Don't discard it. This is the baseline.

**Layer 2: The Unexpected** — Apply 3-4 disruption techniques (selected based on problem type) to generate genuinely different candidates. Each must pass a structural-difference test: "Is this fundamentally different from Layer 1, or just reworded?"

**Layer 3: The Reframed** — Challenge the problem itself. "What if the problem is actually [something else]?" This is where paradigm shifts live.

Present all three layers. Let the user choose. Often Layer 1 IS the best answer — but seeing Layers 2 and 3 either confirms that or reveals something better.

### The Core Techniques (select 3-4 per run)

1. **First-answer rejection** — always applied (generates Layer 1 then moves past it)
2. **Assumption elimination** — what assumptions is the problem hiding?
3. **Domain transfer** — how would [random field] solve this?
4. **Constraint audit** — which constraints are real vs assumed?
5. **Trade-off resolution** — what if you could have BOTH sides of the trade-off?
6. **Negation mining** — what's good about the worst solution?
7. **Provocation** — what if [absurd thing]? What kernel is in there?
8. **Role randomization** — how would a [random profession] approach this?
9. **Scale shift** — solve at 1000x scale, import back
10. **Problem reframing** — what if the real problem is [something else entirely]?

### Testable Predictions

1. If we build this skill and use it on 10 problems, at least 3 should produce a solution that neither the user nor the LLM's default response would have found.
2. The three-layer presentation (obvious, unexpected, reframed) should make users prefer the skill over a plain prompt at least 60% of the time.
3. The structural-difference test should prevent "fake unexpected" answers in at least 80% of cases.

### DO_FIRST

**DO_FIRST 1: Build the skill.** The analysis is clear enough to write it now.

[T:result] UAUA 4x complete: 10 validated, 0 rejected, 2 conditional from 12 candidates
