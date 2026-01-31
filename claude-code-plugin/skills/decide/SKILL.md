---
name: "decide - Make a Decision"
description: Sub-orchestrator for decisions. Routes to comparison, ARAW testing, or goal clarification based on what the user knows.
---

# Decide

**Input**: $ARGUMENTS

---

## Routing Decisions

### 1. Extract the Choice Point

What is being decided? State the options if visible. If only one option is stated ("Should I X?"), the implicit second option is "don't X."

### 2. Is This Actually a Decision?

- **"X is true"** → This is a claim. → INVOKE: /claim $ARGUMENTS
- **"I want X"** → This is a goal, not a choice. → INVOKE: /want $ARGUMENTS
- **"Should I even bother?"** → This is emotional. → INVOKE: /emotion $ARGUMENTS
- **"What about doing X?"** → This is an idea. → INVOKE: /viability $ARGUMENTS
- **If it IS a decision** → continue.

### 3. How Many Options?

- **Binary** ("Should I X?"): ARAW on doing X vs not doing X.
- **Multi-option** ("X or Y or Z?"): Compare first, then ARAW the top candidates.
- **Open** ("What should I do about..."): Options unknown — enumerate first.
  → INVOKE: /search $ARGUMENTS — then return here with discovered options.

### 4. Are Criteria Known?

- **Yes** (user states what matters): proceed with comparison using those criteria.
- **No** (user just says "which is better?"): need to clarify what "better" means.
  → INVOKE: /want $ARGUMENTS — clarify the underlying goal, then return with criteria.

### 5. Stakes

- **Reversible** (which framework, which restaurant): lighter analysis, /cmp is sufficient.
- **Irreversible** (quit job, move countries, major investment): deeper analysis.
  → INVOKE: /araw on each option + /prm (pre-mortem) + /fla (failure anticipation).

---

## Execute

**For binary decisions:**
→ INVOKE: /araw [doing X vs not doing X]

**For multi-option with known criteria:**
→ INVOKE: /cmp [options with criteria]

**For high-stakes decisions, also:**
→ INVOKE: /prm [chosen option]
→ INVOKE: /fla [chosen option]

---

## After Completion

Report:
- The decision as framed
- Options considered
- Criteria used (stated or derived)
- Recommendation with confidence level
- What would change the recommendation
- Foreclosures (what each option gives up)
