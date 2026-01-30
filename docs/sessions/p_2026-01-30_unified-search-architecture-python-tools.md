# PROPOSE — Unified Search Architecture for Python ARAW Tools

**Date**: 2026-01-30
**Input**: Best method integrating configurable AR/AW ratios and UAUA support for Python tools

---

## PLAN REGISTRY

```
PLAN REGISTRY
=============

SOURCE: /ar on configurable AR/AW ratios (4x) + /ar on UAUA support (2x)
PLANS EXTRACTED: 5

[PLAN-1] Build the Search Type Registry as shared foundation
  STEELMAN: Both analyses independently converge on this — it's the architectural keystone
    that makes ratio-mixing and UAUA scheduling use the same abstraction layer.
  STRENGTHS: R49, C14, C21 (convergent across both analyses — strongest possible signal)
  WEAKNESSES: R51 (complexity cost), R50 (significant refactor)
  RISKS: Over-engineering the interface; regression in existing AR/AW behavior
  DEPENDENCIES: None — this is the foundation layer
  REVERSIBILITY: Hard to undo — once code is restructured around the registry, reverting is costly
  COST: Significant refactor of auto_expand_llm.py prompt/schema handling
  GIVES UP: The simplicity of hardcoded AR/AW logic; ability to quickly hack one-off changes
  FIRST ACTIONS:
    1. Define SearchType dataclass: label, prompt_template, response_schema, leverage_weight
    2. Implement AR and AW as the first two registered types (migrate existing prompts)
    3. Implement U as the third type with universalization prompt
    4. Verify existing ARAW behavior unchanged via regression test

[PLAN-2] Implement ratio-mixing scheduling (weighted proportional selection)
  STEELMAN: Simpler scheduling mode that handles the core use case (90AR/10AW) via
    leverage adjustment or explicit two-queue, integrating with existing infrastructure.
  STRENGTHS: R15-R18, R21, R25, R28-R31 (deep support chain, mostly necessary strength)
  WEAKNESSES: R22 (which implementation strategy is better — unresolved)
  RISKS: Leverage adjustment producing drift from configured ratio; two-queue being too rigid
  DEPENDENCIES: PLAN-1 (needs registry to know which types exist and their prompts)
  REVERSIBILITY: Partial — the CLI flags and queue logic are removable; schema changes are harder
  COST: Moderate — queue filtering, leverage formula, CLI args, mid-search change hooks
  GIVES UP: Guarantee of equal adversarial pressure (R6); simplicity of fixed 50/50
  FIRST ACTIONS:
    1. Add --ratio CLI arg accepting format like "90:10" or "40:30:30"
    2. Implement leverage-adjusted scoring per R21 formula
    3. Implement explicit two-queue mode as --explicit-queues fallback
    4. Add mid-search ratio change at --gate-interval checkpoints
    5. Add pure-mode warnings per R27

[PLAN-3] Implement UAUA sequential scheduling with configurable transitions
  STEELMAN: UAUA produces qualitatively different exploration than ratio-mixing —
    sequential phases create distinct tree topologies that explore different claim space.
  STRENGTHS: C2, C4, C16, C21 (necessary strength across multiple items)
  WEAKNESSES: C19 (U-phase quality unknown), C9 (harder implementation — global state)
  RISKS: U-phase producing unusable output; phase state corruption on crash
  DEPENDENCIES: PLAN-1 (needs registry for phase → prompt mapping)
  REVERSIBILITY: Partial — scheduling logic removable; SQLite schema changes harder
  COST: High — phase pointer, state persistence, transition logic, custom sequences, CLI args
  GIVES UP: Simplicity of stateless expansion; ability to explain results without understanding phases
  FIRST ACTIONS:
    1. Add --schedule CLI arg accepting format like "U,AR,U,AW"
    2. Add --transition CLI arg accepting "batch:N", "depth:N", or "exhaust"
    3. Implement phase pointer with SQLite persistence (search_config table)
    4. Implement phase-filtered get_unexplored()
    5. Default: --schedule U,AR,U,AW --transition batch:10, loop until budget

[PLAN-4] Add auto-adjustment (multi-armed bandit) as opt-in layer
  STEELMAN: If branch quality can be measured, automatic ratio optimization eliminates
    the need for users to guess — the system converges on the productive ratio.
  STRENGTHS: R33 (maps to bandits — real theoretical foundation)
  WEAKNESSES: R32 (possible, not necessary), R34 (user agency cost)
  RISKS: No reliable quality metric; system converges on bad ratio; user trusts blindly
  DEPENDENCIES: PLAN-2 (needs ratio-mixing to adjust); quality metric definition (doesn't exist)
  REVERSIBILITY: Easy — opt-in flag, can remove without affecting other features
  COST: Research cost to define quality metric; implementation of bandit algorithm
  GIVES UP: Predictability of static ratios; user's ability to fully control exploration
  FIRST ACTIONS:
    1. Define candidate branch quality metrics (novelty, depth, crux-proximity)
    2. Implement simple UCB1 bandit over search types
    3. Gate behind --auto-adjust flag per R35

[PLAN-5] Add domain presets and confidence-as-input
  STEELMAN: Codifies domain knowledge so users don't re-derive ratio mappings. Confidence
    input translates epistemic state to ratio automatically.
  STRENGTHS: R3, R7 (necessary), R12 (probable)
  WEAKNESSES: R13 (possible — domain detection reliability unknown)
  RISKS: Presets wrong for specific sub-domains; confidence→ratio mapping incorrect
  DEPENDENCIES: PLAN-2 (needs ratio-mixing to set the ratio presets target)
  REVERSIBILITY: Easy — presets are just configuration, removable without code changes
  COST: Low — preset definitions, CLI arg, simple mapping function
  GIVES UP: Nothing significant — presets are additive
  FIRST ACTIONS:
    1. Add --confidence CLI arg (0.0-1.0) with linear mapping to AR:AW ratio
    2. Add --domain CLI arg with preset table (safety=10:90, brainstorm=90:10, balanced=50:50)
    3. Allow --ratio to override presets explicitly

COMPARISON TABLE:
| Plan | Strengths | Weaknesses | Reversible? | Cost | Gives Up |
|------|-----------|------------|-------------|------|----------|
| PLAN-1 Registry | Convergent across both analyses | Significant refactor | No | High | Hardcoded simplicity |
| PLAN-2 Ratio-mix | Deep necessary chain | Implementation strategy unresolved | Partial | Moderate | Equal pressure guarantee |
| PLAN-3 UAUA | Necessary for phase-ordered search | U-phase quality unknown | Partial | High | Stateless simplicity |
| PLAN-4 Auto-adjust | Real theoretical basis | No quality metric exists | Yes | Research + moderate | Predictability |
| PLAN-5 Presets | Necessary confidence input | Domain reliability unknown | Yes | Low | Nothing significant |

PLAN INTERACTIONS:
- PLAN-1 enables PLAN-2: Registry provides the types that ratio-mixing schedules over
- PLAN-1 enables PLAN-3: Registry provides the types that UAUA sequences over
- PLAN-2 and PLAN-3: Compatible — two scheduling modes over the same registry (C16, C21)
- PLAN-2 enables PLAN-4: Auto-adjust modifies the ratio that PLAN-2 implements
- PLAN-2 enables PLAN-5: Presets set the ratio that PLAN-2 implements
- PLAN-4 and PLAN-5: Compatible but partially redundant — auto-adjust makes presets less necessary
- PLAN-3 blocks PLAN-4: Auto-adjustment doesn't apply to phase-sequenced scheduling (different mechanism)
```

