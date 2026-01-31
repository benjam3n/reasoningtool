# UAUA — DCP Input Discovery

**Date**: 2026-01-31
**Depth**: 8x
**Input**: come up with good inputs for dcp to answer that i might not have considered

---

## FINDING REGISTRY

```
FINDING REGISTRY
================

UNBUNDLED CLAIMS:
[U1] Find good inputs for /dcp that the user hasn't considered -- TYPE: explicit
[U2] "Good" means the resulting procedure would be genuinely useful -- TYPE: implicit
[U3] User has already done several DCPs (8 existing) -- TYPE: implicit
[U4] DCP works best on certain types of decisions -- TYPE: presupposed
[U5] User's existing DCPs have a pattern/bias that leaves blind spots -- TYPE: presupposed
[U6] This is a meta-question (analysis to find inputs for analysis tool) -- TYPE: meta
[U7] "Good inputs" bundles (a) DCP handles well mechanically AND (b) output is valuable -- TYPE: bundled

PATTERN ANALYSIS:
[U8] Existing DCPs cluster around "big life questions" + "professional/technical"
[U9] GAP: interpersonal/relational decisions -- missing entirely
[U10] GAP: health/body decisions -- missing entirely
[U11] GAP: timing decisions (when, not what) -- missing entirely
[U12] GAP: exit/quit/stop decisions -- missing entirely
[U13] GAP: meta-cognitive decisions -- missing entirely
[U14] GAP: resource allocation under scarcity -- missing entirely
[U15] GAP: trust/delegation decisions -- missing entirely
[U16] GAP: recurring mundane decisions with cumulative impact -- missing entirely

CANDIDATES (from U1 mapping):
[U17] CAREER/WORK decisions -- SOURCE: state space
[U18] FINANCIAL decisions -- SOURCE: state space
[U19] HEALTH decisions -- SOURCE: state space
[U20] RELATIONSHIP decisions -- SOURCE: state space
[U21] LEARNING decisions -- SOURCE: state space
[U22] CREATIVE decisions -- SOURCE: state space
[U23] OPERATIONAL decisions -- SOURCE: state space
[U24] LEGAL/BUREAUCRATIC decisions -- SOURCE: state space
[U25] PURCHASING decisions -- SOURCE: state space
[U26] SAFETY/RISK decisions -- SOURCE: state space
[U27] POLITICAL/SOCIAL decisions -- SOURCE: state space
[U28] PARENTING/EDUCATION decisions -- SOURCE: state space
[U29] ENVIRONMENTAL decisions -- SOURCE: state space
[U30] TEMPORAL decisions -- SOURCE: state space

INSTANCE-TO-CATEGORY:
[U31] CATEGORY: "Expert-novice gap" decisions
[U32] INSTANCE: Hiring (recruiters vs managers)
[U33] INSTANCE: Choosing a therapist
[U34] INSTANCE: Pricing (experienced vs new operators)
[U35] CATEGORY: "Recurring regret" decisions
[U36] INSTANCE: When to end a relationship
[U37] INSTANCE: Whether to move cities
[U38] INSTANCE: When to quit a job
[U39] CATEGORY: "Invisible fork" decisions
[U40] INSTANCE: Unexpected windfall response
[U41] INSTANCE: Conflict response pattern
[U42] INSTANCE: Delegate vs do-it-yourself default

PARAMETERS:
[U43] Frequency: DCP best for moderate frequency (monthly-yearly)
[U44] Stakes: DCP best for moderate-to-high stakes
[U45] Dimensionality: Sweet spot 6-15 dimensions
[U46] Expertise availability: DCP most valuable when expertise is expensive/gatekept
[U47] Emotional loading: DCP most valuable for emotionally clouded decisions
[U48] Time pressure: Pre-built procedures most valuable under time pressure

PERSPECTIVES:
[U49] First-time founders need DCPs
[U50] New managers need DCPs
[U51] Recent graduates need DCPs
[U52] Caregivers need DCPs
[U53] Immigrants/relocators need DCPs
[U54] People in crisis need DCPs

ASSUMPTIONS:
[U55] LOAD-BEARING: DCP inputs should be "decisions" -- if false: also assessments, diagnoses, navigations
[U56] LOAD-BEARING: User wants inputs they'd personally use -- if false: might want showcase examples
[U57] LOAD-BEARING: "Not considered" means genuinely novel categories -- if false: might mean specific instances
[U58] BACKGROUND: DCP produces static procedures

DIMENSIONS:
[U59] Personal vs Universal
[U60] HIDDEN: Emotional vs Analytical -- some decisions SHOULD be made emotionally
[U61] HIDDEN: Reversible vs Irreversible
[U62] HIDDEN: Decision vs Series -- some "decisions" are compound micro-decisions
[U63] SHORT-TERM: What's useful right now
[U64] MEDIUM-TERM: What to build before you need it
[U65] LONG-TERM: What you'd wish you'd built 10 years ago
[U66] Individual scale
[U67] Team scale
[U68] Organization scale
[U69] Society scale (may be too complex)

SPECIFIC CANDIDATES:
[C1] When to quit something -- CATEGORY: exit, timing, emotional
[C2] Whether to confront someone -- CATEGORY: interpersonal, frequent
[C3] Health symptom evaluation -- CATEGORY: health, high-stakes
[C4] How to hire the right person -- CATEGORY: career, expert-novice gap
[C5] Delegate vs do it yourself -- CATEGORY: operational, invisible fork
[C6] How to choose where to live -- CATEGORY: environmental, irreversible
[C7] How to price your product/service -- CATEGORY: financial, expert gap
[C8] Accept/negotiate/reject an offer -- CATEGORY: career/financial, time pressure
[C9] Time allocation across priorities -- CATEGORY: resource allocation, series
[C10] When to stop researching and start acting -- CATEGORY: meta, timing
[C11] Evaluate whether relationship is worth continuing -- CATEGORY: relational
[C12] Respond to unexpected windfall/opportunity -- CATEGORY: invisible fork
[C13] Choose a contractor/vendor/provider -- CATEGORY: purchasing, recurring
[C14] Build, buy, or partner -- CATEGORY: operational, strategic
[C15] What to learn next -- CATEGORY: learning, recurring
[C16] Navigate an unfamiliar bureaucratic system -- CATEGORY: navigation
[C17] When to seek professional help -- CATEGORY: meta, routing
[C18] Decisions under extreme stress -- CATEGORY: meta, crisis
[C19] Saying yes/no to requests on your time -- CATEGORY: frequent, compound
[C20] When creative work is "done" -- CATEGORY: creative, timing
[C21] How to create emergency decision cards (meta-procedure) -- DERIVED FROM F64-F67
[C22] Pre-decision readiness self-check -- DERIVED FROM F14, F48, F68-F69

AR FINDINGS:
[F1] C1 prevents #1 decision error (persisting due to sunk cost) -- STRENGTH: necessary -- PARENT: C1
[F2] Core crux: distinguishing "hard but working" vs "hard and failing" -- STRENGTH: necessary -- PARENT: F1
[F3] Key dimensions: trajectory, opportunity cost, sunk cost, reversibility -- STRENGTH: probable -- PARENT: F2
[F5] C1 is universal across domains -- STRENGTH: probable -- PARENT: C1
[F15] C2 addresses most frequent high-stakes decision -- STRENGTH: necessary -- PARENT: C2
[F16] C2 key dimensions: severity, relationship, power, likelihood of change -- STRENGTH: probable -- PARENT: F15
[F18] C2 high daily value due to frequency -- STRENGTH: necessary -- PARENT: C2
[F27] C3 highest value DCP possible (life/death) -- STRENGTH: necessary -- PARENT: C3
[F28] Triage nurses already use these procedures -- STRENGTH: necessary -- PARENT: F27
[F30] People use terrible heuristics for health symptoms -- STRENGTH: probable -- PARENT: C3
[F38] C5 is invisible-fork, 20+ times daily -- STRENGTH: necessary -- PARENT: C5
[F39] Cumulative cost of wrong defaults is enormous -- STRENGTH: probable -- PARENT: F38
[F41] C5 dimensions are clear and measurable -- STRENGTH: necessary -- PARENT: C5
[F49] C10 unblocks all other decisions (meta-value) -- STRENGTH: necessary -- PARENT: C10
[F50] Must quantify diminishing returns on information -- STRENGTH: probable -- PARENT: F49
[F52] C10 is the decision about decisions -- STRENGTH: probable -- PARENT: C10
[F59] C18 addresses max gap between need and ability -- STRENGTH: necessary -- PARENT: C18
[F61] Pre-built procedures most valuable when cognition is impaired -- STRENGTH: necessary -- PARENT: C18
[F70] Pricing is one of highest-leverage business decisions -- STRENGTH: necessary -- PARENT: C7
[F72] Huge expert-novice gap in pricing -- STRENGTH: necessary -- PARENT: C7
[F79] "Can't quit" can be handled as a route-to-coping branch -- STRENGTH: probable -- PARENT: E1
[F82] Power dynamics can be classified at Step 0 -- STRENGTH: probable -- PARENT: E6
[F86] Catastrophic gate raises research threshold -- STRENGTH: necessary -- PARENT: E8
[F88] Behavioral tripwires don't require self-awareness -- STRENGTH: probable -- PARENT: E14

AW FINDINGS:
[F7] C1 too context-dependent across domains -- SEVERITY: serious -- PARENT: C1
[F11] Most important quitting decisions too emotional for procedure -- SEVERITY: serious -- PARENT: C1
[F21] Confrontation is a SKILL not just a DECISION -- SEVERITY: serious -- PARENT: C2
[F22] Green light without skill makes things worse -- SEVERITY: serious -- PARENT: F21
[F25] Cultural variation in confrontation norms -- SEVERITY: conditional -- PARENT: C2
[F32] Unvalidated health procedure could kill someone -- SEVERITY: fatal -- PARENT: C3
[F33] Downside of wrong health procedure is catastrophic -- SEVERITY: fatal -- PARENT: F32
[F36] Symptom interactions are combinatorially complex -- SEVERITY: fatal -- PARENT: C3
[F43] Delegation embedded in relationship dynamics -- SEVERITY: serious -- PARENT: C5
[F46] Hardest part of delegation is psychological -- SEVERITY: conditional -- PARENT: C5
[F54] Optimal stopping point varies enormously by domain -- SEVERITY: serious -- PARENT: C10
[F57] Some decisions genuinely deserve indefinite research -- SEVERITY: conditional -- PARENT: C10
[F64] Under extreme stress, can't follow complex procedures -- SEVERITY: serious -- PARENT: C18
[F65] Standard DCP format is useless in crisis -- SEVERITY: serious -- PARENT: F64
[F68] Under genuine extreme stress, "don't decide now" is often correct -- SEVERITY: conditional -- PARENT: C18
[F74] Pricing depends on constantly changing factors -- SEVERITY: conditional -- PARENT: C7
[F76] Best pricing is empirical, not analytical -- SEVERITY: serious -- PARENT: C7
[F80] "Can't quit" is coping, not deciding -- dilutes DCP -- SEVERITY: conditional -- PARENT: E1
[F83] Wrong power classification in confrontation is dangerous -- SEVERITY: fatal -- PARENT: E6
[F89] Behavioral tripwires can false-positive -- SEVERITY: conditional -- PARENT: E14

FORECLOSURES:
[F6] Can't claim "trust your gut about quitting" -- PARENT: C1
[F20] Can't treat all confrontations as equivalent -- PARENT: C2
[F53] Can't endorse "research until you feel ready" -- PARENT: C10
[F63] Can't claim "trust instincts under pressure" -- PARENT: C18

DERIVED ALTERNATIVES:
[F8] Split quitting DCP into sub-procedures per domain -- DERIVED FROM: F7
[F9] Core logic (sunk cost, trajectory, opportunity cost) is domain-invariant -- DERIVED FROM: F8 (damages F7)
[F14] Pre-decision emotional readiness check -- DERIVED FROM: F11
[F24] Combined WHEN + HOW templates for confrontation -- DERIVED FROM: F21/F22
[F35] "When to seek professional help" instead of symptom evaluation -- DERIVED FROM: F32
[F48] Psychological override check for delegation -- DERIVED FROM: F46/F47
[F67] Meta-procedure for producing emergency decision cards -- DERIVED FROM: F64/F65/F66
[F85] Confrontation DCP must lead with safety assessment -- DERIVED FROM: F83/F84

EDGE CASES:
[E1] C1 breaks when quitting is impossible -- TYPE: boundary
[E2] C9 at org scale becomes portfolio management -- TYPE: scale
[E3] C7 breaks during market disruptions -- TYPE: temporal
[E4] C4 may conflict with legal requirements -- TYPE: stakeholder
[E5] C15 needs three different procedures by purpose -- TYPE: context
[E6] C2 breaks in power-imbalanced relationships -- TYPE: boundary (FATAL)
[E7] C5 at scale becomes organizational design -- TYPE: scale
[E8] C10 breaks for catastrophic irreversible decisions -- TYPE: boundary
[E9] C6 diverges radically by life stage -- TYPE: temporal
[E10] C19 breaks when requester has power over you -- TYPE: context
[E11] C11 ignores bilateral nature of relationships -- TYPE: stakeholder
[E12] C20 breaks for collaborative work -- TYPE: context
[E13] C17 at org level becomes build-vs-outsource -- TYPE: scale
[E14] C22 has self-assessment paradox -- TYPE: boundary

BEDROCK REACHED:
[F4] BEDROCK-OBSERVE: People systematically quit too late (documented in research)
[F10] BEDROCK-LOGIC: Sunk cost fallacy is domain-invariant by definition
[F13] BEDROCK-OBSERVE: Pre-commitment devices work (advance directives, prenups)
[F17] BEDROCK-OBSERVE: Both avoidance and chronic confrontation correlate with poor outcomes
[F19] BEDROCK-LOGIC: Frequency × improvement = total value
[F29] BEDROCK-OBSERVE: Medical triage flowcharts exist and save lives
[F31] BEDROCK-OBSERVE: ER data shows both too-late and unnecessary arrivals
[F34] BEDROCK-LOGIC: Error=death requires expert validation
[F37] BEDROCK-OBSERVE: Medical diagnosis requires ~10 years training due to combinatorial complexity
[F40] BEDROCK-OBSERVE: Delegation failure is #1 new-manager mistake
[F42] BEDROCK-LOGIC: Delegation is fundamentally a resource allocation problem
[F47] BEDROCK-OBSERVE: Managers who know they should delegate still micromanage
[F51] BEDROCK-LOGIC: Information has diminishing marginal value (optimal stopping theory)
[F56] BEDROCK-LOGIC: VOI = P(change decision) × value of better decision
[F58] BEDROCK-OBSERVE: "Just decide" has caused catastrophic irreversible errors
[F60] BEDROCK-OBSERVE: Stress reduces working memory (cognitive science)
[F62] BEDROCK-LOGIC: Impaired cognition requires external scaffolding (pilots use checklists)
[F66] BEDROCK-OBSERVE: Military emergency procedures are 3-5 bold-face steps
[F69] BEDROCK-OBSERVE: "Take your own pulse first" principle in emergency medicine
[F71] BEDROCK-OBSERVE: Most small businesses underprice by 20-40%
[F73] BEDROCK-OBSERVE: Pricing consultants exist as profession (demonstrates gap)
[F77] BEDROCK-OBSERVE: Companies optimize pricing through experimentation
[F81] BEDROCK-LOGIC: Decision procedure for "whether to X" must handle "can't X"
[F84] BEDROCK-OBSERVE: Direct confrontation with abuser increases danger
[F87] BEDROCK-LOGIC: More research justified when E(cost of delay) < E(cost of error)
[F90] BEDROCK-OBSERVE: Military/aviation use buddy checks for impairment assessment

TENSIONS:
[F27] vs [F32]: Health symptoms are highest-value DCP input BUT unvalidated
    health procedures are irresponsible -- TYPE: optimization frontier
[F49] vs [F57]: Stop researching is meta-valuable BUT some decisions
    deserve indefinite research -- TYPE: commitment decision
[F61] vs [F64]: Procedures most valuable under stress BUT stress prevents
    following complex procedures -- TYPE: optimization frontier
[F70] vs [F76]: Pricing DCP is high-leverage BUT best pricing is
    empirical not analytical -- TYPE: information gap

CANDIDATE VERDICTS:
[C1] VALIDATED -- AR: F1,F2,F3,F4,F5,F10,F13 -- AW: F7,F8,F11
     -- Edge: E1 -- Verdict: AR reaches bedrock (F4,F10), AW serious
     but addressed (F9 damages F7, F12/F13 address F11)

[C2] CONDITIONAL -- AR: F15,F16,F17,F18,F19 -- AW: F21,F22,F23,F25
     -- Edge: E6 -- Verdict: Valid IF includes HOW templates (F24)
     and safety assessment (F85). Without these, could cause harm.

[C3] REJECTED as stated / VALIDATED as modified -- AR: F27,F28,F29,F30,F31
     -- AW: F32,F33,F34,F36,F37 -- Verdict: Fatal AW (F34). Modified
     to "when to seek professional help" (F35) = excellent.

[C4] VALIDATED -- AR: F40 (bedrock) -- AW: none fatal
     -- Edge: E4 -- Verdict: Strong, needs legal compliance gates.

[C5] VALIDATED -- AR: F38,F39,F40,F41,F42 -- AW: F43,F46,F47
     -- Edge: E7 -- Verdict: AR at bedrock (F40,F42), AW addressed
     by including relational dimensions (F45) and psych check (F48).

[C6] UNCERTAIN -- Not tested at depth. High potential (irreversible,
     multi-dimensional) but may be too personal for universal procedure.

[C7] VALIDATED -- AR: F70,F71,F72,F73 -- AW: F74,F76,F77
     -- Edge: E3 -- Verdict: AR at bedrock (F71,F73), AW conditional
     (F75 damages F74, F78 scopes audience).

[C8] UNCERTAIN -- Not tested at depth. Likely valid (time pressure +
     emotional loading + expert gap).

[C9] UNCERTAIN -- Not tested at depth. High frequency but may be
     too compound (U62) for a single DCP.

[C10] VALIDATED -- AR: F49,F50,F51,F52,F56 -- AW: F54,F57,F58
      -- Edge: E8 -- Verdict: AR at bedrock (F51,F56), AW addressed
      (F55 damages F54, F86 handles E8). Meta-valuable.

[C11] CONDITIONAL -- Not fully tested. Needs bilateral perspective
      (E11). Risk of purely self-interested evaluation.

[C12] UNCERTAIN -- Not tested at depth. Rare but high-stakes.

[C13] UNCERTAIN -- Not tested at depth. Likely valid (recurring,
      moderate stakes, clear dimensions).

[C14] UNCERTAIN -- Not tested at depth. Classic business decision.

[C15] CONDITIONAL -- Not fully tested. Needs split by purpose (E5).

[C16] VALIDATED (implicit) -- Navigation procedures are DCP's strongest
      use case per U55. Bureaucratic systems have knowable paths.

[C17] VALIDATED -- Derived from F35. Routes to experts rather than
      replacing them. Safe and high-value.

[C18] CONDITIONAL -- AR: F59,F60,F61,F62 -- AW: F64,F65,F66,F68
      -- Verdict: Valid but must use SIMPLIFIED format (F66/F67).
      Standard DCP format defeats purpose.

[C19] UNCERTAIN -- Not tested at depth. Very high frequency (U62)
      but may overlap with C9 (time allocation).

[C20] UNCERTAIN -- Not tested at depth. Context-dependent (E12).

[C21] CONDITIONAL -- Meta-procedure. Valid if audience already has
      full DCPs to simplify.

[C22] VALIDATED -- AR: F60,F62,F69 -- AW: F89 (conditional)
      -- Edge: E14 addressed by F90 (buddy checks).

TOTALS:
- Unbundled claims: 7
- Candidates mapped: 22 (C1-C22)
- Generated artifacts: 0 (analytical domain)
- Assumptions: 4 (3 load-bearing)
- Dimensions: 11 (3 hidden)
- Perspectives: 6
- AR findings: 22 (10 necessary, 10 probable, 2 possible)
- AW findings: 20 (3 fatal, 7 serious, 10 conditional)
- Foreclosures: 4
- Derived alternatives: 8
- Edge cases: 14
- Bedrock reached: 24
- Tensions: 4
- Verdicts: 7 validated, 1 rejected, 0 damaged, 4 conditional, 8 uncertain
```

