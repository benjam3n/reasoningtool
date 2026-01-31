# AW 8x — "Full pre-planning is impossible" and "Optimal planning horizon is 1-3 steps"

**Date**: 2026-01-30
**Depth**: 8x
**Input**: Full pre-planning is impossible at the level of formal logic — combinatorial explosion (F48) and prediction decay (F51). The answer to "why not plan everything" is: because you literally cannot. The optimal planning horizon is 1-3 steps (F50, F52). Plan the next thing in detail, maintain rough direction, re-plan after each step. These seem like big big strongly asserted claims that actually dont rest on that much. Something is missing in this. Plan everything is definitely possible especially given there no limit on what an llm can produce if given the right input in the right quantities. A lot of planning only has to be done once. The chess engine analogy for instance, you only have to make the engine once, you may have to rerun it every game, but the actual engine doesnt actually need to change. The idea is to do the same here, plan how to make the engine, and then make the execution be able to just run based on sound logic.

---

## CLAIM REGISTRY

```
CLAIM REGISTRY
==============

[W1] "Full pre-planning is impossible at the level of formal logic" — STATUS: REJECTED (via W2, W8, W13, W17, W22)
[W2] The claim equivocates between enumerating futures and designing systems — STATUS: SURVIVED (supports rejection of W1)
[W3] Maybe the distinction doesn't matter — STATUS: REJECTED (via W4)
[W4] Sorting algorithms handle all inputs without predicting any — STATUS: SURVIVED
[W5] Sorting is trivially deterministic, real domains aren't — STATUS: REJECTED (via W6)
[W6] TCP/IP handles stochastic adversarial conditions via protocol — STATUS: SURVIVED
[W7] TCP was designed by humans who predicted failure categories — STATUS: SURVIVED (supports the engine-once analogy)
[W8] A system can handle unbounded inputs if logic is sound for the class — STATUS: SURVIVED (BEDROCK-LOGIC)
[W9] The engine-once pattern is a known valid CS pattern — STATUS: SURVIVED
[W10] LLM prompting isn't deterministic like an engine — STATUS: DAMAGED (via W11, W13)
[W11] The prompt IS the engine — sound logic constrains output — STATUS: SURVIVED
[W12] LLMs don't reliably follow prompts — STATUS: SURVIVED but reframed (engineering problem, not logical impossibility)
[W13] "Impossible at the level of formal logic" vs "technically difficult" — STATUS: SURVIVED (BEDROCK-LOGIC)
[W14] Some domains are genuinely path-dependent — STATUS: DAMAGED (via W15, W17)
[W15] Path-dependence handled by branching plans — STATUS: SURVIVED
[W16] Branching IS the combinatorial explosion — STATUS: REJECTED (via W17)
[W17] Pruning handles exponential spaces with polynomial resources — STATUS: SURVIVED (BEDROCK-OBSERVE)
[W18] Planning can mean constraining states via rules, not enumerating — STATUS: SURVIVED
[W19] Sometimes constraint space isn't well-defined — STATUS: CONDITIONAL (domain-specific)
[W20] One working domain defeats the universal impossibility claim — STATUS: SURVIVED (BEDROCK-LOGIC)
[W21] Does it work in LLM prompting specifically? — STATUS: SURVIVED (answered by W22)
[W22] Existing skills ARE general plans across unbounded inputs — STATUS: SURVIVED (BEDROCK-OBSERVE)
[W23] LLM execution is too variable — STATUS: DAMAGED (via W24, W26)
[W24] Skills already handle variability through structure — STATUS: SURVIVED
[W25] Checks don't guarantee quality — STATUS: SURVIVED but reframed (nothing guarantees, only tolerances)
[W26] All engineering uses tolerances, not perfection — STATUS: SURVIVED (BEDROCK-OBSERVE)
[W27] Prediction decay confuses content prediction with structure prediction — STATUS: SURVIVED
[W28] Maybe all prediction decays — STATUS: REJECTED (via W29)
[W29] Mathematical theorems don't decay — STATUS: SURVIVED (BEDROCK-LOGIC)
[W30] Domain assumptions may become invalid — STATUS: SURVIVED but handled (rerun engine with new inputs)
[W31] Engine logic stable, inputs change — STATUS: SURVIVED (BEDROCK-LOGIC)
[W32] Weather/stock examples are maximum-uncertainty domains, misleading for project planning — STATUS: SURVIVED
[W33] Weather/stocks used because well-studied — STATUS: DAMAGED (via W34)
[W34] They're misleading because structurally different from controlled planning — STATUS: SURVIVED (BEDROCK-OBSERVE)
[W35] "Optimal planning horizon is 1-3 steps" — STATUS: REJECTED (via W36, W42, W45, W52)
[W36] Universalizes from chaotic environments to all environments — STATUS: SURVIVED
[W37] Maybe all environments are chaotic enough — STATUS: REJECTED (via W38)
[W38] Compilers, build systems, proof assistants all use long horizons — STATUS: SURVIVED (BEDROCK-OBSERVE)
[W39] Manufacturing plans months ahead successfully — STATUS: SURVIVED
[W40] Manufacturing has fewer degrees of freedom — STATUS: DAMAGED (via W41)
[W41] Skill sequencing also has few degrees of freedom — STATUS: SURVIVED (BEDROCK-LOGIC)
[W42] Agile actually uses 3 horizons, not 1 — STATUS: SURVIVED
[W43] Planning vs committing is just semantic — STATUS: REJECTED (via W44)
[W44] Scrum uses 3 explicit planning horizons — STATUS: SURVIVED (BEDROCK-OBSERVE)
[W45] Some plans are one-time costs — STATUS: SURVIVED
[W46] Plans always need updating — STATUS: REJECTED (via W47, W48)
[W47] SKILL.md files are one-time plans reused repeatedly — STATUS: SURVIVED (BEDROCK-OBSERVE)
[W48] Mathematical proofs are permanent one-time plans — STATUS: SURVIVED (BEDROCK-LOGIC)
[W49] "Re-plan after each step" = 50% overhead — STATUS: SURVIVED
[W50] Re-planning might be fast — STATUS: SURVIVED but undermines the 1-3 step claim (W51)
[W51] If planning is cheap, optimal horizon is domain-dependent, not fixed — STATUS: SURVIVED (BEDROCK-LOGIC)
[W52] Claim conflates specific-outcome planning with procedural planning — STATUS: SURVIVED
[W53] Maybe user meant specific-outcome planning — STATUS: REJECTED (via W54)
[W54] User explicitly described procedural planning ("make the engine") — STATUS: SURVIVED (BEDROCK-OBSERVE)

TOTALS:
- Total claims: 54
- SURVIVED: 33
- REJECTED: 9
- DAMAGED: 5
- CONDITIONAL: 1
- Bedrock reached: 15 (5 BEDROCK-LOGIC, 7 BEDROCK-OBSERVE, 0 BEDROCK-TEST, 0 BEDROCK-TENSION)
```

