# /diagnose Why do some skill chains work smoothly while others feel disjointed?
**Date:** 2026-03-09
**Skill:** /diagnose (Find the Cause)

---

## Routing

**Input**: "Why do some skill chains (invocations calling other skills) work smoothly while others feel disjointed?"

**Context**: Skills can chain via `→ INVOKE: /procedure_name [args]`. Some compound skills (like `/dcp` which chains `/dd → /se → /aex → /stg → /fla → /pv`) work well. Others feel like disconnected steps.

### Routing Decisions

1. **Symptom**: Some skill chains produce cohesive, cumulative output where each step builds on the last. Others produce output that reads like six unrelated analyses pasted together.

2. **Is this diagnostic?** Yes — this is genuinely asking "what causes the quality difference between chains?"

3. **Cause known?** Unknown — multiple hypotheses exist but the root cause is unclear.

4. **Technical or non-technical?** Non-technical — this is about information architecture, not code.

5. **Timeline?** No clear timeline — the problem is structural, not event-triggered.

6. **Recurring?** Yes — this manifests every time certain chains are invoked.

7. **Isolated or systemic?** Systemic — the pattern appears across multiple chains.

**Route selected**: /uaua [symptom] — explore the space of possible causes, then test each.

---

## Phase 1: EXPLORATION

### U0: Ground in Exemplars

**What does a smooth chain look like?**

The best exemplar is `/dcp` (Decision Procedure): `/dd → /se → /aex → /stg → /fla → /pv`.

Why this works:
- Each step has a **named, typed output** that the next step explicitly consumes
- `/dd` produces dimensions → `/se` takes those dimensions as input
- `/se` produces an option space → `/aex` examines assumptions about the standard approach within that space
- `/aex` produces assumptions → `/stg` generates a procedure that accounts for them
- `/stg` produces a procedure → `/fla` stress-tests that procedure
- `/fla` produces failure modes → `/pv` validates the final procedure including those failure modes

The felt impression: it reads like a manufacturing pipeline where raw material enters one end and a finished product exits the other. Every step transforms a specific artifact.

**What does a disjointed chain look like?**

Consider `/diagnose` itself when it routes to `/uaua` then suggests supplementary invocations like `/eth`, `/dys`, `/sycs`, `/ata`, `/tbd`. Or consider when `/decide` routes to a chain where one skill produces a broad exploration and the next skill starts fresh with a different framing.

The felt impression: it reads like being handed off between departments that don't share notes.

**What they share**: Both use the `→ INVOKE` pattern.

**What they differ on**: The smooth chains have explicit data contracts between steps. The disjointed chains have implicit or missing contracts.

---

### U1: Map the Space

```
[U1] EXPLICIT: Some chains feel smooth and others feel disjointed
[U2] IMPLICIT: "Smooth" means the output reads as one integrated analysis, not N separate ones
[U3] PRESUPPOSED: Chain quality is a property of the chain DESIGN, not just execution variance
[U4] BUNDLED: "Disjointed" conflates several failure modes: redundancy, context loss, tonal shift, lack of accumulation
[U5] META: This question assumes chains should be smooth — maybe disjointedness is sometimes correct (parallel analyses that DON'T need to connect)
```

**Technique 1: STATE SPACE — What states can a chain be in?**

```
[U6] SMOOTH: Each step consumes the prior step's output and produces a transformed artifact
[U7] ADDITIVE: Each step adds new analysis alongside prior output (grows but doesn't transform)
[U8] DISJOINTED: Each step operates independently, producing separate outputs that don't reference each other
[U9] CONTRADICTORY: Steps produce conclusions that conflict with each other
[U10] REDUNDANT: Steps repeat work already done by prior steps
[U11] REFRAME: Maybe the question is wrong — the issue isn't smooth vs disjointed but "does the chain have a data contract between steps?"
```

**Technique 5: ASSUMPTION EXTRACTION — What must be true for smooth chains?**

```
[U12] LOAD-BEARING: Each skill must know what it receives from the prior skill — if false: the skill starts from scratch, ignoring prior context
[U13] LOAD-BEARING: The output format of skill N must be compatible with the input expectations of skill N+1 — if false: the next skill reinterprets or discards
[U14] LOAD-BEARING: The chain must have a single accumulating artifact — if false: each step produces a separate document
[U15] LOAD-BEARING: The LLM must carry forward context across invocations — if false: each skill is executed as if no prior work happened
[U16] BACKGROUND: The user understands the chain is multi-step and expects cumulative output
```

