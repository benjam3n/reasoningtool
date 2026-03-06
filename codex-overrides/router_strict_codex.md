# CODEX STRICT EXECUTION CONTRACT (ROUTERS)

Applies to router skills that decide which deeper skill to run.

## Covered skills

claim, decide, diagnose, evaluate, search, how, want, emotion, analyze,
viability, action, create, technical, certainty, iterate, meta, next, fonss, wsib,
cs, sc, dtse, mts, fmtsb, uf, it, but, extract, handle, ata, sycs, aso, iagca

## Router behavior

1. No pretending full analysis happened in router step.
2. Router output must end in explicit invoke handoff.
3. Handoff format:
   - `INVOKE: $meta USER_INPUT` (replace `$meta` with chosen target skill id)
4. No speculative conclusion before handoff.
5. No synthetic DO_FIRST list in router.
6. For depth requests (`4x`, `8x`, etc.), preserve depth token in handoff text.

## Output discipline

1. Use atomic sentences.
2. Avoid run-on sentences.
3. Avoid "if" and "but" in decision statements.
4. Use direct classification statements.

## Fail-closed behavior

When routing is unclear:

`INCOMPLETE ROUTE: unclear target skill. Defaulting to $meta USER_INPUT`
