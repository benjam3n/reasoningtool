---
date: 2026-01-29 20:30
topic: Which core skills need improvement and how
depth: 4x
claims: 14
crux_points: 6
status: MIXED
---

# UAUA 4x: Core Skills That Need Improvement

Input: Identify key core skills that could be greatly improved based on what is now known.

---

## U0: EXEMPLAR GROUNDING

What does a great skill file look like NOW, after the UAUA/ARAW rewrite?

The new UAUA (231 lines) and ARAW (254 lines) embody:
- Principles-first (governing rules before procedures)
- Adaptive depth (floors not ceilings, zoom into what's interesting)
- Generative capability (G1 step for creative domains)
- Feedback loops (convergent, not linear)
- Testable predictions (ground analysis in reality)
- Continuous synthesis (integrate as you go)
- ~200-250 lines (enough to guide, not so much it constrains)

The OLD skills (pre-rewrite) are 570-757 lines of procedure-heavy, template-heavy, checklist-heavy instruction. Most of the 220 skills in the toolkit were written in the old style.

### The Quality Gap

The old style: "Here are 12 steps. For each step, here's the exact output format. Here's a verification checklist." → Produces compliant but often shallow output.

The new style: "Here are 5-7 principles. Here's the flow. Explore until insight." → Produces deeper, more adaptive output.

**Most skills in the toolkit are in the old style.**

---

## U1: SPACE MAPPING

### Which skills are "core" and most impactful to improve?

**By usage frequency** (skills most likely to be invoked directly or called by other skills):
1. GOSM (entry point for everything)
2. ARAW (already rewritten)
3. UAUA (already rewritten)
4. procedure_engine (the full 12-step analysis)
5. comparison (used in every decision)
6. meta_reasoning_core (governs when to use what)
7. high_quality_writing (used for all text output)
8. root_cause_5_whys (used for all problem diagnosis)
9. finder (skill discovery — how users find the right skill)
10. space_enumeration (used in every divergent step)

**By improvement potential** (gap between current quality and what's possible):
1. GOSM — bloated router that could be a clean dispatcher
2. procedure_engine — 12 procedural steps, heavy on template
3. high_quality_writing — has good ideas but is structured as checklist
4. comparison — mechanical scoring system that misses qualitative judgment
5. meta_reasoning_core — 10 steps when it needs 3 principles
6. root_cause_5_whys — rigid 5-step recursion that should be adaptive
7. finder — registry lookup when it should understand intent
8. design_procedures / design_thinking_lean — DON'T EXIST (no design skills at all!)
9. space_enumeration — focused on enumeration strategy, not on finding surprising options
10. field_analysis — good compound skill but chains 5 skills mechanically

**By strategic importance** (which improvements cascade to other skills):
1. procedure_engine — called by GOSM-Full, which is the deepest analysis path
2. meta_reasoning_core — governs all skill selection
3. high_quality_writing — affects quality of every text output
4. comparison — used in every decision across the toolkit
5. GOSM — entry point for everything

### CANDIDATES for A1

1. **Rewrite GOSM as a clean dispatcher** — it's the entry point; improvements cascade everywhere
2. **Rewrite procedure_engine with principles-first approach** — it's the deep analysis engine
3. **Rewrite high_quality_writing to embody its own principles** — currently a checklist about writing, not a generative writing tool
4. **Rewrite comparison to handle qualitative judgment** — currently a scoring system that misses gestalt
5. **Rewrite meta_reasoning_core from 10 steps to 3 principles** — over-proceduralized metacognition
6. **Make root_cause_5_whys adaptive** — rigid 5 whys when some problems need 2 and some need 12
7. **Create a design skill** — the toolkit has ZERO design skills despite design being a core domain
8. **Rewrite space_enumeration to find surprising options** — currently focused on completeness, not on discovering what you didn't know existed
9. **Rewrite finder to understand intent** — currently a registry lookup
10. **Add a "generate" skill** — the toolkit is all-evaluation, zero-generation
11. **Add a "critique" skill** — structured critique that uses the gestalt principle
12. **Add an "iterate" skill** — generate → evaluate → improve loop that all creative work needs

[T:result] U1 produced 12 candidates across 3 assessment dimensions

---

## A1: CANDIDATE TESTING

### CANDIDATE 1: Rewrite GOSM as clean dispatcher

**AR: GOSM is bloated and should be simplified**
├── Current GOSM: 6 variants (Lite, Quick, Check, After, Standard, Full), each with full templates
│   ├── AR: Most of this is output format prescription, not decision logic
│   │   ├── The actual DECISION is simple: assess urgency × stakes × expertise → pick variant
│   │   │   ├── AR: This could be a 50-line decision tree, not a 300-line file
│   │   │   │   └── AW: Users need to see what each variant produces
│   │   │   │       └── AR: The variants ARE other skills. GOSM just routes to them.
│   │   │   │           └── [NOVEL] GOSM shouldn't contain variant definitions — it should be a pure router that dispatches to specialized skills
│   │   │   └── AW: Having variants inline makes GOSM self-contained
│   │   │       └── AR: Self-contained = bloated. Better: GOSM routes, other skills execute.
│   │   └── AW: The variant format guides the LLM's output
│   │       └── AR: The LLM knows how to produce brief vs comprehensive analysis without format templates
│   │           └── [LEVEL 5] Template removal hypothesis: the LLM produces BETTER output when given principles than when given templates
├── Cascade impact: GOSM is invoked directly by users AND by the /gosm command
│   └── Every GOSM improvement reaches every user immediately

**AW: GOSM's structure serves a purpose**
├── The variant selection matrix IS the value — users don't know when to go deep vs shallow
│   └── AR: Keep the selection logic. Remove the inline variant implementations.
├── Some users want to see the full procedure before running it
│   └── AR: Show the variant SKILL.md, not duplicate it inside GOSM

**VERDICT: VALIDATED**
Rewrite GOSM as a pure dispatcher (~80-100 lines). Move variant implementations to their own skills or let existing skills handle them.

---

### CANDIDATE 2: Rewrite procedure_engine with principles-first

**AR: procedure_engine is the old style incarnate**
├── 12 sequential steps with output templates for each
│   ├── AR: This is exactly what the UAUA rewrite moved AWAY from
│   │   ├── The 12 steps are: classify → parse guesses → ARAW → goal journey → dual analysis → filter → questions → values → failure check → trace journey → generate steps → verify
│   │   │   ├── AR: Many of these steps are redundant or low-value
│   │   │   │   ├── "Parse as Guesses" + "ARAW" + "Goal Journey" + "Dual Analysis" — these all do variations of "understand the problem deeply"
│   │   │   │   │   └── [NOVEL] procedure_engine has 4 steps that are all "understand the problem" wearing different hats
│   │   │   │   └── AW: Each step surfaces different information
│   │   │   │       └── AR: Yes, but the LLM can surface all that information in ONE step with the right principle
│   │   │   │           └── "Understand the problem from multiple angles" = 1 principle that replaces 4 steps
│   │   │   └── AW: The routing to specific skill chains (GOAL→, PROBLEM→, DECISION→) IS valuable
│   │   │       └── AR: Keep the routing. Rewrite what happens after routing.
│   │   └── AW: procedure_engine handles the most complex cases (GOSM-Full)
│   │       └── AR: All the more reason to make it principled rather than procedural
│   │           └── [CRUX 1: Does the procedure_engine's 12-step structure produce better output than a 5-principle approach would?]
├── The routing table (input type → skill chain) is genuinely valuable
│   └── AR: This is the core value. Everything else is ceremony.

**VERDICT: VALIDATED**
Rewrite procedure_engine: keep routing table, reduce 12 steps to ~5 principles, remove output templates.

---

### CANDIDATE 3: Rewrite high_quality_writing

**AR: The writing skill is a checklist about writing, not a writing tool**
├── It tells you to: define reader, use question-answer structure, detect weak patterns
│   ├── AR: These are good PRINCIPLES but presented as a CHECKLIST
│   │   ├── The skill lists 9 "weak patterns" to detect — this is valuable
│   │   │   └── But it's presented as a post-hoc audit, not as generative guidance
│   │   │       └── [NOVEL] Writing skills should guide GENERATION, not just EVALUATION
│   │   ├── Missing: HOW to write well. It says "answer the exact question" but not how to construct compelling arguments, find the right voice, create flow.
│   │   │   └── AR: The 32x design principles analysis found: for writing, the priority is clarity → structure → audience awareness → voice → formatting
│   │   │       └── The current skill covers clarity and structure. Missing: voice, narrative arc, persuasion.
│   │   └── AW: Writing skill shouldn't try to teach writing — the LLM already knows
│   │       └── AR: The LLM's default writing is competent but generic. The skill should push it beyond generic.
│   │           └── [CRUX 2: Should writing skills guide generation or just evaluate output?]
├── The weak pattern detection is genuinely novel and useful
│   └── Keep it. But embed it in a generative framework.

**VERDICT: VALIDATED**
Rewrite: principles-first generative writing tool. Keep weak pattern detection. Add voice, narrative structure, and the "reader's journey" concept.

---

### CANDIDATE 4: Rewrite comparison to handle qualitative judgment

**AR: comparison is a scoring system that misses what matters**
├── Current: REQUIRED/EXCLUSION/PREFERRED/OPTIONAL criteria, 0-3 scoring
│   ├── AR: This works for objective criteria but fails for qualitative ones
│   │   ├── "Which design looks more professional?" can't be scored 0-3
│   │   │   └── AR: The gestalt principle applies here — overall impression matters more than criterion scores
│   │   │       └── [NOVEL] Comparison should include: "Before scoring, what's your overall impression? Does the scoring match?"
│   │   ├── The scoring creates false precision — "Option A scores 2.3, Option B scores 2.1" implies A is better but the difference is noise
│   │   │   └── AR: Better: tier-based comparison (clearly better / slightly better / equivalent / slightly worse / clearly worse)
│   │   │       └── [CRUX 3: Does quantitative scoring help or hurt comparison quality?]
│   │   └── AW: Structured scoring prevents emotional bias
│   │       └── AR: Good point — but the gestalt check can coexist with structured evaluation
│   │           └── Score first, then check impression, then investigate divergence
├── Missing: the "I just KNOW option B is better but can't articulate why" case
│   └── AR: This is the gestalt principle. The comparison skill needs it.

**VERDICT: VALIDATED**
Rewrite: add gestalt impression check, replace 0-3 scoring with tier-based comparison, keep structured criteria but add qualitative judgment layer.

---

### CANDIDATE 5: Rewrite meta_reasoning_core

**AR: 10 steps of metacognition is 7 too many**
├── The 10 steps: goal reconstruction, failure check, best method, intention check, info elicitation, evidence evaluation, hypothesis generation, process check, story coherence, iteration decision
│   ├── AR: The CORE of metacognition is 3 questions:
│   │   1. What am I actually trying to achieve? (goals)
│   │   2. Is this the best way? (method)
│   │   3. Am I making progress? (feedback)
│   │   ├── AR: Every one of the 10 steps maps to one of these 3
│   │   │   ├── Steps 1, 4, 9 → "What am I trying to achieve?"
│   │   │   ├── Steps 2, 3, 6, 7 → "Is this the best way?"
│   │   │   ├── Steps 5, 8, 10 → "Am I making progress?"
│   │   │   └── [NOVEL] meta_reasoning_core has 10 steps that are 3 questions asked 3 different ways each
│   │   └── AW: The 10 steps make each sub-check explicit
│   │       └── AR: Explicit checks become rote. Principles activate judgment.
│   │           └── [LEVEL 5] Same pattern as UAUA rewrite: procedures → principles = better output

**VERDICT: VALIDATED**
Rewrite: 3 core questions + guidance on when to ask each. From 10 steps to ~80 lines.

---

### CANDIDATE 7: Create a design skill

**AR: The toolkit has ZERO design-specific skills**
├── 220 skills. None for design. This is the biggest gap.
│   ├── AR: The universal design principles (from 32x analysis) provide the foundation
│   │   ├── 40 validated principles, mathematical formalization, domain effort orderings
│   │   │   └── This is ready to become a skill
│   │   └── The UAUA now has perceptual techniques + generation step + gestalt principle
│   │       └── But there's no standalone design skill that a user can invoke for "make this look good"
│   ├── What a design skill would do:
│   │   1. Identify design domain (web, product, communication, sound, game)
│   │   2. Apply domain effort ordering (work on highest-impact elements first)
│   │   3. Check foundational principles (parsimony, hierarchy, grouping, rhythm, convention)
│   │   4. Compare to exemplars (what does good look like in this domain?)
│   │   5. Generate candidates (produce actual artifacts)
│   │   6. Evaluate using gestalt + principles
│   │   7. Iterate
│   │   └── [NOVEL] This is the first skill that would be GENERATIVE by default, not evaluative
│   └── AW: Design is too broad for one skill
│       └── AR: The domain effort ordering handles breadth — it tells you what to focus on per domain
│           └── [CRUX 4: Can one design skill cover all design domains, or does each need its own?]

**VERDICT: VALIDATED**
Create a design skill grounded in the 40 universal design principles. Single skill with domain adaptation via effort orderings.

---

### CANDIDATE 10: Add a "generate" skill

**AR: The toolkit is all-evaluation, zero-generation**
├── Every skill analyzes, evaluates, compares, or validates
│   ├── None produce artifacts (code, prose, designs, strategies)
│   │   ├── AR: UAUA now has G1, but it's embedded in UAUA, not standalone
│   │   │   └── A standalone generate skill would be: "Given constraints and purpose, produce N diverse candidates"
│   │   │       └── AR: This is the most basic creative operation and the toolkit doesn't have it
│   │   │           └── [NOVEL] Generate should be a PRIMITIVE skill that other skills call, like comparison or space_enumeration
│   │   └── AW: The LLM generates by default — you don't need a skill for it
│   │       └── AR: Default generation is one option. Skilled generation is diverse (conventional, unconventional, extreme), constrained, and purpose-driven.
│   │           └── [CRUX 5: Does structured generation produce better output than default LLM generation?]

**VERDICT: VALIDATED**
Create a generate skill: given constraints + purpose + domain, produce N diverse candidates (one conventional, one unconventional, one extreme minimum).

---

### CANDIDATE 8: Rewrite space_enumeration to find surprising options

**AR: Current space_enumeration is exhaustive but not insightful**
├── It focuses on: granularity levels, enumeration strategies (Cartesian product, dimension-by-dimension)
│   ├── AR: Completeness is necessary but not sufficient
│   │   ├── Exhaustive enumeration of obvious dimensions misses non-obvious dimensions
│   │   │   └── AR: The value is in finding what you DIDN'T KNOW was an option
│   │   │       └── This is what universalization techniques do — and space_enumeration doesn't use them
│   │   │           └── [NOVEL] space_enumeration should incorporate universalization to discover hidden dimensions before enumerating
│   │   └── AW: space_enumeration's job is to enumerate a GIVEN space, not to discover the space
│   │       └── AR: Fair distinction. But "given space" is often incomplete. Add an optional "expand space" step.
│   │           └── [CRUX 6: Should enumeration skills also discover dimensions, or leave that to other skills?]

**VERDICT: VALIDATED WITH CONDITIONS**
Add an optional "dimension discovery" preamble. Keep the core enumeration mechanics (they work). Make the skill surface surprising dimensions, not just enumerate known ones.

---

### Remaining candidates (abbreviated)

**CANDIDATE 6: Adaptive root_cause_5_whys** — VALIDATED. The "5" in 5 whys is arbitrary. Some causes are 2 levels deep, some are 10. Make it adaptive: stop when you hit root, not at 5.

**CANDIDATE 9: Rewrite finder** — VALIDATED WITH CONDITIONS. The intent-matching concept is good. But: the 318-skill registry is a flat list. It should be a hierarchy or graph. Lower priority — the current finder works adequately.

**CANDIDATE 11: Critique skill** — VALIDATED. Structured critique using gestalt principle + analytical decomposition. Would complement the generate skill. Generate → Critique → Iterate is the creative loop.

**CANDIDATE 12: Iterate skill** — REJECTED. Iteration is a PATTERN (generate → evaluate → improve), not a standalone skill. It's better embedded in skills that need it (like the design skill).

### A1 SUMMARY

| # | Candidate | Verdict |
|---|-----------|---------|
| 1 | Rewrite GOSM | VALIDATED |
| 2 | Rewrite procedure_engine | VALIDATED |
| 3 | Rewrite high_quality_writing | VALIDATED |
| 4 | Rewrite comparison | VALIDATED |
| 5 | Rewrite meta_reasoning_core | VALIDATED |
| 6 | Adaptive root_cause | VALIDATED |
| 7 | Create design skill | VALIDATED |
| 8 | Improve space_enumeration | WITH CONDITIONS |
| 9 | Rewrite finder | WITH CONDITIONS |
| 10 | Create generate skill | VALIDATED |
| 11 | Create critique skill | VALIDATED |
| 12 | Create iterate skill | REJECTED |

[T:result] A1: 8 validated, 1 rejected, 3 with conditions

---

## U2: EDGE CASE DISCOVERY

**EC1: Rewriting all skills at once risks breaking the toolkit**
- The skills call each other. Changing one might break callers.
- Condition: prioritize by independence — rewrite skills that are called BY others last

**EC2: The new UAUA/ARAW haven't been battle-tested yet**
- We rewrote them based on analysis. They might have issues we haven't found.
- Condition: use the rewritten skills on a few real tasks before rewriting more

**EC3: Some "old style" skills work fine**
- Not everything needs rewriting. Some skills (like space_enumeration) are focused utilities where procedure IS appropriate.
- [NOVEL] Procedure-style is appropriate for MECHANICAL skills (enumeration, scoring). Principles-style is appropriate for JUDGMENT skills (analysis, comparison, writing).

**EC4: Creating new skills (design, generate, critique) adds maintenance burden**
- 220 skills is already a lot. 223 is worse.
- Condition: new skills should REPLACE or CONSOLIDATE existing ones where possible

**EC5: The LLM might read the OLD version of SKILL.md if cached**
- Plugin caching might serve old versions even after rewrite
- Condition: verify cache invalidation after each rewrite

**EC6: Users invoking skills by name expect consistent behavior**
- If /comparison suddenly works differently, users might be confused
- Condition: improvements should make output BETTER, not just DIFFERENT. The interface (what the user asks for) stays the same; the output quality improves.

**EC7: The "principles vs procedures" distinction might be wrong for some skills**
- Some skills ARE inherently procedural (enumeration, data collection, testing strategy)
- [NOVEL] Two categories: JUDGMENT skills (benefit from principles) and MECHANICAL skills (benefit from procedures). Don't force principles onto mechanical skills.

**EC8: Compound skills (field_analysis, assumption_audit) chain other skills**
- If the chained skills improve, the compound skills improve automatically
- Condition: prioritize PRIMITIVE skills (comparison, generate, writing) over COMPOUND skills (field_analysis, cross_domain_report)

[T:result] U2 found 8 edge cases, 2 novel insights

---

## A2: FINAL VALIDATION

**EC3/EC7: Procedure vs Principles split**
└── MATTERS — Categorize skills before rewriting. Don't apply principles-style to mechanical skills.

**EC1: Breaking the toolkit**
└── MATTERS — Rewrite in dependency order: primitives first, callers second.

**EC2: Battle-test first**
└── MATTERS — Run the new UAUA/ARAW on 3-5 real tasks before rewriting more.

**EC8: Primitives before compounds**
└── MATTERS — Compounds auto-improve when primitives improve.

### FINAL STATUS

| # | Candidate | Final Status | Priority |
|---|-----------|-------------|----------|
| 7 | **Create design skill** | VALIDATED | P0 — biggest gap in toolkit |
| 10 | **Create generate skill** | VALIDATED | P0 — enables generative capability |
| 11 | **Create critique skill** | VALIDATED | P0 — complements generate |
| 3 | **Rewrite high_quality_writing** | VALIDATED | P1 — affects all text output |
| 5 | **Rewrite meta_reasoning_core** | VALIDATED | P1 — governs skill selection |
| 4 | **Rewrite comparison** | VALIDATED | P1 — used in every decision |
| 1 | **Rewrite GOSM** | VALIDATED | P2 — entry point, but works adequately |
| 2 | **Rewrite procedure_engine** | VALIDATED | P2 — deep analysis path |
| 6 | **Adaptive root_cause** | VALIDATED | P2 — useful but not critical |
| 8 | **Improve space_enumeration** | WITH CONDITIONS | P3 — works adequately as-is |
| 9 | **Rewrite finder** | WITH CONDITIONS | P3 — works adequately |

[T:result] Final: 9 validated, 1 rejected, 2 with conditions

---

## SYNTHESIS

### Structure of Findings

The toolkit has three categories of improvement:

**1. MISSING CAPABILITIES (create new skills)**
- Generate (produce diverse candidates)
- Design (apply 40 universal principles)
- Critique (gestalt + analytical evaluation)
These three form the creative loop: Generate → Critique → Iterate. The toolkit currently has zero generative capability.

**2. OVER-PROCEDURALIZED JUDGMENT SKILLS (rewrite with principles)**
- high_quality_writing (checklist → generative guide)
- meta_reasoning_core (10 steps → 3 questions)
- comparison (scoring → qualitative + quantitative)
- procedure_engine (12 steps → 5 principles + routing)
- GOSM (6 inline variants → pure dispatcher)

**3. ADEQUATE MECHANICAL SKILLS (leave alone or minor tweaks)**
- space_enumeration (add optional dimension discovery)
- root_cause_5_whys (make depth adaptive)
- finder (minor improvement to intent matching)

### Key Insight

**The toolkit is built for EVALUATION but not for CREATION.** Every skill analyzes, compares, tests, or validates. None produce. The highest-impact improvement is adding the generate/design/critique triad — this makes the toolkit useful for creative work, not just analytical work.

### Testable Predictions

1. If we create a design skill and use it on the website, it should produce better results than the UAUA 16x design session did (because it will GENERATE designs, not just ANALYZE what's wrong).
2. If we rewrite high_quality_writing with generative principles, text output quality should visibly improve on the next writing task.
3. If we reduce meta_reasoning_core from 10 steps to 3 questions, it should route to the correct skill MORE often (because principles activate judgment, procedures activate compliance).

### DO_FIRST Actions

**DO_FIRST 1: Create the generate skill** (~100-150 lines)
- Core: given constraints + purpose + domain → produce N diverse candidates
- At minimum: one conventional, one unconventional, one extreme
- This is a primitive that other skills will call

**DO_FIRST 2: Create the design skill** (~150-200 lines)
- Based on the 40 universal design principles
- Domain-adaptive effort ordering
- Embeds generate + critique + iterate loop
- Includes exemplar grounding and gestalt principle

**DO_FIRST 3: Create the critique skill** (~100-150 lines)
- Structured evaluation: gestalt impression FIRST, then analytical decomposition
- Check for divergence between impression and analysis
- Domain-appropriate criteria (use design principles for design, writing principles for writing)

**DO_FIRST 4: Rewrite high_quality_writing** (~200 lines)
- Principles-first generative writing tool
- Keep weak pattern detection (it's good)
- Add: voice, narrative structure, reader journey
- Make it a WRITING tool, not a writing AUDIT tool

**DO_FIRST 5: Rewrite meta_reasoning_core** (~80 lines)
- 3 core questions: What am I trying to achieve? Is this the best way? Am I making progress?
- Guidance on when to ask each
- Remove 7 redundant steps

**DO_FIRST 6: Rewrite comparison** (~150 lines)
- Add gestalt impression before scoring
- Replace 0-3 scoring with tier comparison
- Keep structured criteria + add qualitative layer
- Add divergence check: does scoring match impression?

[T:result] UAUA 4x complete: 9 validated, 1 rejected, 2 conditional from 12 candidates
[D:derivation] Core insight: the toolkit is evaluation-only; adding generative capability is the highest-impact improvement
