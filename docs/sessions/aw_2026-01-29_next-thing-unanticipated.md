# AW — The Next Thing Is Something I Haven't Anticipated

**Date**: 2026-01-29
**Depth**: 2x
**Input**: the next thing to do is something i havent anticipated

---

## Phase 1: EXPLORATION

### Step 1: State the Claim

```
CLAIM: The next thing to do (in developing this reasoning toolkit) is something I haven't anticipated.
STEELMAN: Complex projects always have emergent needs. The more you build, the more you discover what's missing. Given how much iteration this toolkit has already gone through (rewrites, structural fixes, new primitives), it's likely that usage will surface a need that isn't on any current roadmap.
```

### Step 2: Find Wrongness (Recurse)

```
[W1] "The next thing to do is something I haven't anticipated"
  Wrong because:

  [W2] The next thing to do is probably something you HAVE anticipated but haven't prioritized — Fatal
    Wrong because:
    [W3] You have a clear backlog: the skills were just rewritten, synced, committed. The "next" thing is likely maintenance you already know about (testing, docs, edge cases) — Serious
      Wrong because:
      [W4] Knowing maintenance exists isn't the same as knowing WHICH maintenance matters most — Conditional
        Wrong because:
        [W5] You can determine which maintenance matters most by using the tools you already built (/u on "what needs maintenance") — BEDROCK-TEST: Run /u on "what should I fix next" and see if the output matches your intuition
      [W6] The rewrite itself created known follow-up work: testing the new three-phase architecture with real inputs — Serious
        Wrong because:
        [W7] Testing is anticipated work, not unanticipated — BEDROCK-LOGIC: If you can name it, you anticipated it. Testing was discussed explicitly.
    [W8] Backlogs exist precisely because anticipated work accumulates faster than it gets done — Serious
      Wrong because:
      [W9] A backlog of anticipated items doesn't preclude an unanticipated item being more important — Conditional
        Wrong because:
        [W10] "More important" requires a comparison function, and you can't compare anticipated vs unanticipated because you don't know the unanticipated item — BEDROCK-LOGIC: You cannot rank what you cannot identify. Comparing known to unknown requires at minimum knowing the unknown exists.
      [W11] The claim isn't that unanticipated things DON'T exist, it's that the NEXT thing is unanticipated. The next thing is whatever you do next, which you choose from what you know — BEDROCK-OBSERVE: When you sit down to work, you pick from options you can see. Unanticipated things reveal themselves during work, not before.

  [W12] This claim is unfalsifiable and therefore vacuous — Fatal
    Wrong because:
    [W13] If everything unanticipated, you can never be wrong — the claim just absorbs all evidence — Serious
      Wrong because:
      [W14] It IS falsifiable: if you list your anticipated next steps and then actually do one of them, the claim is false — BEDROCK-TEST: List 5 anticipated next steps. Do the actual next thing. Check if it was on the list.
    [W15] Even if technically falsifiable, the claim functions as learned helplessness: "I can't plan because surprise will override" — Serious
      Wrong because:
      [W16] This framing discourages planning by making all plans feel provisional — Conditional
        Wrong because:
        [W17] Plans being provisional doesn't mean planning is useless — plans surface structure even when they change — Serious
          Wrong because:
          [W18] The claim might not be discouraging planning at all — it might be saying "stay alert for the unexpected" — BEDROCK-TENSION: The claim is genuinely ambiguous between "don't bother planning" and "plan but stay flexible." These lead to opposite behaviors.

  [W19] You're biased toward expecting the unexpected because you just went through a cycle of discovering problems you didn't anticipate (the AW skill failures, the wrong-project bug, the auto-save problem) — Fatal
    Wrong because:
    [W20] Recency bias: recent surprises make you overweight the probability of future surprises — Serious
      Wrong because:
      [W21] But the surprises weren't random — they were structural. The toolkit was undertested. Now it's been rewritten. The structural causes of surprise have been partially addressed — Serious
        Wrong because:
        [W22] "Partially addressed" means some surprise-causing structure remains — Conditional
          Wrong because:
          [W23] You can identify what remains unaddressed: the new three-phase architecture hasn't been stress-tested with real usage — BEDROCK-TEST: Run /araw and /uaua on a real problem and see if the numbered registry actually works as designed.
      [W24] The class of surprise changed: early surprises were "skills don't load" (infrastructure), then "skills produce bad output" (design). The next class is likely "skills produce good output but miss something" (coverage) — that's a predictable trajectory — Serious
        Wrong because:
        [W25] Predicting the CLASS of surprise isn't the same as anticipating the specific surprise — Conditional
          Wrong because:
          [W26] But if you know the class, you can design tests for the class. Run the skills, look for coverage gaps. That's anticipated work — BEDROCK-LOGIC: If you can describe the failure category, you can design detection for it. Detection = anticipation.

  [W27] The claim assumes the toolkit has a single "next thing" — but the next thing is likely multiple things in parallel — Serious
    Wrong because:
    [W28] There are at least three known parallel tracks: test the rewrites, build the community (subreddit), write documentation — Serious
      Wrong because:
      [W29] All three of those are anticipated — BEDROCK-OBSERVE: They were discussed in previous sessions and are visible in the repo (subreddit folder existed, README exists, skills exist to test).
    [W30] The "one next thing" framing is itself a simplification that prevents you from seeing the actual work structure — Conditional
      Wrong because:
      [W31] Serial "next thing" thinking is a known failure mode in project management — doing one thing when three things need parallel attention — BEDROCK-OBSERVE: The git history shows serial work (rewrite skills, then fix skills, then fix other skills) rather than parallel (test while writing).

  [W32] The claim might be a rationalization for not choosing — if the next thing is unknowable, you don't have to decide — Fatal
    Wrong because:
    [W33] "I can't know what's next" relieves the anxiety of prioritization — Serious
      Wrong because:
      [W34] But you DO know several next things: stress-test the three-phase skills, see if numbered registries actually improve output, check if the toolkit works for someone who isn't you — Serious
        Wrong because:
        [W35] Knowing options isn't the same as knowing which one matters most — Conditional
          Wrong because:
          [W36] You have a ranking method: VOI (value of information). The highest-VOI action is the one that, if wrong, costs the most. Testing the three-phase rewrite has the highest VOI because if it doesn't work, all the recent work was wasted — BEDROCK-LOGIC: VOI is defined as the value of resolving uncertainty. The rewrite is the largest recent uncertainty.
```

