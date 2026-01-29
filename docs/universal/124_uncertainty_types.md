# Universal: Uncertainty Types (124)

**Category**: META - Different Uncertainties Require Different Strategies
**Source**: Probability theory, epistemology, decision theory
**Structure**: Questions ordered by Value of Information (action divergence)

---

## VOI Rating = Action Divergence

- **HIGH**: Different answers → completely different action paths
- **MED**: Different answers → same general direction, different approach
- **LOW**: Different answers → same actions, different framing/flavor

---

## Q1: Is this uncertainty reducible (epistemic) or irreducible (aleatoric)?

[VOI: HIGH - epistemic = invest in learning; aleatoric = accept and hedge]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Epistemic (reducible) | HIGH | Can learn away | Invest in research | Accept what could be known |
| Unknown type | MED | May waste effort | Uncertainty type analysis | Either waste research or accept unknowable |
| Aleatoric (irreducible) | HIGH | Must accept | Hedge, don't research | Research the unresearchable |

---

## Q2: Is this risk (known probabilities) or uncertainty (unknown probabilities)?

[VOI: HIGH - risk allows calculation; uncertainty requires different approaches]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| True uncertainty | HIGH | Probabilities unknown | Robustness, scenarios | Calculate with false precision |
| Unknown if risk or uncertainty | MED | May miscalculate | Classification effort | Either false confidence or excessive caution |
| Risk | LOW | Probabilities known | Expected value calculation | Treat as uncertainty unnecessarily |

---

## Q3: Can we reduce uncertainty by gathering more information?

[VOI: HIGH - determines whether to research or act]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Info gathering productive | HIGH | Worth researching | Gather information | Act on reducible ignorance |
| Unknown if reducible | MED | May waste effort | Reducibility check | Either waste research or miss reduction |
| Info won't help | HIGH | Research futile | Act under uncertainty | Research the unreducible |

---

## Q4: Is the uncertainty about the state of the world or about our model?

[VOI: HIGH - model uncertainty requires different handling]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Model uncertainty | HIGH | Wrong framework possible | Model validation | Use wrong model confidently |
| Unknown source | MED | May have wrong frame | Source analysis | Act on wrong model |
| State uncertainty | LOW | Model correct | Apply model | Think model right when wrong |

---

## Q5: Are there unknown unknowns we should expect?

[VOI: HIGH - unknown unknowns require slack and robustness]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Unknown unknowns likely | HIGH | Surprises coming | Build slack, stay flexible | Optimize for known, blindsided |
| Unknown if lurking | MED | May be surprised | Surprise analysis | Either over-hedge or blindsided |
| Domain well-understood | LOW | Few surprises | Optimize for known | Surprised by unknown unknown |

---

## Q6: What's the cost of being wrong under this uncertainty?

[VOI: MED - affects analysis depth but similar process]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Catastrophic if wrong | MED | Must be certain | Max uncertainty reduction | Under-invest in certainty |
| Moderate if wrong | LOW | Balanced approach | Proportional analysis | Over or under invest |
| Minor if wrong | MED | Tolerable | Accept uncertainty | Over-invest in certainty |

---

## Q7: Can we structure the decision to be robust to this uncertainty?

[VOI: MED - affects approach but similar decision]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Can make robust | MED | Design for uncertainty | Robust design | Fragile to uncertainty |
| Unknown if robust possible | MED | May miss robustness | Robustness analysis | Either fragile or over-engineer |
| Cannot make robust | LOW | Must resolve or accept | Resolve or hedge | Seek impossible robustness |

---

## Q8: Is the uncertainty correlated across options?

[VOI: MED - affects diversification but similar decision]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Correlated uncertainty | MED | Diversification useless | Don't diversify | False sense of hedge |
| Unknown correlation | MED | May mis-hedge | Correlation analysis | Either waste hedge or miss protection |
| Uncorrelated | LOW | Diversification helps | Diversify | Diversify when correlated |

---

## Q9: How does the uncertainty evolve over time?

[VOI: LOW - affects timing but similar analysis]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Resolves over time | LOW | Waiting valuable | Wait if possible | Act when waiting helps |
| Unknown evolution | LOW | May mistime | Evolution analysis | Either wait too long or rush |
| Persists indefinitely | LOW | Waiting useless | Act now | Wait for resolution that won't come |

---

## Q10: Is this a fat-tailed distribution (extreme events likely)?

[VOI: LOW - affects risk model but similar process]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Fat tails | LOW | Extremes matter | Prepare for extremes | Blindsided by extremes |
| Unknown tail behavior | LOW | May be surprised | Tail analysis | Either over-prepare or blindsided |
| Thin tails | LOW | Average dominates | Focus on expected value | Miss tail risk |

---

## Summary Statistics

- Total questions: 10
- Total entries: 39
- HIGH VOI: 10 (26%)
- MED VOI: 15 (38%)
- LOW VOI: 14 (36%)

---

## Question Order by Action Divergence

**Ask first (HIGH VOI):**
1. Q1: Epistemic vs aleatoric? - research vs accept
2. Q2: Risk vs uncertainty? - calculate vs hedge
3. Q3: Info gathering helps? - research value
4. Q4: State vs model uncertainty? - framework validity
5. Q5: Unknown unknowns? - surprise preparation

**Ask if relevant (MED VOI):**
6. Q6: Cost of being wrong? - stakes
7. Q7: Robustness possible? - design for uncertainty
8. Q8: Correlated uncertainty? - diversification

**Low priority (LOW VOI):**
9. Q9: Time evolution? - waiting value
10. Q10: Fat tails? - extreme events

---

## Key Insight

**VOI ≠ statistical sophistication. VOI = action divergence.**

"Is this fat-tailed?" affects risk models but has LOW VOI - you do similar analysis regardless.

"Is this epistemic or aleatoric?" has HIGH VOI - epistemic means research to reduce; aleatoric means accept and hedge.

---

## The Fundamental Distinction

**Epistemic uncertainty**: Arises from lack of knowledge. Can be reduced by learning. Example: "What's the customer's budget?" - you can ask.

**Aleatoric uncertainty**: Arises from inherent randomness. Cannot be reduced, only accepted. Example: "Will it rain next Tuesday?" - research can't eliminate randomness.

The meta-mistake: Treating epistemic as aleatoric (accepting ignorance when you could learn) or aleatoric as epistemic (researching randomness endlessly).

First question always: Can I learn this, or must I accept it?
