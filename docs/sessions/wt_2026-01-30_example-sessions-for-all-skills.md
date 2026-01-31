# WANTTO — Example Sessions for All Skills

**Date**: 2026-01-30
**Depth**: 2x
**Input**: create a session for every single skill that can be used as an example

---

## FINDING REGISTRY

```
FINDING REGISTRY
================

UNBUNDLED WANT:
[G1] Every skill has an example session -- TYPE: desire
[G2] Run each skill, save output to docs/sessions/ -- TYPE: method
[G3] Examples are the best way to show what a skill does -- TYPE: belief
[G4] One run on a good input is representative -- TYPE: assumption
[G5] Project looks complete and credible to outsiders -- TYPE: implicit want
[G6] Stop having opaque skills -- TYPE: anti-want

IMPLICATIONS (Assume Right):
[G7] 221+ session files must exist -- TYPE: implication
[G8] Must choose good input for each, diverse topics -- TYPE: commitment
[G9] Forecloses relying on descriptions as sufficient -- TYPE: foreclosure
[G10] Input must exercise each skill's core mechanics -- TYPE: prerequisite

ACTUAL WANT:
[G11] Make the toolkit legible to newcomers -- CONFIDENCE: high
[G12] High confidence -- examples serve legibility
[G13] Stated want serves: LEGIBILITY -- TYPE: deeper want

PREREQUISITES:
[G14] Good input/topic for each of 221 skills -- STATUS: unmet
[G15] Quality bar for what counts as good example -- STATUS: unmet
[G16] Time/tokens for 221 runs -- STATUS: unmet
[G17] Way for users to find/browse examples -- STATUS: partially met

BLOCKERS:
[G18] Many skills produce similar output (clusters) -- REMOVABLE: yes (select representatives)
[G19] Diminishing returns — Tier 1 matters more than Tier 4 -- REMOVABLE: yes (prioritize)

PATHS:
[G20] Exhaustive — all 221 -- TYPE: path
  [G21] Requires: 221 inputs, massive budget, quality review
  [G22] Gives up: Time for other improvements
  [G23] Risk: Mediocre examples, user drowning
[G24] Tiered — Tier 1 + Experimental first (15 skills) -- TYPE: path
  [G25] Requires: 15 good inputs
  [G26] Gives up: Completeness
  [G27] Risk: Tier 3-4 stays opaque (acceptable?)
[G28] Cluster-representative — ~30 examples, one per cluster -- TYPE: path
  [G29] Requires: Cluster taxonomy
  [G30] Gives up: Individual coverage
  [G31] Risk: Claiming similarity when differences exist
[G32] Demand-driven — create examples when asked -- TYPE: unconventional path
  [G33] Requires: Nothing upfront
  [G34] Gives up: Completeness/credibility impression
  [G35] Risk: Obscure skills never get covered
[G36] Do nothing -- TYPE: do-nothing path
  [G37] Outcome: Existing ~40 sessions cover most important skills
  [G38] Acceptable: Partially — gap is Tier 2-4

IMPLICATION CHAINS:
[G39] Each session must be good enough to represent -- FOR: G7 -- STRENGTH: necessary
[G40] Bad examples actively hurt (lose trust) -- PARENT: G39 -- STRENGTH: necessary
[G41] BEDROCK: Bad example worse than no example -- PARENT: G40
[G42] Forecloses: Other uses of time/budget -- TYPE: foreclosure
[G43] Input IS the example — boring input = boring skill -- FOR: G8 -- STRENGTH: necessary
[G44] Input selection is the hard work, not generation -- PARENT: G43 -- STRENGTH: necessary
[G45] BEDROCK: Bottleneck is curation, not generation -- PARENT: G44
[G46] Forecloses: Batch-generating with same topic -- TYPE: foreclosure

CRUX:
[G47] Does exhaustive coverage serve legibility better than selective?
[G48] If exhaustive: users arrive at arbitrary skills, need examples at every page
[G49] If selective: users navigate top-down, learn patterns, don't need examples everywhere
[G50] Resolve by: checking whether users land directly on Tier 4 skills or navigate down

TOTALS:
- Unbundled components: 6
- Implications traced: 12
- Foreclosures: 3
- Prerequisites: 4 (0 met, 3 unmet, 1 partially met)
- Blockers: 2 (2 removable)
- Paths mapped: 5 (including do-nothing and demand-driven)
- Crux identified: yes
```

---

## SYNTHESIS

```
USER SAID: "Create a session for every single skill that can be used as an example"

ACTUAL WANT: Make the toolkit legible to newcomers [G11]
CONFIDENCE: High [G12]
STATED ≠ ACTUAL: Yes — stated want is "221 example sessions" (method). Actual want is
"newcomers can understand what any skill does" (outcome). These diverge because exhaustive
examples may not be the best path to legibility [G47].

CURRENT STATE:
- Prerequisites met: none fully
- Prerequisites unmet: G14 (221 inputs), G15 (quality bar), G16 (token budget)
- Prerequisites partial: G17 (browsing — docs/sessions/ exists, no index)
- Active blockers: G18 (cluster similarity), G19 (diminishing returns)

PATHS AVAILABLE:
| Path | Requires | Gives Up | Risk | Status |
|------|----------|----------|------|--------|
| Exhaustive [G20] | 221 inputs, massive budget, QA | Other improvements [G42] | Mediocre examples [G23], drowning | risky |
| Tiered [G24] | 15 good inputs | Completeness [G26] | Tier 3-4 opaque [G27] | viable |
| Cluster-rep [G28] | Cluster taxonomy [G29] | Individual coverage [G30] | Misrepresenting similar skills [G31] | viable |
| Demand-driven [G32] | Nothing | Completeness [G34] | Obscure skills uncovered [G35] | viable |
| Do nothing [G36] | — | — | Gap at Tier 2-4 [G37] | partially acceptable |

CRUX: Does exhaustive coverage serve legibility better than selective? [G47]
- Resolves by: Checking user navigation patterns [G50]. But since the project is early,
  users likely arrive via Getting Started (top-down), making selective sufficient for now.

COMMITMENT CHAIN (what "every single skill" commits you to):
- 221 curated inputs [G14] — the actual bottleneck [G45]
- Each must exercise the skill's core mechanics [G10]
- Each must be good — bad examples hurt more than no examples [G41]
- Forecloses batch-generating with the same topic [G46]
- Forecloses spending that time on skill improvement or features [G42]

FORECLOSURES:
- Descriptions as sufficient documentation [G9]
- Other uses of the time/token budget [G42]
- Generic/batch input selection [G46]

FIRST ACTIONS:
1. Define quality bar for examples [G15] — what makes an example session
   worth reading? — WHO: user (decide what "good enough" means)
2. Create examples for Tier 1 + Experimental first (15 skills) [G24] —
   these are highest-impact and test the process — WHO: Claude
3. Resolve crux [G47] — decide whether to go exhaustive or stop at
   tiered/cluster — WHO: user (based on who the audience is and how
   they'll navigate)

READY FOR:
- /foht "best way to choose example inputs for 221 skills" (if going exhaustive)
- /ar "tiered coverage is sufficient for toolkit legibility" (to test the selective path)
- /se "all the ways to make a skill toolkit legible to newcomers" (if examples aren't the only answer)
```