---

## RECOMMENDATION SYNTHESIS

```
[PLAN-1] RECOMMENDED: Build the Search Type Registry
  DERIVATION CHAIN:
    R49 + C14 (both necessary) show that a prompt/schema registry is independently required
      by both ratio-mixing and UAUA scheduling.
    C21 (necessary) shows that the registry is the unifying abstraction — it makes PLAN-2
      and PLAN-3 build on the same foundation instead of being parallel implementations.
    R48, C7 (both necessary) show that per-type prompts are required regardless of
      scheduling mode.
    -> Both analyses converge on the same component at "necessary" strength — this is
       the highest-confidence finding across 78 source items.
    -> Therefore: build this first; everything else depends on it.
  USE IF: You intend to implement any of PLAN-2, PLAN-3, PLAN-4, or PLAN-5.
  DON'T USE IF: You only want basic fixed 50/50 ARAW with no configurability — but both
    analyses assume this is insufficient (R2, C1).
  FIRST ACTIONS:
    1. Define SearchType dataclass in a new module (search_types.py) — resolves R49, C14
    2. Migrate existing AR prompt/schema from auto_expand_llm.py into AR type — resolves R48
    3. Migrate existing AW prompt/schema into AW type — resolves R48
    4. Create U type with universalization prompt — resolves C7, R52
    5. Run existing test suite to verify no regression — validates R50 refactor

[PLAN-2] RECOMMENDED: Implement Ratio-Mixing Scheduling
  DERIVATION CHAIN:
    R15-R18 (necessary) show ratio is implementable at queue level with branch_type filter.
    R21 (probable) provides concrete leverage formula. R22 acknowledges tension but
      recommends leverage-adjustment as primary with explicit-queue as debug fallback.
    R28-R31 (necessary/probable) show mid-search changes are required and existing
      infrastructure supports them.
    R37-R42 show randomization adds value and reproducibility is preserved via seed logging.
    -> The implementation path is well-defined with mostly necessary-strength support.
    -> Therefore: implement after PLAN-1 registry is built.
  USE IF: You have PLAN-1 in place. This is the simpler of the two scheduling modes and
    handles the most common use case (adjustable AR/AW proportion).
  DON'T USE IF: You only need strict UAUA sequencing with no ratio flexibility — but R56
    shows sequential UAUA is a special case, not the general case.
  FIRST ACTIONS:
    1. Add --ratio CLI arg — resolves R7, R8
    2. Implement leverage-adjusted scoring — resolves R21
    3. Add --explicit-queues fallback — resolves R22 tension
    4. Hook ratio changes into --gate-interval — resolves R29, R31
    5. Add pure-mode warning — resolves R26, R27

[PLAN-3] CONDITIONALLY RECOMMENDED: Implement UAUA Sequential Scheduling
  DERIVATION CHAIN:
    C2, C4 (necessary) show that UAUA requires phase-ordered expansion with a phase pointer.
    C16, C21 (necessary) show UAUA coexists with ratio-mixing over the same registry.
    C18 (probable) shows UAUA trees have qualitatively different topology.
    -> However, C19 (probable cost) shows U-phase quality is unknown — the entire UAUA
       model depends on LLMs producing useful universalizations.
    -> Therefore: implement after PLAN-1 and PLAN-2, but validate U-phase quality first.
  CONDITION: U-phase prompt produces usable universalizations in initial testing.
  HOW TO CHECK: Run 20 U-phase expansions manually, evaluate whether the abstract claims
    are genuinely more general (not just vague) and whether AR/AW on those claims finds
    novel territory. If >60% of U-nodes produce useful branches, proceed.
  USE IF: U-phase quality passes the check AND you want structured epistemic phase alternation.
  DON'T USE IF: U-phase quality fails — in that case, use ratio-mixing with a small U
    proportion (e.g., 40:30:30) instead of strict sequencing. This gets some U benefit
    without depending on every U-phase being productive.
  IF CONDITION UNKNOWN: Run the 20-node U-phase quality check before implementing the
    full scheduling infrastructure.
  FIRST ACTIONS:
    1. Write and test U-phase prompt — resolves C7, validates C19
    2. Run 20-node quality check — resolves condition
    3. If passes: implement phase pointer and SQLite persistence — resolves C4, C8, C20
    4. Add --schedule and --transition CLI args — resolves C5, C10, C11

[PLAN-4] NOT RECOMMENDED: Auto-Adjustment (Multi-Armed Bandit)
  STEELMAN REMINDER: If branch quality can be measured, automatic ratio optimization
    eliminates user guessing — the system converges on the productive ratio, strictly
    better than any static choice for users without confidence priors.
  DERIVATION CHAIN:
    R33 (necessary) correctly identifies this as an explore/exploit tradeoff.
    -> But R32 (possible, not necessary) is the only item supporting the feature itself.
    -> R34 (probable) shows it removes user agency.
    -> R35 (necessary) constrains it to opt-in only.
    -> No source item defines what "branch quality" means — the reward signal for the
       bandit does not exist yet.
    -> Despite the steelman, this fails because the prerequisite (quality metric) is
       undefined, and the cost (user agency) is real.
  WHY IT FAILS: R32 stayed at "possible" — the weakest non-speculative strength. The quality
    metric it depends on has no definition in either analysis. Building a bandit without a
    reward signal is engineering fiction.
  WHAT WOULD CHANGE THIS VERDICT: A concrete, validated branch quality metric that
    predicts which expansion types produce more valuable nodes. If someone defines and
    tests this metric, auto-adjustment becomes viable.
  USE INSTEAD: PLAN-5 (domain presets / confidence input) addresses the same problem
    (user doesn't know the right ratio) with less risk.

[PLAN-5] CONDITIONALLY RECOMMENDED: Domain Presets and Confidence-as-Input
  DERIVATION CHAIN:
    R7 (necessary) shows confidence must be a system input.
    R3-R4 (necessary/probable) show different confidence levels need different ratios.
    R12-R14 (probable/possible/necessary) show domain-specific asymmetry exists and
      existing infrastructure supports it.
    -> Confidence-as-input is necessary; domain presets are possible but additive.
    -> Therefore: implement confidence input with PLAN-2; add presets when domain
       knowledge is validated.
  CONDITION: PLAN-2 (ratio-mixing) is implemented, providing the mechanism presets target.
  HOW TO CHECK: PLAN-2 must be working and tested.
  USE IF: PLAN-2 is in place. Confidence-as-input is low-cost, high-value — just a
    mapping function from 0.0-1.0 to ratio weights.
  DON'T USE IF: PLAN-2 is not yet implemented — presets have nothing to set.
  IF CONDITION UNKNOWN: Implement PLAN-2 first.
  FIRST ACTIONS:
    1. Add --confidence arg with linear mapping to ratio — resolves R7
    2. Add 3-5 domain presets (safety, brainstorm, balanced, exploratory) — resolves R13
    3. Document that --ratio overrides --confidence and --domain — resolves R35
```

