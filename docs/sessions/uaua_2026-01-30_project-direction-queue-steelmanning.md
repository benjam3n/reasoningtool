# UAUA 8x — Project Direction, Implementation Queuing, Prompt Steelmanning, and Planning Limits

**Date**: 2026-01-30
**Depth**: 8x
**Input**: I feel like I went wrong somewhere. I had high hopes for this project but I'm not sure if it is turning out how I thought it would. One thing I want to add is I want to make it be so some sort of skill or prompt or structure or procedure or gate where one session does the implementation and another does the planning, or at least add a way to do an implementation queue type system maybe with a file or something where I can say /next or something and it can do the next item in the list. also if you think about a prompt, a prompt is almost like an argument, that can be strongmanned or steelmanned, strongman would be adding the best possible critiera and structure, universalizing, arawing but specifically not to actually answer the prompt, just to make the prompt literally couldnt get any better. but need to consider what sorts of information should be used to identify what the best possible next prompt is. also a lot of times the output can be predicted ahead of time and it can just keep trying till it gets it right so is there a limit to how far one could technically plan ahead and why not just plan out everything but only select a few things but always have on hand lots of plans ready to go.

---

## FINDING REGISTRY

```
FINDING REGISTRY
================

UNBUNDLED CLAIMS:
[U1] "I feel like I went wrong somewhere" — TYPE: explicit
[U2] "Had high hopes but not turning out how I thought" — TYPE: explicit
[U3] Want planning/implementation session separation — TYPE: explicit
[U4] Want implementation queue with /next — TYPE: explicit
[U5] A prompt is like an argument that can be steelmanned — TYPE: explicit
[U6] Steelmanning = making prompt as good as possible, not answering — TYPE: explicit
[U7] Need to identify what info determines best next prompt — TYPE: explicit
[U8] Output can sometimes be predicted ahead of time — TYPE: explicit
[U9] System could keep trying till it gets it right — TYPE: explicit
[U10] Question about limits of planning ahead — TYPE: explicit
[U11] "Plan everything but only select a few" — TYPE: explicit
[U12] Want lots of plans ready to go — TYPE: explicit
[U13] Current workflow is too ad-hoc — TYPE: implicit
[U14] Project accumulated features without clear direction — TYPE: implicit
[U15] Website stripping is symptom of the feeling — TYPE: implicit
[U16] Wants system to be more self-improving — TYPE: implicit
[U17] Planning and implementation should be separated — TYPE: presupposed
[U18] Prompts can be objectively improved independent of context — TYPE: presupposed
[U19] More planning produces better outcomes — TYPE: presupposed
[U20] "Prompt as argument" bundles: truth-value structure, quality dimensions, technique transfer — TYPE: bundled
[U21] "Plan everything, select a few" bundles: planning is cheap, selection is hard, unused plans have option value — TYPE: bundled
[U22] This input is itself an instance of the problem it describes — TYPE: meta

CANDIDATES (from U1 mapping):
[U23] State: Toolkit — success = adoption — SOURCE: state space
[U24] State: Framework — success = changed thinking — SOURCE: state space
[U25] State: Research project — success = novel findings — SOURCE: state space
[U26] State: Personal tool — success = daily use — SOURCE: state space
[U27] State: Platform — success = ecosystem — SOURCE: state space
[U28] State: Do nothing more — it already works — SOURCE: state space
[U29] The "went wrong" feeling is about something else (pace, aesthetics, recognition) — SOURCE: negation
[U59] State: Overclaimed, now correcting — success = honest presentation + evidence — SOURCE: loop 1
[U60] Pattern: overclaim → retreat → rebuild credibility — SOURCE: loop 1
[U61] Sibling pattern: startups that marketed before proving — SOURCE: loop 1

ASSUMPTIONS:
[U41] LOAD-BEARING: Separating planning from implementation improves quality — if false: overhead exceeds benefit
[U42] LOAD-BEARING: Prompt quality is a major bottleneck — if false: model handles messy prompts fine
[U43] LOAD-BEARING: "Went wrong" feeling is about the project, not expectations — if false: project is fine
[U44] LOAD-BEARING: More planning produces better outcomes — if false: over-planning is the problem
[U45] BACKGROUND: Claude Code sessions are the right environment
[U46] BACKGROUND: The 221 skills are individually sound
[U62] Claims-to-evidence ratio currently high claims, low evidence — SOURCE: loop 1
[U63] LOAD-BEARING: New features will fix dissatisfaction — if false: they add complexity to something needing simplification
[U64] HIDDEN: Building to avoid evaluating — SOURCE: loop 1

DIMENSIONS:
[U47] Identity clarity — TYPE: discovered
[U48] User vs creator — TYPE: discovered
[U49] Meta-work vs actual use ratio — TYPE: HIDDEN
[U50] Feedback loop — does the tool actually change decisions? — TYPE: HIDDEN
[U51] Diminishing returns on additional skills — TYPE: HIDDEN
[U36] Planning horizon — current: per-session — range: none to fully pre-planned
[U37] Automation level — current: manual — range: manual to autonomous
[U38] Queue persistence — current: none — range: ephemeral to permanent
[U39] Prompt optimization passes — current: 0 — range: 0 to N
[U40] Project scope — current: 221 skills + tools + website

PERSPECTIVES:
[U55] New user: "Which 3 skills should I try? Does this work?"
[U56] Researcher: "Where's the evaluation?"
[U57] Developer: "Just use a YAML file and a script"
[U58] You in 6 months: Either daily use or abandoned

TEMPORAL:
[U52] Short-term: Frustration about website/scatter
[U53] Medium-term: Are core ideas genuinely valuable?
[U54] Long-term: Daily use or built-once?

AR FINDINGS:
[F1] 221 skills mostly noise around 5-10 useful ones — STRENGTH: probable — PARENT: U30
[F2] Project better with fewer, more polished skills — STRENGTH: probable — PARENT: F1
[F3] Effort should go into core skills — STRENGTH: necessary — PARENT: F2
[F4] BEDROCK-LOGIC: Optimizing core > expanding periphery (diminishing returns) — PARENT: F3
[F13] Planning session → plan file → implementation session — STRENGTH: probable — PARENT: U41
[F14] Plan file = persistent queue between sessions — STRENGTH: necessary — PARENT: F13
[F15] File format must be parseable + human-readable — STRENGTH: necessary — PARENT: F14
[F17] Can batch planning — one deep session → 10 tasks — STRENGTH: probable — PARENT: U41
[F18] Implementation sessions become shorter/focused — STRENGTH: probable — PARENT: F17
[F28] Prompt has claims, assumptions, implications — all improvable — STRENGTH: necessary — PARENT: U5
[F29] /u extracts assumptions, /ar traces implications, /aw finds weaknesses in a prompt — STRENGTH: probable — PARENT: F28
[F30] Steelmanned prompt: explicit assumptions, precise scope, defined success criteria — STRENGTH: probable — PARENT: F29
[F31] BEDROCK-LOGIC: Making implicit claims explicit improves reasoning (the project's own premise applied to prompts) — PARENT: F30
[F32] Could create /sp (Steelman Prompt) — STRENGTH: probable — PARENT: F30
[F41] Could run UAUA on anticipated future tasks — STRENGTH: possible — PARENT: U10
[F42] Would have pre-analyzed plan library — STRENGTH: probable — PARENT: F41
[F43] Implementation becomes trivially fast — STRENGTH: possible — PARENT: F42
[F54] Project is actually good, feeling is mismatched expectations — STRENGTH: probable — PARENT: U43
[F55] Initial vision was probably about wide adoption/changing thinking — STRENGTH: probable — PARENT: F54
[F56] Reality (toolkit used by one person with good analysis) is actually a good outcome — STRENGTH: conditional — PARENT: F55
[F65] Queue/steelmanning are META-features reducing need for others — STRENGTH: conditional — PARENT: E12
[F68] Plan file carries context between sessions — STRENGTH: probable — PARENT: E9
[F71] Can plan WHAT to explore even if not what you'll find — STRENGTH: probable — PARENT: E5
[F77] Queue/steelmanning features are a form of proving value — STRENGTH: conditional — PARENT: F64
[F80] Even 1 pass of steelmanning catches worst prompt issues — STRENGTH: probable — PARENT: E6

AW FINDINGS:
[F6] Breadth IS the value — always having a structured starting point — SEVERITY: conditional — PARENT: U30
[F7] Problem is navigation, not count — SEVERITY: probable — PARENT: F6
[F10] "Went wrong" might be about presentation not product — SEVERITY: possible — PARENT: U30
[F11] Problem is marketing/communication — SEVERITY: conditional — PARENT: F10
[F20] Planning/implementation aren't cleanly separable — SEVERITY: fatal — PARENT: U41
[F21] Plans become stale when implementation starts — SEVERITY: probable — PARENT: F20
[F23] Queue overhead exceeds benefit — SEVERITY: serious — PARENT: U41
[F24] Simple TODO list captures 90% of value — SEVERITY: probable — PARENT: F23
[F34] Prompts aren't arguments — arguments have truth values, prompts have intents — SEVERITY: serious — PARENT: U5
[F35] Analogy breaks for non-propositional prompts — SEVERITY: conditional — PARENT: F34
[F37] Model already steelmans prompts implicitly — SEVERITY: serious — PARENT: U5
[F38] Explicit steelmanning adds tokens but not quality — SEVERITY: conditional — PARENT: F37
[F46] Combinatorial explosion — full planning is impossible — SEVERITY: fatal — PARENT: U10
[F47] Cannot enumerate relevant futures — SEVERITY: necessary — PARENT: F46
[F49] Prediction accuracy degrades rapidly with distance — SEVERITY: fatal — PARENT: U10
[F50] Optimal planning horizon is SHORT (1-3 steps) — SEVERITY: probable — PARENT: F49
[F59] Project has real structural problems — SEVERITY: serious — PARENT: U43
[F60] Pattern of retreat from claims — SEVERITY: probable — PARENT: F59
[F62] "Went wrong" is specifically about overclaiming — SEVERITY: probable — PARENT: F61
[F63] Correct move is demonstration, not new features — SEVERITY: probable — PARENT: F62
[F66] Meta-features are the most complex type — interact with everything — SEVERITY: serious — PARENT: E12
[F69] Plan file only carries PLANNED context, not surprises — SEVERITY: serious — PARENT: E9
[F72] Value of exploration is in surprises — can't pre-plan outcomes — SEVERITY: conditional — PARENT: E5
[F75] "I'll use it" is what every builder says — test: have you manually done this? — SEVERITY: serious — PARENT: E4
[F78] Building features is avoiding evaluation — SEVERITY: serious — PARENT: F64
[F81] Model may already steelman implicitly — first pass may duplicate — SEVERITY: conditional — PARENT: E6

FORECLOSURES:
[F5] If feature creep is the problem: "221 skills" branding becomes liability — PARENT: U30
[F19] If plan/implement separation: spontaneous exploration during implementation foreclosed — PARENT: U41
[F33] If prompts are steelmanned: raw intuitive prompts that capture inarticulable signals are lost — PARENT: U5
[F58] If "went wrong" is about expectations: the project doesn't need major changes — PARENT: U43

DERIVED ALTERNATIVES:
[F9] Instead of cutting skills, improve skill discovery — derived from F6
[F26] Lightweight planning step within each session (first 2 min plan, rest implement) — derived from F20
[F27] Use existing task system (GitHub issues, markdown checklist) — derived from F23
[F40] Only steelman propositional prompts (claims, decisions, diagnostics) — derived from F34
[F52] Plan 1-3 steps ahead in detail, rough direction for 5-10, re-plan each step — derived from F46+F49
[F53] Build capacity to plan FAST rather than pre-computing plans — derived from F46

EDGE CASES:
[E1] Queue works for 3 tasks, becomes unmaintained backlog at 30 — TYPE: scale
[E2] Prompt steelmanning at scale: 3x tokens on meta-work — TYPE: scale
[E3] Pre-computed plans expire — how fast do plans rot? — TYPE: temporal
[E4] User-as-builder vs user-as-user conflict — TYPE: stakeholder
[E5] Plan/implement separation fails for exploratory tasks — TYPE: context
[E6] Prompt steelmanning diminishing returns after first pass — TYPE: boundary
[E7] "Lots of plans ready to go" becomes unused plan library — TYPE: scale
[E8] "Went wrong" feeling may be fatigue/time-of-day — TYPE: context
[E9] Implementation session lacks planning session's context — TYPE: boundary
[E10] "Went wrong" feeling may pass tomorrow — TYPE: temporal
[E11] Who updates the plan file? Claude drift vs user overhead — TYPE: boundary
[E12] Adding features to a project accused of having too many — TYPE: contradiction
[E13] "Do nothing more" works if daily use stabilizes — TYPE: conditional
[E14] Queue only matters if multi-step tasks span sessions regularly — TYPE: context

BEDROCK REACHED:
[F4] BEDROCK-LOGIC: Optimizing core > expanding periphery (diminishing returns)
[F8] BEDROCK-OBSERVE: /fnd exists = user already noticed navigation problem
[F12] BEDROCK-OBSERVE: Website stripping = dissatisfaction with presentation
[F16] BEDROCK-TEST: Create plan file, run two sessions, measure quality difference
[F22] BEDROCK-OBSERVE: Waterfall → agile because plans don't survive reality
[F25] BEDROCK-TEST: Compare formal plan-implement vs simple TODO across 5 tasks
[F31] BEDROCK-LOGIC: Making implicit claims explicit improves reasoning (project's own premise)
[F36] BEDROCK-LOGIC: "Should I change careers" is propositional; "write a poem" is not. Steelmanning applies to a subset.
[F39] BEDROCK-TEST: Compare raw vs steelmanned prompts for 10 propositional inputs
[F45] BEDROCK-OBSERVE: Chess engines recompute every move — don't precompute whole game
[F48] BEDROCK-LOGIC: N^K combinatorial explosion makes full planning infeasible
[F51] BEDROCK-OBSERVE: Prediction accuracy drops with horizon in every known domain
[F57] BEDROCK-OBSERVE: User has been using skills intensively for days — tool IS useful
[F61] BEDROCK-OBSERVE: Pattern of removing claims, essays, descriptions from website
[F67] BEDROCK-OBSERVE: Adding features right after stripping is contradictory signal
[F70] BEDROCK-OBSERVE: Plan file is just another file Claude reads — technically feasible
[F73] BEDROCK-LOGIC: Planning to explore valid; planning exploration outcomes not
[F76] BEDROCK-TEST: Has user manually maintained task queue? If yes, automate. If no, need is hypothetical.

TENSIONS:
[F63] contradicts [U3/U4/U5]: Analysis says "demonstrate existing value" but user asks for new features — TYPE: commitment decision
[F67] contradicts [U4]: Adding features right after stripping features is contradictory — TYPE: commitment decision
[F77] contradicts [F78]: Queue features ARE proving value vs queue features AVOID proving value — TYPE: information gap
[F20] contradicts [F13]: Plans don't survive reality vs plan files enable focused sessions — TYPE: optimization frontier
[F37] contradicts [F31]: Model already steelmans vs making implicit explicit helps — TYPE: information gap

CANDIDATE VERDICTS:
[U3/U4] Plan/implement separation with queue — CONDITIONAL
  -- AR evidence: F13, F14, F15, F17, F18, F68, F71
  -- AW evidence: F20, F21, F22, F23, F24, F69, F75
  -- Edge cases: E1, E5, E9, E11, E12, E14
  -- Verdict: Works for DETERMINISTIC tasks with a SIMPLE format (markdown checklist, not a formal system). Fails for exploratory tasks. The simple version (a TODO.md file) captures most of the value.

[U5/U6] Prompt steelmanning — CONDITIONAL
  -- AR evidence: F28, F29, F30, F31, F32, F80
  -- AW evidence: F34, F35, F37, F38, F81
  -- Edge cases: E2, E6
  -- Verdict: Valid for PROPOSITIONAL prompts (claims, decisions, diagnostics). Not valid for creative/open prompts. One pass sufficient. Must test whether model already does this implicitly [F39].

[U10/U11/U12] Plan everything, select from library — REJECTED
  -- AR evidence: F41, F42, F43
  -- AW evidence: F46, F47, F48, F49, F50, F51
  -- Edge cases: E3, E7
  -- Verdict: Combinatorial explosion (F48) and prediction decay (F51) make full pre-planning impossible at bedrock-logic level. Short-horizon planning (1-3 steps) is the optimal approach.

[U59] Project overclaimed, now correcting — VALIDATED
  -- AR evidence: F54, F55, F56, F57
  -- AW evidence: F59, F60, F61, F62, F63
  -- Edge cases: E8, E10
  -- Verdict: Both AR and AW converge on this. AR says expectations were high; AW says the pattern of retreat from claims is observable (F61). The project IS useful (F57) but claimed more than it demonstrated.

[U26] Personal tool — success = daily use — VALIDATED
  -- AR evidence: F57
  -- AW evidence: no fatal AW
  -- Verdict: Observable that the tool is in heavy daily use. This is already succeeding.

[U28] Do nothing more — DAMAGED
  -- AR evidence: (simple, avoids overengineering)
  -- AW evidence: F59, F14 (some persistence mechanism IS needed)
  -- Edge cases: E13
  -- Verdict: Partially right (don't add complex features) but some simple additions (TODO.md, /next) would help.

TOTALS:
- Unbundled claims: 22
- Candidates mapped: 10
- Generated artifacts: 0 (analytical domain)
- Assumptions: 8 (6 load-bearing)
- Dimensions: 10 (3 hidden)
- Perspectives: 4
- AR findings: 29
- AW findings: 24
- Foreclosures: 4
- Derived alternatives: 6
- Edge cases: 14
- Bedrock reached: 17
- Tensions: 5
- Verdicts: 2 validated, 1 rejected, 1 damaged, 2 conditional
```

