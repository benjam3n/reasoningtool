# AR — Long-Form Writing Scaling

**Date**: 2026-01-29
**Depth**: 4x
**Input**: reasoningtool needs to be able to do longer form writing, like hundreds of pages to thousands of pages, to tens of thousands. there are limitations that prevent it from doing this with quality and reliability so far but since it can do one page pretty well i think it can scale. some things need to be changed about the project or some new skills need to be added or some new critieria or something else novel needs to be added.

---

## Phase 1: EXPLORATION

### Step 1: State the Claim

```
CLAIM: Reasoningtool needs to scale to long-form writing (hundreds to tens of thousands of pages), and since it can do one page well, it can scale — but something about the project needs to change (new skills, criteria, or something novel) to get there.
ASSUMING THIS IS: The right approach — that scaling from short-form to long-form is achievable and necessary.
```

This is a compound claim. Let me unbundle before recursing:

- **C-A**: The toolkit needs long-form capability (hundreds to tens of thousands of pages)
- **C-B**: One-page quality implies scalability to longer forms
- **C-C**: Changes to the project (new skills, criteria, or something novel) are what's needed to bridge the gap

### Step 2: Find Implications (Recurse)

```
[R1] "The toolkit needs to scale to long-form writing (100s to 10,000s of pages)"
  If right, then:

  [R2] The toolkit's value proposition shifts from "think better about X" to "produce sustained coherent output about X" — Necessary
    If right, then:
    [R3] The core problem changes: short-form = quality of reasoning per page; long-form = maintaining coherence, consistency, and quality ACROSS pages — Necessary
      If right, then:
      [R4] The bottleneck is no longer the skill prompt but STATE MANAGEMENT — tracking what's been said, decided, established across hundreds of pages — Necessary
        If right, then:
        [R5] Prompt-only solutions cannot work because LLM context windows cannot hold thousands of pages — BEDROCK-LOGIC: Current context windows are 100k-200k tokens ≈ 75-150 pages. Thousands of pages exceeds any single context.
        [R6] You need an external memory system — a database, file system, or index that the writing process reads from and writes to — Necessary
          If right, then:
          [R7] This is no longer prompt engineering — it's software engineering. The "skill" becomes an orchestration layer that manages state across multiple LLM calls — Necessary
            If right, then:
            [R8] The project changes category: from "collection of Claude Code skills" to "agent framework for long-form generation" — BEDROCK-OBSERVE: These are different project types with different architectures, testing needs, and user interfaces.
        [R9] You need a PLAN structure that exists outside any single generation call — an outline, chapter map, or hierarchical structure that governs what each section contains — Necessary
          If right, then:
          [R10] The plan itself is a reasoning artifact — generating a good plan for 1000 pages IS the hard problem, and the actual page-by-page writing is the easier part — Probable
            If right, then:
            [R11] The existing skills (UAUA, ARAW, /u) are well-suited for PLANNING long-form work but not for EXECUTING it — the planning/execution gap is the real bottleneck — BEDROCK-TEST: Run /uaua on "outline a 500-page book on X" and see whether the output is a usable plan vs. an analysis of the idea.

      [R12] Quality at scale requires CONSISTENCY CHECKING — does page 400 contradict page 50? Does the argument on page 200 actually follow from the premise on page 10? — Necessary
        If right, then:
        [R13] You need automated verification that operates across the full document — not just spell-check but logical consistency, argument coherence, style consistency, and factual non-contradiction — Necessary
          If right, then:
          [R14] This is a different skill entirely from writing — it's closer to code review or formal verification applied to prose — Probable
            If right, then:
            [R15] You'd need a /verify_long_form skill that takes a document and checks it against its own premises, claims, and style — BEDROCK-TEST: Build a prototype that checks chapters against an outline for drift.

    [R16] FORECLOSED: The toolkit remains "just skills." If long-form is the goal, skills are components, not the product. — Necessary
      If right, then:
      [R17] The README, the subreddit, the framing of "207 thinking skills" — all of this becomes secondary to the long-form capability — Probable
        If right, then:
        [R18] The user base shifts: from "people who want to think better" to "people who want to produce long documents" — these are overlapping but different audiences — BEDROCK-OBSERVE: Writers, researchers, and analysts need long-form. Quick decision-makers need short-form skills. Different people.

  [R19] The toolkit must handle at MINIMUM three scales that have qualitatively different challenges — Necessary
    If right, then:
    [R20] Scale 1: 1-10 pages — current capability. Single context window. Skill prompt governs quality. Works now. — BEDROCK-OBSERVE: Demonstrated in this session.
    [R21] Scale 2: 10-100 pages — fits in context but pushes limits. Needs outline-first approach, section-by-section generation, and cross-section consistency. — Probable
      If right, then:
      [R22] This is achievable with a "plan then execute" pattern: /uaua generates the plan, then a new skill generates each section while referencing the plan and previous sections — Probable
        If right, then:
        [R23] This is the MINIMUM VIABLE long-form capability — and it's buildable with current tools (Claude Code + file system + skills) — BEDROCK-TEST: Try writing a 50-page document using plan-then-execute and measure coherence degradation.
      [R24] Even at this scale, the "quality per page" assumption breaks: page 80 will be worse than page 5 because the model is farther from the plan and has accumulated drift — Probable
        If right, then:
        [R25] You need a CORRECTION LOOP — generate, verify, revise — not just generate-once — Necessary
          If right, then:
          [R26] This multiplies compute cost by at least 3x (generate + verify + revise) per section — BEDROCK-LOGIC: Three passes minimum means 3x the API calls.

    [R27] Scale 3: 100-10,000+ pages — exceeds any single context. Requires external memory, hierarchical planning, section interdependency tracking, and multi-pass verification — Necessary
      If right, then:
      [R28] This is a FUNDAMENTALLY different engineering problem than Scales 1-2. It's closer to how software manages large codebases (modules, interfaces, dependency graphs) than how writers write books. — Probable
        If right, then:
        [R29] The relevant prior art isn't other writing tools — it's compiler design, database systems, and version control. Documents at this scale need something like "git for prose" — BEDROCK-TEST: Search for existing tools that manage 10,000+ page document consistency. Do they exist? What architecture do they use?
      [R30] No human writes 10,000 pages as a single coherent document. This is the scale of encyclopedias, legal codes, and technical documentation suites — multi-author, multi-year projects — Necessary
        If right, then:
        [R31] The toolkit would be competing with/replacing collaborative document management systems, not writing assistants — BEDROCK-OBSERVE: Confluence, GitBook, and documentation-as-code systems serve this scale.
        [R32] FORECLOSED: A single-user, single-session tool cannot produce 10,000+ coherent pages. The architecture MUST be multi-session, persistent, and probably multi-agent. — BEDROCK-LOGIC: 10,000 pages at 500 words/page = 5 million words. At even 1000 words/minute generation speed, that's 83 hours of continuous generation, not counting verification.

  [R33] "Since it can do one page pretty well, I think it can scale" — if this inference is right, then quality scales sublinearly or linearly with length — Probable
    If right, then:
    [R34] But writing quality doesn't scale linearly — it degrades. The longer the document, the more opportunities for inconsistency, drift, repetition, and structural breakdown — Necessary
      If right, then:
      [R35] The one-page-to-N-pages inference is WRONG in its naive form — quality doesn't just extend, it actively degrades without countermeasures — BEDROCK-TENSION: Contradicts R33. Quality degrades superlinearly with length unless architecture compensates.
      [R36] The correct version: "It can do one page well" implies the COMPONENTS work — the reasoning, the prose, the analysis. What's missing is the ARCHITECTURE to compose components without degradation — Probable
        If right, then:
        [R37] The project needs to add an architectural layer ON TOP of the existing skills, not replace them — Necessary
          If right, then:
          [R38] Existing skills become "micro-generators" that produce quality within their scope, and a new orchestration layer manages their composition — Probable
            If right, then:
            [R39] The new thing isn't a skill — it's an engine. A long-form generation engine that calls skills as subroutines. — BEDROCK-TEST: Prototype an engine that calls /high_quality_writing for each section while maintaining state across sections. Does the output cohere?

    [R40] The degradation has identifiable failure modes that could be specifically countered — Probable
      If right, then:
      [R41] Failure mode: DRIFT — the document gradually shifts away from its plan/premise — Necessary
        If right, then:
        [R42] Counter: periodic re-anchoring against the plan. Every N pages, compare current state to plan and correct. — BEDROCK-TEST: Measure drift at page 10, 20, 50 with and without re-anchoring.
      [R43] Failure mode: CONTRADICTION — page N says X, page M says not-X — Necessary
        If right, then:
        [R44] Counter: maintain a claim registry (like the skills already do!) across the entire document. Every assertion gets tracked. New assertions get checked against existing ones. — Probable
          If right, then:
          [R45] The three-phase architecture you just built (exploration → registry → synthesis) is actually the RIGHT ARCHITECTURE for long-form consistency — the registry IS the consistency mechanism — BEDROCK-TENSION: This is a tension because it implies the skills DO scale, but only if the registry is externalized and persistent, not just per-session.
      [R46] Failure mode: REPETITION — the same point gets made multiple times because the model can't remember what it already said — Necessary
        If right, then:
        [R47] Counter: a summary index that each section checks before generating. "These points have been made: [list]. Do not repeat them." — BEDROCK-TEST: Compare repetition rates with and without a running summary index.
      [R48] Failure mode: STRUCTURAL COLLAPSE — the overall argument structure breaks down. Sections don't connect. The document reads as disconnected chunks. — Necessary
        If right, then:
        [R49] Counter: hierarchical plan with explicit section-to-section transitions. Each section knows what came before and what comes after. — Probable
          If right, then:
          [R50] This requires a "document graph" — not just an outline but a dependency graph of which sections depend on which premises — Probable
            If right, then:
            [R51] Building and maintaining this graph IS the hard engineering problem. The writing itself is secondary. — BEDROCK-TEST: Attempt to build a document graph for a 100-page document and see if the graph itself is manageable.

  [R52] "Some things need to be changed about the project or some new skills need to be added or some new criteria or something else novel needs to be added" — if right, then the changes are identifiable — Necessary
    If right, then:
    [R53] Change type 1: NEW SKILL — a /long_form or /compose skill that orchestrates multi-section generation — Probable
      If right, then:
      [R54] This skill would need to: (a) accept a plan/outline, (b) generate sections sequentially, (c) maintain state between sections, (d) verify consistency, (e) allow revision — Necessary
        If right, then:
        [R55] This exceeds what a SKILL.md prompt can do — it requires code (a script, an agent loop, or a Claude Code hook system) — BEDROCK-LOGIC: A static prompt cannot maintain state across multiple independent LLM calls. State requires persistent storage and procedural logic.

    [R56] Change type 2: NEW CRITERIA — quality metrics specific to long-form coherence — Probable
      If right, then:
      [R57] Metrics needed: consistency score (do claims contradict?), drift score (does content match plan?), repetition score (how often are points restated?), structural coherence score (do sections connect?) — Probable
        If right, then:
        [R58] These metrics could be implemented as a /verify_document skill that runs AFTER generation — BEDROCK-TEST: Build one metric (consistency) and test it on a 20-page generated document.

    [R59] Change type 3: NOVEL ARCHITECTURE — something that doesn't exist yet in the project — Probable
      If right, then:
      [R60] The novel thing is: a persistent registry that spans multiple sessions and skill invocations. The claim registry from ARAW, but externalized and accumulative. — Probable
        If right, then:
        [R61] This turns the toolkit from "stateless skills" into "stateful reasoning system" — a fundamental architectural shift — BEDROCK-OBSERVE: The current architecture is stateless — each skill invocation starts fresh. Long-form requires statefulness.
      [R62] The novel thing might also be: a DECOMPOSITION ENGINE that takes "write 500 pages about X" and produces a complete hierarchical plan with dependency graph, then executes it section by section — Probable
        If right, then:
        [R63] This is essentially a compiler: source (high-level intent) → intermediate representation (plan/outline) → target (generated pages) → optimization passes (verify/revise) — BEDROCK-LOGIC: The compiler analogy is structurally exact. Intent → IR → output → optimization is how compilers work.
```