### Step 3: Find the Pattern

**Pattern: CONVERGENT** — Multiple branches converge on the same root finding:

The claim is wrong because the next things ARE anticipated. Specifically, branches W7, W14, W23, W26, W29, and W36 all converge on: **the next step is stress-testing the three-phase rewrite with real usage**, and that is entirely anticipated work.

The wrongness has a secondary pattern: the claim functions as **avoidance of prioritization** (W32-W36). Calling the next step "unanticipated" avoids having to choose among known options.

---

## Phase 2: CLAIM REGISTRY

```
CLAIM REGISTRY
==============

[W1] "The next thing to do is something I haven't anticipated" — STATUS: REJECTED
[W2] Next thing is probably anticipated but unprioritized — STATUS: SURVIVED
[W3] Next is likely known maintenance — STATUS: SURVIVED
[W4] Knowing maintenance exists ≠ knowing which matters most — STATUS: DAMAGED (W5 provides a method)
[W5] Can determine priority using own tools — STATUS: SURVIVED (BEDROCK-TEST)
[W6] Rewrite created known follow-up: testing — STATUS: SURVIVED
[W7] Testing is anticipated, not unanticipated — STATUS: SURVIVED (BEDROCK-LOGIC)
[W8] Backlogs accumulate anticipated work — STATUS: SURVIVED
[W9] Unanticipated item could be more important than backlog — STATUS: CONDITIONAL (requires W10)
[W10] Can't rank what you can't identify — STATUS: SURVIVED (BEDROCK-LOGIC)
[W11] You choose next steps from what you can see; unanticipated things reveal during work — STATUS: SURVIVED (BEDROCK-OBSERVE)
[W12] Claim is unfalsifiable/vacuous — STATUS: DAMAGED (W14 shows it IS falsifiable)
[W13] If everything unanticipated, claim absorbs all evidence — STATUS: DAMAGED
[W14] Falsifiable: list anticipated steps, do next thing, check — STATUS: SURVIVED (BEDROCK-TEST)
[W15] Claim functions as learned helplessness — STATUS: CONDITIONAL (depends on interpretation, W18)
[W16] Framing discourages planning — STATUS: CONDITIONAL
[W17] Plans are useful even when provisional — STATUS: SURVIVED
[W18] Claim is ambiguous between "don't plan" and "stay flexible" — STATUS: SURVIVED (BEDROCK-TENSION)
[W19] Biased toward expecting unexpected due to recent surprises — STATUS: SURVIVED
[W20] Recency bias overweights future surprise probability — STATUS: SURVIVED
[W21] Surprises were structural, and structure was partially fixed — STATUS: SURVIVED
[W22] "Partially" means some surprise structure remains — STATUS: CONDITIONAL
[W23] Can identify what's unaddressed: test three-phase architecture — STATUS: SURVIVED (BEDROCK-TEST)
[W24] Surprise class follows predictable trajectory: infra → design → coverage — STATUS: SURVIVED
[W25] Predicting class ≠ anticipating specific surprise — STATUS: CONDITIONAL
[W26] If you know the class, you can design detection = anticipation — STATUS: SURVIVED (BEDROCK-LOGIC)
[W27] Assumes single "next thing" but next is likely parallel — STATUS: SURVIVED
[W28] Three known parallel tracks exist — STATUS: SURVIVED
[W29] All three tracks are anticipated — STATUS: SURVIVED (BEDROCK-OBSERVE)
[W30] "One next thing" framing prevents seeing work structure — STATUS: CONDITIONAL
[W31] Serial thinking is a known project management failure mode — STATUS: SURVIVED (BEDROCK-OBSERVE)
[W32] Claim rationalizes not choosing — STATUS: SURVIVED
[W33] "Can't know next" relieves prioritization anxiety — STATUS: SURVIVED
[W34] You DO know several next things — STATUS: SURVIVED
[W35] Knowing options ≠ knowing which matters most — STATUS: CONDITIONAL
[W36] VOI ranking: test three-phase rewrite has highest VOI — STATUS: SURVIVED (BEDROCK-LOGIC)

TOTALS:
- Total claims: 36
- SURVIVED: 22
- DAMAGED: 3
- CONDITIONAL: 8
- REJECTED: 1 (the original claim W1)
- UNCERTAIN: 0
- Bedrock reached: 10 (3 TEST, 4 LOGIC, 2 OBSERVE, 1 TENSION)
```

