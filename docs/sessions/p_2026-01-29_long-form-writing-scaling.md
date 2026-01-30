# Propose — Long-Form Writing Scaling

**Date**: 2026-01-29
**Source**: /ar on "Long-form writing scaling for reasoningtool" at depth 4x
**Input**: look at reasoningtool/araw/sessions long form writing scaling and propose from there

---

## Phase 1: PLAN EXTRACTION

### Step 1: Identify the Source

```
SOURCE ANALYSIS: ar (Assume Right)
SOURCE TOPIC: Long-form writing scaling for reasoningtool
SOURCE DEPTH: 4x
ITEM PREFIX: R
TOTAL SOURCE ITEMS: 63
```

### Step 2: Extract Plan Seeds

```
[SEED-1] Build a plan-then-execute pipeline for Scale 2 (10-100 pages) -- SOURCE: R21, R22, R23 -- SEED TYPE: Validated claim (probable, testable)
[SEED-2] Build an external state/memory system that persists across LLM calls -- SOURCE: R6, R9, R60, R61 -- SEED TYPE: Convergent implication (4 branches converge)
[SEED-3] Build an orchestration engine (not a skill) that calls skills as subroutines -- SOURCE: R7, R39, R55, R63 -- SEED TYPE: Convergent implication (4 branches converge)
[SEED-4] Build a persistent claim registry for cross-document consistency -- SOURCE: R44, R45, R60 -- SEED TYPE: Derived alternative (externalize existing architecture)
[SEED-5] Build a /verify_long_form skill for automated quality checking -- SOURCE: R13, R14, R15, R58 -- SEED TYPE: DO_FIRST action
[SEED-6] Implement drift countermeasures (periodic re-anchoring) -- SOURCE: R41, R42 -- SEED TYPE: Derived alternative
[SEED-7] Implement repetition countermeasures (running summary index) -- SOURCE: R46, R47 -- SEED TYPE: Derived alternative
[SEED-8] Implement structural coherence countermeasures (document dependency graph) -- SOURCE: R48, R49, R50, R51 -- SEED TYPE: Derived alternative
[SEED-9] Build a decomposition engine: intent → plan → sections → verification -- SOURCE: R62, R63 -- SEED TYPE: Convergent implication
[SEED-10] Reposition the project as "agent framework for long-form generation" -- SOURCE: R8, R16, R17, R18 -- SEED TYPE: Foreclosure (toolkit can't remain "just skills")
[SEED-11] Target Scale 3 (100-10,000+ pages) with multi-session, multi-agent architecture -- SOURCE: R27, R28, R29, R30, R31, R32 -- SEED TYPE: Implication
[SEED-12] Add long-form quality metrics (consistency, drift, repetition, structural coherence) -- SOURCE: R56, R57, R58 -- SEED TYPE: Derived alternative
[SEED-13] Implement correction loops (generate-verify-revise) -- SOURCE: R25, R26 -- SEED TYPE: Convergent implication
```

### Step 3: Cluster Seeds into Plans

```
[PLAN-1] Build Scale 2 (10-100 pages) using plan-then-execute with existing tools
  Seeds: SEED-1, SEED-6, SEED-7, SEED-13
  Source items: R21, R22, R23, R24, R25, R26, R41, R42, R46, R47

[PLAN-2] Build a stateful orchestration engine that calls skills as subroutines
  Seeds: SEED-2, SEED-3, SEED-9
  Source items: R6, R7, R9, R39, R55, R60, R61, R62, R63

[PLAN-3] Build a persistent cross-document claim registry
  Seeds: SEED-4, SEED-8
  Source items: R44, R45, R48, R49, R50, R51, R60

[PLAN-4] Build a /verify_long_form skill with automated quality metrics
  Seeds: SEED-5, SEED-12
  Source items: R13, R14, R15, R56, R57, R58

[PLAN-5] Reposition the project from "skill collection" to "long-form generation framework"
  Seeds: SEED-10
  Source items: R8, R16, R17, R18, R31

[PLAN-6] Target Scale 3 (100-10,000+ pages) with multi-session, multi-agent architecture
  Seeds: SEED-11
  Source items: R27, R28, R29, R30, R31, R32
```

### Step 4: Steelman Each Plan

