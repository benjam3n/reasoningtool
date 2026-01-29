# Universal: Validation (19)

**Category**: QUALITY - Validation/Verification
**Source**: [D: CORE DIMENSIONS - Validation (how to verify)]
**Structure**: One question per entry, VOI-marked with realistic distribution

---

## VOI Rating = Action Divergence

- **HIGH**: Different answers → completely different action paths (like phone tree routing to different departments)
- **MED**: Different answers → same general direction, different approach
- **LOW**: Different answers → same actions, different framing/flavor

---

## Q1: Is validation required?
[VOI: HIGH - not required (rare) → skip validation; required → plan validation; completely different paths]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| No, not required | HIGH | Skip validation vs plan | Skip validation | Actually required |
| Yes, required | MED | Plan validation | Plan validation | Not required |
| Depends on outcome | MED | Conditional planning | Decide based on result | Always/never |
| Unknown if required | MED | Clarify first | Requirement clarification | Requirement known |

---

## Q2: What validation criteria exist?
[VOI: HIGH - no criteria → can't validate; wrong criteria → validating wrong thing; different paths]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| No criteria | HIGH | Define criteria first | Define criteria first | Criteria exist |
| Wrong criteria | HIGH | Fix criteria first | Fix criteria | Criteria correct |
| Vague criteria | MED | Clarify criteria | Clarify criteria | Criteria clear |
| Unknown criteria | MED | Discover criteria | Criteria discovery | Criteria known |
| Clear criteria exist | LOW | Apply criteria | Apply criteria | Criteria unclear |

---

## Q3: Who validates?
[VOI: HIGH - third-party → meet external standards; unknown → must determine first; different requirements]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Third-party validates | HIGH | External standards | Meet external standards | Self or stakeholder |
| Unknown who validates | HIGH | Determine first | Validator discovery | Validator known |
| Self-validation | MED | Self-assessment | Self-assessment | External validation |
| Stakeholder validates | MED | Their criteria | Meet their criteria | Self or third-party |
| Multiple validators | MED | Consensus needed | Meet all criteria | Single validator |

---

## Q4: What happens if validation fails?
[VOI: HIGH - no retry → must pass first time; retry → can iterate; completely different approaches]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| No retry (fatal) | HIGH | Maximize first-time success | Maximize success | Retry possible |
| Escalation | MED | Prepare escalation | Prepare escalation | No escalation |
| Unknown consequence | MED | Determine first | Consequence discovery | Consequence known |
| Retry allowed | LOW | Can iterate | Fix and retry | No retry |

---

## Q5: What validation method is used?
[VOI: HIGH - no formal method → formalize; known method → apply it]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| No formal method | HIGH | Formalize method first | Formalize method | Method exists |
| Testing (empirical) | MED | Evidence-based | Run tests | Different method |
| Review (expert judgment) | MED | Opinion-based | Get review | Different method |
| Unknown method | MED | Select method | Choose method | Method known |
| Comparison (benchmarking) | LOW | Relative assessment | Compare to benchmark | Different method |
| Checklist (criteria) | LOW | Systematic check | Use checklist | Different method |

---

## Q6: What is the validation threshold?
[VOI: HIGH - subjective → manage evaluator; objective → meet threshold; different approaches]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Subjective (judgment) | HIGH | Manage subjectivity | Manage subjectivity | Objective |
| Pass/fail (binary) | MED | Clear cutoff | Meet threshold | Gradient |
| Gradient (degrees) | MED | Meet minimum | Meet minimum level | Binary |
| Unknown threshold | MED | Clarify first | Threshold clarification | Threshold known |

---

## Q7: What is the cost of validation?
[VOI: HIGH - high cost → weigh cost vs benefit; low/no cost → always validate; different decisions]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| High cost | HIGH | Cost-benefit analysis | Weigh cost vs benefit | Lower cost |
| Moderate cost | MED | Budget for validation | Budget for validation | Different cost |
| Unknown cost | MED | Assessment needed | Cost assessment | Cost known |
| Low cost | LOW | Include validation | Include validation | Higher cost |
| No cost | LOW | Always validate | Always validate | Cost exists |

---

## Q8: How rigorous must validation be?
[VOI: HIGH - formal certification → certification process; informal → quick check; different processes]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Formal certification | HIGH | Certification process | Certification process | Less formal |
| Rigorous (comprehensive) | MED | Thorough process | Comprehensive process | Less rigor |
| Unknown rigor | MED | Determine first | Rigor determination | Rigor known |
| Moderate (standard) | LOW | Standard process | Standard process | Different rigor |
| Informal (quick check) | LOW | Quick check | Quick check | More rigor |

---

## Q9: What documentation is required?
[VOI: HIGH - audit trail → build traceable records; none → skip documentation; different processes]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Audit trail required | HIGH | Build traceable records | Build audit trail | No audit needed |
| Full documentation | MED | Document everything | Document everything | Less documentation |
| Light documentation | LOW | Keep notes | Keep notes | More documentation |
| No documentation | LOW | Skip documentation | Skip documentation | Documentation needed |
| Unknown requirements | LOW | Determine later | Documentation decision | Requirements known |

---

## Q10: When does validation happen?
[VOI: MED - affects planning but not fundamental approach]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Before action | MED | Pre-validation | Validate before acting | After |
| During action | MED | Continuous monitoring | Monitor during | Before/after |
| After action | LOW | Post-validation | Validate after | Before/during |
| Multiple times | LOW | Multiple checkpoints | Plan multiple checks | Single time |
| Unknown timing | LOW | Decide timing | Timing decision | Timing known |

---

## Coverage Summary

```
QUESTIONS: 10
GUESSES: 52

VOI Distribution:
- HIGH: 12 guesses (23%)
- MED: 23 guesses (44%)
- LOW: 17 guesses (33%)

HIGH-VOI Entries (ask first):
- Q1: Not required - skip validation entirely
- Q2: No / Wrong criteria - can't validate correctly
- Q3: Third-party / Unknown validator - external standards
- Q4: No retry - must pass first time
- Q5: No formal method - must formalize
- Q6: Subjective - manage evaluator
- Q7: High cost - cost-benefit decision
- Q8: Formal certification - certification process
- Q9: Audit trail - traceable records required
```

---

## Question Order by Action Divergence

1. **Q1: Required** (HIGH for no) - Is validation needed at all
2. **Q2: Criteria** (HIGH) - What are we validating against
3. **Q4: Failure handling** (HIGH for no retry) - Can we iterate
4. **Q3: Who validates** (HIGH for third-party) - Authority
5. **Q5: Method** (HIGH for none) - How to validate
6. **Q6: Threshold** (HIGH for subjective) - Pass/fail standard
7. **Q7: Cost** (HIGH for high) - Investment decision
8. **Q8: Rigor** (HIGH for certification) - Process formality
9. **Q9: Documentation** (HIGH for audit) - Record requirements
10. **Q10: Timing** (MED) - When to validate

---

## Key Insight

**VOI ≠ Importance or Difficulty**
**VOI = Action Divergence**

A validation requirement being "important" doesn't make it HIGH-VOI. The question is: does knowing the answer change what you DO?

- No retry is HIGH-VOI because you must maximize first-time success vs can iterate
- Third-party validation is HIGH-VOI because external standards vs self-assessment
- Validation timing is LOW/MED-VOI because the fundamental approach stays similar
