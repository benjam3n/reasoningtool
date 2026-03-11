# /skgap What thinking tasks are people likely to need that reasoningtool doesn't cover yet?
**Date:** 2026-03-09
**Skill:** /skgap (Skill Gap Analysis)

---

## Phase 1: Dimension Mapping

### Sophistication Dimension

```
[G1] SOPHISTICATION_MAP:
     Simple (5-min, one technique): /ezy, /smpl, /sim, /list, /ro, /but, /pick, /blank, /strt, /idk, /lost — COUNT: ~60
     Moderate (15-min, multi-step): /dcp, /cba, /rca, /ht, /cmp, /se, /poa, /hab, /teach — COUNT: ~250
     Sophisticated (30-min+, multi-phase): /certainty, /systhink, /redteam, /araw, /uaua, /imprt — COUNT: ~200
     Expert (requires domain knowledge): /technical, /api, /leg, /nutr, /ai — COUNT: ~80
     GAP: The Simple tier is well-populated with state-based entry points (lost, blank,
     panic, etc.) but thin on simple ANALYTICAL tools. Most simple skills are routing/
     emotional-state skills, not quick thinking techniques. There are few "grab this one
     tool and use it in 2 minutes" analytical skills.
```

### Difficulty Dimension

```
[G2] DIFFICULTY_MAP:
     Easy (anyone can follow): /sim, /list, /ezy, /teach, /blank, /strt, /pick — COUNT: ~80
     Medium (requires some thinking skill): /dcp, /cba, /rca, /se, /poa, /cmp — COUNT: ~300
     Hard (requires significant cognitive effort): /systhink, /redteam, /certainty, /araw — COUNT: ~150
     Expert (requires training or deep domain knowledge): /technical, /api, /leg — COUNT: ~60
     GAP: Heavy concentration at Medium difficulty. The Easy tier has state-entry skills
     but few easy analytical procedures. Expert tier is domain-routed rather than offering
     deep specialist thinking methods.
```

### Generality Dimension

```
[G3] GENERALITY_MAP:
     Universal (works for any domain): /but, /se, /rca, /dcp, /cba, /sim, /teach — COUNT: ~350
     Broad (works for many domains): /systhink, /redteam, /col, /conflict — COUNT: ~150
     Domain-specific (works for one domain): /api, /leg, /nutr — COUNT: ~60
     Niche (very specific use case): /sp (prompt improvement), /skgap — COUNT: ~30
     GAP: Strong universal coverage. Domain-specific tier is shallow — few skills that
     bring genuine domain expertise to bear. Niche tier is mostly meta-toolkit skills.
     Missing: domain-specific thinking patterns for common professional domains (product
     management, engineering architecture, sales, marketing, education, healthcare
     decision-making).
```

### Speed Dimension

```
[G4] SPEED_MAP:
     Instant (< 1 min): /pick, /ro — COUNT: ~15
     Quick (1-5 min): /but, /sim, /list, /ezy, /smpl — COUNT: ~60
     Standard (5-20 min): /dcp, /cba, /rca, /se, /hab — COUNT: ~300
     Deep (20-60 min): /certainty, /systhink, /redteam, /araw — COUNT: ~180
     Exhaustive (60+ min): /certainty at max depth — COUNT: ~35
     GAP: CRITICAL gap at Instant speed. Very few skills that give you a useful thinking
     nudge in under 60 seconds. The toolkit assumes you have time to sit down and think.
     Many real thinking tasks happen in the moment — "I have 30 seconds before I respond
     to this email/message/question."
```

### User State Dimension