```
[PLAN-1] STEELMAN:
  STRONGEST CASE: Scale 2 is buildable with current tools — Claude Code, the file system, and existing
  skills. No new architecture is needed. You already have quality per-page generation. The plan-then-
  execute pattern (use /uaua or /araw for the outline, then generate sections referencing the plan and
  prior sections) is the simplest possible path to long-form capability. Adding drift re-anchoring and
  a summary index are incremental additions, not architectural rewrites. This delivers a working
  50-page document fastest.
  BEST CONDITIONS: When you want a working prototype soon, are willing to accept 10-100 page scope,
  and want to validate the core assumption (components compose) before committing to larger architecture.
  IDEAL OUTCOME: A repeatable process that produces coherent 50-100 page documents using existing skills
  plus lightweight coordination, proving the scaling thesis at the first non-trivial scale.
  SOURCE SUPPORT: R22 (plan-then-execute achievable), R23 (minimum viable long-form, buildable now),
  R20 (Scale 1 already works), R36 (components work, composition is the gap), R42 (re-anchoring
  counters drift), R47 (summary index counters repetition).

[PLAN-2] STEELMAN:
  STRONGEST CASE: Multiple independent branches of the analysis converge on the same conclusion: the
  missing piece isn't another skill — it's an engine that orchestrates skills. R7, R39, R55, and R63
  all arrive at this from different directions. The compiler analogy (R63) is structurally exact:
  intent → intermediate representation (plan) → output (sections) → optimization passes (verification).
  Building this engine is the ONLY path that serves both Scale 2 and Scale 3 — everything else is a
  stopgap. The existing three-phase architecture (exploration → registry → synthesis) already
  demonstrates the right pattern; the engine externalizes and generalizes it.
  BEST CONDITIONS: When you're ready to invest in infrastructure that serves ALL scales, want a
  principled architecture rather than ad-hoc coordination, and have the engineering capacity to build
  software (not just prompts).
  IDEAL OUTCOME: A long-form generation engine that accepts intent, produces a hierarchical plan,
  generates sections by calling existing skills, maintains state across calls, and runs verification
  passes — producing coherent documents at any scale the state system can handle.
  SOURCE SUPPORT: R7 (software engineering needed), R39 (engine not skill), R55 (exceeds SKILL.md
  capability), R63 (compiler structure), R61 (statefulness required), R38 (skills as micro-generators).

[PLAN-3] STEELMAN:
  STRONGEST CASE: The analysis identifies contradiction (R43), structural collapse (R48), and drift
  (R41) as the primary failure modes at scale. All three are solved by the SAME mechanism: a persistent
  registry that tracks every claim, premise, and structural relationship across the entire document.
  R45 explicitly identifies the three-phase registry architecture already built as the right pattern —
  it just needs to be externalized. This is the highest-leverage single component: it enables
  consistency checking, drift detection, contradiction detection, and structural coherence verification.
  Without it, every other plan degrades at scale.
  BEST CONDITIONS: When you want the single component that has the most cross-cutting impact on
  long-form quality. When you believe state management is the real bottleneck (R4).
  IDEAL OUTCOME: A persistent store (file-based or SQLite) that accumulates claims, premises, section
  dependencies, and structural relationships as a document is generated — queryable by any skill or
  engine component at any point during generation or verification.
  SOURCE SUPPORT: R44 (claim registry for contradiction), R45 (existing architecture is right pattern),
  R50 (document dependency graph), R60 (persistent registry spanning sessions), R4 (state management
  is the bottleneck).

[PLAN-4] STEELMAN:
  STRONGEST CASE: Without automated quality metrics, you can't tell whether a 100-page document is
  coherent without reading it yourself — which defeats the purpose of generation. R13 makes automated
  verification necessary, not optional. R14 identifies that this is closer to code review than writing —
  a well-defined problem with known solutions. The four metrics (consistency, drift, repetition,
  structural coherence from R57) are all measurable with LLM-based evaluation. A /verify_long_form
  skill could run post-generation and produce an actionable quality report, flagging specific sections
  that need revision. This makes the correction loop (R25) practical rather than blind.
  BEST CONDITIONS: When you're generating documents too long to manually review. When you want the
  correction loop (generate-verify-revise) to be automated rather than manual.
  IDEAL OUTCOME: A skill that takes a document + its plan, scores it on 4 dimensions, and outputs
  specific section-level flags ("Section 7 contradicts Section 3 on claim X", "Sections 12-15 drift
  from plan chapter 4").
  SOURCE SUPPORT: R13 (automated verification needed), R14 (closer to code review), R15 (specific
  skill needed), R57 (four metrics), R58 (implementable as skill), R25 (correction loop required).

[PLAN-5] STEELMAN:
  STRONGEST CASE: If long-form generation is the goal, then the project's identity must match its
  capability. R16 forecloses the toolkit remaining "just skills." R8 identifies the category shift as
  necessary: from "collection of Claude Code skills" to "agent framework for long-form generation."
  The current framing ("207 thinking skills") undersells what the project would become and attracts
  the wrong users (R18 — thinkers vs. producers). Repositioning aligns marketing with capability,
  attracts the users who actually need long-form output (writers, researchers, analysts), and
  creates a defensible niche rather than competing with every other "AI thinking tool."
  BEST CONDITIONS: When the long-form capability actually works and you're ready to attract users
  who need it. When the old framing is actively limiting growth.
  IDEAL OUTCOME: A clear project identity as "the tool that produces coherent long-form documents
  using structured reasoning" — distinct from both writing assistants (which don't reason) and
  thinking tools (which don't produce long output).
  SOURCE SUPPORT: R8 (project changes category), R16 (foreclosed: remains "just skills"), R17
  (current framing becomes secondary), R18 (user base shifts), R31 (competing with different tools).

[PLAN-6] STEELMAN:
  STRONGEST CASE: If the goal is tens of thousands of pages, then Scale 3 is the actual destination —
  everything else is a waypoint. R27 identifies this as a fundamentally different engineering problem.
  R28-R29 point to the right prior art: compiler design, database systems, version control — not
  writing tools. Building for Scale 3 from the start avoids the trap of building Scale 2 solutions
  that must be thrown away. R30 acknowledges no human writes this much solo either, which means the
  architecture must be multi-session, persistent, and probably multi-agent (R32). Going straight to
  Scale 3 is the most ambitious but also the only plan that addresses the full stated need ("tens of
  thousands of pages").
  BEST CONDITIONS: When you have significant engineering resources, a long time horizon, and the
  ambition to build something unprecedented. When the 10-100 page range is genuinely too small for
  your use cases.
  IDEAL OUTCOME: A multi-session, multi-agent document generation system that manages thousands of
  pages with consistency, producing output at the scale of technical documentation suites or
  encyclopedias.
  SOURCE SUPPORT: R27 (fundamentally different architecture), R28 (closer to codebases than books),
  R29 (prior art is compilers/DB/VCS), R30 (no human does this solo), R32 (must be multi-session,
  persistent, multi-agent).
```

