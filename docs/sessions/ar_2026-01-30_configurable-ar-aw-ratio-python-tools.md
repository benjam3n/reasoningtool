# AR — Configurable AR/AW Ratio for Python Tools

**Date**: 2026-01-30
**Depth**: 4x
**Input**: We need to figure out the best way to make the python tools be able to run just AR or just AW or to specify the exact ratio of AR to AW etc so like if you are 90% confident you can do 90 AR 10 AW or something like that or also just be able to do 100 AW or 100 AR etc and also allow for changing the percentage mid search, so every 10 new generations it randomizes, or randomizes after how many generations it randomizes on some number between 0-30 or also allow for different variation search types etc.

---

## CLAIM REGISTRY

```
[R1]  Configurable AR/AW ratio is the right approach — TYPE: root — STRENGTH: assumed
[R2]  Current 50/50 split is suboptimal for many use cases — TYPE: implication — STRENGTH: necessary
[R3]  Different claims have different confidence levels, search should reflect that — TYPE: implication — STRENGTH: necessary
[R4]  High-confidence claims should spend more on AR than AW — TYPE: implication — STRENGTH: probable
[R5]  Current system wastes ~40% expansion budget on weak AW for confident claims — TYPE: cost — STRENGTH: probable
[R6]  FORECLOSED: Equal adversarial pressure for all claims — TYPE: foreclosure — STRENGTH: necessary
[R7]  System must accept user confidence as input, not just claim text — TYPE: commitment — STRENGTH: necessary
[R8]  LLM prompt schema must pass confidence/ar_weight parameter — TYPE: implication — STRENGTH: necessary
[R9]  Low-confidence claims should spend almost all energy on AW — TYPE: implication — STRENGTH: probable
[R10] Pure AW mode is a distinct tool (stress test / devil's advocate) — TYPE: implication — STRENGTH: probable
[R11] Tool identity changes by ratio: commitment tracer / falsification engine / balanced ARAW — TYPE: implication — STRENGTH: necessary
[R12] Some domains inherently need asymmetric search — TYPE: implication — STRENGTH: probable
[R13] Domain-specific presets should exist (safety=90AW, brainstorm=90AR) — TYPE: implication — STRENGTH: possible
[R14] Existing --domain-weights flag provides infrastructure for this — TYPE: implication — STRENGTH: necessary
[R15] Ratio implementable at node selection level — TYPE: implication — STRENGTH: probable
[R16] Simplest: weighted coin flip between AR queue and AW queue — TYPE: implication — STRENGTH: necessary
[R17] Requires maintaining two separate queues by branch_type — TYPE: commitment — STRENGTH: necessary
[R18] Adding branch_type filter to get_unexplored() is trivial — TYPE: implication — STRENGTH: necessary
[R19] FORECLOSED: Single-queue where AR and AW compete on leverage alone — TYPE: foreclosure — STRENGTH: probable
[R20] AW leverage should be reduced proportional to confidence — TYPE: implication — STRENGTH: probable
[R21] leverage_adjusted formula: leverage_base * confidence for AR, leverage_base * (1-confidence) for AW — TYPE: implication — STRENGTH: probable
[R22] TENSION: Two-queue (R17) vs leverage-adjustment (R21) — TYPE: tension — STRENGTH: n/a
[R23] Alternatively: implement ratio at LLM prompt level — TYPE: implication — STRENGTH: possible
[R24] At 90/10, ask for 4-5 AR consequences and 0-1 AW causes — TYPE: implication — STRENGTH: probable
[R25] Node-level ratio affects tree topology; queue-level affects traversal order. Complementary. — TYPE: implication — STRENGTH: necessary
[R26] COST: At 100% AR, no falsification — tool becomes blind to assumptions — TYPE: cost — STRENGTH: necessary
[R27] Pure AR mode should carry a warning about no adversarial testing — TYPE: commitment — STRENGTH: necessary
[R28] Mid-search ratio changes are the right approach — TYPE: implication — STRENGTH: probable
[R29] Confidence changes as you explore — ratio should track this — TYPE: implication — STRENGTH: necessary
[R30] Requires feedback loop: re-assess confidence after each batch — TYPE: commitment — STRENGTH: probable
[R31] Existing --gate-interval and --checkpoint are natural insertion points — TYPE: implication — STRENGTH: necessary
[R32] Automatic ratio adjustment possible based on branch quality — TYPE: implication — STRENGTH: possible
[R33] This is an explore/exploit tradeoff — maps to multi-armed bandits — TYPE: implication — STRENGTH: necessary
[R34] COST: Auto-adjustment removes user agency — TYPE: cost — STRENGTH: probable
[R35] Auto-adjustment should be opt-in, never override explicit user ratio — TYPE: commitment — STRENGTH: necessary
[R36] Randomized interval switching is the right approach — TYPE: implication — STRENGTH: possible
[R37] Randomization prevents systematic bias from ordering effects — TYPE: implication — STRENGTH: probable
[R38] Same insight as existing --rotate flag — TYPE: implication — STRENGTH: necessary
[R39] Random interval length prevents periodic patterns — TYPE: implication — STRENGTH: probable
[R40] Implementation: draw next_switch ~ Uniform(0,30), switch ratio at that point — TYPE: implication — STRENGTH: probable
[R41] COST: Randomization makes results non-reproducible — TYPE: cost — STRENGTH: necessary
[R42] Log random seed and ratio changes on each node for reproducibility — TYPE: commitment — STRENGTH: necessary
[R43] FORECLOSED: Deterministic ratio scheduling — TYPE: foreclosure — STRENGTH: possible
[R44] Deterministic scheduling is still valid as an option, not foreclosed — TYPE: implication — STRENGTH: necessary
[R45] Different variation search types beyond AR/AW should be pluggable — TYPE: implication — STRENGTH: probable
[R46] Binary AR/AW doesn't capture all useful exploration modes — TYPE: implication — STRENGTH: probable
[R47] Other types: Universalize, Analogy, Inversion, SCAMPER — TYPE: implication — STRENGTH: necessary
[R48] Pluggable types means LLM prompt changes per search type — TYPE: commitment — STRENGTH: necessary
[R49] Expansion schema needs search type → prompt → schema registry — TYPE: implication — STRENGTH: probable
[R50] Significant refactor: define SearchType interface, implement AR/AW as first plugins — TYPE: commitment — STRENGTH: probable
[R51] COST: More search types = more complexity, prompt engineering, drift potential — TYPE: cost — STRENGTH: necessary
[R52] Start with AR, AW, U as three core types (mirrors UAUA) — TYPE: commitment — STRENGTH: probable
[R53] Ratio like 40AR/30AW/30U would implement automated UAUA — TYPE: implication — STRENGTH: probable
[R54] Killer feature: automated UAUA at scale with configurable ratios — TYPE: implication — STRENGTH: probable
[R55] FORECLOSED: UAUA as strictly sequential — TYPE: foreclosure — STRENGTH: probable
[R56] Sequential UAUA is a special case of configurable ratio scheduling — TYPE: implication — STRENGTH: necessary
```