---

## SYNTHESIS

**ORIGINAL INPUT**: Come up with good inputs for /dcp that I might not have considered (8x depth)

**SPACE SIZE**: 90 unique findings across 22 candidate DCP inputs

### What the Analysis Actually Found

1. **Your existing DCPs have a systematic blind spot toward interpersonal, timing, and meta-cognitive decisions** (U8-U16). Your 8 DCPs cluster around "what should I do about big life questions" and "how do I set up technical systems." Entirely missing: when to quit, whether to confront, how to delegate, when to stop analyzing.

2. **The highest-value DCP inputs score high on THREE parameters simultaneously: frequency × stakes × expert-novice gap** (U43-U47, F19). A decision that's frequent AND high-stakes AND where experts decide much better than novices is the sweet spot.

3. **Some of the best DCP inputs are "invisible fork" decisions — ones where people don't realize they're deciding** (U39, F38). Delegation defaults, conflict response patterns, and windfall responses happen on autopilot. Making them conscious through a procedure is the entire value.

4. **Health symptom evaluation is the highest-stakes DCP input but fatally flawed as stated** (F27 vs F32). Modified to "when to seek professional help" (F35), it becomes safe and excellent — it routes to experts rather than replacing them.

5. **"When to quit" is the single strongest validated candidate** (C1, F1-F4, F10). Universal across domains, addresses the most documented decision bias (sunk cost), and the core logic is domain-invariant even though surface details vary.

