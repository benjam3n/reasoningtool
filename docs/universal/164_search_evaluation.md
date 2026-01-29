# Universal: Search Evaluation (164)

**Category**: SEARCH - What Makes An Answer Valid?
**Source**: Consolidated from belief types and reality strategy (Dilts "Beliefs")
**Structure**: Questions ordered by Value of Information (action divergence)

---

## VOI Rating = Action Divergence

- **HIGH**: Different answers → completely different action paths
- **MED**: Different answers → same general direction, different approach
- **LOW**: Different answers → same actions, different framing/flavor

---

## Core Insight

**Evaluation requires knowing: (1) what criteria determine validity, (2) how candidates are tested against criteria, (3) what passes vs fails.**

Evaluation fails when:
- Criteria are unknown or wrong
- Test is too strict (valid answers rejected)
- Test is too loose (invalid answers accepted)
- Test uses wrong modality for the criteria

---

## Q1: What criteria determine validity?

[VOI: HIGH - unknown criteria = unreliable evaluation]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Criteria unknown | HIGH | Cannot evaluate reliably | Identify criteria first | Accept invalid or reject valid |
| Criteria known | LOW | Can evaluate systematically | Apply criteria | Wrong criteria being used |

---

## Q2: Is the test calibrated correctly?

[VOI: HIGH - miscalibration corrupts all results]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Too strict | HIGH | Valid answers rejected | Loosen test | Continue missing options |
| Too loose | HIGH | Invalid answers accepted | Tighten test | Waste effort on invalid |
| Calibrated | LOW | Appropriate filtering | Continue | Actually miscalibrated |

---

## Q3: Does the candidate pass the test?

[VOI: HIGH - determines whether candidate proceeds]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Passes | LOW | Candidate proceeds | Accept as valid | Actually invalid |
| Fails | HIGH | Candidate rejected | Reject or retest | Dismiss valid candidate |

---

## Q4: Is this a cause criterion, meaning criterion, or identity criterion?

[VOI: HIGH - different criteria types need different evaluation]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Cause ("X because Y") | HIGH | Evaluate causal link | Test causation | Wrong evaluation type |
| Meaning ("X means Y") | HIGH | Evaluate interpretation | Check meaning assignment | Wrong evaluation type |
| Identity ("X is Y type") | HIGH | Evaluate classification | Check category membership | Wrong evaluation type |

---

## Q5: Is the stated criterion the actual criterion?

[VOI: HIGH - stated may differ from actual]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Stated = actual | LOW | Work with stated | Apply stated criterion | Chase wrong criterion |
| Stated ≠ actual | HIGH | Hidden criterion operating | Find actual criterion | Evaluate wrong thing |

---

## Q6: What qualities mark "valid"?

[VOI: MED - mechanism of the test]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Qualities identified | LOW | Can test reliably | Use identified qualities | Wrong qualities |
| Qualities unknown | MED | Cannot test reliably | Identify qualities | Test unreliably |

---

## Q7: Can a candidate be re-evaluated?

[VOI: MED - ability to change classification]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes | MED | Classification changeable | Re-evaluate as needed | Stay limited |
| No | MED | Fixed classification | Accept classification | Miss re-evaluation option |

---

## Q8: Are multiple criteria operating?

[VOI: MED - scope of evaluation]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, multiple | MED | Must satisfy all or some | Determine how they combine | Miss hidden criteria |
| No, single | LOW | Simpler evaluation | Apply single criterion | Actually multiple |

---

## Q9: How are criteria weighted?

[VOI: LOW - priority among criteria]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Weights known | LOW | Can prioritize | Apply weights | Wrong weights |
| Weights unknown | LOW | Implicit prioritization | Surface weights | Evaluate with wrong priority |

---

## Q10: Can criteria be updated?

[VOI: LOW - meta-flexibility]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes | LOW | Can improve | Update when needed | Stuck with current |
| No | LOW | Fixed | Accept limitation | Miss update option |

---

## Summary Statistics

- Total questions: 10
- Total entries: 26
- HIGH VOI: 9 (35%)
- MED VOI: 6 (23%)
- LOW VOI: 11 (42%)

---

## Question Order by Action Divergence

**Ask first (HIGH VOI):**
1. Q1: What criteria determine validity?
2. Q2: Is the test calibrated correctly?
3. Q3: Does the candidate pass the test?
4. Q4: Is this a cause, meaning, or identity criterion?
5. Q5: Is the stated criterion the actual criterion?

**Ask if relevant (MED VOI):**
6. Q6: What qualities mark "valid"?
7. Q7: Can a candidate be re-evaluated?
8. Q8: Are multiple criteria operating?

**Low priority (LOW VOI):**
9. Q9: How are criteria weighted?
10. Q10: Can criteria be updated?

---

## Criterion Types

| Type | Structure | How To Evaluate |
|------|-----------|-----------------|
| **Cause** | "X because Y" | Test whether Y actually produces X |
| **Meaning** | "X means Y" | Check whether interpretation is necessary |
| **Identity** | "X is type Y" | Verify category membership |

**The trap**: Evaluating a meaning criterion as if it were a cause criterion, or vice versa.

---

## Calibration Check

```
TEST TOO STRICT:
- Valid candidates rejected
- "Nothing works"
- High false negative rate

TEST TOO LOOSE:
- Invalid candidates accepted
- "Everything seems fine"
- High false positive rate

WELL CALIBRATED:
- Valid accepted, invalid rejected
- Appropriate selectivity
- Matches real constraints
```

---

## Common Evaluation Errors

| Error | What Happens | Fix |
|-------|--------------|-----|
| Unknown criteria | Inconsistent evaluation | Identify criteria |
| Wrong criteria type | Mismatched evaluation | Classify criterion type |
| Test too strict | Valid answers filtered out | Loosen test |
| Test too loose | Invalid answers accepted | Tighten test |
| Stated ≠ actual criteria | Evaluate wrong thing | Find actual criteria |
| Single criterion assumed | Miss other requirements | Check for multiple |
