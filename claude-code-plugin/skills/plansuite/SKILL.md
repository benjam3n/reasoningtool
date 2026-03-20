---
name: "plansuite - Full Planning Suite"
description: Run a comprehensive planning suite (want, sysarch, de, riskmgmt, spec, tradestudy, action, fla, conops) for any project, producing a detailed session-level planning document with concrete artifacts.
output:
  format: "document"
---

# Full Planning Suite

**Input**: $ARGUMENTS

---

## Interpretations

Before executing, identify which interpretation matches the user's input:

**Interpretation 1 — Plan a new project from scratch**: The user has a project idea and wants a complete plan before building. Run the full suite.
**Interpretation 2 — Plan the next phase of an existing project**: The user has a project in progress and wants to plan the next major phase. Run the suite with current-state analysis first.
**Interpretation 3 — Re-plan a stalled or troubled project**: The user has a project that's stuck, over-scoped, or off-track and wants to re-plan from current reality. Run the suite with honest baseline assessment.

If ambiguous, ask: "I can help with planning a new project, planning the next phase of an existing one, or re-planning something that's stuck — which fits?"
If clear from context, proceed with the matching interpretation.

---

## Depth Scaling

Default: 8x. Parse depth from $ARGUMENTS if specified (e.g., "/plansuite 2x [input]").

| Depth | Skills Run | Min Risks | Min Trade Studies | Min Failure Modes | Min Operational Scenarios |
|-------|-----------|-----------|-------------------|-------------------|--------------------------|
| 1x    | want, sysarch, action | 5 | 2 | 5 | 3 |
| 2x    | want, sysarch, de, action | 10 | 3 | 10 | 5 |
| 4x    | want, sysarch, de, riskmgmt, tradestudy, action | 20 | 4 | 20 | 8 |
| 8x    | want, sysarch, de, riskmgmt, spec, tradestudy, action, fla, conops | 30+ | 5+ | 30+ | 12+ |
| 16x   | all 8x skills + /pv + /iterate | 40+ | 7+ | 40+ | 16+ |

---

## The Process

### Pre-Step: Domain Discovery

Before running any skills, understand the domain the user is working in. This step adapts to any project type.

1. **If the project exists**: Read CLAUDE.md, README.md, or equivalent. Check git log for activity. Identify tech stack from config files. Determine current state (shipped, in-progress, planned, stalled). Find existing artifacts (docs, sessions, tests, demos).
2. **If the project is new**: Identify the domain, target users, constraints, and any prior art the user references.
3. **If multiple components/subprojects exist**: Inventory each one with its state and relationships.

```
DOMAIN INVENTORY:

| # | Component | What It Does | Tech/Method | State | Key Artifacts |
|---|-----------|-------------|-------------|-------|---------------|
| 1 | [name]    | [1-line]    | [stack]     | [state] | [artifacts] |
...

CONSTRAINTS:
- [Time, budget, team size, technical, regulatory, etc.]

PRIOR ART / REFERENCE PROJECTS:
- [What the user has referenced or what exists in this space]
```

This inventory feeds every downstream skill. Do not skip it.

---

### Skill 1: /want — Want Tracing

→ INVOKE: /want $ARGUMENTS

Apply want tracing to the project goal. The finding registry must address:

- **Surface wants**: What does the user explicitly say they want?
- **Implicit wants**: What do they want that they haven't stated? (learning, status, fun, control, revenue?)
- **Anti-wants**: What should this project NOT become?
- **Beliefs**: What assumptions is the user making about feasibility, approach, or value?
- **Crux**: What is the single thing that would make or break this project?

Output format:
```
UNBUNDLED WANT:
[G1] ... -- TYPE: desire
[G2] ... -- TYPE: method
[G3] ... -- TYPE: belief
[G4] ... -- TYPE: assumption
[G5] ... -- TYPE: implicit want
[G6] ... -- TYPE: anti-want
...

ACTUAL WANT:
[G2x] ... -- CONFIDENCE: high/moderate/low

CRUX:
[G7x] ...
[G7x+1] Resolve by: ...
```

### Synthesis

```
STATED WANT: [what the user said]
ACTUAL WANT: [what they actually need, with confidence]

FIRST ACTIONS:
1. [Crux-resolving action]
2. [Highest-leverage technical action]
3. [Lowest-risk starting point]
```

---

### Skill 2: /sysarch — System Architecture

→ INVOKE: /sysarch $ARGUMENTS

Design the system architecture. Must produce:

1. **Candidate architectures**: At minimum 3-5 viable approaches, tailored to the domain
2. **Scoring matrix**: Weighted criteria evaluated for each candidate
3. **Selected architecture**: Winner with score comparison
4. **File system / component layout**: Concrete structure
5. **Key design decisions**: Numbered list, each as "X over Y (reason)"

Adapt the candidates and criteria to the project domain:
- Software project → framework, database, deployment architecture
- Content project → format, organization, generation pipeline
- Hardware/physical → components, interfaces, fabrication approach
- Process/workflow → tooling, stages, handoff points
- Research → methodology, data sources, analysis pipeline

---

### Skill 3: /de — Dependency Extraction

→ INVOKE: /de [all tasks from architecture]

Extract dependencies across all build tasks. Must produce:

- **Full task list** (numbered T0-TN across stages)
- **Critical path** (chain notation: T0->T2->T5->...)
- **Parallel groups** (Group A: {T0, T3}, Group B: ...)
- **Conditional branches** (If X fails -> Y becomes critical path)

---

### Skill 4: /riskmgmt — Risk Management

