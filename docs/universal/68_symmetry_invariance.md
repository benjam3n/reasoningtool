# Universal: Symmetry and Invariance (68)

**Category**: MATHEMATICAL - Transformations and Constants
**Source**: [O: universal_goal_analysis.yaml lines 2319-2343 symmetry_and_invariance category]
**Structure**: One question per entry, VOI-marked with realistic distribution

---

## VOI Rating = Action Divergence

- **HIGH**: Different answers → completely different action paths
- **MED**: Different answers → same general direction, different approach
- **LOW**: Different answers → same actions, different framing/flavor

---

## Q1: Does the invariant constrain what outcomes are possible?
[VOI: HIGH - strong constraint limits what's achievable]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, strong constraint | HIGH | Work within constraint, some outcomes impossible | Work within | Weak/no constraint |
| Unknown constraint | MED | Determine constraint impact vs proceed | Constraint check | Constraint known |
| Yes, weak constraint | MED | Note constraint, mostly free | Note constraint | Different level |
| No constraint | LOW | Full range of outcomes possible | Unconstrained | Constraint exists |

---

## Q2: When multiple equivalent choices exist, does it matter which is chosen?
[VOI: HIGH - if choice matters, wrong choice loses; if not, pick any]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, choice matters | HIGH | Choose carefully, find differentiator | Choose carefully | Doesn't matter |
| Unknown if matters | MED | Analyze choice impact vs pick randomly | Choice analysis | Choice known |
| No, doesn't matter | LOW | Pick any, move on | Pick one | Actually matters |

---

## Q3: Are there transformations that leave the problem unchanged?
[VOI: MED - symmetries enable simplification]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, symmetries exist | MED | Exploit symmetry for simplification | Exploit symmetry | No symmetry |
| Unknown if symmetries | MED | Symmetry search vs full complexity | Symmetry search | Symmetries known |
| No symmetries | LOW | Direct approach, full complexity | Direct approach | Symmetries exist |

---

## Q4: Can symmetry be exploited to simplify the problem?
[VOI: MED - simplification affects efficiency]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, significant simplification | MED | Use symmetry for efficiency vs direct | Use symmetry | Minor/no simplification |
| Unknown utility | MED | Test symmetry exploitation vs skip | Exploitation testing | Utility known |
| Yes, minor simplification | LOW | Consider using vs skip | Consider | Different level |
| No, symmetry doesn't help | LOW | Direct solve vs try symmetry | Direct solve | Symmetry helps |

---

## Q5: Can symmetry generate new solutions from known solutions?
[VOI: MED - solution generation expands option space]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, generates solutions | MED | Apply symmetry to multiply solutions | Apply symmetry | Doesn't generate |
| Unknown if generates | MED | Test generation vs find each | Generation testing | Generation known |
| No, doesn't generate | LOW | Find each solution independently | Find each | Actually generates |

---

## Q6: Are there quantities that remain constant regardless of actions?
[VOI: MED - invariants provide constraints and checks]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, invariants exist | MED | Use invariants for constraints/checks | Use invariants | No invariants |
| Unknown if invariants | MED | Search for invariants vs assume none | Invariant search | Invariants known |
| No invariants | LOW | Everything changes, track all | Track all | Invariants exist |

---

## Q7: What is conserved and why?
[VOI: MED - understanding conservation enables prediction]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Conservation unclear | MED | Investigate cause of conservation | Investigate cause | Conservation clear |
| Unknown conservation | MED | Conservation analysis vs proceed | Conservation analysis | Conservation known |
| Conservation understood | LOW | Use understanding for prediction | Use understanding | Wrong conservation |

---

## Q8: Is there symmetry that needs to be broken to make progress?
[VOI: MED - symmetry breaking requires decision]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, must break symmetry | MED | Make deliberate choice vs stay stuck | Make choice | No breaking needed |
| Unknown if must break | MED | Analyze symmetry breaking need vs maintain | Symmetry analysis | Breaking known |
| No, symmetry can remain | LOW | No forced choice, maintain | Maintain symmetry | Must break |

---

## Q9: What breaks the symmetry (makes one choice better)?
[VOI: MED - breaker provides decision criterion]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Breaker unclear | MED | Find breaker or accept arbitrary | Find breaker or accept | Breaker clear |
| No breaker exists | MED | Truly arbitrary, pick any | Pick any | Breaker exists |
| Unknown breaker | MED | Search for breaker vs pick randomly | Breaker search | Breaker known |
| Breaker identified | LOW | Use breaker criterion vs wrong breaker | Use breaker | Wrong breaker |

---

## Q10: Does the invariant provide a check on correctness?
[VOI: LOW - validation tool vs no tool]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, useful check | LOW | Use check for validation | Use check | No check |
| No useful check | LOW | Other validation needed | Different checks | Check exists |
| Unknown if check | LOW | Test if useful vs skip | Check testing | Check known |

---

## Coverage Summary

```
QUESTIONS: 10
ENTRIES: 38

VOI Distribution:
- HIGH: 2 entries (5%)
- MED: 22 entries (58%)
- LOW: 14 entries (37%)

Note: Lower HIGH% because symmetry analysis is usually optimization
```

---

## Question Order by Action Divergence

**HIGH VOI (ask first - routes to different action paths):**
1. Q1 (Strong constraint?) - limits what's possible
2. Q2 (Choice matters?) - careful selection needed

**MED VOI (ask second - same direction, different approach):**
3. Q3 (Symmetries exist?) - simplification possible
4. Q4 (Symmetry simplifies?) - efficiency gain
5. Q5 (Generates solutions?) - solution multiplication
6. Q6 (Invariants exist?) - constraints available
7. Q7 (Conservation?) - prediction enabled
8. Q8 (Must break symmetry?) - decision needed
9. Q9 (Symmetry breaker?) - decision criterion

**LOW VOI:**
10. Q10 (Correctness check?) - validation tool

---

## Key Insight

**VOI ≠ mathematical elegance**

**VOI = action divergence**

Q2 "Does choice among equivalents matter?" is HIGH VOI because:
- YES → must find differentiator, wrong choice loses
- NO → pick any and move on (completely different decision process)

Q10 "Does invariant provide correctness check?" is LOW VOI because:
- YES → use the check
- NO → use different validation (same goal, different tool)

Choice significance determines how you decide. Validation tools are interchangeable means to the same end.
