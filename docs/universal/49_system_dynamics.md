# Universal: System Dynamics (49)

**Category**: CORE - Complex System Behavior
**Source**: [O: universal_goal_analysis.yaml lines 1578-1630 system_dynamics category]
**Structure**: One question per entry, VOI-marked with realistic distribution

---

## VOI Rating = Action Divergence

- **HIGH**: Different answers → completely different action paths
- **MED**: Different answers → same general direction, different approach
- **LOW**: Different answers → same actions, different framing/flavor

---

## Q1: Are there feedback loops?
[VOI: HIGH - Reinforcing loops/unknown means leverage or counter vs linear approach]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, reinforcing loops | HIGH | Leverage or counter vs linear | Leverage or counter | No reinforcing |
| Unknown if loops | HIGH | Loop analysis vs linear | Loop analysis | Loops known |
| Yes, balancing loops | MED | Work with loops vs ignore | Work with loops | No balancing |
| No feedback loops | LOW | Linear approach either way | Linear approach | Loops exist |

---

## Q2: Are there thresholds that cause significant change?
[VOI: HIGH - Critical thresholds/unknown means know and avoid vs gradual approach]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Critical thresholds exist | HIGH | Know thresholds vs gradual | Know thresholds | No thresholds |
| Unknown thresholds | HIGH | Threshold discovery vs gradual | Threshold discovery | Thresholds known |
| Minor thresholds | MED | Be aware vs ignore | Be aware | Different level |
| No thresholds | LOW | Gradual change either way | Linear approach | Thresholds exist |

---

## Q3: How close is current state to thresholds?
[VOI: HIGH - Very close/unknown means careful action vs normal approach]
Prerequisite: Q2 shows thresholds exist

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Very close | HIGH | Careful action vs normal | Careful action | Far away |
| Unknown proximity | HIGH | Proximity check vs assume safe | Proximity check | Proximity known |
| Moderately close | MED | Monitor closely vs relax | Monitor closely | Different distance |
| Far away | LOW | Safe margin either way | Normal approach | Actually close |

---

## Q4: Are there delays between cause and effect?
[VOI: HIGH - Significant delays means patience/account for vs immediate feedback]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Significant delays | HIGH | Account for delay vs immediate | Account for delay | Less delay |
| Unknown delays | MED | Delay measurement vs assume | Delay measurement | Delays known |
| Minor delays | LOW | Quick feedback either way | Near-immediate | More delay |
| No delays | LOW | Instant feedback either way | React immediately | Delays exist |

---

## Q5: Are there emergent behaviors?
[VOI: HIGH - Harmful emergence means prevent/mitigate vs proceed]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, harmful emergence | HIGH | Prevent or mitigate vs proceed | Prevent or mitigate | Helpful |
| Unknown emergence | MED | Emergence watch vs assume | Emergence watch | Emergence known |
| Yes, helpful emergence | MED | Use emergence vs ignore | Use emergence | Harmful |
| No emergence | LOW | Predictable either way | Direct planning | Emergence exists |

---

## Q6: Is the approach intended for a particular scale?
[VOI: HIGH - Different scale than intended means adjust approach vs proceed]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, different scale | HIGH | Adjust approach vs proceed | Adjust approach | Current scale |
| Unknown scale | MED | Scale analysis vs assume | Scale analysis | Scale known |
| No scale assumptions | MED | Scale-independent vs check | Proceed | Scale-dependent |
| Yes, current scale | LOW | Appropriate either way | Continue | Different scale |

---

## Q7: At what scale does the approach break?
[VOI: HIGH - Near current scale means prepare alternatives vs proceed]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Near current scale | HIGH | Prepare alternatives vs proceed | Prepare alternatives | Far beyond |
| Unknown break point | MED | Limit discovery vs assume | Limit discovery | Break point known |
| Far beyond current | LOW | Safe margin either way | Proceed | Closer to break |

---

## Q8: Does achieving goal cause second-order effects?
[VOI: HIGH - Significant negative means factor in or change vs proceed]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Significant negative | HIGH | Factor in or change vs proceed | Factor in or change | Less negative |
| Unknown effects | MED | Effect analysis vs assume | Effect analysis | Effects known |
| Significant positive | LOW | Bonus either way | Proceed | Less positive |
| Minor effects | LOW | Negligible either way | Ignore | More significant |

---

## Q9: Do second-order effects change goal value?
[VOI: HIGH - Decrease value means reconsider vs proceed]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Decrease value | HIGH | Reconsider vs proceed | Reconsider | Increase value |
| Unknown impact | MED | Value analysis vs assume | Value analysis | Impact known |
| Increase value | LOW | Better than thought either way | Proceed | Decrease value |
| No change | LOW | Value stable either way | Proceed | Value changes |

---

## Q10: Is goal affected by system with multiple interacting parts?
[VOI: MED - Complex system affects approach but doesn't change direction]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, complex system | MED | System thinking vs linear | Apply system analysis | Simple system |
| Unknown complexity | MED | Complexity check vs assume | Complexity check | Complexity known |
| No, simple system | LOW | Direct approach either way | Linear planning | Actually complex |

---

## Question Order by Action Divergence

**HIGH VOI (ask first - route to different action paths):**
1. Q1: Feedback loops? (Reinforcing/unknown → leverage vs linear)
2. Q2: Thresholds? (Critical/unknown → know and avoid vs gradual)
3. Q3: Proximity to threshold? (Very close/unknown → careful vs normal)
4. Q4: Delays? (Significant → account for vs immediate)
5. Q5: Emergent behaviors? (Harmful → prevent vs proceed)
6. Q6: Scale mismatch? (Different → adjust vs proceed)
7. Q7: Breaking scale? (Near → alternatives vs proceed)
8. Q8: Second-order effects? (Negative → factor in vs proceed)
9. Q9: Value change? (Decrease → reconsider vs proceed)

**MED/LOW VOI (ask second - refine approach):**
10. Q10: Complex system? (Affects approach, not direction)

---

## Key Insight

**VOI ≠ System Complexity**

VOI = Action Divergence

A HIGH VOI system dynamics question is one where the answer determines whether you USE A DIFFERENT APPROACH or CONTINUE WITH CURRENT APPROACH. "Reinforcing feedback loops exist" routes you to "leverage or counter the loops" - a fundamentally different strategy than "linear execution."

A LOW VOI system dynamics question like "complex vs simple system" doesn't change your fundamental approach - you'll pursue the goal either way, just with more or less system analysis.

---

## Coverage Summary

```
QUESTIONS: 10
ENTRIES: 42

VOI Distribution:
- HIGH: 11 entries (26%)
- MED: 17 entries (40%)
- LOW: 14 entries (33%)
```