→ INVOKE: /riskmgmt $ARGUMENTS

Identify risks across all categories relevant to the project:

- **External risks**: Dependencies on third parties, APIs, platforms, regulations
- **Technical risks**: Feasibility unknowns, integration challenges, performance
- **Process risks**: Over-engineering, scope creep, perfectionism, abandonment
- **Domain risks**: Market, user adoption, competitive, legal
- **Resource risks**: Time, money, expertise, burnout

Output format:
```
Risk Register Summary
Total: N risks | Critical: X | High: Y | Medium: Z | Low: W

Top risks table:
| Risk | RPN Score | Mitigation | Post-Mitigation RPN |

Day-1 actions that resolve top risks: [list]
```

---

### Skill 5: /spec — Speculative Analysis

→ INVOKE: /spec [can this project succeed given the constraints?]

Assess plausibility of the plan. Must address:

- **Key assumptions** with individual probability estimates
- **Time/resource budget**: How long to build? To maintain?
- **Size budget**: LOC, file count, component count — concrete caps
- **Weakest link**: Which assumption is most likely to fail?
- **Verdict**: Build it / Simplify first / Rethink approach / Kill it

```
SPECULATION: [one-sentence claim about feasibility]
PLAUSIBILITY RATING: [LOW / MODERATE / MODERATE-HIGH / HIGH]

Weakest link: [which assumption] at [X%]

VERDICT: [decision + reasoning]
```

---

### Skill 6: /tradestudy — Trade Studies

→ INVOKE: /tradestudy [key technology/approach decisions]

Run trade studies on every significant decision point identified in sysarch. Minimum 5 decisions evaluated.

For each decision:
- At least 3 candidates
- Weighted scoring criteria
- Winner, Runner-Up, Confidence level

Output: Decision matrix:
```
| Decision | Winner | Runner-Up | Confidence |
|----------|--------|-----------|-----------|
```

Plus combined stack / approach summary.

---

### Skill 7: /action — Execution Plan

→ INVOKE: /action [build the project]

Produce a concrete execution plan. Must include:

- **Phased delivery**: What ships first? What comes in later phases?
- **Session-by-session or day-by-day tasks** with specific deliverables per unit of time
- **Success criteria**: How do you know each phase is done?
- **Hard deadlines or forcing functions**: What prevents indefinite building?

---

### Skill 8a: /fla — Failure Anticipation

→ INVOKE: /fla $ARGUMENTS

Identify failure modes. Must include:

- **Failure modes** with RPN scoring (likelihood × impact × detectability)
- **Critical failures** (RPN > 200): table with ID, failure, RPN, post-mitigation RPN
- **Cascade failure chains**: sequences where one failure triggers others
- **Kill criteria**: concrete thresholds for stopping, simplifying, or pivoting

---

### Skill 8b: /conops — Concept of Operations

→ INVOKE: /conops $ARGUMENTS

Define how the project operates after initial build. Must include:

- **Mission statement**: One sentence
- **Operational scenarios**: Numbered list covering normal use, maintenance, edge cases, evolution, and shutdown
- **Operational modes**: State machine (e.g., NORMAL -> DEGRADED -> MAINTENANCE -> DORMANT)
- **Key success criteria**: Measurable signals that the project is working

---

## Session Document Output

All output goes into a session document at:
```
docs/sessions/plansuite_[YYYY-MM-DD]_[descriptive-title].md
```

The document must follow the session format:

```markdown
# [Title] — Full Planning Suite

**Date**: [YYYY-MM-DD]
**Depth**: [Nx]
**Skills Used**: /want, /sysarch, /de, /riskmgmt, /spec, /tradestudy, /action, /fla, /conops ([count] skills, [count] invocations)
**Input**: [user's original input]

---

## Domain Inventory

[Pre-step output]

---

## Skill 1: /want — Want Tracing ([depth])

[Full output including Finding Registry and Synthesis]

---

## Skill 2: /sysarch — System Architecture ([depth])

[Full output including scoring matrix, layout, design decisions]

---

[... remaining skills ...]

---

## Summary: What to Do

### Before Writing Any Code
[Prioritized pre-build actions that resolve top risks and cruxes]

### Build Order
[Sequenced build plan from dependency extraction]

### The Most Important Thing
[The behavioral/strategic insight that matters more than any technical decision —
what will actually determine success or failure]
```

---

## When to Use

- User has a project idea and wants a comprehensive plan before building
- User wants the same rigor as the SAIS planning doc for their project
- User needs to go from fuzzy idea to concrete build plan in one session
- User wants structured risk assessment, architecture evaluation, and execution planning
- User says "plan this", "figure out how to build this", or "give me the full treatment"

---

## Verification Checklist

Before delivering the session document, verify:

- [ ] Domain inventory is complete — every component/subproject accounted for
- [ ] Want tracing found implicit wants and anti-wants, not just restated the input
- [ ] Architecture decision is justified with scoring matrix, not vibes
- [ ] Critical path is identified and conditional branches have fallbacks
- [ ] Top risks have concrete mitigations with post-mitigation RPN scores
- [ ] Spec includes a plausibility verdict with explicit weakest-link analysis
- [ ] Trade studies cover at least 5 decisions with 3+ candidates each
- [ ] Build plan has specific deliverables per phase, not vague goals
- [ ] Failure modes include cascade chains and kill criteria
- [ ] ConOps addresses ongoing operations, not just initial build
- [ ] "The Most Important Thing" identifies the real constraint — usually behavioral, not technical
- [ ] Total document is actionable: someone could start building from it today
