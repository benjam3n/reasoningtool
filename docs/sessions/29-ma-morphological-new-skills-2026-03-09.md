# /ma Generate new skill ideas by crossing domain × mode
**Date:** 2026-03-09
**Skill:** /ma (Morphological Analysis)

---

## Interpretation

**Interpretation 2 — Creative unblocking.** The user wants forced combinations across structured dimensions to surface novel skill ideas that 592 existing skills have not yet covered.

**Depth**: 2x (default) — 4 dimensions, 4+ options each, 10+ combinations evaluated, 2+ cross-dimension interactions analyzed.

---

## Step 1: Problem Statement

Generate novel, non-redundant thinking skill concepts for the Reasoning Toolkit by systematically crossing independent dimensions of skill design. Each viable combination should name a skill that does not substantially duplicate any of the 592 existing skills.

---

## Step 2: Independent Dimensions

| # | Dimension | Why independent | Why variable |
|---|-----------|----------------|--------------|
| 1 | **Domain** | What life-area the skill addresses | Personal, professional, creative, analytical contexts each produce different inputs and success criteria |
| 2 | **Mode** | How the skill engages with the input | Exploratory (open search), evaluative (judge quality), generative (produce new output), corrective (fix what's broken) are orthogonal cognitive stances |
| 3 | **Scope** | The grain-size the skill operates at | Single-item, comparison (2 items), portfolio (many items), system (interconnected whole) — determines what the skill takes in and puts out |
| 4 | **Temporality** | The time-orientation of the skill | Past-facing (retrospective/forensic), present-facing (situational), future-facing (projective), timeless (structural/abstract) — determines the lens |

---

## Step 3: Values for Each Dimension

| Dimension | Values |
|-----------|--------|
| **Domain** | Personal (P) · Professional (W) · Creative (C) · Analytical (A) |
| **Mode** | Exploratory (x) · Evaluative (v) · Generative (g) · Corrective (r) |
| **Scope** | Single (1) · Comparison (2) · Portfolio (n) · System (s) |
| **Temporality** | Past (←) · Present (•) · Future (→) · Timeless (∞) |

---

## Step 4: Morphological Box

```
              Exploratory (x)    Evaluative (v)    Generative (g)    Corrective (r)
           ┌──────────────────┬──────────────────┬──────────────────┬──────────────────┐
Personal   │  P-x             │  P-v             │  P-g             │  P-r             │
           ├──────────────────┼──────────────────┼──────────────────┼──────────────────┤
Profession │  W-x             │  W-v             │  W-g             │  W-r             │
           ├──────────────────┼──────────────────┼──────────────────┼──────────────────┤
Creative   │  C-x             │  C-v             │  C-g             │  C-r             │
           ├──────────────────┼──────────────────┼──────────────────┼──────────────────┤
Analytical │  A-x             │  A-v             │  A-g             │  A-r             │
           └──────────────────┴──────────────────┴──────────────────┴──────────────────┘

Each cell above further crosses with Scope (1/2/n/s) and Temporality (←/•/→/∞).
```

---

## Step 5: Combination Count

4 domains × 4 modes × 4 scopes × 4 temporalities = **256 total combinations.**

256 is manageable with constraint filtering. We will prune aggressively and surface the 10–15 most novel, non-redundant combinations.

---

## Step 6: Constraint Filter

**Eliminated categories (substantially covered by existing skills):**

| Combination space | Already covered by | Status |
|---|---|---|
| A-v (Analytical × Evaluative), any scope/time | `/pv`, `/mv`, `/vbo`, `/skev`, `/vldt`, `/fwa` | COVERED — skip |
| A-x (Analytical × Exploratory), single, present | `/se`, `/dd`, `/frq`, `/ipss` | COVERED — skip |
| W-v (Professional × Evaluative), single, present | `/evaluate`, `/cmp`, `/dcp` | COVERED — skip |
| P-r (Personal × Corrective), single, present | `/rmm`, `/kta`, `/reframe`, `/sbfow` | COVERED — skip |
| A-g (Analytical × Generative), single, timeless | `/ma` (this skill!), `/cda`, `/gg` | COVERED — skip |
| C-g (Creative × Generative), single, present | `/pw`, `/stl`, `/w`, `/draft`, `/story` | COVERED — skip |
| A-r (Analytical × Corrective), single, present | `/rca`, `/dbg`, `/diagnose` | COVERED — skip |
| W-x (Professional × Exploratory), single, present | `/cd`, `/mr`, `/jss`, `/lr` | COVERED — skip |
| P-x (Personal × Exploratory), single, present | `/eg`, `/gu`, `/gd` | COVERED — skip |

**Surviving combination space**: ~140 combinations. Sampling the most promising.

---

## Step 7: Evaluate Viable Combinations

### Tier 1: High novelty, clearly unserved

| # | Combination | Proposed Skill | Description | Feasibility | Novelty |
|---|-------------|---------------|-------------|-------------|---------|
| 1 | **P-g-n-←** Personal × Generative × Portfolio × Past | `/lifearc` — Life Arc Synthesis | Given a portfolio of past experiences (jobs, relationships, projects), generate the narrative arc — recurring themes, hidden patterns, inflection points. Produces a synthesized "story of you" that reveals what you've actually been optimizing for. | High | **High** — no existing skill synthesizes a personal history into a coherent generative narrative |
| 2 | **W-x-s-→** Professional × Exploratory × System × Future | `/orgfut` — Organizational Futures Exploration | Map the system of forces acting on a team/org (market, talent, tech, regulation) and explore where the system is heading. Not forecasting a single outcome but mapping the phase space of plausible organizational futures. | High | **High** — `/fut` is generic; no skill explores organizational systems specifically |
| 3 | **C-r-1-•** Creative × Corrective × Single × Present | `/unstyl` — Style Repair | Take a piece of creative work that "isn't working" and diagnose the specific stylistic failure (tonal inconsistency, register mismatch, rhythm collapse, structural sag). Then prescribe targeted corrections. Not rewriting — isolating the craft-level defect. | High | **High** — `/wre` edits for clarity; nothing diagnoses *style failure* as a corrective procedure |
| 4 | **P-v-n-→** Personal × Evaluative × Portfolio × Future | `/lifeaudit` — Future-Facing Life Portfolio Audit | Evaluate your current portfolio of commitments (relationships, projects, habits, investments of time) against where you want to be in 5 years. Score each commitment on trajectory-alignment. Surface the ones that are coasting, deadweight, or actively pulling you off-course. | High | **High** — `/pv` validates work output; nothing evaluates a life-portfolio against a future self |
| 5 | **A-x-s-←** Analytical × Exploratory × System × Past | `/postmorph` — Systemic Post-Mortem Exploration | After a complex failure, explore the *system* that produced it — not just the root cause (that's `/rca`) but the full landscape of contributing factors, feedback loops, and structural conditions. Map which were necessary vs. sufficient vs. amplifying. | High | **High** — `/rca` finds *the* root cause; this explores the full failure ecology |
| 6 | **C-x-2-∞** Creative × Exploratory × Comparison × Timeless | `/stylecross` — Cross-Style Exploration | Take two creative styles, genres, or traditions and systematically explore the space between them. What would film noir × bossa nova produce? Brutalist architecture × haiku? Maps the combination space structurally rather than just mashing them together. | High | **High** — `/anag` generates analogies; nothing systematically explores inter-style spaces |
| 7 | **W-g-s-•** Professional × Generative × System × Present | `/procgen` — Process Generation from System State | Given a description of how work currently flows through a system (team, pipeline, org), generate new process designs that resolve observed bottlenecks. Not optimization of existing process — generation of structurally different alternatives. | High | **High** — `/to` orders tasks; nothing generates *new process architectures* from system state |
| 8 | **P-x-s-•** Personal × Exploratory × System × Present | `/lifesys` — Personal System Mapping | Map the system of your current life — how your energy, time, relationships, health, work, and finances interconnect. Identify feedback loops (positive and negative), leverage points, and hidden couplings. Not goal-setting — system-seeing. | High | **High** — `/sysk` does systems analysis for external systems; nothing turns that lens inward |
| 9 | **C-v-n-←** Creative × Evaluative × Portfolio × Past | `/bodywork` — Body of Work Evaluation | Evaluate a portfolio of creative work (all your essays, paintings, songs, projects) as a *body*. What's the through-line? Where did you peak? Where did you repeat yourself? What's missing from the collection? Evaluates the portfolio, not individual pieces. | High | **High** — no skill evaluates creative output as a retrospective corpus |
| 10 | **W-r-n-→** Professional × Corrective × Portfolio × Future | `/careerfix` — Career Portfolio Correction | Given a portfolio of professional skills, experiences, and credentials, identify what's misaligned with where the market/field is heading. Prescribe specific corrections: skills to acquire, experiences to seek, credentials to drop, bets to place. | High | **High** — `/jss` does job search; nothing corrects a career portfolio against future trajectories |
| 11 | **A-g-2-→** Analytical × Generative × Comparison × Future | `/scenfork` — Scenario Fork Generation | Given two possible futures (or two strategies), generate the specific decision points where they diverge. Produce a forking-path map showing exactly which choices lead to which outcome. The output is a decision tree you can actually use. | Med-High | **High** — `/dcp` decides; `/fut` forecasts; nothing generates the fork-point structure between two futures |
| 12 | **P-r-s-←** Personal × Corrective × System × Past | `/patternbreak` — Personal Pattern Correction | Identify a recurring negative pattern in your life history (the same relationship dynamic, the same project failure mode, the same avoidance behavior). Trace it to its systemic root. Design a structural intervention, not a willpower-based one. | High | **High** — `/rmm` corrects mental models; nothing corrects recurring life patterns systemically |

---

## Step 8: Cross-Dimension Interactions

### Interaction 1: Scope × Temporality amplification

The most novel skills emerge at **portfolio (n) or system (s) scope** combined with **non-present temporality (← or →)**. This is because most existing skills operate at **single-item × present** — they take one thing and analyze it now. The moment you ask "evaluate my portfolio of X against the future" or "explore the system that produced this past outcome," you leave the territory covered by the existing 592 skills.

**Implication**: Prioritize new skills at portfolio/system scope with past or future orientation.

### Interaction 2: Domain × Mode creates "character" archetypes

Each domain × mode pairing implies a different persona:
- **Personal × Exploratory** = the self-discoverer (partially covered)
- **Personal × Generative** = the life-designer (UNDERCOVERED)
- **Creative × Corrective** = the craft doctor (UNDERCOVERED)
- **Professional × Generative at system scope** = the org architect (UNDERCOVERED)

**Implication**: The toolkit has strong coverage of the "analytical evaluator" and "personal corrector" archetypes but weak coverage of life-designers, craft doctors, and organizational architects.

---

## Step 9: Top Selections (Shortlisted for Development)

Ranked by (Novelty × Feasibility × Demand likelihood):

| Rank | Skill | Combination | Why top-pick |
|------|-------|-------------|-------------|
| **1** | **`/lifesys` — Personal System Mapping** | P-x-s-• | Universally useful. Everyone has a life; almost no one maps it as a system. Leverages the toolkit's existing systems analysis strength (`/sysk`, `/fohw`) turned inward. |
| **2** | **`/patternbreak` — Personal Pattern Correction** | P-r-s-← | High emotional resonance. Addresses a pain point (recurring failures) that most people recognize but lack tools for. Structural intervention > willpower is a powerful frame. |
| **3** | **`/unstyl` — Style Repair** | C-r-1-• | Fills a clear gap for writers and creators. The existing writing skills generate or edit; nothing *diagnoses craft failure*. Could become a go-to for "why isn't this working?" |
| **4** | **`/bodywork` — Body of Work Evaluation** | C-v-n-← | Unique and resonant for anyone with 5+ years of creative output. No tool does this. |
| **5** | **`/lifeaudit` — Future-Facing Life Portfolio Audit** | P-v-n-→ | Practical, high-demand. "Am I spending my time on the right things?" is a perennial question. |
| **6** | **`/postmorph` — Systemic Post-Mortem Exploration** | A-x-s-← | Professional teams need this constantly. Goes beyond root cause to map full failure ecology. |
| **7** | **`/scenfork` — Scenario Fork Generation** | A-g-2-→ | Decision-support with high visual/structural output. Produces an artifact (fork-point map) that other skills don't. |
| **8** | **`/lifearc` — Life Arc Synthesis** | P-g-n-← | Deeply personal, potentially transformative. "What have I actually been optimizing for?" is a question most people cannot answer. |
| **9** | **`/procgen` — Process Generation** | W-g-s-• | High professional utility. Organizations constantly need new process architectures, not just optimized old ones. |
| **10** | **`/stylecross` — Cross-Style Exploration** | C-x-2-∞ | Niche but powerful for creative practitioners. No other tool does systematic inter-style exploration. |

---

## Verification Checklist

- [x] Dimensions are independent (domain, mode, scope, and temporality can vary without forcing changes in each other)
- [x] Values are mutually exclusive within each dimension (a skill can't be both exploratory and evaluative as its primary mode)
- [x] Values are exhaustive (the four values in each dimension cover the space reasonably)
- [x] Combination count is correct (4 × 4 × 4 × 4 = 256)
- [x] Constraints are justified (eliminations reference specific existing skills)
- [x] Evaluation criteria are clear (feasibility, novelty, demand likelihood)

---

## Summary

The morphological box reveals that the Reasoning Toolkit's 592 skills cluster heavily in the **single-item × present × analytical/evaluative** quadrant. The largest gaps are:

1. **Personal × system scope** — treating your own life as a system rather than a series of isolated problems
2. **Creative × corrective** — diagnosing craft-level failures rather than just editing
3. **Portfolio scope × non-present temporality** — evaluating collections of things against past patterns or future trajectories
4. **Professional × generative × system** — creating new organizational processes rather than optimizing existing ones

The 10 shortlisted skills above exploit these gaps. The top 3 recommendations for immediate development are `/lifesys`, `/patternbreak`, and `/unstyl`.
