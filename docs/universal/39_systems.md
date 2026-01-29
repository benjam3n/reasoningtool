# Universal: Systems (39)

**Category**: CORE - Systems and Processes
**Source**: [O: universal_goal_analysis.yaml lines 847-889 systems category]
**Structure**: One question per entry, VOI-marked with realistic distribution

---

## VOI Rating = Action Divergence

- **HIGH**: Different answers → completely different action paths
- **MED**: Different answers → same general direction, different approach
- **LOW**: Different answers → same actions, different framing/flavor

---

## Q1: What systems currently support this goal?
[VOI: MED - affects system awareness but same direction]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Unknown what exists | MED | System audit vs duplicate | System audit | Systems known |
| No systems exist | MED | Build from scratch vs use existing | Build from scratch | Systems exist |
| Systems identified | LOW | Assess each vs audit | Assess each | Missing systems |

---

## Q2: How well does each system perform its function?
[VOI: HIGH - performs poorly means bottleneck requiring fix]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Performs poorly | HIGH | Fix or replace vs accept | Fix or replace | Performs well |
| Unknown performance | MED | Performance check vs assume okay | Performance check | Performance known |
| Performs adequately | LOW | Accept or improve vs analyze | Accept or improve | Different level |
| Performs well | LOW | Continue using vs improve | Continue using | Performs poorly |

---

## Q3: Is each system under my control?
[VOI: MED - affects flexibility but same direction]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Unknown control | MED | Control assessment vs assume | Control assessment | Control known |
| Partially controlled | MED | Work within limits vs seek full | Work within limits | Full control |
| Not controlled | MED | Work around vs seek control | Work around | Actually controlled |
| Under my control | LOW | Modify as needed vs analyze | Modify as needed | Not controlled |

---

## Q4: What functions need to be performed that no system handles?
[VOI: HIGH - critical/unknown gaps must be filled]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Critical gaps exist | HIGH | Create systems urgently vs proceed | Create systems | No critical gaps |
| Unknown gaps | HIGH | Gap analysis vs be stuck | Gap analysis | Gaps known |
| Minor gaps exist | MED | Prioritize vs accept | Prioritize | Different gaps |
| No gaps | LOW | Proceed vs analyze | Proceed | Gaps exist |

---

## Q5: Can missing systems be accessed, built, or substituted?
[VOI: HIGH - cannot fill gap means blocked]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Cannot fill gap | HIGH | Change approach vs keep trying | Change approach | Can fill |
| Manual substitute | MED | Accept overhead vs automate | Accept overhead | Better option |
| Must build | MED | Plan build vs access | Plan build | Can access |
| Can access existing | LOW | Access system vs build | Access system | Must build |

---

## Q6: What systems should be modified to better support the goal?
[VOI: MED - optimization but same direction]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Unknown what to modify | MED | Modification analysis vs accept | Modification analysis | Modifications known |
| Modifications identified | MED | Plan modifications vs maintain | Plan modifications | Wrong modifications |
| No modifications needed | LOW | Use as-is vs analyze | Use as-is | Modifications needed |

---

## Q7: What is the cost vs benefit of each modification?
[VOI: MED - affects modification decisions]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Unknown ratio | MED | Cost-benefit analysis vs guess | Cost-benefit analysis | Ratio known |
| Cost exceeds benefit | MED | Skip modification vs proceed | Skip modification | Actually worth it |
| Benefit exceeds cost | LOW | Make modification vs analyze | Make modification | Cost exceeds |

---

## Q8: What systems currently interfere with the goal?
[VOI: HIGH - interfering/unknown systems work against you]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Interfering systems exist | HIGH | Address interference vs be blocked | Address interference | No interference |
| Unknown interference | HIGH | Interference audit vs be surprised | Interference audit | Interference known |
| No interference | LOW | Proceed vs analyze | Proceed | Interference exists |

---

## Q9: Can interfering systems be modified or removed?
[VOI: HIGH - cannot modify means must design around]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Cannot modify/remove | HIGH | Design around vs keep trying | Design around | Can fix |
| Unknown if possible | MED | Feasibility check vs assume | Feasibility check | Possibility known |
| Can modify/remove | MED | Fix interference vs work around | Fix interference | Cannot |

---

## Q10: Are default behaviors appropriate when no decision is made?
[VOI: HIGH - poor/unknown defaults means risky inaction]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Poor defaults | HIGH | Change defaults vs accept risk | Change defaults | Good defaults |
| Unknown defaults | HIGH | Default audit vs be surprised | Default audit | Defaults known |
| No defaults | MED | Define defaults vs accept chaos | Define defaults | Defaults exist |
| Good defaults | LOW | Acceptable defaults vs improve | Acceptable defaults | Poor defaults |

---

## Q11: Is there a fallback plan if primary approach fails?
[VOI: HIGH - no fallback means single point of failure]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| No fallback exists | HIGH | Create fallback vs single path | Create fallback | Fallback exists |
| Unknown if fallback | MED | Fallback audit vs assume | Fallback audit | Fallback known |
| Fallback exists untested | MED | Test fallback vs trust | Test fallback | Tested |
| Fallback exists and tested | LOW | Maintain fallback vs create new | Maintain fallback | Not tested |

---

## Question Order by Action Divergence

**HIGH VOI Questions (ask first - route to different action paths):**
1. Q8: What systems interfere? (what's working against you?)
2. Q4: What functions are missing? (what's needed?)
3. Q11: Is there a fallback? (what if it fails?)
4. Q2: How well does each system perform? (bottlenecks)
5. Q10: Are defaults appropriate? (safe inaction?)
6. Q9: Can interfering systems be modified? (fix or work around?)
7. Q5: Can missing systems be filled? (feasibility)

**MED VOI Questions (ask second - same direction, different approach):**
8. Q1: What systems exist? (inventory)
9. Q3: Is each system under my control? (flexibility)
10. Q6: What modifications would help? (optimization)
11. Q7: What is cost vs benefit of modifications? (trade-offs)

---

## Key Insight

**VOI ≠ Importance or Severity**

VOI = Action Divergence

A question has HIGH VOI when different answers lead to completely different action paths. "Are there systems interfering?" is HIGH VOI because YES → address interference or design around, NO → proceed normally. These are fundamentally different approaches.

Systems and processes either enable your goal or create friction against it.

---

## Coverage Summary

```
QUESTIONS: 11
ENTRIES: 46

VOI Distribution:
- HIGH: 10 entries (22%)
- MED: 21 entries (46%)
- LOW: 15 entries (32%)

HIGH-VOI Entries (ask first):
- Q2: Performs poorly - bottleneck
- Q4: Critical gaps / Unknown gaps - must fill
- Q5: Cannot fill gap - blocked
- Q8: Interfering / Unknown interference - working against
- Q9: Cannot modify - must work around
- Q10: Poor defaults / Unknown - risky inaction
- Q11: No fallback - single point of failure
```
