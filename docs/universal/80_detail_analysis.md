# Universal: Detail Analysis (80)

**Category**: APPLIED - Thorough Examination of Specifics
**Source**: [O: universal_goal_analysis.yaml lines 2962-3005 detail_analysis category]
**Structure**: One question per entry, VOI-marked with realistic distribution

---

## VOI Rating = Action Divergence

- **HIGH**: Different answers → completely different action paths
- **MED**: Different answers → same general direction, different approach
- **LOW**: Different answers → same actions, different framing/flavor

---

## Q1: For each piece of information, is it correct?
[VOI: HIGH - errors require fixes vs correct enables proceeding]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Some errors | HIGH | Fix errors vs proceed with errors | Fix errors | All correct |
| Unknown accuracy | MED | Accuracy check vs proceed | Accuracy check | Accuracy known |
| All correct | LOW | Proceed | Proceed | Errors exist |

---

## Q2: Is information consistent across locations?
[VOI: HIGH - inconsistencies require resolution vs consistency enables proceeding]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Inconsistencies exist | HIGH | Resolve conflicts vs proceed with conflicts | Resolve | Consistent |
| Unknown consistency | MED | Consistency check vs proceed | Consistency check | Consistency known |
| Yes, consistent | LOW | Proceed | Proceed | Inconsistent |

---

## Q3: If same info appears multiple places, do they match?
[VOI: HIGH - mismatches require determining which is right vs matches enable proceeding]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Mismatches exist | HIGH | Resolve which is right vs proceed with conflict | Resolve | All match |
| Unknown if match | MED | Match check vs proceed | Match check | Match known |
| Yes, all match | LOW | Proceed | Proceed | Mismatch |

---

## Q4: Are all required elements present?
[VOI: HIGH - missing elements require adding vs complete enables proceeding]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Some missing | HIGH | Add missing vs proceed incomplete | Add missing | All present |
| Unknown if complete | MED | Completeness check vs proceed | Completeness check | Completeness known |
| Yes, all present | LOW | Finalize | Finalize | Missing elements |

---

## Q5: Has each element been verified?
[VOI: HIGH - none verified means all assumptions vs verified means confirmed]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| None verified | HIGH | Verify all vs proceed on assumptions | Verify all | Some verified |
| Some not verified | MED | Verify remaining vs proceed partial | Verify remaining | All verified |
| Unknown verification | MED | Verification check vs proceed | Verification check | Verification known |
| All verified | LOW | Proceed with confidence | Proceed | Not all verified |

---

## Q6: How was correctness verified?
[VOI: HIGH - no verification means assumptions vs verification means confirmed]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| No verification | HIGH | Verify vs proceed unverified | Verify | Some verification |
| Secondary verification | MED | Accept with note vs reverify | Accept with note | Different method |
| Unknown method | MED | Method check vs proceed | Method check | Method known |
| Primary source verification | LOW | Trust verification | Trust | Weaker method |

---

## Q7: Could information have changed since verification?
[VOI: HIGH - likely changed requires reverification vs stable enables proceeding]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, likely changed | HIGH | Reverify vs proceed with stale | Reverify | Stable |
| Yes, may have changed | MED | Recheck vs proceed | Reverify | Stable |
| Unknown if changed | MED | Currency check vs proceed | Currency check | Currency known |
| No, stable information | LOW | Proceed | Proceed | Actually changed |

---

## Q8: Are there edge cases that haven't been considered?
[VOI: HIGH - uncovered edges will fail in unusual cases vs covered is robust]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Edge cases not covered | HIGH | Cover edges vs proceed with gaps | Cover edges | All covered |
| Unknown if covered | MED | Edge case review vs proceed | Edge case review | Coverage known |
| All edge cases covered | LOW | Proceed robust | Proceed | Edge cases missed |

---

## Q9: What happens at boundaries (min, max, empty, null)?
[VOI: HIGH - unhandled boundaries will fail at edges vs handled is robust]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Boundaries not handled | HIGH | Handle boundaries vs proceed with gaps | Handle boundaries | Handled |
| Unknown if handled | MED | Boundary check vs proceed | Boundary check | Handling known |
| Boundaries handled | LOW | Proceed robust | Proceed | Boundaries not handled |

---

## Q10: For each reference, does referenced thing exist and is it current?
[VOI: HIGH - broken references require fixing vs valid enables proceeding]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Broken references | HIGH | Fix references vs proceed with broken | Fix references | All valid |
| Unknown if valid | MED | Reference check vs proceed | Reference check | Validity known |
| All references valid | LOW | Proceed | Proceed | Broken references |

---

## Q11: Is there a checklist of required elements?
[VOI: MED - no checklist may miss items vs checklist enables systematic check]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| No checklist | MED | Create checklist vs proceed without | Create checklist | Checklist exists |
| Unknown if checklist | LOW | Checklist search vs proceed | Checklist search | Checklist known |
| Yes, checklist exists | LOW | Use checklist | Use checklist | No checklist |

---

## Q12: Does format match requirements/standards?
[VOI: MED - format issues require fixing vs correct format proceeds]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Format issues | MED | Fix format vs proceed non-compliant | Fix format | Format correct |
| Unknown format compliance | LOW | Format check vs proceed | Format check | Format known |
| Yes, format correct | LOW | Proceed | Proceed | Format wrong |

---

## Coverage Summary

```
QUESTIONS: 12
ENTRIES: 46

VOI Distribution:
- HIGH: 10 entries (22%)
- MED: 20 entries (43%)
- LOW: 16 entries (35%)
```

---

## Question Order by Action Divergence

**HIGH VOI (ask first - routes to different action paths):**
- Q1: Correct? - accuracy foundation
- Q2-Q3: Consistent? Match? - conflicts require resolution
- Q4-Q6: Complete? Verified? Method? - coverage and confirmation
- Q7: Changed? - currency
- Q8-Q10: Edges? Boundaries? References? - robustness

**MED VOI (ask second - same direction, different approach):**
- Q11-Q12: Checklist, format - systematic checking and compliance

---

## Key Insight

**VOI ≠ detail importance or precision level**

**VOI = action divergence**

A question has HIGH VOI when knowing the answer changes what you do next (fix errors vs proceed, resolve conflicts vs accept, handle boundaries vs ignore). Low VOI questions refine quality within an established verification approach.
