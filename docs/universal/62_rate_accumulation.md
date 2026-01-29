# Universal: Rate and Accumulation (62)

**Category**: MATHEMATICAL - Change and Accumulation Analysis
**Source**: [O: universal_goal_analysis.yaml lines 2083-2129 rate_and_accumulation category]
**Structure**: One question per entry, VOI-marked with realistic distribution

---

## VOI Rating = Action Divergence

- **HIGH**: Different answers → completely different action paths
- **MED**: Different answers → same general direction, different approach
- **LOW**: Different answers → same actions, different framing/flavor

---

## Q1: Are there threshold values where behavior changes qualitatively?
[VOI: HIGH - crossing threshold changes the game vs linear progression]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, critical thresholds | HIGH | Target/avoid threshold vs gradual approach | Know and target/avoid | No thresholds |
| Unknown if thresholds | MED | Threshold discovery vs assume continuous | Threshold discovery | Thresholds known |
| No, smooth changes only | LOW | Gradual approach vs threshold-aware | Gradual approach | Thresholds exist |

---

## Q2: Is crossing the threshold reversible?
[VOI: HIGH - irreversible threshold requires caution vs recoverable]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| No, irreversible | HIGH | Extra caution required vs normal risk tolerance | Extra caution | Reversible |
| Unknown reversibility | HIGH | Must determine before acting vs proceed | Reversibility check | Reversibility known |
| Partially reversible | MED | Careful approach vs full caution | Careful approach | Different level |
| Yes, reversible | LOW | Lower stakes, can recover vs irreversible | Lower stakes | Irreversible |

---

## Q3: Are contributions being lost faster than they accumulate?
[VOI: HIGH - net negative requires rate/decay intervention vs continue]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, net negative | HIGH | Increase rate or reduce decay vs maintain current | Increase rate or reduce decay | Net positive |
| Unknown net direction | MED | Calculate net direction vs assume progress | Net calculation | Direction known |
| Breakeven | MED | Adjust rate to make progress vs continue | Adjust rate | Different level |
| No, net positive | LOW | Continue current vs actually negative | Continue | Actually negative |

---

## Q4: Is there a quantity to maximize or minimize?
[VOI: HIGH - multiple competing objectives require tradeoff analysis vs single optimization]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Multiple competing | HIGH | Multi-objective tradeoff analysis vs single focus | Multi-objective analysis | Single objective |
| Unknown objective | MED | Clarify what to optimize vs proceed | Objective clarification | Objective known |
| Yes, clear objective | LOW | Optimize single objective vs no clear target | Optimization approach | No clear objective |
| No optimization needed | LOW | Meet threshold, don't optimize | Meet threshold | Optimization needed |

---

## Q5: Are there quantities approaching a limiting value?
[VOI: HIGH - hard limit constrains all planning vs unconstrained pursuit]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, hard limit | HIGH | Plan within limit vs pursue unlimited | Plan within limit | Soft/no limit |
| Unknown if limited | MED | Discover limits vs assume unlimited | Limit discovery | Limits known |
| Yes, soft limit | MED | Factor in increasing difficulty vs unconstrained | Factor in difficulty | Different limit type |
| No limit relevant | LOW | Full pursuit vs limited | Full pursuit | Limit exists |

---

## Q6: Are there quantities that change over time relevant to this goal?
[VOI: HIGH - critical changing quantities require monitoring vs point-in-time]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, critical quantities changing | HIGH | Monitor and project vs snapshot analysis | Monitor and project | Static situation |
| Unknown if changing | MED | Rate identification vs assume static | Rate identification | Rates known |
| Yes, minor quantities changing | LOW | Optional monitoring vs ignore | Optional monitoring | More significant |
| No, all static | LOW | Point-in-time plan vs need tracking | Point-in-time plan | Actually changing |

---

## Q7: Is the rate of change itself changing (accelerating/decelerating)?
[VOI: HIGH - acceleration means linear projections wrong]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Accelerating | HIGH | Adjust projections for acceleration vs linear | Adjust projections | Constant rate |
| Unknown acceleration | MED | Measure acceleration vs assume constant | Acceleration check | Pattern known |
| Decelerating | MED | Adjust for deceleration vs different pattern | Adjust | Different pattern |
| Constant rate | LOW | Linear extrapolation vs rate changing | Simple extrapolation | Rate changing |

---

## Q8: At current rate, when will quantity reach target/zero?
[VOI: MED - urgency level affects prioritization but not fundamental approach]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Soon (days/weeks) | MED | Act quickly vs have time to plan | Act quickly | More time |
| Unknown timeline | MED | Estimate timeline vs proceed blind | Timeline estimation | Timeline known |
| Medium term (months) | LOW | Planned approach vs different timeline | Planned approach | Different timeline |
| Long term (years) | LOW | Strategic approach vs shorter timeline | Strategic approach | Sooner |

---

## Q9: Are there small actions that accumulate over time?
[VOI: MED - compound effects need tracking vs discrete events]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, accumulation matters | MED | Track cumulative effects vs ignore | Track cumulative | No accumulation |
| Unknown if accumulates | MED | Check for accumulation vs assume discrete | Accumulation check | Accumulation known |
| No, discrete events | LOW | Event-based focus vs track accumulation | Focus on events | Actually accumulates |

---

## Q10: Is there diminishing returns (increasing input, decreasing output)?
[VOI: MED - affects when to stop investing vs continue scaling]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, diminishing | MED | Find optimal stopping point vs continue | Find optimal point | No diminishing |
| Unknown returns curve | MED | Analyze returns curve vs assume linear | Returns analysis | Curve known |
| No, linear or increasing | LOW | Continue scaling vs diminishing exists | Continue scaling | Actually diminishing |

---

## Coverage Summary

```
QUESTIONS: 10
ENTRIES: 40

VOI Distribution:
- HIGH: 8 entries (20%)
- MED: 19 entries (48%)
- LOW: 13 entries (32%)
```

---

## Question Order by Action Divergence

**HIGH VOI (ask first - routes to different action paths):**
1. Q1 (Thresholds?) - phase change points
2. Q2 (Reversible?) - point of no return
3. Q3 (Net direction?) - losing ground
4. Q4 (Objectives?) - tradeoffs needed
5. Q5 (Limits?) - hard constraints
6. Q6 (Critical changing?) - must track rate
7. Q7 (Accelerating?) - projections off

**MED VOI (ask second - same direction, different approach):**
8. Q8 (Timeline?) - urgency
9. Q9 (Accumulation?) - compound effects
10. Q10 (Diminishing?) - optimal stopping

---

## Key Insight

**VOI ≠ mathematical complexity**

**VOI = action divergence**

Q2 "Is crossing the threshold reversible?" is HIGH VOI because:
- REVERSIBLE → normal risk tolerance, can experiment
- IRREVERSIBLE → extreme caution, no do-overs (completely different behavior)

Q10 "Is there diminishing returns?" is MED VOI because:
- YES → find optimal stopping point
- NO → continue scaling (same general direction, just different cutoff)

Both involve calculus-level concepts. But reversibility determines your entire risk posture, while diminishing returns fine-tunes when to stop.