### Step 5: Evaluate Against Source Evidence

```
[PLAN-1] EVALUATION:
  SUPPORTING EVIDENCE: R20 (Scale 1 works — BEDROCK), R22 (plan-then-execute achievable), R23 (minimum
  viable long-form, buildable with current tools — BEDROCK-TEST), R36 (components work), R42 (re-anchoring
  counters drift — BEDROCK-TEST), R47 (summary index counters repetition — BEDROCK-TEST)
  OPPOSING EVIDENCE: R24 (quality degrades with distance from plan), R26 (3x compute cost — BEDROCK-LOGIC),
  R34 (quality degrades superlinearly — necessary), R35 (naive scaling inference is wrong — BEDROCK-TENSION)
  EVIDENCE BALANCE: Supporting side is stronger for the limited scope (10-100 pages). Opposing evidence
  is real but describes problems that countermeasures (R42, R47) address. R35 is the strongest opposing
  item but R36 resolves it: components work, composition is the gap.
  CRITICAL DEPENDENCY: R22 — that plan-then-execute actually produces coherent output. Untested (marked
  BEDROCK-TEST, meaning it NEEDS testing).
  FAILURE MODE: Quality degrades enough at 50-100 pages that the output requires so much manual revision
  it's not worth generating. The countermeasures (re-anchoring, summary index) are insufficient. Predicted
  by R24, R34.

[PLAN-2] EVALUATION:
  SUPPORTING EVIDENCE: R7 (software engineering needed — necessary), R39 (engine not skill — BEDROCK-TEST),
  R55 (exceeds SKILL.md — BEDROCK-LOGIC), R63 (compiler structure — BEDROCK-LOGIC), R61 (statefulness
  required — BEDROCK-OBSERVE), R38 (skills as micro-generators)
  OPPOSING EVIDENCE: R23 (Scale 2 is buildable with CURRENT tools — suggesting engine may be premature
  for Scale 2), R39 itself is only BEDROCK-TEST (untested whether engine works)
  EVIDENCE BALANCE: Strongly supporting. Four independent branches converge. The opposing evidence
  doesn't say the engine is wrong — only that it might not be needed YET for Scale 2.
  CRITICAL DEPENDENCY: R55 — this requires writing code. The project must cross from prompt engineering
  to software engineering. This is a capability/commitment dependency, not just a technical one.
  FAILURE MODE: Overengineering. Building the engine takes so long that no long-form output is produced
  for months, while PLAN-1 could have delivered value sooner. The engine is architecturally sound but
  never ships.

[PLAN-3] EVALUATION:
  SUPPORTING EVIDENCE: R44 (claim registry for contradiction), R45 (existing architecture is right —
  BEDROCK-TENSION), R4 (state management is bottleneck — necessary), R60 (persistent registry spans
  sessions)
  OPPOSING EVIDENCE: R50 (document dependency graph — marked probable, untested), R51 (building the
  graph is the hard problem — BEDROCK-TEST, untested)
  EVIDENCE BALANCE: Supporting evidence is strong (R4 is necessary, R45 identifies existing pattern).
  Opposing evidence is about difficulty, not wrongness — the registry is the right thing, the question
  is whether it's manageable.
  CRITICAL DEPENDENCY: R51 — whether the document graph is manageable at 100+ page scale. Untested.
  FAILURE MODE: The registry becomes too complex to maintain at scale. The graph grows faster than it
  can be queried efficiently. Adding claims is cheap; finding contradictions among thousands of claims
  is expensive.

[PLAN-4] EVALUATION:
  SUPPORTING EVIDENCE: R13 (automated verification needed — necessary), R14 (closer to code review),
  R15 (specific skill needed — BEDROCK-TEST), R57 (four measurable metrics), R25 (correction loop
  needed — necessary)
  OPPOSING EVIDENCE: R58 is only BEDROCK-TEST (implementable as skill — untested). No source item
  argues AGAINST verification; the risk is in execution, not concept.
  EVIDENCE BALANCE: Strongly supporting. Verification is marked necessary (R12, R13), and the failure
  modes it addresses (R41, R43, R46, R48) are all marked necessary. Opposition is about feasibility,
  not direction.
  CRITICAL DEPENDENCY: R58 — whether automated metrics produce actionable scores. An LLM checking its
  own output may not catch its own systematic blind spots.
  FAILURE MODE: Metrics are too coarse ("this document scores 0.7 on consistency") or too noisy
  (flagging false positives) to be actionable. The correction loop runs but doesn't improve quality.

[PLAN-5] EVALUATION:
  SUPPORTING EVIDENCE: R8 (project changes category — BEDROCK-OBSERVE), R16 (foreclosed: remains just
  skills — necessary), R17 (current framing secondary — probable)
  OPPOSING EVIDENCE: R18 (user base shifts — BEDROCK-OBSERVE: notes these are DIFFERENT audiences,
  meaning repositioning may lose the existing user base), R31 (competing with collaborative document
  systems — different competitive landscape, much harder to win)
  EVIDENCE BALANCE: Mixed. The analysis says repositioning is necessary IF long-form is the goal. But
  it also notes the audiences are different (R18) and the competitive landscape shifts unfavorably (R31).
  CRITICAL DEPENDENCY: That long-form capability actually works before repositioning. Repositioning
  without capability is empty.
  FAILURE MODE: Repositioning alienates the existing user base (people who use the 207 skills for
  thinking) before the long-form capability is mature enough to attract new users. Caught between
  two identities.

[PLAN-6] EVALUATION:
  SUPPORTING EVIDENCE: R27 (fundamentally different architecture — necessary), R28 (closer to codebases),
  R29 (prior art in compilers/DB/VCS — BEDROCK-TEST), R30 (no human writes this solo — necessary)
  OPPOSING EVIDENCE: R32 (FORECLOSED: single-user single-session — BEDROCK-LOGIC, meaning the architecture
  must be multi-agent), R30 (no human does this — implying the DEMAND for this may be niche), R29 itself
  is BEDROCK-TEST (prior art needs investigation), R23 (Scale 2 is the minimum viable — suggesting Scale 3
  can wait)
  EVIDENCE BALANCE: The analysis strongly supports that Scale 3 IS different, but doesn't provide evidence
  that Scale 3 should be built NOW. Multiple items (R23, and the synthesis "minimum viable next step")
  point to Scale 2 first.
  CRITICAL DEPENDENCY: R29 — what prior art exists. This is unresolved in the source analysis.
  FAILURE MODE: Building for a scale nobody actually needs yet. Years of engineering before any usable
  output. The "tens of thousands of pages" use case may not exist for a solo developer's tool.
```

