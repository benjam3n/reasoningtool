# CODEX STRICT EXECUTION CONTRACT (EVALUATE)

1. Output this sequence:
   - `TARGET: ...`
   - `EVALUATION TYPE: correctness|completeness|quality|assumptions|risk`
   - `STANDARD: explicit|implicit`
2. Route by evaluation type:
   - correctness -> `INVOKE: $araw [core claims]`
   - completeness -> `INVOKE: $mv [structure]`
   - quality -> `INVOKE: $pv [target]`
   - assumptions -> `INVOKE: $aex [target]`
   - risk -> `INVOKE: $fla [target]`
3. If standard is implicit, state missing standard and still hand off to the selected evaluator.
4. Do not emit final verdict in this router.
5. Last line must be a single `INVOKE:` handoff.
