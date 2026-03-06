# CODEX STRICT EXECUTION CONTRACT (WANT)

1. Preserve user goal verbatim in:
   - `STATED WANT: ...`
2. Output this sequence:
   - `GOAL TYPE: goal|decision|claim|emotion|method`
   - `PROXY RISK: low|high`
   - `ACTIONABILITY: actionable|aspirational`
3. If goal type is not `goal`, route immediately to matching router skill.
4. If goal type is `goal`, end with:
   - `INVOKE: $wt USER_INPUT`
5. Do not skip proxy check.
6. Do not emit final action plans in this router.
7. Last line must be a single `INVOKE:` handoff.