```
[G5] USER_STATE_MAP:
     Exploring (no clear direction): /se, /search, /dd, /poa — COUNT: ~40
     Deciding (between options): /dcp, /cmp, /cba, /pick, /decide — COUNT: ~50
     Executing (knows what to do): /action, /to, /de, /ata — COUNT: ~40
     Stuck (blocked, need unblocking): /unstk, /but, /iaw, /dbg, /lost — COUNT: ~35
     Recovering (something went wrong): /rmm, /kta, /panic, /ret — COUNT: ~20
     Validating (checking work): /pv, /mv, /vbo, /fwa, /frq — COUNT: ~40
     Learning (building understanding): /teach, /lr, /fia, /fohw, /insd, /mem — COUNT: ~35
     Creating (generating new things): /create, /ma, /cda, /story, /pw, /w — COUNT: ~50
     GAP: "Recovering" state is significantly underserved relative to its importance.
     Also missing: the COMMUNICATING state (user knows what they think, needs to convey
     it to others), the WAITING state (user has acted and is now monitoring/uncertain
     about outcomes), and the MAINTAINING state (user has a working system and needs to
     keep it healthy).
```

---

## Phase 2: Cross-Dimensional Analysis

```
[G6] INTERSECTION_GAP:
     DIMENSIONS: Instant × Decision making
     EXISTING: /pick (barely)
     NEED: People make dozens of small decisions daily under time pressure. No skill
     gives you a 30-second decision heuristic.
     SEVERITY: critical
     EXAMPLE_USE_CASE: "Someone just asked me to take on a new project in a meeting.
     I have 10 seconds to respond. How do I quickly assess?"
```

```
[G7] INTERSECTION_GAP:
     DIMENSIONS: Simple × Communication/Conveyance
     EXISTING: None dedicated. /persua is analytical (how to persuade), not
     "help me structure what I want to say right now."
     NEED: The most common thinking task in professional life is "I need to
     communicate something and I'm not sure how to frame it." Not writing (long form)
     — framing (choosing what to say and how).
     SEVERITY: critical
     EXAMPLE_USE_CASE: "I need to give someone bad news. How do I structure this
     30-second conversation?"
```

```
[G8] INTERSECTION_GAP:
     DIMENSIONS: Easy × Recovery
     EXISTING: /panic exists but is a full framework. /rmm and /kta require
     reflection.
     NEED: Simple "I messed up, what do I do RIGHT NOW" triage — not analysis,
     just immediate next action.
     SEVERITY: significant
     EXAMPLE_USE_CASE: "I just sent the wrong email to the wrong person. What's
     my first move?"
```

```
[G9] INTERSECTION_GAP:
     DIMENSIONS: General × Maintenance/Monitoring
     EXISTING: /ret (retrospective) is post-hoc. No skill for ongoing monitoring
     of something that's currently working.
     NEED: Many thinking tasks aren't about building or fixing but about SUSTAINING.
     "Is this still working? What should I watch for? When should I intervene?"
     SEVERITY: significant
     EXAMPLE_USE_CASE: "My team process has been working for 3 months. How do I
     check if it's degrading before it breaks?"
```

```
[G10] INTERSECTION_GAP:
     DIMENSIONS: Simple × Self-awareness
     EXISTING: /sdc, /sid, /ecal are all sophisticated multi-phase skills.
     NEED: Quick cognitive bias checks. "Am I being dumb right now?" as a
     30-second sanity test, not a 20-minute analysis.
     SEVERITY: significant
     EXAMPLE_USE_CASE: "I'm about to make a purchase/hire/commitment. Quick
     gut check — am I thinking straight?"
```

```
[G11] INTERSECTION_GAP:
     DIMENSIONS: Moderate × Interpersonal/Group Thinking
     EXISTING: /col (collaboration design), /conflict (analysis), /trust (analysis).
     All are analytical — they analyze the situation. None help you THINK TOGETHER
     with others in real-time.
     NEED: Skills for group thinking processes — how to run a productive disagreement,
     how to synthesize multiple perspectives, how to facilitate a group toward a decision.
     SEVERITY: significant
     EXAMPLE_USE_CASE: "My team disagrees on the approach. How do I facilitate a
     conversation that produces a better answer than any individual has?"
```