**Technique 2: INSTANCE-TO-CATEGORY — What is this an instance of?**

```
[U17] Chain coherence is an instance of PIPELINE DESIGN — same principles as ETL pipelines, manufacturing lines, and compiler passes
[U18] Sibling: Function composition in programming — f(g(x)) works when g's output type matches f's input type
[U19] Sibling: Assembly lines — smooth when each station transforms the same workpiece; disjointed when stations work on separate pieces
[U20] Sibling: Writing process — draft → edit → polish works because each stage modifies the SAME document
```

**Technique 4: PERSPECTIVE ROTATION — Who sees this differently?**

```
[U21] SKILL AUTHOR sees: "I designed each skill to be standalone and reusable"
[U22] CHAIN DESIGNER sees: "I need these skills to compose into a coherent sequence"
[U23] LLM EXECUTOR sees: "I receive instructions from each skill; I carry context in my context window"
[U24] END USER sees: "I invoked one command and got back something that reads like six different answers"
```

**Technique 6: DIMENSION DISCOVERY — What axes define chain quality?**

```
[U25] Dimension: DATA CONTRACT EXPLICITNESS — does the chain specify what artifact flows between steps? (explicit / implicit / absent)
[U26] Dimension: ACCUMULATION MODEL — does the chain transform one artifact or produce parallel artifacts? (transform / accumulate / parallel)
[U27] Dimension: CONTEXT DEPENDENCY — does each skill reference prior steps' output or start fresh? (references / ignores)
[U28] HIDDEN dimension: GRAIN SIZE MATCH — do adjacent skills operate at the same level of abstraction? (matched / mismatched)
[U29] HIDDEN dimension: SKILL SOVEREIGNTY — does each skill assume it "owns" the full response, or does it know it's part of a chain? (sovereign / chain-aware)
```

---

### A1: Test with ARAW

**Candidate [U12]: Each skill must know what it receives from the prior skill**

```
ASSUME RIGHT:
[F1] If right: Then smooth chains are ones where the SKILL.md explicitly says "receives [X] from prior step" — Necessary
  [F2] If F1 right: Then /dcp works because /dd says "produce dimensions" and /se says "prerequisites: dimensions identified" — Necessary
    [F3] → BEDROCK-OBSERVE: Reading /dd and /se, /dd's output is "DIMENSIONS DISCOVERED FOR: [domain]" and /se's first step is "Confirm Dimensions" with "Prerequisites: Dimensions identified (use /dd if unknown)"
  [F4] If F1 right: Disjointed chains are ones where no such contract exists — Probable
[F5] FORECLOSED if right: You cannot fix chain quality purely through LLM prompting — the skill files themselves must encode the contracts

ASSUME WRONG:
[F6] Wrong because: Some chains feel smooth even without explicit contracts — the LLM carries context naturally — Conditional
  [F7] If F6 holds: Then chain quality is primarily an LLM context management issue, not a skill design issue — Possible
    [F8] → BEDROCK-TEST: Test by running the same chain with and without explicit data contracts — does output quality differ?
  [F9] Alternative derived from F6: Chain quality might be about the FRAMING PARAGRAPH at the start of each skill, not about data contracts per se
[F10] Wrong because: Even with explicit contracts, if the skills are at mismatched abstraction levels, the chain feels disjointed — Serious
  [F11] If F10 holds: Grain size mismatch is the real cause, not contract absence — Probable
    [F12] → BEDROCK-OBSERVE: /dcp chains /dd (tactical: list dimensions) → /se (tactical: enumerate) → /aex (strategic: hidden assumptions) → /stg (tactical: generate steps) — all roughly same grain. Compare to /diagnose which jumps from routing (meta) to /uaua (deep strategic exploration) to /rca (tactical trace) — grain varies widely
```

**Candidate [U14]: The chain must have a single accumulating artifact**