---

## Phase 2: PLAN REGISTRY

```
PLAN REGISTRY
=============

SOURCE: /ar on "Long-form writing scaling for reasoningtool" at depth 4x
PLANS EXTRACTED: 6

[PLAN-1] Build Scale 2 (10-100 pages) using plan-then-execute with existing tools
  STEELMAN: Simplest path to long-form. Components already work. Plan-then-execute + drift
  countermeasures + summary index = working 50-page documents with current tools.
  STRENGTHS: Buildable now (R23), leverages proven components (R20, R36), specific countermeasures
  identified (R42, R47)
  WEAKNESSES: Quality degradation is real and may overwhelm countermeasures (R24, R34), 3x compute
  cost (R26), untested at this scale (R23 is BEDROCK-TEST)
  RISKS: The 50-page test fails — quality degrades enough to make output unusable without heavy
  manual revision. Countermeasures prove insufficient.
  DEPENDENCIES: R22 must hold — plan-then-execute must actually produce coherent multi-section output.
  REVERSIBILITY: Easy to undo. This is a prototype test. If it fails, you've learned what doesn't
  work with minimal investment.
  COST: Low — uses existing tools. Main cost is time to set up the pipeline and run the test.
  Plus 3x compute for correction loops.
  GIVES UP: Architectural elegance. If this works "well enough," it may prevent building the proper
  engine (PLAN-2) because the hack is good enough. Technical debt from the start.
  FIRST ACTIONS: (1) Pick a specific 50-page document to generate. (2) Use /uaua to generate a
  detailed plan/outline. (3) Generate section-by-section with re-anchoring every 10 pages. (4)
  Measure coherence at pages 10, 25, 50. (5) Compare with and without countermeasures.

[PLAN-2] Build a stateful orchestration engine that calls skills as subroutines
  STEELMAN: Four independent analysis branches converge: this requires an engine, not a skill. The
  compiler analogy is structurally exact. This is the only plan that serves all scales.
  STRENGTHS: Strongest convergent evidence in the source (R7, R39, R55, R63), serves all scales,
  principled architecture, compiler analogy provides proven design pattern
  WEAKNESSES: Major engineering effort (R62 marked probable), requires crossing from prompt engineering
  to software engineering (R55), risk of overengineering before validating the core thesis
  RISKS: Takes months to build. No long-form output during construction. Architecture is right but
  execution is too slow/complex. May be premature if Scale 2 is achievable without it.
  DEPENDENCIES: R55 — requires code, not just prompts. Engineering capacity must exist.
  REVERSIBILITY: Hard to undo. Significant engineering investment. If the architecture is wrong, the
  sunk cost is high. But the compiler pattern is well-understood, reducing architecture risk.
  COST: High — software engineering effort. Multiple components (planner, state manager, section
  generator, verifier). Testing infrastructure. Ongoing maintenance.
  GIVES UP: Speed to first result. While building the engine, PLAN-1 could have delivered working
  50-page documents. Also gives up the simplicity of "just skills" — permanently.
  FIRST ACTIONS: (1) Design the engine architecture (compiler: intent → plan → sections → verification).
  (2) Define the state model (what gets persisted, in what format). (3) Build the planner component
  first (it can use existing skills). (4) Test with a 20-page document before scaling.

[PLAN-3] Build a persistent cross-document claim registry
  STEELMAN: Single highest-leverage component. Solves contradiction, drift, and structural collapse
  simultaneously. The three-phase architecture already built is the right pattern — it just needs
  to be externalized.
  STRENGTHS: Addresses the identified bottleneck (R4 — state management), existing pattern to follow
  (R45), cross-cutting impact on all failure modes, enables verification (PLAN-4)
  WEAKNESSES: Graph complexity at scale (R51 — untested), may be expensive to query, unproven whether
  LLM-populated registries are accurate enough
  RISKS: The registry fills with low-quality claims that produce false contradiction signals. The
  graph becomes unmanageable above 100 pages (R51).
  DEPENDENCIES: R51 — document graph must be manageable at scale. R44 — claim registry must actually
  catch contradictions.
  REVERSIBILITY: Partial. The registry can be built incrementally. If it doesn't work at scale, the
  small-scale version is still useful.
  COST: Medium — needs a persistence layer (file or SQLite), claim extraction logic, query interface.
  Not as large as the full engine but not trivial.
  GIVES UP: Simplicity. Every generation step now has a side-effect (updating the registry). Debugging
  becomes harder when state is involved.
  FIRST ACTIONS: (1) Define the claim schema (what gets stored per claim). (2) Build extraction:
  given a generated section, extract claims. (3) Build contradiction check: given a new claim, check
  against existing claims. (4) Test on a 20-page document — does it catch real contradictions?

[PLAN-4] Build a /verify_long_form skill with automated quality metrics
  STEELMAN: Without verification, you can't tell if a long document is coherent without reading it.
  The four metrics (consistency, drift, repetition, structural coherence) are measurable. This makes
  the correction loop practical rather than blind.
  STRENGTHS: Verification is marked necessary (R12, R13), well-defined metrics (R57), enables the
  correction loop (R25), can be built as a standalone skill
  WEAKNESSES: LLM checking its own output may miss systematic blind spots (R58 untested), metrics
  may be too coarse or too noisy, correction loop multiplies compute (R26)
  RISKS: Metrics sound good on paper but produce scores that don't correlate with human quality
  judgment. The verification skill says "looks good" on bad documents.
  DEPENDENCIES: R58 — whether automated metrics are actionable. May also depend on PLAN-3 (registry)
  for contradiction checking.
  REVERSIBILITY: Easy to undo. It's a standalone skill. If it doesn't work, remove it.
  COST: Medium — one skill to build, but requires careful design of metrics and testing against
  human judgment.
  GIVES UP: Nothing significant. This is purely additive.
  FIRST ACTIONS: (1) Build the consistency metric first (R58 suggests starting with one). (2) Generate
  a 20-page test document with intentional contradictions and drift. (3) Run the metric and measure
  detection rate. (4) Add remaining metrics if the first one works.

[PLAN-5] Reposition the project from "skill collection" to "long-form generation framework"
  STEELMAN: If long-form is the goal, identity must match capability. "207 thinking skills" undersells
  the vision and attracts users who don't need long-form. Repositioning creates a defensible niche.
  STRENGTHS: Foreclosure analysis (R16) says this is necessary, creates clearer value proposition,
  aligns marketing with direction
  WEAKNESSES: Loses existing audience (R18 — different users), enters harder competitive landscape
  (R31 — collaborative document systems), premature if capability isn't proven yet
  RISKS: Alienates existing users before attracting new ones. Repositioning without working long-form
  capability is empty marketing. The "agent framework" label may scare off non-technical users.
  DEPENDENCIES: Long-form capability must actually work before repositioning is credible.
  REVERSIBILITY: Hard to undo. Brand repositioning is a one-way door. Users who leave during the
  transition may not come back.
  COST: Medium — requires rewriting documentation, README, messaging, possibly subreddit. Opportunity
  cost of losing short-form positioning.
  GIVES UP: The "207 thinking skills" identity. The short-form user base. The simplicity of "copy
  skills into your project."
  FIRST ACTIONS: (1) Do NOT start here. Build capability first. (2) When capability is proven, draft
  new positioning. (3) Test with a small audience before full rebrand. (4) Keep existing skills
  available — don't break anything for current users.

[PLAN-6] Target Scale 3 (100-10,000+ pages) with multi-session, multi-agent architecture
  STEELMAN: Tens of thousands of pages is the stated goal. Building for Scale 3 from the start avoids
  throwaway Scale 2 solutions. The prior art (compilers, databases, VCS) provides proven patterns.
  STRENGTHS: Addresses the full stated need, prior art exists (R29), forces the right architecture
  from the start
  WEAKNESSES: No evidence Scale 3 demand exists (R30 — no human does this solo), prior art is
  uninvestigated (R29 — BEDROCK-TEST), massive engineering effort, source analysis itself says
  Scale 2 is the minimum viable step (R23)
  RISKS: Years of engineering with no output. Building for a use case that doesn't exist. The
  multi-agent architecture is harder than expected and never ships.
  DEPENDENCIES: R29 — prior art must be investigated. Engineering resources must be substantial.
  REVERSIBILITY: One-way door. Multi-year commitment. If the architecture is wrong, the investment
  is lost.
  COST: Very high — multi-session infrastructure, multi-agent coordination, persistent storage at
  scale, testing infrastructure for huge documents. Likely months to years of engineering.
  GIVES UP: Everything else. While building Scale 3, no Scale 2 capability ships. No incremental
  value. No user feedback until the system works end-to-end.
  FIRST ACTIONS: (1) Investigate prior art (R29). (2) Define the Scale 3 architecture on paper.
  (3) Identify the components that can be prototyped at Scale 2 without throwaway work. (4) Build
  those components first.

COMPARISON TABLE:
| Plan | Strengths | Weaknesses | Reversible? | Cost | Gives Up |
|------|-----------|------------|-------------|------|----------|
| PLAN-1: Scale 2 prototype | Buildable now, low risk | Untested, possible quality degradation | Yes | Low | Architectural elegance, may create debt |
| PLAN-2: Orchestration engine | Strongest convergence (4 branches), serves all scales | Major eng effort, may be premature | No | High | Speed to first result, simplicity |
| PLAN-3: Claim registry | Highest-leverage single component, existing pattern | Complexity at scale untested | Partial | Medium | Simplicity (adds stateful side-effects) |
| PLAN-4: Verification skill | Necessary per source, standalone | Metrics may not be actionable | Yes | Medium | Nothing significant |
| PLAN-5: Reposition project | Aligns identity with capability | Loses existing audience, premature risk | No | Medium | Existing identity and user base |
| PLAN-6: Scale 3 full build | Addresses full stated need | Massive effort, unproven demand | No | Very High | Everything else while building |

PLAN INTERACTIONS:
- PLAN-1 and PLAN-2: Sequential — PLAN-1 validates assumptions PLAN-2 builds on. Compatible.
- PLAN-1 enables PLAN-4: The prototype from PLAN-1 provides test documents for PLAN-4's metrics.
- PLAN-2 depends on PLAN-3: The engine needs a state system; the claim registry IS the state system.
- PLAN-3 enables PLAN-2 and PLAN-4: Registry is a prerequisite for both the engine and verification.
- PLAN-4 enables PLAN-1 (correction loop): Without verification, PLAN-1's correction loop is blind.
- PLAN-5 depends on PLAN-1 or PLAN-2: Repositioning without capability is empty.
- PLAN-6 depends on PLAN-2: Scale 3 requires the engine. PLAN-6 is PLAN-2 taken to its conclusion.
- PLAN-1 and PLAN-6: Incompatible as simultaneous efforts. Sequential is fine (PLAN-1 first).
- PLAN-2 and PLAN-6: PLAN-2 is a subset of PLAN-6. Building PLAN-2 is a step toward PLAN-6.
```

