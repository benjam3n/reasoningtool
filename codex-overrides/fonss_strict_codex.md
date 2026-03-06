# CODEX STRICT EXECUTION CONTRACT (FONSS)

1. Output `CURRENT_GOAL` first.
2. Output at least 3 ordered next skills when enough context exists.
3. Each skill entry must include:
   - `WHY_NOW`
   - `INVOCATION`
   - `EXPECTED_OUTPUT`
   - `STOP_CONDITION`
4. Sequence must be dependency-aware.
5. Do not output a single-skill answer unless constraints force it.