### Step 3: Find the Pattern

**Pattern: CONSTRAINING then CONVERGENT**

The claim starts expansive (long-form is possible!) but rapidly constrains: it requires external memory (R6), code not just prompts (R7, R55), multi-session persistence (R32, R61), and a fundamentally different architecture (R8, R39, R63). Multiple branches converge on the same requirement: **the toolkit needs a stateful orchestration engine, not more skills.**

Key convergence points:
- R7, R39, R55, R63 all converge on: **this requires code, not prompts**
- R6, R9, R44, R60, R61 all converge on: **state must persist across calls**
- R36, R37, R38, R45 all converge on: **existing skills are valid components, the missing piece is composition**

One critical tension: R35 contradicts R33. Quality doesn't scale linearly — it degrades. But R45 suggests the registry architecture already built might be the right consistency mechanism IF externalized.

---

## Phase 2: CLAIM REGISTRY

```
CLAIM REGISTRY
==============

[R1] Toolkit needs to scale to 100s-10,000s of pages — TYPE: implication — STRENGTH: necessary
[R2] Value shifts from "think better" to "produce sustained coherent output" — TYPE: commitment — STRENGTH: necessary
[R3] Core problem changes to maintaining coherence ACROSS pages — TYPE: implication — STRENGTH: necessary
[R4] Bottleneck becomes state management — TYPE: implication — STRENGTH: necessary
[R5] Context windows can't hold 1000s of pages — TYPE: foreclosure — STRENGTH: necessary (BEDROCK-LOGIC)
[R6] External memory system needed — TYPE: implication — STRENGTH: necessary
[R7] Becomes software engineering, not prompt engineering — TYPE: commitment — STRENGTH: necessary
[R8] Project changes category to "agent framework for long-form generation" — TYPE: commitment — STRENGTH: necessary (BEDROCK-OBSERVE)
[R9] Plan structure must exist outside any single generation call — TYPE: implication — STRENGTH: necessary
[R10] Generating the plan IS the hard problem — TYPE: implication — STRENGTH: probable
[R11] Existing skills suited for PLANNING but not EXECUTING long-form — TYPE: tension — STRENGTH: probable (BEDROCK-TEST)
[R12] Quality at scale requires consistency checking — TYPE: implication — STRENGTH: necessary
[R13] Automated verification across full document needed — TYPE: implication — STRENGTH: necessary
[R14] Verification is closer to code review than writing — TYPE: implication — STRENGTH: probable
[R15] Need a /verify_long_form skill — TYPE: implication — STRENGTH: probable (BEDROCK-TEST)
[R16] FORECLOSED: toolkit remains "just skills" — TYPE: foreclosure — STRENGTH: necessary
[R17] Current framing (207 skills, subreddit) becomes secondary — TYPE: cost — STRENGTH: probable
[R18] User base shifts from thinkers to producers — TYPE: commitment — STRENGTH: probable (BEDROCK-OBSERVE)
[R19] Three qualitatively different scales exist — TYPE: implication — STRENGTH: necessary
[R20] Scale 1 (1-10 pages) works now — TYPE: implication — STRENGTH: necessary (BEDROCK-OBSERVE)
[R21] Scale 2 (10-100 pages) needs outline-first + section-by-section — TYPE: implication — STRENGTH: probable
[R22] Plan-then-execute pattern achievable for Scale 2 — TYPE: implication — STRENGTH: probable
[R23] Scale 2 is minimum viable long-form — TYPE: implication — STRENGTH: probable (BEDROCK-TEST)
[R24] Quality degrades with distance from plan — TYPE: cost — STRENGTH: probable
[R25] Correction loop needed (generate-verify-revise) — TYPE: implication — STRENGTH: necessary
[R26] 3x compute cost minimum — TYPE: cost — STRENGTH: necessary (BEDROCK-LOGIC)
[R27] Scale 3 (100-10,000+) requires fundamentally different architecture — TYPE: implication — STRENGTH: necessary
[R28] Engineering problem closer to codebases than books — TYPE: implication — STRENGTH: probable
[R29] Prior art is compilers/databases/VCS, not writing tools — TYPE: implication — STRENGTH: probable (BEDROCK-TEST)
[R30] No human writes 10,000 coherent pages solo — TYPE: implication — STRENGTH: necessary
[R31] Competing with collaborative document systems — TYPE: commitment — STRENGTH: probable (BEDROCK-OBSERVE)
[R32] FORECLOSED: single-user, single-session at 10K+ pages — TYPE: foreclosure — STRENGTH: necessary (BEDROCK-LOGIC)
[R33] Quality scales sublinearly/linearly with length — TYPE: implication — STRENGTH: probable
[R34] Quality actually degrades superlinearly — TYPE: cost — STRENGTH: necessary
[R35] Naive one-page-to-N inference is wrong — TYPE: tension — STRENGTH: necessary (BEDROCK-TENSION with R33)
[R36] Components work; architecture for composition is missing — TYPE: implication — STRENGTH: probable
[R37] Need architectural layer ON TOP of existing skills — TYPE: implication — STRENGTH: necessary
[R38] Skills become micro-generators; orchestration layer composes — TYPE: implication — STRENGTH: probable
[R39] The new thing is an ENGINE, not a skill — TYPE: implication — STRENGTH: probable (BEDROCK-TEST)
[R40] Degradation has identifiable, counterable failure modes — TYPE: implication — STRENGTH: probable
[R41] Failure: DRIFT from plan — TYPE: implication — STRENGTH: necessary
[R42] Counter: periodic re-anchoring — TYPE: implication — STRENGTH: probable (BEDROCK-TEST)
[R43] Failure: CONTRADICTION across pages — TYPE: implication — STRENGTH: necessary
[R44] Counter: persistent claim registry across document — TYPE: implication — STRENGTH: probable
[R45] Three-phase registry architecture IS the consistency mechanism (if externalized) — TYPE: tension — STRENGTH: probable (BEDROCK-TENSION)
[R46] Failure: REPETITION — TYPE: implication — STRENGTH: necessary
[R47] Counter: running summary index — TYPE: implication — STRENGTH: probable (BEDROCK-TEST)
[R48] Failure: STRUCTURAL COLLAPSE — TYPE: implication — STRENGTH: necessary
[R49] Counter: hierarchical plan with explicit transitions — TYPE: implication — STRENGTH: probable
[R50] Need a document dependency graph — TYPE: implication — STRENGTH: probable
[R51] Building the graph IS the hard problem — TYPE: implication — STRENGTH: probable (BEDROCK-TEST)
[R52] The needed changes are identifiable — TYPE: implication — STRENGTH: necessary
[R53] New skill: /long_form or /compose — TYPE: implication — STRENGTH: probable
[R54] Skill needs: plan input, sequential generation, state, verification, revision — TYPE: implication — STRENGTH: necessary
[R55] Exceeds what SKILL.md can do — needs code — TYPE: foreclosure — STRENGTH: necessary (BEDROCK-LOGIC)
[R56] New criteria: long-form quality metrics — TYPE: implication — STRENGTH: probable
[R57] Metrics: consistency, drift, repetition, structural coherence — TYPE: implication — STRENGTH: probable
[R58] Implementable as /verify_document skill — TYPE: implication — STRENGTH: probable (BEDROCK-TEST)
[R59] Novel architecture needed — TYPE: implication — STRENGTH: probable
[R60] Novel thing: persistent registry spanning sessions — TYPE: implication — STRENGTH: probable
[R61] Shifts toolkit from stateless to stateful — TYPE: commitment — STRENGTH: necessary (BEDROCK-OBSERVE)
[R62] Decomposition engine: intent → plan → sections → verification — TYPE: implication — STRENGTH: probable
[R63] Structurally identical to a compiler — TYPE: implication — STRENGTH: probable (BEDROCK-LOGIC)

TOTALS:
- Total claims: 63
- Implications: 44
- Foreclosures: 5 (R5, R16, R32, R35, R55)
- Commitments: 6 (R2, R7, R8, R18, R31, R61)
- Costs: 4 (R17, R24, R26, R34)
- Tensions: 3 (R11, R35, R45)
- Bedrock reached: 17 (6 TEST, 4 LOGIC, 4 OBSERVE, 3 TENSION)
- Strength: 20 necessary, 36 probable, 0 possible
```

