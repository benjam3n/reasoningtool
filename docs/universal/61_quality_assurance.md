# Universal: Quality Assurance (61)

**Category**: APPLIED - Output Quality
**Source**: [O: universal_goal_analysis.yaml lines 2906-2956 quality_assurance category]
**Structure**: One question per entry, VOI-marked with realistic distribution

---

## VOI Rating = Action Divergence

- **HIGH**: Different answers → completely different action paths
- **MED**: Different answers → same general direction, different approach
- **LOW**: Different answers → same actions, different framing/flavor

---

## Q1: Is there a specification defining quality?
[VOI: HIGH - without spec, you measure against nothing vs against defined standard]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Vague spec | HIGH | Clarify spec first vs measure against unclear target | Clarify spec | Clear spec |
| No spec | HIGH | Define spec vs measure against undefined standard | Define spec | Spec exists |
| Unknown if spec | MED | Spec discovery vs proceed to measure | Spec discovery | Spec known |
| Yes, clear spec | LOW | Measure against spec vs no clear spec | Measure against spec | No clear spec |

---

## Q2: Is the specification documented and accessible?
[VOI: HIGH - undocumented spec forces tacit knowledge vs documented reference]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Not documented | HIGH | Document tacit knowledge vs use existing docs | Document | Documented |
| Partially documented | MED | Complete gaps vs use available docs | Complete docs | Different level |
| Unknown documentation | MED | Documentation audit vs proceed | Documentation check | Documentation known |
| Yes, documented | LOW | Reference docs vs not documented | Use docs | Not documented |

---

## Q3: What happens when defects are found?
[VOI: HIGH - inconsistent handling vs consistent fix process]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Sometimes fixed | HIGH | Enforce always-fix policy vs maintain current | Always fix | Always fixed |
| Not fixed | HIGH | Change practice to fix vs continue bad quality | Change practice | Fixed |
| Unknown handling | MED | Review handling process vs proceed | Handling review | Handling known |
| Fixed before release | LOW | Continue current vs not always fixed | Continue | Not always fixed |

---

## Q4: Are there defects present?
[VOI: HIGH - significant defects require fix before release vs proceed]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Significant defects | HIGH | Fix before release vs proceed | Fix before release | Less significant |
| Minor defects | MED | Fix or accept tradeoff | Fix or accept | Different level |
| Unknown defect status | MED | Defect check vs proceed | Defect check | Status known |
| No known defects | LOW | Maintain quality vs defects exist | Maintain | Defects exist |

---

## Q5: What is causing defects?
[VOI: HIGH - unknown cause means blind fixing vs targeted fix]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Cause unclear | HIGH | Root cause analysis vs fix symptoms | Find cause | Cause clear |
| Unknown cause | HIGH | Cause analysis vs blind fixing | Cause analysis | Cause known |
| Cause identified | MED | Fix root cause vs wrong cause | Fix cause | Wrong cause |
| No defects to analyze | LOW | Maintain quality vs defects exist | Maintain | Defects exist |

---

## Q6: Are there recurring defects?
[VOI: HIGH - recurring defects require process fix vs symptom fix]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, same defects repeat | HIGH | Fix process vs fix instances | Fix process | No recurrence |
| Occasionally repeat | MED | Process improvement vs maintain | Improve process | Different level |
| Unknown recurrence | MED | Recurrence analysis vs proceed | Recurrence check | Recurrence known |
| No recurrence | LOW | Maintain process vs recurrence exists | Maintain | Recurrence exists |

---

## Q7: Can the process consistently produce quality output?
[VOI: HIGH - inconsistent process needs overhaul vs maintain current]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Sometimes | HIGH | Process improvement vs maintain | Improve process | Consistent |
| Rarely | HIGH | Major process overhaul vs minor tweaks | Major overhaul | Better than thought |
| Unknown capability | MED | Capability assessment vs proceed | Capability assessment | Capability known |
| Yes, consistently | LOW | Maintain process vs inconsistent | Maintain | Inconsistent |

---

## Q8: Can defects be traced to source?
[VOI: HIGH - no traceability means can't investigate vs can investigate]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| No traceability | HIGH | Add tracing infrastructure vs investigate directly | Add tracing | Traceable |
| Partial traceability | MED | Improve tracing vs use existing | Improve | Different level |
| Unknown traceability | MED | Traceability check vs assume traceable | Traceability check | Traceability known |
| Yes, full traceability | LOW | Use traceability vs limited | Use traceability | Limited |

---

## Q9: Is output being inspected for quality?
[VOI: HIGH - no inspection means defects escape vs caught]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| No inspection | HIGH | Add inspection process vs maintain none | Add inspection | Inspection exists |
| Yes, ad hoc | MED | Systematize inspection vs maintain ad hoc | Systematize | Different level |
| Unknown if inspected | MED | Inspection audit vs proceed | Inspection audit | Inspection known |
| Yes, systematic inspection | LOW | Maintain inspection vs no inspection | Maintain | No inspection |

---

## Q10: Can detection move earlier in process?
[VOI: MED - efficiency improvement vs current timing]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, significantly earlier | MED | Shift left vs maintain timing | Shift left | Cannot |
| Unknown if earlier | MED | Detection timing analysis vs proceed | Detection timing | Timing known |
| Yes, somewhat earlier | LOW | Consider shift vs current timing | Consider shift | Different amount |
| No, already early | LOW | Maintain current vs can shift | Maintain | Can shift |

---

## Coverage Summary

```
QUESTIONS: 10
ENTRIES: 43

VOI Distribution:
- HIGH: 12 entries (28%)
- MED: 18 entries (42%)
- LOW: 13 entries (30%)

Note: Higher HIGH% because quality failures cascade to customers
```

---

## Question Order by Action Divergence

**HIGH VOI (ask first - routes to different action paths):**
1. Q1 (Spec?) - defines what quality means
2. Q2 (Documented?) - accessible standard
3. Q3 (Defects fixed?) - handling consistency
4. Q4 (Defects present?) - current state
5. Q5 (Defect cause?) - where to fix
6. Q6 (Recurring?) - process vs instance fix
7. Q7 (Process consistent?) - process capability
8. Q8 (Traceable?) - investigation capability
9. Q9 (Inspection?) - detection exists

**MED VOI (ask second - same direction, different approach):**
10. Q10 (Earlier detection?) - efficiency improvement

---

## Key Insight

**VOI ≠ importance or severity**

**VOI = action divergence**

A question has HIGH VOI when different answers lead to completely different action paths. Q1 "Is there a spec?" is HIGH VOI because:
- YES → measure against spec
- NO → must define spec first (completely different work)

Q10 "Can detection move earlier?" is MED VOI because:
- YES → improve timing (optimization)
- NO → keep current timing (same general approach)

Both questions matter for quality. But Q1 determines whether you can even measure quality, while Q10 optimizes an existing process.
