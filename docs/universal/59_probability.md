# Universal: Probability and Uncertainty (59)

**Category**: MATHEMATICAL - Probability Analysis
**Source**: [O: universal_goal_analysis.yaml lines 2034-2078 probability_and_uncertainty category]
**Structure**: One question per entry, VOI-marked with realistic distribution

---

## VOI Rating = Action Divergence

- **HIGH**: Different answers → completely different action paths
- **MED**: Different answers → same general direction, different approach
- **LOW**: Different answers → same actions, different framing/flavor

---

## Q1: Can expected value be calculated?
[VOI: HIGH - Negative expected value means reconsider vs proceed]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, negative expected value | HIGH | Reconsider vs proceed | Reconsider | Actually positive |
| Cannot calculate | MED | Scenario analysis vs quantitative | Scenario analysis | Can calculate |
| Yes, near zero | MED | Careful evaluation vs proceed | Careful evaluation | Different value |
| Yes, positive expected value | LOW | Worth pursuing either way | Proceed | Actually negative |

---

## Q2: Is variance acceptable even if expected value is positive?
[VOI: HIGH - Variance too high means too risky, reduce variance vs proceed]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| No, variance too high | HIGH | Reduce variance vs proceed | Reduce variance | Variance acceptable |
| Unknown variance | MED | Variance analysis vs assume | Variance analysis | Variance known |
| Yes, acceptable variance | LOW | Risk tolerable either way | Proceed | Variance too high |

---

## Q3: What evidence supports probability estimates?
[VOI: HIGH - No data means guessing, treat as uncertain vs trust estimates]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| No data | HIGH | Treat as uncertain vs trust | Treat as uncertain | Data exists |
| Unknown evidence quality | MED | Evidence review vs assume | Evidence review | Quality known |
| Limited data | MED | Wide confidence vs trust | Wide confidence | More data |
| Strong historical data | LOW | Reliable estimates either way | Trust estimates | Data weak |

---

## Q4: Are there events treated as independent that may not be?
[VOI: HIGH - Some not independent/unknown means hidden correlation, account for vs calculate independently]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Some not independent | HIGH | Account for correlation vs independent | Account for correlation | Independent |
| Unknown independence | HIGH | Independence check vs assume | Independence check | Independence known |
| All truly independent | LOW | Correct analysis either way | Calculate independently | Not independent |

---

## Q5: What is the base rate success for reference class?
[VOI: HIGH - Low rate means unfavorable odds, reconsider vs proceed]
Prerequisite: Q7 shows reference class exists

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Low rate (<30%) | HIGH | Reconsider vs proceed | Reconsider | Rate higher |
| Unknown rate | MED | Rate research vs assume | Rate research | Rate known |
| Moderate rate (30-70%) | MED | Careful analysis vs proceed | Careful analysis | Different rate |
| High success rate (>70%) | LOW | Favorable odds either way | Proceed | Rate lower |

---

## Q6: Are there uncertain outcomes relevant to this goal?
[VOI: MED - Significant uncertainty affects planning but doesn't change direction]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Unknown uncertainty level | MED | Uncertainty mapping vs assume | Uncertainty mapping | Level known |
| Yes, significant uncertainty | MED | Probabilistic planning vs deterministic | Probabilistic planning | Less uncertain |
| Yes, minor uncertainty | LOW | Mostly predictable either way | Slight hedging | More uncertainty |
| No, outcomes certain | LOW | Deterministic either way | Execute directly | Uncertainty exists |

---

## Q7: Is there a reference class for base rate analysis?
[VOI: MED - Reference class helps calibration but doesn't change direction]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Unknown if reference exists | MED | Reference search vs assume | Reference search | Reference known |
| No reference class | MED | First principles vs calibrate | First principles | Reference exists |
| Yes, imperfect reference | MED | Adjust estimates vs apply | Use with adjustment | Different quality |
| Yes, good reference class | LOW | Calibrated estimates either way | Use base rate | Poor reference |

---

## Q8: Can probability be estimated numerically?
[VOI: MED - Estimation ability affects approach but not direction]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Unknown if estimable | MED | Estimation check vs assume | Estimation check | Estimability known |
| No, cannot estimate | MED | Qualitative analysis vs quantitative | Scenario planning | Can estimate |
| Yes, rough estimates | MED | Use with caution vs precise | Use with caution | Different quality |
| Yes, good estimates | LOW | Quantitative planning either way | Use estimates | Estimates poor |

---

## Question Order by Action Divergence

**HIGH VOI (ask first - route to different action paths):**
1. Q1: Expected value? (Negative → reconsider vs proceed)
2. Q2: Variance? (Too high → reduce vs proceed)
3. Q3: Evidence? (No data → treat as uncertain vs trust)
4. Q4: Independence? (Not independent/unknown → account for vs calculate)
5. Q5: Base rate? (Low → reconsider vs proceed)

**MED/LOW VOI (ask second - refine approach):**
6. Q6: Uncertainty? (Planning approach, not direction)
7. Q7: Reference class? (Calibration, not direction)
8. Q8: Estimable? (Analysis approach, not direction)

---

## Key Insight

**VOI ≠ Probability Magnitude**

VOI = Action Divergence

A HIGH VOI probability question is one where the answer determines whether you PROCEED or RECONSIDER. "Negative expected value" routes you to "reconsider the goal" - a completely different action than "proceed with positive expected value."

A LOW VOI probability question like "good vs rough estimates" doesn't change your fundamental approach - you'll make decisions either way, just with different confidence levels.

---

## Coverage Summary

```
QUESTIONS: 8
ENTRIES: 35

VOI Distribution:
- HIGH: 7 entries (20%)
- MED: 18 entries (51%)
- LOW: 10 entries (29%)
```