---

## SYNTHESIS

ORIGINAL INPUT: Feeling of having "gone wrong", wanting plan/implement separation, queue system, prompt steelmanning, pre-computed plans, and limits of planning.

SPACE SIZE: 85 unique findings

WHAT THE ANALYSIS ACTUALLY FOUND:

1. The "went wrong" feeling is most likely about overclaiming — the project promised more than it demonstrated, and the recent pattern of stripping the website (F61, F62) is evidence of recognizing this.
2. The project IS working as a personal tool — intensive daily use is observable (F57). The gap is between "personal tool that works" and the initial vision.
3. Full pre-planning is impossible at the level of formal logic — combinatorial explosion (F48) and prediction decay (F51). The answer to "why not plan everything" is: because you literally cannot.
4. The optimal planning horizon is 1-3 steps (F50, F52). Plan the next thing in detail, maintain rough direction, re-plan after each step.
5. A simple TODO.md file captures ~90% of the queue value the user wants (F24, F27). A formal system is overengineering.
6. Prompt steelmanning is valid but only for propositional prompts (F36) and may duplicate what the model already does (F37). Needs empirical testing (F39).
7. Adding new features right after stripping features is a contradictory signal (F67). The analysis suggests the priority is demonstrating value, not building more features.
8. The plan/implement separation works for deterministic tasks but fails for exploratory ones (E5, F73). Most of this project's work is exploratory.
9. The "prompt as argument" analogy partially holds — propositional prompts have claims that can be made explicit (F31) but creative/request prompts do not (F36).
10. Building capacity to plan fast (F53) is more valuable than pre-computing plans — because plans expire but the ability to plan doesn't.