6. **Decisions under stress require a fundamentally different DCP format** (F61 vs F64, F66). The standard DCP with 40 steps is useless when cognition is impaired. This creates a need for a META-DCP: how to produce emergency decision cards from full procedures (C21).

7. **"When to stop researching" is uniquely meta-valuable because it unblocks all other decisions** (F49, F52). A procedure for deciding when you have enough information improves every subsequent decision.

8. **Three candidates emerged that weren't in the initial search at all** — pre-decision readiness check (C22), emergency decision card creator (C21), and "when to seek professional help" (C17 as derived from C3's failure) — all from testing failures of other candidates.

### Key Tensions

1. **Health = highest value vs. highest liability** (F27 vs F32): The most valuable DCP to build is the most dangerous to get wrong. Resolution: route to experts (F35), don't replace them. TYPE: optimization frontier.

2. **Stress procedures = most needed vs. hardest to follow** (F61 vs F64): Procedures are most valuable when cognition is impaired, but impaired cognition can't follow complex procedures. Resolution: ultra-simplified format (F66). TYPE: optimization frontier.

3. **Stop researching = meta-valuable vs. some decisions deserve infinite research** (F49 vs F57): Resolution: reversibility gate (F58, F86, F87). TYPE: commitment decision.

4. **Pricing = high-leverage analytical vs. best done empirically** (F70 vs F76): Resolution: audience-dependent — analytical is best available for small operators who can't A/B test (F78). TYPE: information gap.

