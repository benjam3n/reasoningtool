---
name: "action - Execute a Command"
description: Sub-orchestrator for commands and action requests. Routes to direct execution, step generation, or reclassifies when the command needs analysis first.
---

# Action

**Input**: $ARGUMENTS

---

## Routing Decisions

### 1. Extract the Action

What does the user want done? State it as a verb + object. "Write a business plan" / "Compare X and Y" / "Fix this code" / "Do next" / "Continue".

### 2. Is This Actually a Command?

- **"What are my options?"** → This is exploration. → INVOKE: /search $ARGUMENTS
- **"How should I approach this?"** → This is method-seeking. → INVOKE: /how $ARGUMENTS
- **"Is this good?"** → This is evaluation. → INVOKE: /evaluate $ARGUMENTS
- **"I want to X"** → This is a goal. → INVOKE: /want $ARGUMENTS
- **If it IS a command** → continue.

### 3. Is It Executable or Does It Need Analysis?

- **Executable** ("List the pros and cons", "Summarize this", "Rewrite this paragraph"): can be done directly. Execute.
- **Needs analysis** ("Fix my business", "Make this better", "Solve this"): too vague for direct execution.
  - If the problem is unclear → INVOKE: /diagnose $ARGUMENTS
  - If the goal is unclear → INVOKE: /want $ARGUMENTS
  - If the method is unclear → INVOKE: /how $ARGUMENTS

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

If no clear match, proceed with general execution.

### 5. Single Step or Multi-Step?

- **Single step** ("Summarize this"): execute directly.
- **Multi-step** ("Build a deployment pipeline", "Set up the project"): needs step generation.
  → INVOKE: /stg [action] — generate steps.
  → INVOKE: /to [steps] — order by dependencies.
  → Execute each step.

### 6. Does the User Want Options or Just Execution?

- **Options** ("How should I approach this?"): they actually want method discovery.
  → INVOKE: /how $ARGUMENTS
- **Execution** ("Just do it", "Go ahead", "Do it"): execute with best judgment.

---

## Execute

**Simple commands:** Execute directly — no skill invocation needed.

**Multi-step commands:**
→ INVOKE: /stg [action] for step generation
→ INVOKE: /to [steps] if dependencies matter

**Continuation commands** ("do next", "continue", "keep going"):
Continue from the most recent context. Apply whatever skill or approach is currently active.

---

## After Completion

Report:
- What was done
- Result
- If multi-step: what's completed and what remains
