# Universal: Graph and Network (66)

**Category**: MATHEMATICAL - Graph Theory Analysis
**Source**: [O: universal_goal_analysis.yaml lines 2246-2281 graph_and_network category]
**Structure**: One question per entry, VOI-marked with realistic distribution

---

## VOI Rating = Action Divergence

- **HIGH**: Different answers → completely different action paths
- **MED**: Different answers → same general direction, different approach
- **LOW**: Different answers → same actions, different framing/flavor

---

## Q1: Is there a path from current state to goal?
[VOI: HIGH - no path means unreachable, must add edges or change goal]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| No path exists | HIGH | Add edges or change goal vs traverse | Add edges or change goal | Path exists |
| Unknown if path | MED | Path search needed vs proceed | Path search | Path known |
| Yes, path exists | LOW | Find and follow path vs no path | Find and follow | No path |

---

## Q2: Are there critical edges that appear in all paths?
[VOI: HIGH - bottleneck edges are single points of failure]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, bottleneck edges | HIGH | Protect bottlenecks, build redundancy | Protect bottlenecks | No bottlenecks |
| Unknown if bottlenecks | MED | Analyze for critical paths vs assume robust | Bottleneck analysis | Bottlenecks known |
| No bottlenecks | LOW | Multiple routes available vs protect specific | Multiple routes | Bottlenecks exist |

---

## Q3: Are there cycles (paths that return to starting point)?
[VOI: HIGH - undesirable cycles mean stuck in loops]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, undesirable cycles | HIGH | Break cycles vs get stuck | Break cycles | Desirable/no cycles |
| Unknown if cycles | MED | Cycle detection needed vs assume acyclic | Cycle detection | Cycles known |
| Yes, desirable cycles | LOW | Maintain sustainable loops vs break | Maintain cycles | No cycles |
| No cycles | LOW | Linear progression vs cycles exist | Linear progression | Cycles exist |

---

## Q4: Can undesirable cycles be broken?
[VOI: HIGH - unbreakable cycles mean stuck forever]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| No, not breakable | HIGH | Avoid entering cycle entirely | Avoid entering | Breakable |
| Unknown if breakable | MED | Analyze before entering vs assume | Breakability analysis | Breakability known |
| Yes, breakable | MED | Can escape, enter with caution | Break cycle | Not breakable |

---

## Q5: Are there nodes whose removal disconnects the graph?
[VOI: HIGH - critical nodes are single points of failure]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, critical nodes | HIGH | Protect critical nodes, build redundancy | Protect critical | No critical |
| Unknown criticality | MED | Analyze node criticality vs assume robust | Criticality analysis | Criticality known |
| No critical nodes | LOW | Robust structure vs protect specific | Distributed | Critical nodes exist |

---

## Q6: Can the problem be represented as a graph?
[VOI: MED - graph representation enables graph tools]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Partially graph-like | MED | Some graph tools apply vs full or none | Selective use | Different level |
| Yes, natural graph | LOW | Use graph analysis tools | Use graph analysis | Not a graph |
| No, not a graph | LOW | Different model needed vs graph | Other approaches | Graph structure exists |
| Unknown if graph | LOW | Model exploration needed | Graph test | Model known |

---

## Q7: What are the nodes (entities)?
[VOI: MED - wrong nodes means wrong analysis]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Nodes ambiguous | MED | Clarify node definition vs proceed | Clarify nodes | Nodes clear |
| Unknown nodes | MED | Node identification needed vs proceed | Node identification | Nodes known |
| Nodes clearly defined | LOW | Work with defined nodes vs wrong nodes | Work with nodes | Wrong nodes |

---

## Q8: What are the edges (relationships)?
[VOI: MED - wrong edges means wrong connectivity]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Edges ambiguous | MED | Clarify relationships vs proceed | Clarify edges | Edges clear |
| Unknown edges | MED | Edge discovery needed vs proceed | Edge discovery | Edges known |
| Edges clearly defined | LOW | Use relationships vs wrong edges | Use relationships | Wrong edges |

---

## Q9: Are edges directed (one-way) or undirected (two-way)?
[VOI: MED - direction affects traversal options]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| All directed | MED | Respect one-way direction vs assume bidirectional | Respect direction | Undirected |
| Mixed | MED | Check direction each edge vs uniform | Check each | Uniform direction |
| Unknown direction | MED | Direction analysis needed vs assume | Direction analysis | Direction known |
| All undirected | LOW | Both ways available vs one-way | Flexible traversal | Directed |

---

## Q10: What is the shortest/lowest-cost path?
[VOI: MED - affects efficiency of reaching goal]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Only one path | MED | No alternatives, must take it | Must take it | Other paths exist |
| Optimal unknown | MED | Path optimization needed vs suboptimal | Path optimization | Optimal known |
| Optimal path known | LOW | Follow optimal path vs suboptimal | Follow optimal | Suboptimal path |
| Multiple good paths | LOW | Choose by secondary criteria | Choose by criteria | Single path |

---

## Q11: Which nodes have the most connections?
[VOI: MED - hubs provide leverage points]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Unknown centrality | MED | Centrality analysis needed vs miss leverage | Centrality analysis | Centrality known |
| Hub nodes identified | LOW | Leverage hubs vs wrong hubs | Leverage hubs | Wrong hubs |
| No clear hubs | LOW | Distributed approach vs target hubs | Equal treatment | Hubs exist |

---

## Coverage Summary

```
QUESTIONS: 11
ENTRIES: 44

VOI Distribution:
- HIGH: 6 entries (14%)
- MED: 21 entries (48%)
- LOW: 17 entries (38%)
```

---

## Question Order by Action Divergence

**HIGH VOI (ask first - routes to different action paths):**
1. Q1 (Path exists?) - reachable or not
2. Q2 (Bottleneck edges?) - single points of failure
3. Q3 (Undesirable cycles?) - getting stuck
4. Q4 (Cycles breakable?) - escape possible
5. Q5 (Critical nodes?) - single points of failure

**MED VOI (ask second - same direction, different approach):**
6. Q6 (Graph representation?) - tool applicability
7. Q7 (Nodes?) - entity identification
8. Q8 (Edges?) - relationship identification
9. Q9 (Direction?) - traversal constraints
10. Q10 (Optimal path?) - efficiency
11. Q11 (Hubs?) - leverage points

---

## Key Insight

**VOI ≠ graph theory complexity**

**VOI = action divergence**

Q1 "Path exists?" is HIGH VOI because:
- YES → find and traverse the path
- NO → must add connections or change goal (completely different work)

Q11 "Which nodes are hubs?" is MED VOI because:
- IDENTIFIED → leverage hubs for efficiency
- DISTRIBUTED → equal treatment (same goal, different optimization)

Path existence determines if the goal is achievable. Hub identification optimizes how you achieve an achievable goal.
