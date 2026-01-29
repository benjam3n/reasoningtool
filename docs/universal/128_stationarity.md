# Universal: Stationarity (128)

**Category**: META - Is the Problem Itself Changing?
**Source**: Dynamic systems, adaptive optimization, time-varying environments
**Structure**: Questions ordered by Value of Information (action divergence)

---

## VOI Rating = Action Divergence

- **HIGH**: Different answers → completely different action paths
- **MED**: Different answers → same general direction, different approach
- **LOW**: Different answers → same actions, different framing/flavor

---

## Q1: Is the underlying system changing over time?

[VOI: HIGH - changing system = adaptive strategy; stable = one-time optimization]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| System changing | HIGH | Moving target | Adaptive approach | Optimize for past, miss present |
| Unknown if changing | MED | May be stale | Change detection | Either over-adapt or stale |
| System stable | LOW | One-time optimization | Optimize once | Re-optimize unnecessarily |

---

## Q2: How fast is the change relative to our response time?

[VOI: HIGH - fast change = continuous adaptation; slow = periodic review]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Change faster than response | HIGH | Can't catch up | Accept lag, robust strategies | Chase ever-moving target |
| Change rate unknown | MED | May mismatch | Rate measurement | Either over or under adapt |
| Change slower than response | LOW | Can track | Periodic adaptation | Over-adapt to slow change |

---

## Q3: Is our model of the system still valid?

[VOI: HIGH - invalid model = optimizing wrong thing]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Model outdated | HIGH | Optimizing wrong thing | Rebuild model | Act on stale understanding |
| Unknown if valid | MED | May be stale | Model validation | Either stale or paranoid |
| Model still valid | LOW | Can use | Trust model | Use invalid model |

---

## Q4: Is this a trend or noise?

[VOI: HIGH - trend requires adaptation; noise should be filtered]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Trend | HIGH | Adapt to direction | Track trend | Filter out real change |
| Unknown | MED | May misrespond | Signal analysis | Either chase noise or miss trend |
| Noise | HIGH | Filter out | Ignore fluctuation | Chase noise endlessly |

---

## Q5: Are the rules of the game changing?

[VOI: HIGH - rule changes obsolete strategies]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Rules changing | HIGH | Strategy may become invalid | Monitor rules, adapt | Play by old rules |
| Unknown if rules changing | MED | May be blindsided | Rule monitoring | Either over-cautious or blindsided |
| Rules stable | LOW | Strategy persists | Use current strategy | Miss rule change |

---

## Q6: Is there a regime change (discontinuous shift)?

[VOI: HIGH - regime change = previous learning may not apply]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Regime change | HIGH | Previous patterns break | Fresh analysis | Extrapolate into new regime |
| Unknown if regime change | MED | May be using stale patterns | Regime analysis | Either miss change or false alarm |
| Continuous change | LOW | Patterns persist | Gradual adaptation | Treat continuous as discontinuous |

---

## Q7: Is there cyclical variation?

[VOI: MED - cycles are predictable but require timing]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Cyclical | MED | Timing matters | Anticipate cycle | Miss predictable variation |
| Unknown if cyclical | MED | May miss pattern | Cycle analysis | Either miss or see false cycles |
| Not cyclical | LOW | No timing component | Ignore timing | Miss cycle |

---

## Q8: How much memory should our system have?

[VOI: MED - affects weighting of past vs present]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Short memory needed | MED | Recent data dominates | Forget fast | Use stale data |
| Unknown memory length | MED | May misweight | Memory analysis | Either too much or too little history |
| Long memory needed | LOW | History matters | Remember | Forget useful history |

---

## Q9: Is there concept drift (gradual meaning change)?

[VOI: LOW - affects interpretation but similar monitoring]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Concept drift | LOW | Definitions shifting | Monitor definitions | Use stale concepts |
| Unknown if drifting | LOW | May be confused | Drift detection | Either stale or paranoid |
| Concepts stable | LOW | Definitions hold | Use definitions | Miss drift |

---

## Q10: Can we influence the change?

[VOI: LOW - affects agency but similar adaptation process]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Can influence change | LOW | Agency available | Shape change | Miss influence opportunity |
| Unknown if influenceable | LOW | May miss opportunity | Influence analysis | Either waste effort or miss chance |
| Cannot influence | LOW | Pure adaptation | Adapt to change | Waste effort on unchangeable |

---

## Summary Statistics

- Total questions: 10
- Total entries: 38
- HIGH VOI: 11 (29%)
- MED VOI: 13 (34%)
- LOW VOI: 14 (37%)

---

## Question Order by Action Divergence

**Ask first (HIGH VOI):**
1. Q1: System changing? - adaptive vs static strategy
2. Q2: Change rate? - can we keep up
3. Q3: Model valid? - optimizing right thing
4. Q4: Trend or noise? - filter vs follow
5. Q5: Rules changing? - strategy validity
6. Q6: Regime change? - discontinuity

**Ask if relevant (MED VOI):**
7. Q7: Cyclical? - timing
8. Q8: Memory length? - history weighting

**Low priority (LOW VOI):**
9. Q9: Concept drift? - definition stability
10. Q10: Can influence? - agency

---

## Key Insight

**VOI ≠ dynamic systems sophistication. VOI = action divergence.**

"Can we influence the change?" is interesting but has LOW VOI - you adapt similarly regardless.

"Is the underlying system changing?" has HIGH VOI - changing systems require continuous adaptation; stable systems need one-time optimization.

---

## The Stationarity Assumption

Most optimization assumes the world sits still while you optimize.
Reality: The world moves.

**Static world**: Find optimal, implement, done.
**Non-stationary world**: Find optimal, implement, it's already stale, re-optimize, repeat forever.

The meta-insight: Before optimizing, determine if optimization is even meaningful. If the system changes faster than you can optimize, you need a different approach:
- Accept being perpetually suboptimal
- Optimize for robustness to change, not performance under current conditions
- Build adaptive systems that track change automatically

The biggest stationarity mistake: Assuming stability when the world is changing, then wondering why your "optimal" solution stopped working.
