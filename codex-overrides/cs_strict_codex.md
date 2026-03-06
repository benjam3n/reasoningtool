# CODEX STRICT EXECUTION CONTRACT (CS)

1. State mode explicitly: `CREATE`, `UPDATE`, or `GAP_SCAN`.
2. For `GAP_SCAN`, output ordered missing-skill candidates.
3. For each candidate include:
   - suggested skill id
   - purpose
   - expected ROI
4. Do not produce vague recommendations without concrete skill ids.