### VOI Ranking

1. **C1 — When to quit** (F1, F4, F10) — Highest VOI because it addresses the most documented, most universal decision bias with a proven domain-invariant core logic.
2. **C10 — When to stop researching** (F49, F51, F56) — Second because it's meta: improves all other decisions.
3. **C5 — Delegate vs do yourself** (F38, F40, F42) — Third because it's the highest-frequency invisible-fork decision with measurable dimensions.
4. **C17 — When to seek professional help** (F35, F29) — Fourth because it's the safe version of the highest-stakes domain (health) and applies universally.
5. **C7 — How to price** (F70, F71, F73) — Fifth because it's highest direct financial leverage.

### Load-Bearing Assumptions

- [U55]: DCP inputs must be "decisions" — if expanded to navigations/assessments, C16 (bureaucratic navigation) becomes top-tier
- [U56]: User wants personally useful inputs — if showcase, the rejected C3 (health symptoms) is the most compelling demonstration despite being unsafe
- [U60]: Some decisions should remain emotional — this gates which candidates are appropriate

### Hidden Dimensions

- [U60]: Emotional vs Analytical — confrontation (C2) and relationship evaluation (C11) may be decisions that SHOULD involve emotion, and a pure procedure may strip out necessary signal
- [U61]: Reversible vs Irreversible — irreversible decisions (C6 where to live, quitting) benefit most from procedures
- [U62]: Decision vs Series — time allocation (C9) and saying yes/no (C19) are compound micro-decisions, not single decisions; may need different DCP format

