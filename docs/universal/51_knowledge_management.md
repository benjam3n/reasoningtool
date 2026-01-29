# Universal: Knowledge Management (51)

**Category**: CORE - Knowledge Capture and Preservation
**Source**: [O: universal_goal_analysis.yaml lines 1688-1740 knowledge_management category]
**Structure**: One question per entry, VOI-marked with realistic distribution

---

## VOI Rating = Action Divergence

- **HIGH**: Different answers → completely different action paths
- **MED**: Different answers → same general direction, different approach
- **LOW**: Different answers → same actions, different framing/flavor

---

## Q1: What form is the knowledge in?
[VOI: HIGH - Tacit knowledge in minds means loss risk, convert vs maintain docs]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Tacit (in minds) | HIGH | Convert to explicit vs maintain | Convert to explicit | Actually explicit |
| Unknown form | MED | Form assessment vs assume | Form assessment | Form known |
| Mixed | MED | Convert tacit vs maintain | Convert tacit | Different mix |
| Explicit (documented) | LOW | Preserved either way | Maintain docs | Actually tacit |

---

## Q2: Is there risk of tacit knowledge being lost?
[VOI: HIGH - High loss risk means immediate capture vs lower priority]
Prerequisite: Q1 shows tacit knowledge exists

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| High loss risk | HIGH | Immediate capture vs schedule | Immediate capture | Lower risk |
| Unknown risk | MED | Risk evaluation vs assume | Risk evaluation | Risk known |
| Moderate risk | MED | Scheduled capture vs ignore | Scheduled capture | Different level |
| Low risk | LOW | When convenient either way | When convenient | Higher risk |

---

## Q3: Can tacit knowledge be converted to explicit?
[VOI: HIGH - Cannot convert means accept risk and mitigate vs convert]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| No, inherently tacit | HIGH | Mitigate risk vs convert | Mitigate risk | Can convert |
| Unknown if convertible | MED | Conversion test vs assume | Conversion test | Convertibility known |
| Yes, with effort | MED | Evaluate worth vs convert | Evaluate worth | Different effort |
| Yes, easily | LOW | Do it either way | Convert | Not easily |

---

## Q4: Do those who need access have it?
[VOI: HIGH - Few have access means major gap, expand vs maintain]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Few have access | HIGH | Expand access vs maintain | Expand access | More have |
| Unknown access status | MED | Access audit vs assume | Access audit | Status known |
| Most have access | MED | Fill gaps vs maintain | Fill gaps | More lack |
| All have access | LOW | Complete either way | Maintain | Some lack |

---

## Q5: Is version history preserved?
[VOI: HIGH - Not preserved means loss risk, start preserving vs maintain]
Prerequisite: Q7 shows versioning needed

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Not preserved | HIGH | Start preserving vs maintain | Start preserving | Preserved |
| Unknown preservation | MED | Preservation check vs assume | Preservation check | Preservation known |
| Partially preserved | MED | Improve vs maintain | Improve | Different level |
| Yes, fully preserved | LOW | Can recover either way | Maintain | Not preserved |

---

## Q6: Can previous versions be restored?
[VOI: HIGH - Cannot restore means permanent changes, extra caution vs proceed]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| No, cannot restore | HIGH | Extra caution vs proceed | Extra caution | Can restore |
| Unknown restorability | MED | Restore testing vs assume | Restore testing | Restorability known |
| Yes, with effort | MED | Acceptable recovery vs easy | Acceptable | Different effort |
| Yes, easily | LOW | Good recovery either way | Maintain | Not easily |

---

## Q7: Is version control needed?
[VOI: MED - Determines setup but doesn't change goal direction]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Unknown if needed | MED | Needs assessment vs assume | Needs assessment | Need known |
| Yes, needed | MED | Set up version control vs proceed | Set up version control | Not needed |
| No, not needed | LOW | Simpler either way | Proceed without | Actually needed |

---

## Q8: Is knowledge being created during goal pursuit?
[VOI: MED - Significant knowledge affects capture planning but not goal]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, significant knowledge | MED | Plan capture vs ignore | Plan capture | Less significant |
| Unknown if knowledge | LOW | Periodic review either way | Periodic review | Known if creating |
| Yes, minor knowledge | LOW | Consider capture either way | Consider capture | More significant |
| No knowledge created | LOW | No capture needed either way | Proceed | Knowledge created |

---

## Q9: Who needs access to this knowledge?
[VOI: MED - Broad access affects distribution but not goal direction]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Unknown access needs | MED | Access analysis vs assume | Access analysis | Needs known |
| Broad access needed | MED | Wide distribution vs targeted | Distribute widely | Narrower |
| Access needs identified | LOW | Can provide either way | Provide access | Wrong identification |
| Limited access needed | LOW | Targeted sharing either way | Share targeted | Broader |

---

## Question Order by Action Divergence

**HIGH VOI (ask first - route to different action paths):**
1. Q1: Form? (Tacit → convert vs maintain)
2. Q2: Loss risk? (High → immediate capture vs schedule)
3. Q3: Convertible? (No → mitigate risk vs convert)
4. Q4: Access? (Few have → expand vs maintain)
5. Q5: History preserved? (No → start preserving vs maintain)
6. Q6: Restorable? (No → extra caution vs proceed)

**MED/LOW VOI (ask second - refine approach):**
7. Q7: Version control needed? (Setup, not direction)
8. Q8: Knowledge created? (Capture planning, not direction)
9. Q9: Access needs? (Distribution, not direction)

---

## Key Insight

**VOI ≠ Knowledge Value**

VOI = Action Divergence

A HIGH VOI knowledge management question is one where the answer determines whether you URGENTLY CAPTURE KNOWLEDGE or PROCEED NORMALLY. "Tacit knowledge at high risk of loss" routes you to "immediate capture" - a completely different action priority than "maintain documentation."

A LOW VOI knowledge management question like "limited vs broad access needed" doesn't change your fundamental approach - you'll manage the knowledge either way, just with different distribution scope.

---

## Coverage Summary

```
QUESTIONS: 9
ENTRIES: 39

VOI Distribution:
- HIGH: 6 entries (15%)
- MED: 21 entries (54%)
- LOW: 12 entries (31%)

Note: Lower HIGH% because knowledge management is usually optimization, not strategy
```