---

```
RECOMMENDATION SUMMARY
======================

SOURCE: /ar on configurable AR/AW ratios (4x) + /ar on UAUA support (2x)

RECOMMENDED:
- PLAN-1: Build search type registry (AR/AW/U) — USE IF: implementing any configurability
- PLAN-2: Implement ratio-mixing scheduling — USE IF: PLAN-1 is built

CONDITIONALLY RECOMMENDED:
- PLAN-3: UAUA sequential scheduling — CONDITION: U-phase prompt produces usable output (test 20 nodes)
- PLAN-5: Domain presets / confidence input — CONDITION: PLAN-2 is working

NOT RECOMMENDED:
- PLAN-4: Auto-adjustment (bandit) — BECAUSE: no quality metric exists
  WOULD CHANGE IF: validated branch quality metric defined and tested

SUGGESTED SEQUENCE:
1. Build search type registry with AR, AW, U types [PLAN-1]
2. Implement ratio-mixing scheduling (--ratio, leverage adjustment, mid-search changes) [PLAN-2]
3. Test U-phase prompt quality (20 manual expansions) [PLAN-3 prerequisite]
4. If U-quality passes: implement UAUA sequential scheduling [PLAN-3]
   If U-quality fails: use ratio-mixing with U proportion (e.g., 40:30:30) as fallback
5. Add --confidence and domain presets [PLAN-5]
6. Defer auto-adjustment until a quality metric is defined [PLAN-4 parked]

WHAT THIS ANALYSIS DOES NOT COVER:
- The actual U-phase prompt engineering (what specific prompt produces good universalizations)
- Whether leverage adjustment or explicit two-queue performs better (R22 — needs empirical test)
- Specific domain preset values beyond directional (safety=AW-heavy, brainstorm=AR-heavy)
- Performance impact of additional SQLite queries for phase state and queue filtering
- UI/UX for communicating ratio changes to users during long runs
```