---

## Phase 3: RECOMMENDATION SYNTHESIS

**[PLAN-1] RECOMMENDED** — Build Scale 2 (10-100 pages) using plan-then-execute with existing tools
```
DERIVATION CHAIN:
  R20 shows Scale 1 (1-10 pages) works now (BEDROCK-OBSERVE)
  R36 shows components work; composition architecture is missing
  R23 identifies Scale 2 as minimum viable long-form, buildable with current tools (BEDROCK-TEST)
  R22 identifies plan-then-execute as achievable for this scale
  -> Components are proven; only the composition pattern is untested
  -> The cheapest way to test composition is to try it at Scale 2
  -> Therefore: build the prototype and measure what happens
USE IF: You want to validate the long-form thesis before committing to engine architecture.
  You have a specific document (50+ pages) you want to produce. You want results within
  days, not months.
DON'T USE IF: You already know Scale 2 works (evidence from prior attempts) and need to
  jump straight to the engine. You have no specific document to produce (the test needs a
  real use case, not a toy example).
FIRST ACTIONS:
  1. Pick a real 50-page document to generate — resolves the need for a concrete test case
  2. Run /uaua on the document topic to generate a detailed plan — resolves the plan dependency (R9)
  3. Generate sections referencing plan + prior sections, re-anchoring every 10 pages — tests R22, R42
  4. Measure coherence at pages 10, 25, 50 with and without countermeasures — tests R24, R42, R47
```

