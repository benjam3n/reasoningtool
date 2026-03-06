# CODEX STRICT EXECUTION CONTRACT (DECIDE)

1. Output this sequence:
   - `DECISION: ...`
   - `OPTIONS: ...`
   - `CRITERIA: known|unknown`
   - `STAKES: reversible|irreversible`
2. If options are unknown, end with:
   - `INVOKE: $search USER_INPUT`
3. If criteria are unknown, end with:
   - `INVOKE: $want USER_INPUT`
4. If binary and criteria are known, end with:
   - `INVOKE: $araw [do X vs do not X + depth token]`
5. If multi-option and criteria are known, end with:
   - `INVOKE: $cmp [options + criteria]`
6. Do not recommend final choice in this router.
7. Last line must be a single `INVOKE:` handoff.
