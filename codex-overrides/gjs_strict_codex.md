# CODEX STRICT EXECUTION CONTRACT (GJS)

1. Show selected context variant before deeper analysis.
2. Do not collapse goal chain early.
3. Goal chain must include:
   - `ACTION`
   - `GOAL` levels
   - `INTRINSIC`
4. OPEN claims must trigger explicit ARAW handoff:
   - `INVOKE: $araw [OPEN claims]`
5. No synthesis-only output.
6. Next procedure section must name a concrete skill id.
7. If chain has unresolved gaps:
   - `INCOMPLETE GJS: goal chain gap detected. Continuing analysis.`