```
[G12] INTERSECTION_GAP:
     DIMENSIONS: Quick × Estimation
     EXISTING: No dedicated estimation skill.
     NEED: Fermi estimation, quick sizing, order-of-magnitude reasoning. "How big
     is this? How long will this take? How many people does this affect?" These are
     among the most common thinking tasks in business and life.
     SEVERITY: critical
     EXAMPLE_USE_CASE: "How long will this migration take? I need a rough number
     for the meeting in 10 minutes."
```

```
[G13] INTERSECTION_GAP:
     DIMENSIONS: Standard × Teaching/Explanation
     EXISTING: /teach (Feynman explanation) explains concepts. No skill for
     designing how someone else should learn something.
     NEED: Curriculum/learning design — not "explain X to me" but "design how
     someone should learn X over time."
     SEVERITY: moderate
     EXAMPLE_USE_CASE: "I need to onboard a new team member on our system.
     What should they learn in what order?"
```

```
[G14] INTERSECTION_GAP:
     DIMENSIONS: Easy × Saying No / Boundary Setting
     EXISTING: /awtlytrn, /iagca, /ycshikfmif are scope-management skills
     but focused on scope of ANALYSIS, not personal/professional boundaries.
     NEED: "Should I take this on? How do I decline?" — practical boundary
     reasoning.
     SEVERITY: significant
     EXAMPLE_USE_CASE: "My boss asked me to take on a third project. I'm
     already stretched. How do I think through whether to push back, and how?"
```

---

## Phase 3: Thinking Mode Coverage

```
[G15] THINKING_MODE: Divergent thinking
     DEFINITION: Generate many different options
     EXISTING_SKILLS: /se, /ma, /cda, /poa, /dd
     COVERAGE: strong
     IF_WEAK_OR_ABSENT: N/A
```

```
[G16] THINKING_MODE: Convergent thinking
     DEFINITION: Narrow from many to best
     EXISTING_SKILLS: /dcp, /cmp, /pick, /cba, /pri
     COVERAGE: strong
     IF_WEAK_OR_ABSENT: N/A
```

```
[G17] THINKING_MODE: Critical thinking
     DEFINITION: Test and challenge claims
     EXISTING_SKILLS: /stc, /advr, /aex, /ht, /redteam, /claim
     COVERAGE: strong
     IF_WEAK_OR_ABSENT: N/A
```

```
[G18] THINKING_MODE: Systems thinking
     DEFINITION: See interconnections and feedback loops
     EXISTING_SKILLS: /systhink, /fohw, /insd
     COVERAGE: adequate
     IF_WEAK_OR_ABSENT: N/A
```

```
[G19] THINKING_MODE: Lateral thinking
     DEFINITION: Approach from unexpected angles
     EXISTING_SKILLS: /iaw, /but, /reframe, /cda
     COVERAGE: adequate
     IF_WEAK_OR_ABSENT: N/A
```

```
[G20] THINKING_MODE: Analogical thinking
     DEFINITION: Transfer knowledge from one domain to another
     EXISTING_SKILLS: /mem (mental models) references this. No dedicated skill.
     COVERAGE: weak
     IF_WEAK_OR_ABSENT: Need a skill that systematically finds analogues:
     "What other domain has solved a problem structurally similar to mine?
     What can I borrow from that solution?"
```

```
[G21] THINKING_MODE: Counterfactual thinking
     DEFINITION: What if things were different?
     EXISTING_SKILLS: /fut (future analysis), /dys (dystopian futures) touch this.
     No dedicated "what if X had been different?" skill.
     COVERAGE: weak
     IF_WEAK_OR_ABSENT: Need a structured counterfactual analysis — "If we had
     done X instead of Y, what would be different now? What does that tell us
     about the causal structure?"
```

```
[G22] THINKING_MODE: Temporal thinking
     DEFINITION: Past patterns, present state, future projection
     EXISTING_SKILLS: /fut, /ret, /dys, /utp
     COVERAGE: adequate
     IF_WEAK_OR_ABSENT: Weak on PRESENT-STATE temporal thinking: "Where are we
     in the lifecycle of this thing?"
```

