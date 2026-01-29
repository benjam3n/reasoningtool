# Intent Regress System (v1)

**Project**: `projects/2026-01-22_gosm-swot-analysis/`
**Purpose**: Turn unclear seed questions into *clear goal-questions* by repeatedly asking “what did I mean by that?” until the next move becomes obvious.

This is not “guess the right answer”. It is:
1) generate questions,
2) regress on the intent of those questions,
3) regress again on the intent of the refinements,
4) stop locally when a goal-question becomes clear enough that a small amount of reasoning/lookup would be maximally useful.

---

## Core Output Structure (per seed question)

For each seed question `Q0`, produce one or more **intent ladders** (branches), each with:

- `Q0` **Seed** (as written)
- `Q1..Qk` **Meaning regress** (questions about what `Qi-1` *meant*)
- **Goal candidates** (questions like “Why was X included?” / “What caused X to appear?”)
- **Answer-interface questions** (what evidence/artifact would resolve the goal-question?)
- **Action hooks** (repo-grounded lookups: searches, files to inspect, logs/registers to check)

Notes:
- Branch rather than pick when intent is ambiguous.
- Prefer “easy discriminations first” (synonym/type-check/where-it-appears) before “hard” questions (importance/causality).
- Local stopping ≠ global stopping: you can stop a ladder when it becomes actionable, without ending the overall journey.

---

## Example (Go Impulse)

Seed:
- `Is there a go impulse in this question stream?`

One possible ladder:
- What did I mean by “go impulse” (command, permission, motivation)?
- Why did “go” show up in this stream (what caused it to appear)?
- Did “go” appear as user pressure to continue, or as a bias toward closure, or as a gate/permission signal?
- **Goal-question**: Why was “go” included here?
- **Answer-interface**: Where did “go” first appear in the conversation/artifacts, and what did it cause immediately afterward?

Local stop: once you have “why was X included?” + “where did it first appear?”, the next step is an obvious provenance check (minimal guessing, maximal leverage).

---

## Local “Self-Evident” Criterion (Stop This Ladder, Not The Journey)

Stop a ladder when you have a goal-question whose next step is obvious, e.g.:
- It is resolvable by a simple artifact/provenance check (“Where did X first appear?”).
- It is resolvable by an easy definitional split (“Did I mean identity vs membership?”).
- It is resolvable by a concrete interface question (“What observation would discriminate?”).

If you can’t name the next step without guessing, you haven’t reached the goal-question yet; regress again.

---

## Files / Workflow

Previous experiments are archived in:
- `projects/2026-01-22_gosm-swot-analysis/pure_regress/previous_attempts/`

Current workflow (recommended):
1) Generate a seed question stream file (questions-only) in `pure_regress/` using `scripts/openai_append_questions.sh`.
2) Run an intent-regress pass on that file using `scripts/openai_intent_regress.sh` to produce an index + numbered parts.
