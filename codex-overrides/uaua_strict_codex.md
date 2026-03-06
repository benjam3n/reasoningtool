# CODEX STRICT EXECUTION CONTRACT (UAUA)

This contract is Codex-specific and overrides any softer behavior.

## Output discipline

1. Use atomic sentences.
2. Use short lines.
3. Avoid run-on sentences.
4. Do not use "if" in analytical findings.
5. Do not use "but" in analytical findings.
6. Use numbered findings in every exploration block.
7. Print tree structures in visible output.

## Non-negotiable requirements

1. Use exact sequence:
   - U0: Ground
   - U1: Map
   - G1: Generate (creative domains only)
   - A1: Test
   - U2: Edge-case
   - A2: Validate
   - Registry
   - Synthesis
2. Exploration first. No early summary.
3. Registry completeness:
   - Every U#/G#/F#/E# from exploration appears in registry.
4. Synthesis introduces no new findings.
5. Depth floors are hard floors.
6. CRUX and DO_FIRST must map to numbered findings.
7. No U1 mapping, A1 testing, or claim-tree output before opening scaffold completion.

## Required opening scaffold

The beginning must include this structure in order:

1. Session header block:
   - date
   - topic
   - depth
   - claims target
   - crux target
2. Title line:
   - `UAUA [depth]: [topic]`
3. `META-STRATEGY SELECTION` section with:
   - Restated question
   - Original input
   - Match check
   - Response mode
   - Problem type
   - Uncertainty type
   - Pitfall risks
   - Selected frame
   - Criteria
   - Selected strategy
4. `CLAIMS IDENTIFIED` section with C# table.
5. `Blind Spot Check` section.

No exploration blocks are allowed before these five parts are present.

## Tree visibility contract

1. U1, A1, U2, and A2 trees must be shown in output.
2. Hidden internal-only trees are forbidden.
3. Summary-only output is forbidden.
4. For each tested candidate, print:
   - `CANDIDATE n`
   - `ASSUME RIGHT` tree
   - `ASSUME WRONG` tree
5. Use explicit branch indentation with tree markers:
   - `│`, `├──`, `└──`
6. Every analytical node must carry a numbered id:
   - `U#`, `G#`, `F#`, or `E#`
7. Bedrock nodes must be visible in-tree.
8. CRUX links must reference visible numbered nodes.
9. DO_FIRST links must reference visible numbered nodes.

## DO_FIRST derivation gate

Every DO_FIRST item must include:

`-- DERIVATION: [U#/G#/F#/E# ...] -> [CRUX#] -> [action]`

No derivation trail means no action line.

## Fail-closed behavior

When a required element is missing, output:

`INCOMPLETE UAUA: missing [item]. Continuing exploration...`

and continue exploration.
