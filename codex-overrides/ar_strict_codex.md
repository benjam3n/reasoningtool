# CODEX STRICT EXECUTION CONTRACT (AR)

## Root rule

1. Root statement is accepted in `ASSUME RIGHT`.
2. Root statement is rejected in `ASSUME WRONG`.

## Output rules

1. Show visible trees in output.
2. Use recursive statement expansion.
3. For every node, create `ASSUME RIGHT` and `ASSUME WRONG` child statements.
4. Number all findings (`R#`).
5. No summary-only output.
6. No early conclusion before exploration and registry are complete.
7. Use atomic sentences.
8. Avoid run-on sentences.
9. Avoid "based on" prose in node expansion.

## Template

`[R1] [statement]`
`├── ASSUME RIGHT`
`│   └── [R2] [next statement from right branch]`
`└── ASSUME WRONG`
`    └── [R3] [next statement from wrong branch]`