```
[G23] THINKING_MODE: Probabilistic thinking
     DEFINITION: Reason under uncertainty
     EXISTING_SKILLS: /pbr, /nsa, /it, /prob
     COVERAGE: adequate
     IF_WEAK_OR_ABSENT: N/A
```

```
[G24] THINKING_MODE: Adversarial thinking
     DEFINITION: What would an opponent do?
     EXISTING_SKILLS: /redteam, /advr, /stc
     COVERAGE: strong
     IF_WEAK_OR_ABSENT: N/A
```

```
[G25] THINKING_MODE: Empathic thinking
     DEFINITION: See from another's perspective
     EXISTING_SKILLS: /empth, /per, /persua (partially)
     COVERAGE: adequate
     IF_WEAK_OR_ABSENT: N/A
```

```
[G26] THINKING_MODE: Metacognitive thinking
     DEFINITION: Think about your own thinking process
     EXISTING_SKILLS: /sdc, /sid, /ecal, /meta
     COVERAGE: adequate
     IF_WEAK_OR_ABSENT: N/A
```

```
[G27] THINKING_MODE: Reductive thinking
     DEFINITION: Simplify complex things
     EXISTING_SKILLS: /sim, /smpl, /ezy
     COVERAGE: strong
     IF_WEAK_OR_ABSENT: N/A
```

```
[G28] THINKING_MODE: Constructive thinking
     DEFINITION: Build up from components
     EXISTING_SKILLS: /de, /to, /create, /action
     COVERAGE: adequate
     IF_WEAK_OR_ABSENT: N/A
```

```
[G29] THINKING_MODE: Dialectical thinking
     DEFINITION: Synthesis from opposing views
     EXISTING_SKILLS: /steelman addresses one side. /conflict maps both sides.
     No skill specifically synthesizes a THIRD position from two opposing views.
     COVERAGE: weak
     IF_WEAK_OR_ABSENT: Need a synthesis skill: "Here are two opposing positions.
     Generate a position that genuinely incorporates the strongest parts of both,
     not just a compromise but a transcendence."
```

```
[G30] THINKING_MODE: Estimation thinking
     DEFINITION: Quick sizing, Fermi estimates, order-of-magnitude reasoning
     EXISTING_SKILLS: None dedicated
     COVERAGE: absent
     IF_WEAK_OR_ABSENT: This is one of the most practically useful thinking
     modes and it's completely unrepresented. Need a Fermi estimation skill.
```

```
[G31] THINKING_MODE: Narrative thinking
     DEFINITION: Construct or deconstruct stories to understand meaning
     EXISTING_SKILLS: /story generates narratives. No skill DECONSTRUCTS
     narratives — "What story am I telling myself? What story is this person/
     organization telling? Is the narrative accurate or distorting reality?"
     COVERAGE: weak
     IF_WEAK_OR_ABSENT: Need a narrative deconstruction skill.
```

---

## Phase 4: Recommendations

```
[G32] RECOMMENDED_SKILL:
     NAME: /est — Fermi Estimation
     FILLS_GAP: Absent "estimation thinking" mode (G30), Instant/Quick speed gap (G4),
     Quick x Estimation intersection (G12)
     DIMENSIONS: Simple sophistication, Easy difficulty, Universal generality, Quick speed
     PURPOSE: Produce a defensible order-of-magnitude estimate for any quantity
     using decomposition, reference classes, and sanity checks.
     USER_ARRIVES: Needs a rough number and has no data
     USER_LEAVES: Has an estimate with explicit assumptions and a confidence range
     CORE_MECHANISM: Decompose the unknown quantity into factors you CAN estimate.
     Estimate each factor independently. Multiply. Sanity-check against known
     reference points. State the confidence interval. Takes 3-5 minutes.
     Example: "How many piano tuners in Chicago?" becomes population x piano
     ownership rate x tuning frequency / tuner capacity.
     PRIORITY: critical
     BUILD_COMPLEXITY: simple to build
```

