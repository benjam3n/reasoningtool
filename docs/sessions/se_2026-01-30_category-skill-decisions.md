# SE 4x — Decisions Each Category Skill Makes

**Date**: 2026-01-30
**Depth**: 4x
**Input**: figure out what sorts of decisions each category skill needs to make

---

## Universal Decisions (All Sub-Orchestrators)

```
D1. DEPTH: How deep should the analysis go? (1x/2x/4x/8x — infer from input complexity)
D2. SCOPE: Single thing or compound input? If compound, split or handle as one?
D3. CONTEXT: Enough context provided or needs clarification?
D4. PRIOR WORK: Continuation of previous analysis? What exists already?
D5. OUTPUT FORMAT: User wants analysis, a decision, a plan, or just an answer?
```

---

## Per-Category Decisions

### /claim — ARAW mode

```
C1. Extract the testable proposition
C2. Is it actually a claim? (or disguised decision/feeling/question)
    - IF looks like a decision → route to /decide
    - IF looks like a feeling → route to /emotion
    - IF looks like a question → route to /search
C3. Single claim or bundled?
C4. Is the claim testable?
    - IF untestable/definitional → unpack what it would MEAN, then test the meaning
C5. What depth? (infer from input complexity)
C6. AR/AW balance: default 50/50
    - User says "I believe X" → push AW harder (60% AW)
    - User says "I doubt X" → push AR harder (60% AR)
    - User says "is X true?" → balanced 50/50

INVOKES: → /araw [claim] at determined depth
ALSO: → /aex if many hidden assumptions, → /ht if hypothesis-shaped
```

### /decide — ARAW mode

```
C7. Extract the choice point
C8. How many options? (binary / multi / open)
    - Binary → ARAW on doing X vs not doing X
    - Multi → /cmp first, then ARAW on top candidates
    - Open → /se to enumerate options first, then /cmp
C9. Are criteria known?
    - Yes → /cmp with stated criteria
    - No → /want to clarify what they want, THEN decide
C10. Is it reversible? (stakes determine depth)
    - Reversible → lighter analysis, /cmp sufficient
    - Irreversible → deeper analysis, ARAW + /prm + /fla
C11. Is it actually a decision? (or disguised claim/goal/vent)

INVOKES: → /cmp if multi-option with known criteria
          → /araw if binary
          → /dcp if recurring decision needs a procedure
          → /gu if criteria unknown
```

### /diagnose — UAUA mode

```
C12. Extract the symptom
C13. Is the cause known, suspected, or unknown?
    - Known → actually a CLAIM about causation → /claim
    - Suspected → test hypothesis → /ht or ARAW on "X causes the problem"
    - Unknown → UAUA to map possible causes, then test each
C14. Technical or non-technical?
    - Technical → /dbg, /rca with technical framing
    - Non-technical → /rca, /fowwr with systems framing
C15. Is there a timeline? What changed?
    - Clear timeline → /fowwr
    - No timeline → /uaua to map then /rca
C16. Has this been diagnosed before? Recurring?
    - First time → full diagnosis
    - Recurring → /sbfow (still bad, figure out why)
C17. Single cause or systemic?
    - Isolated → /rca
    - Pattern → /sya (systems analysis)

INVOKES: → /uaua if cause unknown
          → /rca if ready for direct causal tracing
          → /fowwr if something specific broke
          → /sbfow if previous fix didn't work
```

### /search (explore) — UAUA mode

```
C18. What is the space being explored?
    - Option space / landscape space / factor space / knowledge space
C19. How much is already known?
    - Nothing → full UAUA
    - Some → /se to enumerate missing, then ARAW on discoveries
    - A lot → probably /evaluate or /claim instead
C20. Completeness criterion?
    - Exhaustive → /se EXHAUSTIVE, then UAUA on top findings
    - Representative → /se REPRESENTATIVE, then ARAW on top 3-5
    - Quick → /se TOP-N, lighter testing
C21. Actually exploration or disguised goal/decision?
    - "What are my options for..." often = "help me decide" → /decide after exploration
    - "What should I do about..." = goal-stating → /want
C22. Explore-then-what?
    - Explore → decide: /se → /cmp → /decide
    - Explore → test: /se → /araw on most interesting findings
    - Explore → build: /se → /how for the chosen option

INVOKES: → /uaua for full explore-then-test
          → /se if just mapping needed
          → /dd if dimensions need discovering
          → /u for pure universalization
```

### /how (method) — AR-forward mode

```
C23. Extract the goal
C24. Is the goal well-defined?
    - Well-defined → proceed to method discovery
    - Vague → /want to clarify, then return
C25. Are constraints known?
    - Yes → method search within constraints
    - No → ask or explore unconstrained first
C26. Single method or full plan?
    - Single method → /foht
    - Multi-step → /foht → /stg → /to
C27. Is the how actually known? (maybe just needs steps)
    - Method unknown → /foht to discover
    - Method known, steps unknown → /stg or /op
    - Both known → /action

INVOKES: → /foht for method discovery
          → /stg for step generation
          → /br for backward reasoning
          → /op for ordering steps
```

### /want (goal) — AR-forward mode

```
C28. Extract the want
C29. Is it the real want or a proxy?
    - ALWAYS trace deeper via /wt implication chain
C30. Is this a goal or a decision?
    - Goal → /wt
    - Decision → /decide
C31. Are prerequisites known?
C32. Actionable or aspirational?
    - Actionable → /wt → /how → /action
    - Aspirational → /wt to trace what it means, then /gu

INVOKES: → /wt for full want analysis
          → /gu for goal understanding
          → /gd for goal decomposition
```