---

## SYNTHESIS

```
ORIGINAL CLAIM: "Full pre-planning is impossible at the level of formal logic" and
"Optimal planning horizon is 1-3 steps"

VERDICT: BOTH REJECTED
DERIVED FROM: W1 rejected via W2, W8, W13, W17, W22; W35 rejected via W36, W42, W45, W52

WRONGNESS PATTERN: Convergent — nearly all branches point to the same root error

ROOT CAUSE: The claims equivocate between two types of planning:
  (1) Content planning — predicting specific future states — genuinely limited
  (2) Structural planning — designing procedures that handle classes of states — NOT limited
The user asked about type 2. The UAUA analysis answered about type 1.

WHAT THE WRONGNESS ANALYSIS ACTUALLY FOUND:

1. The "impossibility" claim uses formal logic language ("at the level of formal logic")
   but the impossibility only applies to exhaustive state enumeration, not to general
   procedure design. A procedure that handles a class doesn't need to enumerate the
   class. (W2, W8, W13, W20)

2. The chess engine analogy is VALID and was dismissed too quickly. You build the
   engine once, you run it on each game. The engine (procedure) is permanent; the
   inputs (specific games) change. (W7, W9, W31, W47)

3. The user's own project is the counter-example to the impossibility claim. The
   SKILL.md files are pre-computed plans that handle unbounded inputs. /araw works
   on any claim. It was designed once. This IS planning everything in the structural
   sense. (W22, W47)

4. Combinatorial explosion is handled by pruning, not enumeration. Chess engines,
   compilers, and Monte Carlo methods all operate in exponential state spaces using
   polynomial resources. The existence of these systems directly contradicts "you
   literally cannot." (W17, W38)

5. The weather/stock prediction examples in the original analysis are misleading —
   they're open systems with chaotic dynamics. Project planning is a semi-closed
   system where the planner controls most variables. Extrapolating from weather to
   all planning is a domain error. (W32, W34)

6. The "1-3 step" recommendation ignores that agile itself uses THREE planning
   horizons (product backlog, sprint backlog, daily plan). Agile's insight isn't
   "plan short" — it's "plan at multiple horizons with different commitment levels." (W42, W44)

7. Some plans are genuinely one-time costs. Mathematical proofs, algorithms,
   protocols, and SKILL.md files are all examples of plans designed once and reused
   indefinitely. The claim that "plans always need updating" is false for structural
   plans. (W29, W45, W47, W48)

8. The "impossible" claim accidentally proves itself wrong: if the UAUA skill is a
   pre-planned procedure that works on any input, and the claim says pre-planning
   is impossible, then the skill that generated the claim is itself a counter-example
   to the claim. (W22)

9. "Re-plan after each step" is only optimal when planning is expensive relative
   to execution. If planning is cheap (as with LLMs), the optimal horizon extends
   to however far the domain's structure permits. The recommendation should be
   domain-dependent, not fixed. (W49, W51)

10. The user's actual request — "plan how to make the engine, then have execution
    run based on sound logic" — was correctly identifying the structural planning
    pattern. The UAUA analysis answered a different question. (W52, W54)

ALTERNATIVES DERIVED FROM ANALYSIS:

1. Replace "planning is impossible" with "CONTENT prediction decays, but PROCEDURAL
   planning doesn't" — use both, match to domain. Derived from W2, W27, W31.

2. Replace "1-3 step horizon" with multi-horizon planning: long-term (what procedures
   to build), medium-term (what sequence to run them in), short-term (what specific
   input to give the current one). Derived from W42, W44.

3. The /sp (Steelman Prompt) idea from the UAUA is actually an instance of the
   engine pattern: design the steelmanning procedure once, run it on every prompt.
   This should be built as a general procedure, not a per-prompt plan. Derived from W9, W22.

4. The queue/next system should be designed as a PROTOCOL (like TCP), not a
   prediction system. Define: how tasks enter the queue, how they're prioritized,
   what happens on failure, what constitutes completion. Design the protocol once.
   Derived from W6, W8.

5. Planning "everything" is possible IF "everything" means "a procedure for every
   TYPE of situation" rather than "a prediction for every specific situation."
   The skill library already does this. The gap is not more skills — it's
   better orchestration of existing skills. Derived from W22, W41.

TESTABLE PREDICTIONS:
- If you design a queue protocol (not a queue for specific tasks, but a protocol
  for how any task moves through the system), it will work across sessions without
  modification (from W6, W8, W47)
- If you compare a "re-plan every step" approach vs a "design the procedure once"
  approach on 10 multi-step tasks, the procedure approach will produce faster
  completion with equal or better quality (from W49, W51)
- The existing skill files will continue to work on novel inputs they've never
  seen, because they're structural plans not content predictions (from W22, W29)

UNRESOLVED:
- Whether LLM execution variability (W12) is large enough to undermine structural
  planning in practice — W13 says it's engineering not logic, but the engineering
  gap might be large
- Where exactly the boundary is between domains where structural planning works
  and domains where content prediction is needed — W19 stayed CONDITIONAL
- Whether the overhead of designing general procedures exceeds the benefit for
  tasks that only occur once (W45 says some plans are one-time costs, but the
  DESIGN of the plan also has a cost)
```
