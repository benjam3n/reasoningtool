# Universal: Continuity and Connectedness (64)

**Category**: MATHEMATICAL - Topology Concepts
**Source**: [O: universal_goal_analysis.yaml lines 2173-2207 continuity_and_connectedness category]
**Structure**: One question per entry, VOI-marked with realistic distribution

---

## VOI Rating = Action Divergence

- **HIGH**: Different answers → completely different action paths
- **MED**: Different answers → same general direction, different approach
- **LOW**: Different answers → same actions, different framing/flavor

---

## Q1: Is there a continuous path from current state to goal state?
[VOI: HIGH - no path requires bridge or goal change vs incremental progress]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| No, gap exists | HIGH | Find bridge or change goal vs step-by-step | Find bridge or change goal | Path exists |
| Unknown if path exists | MED | Path discovery needed vs proceed | Path discovery | Path known |
| Multiple paths | LOW | Choose best path vs find any path | Choose best path | Single/no path |
| Yes, continuous path | LOW | Step-by-step progress vs need bridge | Step-by-step | No path |

---

## Q2: Is the space of possibilities connected?
[VOI: HIGH - disconnected means isolated regions, may be trapped]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| No, separate components | HIGH | Determine which component you're in vs explore freely | Know which component | Connected |
| Unknown connectedness | MED | Test connectedness vs assume connected | Connectedness check | Connectedness known |
| Yes, fully connected | LOW | Can reach anywhere vs trapped in region | Full exploration | Not connected |

---

## Q3: Is goal in same component as current state?
[VOI: HIGH - different component means cannot reach directly]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| No, different components | HIGH | Find bridge between components vs direct path | Find component bridge | Same component |
| Unknown component | HIGH | Analyze component membership vs assume reachable | Component analysis | Component known |
| Yes, same component | LOW | Path exists somewhere vs need bridge | Path exists | Different components |

---

## Q4: Can the path be traversed in small steps without jumps?
[VOI: HIGH - major jump required changes entire approach]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Major jump needed | HIGH | Prepare for discontinuous leap vs gradual | Prepare for jump | Smaller steps possible |
| Unknown step sizes | MED | Analyze step requirements vs assume gradual | Step analysis | Step sizes known |
| Some jumps required | MED | Plan for discontinuities vs all gradual | Plan for jumps | All gradual |
| Yes, all small steps | LOW | Incremental approach vs need jumps | Incremental approach | Jumps needed |

---

## Q5: What is the gap that cannot be crossed continuously?
[VOI: HIGH - unclear gap means can't plan bridge]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Gap unclear | HIGH | Gap clarification needed vs address known gap | Gap clarification | Gap clear |
| Gap clearly identified | MED | Design bridge for specific gap vs discover | Bridge the gap | Wrong gap |
| Multiple gaps | MED | Address each gap vs single solution | Address each | Single gap |
| Gap doesn't exist | LOW | Continuous path possible vs find gap | Incremental | Gap exists |

---

## Q6: For current state, what states are nearby (reachable with small changes)?
[VOI: MED - affects immediate options but not fundamental approach]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Few nearby options | MED | Careful choice among limited vs many options | Careful choice | More options |
| Only one nearby | MED | Take it or stay vs choose among | Take it or stay | Multiple nearby |
| Unknown neighborhood | MED | Map nearby options vs assume known | Neighborhood mapping | Neighborhood known |
| Many nearby options | LOW | Choose best among many vs limited | Choose best | Few options |

---

## Q7: Is there a state nearby both current and goal?
[VOI: MED - intermediate waypoint simplifies journey]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| No intermediate | MED | Direct path only vs use waypoint | Long jump or different path | Intermediate exists |
| Unknown intermediate | MED | Search for intermediate vs direct | Intermediate search | Intermediate known |
| Yes, intermediate exists | LOW | Use waypoint vs direct path | Use intermediate | No intermediate |

---

## Q8: Is the goal on the boundary of what's possible or in the interior?
[VOI: MED - boundary means active constraints vs slack available]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| On boundary | MED | Work with active constraints vs adjust freely | Active constraints | In interior |
| Unknown location | MED | Determine constraint status vs assume | Location check | Location known |
| In interior | LOW | Room for adjustment vs constrained | Room for adjustment | On boundary |

---

## Q9: Which constraints are active at the goal?
[VOI: MED - knowing binding constraints affects approach]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Constraints unclear | MED | Identify binding constraints vs work with known | Constraint identification | Constraints clear |
| Constraints identified | LOW | Work with known constraints vs wrong constraints | Work with constraints | Wrong constraints |
| No active constraints | LOW | Interior solution, no binding vs constrained | Interior solution | Constraints active |

---

## Q10: Are there discontinuities at the boundary?
[VOI: MED - sharp transitions require preparation]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, sharp transitions | MED | Prepare for sudden change vs gradual approach | Prepare for transition | Smooth |
| Unknown boundary behavior | MED | Analyze boundary vs assume smooth | Boundary analysis | Behavior known |
| No, smooth boundary | LOW | Approach confidently vs prepare for jump | Approach confidently | Discontinuities exist |

---

## Coverage Summary

```
QUESTIONS: 10
ENTRIES: 40

VOI Distribution:
- HIGH: 6 entries (15%)
- MED: 22 entries (55%)
- LOW: 12 entries (30%)
```

---

## Question Order by Action Divergence

**HIGH VOI (ask first - routes to different action paths):**
1. Q1 (Path exists?) - can we get there at all
2. Q2 (Space connected?) - trapped or free
3. Q3 (Same component?) - reachable or bridging needed
4. Q4 (Jumps needed?) - gradual or discontinuous
5. Q5 (Gap clarity?) - what to bridge

**MED VOI (ask second - same direction, different approach):**
6. Q6 (Nearby options?) - immediate moves
7. Q7 (Intermediate?) - waypoints
8. Q8 (Boundary?) - constraint status
9. Q9 (Active constraints?) - binding limits
10. Q10 (Discontinuities?) - transition preparation

---

## Key Insight

**VOI ≠ topological complexity**

**VOI = action divergence**

Q1 "Is there a continuous path?" is HIGH VOI because:
- YES → incremental progress possible
- NO → must find bridge or change goal (completely different work)

Q10 "Discontinuities at boundary?" is MED VOI because:
- YES → prepare for sharp transition
- NO → approach confidently (same approach, different preparation)

Path existence determines if the goal is achievable at all. Boundary smoothness affects how you approach an achievable goal.