```
[G33] RECOMMENDED_SKILL:
     NAME: /snap — Snap Decision
     FILLS_GAP: Instant x Decision making (G6), speed gap at Instant tier (G4)
     DIMENSIONS: Simple sophistication, Easy difficulty, Universal generality,
     Instant speed
     PURPOSE: Make a good-enough decision in under 60 seconds using a minimal
     checklist of the 3-4 things that actually matter.
     USER_ARRIVES: Has to decide something right now with no time to analyze
     USER_LEAVES: Has a defensible decision and knows what to watch for post-decision
     CORE_MECHANISM: Four questions: (1) What's the worst realistic outcome of each
     option? (2) Is this reversible or irreversible? (3) What would I tell a friend
     to do? (4) Decide — and note what would make you revisit. Irreversible
     decisions get a "STOP — take more time" flag. Reversible decisions get
     "pick and move."
     PRIORITY: critical
     BUILD_COMPLEXITY: simple to build
```

```
[G34] RECOMMENDED_SKILL:
     NAME: /frame — Message Framing
     FILLS_GAP: Simple x Communication gap (G7), missing "communicating" user
     state (G5)
     DIMENSIONS: Simple sophistication, Easy difficulty, Universal generality,
     Quick speed
     PURPOSE: Structure what you want to say to a specific person in a specific
     situation — not writing, but choosing what to include, what order, and what
     tone.
     USER_ARRIVES: Knows what they think, not sure how to say it
     USER_LEAVES: Has a structured message framework: lead with X, then Y,
     close with Z, in tone T
     CORE_MECHANISM: Four steps: (1) What does the listener need to HEAR (not
     what you want to say)? (2) What's the one sentence they should remember?
     (3) What's the emotional context — is the listener expecting this, dreading
     it, or indifferent? (4) Structure: context-message-ask, or ask-reason-
     context, depending on urgency and relationship.
     PRIORITY: critical
     BUILD_COMPLEXITY: simple to build
```

```
[G35] RECOMMENDED_SKILL:
     NAME: /anl — Analogical Transfer
     FILLS_GAP: Weak analogical thinking mode (G20)
     DIMENSIONS: Moderate sophistication, Medium difficulty, Universal generality,
     Standard speed
     PURPOSE: Find structurally similar problems in other domains and transfer
     their solutions, adapting for context differences.
     USER_ARRIVES: Stuck on a problem, needs a fresh approach from outside
     their domain
     USER_LEAVES: Has 2-3 analogues from other fields with specific transferable
     insights and explicit notes on where the analogy breaks down
     CORE_MECHANISM: (1) Abstract your problem to its structural essence — strip
     domain-specific details. (2) Identify the core dynamic (coordination problem?
     incentive misalignment? search problem? scaling bottleneck?). (3) Find 3
     domains that face the same structural dynamic. (4) Examine how each domain
     solved it. (5) Map solutions back to your domain, noting where the analogy
     holds and where it breaks. (6) Synthesize: what principle generalizes
     across all analogues?
     PRIORITY: high
     BUILD_COMPLEXITY: moderate
```

```
[G36] RECOMMENDED_SKILL:
     NAME: /synth — Dialectical Synthesis
     FILLS_GAP: Weak dialectical thinking mode (G29)
     DIMENSIONS: Sophisticated, Hard difficulty, Universal generality, Standard speed
     PURPOSE: Given two opposing positions, generate a third position that
     genuinely transcends both — not a compromise but an integration that
     captures what each side is right about.
     USER_ARRIVES: Sees two sides of an argument, suspects both are partially
     right, can't reconcile them
     USER_LEAVES: Has a synthesis position with explicit reasoning for what
     was kept, what was discarded, and why the synthesis is stronger than either
     original position
     CORE_MECHANISM: (1) Steelman both positions to their strongest form.
     (2) Identify what SPECIFIC insight each position captures that the other
     misses. (3) Identify the hidden assumption that makes them SEEM contradictory.
     (4) Ask: "Under what conditions is A right? Under what conditions is B
     right?" If the answer reveals different conditions, the synthesis is
     conditional. (5) Construct the synthesis: a position that includes A's
     insight + B's insight + the resolution of the hidden tension. (6) Test:
     would a strong advocate of A and B each agree this captures their core
     concern?
     PRIORITY: high
     BUILD_COMPLEXITY: moderate
```