---

## Phase 3: SYNTHESIS

```
ORIGINAL CLAIM: Reasoningtool needs long-form capability and can scale from one-page quality.

IMPLICATION PATTERN: Constraining then Convergent

COMMITMENT CHAIN:
If this is right:
→ you must accept:
  - The project changes category from "skill collection" to "agent framework" (R8)
  - This is software engineering, not prompt engineering (R7)
  - The toolkit must become stateful (R61)
  - State management is the bottleneck, not writing quality (R4)
  - Correction loops are mandatory, 3x+ compute cost (R25, R26)
  - External memory is required (R6)
  - A plan structure must exist outside any single call (R9)
  - Consistency checking is non-optional (R12, R13)

→ you probably accept:
  - Existing skills become components of a larger engine (R38)
  - The three-phase registry architecture is the right consistency mechanism if externalized (R45)
  - The system is structurally a compiler: intent → plan → output → optimization (R63)
  - User base shifts from thinkers to producers (R18)

→ you can no longer:
  - Keep the toolkit as "just skills" (R16)
  - Use single-session, single-user architecture at scale 3 (R32)
  - Rely on prompt-only solutions (R5, R55)
  - Assume quality extends linearly with length (R35)

→ you lose:
  - Simplicity of "copy skills into your project and go" (R17)
  - Low compute costs (R26)
  - The current value proposition for short-form users (R17, R18)

WHAT THE RIGHTNESS ANALYSIS ACTUALLY FOUND:
1. Three distinct scales exist with qualitatively different challenges:
   1-10 pages (works now), 10-100 pages (achievable with plan-execute
   pattern), 100-10,000+ pages (requires fundamentally different
   architecture) — R19-R32
2. The naive inference "one page works → N pages work" is wrong.
   Quality degrades superlinearly. But the COMPONENTS work — the
   missing piece is composition architecture. — R33-R39
3. Four specific failure modes at scale: drift (R41), contradiction
   (R43), repetition (R46), structural collapse (R48). Each has
   identifiable counters. — R40-R51
4. The three-phase registry architecture already built (exploration →
   registry → synthesis) is actually the right pattern for long-form
   consistency — IF the registry is externalized and persistent rather
   than per-session. — R44, R45, R60
5. The new thing needed is an ENGINE (orchestration layer), not a
   SKILL (prompt). Skills become subroutines the engine calls. — R7,
   R39, R55, R63
6. The engine is structurally a compiler: high-level intent → plan
   (IR) → generated sections (output) → verification passes
   (optimization). — R63
7. Scale 2 (10-100 pages) is the minimum viable next step and is
   buildable with current tools. — R22, R23
8. Scale 3 (100-10,000+) competes with collaborative document systems,
   not writing assistants. No human writes this much solo either. — R30, R31

TENSIONS / CONTRADICTIONS:
1. R33 vs R35: Quality scales linearly vs. quality degrades. Resolved
   by R36 — components scale, composition doesn't without architecture.
2. R45 vs R61: Registry architecture is right vs. toolkit must become
   stateful. These aren't contradictory — they converge. The registry
   is right but must be externalized.
3. R11: Skills suited for planning but not executing. Tension between
   current capability and target capability.

WEAKEST LINKS:
- R22 (Probable): Plan-then-execute works for Scale 2. Untested.
- R38 (Probable): Skills as micro-generators. Assumes they compose well.
- R44 (Probable): Persistent claim registry as contradiction detector. Unbuilt.
- R50 (Probable): Document dependency graph is manageable. Untested at scale.
- R62 (Probable): Decomposition engine is buildable. Major engineering effort.

TESTABLE PREDICTIONS:
- A 50-page document generated with plan-then-execute will show
  measurable coherence degradation vs. a 5-page one (R23, R24)
- Re-anchoring every 10 pages will reduce drift compared to no
  re-anchoring (R42)
- A persistent claim registry will catch contradictions that a human
  reader misses on first pass (R44, R45)
- The plan/outline generation (using existing skills) will be the
  highest-quality part; the section-by-section execution will be where
  quality drops (R10, R11)

UNRESOLVED:
- R23: Whether Scale 2 actually works — needs empirical test
- R29: What prior art exists for 10,000+ page document consistency
- R39: Whether the engine can be built within Claude Code or needs a
  separate codebase
- R51: Whether document graphs are manageable at 100+ page scale
- R58: Whether automated quality metrics produce actionable scores
```