---

## Phase 3: SYNTHESIS

```
ORIGINAL CLAIM: "The next thing to do is something I haven't anticipated"

VERDICT: REJECTED
DERIVED FROM: W2, W7, W11, W14, W23, W26, W29, W34, W36

WRONGNESS PATTERN: Convergent
ROOT CAUSE: The next things are anticipated — the claim confuses
"haven't prioritized" with "haven't anticipated."

WHAT THE WRONGNESS ANALYSIS ACTUALLY FOUND:
1. The next step is stress-testing the three-phase rewrite — this is
   entirely anticipated and has the highest VOI (W6, W7, W23, W36)
2. You're biased by recent surprises into expecting more surprises,
   but the structural causes of those surprises were addressed (W19-W26)
3. The surprise trajectory is predictable: infrastructure → design →
   coverage. You're now in the coverage phase. (W24, W26)
4. The claim functions as prioritization avoidance — calling the next
   step "unknown" avoids choosing among known options (W32-W36)
5. Serial "next thing" framing is itself a problem — there are at least
   three parallel tracks that are all anticipated (W27-W31)
6. The claim is genuinely ambiguous between "don't plan" and "stay
   flexible" — these lead to opposite behaviors (W18)
7. Plans remain useful even when provisional (W17)
8. You can use your own tools (/u) to surface what you haven't
   noticed, making the unanticipated anticipated (W5)

ALTERNATIVES DERIVED FROM ANALYSIS:
1. "The next thing to do is the highest-VOI anticipated item I haven't
   prioritized yet" — derived from W2, W36
2. "The next things to do are three parallel tracks I already know
   about" — derived from W28, W29
3. "The next thing to do is use /u on my own roadmap to surface blind
   spots" — derived from W5

TESTABLE PREDICTIONS:
- If you list 5 anticipated next steps right now and then observe what
  you actually do next, it will be on the list (W14)
- If you run /araw on a real problem, the numbered registry will reveal
  whether the three-phase rewrite works (W23)
- If you run /u on "what's missing from this toolkit," the output will
  contain items you already had a vague sense about but hadn't
  articulated (W5, W11)

UNRESOLVED:
- W18: Whether this claim was meant as "don't plan" or "stay flexible"
  — only you know your intent
- W22: What specific surprise-causing structure remains unaddressed —
  would need real usage testing to find out
```