```
ASSUME RIGHT:
[F13] If right: Smooth chains pass one artifact forward that gets progressively refined — Necessary
  [F14] If F13 right: /dcp works because the artifact is "the decision procedure" — dimensions → option space → assumption-aware procedure → failure-tested procedure → validated procedure — Necessary
    [F15] → BEDROCK-OBSERVE: /dcp's steps explicitly say "procedure from Step 4" in Step 5, "complete procedure from Steps 4-5" in Step 6 — one artifact accumulating
  [F16] FORECLOSED if right: Skills that produce multiple parallel artifacts (e.g., "here are 3 separate analyses") cannot form smooth chains

ASSUME WRONG:
[F17] Wrong because: Some chains produce separate analyses that integrate at the end — this can still feel smooth if the integration step is strong — Conditional
  [F18] If F17 holds: The integration step is what matters, not single-artifact accumulation — Possible
    [F19] → BEDROCK-TEST: Identify chains with integration-at-end pattern — do they feel smooth?
[F20] Wrong because: /uaua itself is a chain (U0→U1→A1→U2→A2→Registry→Synthesis) and it accumulates numbered findings, not a single artifact — yet it works — Serious
  [F21] → BEDROCK-OBSERVE: /uaua accumulates findings into a REGISTRY, then derives SYNTHESIS from the registry. The registry IS the single accumulating artifact — it just grows additively rather than transformatively.
```

**Candidate [U29]: Skill sovereignty — does each skill assume it owns the full response?**

```
ASSUME RIGHT:
[F22] If right: Skills designed as standalone tools (sovereign) fight for control of the output when chained — each tries to frame the problem, produce a complete answer, and conclude — Necessary
  [F23] If F22 right: This explains why chaining two sovereign skills feels like reading two separate essays — each has its own introduction, body, and conclusion — Probable
    [F24] → BEDROCK-OBSERVE: Compare /dd (has its own "Purpose", "The Process", "Quality Checklist") vs /stg (assumes it receives a COMPLETE_PLAN — chain-aware). /dd is semi-sovereign; /stg is chain-aware.
  [F25] FORECLOSED if right: You can't make skills both good standalone AND good in chains without explicit chain-mode behavior

ASSUME WRONG:
[F26] Wrong because: The LLM naturally suppresses the "standalone" framing when it knows a chain is happening — Conditional
  [F27] If F26 holds: Chain quality is about LLM behavior, not skill design — Possible
    [F28] But F27 requires the LLM to KNOW it's in a chain — how? The compound skill (like /dcp) tells it. Skills invoked by /diagnose's routing don't always make this clear.
    [F29] → BEDROCK-OBSERVE: /dcp's chain header says "This is a compound skill — it chains 6 skills in sequence." /diagnose's routing says "→ INVOKE: /uaua [symptom]" with no indication of chain context.
```

**Candidate [U28]: Grain size match — adjacent skills at same abstraction level**

```
ASSUME RIGHT:
[F30] If right: Chains feel smooth when adjacent skills operate at similar granularity — Necessary
  [F31] If F30 right: /dcp works because all 6 skills are "mid-level analysis" tools — Probable
  [F32] Disjointed example: /diagnose routes to /uaua (exhaustive deep exploration at 2x depth = 35+ findings) then suggests supplementary /ata (tactical "and then also") — massive grain mismatch — Probable
    [F33] → BEDROCK-OBSERVE: /uaua produces 35+ numbered findings at 2x depth. /ata is a quick tactical check. Running /ata after /uaua would feel like doing a deep ocean dive then checking the swimming pool.

ASSUME WRONG:
[F34] Wrong because: Grain mismatch might be perceptible but not the PRIMARY cause — the real issue is context loss — Conditional
  [F35] If F34 holds: Fixing grain size alone wouldn't fix the disjointedness — Possible
    [F36] → BEDROCK-TEST: Run a chain with matched grain but no data contract — is it still disjointed?
```

### Feedback Loop

A1 revealed a genuinely new candidate not in U1:

```
[U30] NEW CANDIDATE from F28-F29: CHAIN CONTEXT DECLARATION — whether the compound skill tells the LLM "you are in step N of M, here is what you've built so far" vs just saying "→ INVOKE: /skill"
[U31] NEW CANDIDATE from F21: ACCUMULATION PATTERN — whether findings accumulate in a structured container (registry, table, artifact) vs dissolving into prose that the next skill cannot easily reference
```

### U2: Edge Cases

```
[E1] Boundary: What about 2-step chains? — Even 2 steps can feel disjointed if the second skill doesn't reference the first's output (/diagnose → /rca where /rca starts fresh)
[E2] Scale failure: What about 10-step chains? — Even with perfect data contracts, very long chains accumulate context window pressure and drift. At some point the LLM "forgets" early steps.
[E3] Temporal limit: When does the data contract pattern stop working? — When the intermediate artifact becomes too large for the LLM to hold in working memory while executing the next step
[E4] Stakeholder conflict: Skill reusability vs chain optimization — making skills chain-aware reduces their standalone utility. /se works great independently AND in /dcp's chain because it was designed for both. Many skills only designed for standalone use.
[E5] Context dependency: Chains work differently depending on LLM model — larger context windows tolerate looser data contracts because they carry more prior context naturally
[E6] Rejected candidate works if: [U8] Parallel/disjointed output works if the user WANTS multiple independent analyses (e.g., "give me three different perspectives on X") — disjointedness is a feature
[E7] Boundary: What about chains where the intermediate skill SHOULD reset? — /diagnose → /claim is a valid redirect, not a chain. The disjointedness is appropriate because the diagnosis found "this isn't a diagnostic question."
```

