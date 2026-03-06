# CODEX STRICT EXECUTION CONTRACT (HOW)

1. Output this sequence:
   - `GOAL: ...`
   - `GOAL CLARITY: clear|vague`
   - `METHOD STATE: unknown|known`
   - `TASK SIZE: trivial|multi-step`
2. If goal clarity is `vague`, end with:
   - `INVOKE: $want USER_INPUT`
3. If task size is `trivial` and method state is `known`, end with:
   - `INVOKE: $action USER_INPUT`
4. If method state is `unknown`, end with:
   - `INVOKE: $foht USER_INPUT`
5. If method is known and steps are needed, end with:
   - `INVOKE: $stg [known method]`
6. Do not invent full plans in this router.
7. Last line must be a single `INVOKE:` handoff.
