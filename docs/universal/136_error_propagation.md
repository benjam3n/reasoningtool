# Universal: Error Propagation (136)

**Category**: META - How Do Mistakes Compound?
**Source**: Statistics, signal processing, reliability engineering
**Structure**: Questions ordered by Value of Information (action divergence)

---

## VOI Rating = Action Divergence

- **HIGH**: Different answers → completely different action paths
- **MED**: Different answers → same general direction, different approach
- **LOW**: Different answers → same actions, different framing/flavor

---

## Q1: How long is the inference chain?

[VOI: HIGH - longer chains accumulate more error]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Very long chain | HIGH | High error accumulation | Shorten chain or verify each step | Confident in unreliable |
| Unknown chain length | MED | May have hidden length | Chain analysis | Either unreliable or fine |
| Short chain | LOW | Low error accumulation | Proceed | Actually long |

---

## Q2: Are errors additive or multiplicative?

[VOI: HIGH - multiplicative errors compound catastrophically]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Multiplicative errors | HIGH | Exponential degradation | Fix error sources | Catastrophic compound |
| Unknown error type | MED | May be multiplicative | Error analysis | Either catastrophic or linear |
| Additive errors | LOW | Linear degradation | Standard precautions | Actually multiplicative |

---

## Q3: Is there error correction along the chain?

[VOI: HIGH - no correction = errors only accumulate]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| No error correction | HIGH | Errors only grow | Add correction points | Errors accumulate unchecked |
| Unknown correction status | MED | May be accumulating | Correction analysis | Either accumulating or corrected |
| Error correction exists | LOW | Errors bounded | Proceed | Actually no correction |

---

## Q4: What's the error rate per step?

[VOI: HIGH - high per-step error = chain degrades fast]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| High error rate per step | HIGH | Chain unreliable | Reduce steps or improve accuracy | Trust unreliable chain |
| Unknown error rate | MED | May be unreliable | Error rate estimation | Either unreliable or fine |
| Low error rate per step | LOW | Chain reliable | Proceed | Actually high error rate |

---

## Q5: Are there single points of failure?

[VOI: HIGH - single point failure = entire chain fails]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Single point exists | HIGH | Chain fragile | Add redundancy or verify point | Chain breaks at weak link |
| Unknown fragility | MED | May have weak point | Fragility analysis | Either fragile or robust |
| No single points | LOW | Chain robust | Proceed | Actually has single point |

---

## Q6: Can we validate the final output independently?

[VOI: MED - validation catches accumulated error]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Can validate but haven't | MED | Avoidable risk | Validate output | Trust unvalidated |
| Unknown if validatable | MED | May be testable | Validation check | Either test or accept |
| Can't validate | LOW | Must trust chain | Accept chain risk | Think can't when can |
| Already validated | LOW | Confirmed | Proceed confidently | Actually not validated |

---

## Q7: Are errors systematic or random?

[VOI: MED - systematic errors can be corrected]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Systematic errors | MED | Can correct | Identify and correct bias | Repeated same error |
| Unknown error type | MED | May be correctable | Error analysis | Either correct or accept |
| Random errors | LOW | Average out somewhat | Accept noise | Think random when systematic |

---

## Q8: Is there amplification of certain error types?

[VOI: MED - amplified errors dominate]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Certain errors amplified | MED | Must prevent those | Focus on amplified types | Small errors become large |
| Unknown amplification | MED | May have hidden amplification | Amplification analysis | Either large or contained |
| No amplification | LOW | Errors stay sized | Standard precautions | Actually amplified |

---

## Q9: What's the confidence in intermediate steps?

[VOI: LOW - affects overall confidence but similar process]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Low intermediate confidence | LOW | Low overall confidence | Reduce expectations | Over-confident in final |
| Unknown intermediate confidence | LOW | May be over-confident | Confidence check | Either over or under confident |
| High intermediate confidence | LOW | High overall confidence | Proceed confidently | Actually low confidence |

---

## Q10: Can we bound the maximum error?

[VOI: LOW - affects risk assessment but similar actions]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Can bound error | LOW | Known worst case | Plan for worst case | Underestimate worst |
| Unknown if boundable | LOW | May have unknown worst | Bound analysis | Either known or unknown worst |
| Cannot bound | LOW | Unknown worst case | Extra caution | Think unbounded when bounded |

---

## Summary Statistics

- Total questions: 10
- Total entries: 38
- HIGH VOI: 10 (26%)
- MED VOI: 14 (37%)
- LOW VOI: 14 (37%)

---

## Question Order by Action Divergence

**Ask first (HIGH VOI):**
1. Q1: Chain length? - accumulation distance
2. Q2: Additive or multiplicative? - compounding type
3. Q3: Error correction? - accumulation control
4. Q4: Error rate per step? - degradation speed
5. Q5: Single points of failure? - fragility

**Ask if relevant (MED VOI):**
6. Q6: Can validate output? - end-to-end check
7. Q7: Systematic or random? - correctability
8. Q8: Error amplification? - hidden growth

**Low priority (LOW VOI):**
9. Q9: Intermediate confidence? - overall confidence
10. Q10: Can bound error? - worst case

---

## Key Insight

**VOI ≠ statistical sophistication. VOI = action divergence.**

"Can we bound the maximum error?" is useful but has LOW VOI - you plan cautiously either way.

"Are errors additive or multiplicative?" has HIGH VOI - multiplicative errors require completely different strategies.

---

## The Reliability Equation

For independent steps with probability p of correctness:
- Chain of n steps: p^n reliability
- 10 steps at 95% each: 0.95^10 = 60% reliable
- 20 steps at 95% each: 0.95^20 = 36% reliable

**Implications:**
- Long chains are unreliable even with good steps
- Must either shorten chains or add verification
- Single weak steps dominate reliability

**The trap:** Assuming each step is fine, therefore the whole is fine.

**The move:** Before trusting a long inference chain, compute the compound reliability. Add verification points at critical junctures.
