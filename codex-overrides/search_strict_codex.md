# CODEX STRICT EXECUTION CONTRACT (SEARCH)

1. Output this sequence:
   - `SPACE TYPE: option|landscape|factor|knowledge`
   - `KNOWNNESS: none|some|high`
   - `COMPLETENESS TARGET: exhaustive|representative|quick`
2. If knownness is `none`, end with:
   - `INVOKE: $uaua USER_INPUT`
3. If knownness is `some`, end with:
   - `INVOKE: $se USER_INPUT`
4. If dimensions are unclear, route via:
   - `INVOKE: $dd USER_INPUT`
5. Do not jump to recommendation before mapping handoff.
6. Do not output final conclusions in this router.
7. Last line must be a single `INVOKE:` handoff.
