---
name: "unsure - Not Sure About This"
description: "For mild uncertainty — you have a direction but aren't confident. A decision tree to move from hesitation to action or justified pause."
---

# Unsure - Not Sure About This

**Input**: $ARGUMENTS

---

## Core Principles

1. **Uncertainty is information, not weakness.** Being unsure means you're aware of risk, complexity, or missing data. That awareness is an asset. The goal isn't to eliminate uncertainty — it's to make it actionable.

2. **Most uncertainty is resolvable.** The question is whether it's worth resolving BEFORE acting or whether you can resolve it BY acting.

3. **Confidence is not binary.** You don't need to go from unsure to certain. You need to go from unsure to "sure enough to move."

4. **The cost of waiting matters.** Uncertainty sometimes justifies delay. But delay has its own cost — missed windows, accumulated anxiety, lost momentum. Weigh both sides.

---

## Phase 1: Name the Uncertainty

```
[U1] WHAT_UNSURE_ABOUT: [state it precisely — not "I'm not sure" but "I'm not sure whether X because Y"]
[U2] CURRENT_LEAN: [which way are you leaning, even slightly?]
[U3] STAKES: [what happens if you're wrong?]
```

---

## Phase 2: What Would Make You Sure?

```
[U4] CERTAINTY_SOURCE: What kind of input would resolve this?
```

| Source | Example | Speed |
|--------|---------|-------|
| **Information** | A fact you don't have yet | Minutes to days |
| **Validation** | Someone confirming your thinking | Hours to days |
| **Experience** | You've never done this before | Only gained by doing |
| **Time** | You need to see how things develop | Days to weeks |
| **Gut check** | You know but don't trust yourself | Already available |

```
[U5] IDENTIFIED_SOURCE: [information | validation | experience | time | gut]
```

---

## Phase 3: Decision Tree

```
Can you get that certainty quickly (< 1 day)?
├── YES → Go get it. Then decide.
│   [U6] ACTION: [specific step to get the information/validation/etc.]
│   → Return here after.
│
└── NO → Is the cost of being wrong recoverable?
    ├── YES (recoverable) → Proceed with a checkpoint.
    │   [U7] PROCEED_ACTION: [what to do now]
    │   [U8] CHECKPOINT: [when/how to check if this was right]
    │   [U9] REVERSAL_COST: [what it takes to undo if wrong]
    │   "Act, check, adjust. Don't wait for certainty you can't get cheaply."
    │
    └── NO (not easily recoverable) → Invest in certainty.
        [U10] INVESTMENT: [what it takes to become more sure]
        [U11] TIMELINE: [how long this investment takes]
        [U12] MINIMUM_CONFIDENCE: [what level of certainty justifies acting]
        "This is worth slowing down for. The cost of being wrong exceeds the cost of waiting."
```

---

## Phase 4: Gut Check Override

Before following the tree, check:

```
[U13] GUT_SAYS: [what does your instinct say, separate from analysis?]
[U14] GUT_CONFLICT: [does your gut conflict with the decision tree result?]
```

If gut conflicts with the tree:
- Gut says GO but tree says WAIT → Check if you're avoiding the discomfort of uncertainty rather than responding to actual risk
- Gut says WAIT but tree says GO → Check if there's information your gut is processing that your analysis missed. Name it if you can.

---

## Phase 5: Output

```
NOT SURE ABOUT THIS
===================

UNCERTAINTY: [precise statement of what's unsure]
LEANING: [current lean]
STAKES: [what's at risk]

WHAT WOULD HELP: [certainty source]
CAN GET IT QUICKLY: [yes/no]

RECOMMENDATION:
  [One of three paths:]
  a) GET THE INFO: [specific action] — then decide
  b) PROCEED WITH CHECKPOINT: [action] — check at [checkpoint]
  c) INVEST IN CERTAINTY: [what to do] — timeline [X]

GUT CHECK: [aligned / conflicting — with note if conflicting]

READY FOR:
- /dcp [decision] — if this is really a decision between options
- /aex [assumption] — if the uncertainty is about an assumption you're making
- /ht [hypothesis] — if you want to test your lean before committing
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Analysis paralysis** | User keeps seeking certainty for a recoverable decision | Name the recoverability explicitly — "If wrong, you can [undo action] at [cost]" |
| **False urgency** | Pushing to act when stakes are genuinely high | Check stakes honestly — not everything is recoverable |
| **Gut dismissal** | Ignoring intuition because the tree says otherwise | Gut check is mandatory, not optional |
| **Certainty theater** | Going through motions of research without actually resolving uncertainty | Ask: "Will this information actually change your decision?" |
| **Proxy uncertainty** | Unsure about X but the real issue is Y | If the named uncertainty feels thin, dig one level deeper |

---

## Depth Scaling

| Depth | Phases | Decision Tree | Gut Check |
|-------|--------|--------------|-----------|
| 1x | Name + tree | Single path | Skip |
| 2x | Name + tree + gut | Single path + gut | Include |
| 4x | Full + multiple scenarios | All paths explored | Deep gut analysis |
| 8x | Full + meta-analysis of uncertainty patterns | Full tree + second-order effects | Gut + pattern history |

Default: 2x. These are floors.

---

## Pre-Completion Checklist

- [ ] Uncertainty named precisely (not vague)
- [ ] Current lean identified (even if slight)
- [ ] Stakes assessed honestly
- [ ] Certainty source identified
- [ ] Decision tree followed to a recommendation
- [ ] Gut check performed and noted
- [ ] Recommendation is specific and actionable

---

## Integration

- Use from: "I'm not sure", "I think so but...", "maybe I should", mild hesitation
- Routes to: `/dcp` (decision process), `/aex` (assumption examination), `/ht` (hypothesis testing)
- Differs from `/idk`: idk has no direction; unsure has a direction but lacks confidence
- Differs from `/cnfsd`: cnfsd doesn't understand something; unsure understands but doesn't trust
- Differs from `/dcp`: dcp compares defined options; unsure may not have clear options yet