### /action (command) — Non-analytical mode

```
C33. Extract the action
C34. Executable or needs analysis first?
    - Executable → do it
    - Too vague → /diagnose or /want first
C35. Maps to a specific skill?
    - "Compare" → /cmp, "Write" → /create, "Debug" → /diagnose, "Plan" → /how, "Review" → /evaluate
C36. Single step or multi-step?
    - Single → direct execution
    - Multi → /stg → /to → execute each
C37. Wants options or just execution?
    - Options → reroute to /how or /search
    - Execution → execute with best judgment

INVOKES: → direct execution for simple commands
          → /stg for multi-step plans
          → reroutes when command is actually a question
```

### /evaluate — ARAW mode

```
C38. Extract the thing being evaluated
C39. What kind of evaluation?
    - Correctness → /araw on core claims
    - Completeness → /mv or /se
    - Quality → /pv or /val
    - Assumptions → /aex
    - Risks → /fla or /prm
C40. Standard to evaluate against?
    - Yes → check against standard
    - No → needs criteria first → /crw or ask user
C41. Whole or part?
C42. Self-evaluation or external?
    - Self → more adversarial (check confirmation bias)
    - External → balanced

INVOKES: → /araw for correctness
          → /mv for MECE checks
          → /pv for procedure validation
          → /aex for assumptions
          → /fla for risks
```

### /emotion — AR-forward mode

```
C43. Identify the emotion (frustration / overwhelm / stuck / doubt / excitement)
C44. Implicit request behind the emotion?
    - Frustration → /diagnose
    - Overwhelm → /how or /dcm (break it down)
    - Stuck → /how (find new approaches)
    - Doubt → /claim (test the belief) + /want
    - Excitement → /viability
C45. Acknowledge first or route directly?
    - High emotion → acknowledge first, then route
    - Low emotion → route directly
    - RULE: Always acknowledge briefly before routing
C46. About the problem, themselves, or the process?
    - Problem → /diagnose
    - Themselves → /claim (test belief) + /want
    - Process → /evaluate

INVOKES: → acknowledge emotion, THEN route to appropriate category
```

### /viability (idea) — ARAW mode

```
C47. Extract the idea/proposal
C48. Idea or claim? (viability vs truth)
    - Ideas tested for VIABILITY, claims tested for TRUTH
C49. How developed?
    - Seed → /ar first to develop, THEN /aw
    - Developed → ready for ARAW
    - Fully formed → /evaluate instead
C50. Risk profile?
    - Low risk → lighter analysis
    - High risk → deep ARAW + /prm + /fla
C51. Needs comparison to alternatives?
    - Yes → /decide
    - No → ARAW on viability

INVOKES: → /ar to develop underdeveloped ideas
          → /araw to test developed ideas
          → /prm + /fla for high-risk ideas
```

### /meta — Informational mode

```
C52. What do they want to know? (available skills / comparison / usage / general help)
C53. Need a skill or information?
C54. Can we infer what they actually need?
    - "Help" with context → route based on context
    - "Help" without context → ask what they're working on
```

### /create — Non-analytical mode

```
C55. Content type? (writing / narrative / proposal / technical)
C56. Quality standard?
C57. Needs analysis first? ("Write a market analysis" → /mr FIRST, then /create)
C58. Options or one output?

INVOKES: → /w or /pw for writing
          → /stl for narrative
          → /gw for proposals
```

### /technical — Router mode

```
C59. Domain? (software / business / marketing / finance / career / research / planning)
C60. Task type within domain? (build / fix / evaluate / plan)
C61. Too specific for general category? → invoke domain skill directly

INVOKES: → domain-specific skills based on C59 × C60
```

### /analysis — Router mode

```
C62. Kind of analysis? (causal / structural / comparative / risk / data / strategic)
C63. Thing or situation?
    - Thing → /evaluate is better fit
    - Situation → route to analytical skill
C64. Decomposition or synthesis?
    - Decomposition → /dcm
    - Synthesis → /ins
    - Both → /dcm then /ins
```

### /certainty — Maximum effort mode

```
C65. What is the question to resolve?
C66. What does "resolved" mean? (factual / analytical / decision)
C67. Starting mode? (classify via taxonomy → appropriate category)
C68. When to escalate? (unresolved branches → explore; untested assumptions → test;
     competing conclusions → stress-test)
C69. How to chain? (explore → claim/evaluate → diagnose contradictions → synthesize →
     evaluate synthesis → loop until satisfied)

INVOKES: → starts with appropriate category at 8x
          → chains through multiple skills iteratively
          → uses /evaluate between iterations
          → continues until resolution criteria met
```

---

## Key Patterns

- Every category asks "is this actually MY category?" — self-correcting reclassification
- 4 analytical modes: ARAW-balanced (claim, decide, evaluate, viability), UAUA-exploratory (diagnose, search), AR-forward (emotion, how, want), Non-analytical (action, create, meta)
- ARAW = you HAVE a specific thing to test. UAUA = you DON'T have the thing yet, discover then test.

## Metadata

- Total categories: 15
- Total decisions: 69 category-specific + 5 universal = 74
- Cross-dimensional overlaps: 5 identified with resolution rules