### A2: Validate Edge Cases

```
[E1] "Even 2-step chains can feel disjointed"
  [F37] AR: True — /diagnose → /rca starts /rca from scratch with its own "Step 1: Define and scope the problem" even though /diagnose already did this — Necessary
    [F38] → BEDROCK-OBSERVE: /rca Step 1 says "Clearly articulate what problem you're analyzing" — it doesn't say "using the symptom identified by /diagnose"
  [F39] AW: Maybe the LLM just carries the context — Conditional
    [F40] The LLM DOES carry context, but /rca's instructions tell it to start fresh, creating a tension between carried context and skill instructions

[E4] "Skill reusability vs chain optimization"
  [F41] AR: This is a genuine tension — making /se say "consume dimensions from /dd" makes it less useful when invoked standalone — Probable
  [F42] AW: /se already handles this — its first step is "Confirm Dimensions" with a note "(use /dd if unknown)" — so it's chain-aware without being chain-dependent — Conditional
    [F43] → BEDROCK-OBSERVE: /se's prerequisite says "Dimensions identified (use /dd if unknown)" — this is the pattern. It works both ways. Not all skills do this.

[E2] "Very long chains accumulate drift"
  [F44] AR: At 6+ steps, the LLM's attention to early-chain artifacts degrades — Probable
  [F45] AW: /uaua manages this with explicit REGISTRY compilation — forcing re-summarization prevents drift — Serious
    [F46] → BEDROCK-OBSERVE: /uaua's Phase 2 says "After ALL exploration is complete, compile EVERY numbered item" — this is a deliberate drift-prevention mechanism. Chains without this mechanism are more susceptible.
```

---

## Phase 2: FINDING REGISTRY