```
[G37] RECOMMENDED_SKILL:
     NAME: /dmg — Damage Control
     FILLS_GAP: Easy x Recovery intersection (G8), underserved Recovery user
     state (G5)
     DIMENSIONS: Simple sophistication, Easy difficulty, Universal generality,
     Instant speed
     PURPOSE: Immediate triage after a mistake — not analysis of what went
     wrong, but "what's my first move in the next 5 minutes?"
     USER_ARRIVES: Just made a mistake, feeling the adrenaline, needs to act
     NOW not think
     USER_LEAVES: Has taken the right first action and has a short list of
     next steps
     CORE_MECHANISM: (1) STOP — do nothing for 10 seconds (prevent compounding
     the error). (2) Classify: is the damage still happening or already done?
     If still happening, stop the bleeding first. (3) Who needs to know? Tell
     them now — bad news doesn't improve with age. (4) What's the single most
     important thing to do in the next hour? Do that. (5) Schedule the real
     retrospective for later — right now, execute.
     PRIORITY: high
     BUILD_COMPLEXITY: simple to build
```

```
[G38] RECOMMENDED_SKILL:
     NAME: /bias — Quick Bias Check
     FILLS_GAP: Simple x Self-awareness intersection (G10)
     DIMENSIONS: Simple sophistication, Easy difficulty, Universal generality,
     Quick speed
     PURPOSE: Run through the 5-6 most common cognitive biases that derail
     decisions and check if any are active right now.
     USER_ARRIVES: About to make a decision or commitment, wants a quick sanity
     check
     USER_LEAVES: Either confirmed "thinking seems sound" or flagged a specific
     bias that needs addressing
     CORE_MECHANISM: Rapid checklist of the most decision-distorting biases:
     (1) Sunk cost — "Am I continuing because of what I've already invested?"
     (2) Confirmation — "Have I only looked at evidence that supports my
     preference?" (3) Anchoring — "Is my number based on real analysis or
     the first number I heard?" (4) Availability — "Am I overweighting a
     vivid recent example?" (5) Status quo — "Am I choosing this because
     it's the default?" (6) Social proof — "Am I doing this because others
     are?" For each: yes/no and, if yes, one sentence on how to adjust.
     PRIORITY: high
     BUILD_COMPLEXITY: simple to build
```

```
[G39] RECOMMENDED_SKILL:
     NAME: /narr — Narrative Deconstruction
     FILLS_GAP: Weak narrative thinking mode (G31)
     DIMENSIONS: Moderate sophistication, Medium difficulty, Universal generality,
     Standard speed
     PURPOSE: Identify the narrative being told (by you, by someone else, by an
     organization) and test whether it's accurate or distorting reality.
     USER_ARRIVES: Senses that a story is being told that might not reflect
     reality, or realizes they're telling themselves a story
     USER_LEAVES: Can see the narrative, its distortions, and the reality
     underneath — and can choose whether to keep or revise the story
     CORE_MECHANISM: (1) State the narrative in one paragraph — the story as
     told. (2) Identify the protagonist, antagonist, and moral of the story.
     (3) What facts does the narrative OMIT? (4) What alternative narrative
     could you tell with the SAME facts? (5) Who benefits from this narrative
     being believed? (6) What would a neutral observer's narrative look like?
     (7) Revised understanding: what's actually true, stripped of narrative
     framing?
     PRIORITY: high
     BUILD_COMPLEXITY: moderate
```

