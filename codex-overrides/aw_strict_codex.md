# CODEX STRICT EXECUTION CONTRACT (AW)

## Root rule

1. Root statement is rejected in `ASSUME WRONG`.
2. Root statement is accepted in `ASSUME RIGHT`.

## Output rules

1. Show visible trees in output.
2. Use recursive statement expansion.
3. For every node, create `ASSUME WRONG` and `ASSUME RIGHT` child statements.
4. Number all findings (`W#`).
5. No summary-only output.
6. No early conclusion before exploration and registry are complete.
7. Use atomic sentences.
8. Avoid run-on sentences.
9. Avoid "based on" prose in node expansion.

## Template

`[W1] [statement]`
`├── ASSUME WRONG`
`│   └── [W2] [next statement from wrong branch]`
`└── ASSUME RIGHT`
`    └── [W3] [next statement from right branch]`

