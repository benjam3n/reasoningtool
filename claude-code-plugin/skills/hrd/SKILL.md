---
name: "hrd - Hard Mode Analysis"
description: "Apply maximum rigor to a problem — no shortcuts, no defaults, no simplifications. Every assumption surfaced, every edge case considered, every tradeoff explicit. For when getting it wrong is expensive."
output:
  format: "prose"
---

# Hard Mode Analysis

**Input**: $ARGUMENTS

---

## Core Principles

1. **Hard mode means no invisible assumptions.** Every assumption must be surfaced, stated, and evaluated. If the analysis rests on "X is probably true," hard mode requires specifying what "probably" means (70%? 95%?), what changes if X is false, and how to verify X.

2. **Hard mode means no shortcuts.** Easy mode provides defaults. Hard mode makes you choose. Simple mode skips edge cases. Hard mode enumerates them. This isn't complexity for its own sake — it's for situations where the shortcuts could be the thing that causes failure.

3. **Hard mode is justified by stakes.** Use hard mode when the cost of being wrong is high: irreversible decisions, high-stakes commitments, safety-critical systems, situations where you'll live with the consequences for years. Don't use it for lunch choices.

4. **Completeness is the goal, not difficulty.** Hard mode isn't hard because it's confusing — it's hard because it's thorough. Every step should be clear. The difficulty comes from the number of things to consider, not from the opacity of the analysis.

5. **Hard mode produces a decision audit trail.** Every conclusion must be traceable to evidence and reasoning. Someone reviewing the analysis should be able to see exactly why each conclusion was reached, what was considered and rejected, and where uncertainty remains.

---

## Phase 1: Scope and Stakes

```
[H1] PROBLEM: [the problem or decision]
[H2] STAKES: [what happens if you get this wrong — be specific]
[H3] IRREVERSIBILITY: [how hard is it to undo this decision?]
[H4] TIME_PRESSURE: [how much time for analysis? hard mode takes time]
[H5] HARD_MODE_JUSTIFIED: [yes/no — is the rigor warranted by the stakes?]
```

→ If hard mode isn't justified, say so and route to `/ezy` or `/smpl`.

---

## Phase 2: Assumption Audit

Surface every assumption the analysis rests on.

```
[H-N] ASSUMPTION: [stated assumption]
     SOURCE: [where this assumption comes from — data, experience, convention, guess]
     CONFIDENCE: [0-100% with reasoning]
     IF_WRONG: [what changes if this assumption is false]
     VERIFICATION: [how to test this assumption]
     STATUS: [verified | plausible | uncertain | untestable]
```

### Required Assumption Categories

| Category | What to Check |
|----------|--------------|
| **Factual** | Data points, statistics, reported facts |
| **Causal** | "X causes Y" — is the mechanism confirmed? |
| **Scope** | "This applies in our context" — does it? |
| **Temporal** | "This will still be true in [timeframe]" |
| **Behavioral** | "People/systems will respond by [doing X]" |
| **Resource** | "We have/can get [resource]" |
| **Environmental** | "The context won't change significantly" |

---

## Phase 3: Full Option Enumeration

List ALL options, not just the obvious ones.

```
[H-N] OPTION: [option name]
     DESCRIPTION: [what this option entails — specifically]
     REQUIREMENTS: [what must be true for this option to work]
     BEST_CASE: [outcome if everything goes well]
     WORST_CASE: [outcome if things go badly]
     EXPECTED_CASE: [most likely outcome with reasoning]
     EDGE_CASES: [unusual situations where this option behaves differently]
     SECOND_ORDER: [downstream effects beyond the immediate outcome]
     IRREVERSIBILITY: [how hard to undo if this option fails]
     DEPENDENCIES: [what this option depends on — people, resources, timing]
```

### Option Completeness Check

- [ ] "Do nothing" considered as an option
- [ ] "Do the opposite of instinct" considered
- [ ] Options from analogous situations in other domains considered
- [ ] Combinations of options considered
- [ ] Partial versions of options considered

---

## Phase 4: Risk Enumeration

For the most promising options, enumerate all risks:

```
[H-N] RISK: [risk description]
     PROBABILITY: [low | medium | high — with reasoning]
     IMPACT: [low | medium | high | catastrophic — with reasoning]
     DETECTION: [how would you know this risk is materializing?]
     MITIGATION: [what reduces probability or impact]
     CONTINGENCY: [what to do if it happens]
     RESIDUAL_RISK: [risk remaining after mitigation]
```

### Risk Categories to Check