---

## SYNTHESIS

```
ORIGINAL CLAIM: The Python ARAW tools should support configurable AR/AW ratios
with mid-search changes, randomization, and pluggable search types.

IMPLICATION PATTERN: Expansive with convergent core

COMMITMENT CHAIN:
If this is right:
→ you must accept: R6 (no more equal pressure), R7 (confidence as input),
  R8 (schema changes), R11 (tool identity changes by ratio), R18 (branch_type filter),
  R25 (two levels: topology + traversal), R27 (pure-mode warnings),
  R35 (user intent > auto-adjustment), R42 (log everything for reproducibility),
  R48 (prompt changes per type), R56 (sequential UAUA is a special case)
→ you probably accept: R4, R9, R21 (leverage weighting), R29 (confidence tracks exploration),
  R32 (auto-adjustment possible), R49 (search type registry), R53 (automated UAUA)
→ you can no longer: R6 (equal pressure assumption), R19 (single-queue selection),
  R43 (deterministic-only scheduling), R55 (UAUA as strictly sequential)
→ you lose: R26 (at pure AR, you lose falsification), R34 (at auto-adjust, you lose user agency),
  R41 (at randomized, you lose reproducibility), R51 (at pluggable types, you lose simplicity)

WHAT THE RIGHTNESS ANALYSIS ACTUALLY FOUND:
1. The ratio system operates at TWO independent levels that are complementary, not
   competing: node-level (how many AR vs AW branches per expansion, R25) and
   queue-level (which branch_type to explore next, R15-R18). Both should be configurable.
2. There are two competing implementation strategies for queue-level ratios: explicit
   two-queue selection (R17) and leverage-score adjustment (R21). Leverage adjustment
   is more elegant and integrates with existing strategy logic; two-queue is more
   explicit and debuggable. (R22)
3. The configurable ratio system GENERALIZES UAUA (R54-R56). Sequential UAUA (U→A→U→A)
   is just one scheduling preset. Proportional mixing (40AR/30AW/30U) is a strictly
   more powerful operation. This is the most important finding.
4. Pure modes (100% AR or 100% AW) create genuinely different tools (R11): a commitment
   tracer, a falsification engine, and balanced exploration. These aren't just parameter
   variations — they're different epistemic operations.
5. Mid-search ratio changes are necessary because confidence shifts during exploration (R29).
   The existing --checkpoint and --gate-interval mechanisms are natural insertion points (R31).
6. Auto-adjustment maps to multi-armed bandit theory (R33) but must be opt-in because
   it fights user intent (R34-R35).
7. Randomized scheduling prevents ordering bias (R37) but costs reproducibility (R41).
   Logging the seed and per-node ratio preserves reproducibility (R42).
8. Pluggable search types beyond AR/AW are the path to automated UAUA at scale (R52-R54),
   but should start with just three types: AR, AW, U.

TENSIONS / CONTRADICTIONS:
[R22] Two-queue (R17) vs leverage-adjustment (R21) — competing implementations.
      Resolution: Use leverage adjustment as primary (integrates with strategies),
      offer explicit queue mode as --explicit-queues for debugging/transparency.

WEAKEST LINKS:
- R32 (auto ratio adjustment) — Possible, not Necessary. Requires defining "branch quality"
  metrics that don't exist yet. May over-engineer before the basic ratio works.
- R13 (domain presets) — Possible. Depends on whether domain detection is reliable enough.
- R36 (randomized intervals) — Possible. The benefit over deterministic scheduling is
  theoretical. May not matter in practice.
- R49 (search type registry) — Probable but expensive. The refactor is significant.
  Should only happen after AR/AW ratios work well.

TESTABLE PREDICTIONS:
- [from R5] Runs with 90AR/10AW on high-confidence claims will produce fewer trivial AW
  branches and more novel implications than 50/50 runs.
- [from R21] Leverage-adjusted queues will produce realized ratios within 5% of configured
  ratios over 100+ node runs.
- [from R53] A 40AR/30AW/30U configuration will discover claims that neither pure ARAW
  nor sequential UAUA finds, because simultaneous mixing explores a different region
  of the search space.
- [from R41→R42] Logged random seeds will allow exact reproduction of randomized runs.

UNRESOLVED:
- Whether leverage adjustment (R21) or explicit queues (R17) performs better in practice —
  need to build both and compare.
- What "branch quality" metric drives auto-adjustment (R32) — no clear definition yet.
- Whether three search types (AR/AW/U) are sufficient or whether Analogy/Inversion/SCAMPER
  add enough value to justify the plugin complexity (R47 stayed Possible).
```