```
FINDING REGISTRY
================

UNBUNDLED CLAIMS:
[U1] Some chains feel smooth and others feel disjointed -- TYPE: explicit
[U2] "Smooth" means output reads as one integrated analysis -- TYPE: implicit
[U3] Chain quality is a property of chain DESIGN -- TYPE: presupposed
[U4] "Disjointed" conflates redundancy, context loss, tonal shift, lack of accumulation -- TYPE: bundled
[U5] Maybe disjointedness is sometimes correct -- TYPE: meta

CANDIDATES (from U1 mapping):
[U6] SMOOTH: Each step consumes prior output and produces transformed artifact -- SOURCE: state space
[U7] ADDITIVE: Each step adds analysis alongside prior output -- SOURCE: state space
[U8] DISJOINTED: Each step operates independently -- SOURCE: state space
[U9] CONTRADICTORY: Steps produce conflicting conclusions -- SOURCE: state space
[U10] REDUNDANT: Steps repeat prior work -- SOURCE: state space
[U11] Reframe: issue is "does the chain have a data contract?" -- SOURCE: state space

ASSUMPTIONS:
[U12] Each skill must know what it receives -- LOAD-BEARING -- if false: skill starts from scratch
[U13] Output format of skill N must match input expectations of N+1 -- LOAD-BEARING -- if false: next skill reinterprets/discards
[U14] Chain must have single accumulating artifact -- LOAD-BEARING -- if false: separate documents
[U15] LLM must carry context across invocations -- LOAD-BEARING -- if false: each skill fresh
[U16] User expects cumulative output -- BACKGROUND

PERSPECTIVES:
[U17] Pipeline design analogy -- SOURCE: instance-to-category
[U18] Function composition analogy (type matching) -- SOURCE: instance-to-category
[U19] Assembly line analogy -- SOURCE: instance-to-category
[U20] Writing process analogy -- SOURCE: instance-to-category
[U21] Skill author: designed for standalone reuse -- SOURCE: perspective
[U22] Chain designer: needs composition -- SOURCE: perspective
[U23] LLM executor: carries context in window -- SOURCE: perspective
[U24] End user: wants one coherent answer -- SOURCE: perspective

DIMENSIONS:
[U25] Data contract explicitness (explicit/implicit/absent) -- DISCOVERED
[U26] Accumulation model (transform/accumulate/parallel) -- DISCOVERED
[U27] Context dependency (references/ignores) -- DISCOVERED
[U28] Grain size match (matched/mismatched) -- HIDDEN
[U29] Skill sovereignty (sovereign/chain-aware) -- HIDDEN

NEW CANDIDATES (from feedback loop):
[U30] Chain context declaration -- whether compound skill tells LLM "you are in step N of M"
[U31] Accumulation pattern -- whether findings accumulate in structured container vs dissolving into prose

AR FINDINGS:
[F1] Smooth chains have explicit "receives X" contracts -- STRENGTH: necessary -- PARENT: U12
[F2] /dcp works because /dd outputs dimensions and /se inputs dimensions -- STRENGTH: necessary -- PARENT: F1
[F3] BEDROCK-OBSERVE: /dd outputs "DIMENSIONS DISCOVERED" and /se says "Prerequisites: Dimensions identified" -- PARENT: F2
[F13] Smooth chains pass one artifact that gets refined -- STRENGTH: necessary -- PARENT: U14
[F14] /dcp's artifact is "the decision procedure" accumulating through 6 steps -- STRENGTH: necessary -- PARENT: F13
[F15] BEDROCK-OBSERVE: /dcp says "procedure from Step 4" in Step 5, "complete procedure from Steps 4-5" in Step 6 -- PARENT: F14
[F22] Sovereign skills fight for output control when chained -- STRENGTH: necessary -- PARENT: U29
[F23] Two sovereign skills read like two separate essays -- STRENGTH: probable -- PARENT: F22
[F30] Chains smooth when adjacent skills at similar granularity -- STRENGTH: necessary -- PARENT: U28
[F31] /dcp works because all 6 skills are mid-level analysis -- STRENGTH: probable -- PARENT: F30
[F37] 2-step chains disjointed when second skill starts from scratch -- STRENGTH: necessary -- PARENT: E1
[F41] Making skills chain-aware reduces standalone utility -- STRENGTH: probable -- PARENT: E4
[F42] /se handles both modes with "use /dd if unknown" -- STRENGTH: conditional -- PARENT: F41
[F44] 6+ step chains degrade attention to early artifacts -- STRENGTH: probable -- PARENT: E2
[F45] /uaua prevents drift with explicit REGISTRY compilation -- STRENGTH: serious (AW to drift) -- PARENT: E2

AW FINDINGS:
[F6] Some chains smooth even without explicit contracts (LLM carries context) -- SEVERITY: conditional -- PARENT: U12
[F10] Even with contracts, mismatched abstraction levels cause disjointedness -- SEVERITY: serious -- PARENT: U12
[F17] Parallel analyses with strong integration step can feel smooth -- SEVERITY: conditional -- PARENT: U14
[F20] /uaua accumulates findings not a single artifact — but works -- SEVERITY: serious -- PARENT: U14
[F26] LLM naturally suppresses standalone framing in chains -- SEVERITY: conditional -- PARENT: U29
[F34] Grain mismatch perceptible but maybe not primary cause -- SEVERITY: conditional -- PARENT: U28

FORECLOSURES:
[F5] Cannot fix chain quality purely through LLM prompting -- PARENT: U12
[F16] Skills producing parallel artifacts cannot form smooth chains (unless integration step) -- PARENT: U14
[F25] Cannot make skills both great standalone AND great in chains without explicit dual-mode design -- PARENT: U29

DERIVED ALTERNATIVES:
[F9] Quality might be about framing paragraph, not data contracts -- DERIVED FROM: F6
[F11] Grain size mismatch might be real cause, not contract absence -- DERIVED FROM: F10
[F18] Integration step might matter more than single-artifact accumulation -- DERIVED FROM: F17
[F21] Registry/structured container IS the single artifact (additive, not transformative) -- DERIVED FROM: F20

EDGE CASES:
[E1] 2-step chains can still be disjointed -- TYPE: boundary
[E2] 10+ step chains accumulate drift regardless -- TYPE: scale
[E3] Intermediate artifacts too large for LLM working memory -- TYPE: scale
[E4] Reusability vs chain optimization tension -- TYPE: stakeholder conflict
[E5] Model-dependent (larger context = more tolerance) -- TYPE: context dependency
[E6] Disjointedness appropriate when user wants parallel analyses -- TYPE: boundary
[E7] Routing redirects (not chains) appropriately feel disjointed -- TYPE: boundary

BEDROCK REACHED:
[F3] BEDROCK-OBSERVE: /dd and /se have explicit input/output contract in their skill files
[F12] BEDROCK-OBSERVE: /dcp skills at similar grain; /diagnose routes between widely different grains
[F15] BEDROCK-OBSERVE: /dcp explicitly references "procedure from Step N" in each subsequent step
[F21] BEDROCK-OBSERVE: /uaua uses REGISTRY as accumulation container
[F24] BEDROCK-OBSERVE: /dd is semi-sovereign; /stg is chain-aware (expects COMPLETE_PLAN input)
[F29] BEDROCK-OBSERVE: /dcp declares "compound skill — chains 6 skills"; /diagnose routes with bare "→ INVOKE"
[F33] BEDROCK-OBSERVE: /uaua (35+ findings) vs /ata (quick tactical check) = massive grain mismatch
[F38] BEDROCK-OBSERVE: /rca Step 1 starts fresh ("Clearly articulate") without referencing /diagnose's prior work
[F43] BEDROCK-OBSERVE: /se says "use /dd if unknown" — dual-mode pattern that works standalone and in chain
[F46] BEDROCK-OBSERVE: /uaua Phase 2 forces re-compilation, preventing drift

TENSIONS:
[F41] contradicts [F42]: Reusability vs chain-awareness — but /se shows it's solvable with dual-mode design
[F6] contradicts [F5]: LLM carries context naturally vs cannot fix through prompting alone — resolved: LLM helps but explicit contracts are more reliable
[U21] contradicts [U22]: Skill author wants standalone vs chain designer wants composition — fundamental tension

CANDIDATE VERDICTS:
[U12] "Skills must know what they receive" — VALIDATED
  -- AR evidence: F1, F2, F3
  -- AW evidence: F6 (conditional — LLM helps but not sufficient)
  -- Verdict derived from: F3 (bedrock) shows explicit contracts exist in smooth chains; F38 (bedrock) shows they're absent in disjointed chains

[U14] "Single accumulating artifact" — DAMAGED
  -- AR evidence: F13, F14, F15
  -- AW evidence: F20, F21 (serious — /uaua works with additive accumulation)
  -- Verdict derived from: Principle is right but formulation is too narrow. Revised: chain needs a STRUCTURED ACCUMULATION CONTAINER — could be single artifact OR numbered registry

[U28] "Grain size match" — VALIDATED
  -- AR evidence: F30, F31, F33
  -- AW evidence: F34 (conditional)
  -- Verdict derived from: F12 and F33 (bedrock) show clear grain mismatch in disjointed chains vs matched grain in smooth chains

[U29] "Skill sovereignty" — VALIDATED
  -- AR evidence: F22, F23, F24
  -- AW evidence: F26 (conditional — LLM can compensate partially)
  -- Verdict derived from: F24 and F29 (bedrock) show sovereign vs chain-aware skills differ observably; F38 shows sovereign skills restart unnecessarily

[U30] "Chain context declaration" — VALIDATED
  -- AR evidence: F29 (bedrock direct)
  -- AW evidence: none that reaches bedrock
  -- Verdict derived from: F29 (bedrock) — /dcp declares chain context, /diagnose doesn't

[U31] "Structured accumulation container" — VALIDATED
  -- AR evidence: F15, F21, F46 (all bedrock)
  -- AW evidence: none reaching bedrock
  -- Verdict derived from: Three independent bedrock observations confirm this

TOTALS:
- Unbundled claims: 5
- Candidates mapped: 12 (U6-U11, U17-U20, U30-U31)
- Assumptions: 5 (4 load-bearing)
- Dimensions: 5 (2 hidden)
- Perspectives: 8
- AR findings: 14 (7 necessary, 5 probable, 2 conditional)
- AW findings: 6 (0 fatal, 2 serious, 4 conditional)
- Foreclosures: 3
- Derived alternatives: 4
- Edge cases: 7
- Bedrock reached: 10
- Tensions: 3
- Verdicts: 5 validated, 0 rejected, 1 damaged, 0 conditional, 0 uncertain
```

