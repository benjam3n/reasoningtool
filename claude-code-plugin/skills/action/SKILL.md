---
name: "action - Execute a Command"
description: Sub-orchestrator for commands and action requests. Routes to direct execution, step generation, task sequencing, or reclassifies when the command needs analysis first.
output:
  format: "prose"
---

# Action

**Input**: $ARGUMENTS

---

## Interpretations

Before executing, identify which interpretation matches the user's input:

**Interpretation 1 — Direct command**: The user wants a specific thing done now ("Write a summary", "List the pros and cons").
**Interpretation 2 — Multi-step task**: The user wants something done that requires planning ("Build a deployment pipeline", "Set up the project").
**Interpretation 3 — Continuation**: The user wants to continue from where we left off ("Do next", "Continue", "Keep going").
**Interpretation 4 — Vague directive**: The user gives a broad instruction that needs decomposition before execution ("Fix this", "Make it better", "Handle this").

If ambiguous, ask: "Should I execute this directly, or does it need planning first?"
If clear from context, proceed with the matching interpretation.

---

## Core Principles

1. **Action requires clarity.** If the command is vague, clarify before executing. Executing the wrong thing wastes more time than asking.

2. **Not every command is ready for execution.** Many "do this" requests actually need analysis, diagnosis, or goal clarification first. Route accordingly.

3. **Multi-step actions need ordering.** Don't start executing until dependencies are mapped and steps are sequenced.

4. **Execution includes adjacent tasks.** The user often forgets implied prerequisites and follow-up tasks. Surface them.

---

## Routing Decisions

### 1. Extract the Action

What does the user want done? State it as a verb + object. "Write a business plan" / "Compare X and Y" / "Fix this code" / "Do next" / "Continue".

### 2. Is This Actually a Command?

- **"What are my options?"** → This is exploration. → INVOKE: /search $ARGUMENTS
- **"How should I approach this?"** → This is method-seeking. → INVOKE: /how $ARGUMENTS
- **"Is this good?"** → This is evaluation. → INVOKE: /evaluate $ARGUMENTS
- **"I want to X"** → This is a goal. → INVOKE: /want $ARGUMENTS
- **"I think I should X"** → Formalize the belief. → INVOKE: /it $ARGUMENTS
- **"I should X, but Y"** → Tension between action and obstacle. → INVOKE: /but $ARGUMENTS
- **"I'm not sure what to do"** → Classify the uncertainty. → INVOKE: /nsa $ARGUMENTS
- **"Handle this"** (maximally vague) → INVOKE: /handle $ARGUMENTS
- **If it IS a command** → continue.

### 3. Is It Executable or Does It Need Analysis?

- **Executable** ("List the pros and cons", "Summarize this", "Rewrite this paragraph"): can be done directly. Execute.
- **Needs analysis** ("Fix my business", "Make this better", "Solve this"): too vague for direct execution.
  - If the problem is unclear → INVOKE: /diagnose $ARGUMENTS
  - If the goal is unclear → INVOKE: /want $ARGUMENTS
  - If the method is unclear → INVOKE: /how $ARGUMENTS
  - If the situation is unclear → INVOKE: /sid $ARGUMENTS
- **Blocked by knowledge gap** ("I know what to do but can't start"): execution barrier.
  → INVOKE: /kta $ARGUMENTS — convert knowledge to action.

### 4. Does It Map to a Specific Skill?

| Action word | Route to |
|------------|----------|
| Compare | → /cmp |
| Write / Draft | → /create |
| Debug / Fix (code) | → /diagnose |
| Plan | → /how |
| Review / Check | → /evaluate |
| Analyze | → /analyze |
| Research | → /search |
| List | → /list (high-quality list building) |
| Reorder / Rank | → /ro (expert reordering) |
| Expand ("and so on", "etc") | → /etc or /aso (pattern expansion) |
| Test (a claim) | → /claim |
| Test (an idea) | → /viability |
| Decide | → /decide |
| Reframe / "another way" | → /iaw |
| Story / Narrative | → /story |
| Debate | → /deb |