**[PLAN-4] RECOMMENDED** — Build a /verify_long_form skill with automated quality metrics
```
DERIVATION CHAIN:
  R12 and R13 establish automated verification as necessary (not optional)
  R25 establishes correction loops as necessary
  R57 identifies four specific measurable metrics
  R58 identifies this as implementable as a skill (BEDROCK-TEST)
  -> Verification is necessary regardless of which scale you target
  -> Without it, correction loops are blind
  -> A standalone skill is low-cost and low-risk
  -> Therefore: build it, starting with the consistency metric
USE IF: You are doing any long-form generation at all (Scale 2 or above). This is the
  first thing to validate because every other plan's correction loop depends on it.
DON'T USE IF: You are only doing 1-10 page outputs where manual review is feasible.
FIRST ACTIONS:
  1. Build the consistency metric (do claims contradict?) — resolves R58's test
  2. Create a 20-page test doc with intentional contradictions — provides ground truth
  3. Measure detection rate — validates whether LLM-based verification works at all
  4. Add drift, repetition, structural coherence metrics if consistency works — builds incrementally
```

**[PLAN-3] CONDITIONALLY RECOMMENDED** — Build a persistent cross-document claim registry
```
DERIVATION CHAIN:
  R4 identifies state management as the bottleneck (necessary)
  R45 identifies the existing registry architecture as the right pattern (BEDROCK-TENSION)
  R44 identifies claim registries as contradiction detectors
  R50, R51 identify the document graph as the key data structure but mark it untested
  -> The registry is the right idea (strong source support)
  -> But manageability at scale is unproven (R51)
  -> Therefore: build it IF Scale 2 prototype (PLAN-1) reveals state management as the binding constraint
CONDITION: PLAN-1's prototype reveals that state management (not generation quality) is the bottleneck.
  Specifically: if the 50-page test shows contradictions or structural collapse that a registry would catch.
HOW TO CHECK: Run PLAN-1's prototype. If the main quality problems are contradictions between sections
  or structural collapse, the registry is needed. If the main problems are per-section quality, the
  registry won't help.
USE IF: PLAN-1 produces contradictions between sections or structural breakdown. You're planning to
  build PLAN-2 (engine) and need a state system for it.
DON'T USE IF: PLAN-1's main quality problems are within sections (per-page quality), not between
  sections (cross-page consistency). In that case, focus on improving per-section generation first.
IF CONDITION UNKNOWN: Run PLAN-1 first. The prototype will reveal the failure modes.
FIRST ACTIONS:
  1. Define claim schema — resolves "what gets stored"
  2. Build extraction from generated sections — resolves "how claims enter the registry"
  3. Build contradiction checker — resolves "how the registry is used"
  4. Test on PLAN-1's prototype output — resolves "does it catch real problems"
```