---

## Phase 3: SYNTHESIS

```
ORIGINAL INPUT: Why do some skill chains work smoothly while others feel disjointed?

SPACE SIZE: 53 unique findings

WHAT THE ANALYSIS ACTUALLY FOUND:

1. EXPLICIT DATA CONTRACTS are the primary differentiator. Smooth chains
   (/dcp) have skills whose SKILL.md files explicitly state what they
   produce and what they expect to receive. Disjointed chains (/diagnose
   routing) use bare "→ INVOKE" with no artifact specification. (F1, F2, F3, F38)

2. STRUCTURED ACCUMULATION CONTAINERS prevent drift and create coherence.
   /dcp accumulates "the procedure" through 6 steps. /uaua accumulates
   numbered findings in a REGISTRY. Chains without a named container for
   accumulated work lose coherence because findings dissolve into prose.
   (F13, F14, F15, F21, F46)

3. GRAIN SIZE MATCH matters. /dcp chains six mid-level analysis tools.
   /diagnose routes between meta-level routing, exhaustive deep exploration
   (/uaua at 35+ findings), and quick tactical checks (/ata). The jump
   between abstraction levels is jarring. (F30, F31, F12, F33)

4. SKILL SOVEREIGNTY creates disjointedness. Skills designed as standalone
   tools (with their own framing, purpose section, and conclusion) fight for
   narrative control when chained. Each tries to be a complete essay. /stg
   avoids this by explicitly expecting a COMPLETE_PLAN as input — it knows
   it's not standalone. /rca does not — it restarts the entire diagnostic
   process from scratch. (F22, F23, F24, F38)

5. CHAIN CONTEXT DECLARATION signals the LLM to operate in chain mode.
   /dcp's header says "This is a compound skill — it chains 6 skills in
   sequence." /diagnose's routing says "→ INVOKE: /uaua [symptom]" with no
   chain context. This difference determines whether the LLM treats each
   skill as a fresh start or a continuation. (F29)

6. LLM context carrying is HELPFUL but INSUFFICIENT. The LLM naturally
   carries some context across skill invocations within its context window.
   This compensates partially for missing data contracts. But when skill
   instructions say "start fresh" (as /rca does), the instructions override
   the carried context. (F6, F26, F39, F40)

7. DISJOINTEDNESS IS SOMETIMES APPROPRIATE. Routing redirects (/diagnose →
   /claim when "this isn't diagnostic") should feel like a pivot, not a
   continuation. Parallel analyses the user wants should stay separate.
   Not all chains should be smooth. (E6, E7, U5)

KEY TENSIONS:

1. Standalone reusability vs chain coherence (U21 vs U22) — TYPE: optimization frontier
   /se resolves this by saying "Prerequisites: Dimensions identified (use /dd
   if unknown)" — dual-mode design. Most skills haven't adopted this pattern.

2. LLM context carrying vs explicit contracts (F6 vs F5) — TYPE: information gap
   We don't know exactly how much the LLM compensates. Larger models with
   bigger context windows may tolerate looser contracts.

3. Skill author intent vs chain designer intent (F41 vs F42) — TYPE: commitment decision
   Each skill author designs for standalone use. Chain coherence is an
   emergent property nobody explicitly owns.

VOI RANKING (Value of Information):

1. [F38] /rca starts fresh despite /diagnose already doing symptom identification — learning whether adding "using the symptom from /diagnose:" to /rca's invocation fixes the disjointedness would resolve whether explicit contracts are sufficient
2. [F29] /dcp declares "compound skill" but /diagnose doesn't — testing whether adding chain declarations to /diagnose improves output quality
3. [E2] Context window drift at 6+ steps — testing at what chain length contracts stop being sufficient

LOAD-BEARING ASSUMPTIONS:
[U12] [U13] [U15] — If any of these are false, the entire diagnosis changes direction

HIDDEN DIMENSIONS:
[U28] Grain size match — not discussed in any skill file but observably present
[U29] Skill sovereignty — not discussed anywhere but explains the "two essays" phenomenon

WEAKEST LINKS:
[F31] "All 6 /dcp skills are mid-level" — rated Probable, not verified systematically
[F44] "6+ step chains degrade" — rated Probable, no empirical test
[F34] "Grain mismatch might not be primary" — still Conditional

ALTERNATIVES DERIVED FROM ANALYSIS:
1. Add dual-mode headers to all skills (like /se's pattern) — derived from F42, F43
2. Add chain context declarations to compound skills — derived from F29
3. Add explicit "receives: [artifact]" and "produces: [artifact]" to skill frontmatter — derived from F3, F15
4. Add registry/accumulation checkpoints to long chains — derived from F46

TESTABLE PREDICTIONS:
- Adding "receives: [symptom from /diagnose]" to /rca's invocation will reduce disjointedness (from F1, F3, F38)
- Adding "This is step N of M in the chain: [chain name]" before each invocation will improve coherence (from F29)
- Chains where all skills operate at similar depth (1x-2x vs 8x-16x) will feel smoother than mixed-depth chains (from F30, F33)
- Adding a "checkpoint: compile accumulated findings" step every 3 skills in a long chain will prevent drift (from F46)

DO_FIRST ACTIONS:
1. Audit /dcp chain for explicit data contracts — WHO: Claude — resolves: confirms F3
2. Identify all compound skills and check for chain context declarations — WHO: Claude — resolves: F29, U30
3. Add "receives:" and "produces:" fields to skill frontmatter as a convention — WHO: user — resolves: U12, U13, F1
4. Add /se-style dual-mode prerequisites to chain-frequent skills — WHO: user — resolves: F41, F42

UNRESOLVED:
- How much LLM context carrying compensates for missing contracts — needs empirical testing
- Whether grain size is independently causal or merely correlated with other factors — F34 stayed Conditional
- Optimal chain length before accumulation checkpoints become necessary — E2 needs testing

READY FOR:
- /ar "Adding explicit data contracts between skills is sufficient to fix chain disjointedness" — to test whether contracts alone are enough
- /aw "Skill sovereignty is a real problem" — to stress-test whether the LLM actually compensates fully
- /how "Add input/output contracts to all chainable skills" — to operationalize the fix
```