```
[G40] RECOMMENDED_SKILL:
     NAME: /hlth — System Health Check
     FILLS_GAP: General x Maintenance/Monitoring intersection (G9), missing
     "maintaining" user state (G5)
     DIMENSIONS: Moderate sophistication, Medium difficulty, Universal generality,
     Standard speed
     PURPOSE: Assess whether a currently-working system (team, process, product,
     relationship, habit) is healthy or silently degrading.
     USER_ARRIVES: Has something that's working and wants to know if it's still
     sound
     USER_LEAVES: Knows which vital signs are healthy, which are concerning,
     and what specifically to monitor or intervene on
     CORE_MECHANISM: (1) Identify the system's vital signs — what metrics or
     observations indicate health? (2) Check leading indicators (not lagging) —
     what degrades BEFORE you see failure? (3) Compare current state to the
     system at its best — what's changed? (4) Identify the single biggest risk
     to continued health. (5) Prescribe: monitor X, intervene if Y, schedule
     next check-in for Z.
     PRIORITY: medium
     BUILD_COMPLEXITY: moderate
```

```
[G41] RECOMMENDED_SKILL:
     NAME: /cfact — Counterfactual Analysis
     FILLS_GAP: Weak counterfactual thinking mode (G21)
     DIMENSIONS: Moderate sophistication, Medium difficulty, Universal generality,
     Standard speed
     PURPOSE: Analyze what would have happened if a different choice had been
     made, to extract causal understanding and improve future decisions.
     USER_ARRIVES: Made a decision (good or bad outcome) and wants to understand
     whether the decision actually caused the outcome
     USER_LEAVES: Understands the causal structure — what was due to the
     decision vs. luck/context — and has extracted transferable lessons
     CORE_MECHANISM: (1) State the actual decision and its outcome. (2) Identify
     the most plausible alternative decision. (3) Trace the counterfactual:
     given everything else being equal, what would have happened? (4) Identify
     where the paths diverge — THAT is where the decision actually mattered.
     (5) Identify where the paths stay similar — THAT is where context/luck
     dominated. (6) Lesson: "This decision mattered for X but not for Y.
     Next time, focus on X."
     PRIORITY: medium
     BUILD_COMPLEXITY: moderate
```

```
[G42] RECOMMENDED_SKILL:
     NAME: /bound — Boundary Reasoning
     FILLS_GAP: Easy x Boundary Setting intersection (G14)
     DIMENSIONS: Simple sophistication, Easy difficulty, Universal generality,
     Quick speed
     PURPOSE: Decide whether to take something on or decline, and if declining,
     how to do it clearly and non-defensively.
     USER_ARRIVES: Asked to commit to something, feeling pressure, not sure
     whether to accept
     USER_LEAVES: Has a clear yes/no with reasoning, and if no, has the actual
     words to say
     CORE_MECHANISM: (1) What am I saying yes TO? (Specific time, energy,
     opportunity cost.) (2) What am I saying no to BY saying yes to this?
     (What gets crowded out?) (3) If I imagine having already said no, do I
     feel relief or regret? (4) If declining: state what you're declining,
     why briefly (not defensively), and what you CAN offer instead. Provide
     the actual script.
     PRIORITY: high
     BUILD_COMPLEXITY: simple to build
```

```
[G43] RECOMMENDED_SKILL:
     NAME: /facil — Facilitated Group Thinking
     FILLS_GAP: Moderate x Interpersonal/Group intersection (G11)
     DIMENSIONS: Moderate sophistication, Medium difficulty, Broad generality,
     Standard speed
     PURPOSE: Design and run a structured group thinking process that produces
     better answers than any individual in the group.
     USER_ARRIVES: Has a group that needs to think together about something
     and wants to avoid groupthink, loudest-voice-wins, and analysis paralysis
     USER_LEAVES: Has a facilitation plan with specific steps, time boxes,
     and techniques for drawing out diverse views and converging
     CORE_MECHANISM: (1) Identify the thinking task: is the group diverging
     (generating), converging (deciding), or evaluating (judging)? (2) Match
     to technique: silent individual brainstorm then share (diverging),
     criteria-first then score (converging), red team / steelman pairs
     (evaluating). (3) Design the sequence: individual thinking first, then
     share, then build, then decide. (4) Assign roles: facilitator,
     timekeeper, devil's advocate. (5) Set explicit decision rule: consensus,
     majority, HIPPO-with-input, etc.
     PRIORITY: medium
     BUILD_COMPLEXITY: moderate
```

