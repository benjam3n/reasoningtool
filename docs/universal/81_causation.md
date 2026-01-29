# Universal: Causation (81)

**Category**: CORE - Cause and Effect Analysis
**Source**: New category not in YAML - fundamental to reasoning about goals
**Structure**: One question per entry, VOI-marked with realistic distribution

---

## VOI Rating = Action Divergence

- **HIGH**: Different answers → completely different action paths
- **MED**: Different answers → same general direction, different approach
- **LOW**: Different answers → same actions, different framing/flavor

---

## Q1: Is the causal relationship established or assumed?
[VOI: HIGH - assumed causation may be wrong vs established enables intervention]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Assumed | HIGH | Verify causation vs act on assumption | Verify causation | Actually established |
| Unknown if established | HIGH | Establishment check vs proceed | Establishment check | Status known |
| Established (evidence) | LOW | Use relationship confidently | Use relationship | Actually assumed |

---

## Q2: Could this be correlation without causation?
[VOI: HIGH - correlation only means intervention won't work vs causation enables intervention]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Likely correlation only | HIGH | Find true cause vs intervene on correlation | Find true cause | Actually causation |
| Unknown | MED | Correlation test vs proceed | Correlation test | Relationship known |
| Causation confirmed | LOW | Intervene on cause | Intervene on cause | Actually correlation |

---

## Q3: What is the direction of causation (A→B or B→A or both)?
[VOI: HIGH - wrong direction means intervening on wrong thing vs right direction enables effective intervention]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| B causes A | HIGH | Change B instead of A | Change B | A causes B |
| Unknown direction | HIGH | Direction testing vs guess | Direction testing | Direction known |
| Bidirectional | MED | Address both vs one | Address both | One direction |
| A causes B | LOW | Intervene on A | Change A | Wrong direction |

---

## Q4: Are there confounding variables?
[VOI: HIGH - unknown confounders mean spurious relationship vs controlled enables accurate intervention]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Confounders likely but unknown | HIGH | Confounder search vs act on spurious | Confounder search | No confounders |
| Confounders identified | MED | Account for confounders vs ignore | Account for confounders | Different confounders |
| Unknown if confounders | MED | Confounder check vs proceed | Confounder check | Confounders known |
| No confounders | LOW | Use direct relationship | Use direct | Confounders exist |

---

## Q5: What is the mechanism by which cause produces effect?
[VOI: HIGH - no known mechanism may mean spurious vs understood mechanism enables precise intervention]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| No known mechanism | HIGH | Mechanism search vs act blindly | Mechanism search | Mechanism exists |
| Mechanism unclear | MED | Investigate vs proceed imprecise | Investigate | Mechanism clear |
| Black box (works but unknown) | MED | Use carefully vs trust fully | Use carefully | Mechanism known |
| Mechanism understood | LOW | Intervene precisely | Use mechanism | Mechanism wrong |

---

## Q6: Are there necessary vs sufficient causes?
[VOI: HIGH - necessary but not sufficient means need more vs sufficient means single action works]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Necessary (required but not enough) | HIGH | Find other requirements vs act alone | Find other requirements | Actually sufficient |
| Sufficient (enough alone) | MED | Use alone vs combine | Use alone | Actually necessary |
| Contributory (helps but neither) | MED | Combine with others vs rely on | Combine with others | Different type |
| Unknown type | MED | Type analysis vs guess | Type analysis | Type known |

---

## Q7: What is the causal chain from action to outcome?
[VOI: HIGH - unknown chain may break somewhere vs known chain enables verification]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Unknown chain | HIGH | Chain mapping vs proceed blind | Chain mapping | Chain known |
| Indirect (A→X→B) | MED | Address whole chain vs direct | Address whole chain | Different chain |
| Long chain | MED | Verify each link vs assume | Verify each link | Shorter chain |
| Direct (A→B) | LOW | Direct action | Direct action | Actually indirect |

---

## Q8: Could there be unintended effects of intervening on the cause?
[VOI: HIGH - likely unintended effects require analysis before action vs safe enables proceeding]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Unintended effects likely | HIGH | Effect analysis before acting | Effect analysis | No effects |
| Unintended effects identified | MED | Plan for them vs ignore | Mitigate | Different effects |
| Unknown if effects | MED | Effect check vs proceed | Effect check | Effects known |
| No unintended effects | LOW | Proceed safely | Proceed | Effects exist |

---

## Q9: Is the causal relationship stable over time/context?
[VOI: HIGH - context-dependent means may not work here vs stable enables reliable use]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| No, context-dependent | HIGH | Check context vs assume works | Check context | Actually stable |
| Unknown stability | MED | Stability check vs proceed | Stability check | Stability known |
| Yes, stable | LOW | Rely on relationship | Rely on | Actually unstable |

---

## Q10: Is there a claimed causal relationship relevant to this goal?
[VOI: MED - determines whether causal analysis applies]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Unknown if causal | MED | Causation check vs proceed | Causation check | Causation known |
| Yes, causal claim | LOW | Examine causation | Examine causation | No causal claim |
| No, descriptive only | LOW | Skip causation analysis | Skip causation | Causal claim exists |

---

## Q11: How strong is the causal effect?
[VOI: MED - effect size determines prioritization]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Weak effect | MED | Deprioritize or combine vs invest heavily | Deprioritize or combine | Strong effect |
| Unknown strength | MED | Effect size estimation vs guess | Effect size estimation | Strength known |
| Strong effect | LOW | Prioritize this lever | Prioritize | Weak effect |

---

## Coverage Summary

```
QUESTIONS: 11
ENTRIES: 43

VOI Distribution:
- HIGH: 9 entries (21%)
- MED: 21 entries (49%)
- LOW: 13 entries (30%)
```

---

## Question Order by Action Divergence

**HIGH VOI (ask first - routes to different action paths):**
- Q1-Q2: Established? Correlation only? - is the relationship real
- Q3-Q4: Direction? Confounders? - what's really happening
- Q5-Q7: Mechanism? Type? Chain? - how it works
- Q8-Q9: Side effects? Stable? - risks of intervention

**MED VOI (ask second - same direction, different approach):**
- Q10-Q11: Causal claim exists? Effect strength? - relevance and prioritization

---

## Key Insight

**VOI ≠ causal importance or scientific rigor**

**VOI = action divergence**

A question has HIGH VOI when knowing the answer changes what you do next (verify causation vs assume, find true cause vs intervene on correlation, check context vs apply universally). Low VOI questions refine understanding within an established causal model.