**[PLAN-2] CONDITIONALLY RECOMMENDED** — Build a stateful orchestration engine that calls skills as subroutines
```
DERIVATION CHAIN:
  R7, R39, R55, R63 converge from four independent branches: an engine is needed (strongest convergence
  in the source analysis)
  R55 establishes this exceeds SKILL.md capability (BEDROCK-LOGIC)
  R63 identifies the compiler pattern as structurally exact (BEDROCK-LOGIC)
  -> The analysis is clear that an engine is the right architecture
  -> But R23 says Scale 2 is buildable with current tools
  -> Therefore: build the engine IF PLAN-1 validates the core thesis but hits limits that only an engine solves
CONDITION: PLAN-1 succeeds well enough to validate long-form output is valuable, but hits
  coordination limits that can't be solved with ad-hoc scripting.
HOW TO CHECK: After running PLAN-1, ask: "Could I generate a 100-page document by extending this
  approach?" If the answer is "yes, but the coordination overhead is unsustainable," the engine is
  needed. If "no, the per-section quality is the problem," the engine won't help.
USE IF: PLAN-1 validates the concept but coordination becomes the bottleneck. You have engineering
  capacity for a multi-week build. You want to target Scale 2+ sustainably.
DON'T USE IF: PLAN-1 fails at the component level (per-section quality is the problem, not
  orchestration). You need long-form output within days, not weeks.
IF CONDITION UNKNOWN: Run PLAN-1. Use its results to decide.
FIRST ACTIONS:
  1. Design the compiler pipeline: intent → plan → sections → verification — resolves architecture
  2. Define the state model (incorporating PLAN-3's registry) — resolves persistence
  3. Build the planner component using existing skills — resolves the easiest piece first
  4. Test end-to-end on a 20-page document — validates before scaling
```

**[PLAN-5] NOT RECOMMENDED** — Reposition the project from "skill collection" to "long-form generation framework"
```
STEELMAN REMINDER: If long-form is the goal, identity must match capability. "207 thinking skills"
  undersells the vision and attracts users who don't need long-form. Repositioning creates a
  defensible niche.
DERIVATION CHAIN:
  R16 says the toolkit can't remain "just skills" (foreclosure — necessary)
  R8 says the project changes category (BEDROCK-OBSERVE)
  R18 says the user base shifts (BEDROCK-OBSERVE) — but notes these are DIFFERENT audiences
  R31 says the competitive landscape shifts to collaborative document systems
  -> Repositioning IS necessary eventually
  -> But R18 explicitly notes different audiences — repositioning risks losing the current one
  -> No source item provides evidence that long-form capability works yet
  -> Therefore: repositioning now is premature. Capability must precede identity change.
WHY IT FAILS: R18 identifies the audiences as different (BEDROCK-OBSERVE). Repositioning before
  capability is proven means losing the existing audience (thinkers) without gaining the new one
  (producers). R31 shifts the competitive landscape to collaborative document systems — a much
  harder market. Nothing in the source analysis shows the long-form capability works yet.
WHAT WOULD CHANGE THIS VERDICT: PLAN-1 or PLAN-2 delivers a working long-form capability that
  users actually want. Evidence that the existing user base WANTS long-form. Evidence that the
  "thinking skills" positioning is actively limiting growth.
USE INSTEAD: Build capability first (PLAN-1 → PLAN-2). Repositioning is a consequence of success,
  not a prerequisite for it.
```

