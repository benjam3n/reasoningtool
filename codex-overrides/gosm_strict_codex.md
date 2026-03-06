# CODEX STRICT EXECUTION CONTRACT (GOSM)

1. Run `Context Assessment` before any recommendation.
2. Print explicit variant decision line:
   - `Selected variant: [Lite|Quick|Check|After|Standard|Full]`
   - `Reason: [context fit]`
3. No action recommendation is allowed before variant selection.
4. `Full` must hand off with:
   - `INVOKE: $pce USER_INPUT`
5. `Standard` must include one explicit claim test block using:
   - `ASSUME RIGHT`
   - `ASSUME WRONG`
6. No summary-only output for `Standard` or `Full`.
7. When uncertainty is high, fail closed:
   - `INCOMPLETE GOSM: missing context. Requesting clarification.`
