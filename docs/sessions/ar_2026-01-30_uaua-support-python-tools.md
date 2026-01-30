# AR — UAUA Support with Customization and Variation

**Date**: 2026-01-30
**Depth**: 2x
**Input**: We also need to add UAUA support and all the customization and variation possible with that

---

## CLAIM REGISTRY

```
CLAIM REGISTRY
==============

[C1]  UAUA should be a first-class search mode in the Python tools
      TYPE: root — STRENGTH: assumed

[C2]  UAUA is phase-ordered, not ratio-mixed — requires phase-sequenced expansion
      TYPE: implication — STRENGTH: necessary

[C3]  Each UAUA phase has distinct prompt and node type (U1, AR, U2, AW)
      TYPE: implication — STRENGTH: necessary

[C4]  Expansion loop needs a phase pointer tracking current UAUA phase
      TYPE: implication — STRENGTH: necessary

[C5]  Phase transitions configurable: batch-size, depth, or exhaustion triggers
      TYPE: implication — STRENGTH: probable

[C6]  branch_type column must expand beyond "ar"/"aw" to support "u1"/"u2" or arbitrary labels
      TYPE: implication — STRENGTH: necessary

[C7]  Each phase needs its own LLM prompt template (U asks for universalization)
      TYPE: implication — STRENGTH: necessary

[C8]  Phase pointer must persist in SQLite (survives interruptions)
      TYPE: implication — STRENGTH: probable

[C9]  FORECLOSED: Stateless per-node type selection — UAUA requires global phase coordination
      TYPE: foreclosure — STRENGTH: necessary

[C10] Three transition modes via CLI: batch:N, depth:N, exhaust
      TYPE: implication — STRENGTH: probable

[C11] Custom phase sequences beyond U→AR→U→AW (e.g., U→AR→AR→AW, reversed order)
      TYPE: implication — STRENGTH: probable

[C12] get_unexplored() must filter by current phase label
      TYPE: implication — STRENGTH: necessary

[C13] Leverage scoring needs phase-aware weights (universalize ≠ consequence-tracing)
      TYPE: implication — STRENGTH: probable

[C14] Prompt registry: phase_label → prompt_template → response_schema
      TYPE: implication — STRENGTH: necessary

[C15] U-phase outputs universalized_claims — broadening nodes vs AR/AW deepening nodes
      TYPE: implication — STRENGTH: necessary

[C16] UAUA (sequential phases) and ratio-mixing (proportional) are two scheduling modes
      over the same search types — both should coexist
      TYPE: implication — STRENGTH: necessary

[C17] Phase sequence should loop by default until budget exhausted
      TYPE: implication — STRENGTH: probable

[C18] UAUA trees have different topology — wider at U boundaries, deeper in AR/AW phases
      TYPE: implication — STRENGTH: probable

[C19] COST: U-phase expansions are harder for the LLM — expect lower quality, more retries
      TYPE: cost — STRENGTH: probable

[C20] SQLite search_config stores: current_phase, phase_sequence, transition_mode, phase_history
      TYPE: implication — STRENGTH: probable

[C21] Clean architecture: search types (AR/AW/U) are registry entries; UAUA and ratio-mixing
      are scheduling policies over those types — this unifies both systems
      TYPE: implication — STRENGTH: necessary

[C22] New search types (Analogy, Inversion, SCAMPER) become trivial additions to the registry
      TYPE: implication — STRENGTH: probable

TOTALS:
- Root claims: 1
- Necessary implications: 11
- Probable implications: 9
- Foreclosures: 1
- Costs: 1
```

---

## SYNTHESIS

```
ORIGINAL CLAIM: The Python ARAW tools should support UAUA as a first-class search
mode with full customization and variation.

IMPLICATION PATTERN: Convergent — most implications point to a single architectural insight.

COMMITMENT CHAIN:
If this is right:
→ you must accept: C2 (phase-ordered expansion), C3 (distinct prompts per phase),
  C4 (phase pointer), C6 (expanded branch_type), C7 (per-phase prompts),
  C9 (FORECLOSED stateless selection), C12 (phase-filtered querying),
  C14 (prompt registry), C15 (U-nodes broaden, AR/AW deepen),
  C16 (two scheduling modes coexist), C21 (unified architecture)
→ you probably accept: C5 (configurable transitions), C8 (persistent phase state),
  C10 (CLI transition modes), C11 (custom sequences), C13 (phase-aware leverage),
  C17 (looping), C20 (search_config table), C22 (pluggable types)
→ you can no longer: C9 (stateless per-node selection for UAUA)
→ you lose: C19 (U-phase quality — universalization is harder for LLMs than
  consequence-tracing, expect degraded output)

WHAT THE RIGHTNESS ANALYSIS ACTUALLY FOUND:

1. The critical architectural insight is C21: UAUA and the configurable ratio system
   from the previous analysis are NOT competing features — they are two scheduling
   policies over the same set of search types. The search type registry (C14) is the
   shared foundation. AR, AW, and U are registered search types with prompts and schemas.
   UAUA schedules them sequentially. Ratio-mixing schedules them proportionally.
   Both use the same registry.

2. UAUA requires global state (C4, C8, C9) that pure ratio-mixing does not. A phase
   pointer must coordinate which type is active, when transitions happen, and what the
   sequence is. This is a strictly harder scheduling problem than weighted coin flips.

3. The customization space has three independent dimensions:
   - Search types: what expansion operations exist (AR, AW, U, and future types)
   - Phase sequence: in what order to apply them (U→AR→U→AW, or any permutation)
   - Transition triggers: when to switch phases (batch count, depth, exhaustion)
   These should be independently configurable.

4. U-phase nodes are topologically different from AR/AW nodes (C15, C18). U broadens
   (abstracting from a specific claim to a general principle), while AR/AW deepen
   (tracing consequences or causes). This means UAUA trees have a characteristic
   shape: fan-out at U boundaries, depth within AR/AW phases. Analysis tools need
   to understand this.

5. The implementation path is: build the search type registry first (C14), then
   implement UAUA scheduling on top of it (C4, C16), then add configurable transitions
   (C5, C10), then custom sequences (C11). This order means each step is independently
   useful and testable.

TENSIONS:
- C19 vs C15: U-phase is architecturally important (C15) but may produce lower-quality
  output (C19). If U-nodes are reliably weak, the whole UAUA value proposition degrades.
  Resolution: Build it and measure. If U-quality is too low, fall back to ratio-mixing
  with a small U proportion rather than strict phase sequencing.

WEAKEST LINKS:
- C19 (U-phase quality) — The entire UAUA model depends on universalization being a
  productive operation for LLMs. If it isn't, sequential UAUA loses to ratio-mixing.
- C13 (phase-aware leverage) — Unclear what the right leverage weights are for U-nodes.
  Needs empirical tuning.

TESTABLE PREDICTIONS:
- [from C18] UAUA trees will have measurably different branching factor at U-boundary
  nodes vs within AR/AW phases.
- [from C21] A system built with the search type registry can run both UAUA mode and
  ratio-mixing mode without code changes — just CLI flag differences.
- [from C16] Users will use both modes: UAUA for structured analysis, ratio-mixing
  for exploratory search. They solve different problems.

UNRESOLVED:
- Whether LLMs can reliably universalize (C19) — no data yet.
- Optimal transition trigger for UAUA phases — batch:10, depth:3, or exhaust?
  Needs experimentation.
- Whether custom sequences beyond standard UAUA (C11) are actually useful or
  just theoretical flexibility nobody uses.
```