| Category | Examples |
|----------|---------|
| **Known risks** | Identified and quantifiable |
| **Known unknowns** | Identified but not quantifiable |
| **Failure modes** | Specific ways each option could fail |
| **Interaction risks** | Risks from combining factors |
| **Timing risks** | Risks from doing this now vs. later |
| **Reputation risks** | How this looks to others |
| **Precedent risks** | What this commits you to in the future |

---

## Phase 5: Tradeoff Matrix

```
[H-N] TRADEOFF: [option A] vs [option B]
     A_ADVANTAGE: [where A is better]
     B_ADVANTAGE: [where B is better]
     DECISIVE_FACTOR: [what determines which advantage matters more]
     PREFERENCE_IF: [choose A if..., choose B if...]
```

For the top 2-3 options, construct:

```
TRADEOFF MATRIX
                    | Option A | Option B | Option C |
  Best case         |          |          |          |
  Worst case        |          |          |          |
  Expected case     |          |          |          |
  Irreversibility   |          |          |          |
  Time to result    |          |          |          |
  Resource cost     |          |          |          |
  Risk level        |          |          |          |
  Upside potential  |          |          |          |
```

---

## Phase 6: Decision and Audit Trail

```
HARD MODE ANALYSIS
==================

PROBLEM: [stated]
STAKES: [why hard mode]

ASSUMPTIONS (verified):
  [list verified assumptions with confidence levels]

ASSUMPTIONS (uncertain):
  [list uncertain assumptions — these are the biggest risk]

OPTIONS CONSIDERED: [N total]
  ELIMINATED: [options and why each was eliminated]
  FINAL CANDIDATES: [2-3 with tradeoff summary]

RISKS:
  [top risks with probability × impact ranking]

RECOMMENDATION: [choice with full reasoning]
  BECAUSE: [specific reasons, traced to evidence]
  DESPITE: [acknowledged downsides]
  CONTINGENCY: [what to do if it goes wrong]
  REVIEW_TRIGGER: [what would cause you to revisit this decision]

CONFIDENCE: [level with specific sources of uncertainty]
AUDIT_TRAIL: [every major judgment call, what was considered, what was rejected]

READY FOR:
- /ezy — if this was too much and you want the simple version
- /soph — for structural analysis of the chosen option
- /ar — to explore what follows from the recommendation
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Analysis paralysis** | Hard mode produced so much analysis that no decision was reached | The goal is a DECISION, not a document. Force a recommendation |
| **Unjustified rigor** | Hard mode applied to a low-stakes reversible decision | Check stakes first. Route to /ezy or /smpl if unwarranted |
| **Assumptions unsurfaced** | Analysis proceeded on hidden assumptions | Run the assumption audit categories. Every category must be checked |
| **Options too narrow** | Only considered 2-3 obvious options | Run the completeness check. Consider opposites, combinations, partials |
| **Risk blind spots** | Only considered technical risks, missed reputational or precedent risks | Check all risk categories |
| **No contingency** | Recommendation made but no plan for failure | Every recommendation needs: what if I'm wrong? |
| **False precision** | "73.2% chance of success" without basis | Confidence levels must be justified. Don't quantify beyond your actual knowledge |

---

## Depth Scaling

| Depth | Assumptions | Options | Risks | Tradeoffs |
|-------|-----------|---------|-------|-----------|
| 1x | Top 5 | 3-4 | Top 3 | Key tradeoff |
| 2x | Full audit | 5-7 | Full enumeration | Full matrix |
| 4x | Full + sensitivity analysis | All + combinations | Full + interaction risks | Full + scenario analysis |
| 8x | Full + adversarial challenge | Exhaustive | Full + pre-mortem | Full + decision tree |

Default: 2x. These are floors.

---

## Pre-Completion Checklist

- [ ] Stakes justified hard mode
- [ ] All assumption categories checked
- [ ] Each uncertain assumption has an if-wrong analysis
- [ ] "Do nothing" considered as an option
- [ ] Options include non-obvious alternatives
- [ ] All risk categories checked
- [ ] Tradeoffs between top options made explicit
- [ ] Recommendation includes contingency plan
- [ ] Review trigger specified (when to revisit)
- [ ] Audit trail is complete (every judgment call documented)

---

## Integration

- Use from: high-stakes decisions, irreversible commitments, safety-critical analysis
- Routes to: `/ar` (explore consequences of recommendation), `/soph` (structural analysis)
- Complementary: `/ezy` (opposite — minimum cognitive load path)
- Differs from `/ezy`: ezy minimizes complexity; hrd maximizes thoroughness
- Differs from `/soph`: soph pursues structural insight; hrd pursues completeness and rigor
- Differs from `/certainty`: certainty pursues maximum confidence on truth claims; hrd pursues maximum rigor on decisions
- Differs from `/dcp`: dcp is a decision-making framework; hrd is a rigor level applied to any analysis
