# CODEX STRICT EXECUTION CONTRACT (DIAGNOSE)

1. Output this sequence:
   - `SYMPTOM: ...`
   - `CAUSE STATE: known|suspected|unknown`
   - `TIMELINE: clear|unclear`
   - `SCOPE: isolated|systemic|unknown`
2. If cause state is `known`, end with:
   - `INVOKE: $claim [cause claim]`
3. If cause state is `suspected`, end with:
   - `INVOKE: $araw [suspected cause claim]`
4. If cause state is `unknown` and timeline is clear, end with:
   - `INVOKE: $fowwr [symptom + timeline]`
5. If cause state is `unknown` and timeline is unclear, end with:
   - `INVOKE: $uaua [symptom]`
6. Do not prescribe fixes in this router.
7. Last line must be a single `INVOKE:` handoff.