---

## Diagnostic Report

### The Symptom As Stated
Some skill chains produce integrated, cumulative output where each step builds naturally on the last. Others produce output that reads like separate, disconnected analyses pasted together.

### Root Causes Identified

**Root Cause 1: Missing Data Contracts (CONFIRMED)**
Smooth chains (/dcp) have skills whose SKILL.md files explicitly state what they produce and what they expect. `/dd` produces "DIMENSIONS DISCOVERED FOR: [domain]" and `/se` opens with "Confirm Dimensions — Prerequisites: Dimensions identified." Disjointed chains use bare `→ INVOKE: /skill [args]` with no artifact specification. The next skill doesn't know what it received.

**Root Cause 2: Missing Accumulation Container (CONFIRMED)**
Smooth chains maintain a single named artifact ("/dcp" accumulates "the procedure") or a structured registry (/uaua's numbered findings). Disjointed chains let findings dissolve into prose, making them unreferenceable by later steps.

**Root Cause 3: Skill Sovereignty (CONFIRMED)**
Skills designed as standalone tools (with their own introduction, framing, and conclusion) each try to "own" the response. When chained, this produces the "two separate essays" effect. Chain-aware skills like `/stg` (which expects a COMPLETE_PLAN as input) avoid this.

**Root Cause 4: Grain Size Mismatch (CONFIRMED)**
Adjacent skills in smooth chains operate at similar abstraction levels. In disjointed chains, the jump between exhaustive deep exploration (/uaua at 35+ findings) and quick tactical checks (/ata) is jarring.

**Root Cause 5: Missing Chain Context Declaration (CONFIRMED)**
/dcp tells the LLM "This is a compound skill — it chains 6 skills in sequence." /diagnose's routing just says "→ INVOKE." The LLM needs to know it's in a chain to suppress standalone behavior.

### Causal Chain
```
Skills designed for standalone use (sovereignty)
  + No data contracts between skills
  + No chain context declaration in compound skill
  + No named accumulation container
  = Each skill starts fresh, frames independently, produces separate output
  = User reads N disconnected analyses instead of one coherent chain
```

### Prevention

1. **Add `receives:` and `produces:` to skill frontmatter** — makes data contracts explicit
2. **Adopt /se's dual-mode pattern** — "Prerequisites: X (use /dd if unknown)" lets skills work both standalone and in chains
3. **Add chain context declarations** — "This is a compound skill — it chains N skills in sequence. Each step builds on the prior step's output."
4. **Name the accumulating artifact** in compound skills — "This chain progressively builds: [artifact name]"
5. **Match grain sizes** — don't chain a 16x-depth skill with a 1x-depth skill without a compression step between them
6. **Add registry checkpoints** in chains longer than 4 steps — force re-compilation of accumulated findings to prevent drift

### What's Still Unresolved
- Exact threshold where LLM context carrying stops compensating for missing contracts
- Whether grain size mismatch is independently causal or a proxy for the other root causes
- Optimal chain length before mandatory accumulation checkpoints