If no clear match, proceed with general execution.

### 5. Single Step or Multi-Step?

- **Single step** ("Summarize this"): execute directly.
- **Multi-step** ("Build a deployment pipeline", "Set up the project"): needs step generation.
  → INVOKE: /stg [action] — generate steps.
  → INVOKE: /to [steps] — order by dependencies.
  → Execute each step.
- **Multi-step with unresolved decisions**: → INVOKE: /tbd after step generation to surface open questions.
  → INVOKE: /tobd to sequence the resolutions.

### 6. Does the User Want Options or Just Execution?

- **Options** ("How should I approach this?"): they actually want method discovery.
  → INVOKE: /how $ARGUMENTS
- **Execution** ("Just do it", "Go ahead", "Do it"): execute with best judgment.

### 7. Adjacent Tasks

After identifying the core action, check for implied adjacent tasks:
- → INVOKE: /ata $ARGUMENTS — surface implied prerequisites and follow-ups.
- If scope is expanding too much → INVOKE: /iagca to compress back.

### 8. Depth and Mode Selection

| Situation | Mode |
|-----------|------|
| User wants simplest execution | → /ezy (easy mode) |
| User wants maximum rigor | → /hrd (hard mode) |
| Task is trivial (answer directly) | No skill needed |
| Task involves safety | → also /saf |
| Task involves ethics | → also /eth |

---

## Execute

**Simple commands:** Execute directly — no skill invocation needed.

**Multi-step commands:**
→ INVOKE: /stg [action] for step generation
→ INVOKE: /to [steps] if dependencies matter

**Continuation commands** ("do next", "continue", "keep going"):
Continue from the most recent context. Apply whatever skill or approach is currently active.
If no context: → INVOKE: /next $ARGUMENTS to determine the best next step.

**Broad commands** ("handle this"):
→ INVOKE: /handle $ARGUMENTS

### Supplementary Analysis (invoke when relevant)

| Situation | Also invoke |
|-----------|------------|
| Obvious steps might be missed | → /obv (obvious check) |
| Obvious bad outcomes | → /obo |
| Risks in execution | → /fla (failure anticipation) |
| Need to see implications | → /sycs (so you can see) |
| Execution scope growing | → /iagca (scope compression) |
| Need to know limits | → /awtlytrn (estimate limits) |
| Need to differentiate approaches | → /difr |

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Executing before understanding** | User said "fix this" and you started changing things | Pause — diagnose first, then execute |
| **Skipping prerequisites** | Multi-step task started at step 3 | Map dependencies first with /to |
| **Ignoring adjacent tasks** | Core task done but obvious follow-ups missed | Use /ata to surface what else needs doing |
| **Over-analyzing instead of executing** | User said "just do it" and got a plan instead | If the command is clear, execute it |

---

## After Completion

Report:
- What was done
- Result
- If multi-step: what's completed and what remains
- Adjacent tasks identified (if any)

### Follow-Up Routing

After execution, the user may need:
- **"What's next?"** → INVOKE: /next
- **"Did I miss anything?"** → INVOKE: /obv or /ata
- **"Is this good?"** → INVOKE: /evaluate
- **"What could go wrong?"** → INVOKE: /fla or /obo
- **"What skills should I run?"** → INVOKE: /fonss or /wsib
- **"What's still undecided?"** → INVOKE: /tbd

---

## Integration

- **Use from**: /how (after method is chosen, execute it), /want (after goal is clear, act on it), /decide (after decision is made, implement it)
- **Routes to**: /stg (step generation), /to (task ordering), /create (content production), /diagnose (when problem is unclear), /handle (broad directives), /kta (execution barriers)
- **Differs from**: /how (action executes, how finds the method), /create (action is general execution, create is specifically content production)
- **Complementary**: /ata (adjacent tasks), /tbd (unresolved decisions), /next (next step selection)
