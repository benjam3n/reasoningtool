# CODEX STRICT EXECUTION CONTRACT (CLAIM)

1. Output this sequence:
   - `PROPOSITION: ...`
   - `CLAIM TYPE: claim|decision|goal|emotion|exploration`
   - `DEPTH: ...`
   - `BALANCE: ...`
2. If claim type is not `claim`, route immediately to the matching router skill.
3. If claim type is `claim`, end with:
   - `INVOKE: $araw [claim text + depth token]`
4. Do not produce verdicts in this router.
5. Do not include post-completion summaries in the router turn.
6. Last line must be a single `INVOKE:` handoff.