---

## Phase 5: Priority Matrix

```
SKILL GAP PRIORITY MATRIX
==========================

CRITICAL GAPS (create these first):
  1. /est — Fermi Estimation — FILLS: absent estimation thinking mode, instant/quick
     speed gap — COMPLEXITY: simple to build
  2. /snap — Snap Decision — FILLS: instant x decision intersection — COMPLEXITY:
     simple to build
  3. /frame — Message Framing — FILLS: simple x communication gap, missing
     "communicating" user state — COMPLEXITY: simple to build

HIGH PRIORITY:
  1. /bias — Quick Bias Check — FILLS: simple x self-awareness gap
  2. /dmg — Damage Control — FILLS: easy x recovery gap, underserved recovery state
  3. /bound — Boundary Reasoning — FILLS: easy x boundary-setting gap
  4. /anl — Analogical Transfer — FILLS: weak analogical thinking mode
  5. /synth — Dialectical Synthesis — FILLS: weak dialectical thinking mode
  6. /narr — Narrative Deconstruction — FILLS: weak narrative thinking mode

MEDIUM PRIORITY:
  1. /hlth — System Health Check — FILLS: general x maintenance gap
  2. /cfact — Counterfactual Analysis — FILLS: weak counterfactual thinking mode
  3. /facil — Facilitated Group Thinking — FILLS: moderate x interpersonal gap

NICE TO HAVE:
  (Identified but not specified in detail — would warrant future /skgap runs)
  1. /lifecycle — "Where are we in the lifecycle of this thing?" (temporal
     thinking for present state)
  2. /onboard — Learning path design / curriculum structure for onboarding
     someone to a new domain
  3. /preread — Quick pre-meeting preparation framework ("what should I know
     and what should I ask?")
  4. /scale — "Will this approach still work at 10x?" — scaling analysis
  5. /unlearn — Identifying and letting go of beliefs/practices that were once
     useful but aren't anymore

DIMENSION SUMMARY:
  Most underrepresented sophistication level: Simple analytical skills (many
  simple STATE-ENTRY skills exist, but few simple THINKING TOOLS)
  Most underrepresented difficulty level: Easy (for analytical tasks, not
  just routing/emotional support)
  Most underrepresented user state: Communicating (knows what to think, needs
  to convey it), Maintaining (has a working thing, needs to keep it healthy),
  and Recovering (at the easy/instant end)
  Most underrepresented thinking mode: Estimation thinking (completely absent),
  followed by analogical, dialectical, counterfactual, and narrative
  deconstruction (all weak)

PATTERN INSIGHT:
  The toolkit is heavily weighted toward ANALYTICAL sophistication — skills
  for when you have time to sit down and think deeply. The biggest systemic
  gap is OPERATIONAL thinking — quick tools for the moment you're in. The
  toolkit serves the study well but underserves the field. The recommended
  critical-priority skills (/est, /snap, /frame) all address this: they're
  fast, simple, and designed for people who need to think WHILE doing, not
  thinking ABOUT doing.

READY FOR:
- /cs [skill spec] — to create the recommended skills
- /mts [skill spec] — alternative creation path
- /imprt — to combine gap analysis with quality improvement
```

---

## Pre-Completion Checklist

- [x] All 5 core dimensions mapped with counts
- [x] Cross-dimensional intersections analyzed (9 intersections)
- [x] Thinking modes checked for coverage (all 15 + 2 additional modes)
- [x] Each recommendation is specific enough to build (passes specificity test)
- [x] Each recommendation is distinct from existing skills (passes distinctness test)
- [x] Recommendations span multiple sophistication and difficulty levels (Simple through Sophisticated, Easy through Hard)
- [x] Priority matrix has clear ordering (3 Critical, 6 High, 3 Medium, 5 Nice-to-Have)
- [x] Simple/easy skills represented in recommendations (/snap, /frame, /bias, /dmg, /bound are all Simple/Easy)