**[PLAN-6] NOT RECOMMENDED** — Target Scale 3 (100-10,000+ pages) with multi-session, multi-agent architecture
```
STEELMAN REMINDER: Tens of thousands of pages is the stated goal. Building for Scale 3 from the
  start avoids throwaway Scale 2 solutions. The prior art (compilers, databases, VCS) provides
  proven patterns at this scale.
DERIVATION CHAIN:
  R27 says Scale 3 is fundamentally different (necessary)
  R30 says no human writes 10,000 pages solo (necessary)
  R32 forecloses single-session architecture for Scale 3 (BEDROCK-LOGIC)
  R23 says Scale 2 is the minimum viable next step (BEDROCK-TEST)
  R29 says prior art needs investigation (BEDROCK-TEST — meaning it's unresearched)
  -> Scale 3 is real and different, but:
  -> No evidence that demand for 10,000-page single-author generation exists (R30)
  -> Prior art is uninvestigated (R29)
  -> The source analysis itself recommends Scale 2 first (R23)
  -> Therefore: targeting Scale 3 now skips necessary validation steps
WHY IT FAILS: The source analysis's own synthesis identifies Scale 2 as "minimum viable next step"
  (R23). R30 notes no human writes this much solo — raising the question of whether this use case
  exists for a solo developer's tool. R29 marks prior art as needing investigation (BEDROCK-TEST) —
  meaning the foundational research hasn't been done. Building for Scale 3 without validating Scale 2
  and without investigating prior art is building blind.
WHAT WOULD CHANGE THIS VERDICT: (1) PLAN-1 succeeds at Scale 2 and reveals that the same approach
  cannot extend to Scale 3 (confirming R27). (2) Investigation of prior art (R29) reveals tractable
  architecture. (3) A concrete use case for 10,000+ page generation is identified. All three would
  upgrade this to CONDITIONALLY RECOMMENDED.
USE INSTEAD: PLAN-1 (validate Scale 2), then PLAN-2 (build engine with Scale 3 in mind). Design
  PLAN-2's architecture to NOT preclude Scale 3, but don't build for it yet.
```

---

```
RECOMMENDATION SUMMARY
======================

SOURCE: /ar on "Long-form writing scaling for reasoningtool"

RECOMMENDED:
- PLAN-1: Build Scale 2 prototype (plan-then-execute, 50 pages) -- USE IF: You want to validate the
  long-form thesis before committing to heavy engineering
- PLAN-4: Build /verify_long_form skill -- USE IF: You are doing any long-form generation at all

CONDITIONALLY RECOMMENDED:
- PLAN-3: Persistent claim registry -- CONDITION: PLAN-1 reveals cross-section consistency as the
  binding constraint
- PLAN-2: Orchestration engine -- CONDITION: PLAN-1 validates the concept but hits coordination limits

NOT RECOMMENDED:
- PLAN-5: Reposition project -- BECAUSE: Capability must precede identity change; audiences are different
  (R18); competitive landscape shifts unfavorably (R31)
  WOULD CHANGE IF: Working long-form capability + evidence existing users want it
- PLAN-6: Target Scale 3 directly -- BECAUSE: Source analysis itself says Scale 2 first (R23); prior art
  uninvestigated (R29); no evidence demand exists (R30)
  WOULD CHANGE IF: Scale 2 validated + prior art investigated + concrete 10K-page use case identified

SUGGESTED SEQUENCE:
1. PLAN-4: Build consistency metric first (standalone, low risk, needed by everything else)
2. PLAN-1: Run the 50-page prototype with /uaua planning + re-anchoring + verification from PLAN-4
3. Evaluate: What failed? Cross-section consistency (→ PLAN-3) or coordination limits (→ PLAN-2)?
4. PLAN-3 or PLAN-2 based on what the prototype reveals
5. PLAN-5 only after capability is proven and demanded
6. PLAN-6 only after Scale 2 is validated and prior art is investigated

WHAT THIS ANALYSIS DOES NOT COVER:
- Whether the user actually needs long-form output (the source analysis assumes the goal; /propose
  doesn't question goals)
- The specific engineering design of any component (architecture decisions within each plan)
- Cost in dollars for compute (R26 says 3x minimum but doesn't estimate actual API costs)
- Timeline (how long any of this takes to build)
- Whether there are approaches the /ar analysis missed entirely (this analysis is bounded by its source)
```