KEY TENSIONS:

1. [F63] vs [U3/U4/U5]: Analysis says "demonstrate, don't build more" but user wants new features — TYPE: commitment decision
2. [F67] vs [U4]: Stripping followed by adding is contradictory — TYPE: commitment decision
3. [F20] vs [F13]: Plans don't survive vs plan files enable focus — TYPE: optimization frontier. Resolution: lightweight plans (TODO.md) survive. Heavyweight plans (formal queue system) don't.
4. [F77] vs [F78]: Features as proof of value vs features as avoidance of evaluation — TYPE: information gap. Resolution: only resolvable by running the evaluation (F39, F16, F25).
5. [F37] vs [F31]: Model already steelmans vs making explicit helps — TYPE: information gap. Resolution: empirical test (F39).

VOI RANKING (Value of Information):

1. F39 — Does steelmanning actually produce different outputs? Testing 10 prompts raw vs steelmanned would resolve whether /sp is worth building.
2. F76 — Has the user manually maintained a task queue between sessions? If yes, /next is warranted. If no, the need is hypothetical.
3. F16 — Does plan-then-implement produce better results than single-session? This resolves whether the entire queue idea has value.

LOAD-BEARING ASSUMPTIONS:
[U41] plan/implement separation improves quality, [U42] prompt quality is a bottleneck, [U43] feeling is about the project not expectations, [U44] more planning = better outcomes, [U63] new features will fix dissatisfaction