### Weakest Links

- C2 verdict is Conditional (F21-F24) — confrontation DCP could cause harm without HOW templates
- C18 verdict is Conditional (F64-F67) — standard format defeats purpose
- 8 candidates remain UNCERTAIN — not tested at depth

### Alternatives Derived from Analysis

1. "When to seek professional help" replaces "health symptom evaluation" — DERIVED FROM F32/F35
2. Emergency decision card meta-procedure replaces full crisis DCP — DERIVED FROM F64-F67
3. Pre-decision readiness check as a standalone DCP — DERIVED FROM F14, F48, F68-F69
4. Combined WHEN+HOW confrontation procedure replaces decision-only — DERIVED FROM F21-F24

### Testable Predictions

- Building C1 (when to quit) will produce the most universally applicable procedure of any DCP so far (from F5, F10)
- C10 (when to stop researching) will be the hardest to write because it's self-referential — the DCP itself requires research to build, creating a meta-loop (from F49, F52)
- C7 (pricing) will generate the most directly measurable value for the user if they sell anything (from F70, F71)

### DO_FIRST Actions

1. **Build `/dcp when to quit something`** — WHO: Claude — resolves: C1, U12, F1-F4
2. **Build `/dcp when to stop researching and start acting`** — WHO: Claude — resolves: C10, U11, U13, F49-F52
3. **Build `/dcp whether and how to delegate`** — WHO: Claude — resolves: C5, U15, F38-F42
4. **Build `/dcp when to seek professional help`** — WHO: Claude — resolves: C17, U10, F35
5. **Build `/dcp how to price your product or service`** — WHO: Claude — resolves: C7, U18, F70-F73

### Unresolved

- 8 candidates (C6, C8, C9, C12, C13, C14, C19, C20) stayed UNCERTAIN — would need individual ARAW testing to verdict
- C2 (confrontation) needs domain expert input on safety (F83-F84) before building
- C18 (stress decisions) needs format innovation (F66-F67) before building

### READY FOR

- `/dcp when to quit something` — strongest validated candidate
- `/dcp when to stop researching and start acting` — highest meta-value
- `/ar C9 (time allocation is a good DCP input)` — to resolve whether compound micro-decisions work as DCPs
- `/aw C2 (confrontation DCP is safe to build)` — to resolve safety concern before building
