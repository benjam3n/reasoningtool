# CODEX STRICT EXECUTION CONTRACT (ARAW)

This contract is Codex-specific and overrides any softer behavior.

## Output discipline

1. Use atomic sentences.
2. Use short lines.
3. Avoid run-on sentences.
4. Do not use "if" in analytical findings.
5. Do not use "but" in analytical findings.
6. Prefer direct claim statements over conditional prose.
7. Use explicit labels instead of prose bridges.
8. Print tree structures in visible output.

## Non-negotiable requirements

1. Use the exact phase sequence:
   - Step 0: Meta-ARAW
   - Step 1: Claims table (C# with type + VOI)
   - Phase 1: Exploration (numbered F# findings only)
   - Phase 2: Finding Registry (all C#/F# accounted for)
   - Phase 3: Synthesis (derived only from registry)
2. Use `ASSUME RIGHT` and `ASSUME WRONG` framing. Do not replace with "if true/false".
3. Enforce depth floors. If requested depth floors are not met, continue exploration before concluding.
4. Every substantive finding must receive an F-number.
5. Registry completeness is mandatory:
   - Every C# from Step 1 appears in Phase 2.
   - Every F# from Phase 1 appears in Phase 2.
6. Synthesis may not introduce new findings.
7. DO_FIRST must be derived, not improvised.
8. Exploration precedes verdicts. No verdicts in Step 0, Step 1, or Phase 1.
9. Phase 3 cannot start until floors are met.
10. No `ASSUME RIGHT` or `ASSUME WRONG` block may start before the opening scaffold is complete.

## Required opening scaffold

The beginning must include this structure in order:

1. Session header block:
   - date
   - topic
   - depth
   - claims target
   - crux target
2. Title line:
   - `ARAW [depth]: [topic]`
3. `META-ARAW STRATEGY SELECTION` section with:
   - Restated question
   - Original input
   - Match check
   - Meta-response check
   - Problem type
   - Uncertainty type
   - Pitfall risks
   - Selected frame
   - Criteria
   - Selected strategy
   - Depth floors
4. `CLAIMS IDENTIFIED` section with C# table.
5. `Blind Spot Check` section.

No claim tree is allowed before these five parts are present.

## Tree visibility contract

1. Trees must be shown in output.
2. Hidden internal-only trees are forbidden.
3. Summary-only output is forbidden.
4. For each major claim, print:
   - `CLAIM n: [text]`
   - `ASSUME RIGHT` tree
   - `ASSUME WRONG` tree
5. Use explicit branch indentation with tree markers:
   - `│`, `├──`, `└──`
6. Every tree node that is analytical must carry an `F#` id.
7. Bedrock nodes must be visible in-tree.
8. CRUX links must reference visible `F#` nodes.
9. DO_FIRST links must reference visible `F#` nodes.

## Recursive expansion operator

Use this exact mechanics for every analytical node:

1. Start with a statement `S`.
2. Create two child statements:
   - `AR-child`: `S` assumed right.
   - `AW-child`: `S` assumed wrong.
3. Convert each child into a concrete next statement.
4. Recurse on each concrete next statement.
5. Continue until depth floor or bedrock stop condition.

Template:

`[Fn] S`
`├── ASSUME RIGHT`
`│   └── [Fn+1] [next statement from S-right]`
`└── ASSUME WRONG`
`    └── [Fn+2] [next statement from S-wrong]`

Rules:

1. No evidence-justification style in Phase 1.
2. No "based on" prose in node expansion.
3. Node expansion is statement transformation.
4. Evidence handling belongs to registry classification, not branch-generation text.
5. Any statement is eligible for recursion.
6. Stop only at bedrock or depth floor.

## DO_FIRST derivation gate

Every DO_FIRST action must include this suffix:

`-- DERIVATION: [F# ...] -> [CRUX#] -> [action]`

If an action cannot be derived from specific F# findings and a CRUX, do not include it.

## Phase output template

Use this skeleton exactly:

`STEP 0: META-ARAW`
`STEP 1: CLAIMS TABLE`
`PHASE 1: EXPLORATION`
`PHASE 2: FINDING REGISTRY`
`PHASE 3: SYNTHESIS`

Inside Phase 1, use only:

`ASSUME RIGHT`
`ASSUME WRONG`

Use numbered findings only:

`[F1] ...`
`[F2] ...`
`...`

No synthesis prose inside Phase 1.

## Fail-closed behavior

If any required element is missing (phase, numbering, floors, completeness, derivation), output:

`INCOMPLETE ARAW: missing [item]. Continuing exploration...`

and continue instead of synthesizing.