HIDDEN DIMENSIONS:
[U49] Meta-work vs actual use ratio, [U50] Does the tool change decisions?, [U64] Building to avoid evaluating

WEAKEST LINKS:
F56 (reality is a good outcome — conditional), F65 (meta-features reduce other needs — conditional), F77 (features as proof — conditional). These are where the optimistic reading of the project rests.

ALTERNATIVES DERIVED FROM ANALYSIS:
1. Instead of a formal queue: a TODO.md file that /next reads the top item from — derived from F23, F24, F27
2. Instead of full plan/implement separation: 2-minute planning step at the start of each session — derived from F20, F26
3. Instead of steelmanning all prompts: only steelman propositional claims — derived from F34, F40
4. Instead of pre-computing plans: build the capacity to plan fast on-demand — derived from F46, F53
5. Instead of new features: run the 3 experiments from the novelty analysis (reducibility, enforcement, drift) to prove existing value — derived from F63, F78
6. Instead of a plan library: maintain a single "current direction" document (1 page) — derived from F52

TESTABLE PREDICTIONS:
- If a simple TODO.md with /next is built, it will be used for < 2 weeks before being abandoned (from E1, E7)
- If prompt steelmanning is tested (F39), the steelmanned and raw outputs will be indistinguishable for >60% of cases (from F37)
- If the user stops building features for 1 week and only USES the existing skills, the "went wrong" feeling will decrease (from F57, F64)

DO_FIRST ACTIONS:
1. Create a TODO.md file in the project root — WHO: Claude — resolves: U4, F24, F27
2. Run 10 prompts raw vs with explicit assumption/scope/criteria extraction — WHO: user — resolves: F39, U42
3. Use the existing skills daily for a week without adding features — WHO: user — resolves: F57, F64, U50
4. Write a 1-page "what this project actually is" document — WHO: user — resolves: U47, F62

UNRESOLVED:
- Whether prompt steelmanning produces different outputs (F39 — needs testing)
- Whether the tool actually changes decisions or just produces analysis that gets ignored (U50 — needs observation)
- Whether the "went wrong" feeling is temporary (E10 — needs time)
- Whether 221 skills is a strength or liability (F1 vs F6 — needs user data)

READY FOR:
- /ar "the project's real value is RLHF sycophancy correction, not the reasoning structure" — to go deeper on the novelty analysis finding
- /aw "a simple TODO.md is enough for cross-session persistence" — to stress-test the lightweight approach
- /u "what would a 1-page project identity document contain" — to explore the clarity question
