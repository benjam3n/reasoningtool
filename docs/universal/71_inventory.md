# Universal: Inventory and Resource Tracking (71)

**Category**: BUSINESS - Physical and Digital Asset Tracking
**Source**: [O: universal_goal_analysis.yaml lines 2405-2446 inventory_and_resource_tracking category]
**Structure**: One question per entry, VOI-marked with realistic distribution

---

## VOI Rating = Action Divergence

- **HIGH**: Different answers → completely different action paths
- **MED**: Different answers → same general direction, different approach
- **LOW**: Different answers → same actions, different framing/flavor

---

## Q1: What is current quantity vs needed quantity?
[VOI: HIGH - insufficient means acquisition needed vs proceed]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Insufficient (current < needed) | HIGH | Acquire more immediately | Acquire more | Sufficient |
| Unknown quantities | MED | Quantity check needed vs proceed blind | Quantity check | Quantities known |
| Marginal (current ≈ needed) | MED | Close monitoring, potential acquisition | Close monitoring | Different level |
| Sufficient (current > needed) | LOW | Proceed, monitor later | Monitor | Insufficient |

---

## Q2: When will it run out at current consumption rate?
[VOI: HIGH - soon means urgent action needed vs can plan]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Soon (days/weeks) | HIGH | Act now, urgent | Act now | Later |
| Unknown runway | MED | Runway calculation needed vs proceed | Runway calculation | Runway known |
| Medium term (months) | MED | Plan replenishment | Schedule order | Different timeline |
| Long term (years+) | LOW | Periodic check sufficient | Periodic check | Sooner |

---

## Q3: What happens when it drops below minimum?
[VOI: HIGH - critical failure requires prevention vs minor issue]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Operations disrupted | HIGH | Must prevent, maintain buffer | Maintain buffer | Less severe |
| Critical failure | HIGH | Cannot allow, strong buffer | Strong buffer | Less critical |
| Unknown consequence | MED | Consequence analysis needed vs assume ok | Consequence analysis | Consequence known |
| Minor inconvenience | LOW | Acceptable risk, lower priority | Lower priority | More severe |

---

## Q4: Is there a record of what exists, where, and quantity?
[VOI: HIGH - inaccurate/no record means flying blind]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, inaccurate record | HIGH | Verify/update before relying | Verify/update | Record accurate |
| No record | HIGH | Create record first | Create record | Record exists |
| Unknown record status | MED | Record audit needed vs assume accurate | Record audit | Status known |
| Yes, accurate record | LOW | Use record for planning | Use record | Record inaccurate |

---

## Q5: Is there a tracking system for inventory?
[VOI: HIGH - outdated/no system means unreliable data]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, outdated/inaccurate | HIGH | Update/verify system | Update/verify | System accurate |
| No system | HIGH | Create tracking system | Create system | System exists |
| Unknown system status | MED | System audit needed vs assume accurate | System audit | Status known |
| Yes, accurate system | LOW | Use system for decisions | Use system | System inaccurate |

---

## Q6: What triggers reorder (threshold, time, event)?
[VOI: HIGH - no trigger means potential stockout]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| No trigger defined | HIGH | Define trigger to prevent stockout | Define trigger | Trigger exists |
| Unknown trigger | MED | Trigger definition needed vs assume exists | Trigger definition | Trigger known |
| Multiple triggers | MED | Coordinate triggers | Coordinate | Single trigger |
| Clear trigger defined | LOW | Use existing trigger | Use trigger | Wrong trigger |

---

## Q7: Does this goal involve items that must be tracked?
[VOI: MED - tracking requirement affects approach]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, physical items | MED | Physical inventory tracking | Track inventory | No tracking needed |
| Yes, digital items | MED | Digital asset tracking | Track digitally | No tracking needed |
| Unknown if items | MED | Inventory check | Inventory check | Items known |
| No items to track | LOW | Skip tracking concerns | Skip tracking | Items exist |

---

## Q8: Are there items that can be depleted?
[VOI: MED - depletable items need monitoring]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, depletable | MED | Level monitoring needed | Track levels | Non-depletable |
| Unknown if depletable | MED | Depletability check | Depletability check | Depletability known |
| No, non-depletable | LOW | Stable supply, less monitoring | Less monitoring | Actually depletable |

---

## Q9: Are there items that must be reordered/replenished?
[VOI: MED - reorder need affects process requirements]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, regular reorder | MED | Reorder process needed | Establish process | No reorder needed |
| Unknown if reorder | MED | Reorder analysis | Reorder analysis | Reorder known |
| No, one-time acquisition | LOW | Single purchase, no process | Complete once | Regular reorder |

---

## Q10: What is the lead time from order to receipt?
[VOI: MED - long lead time requires early ordering]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Long lead time | MED | Order early, factor delay | Factor in delay | Short lead time |
| Variable lead time | MED | Buffer for uncertainty | Buffer | Consistent lead time |
| Unknown lead time | MED | Lead time discovery | Lead time discovery | Lead time known |
| Short lead time | LOW | Flexible ordering | Order as needed | Long lead time |

---

## Coverage Summary

```
QUESTIONS: 10
ENTRIES: 42

VOI Distribution:
- HIGH: 9 entries (21%)
- MED: 22 entries (52%)
- LOW: 11 entries (27%)
```

---

## Question Order by Action Divergence

**HIGH VOI (ask first - routes to different action paths):**
1. Q1 (Quantity?) - shortage or sufficient
2. Q2 (Runway?) - urgency level
3. Q3 (Consequence?) - severity of running out
4. Q4 (Record?) - data reliability
5. Q5 (System?) - tracking reliability
6. Q6 (Trigger?) - reorder process exists

**MED VOI (ask second - same direction, different approach):**
7. Q7 (Items to track?) - tracking requirement
8. Q8 (Depletable?) - monitoring need
9. Q9 (Reorder needed?) - process requirement
10. Q10 (Lead time?) - timing buffer

---

## Key Insight

**VOI ≠ inventory importance**

**VOI = action divergence**

Q1 "Current vs needed quantity?" is HIGH VOI because:
- SUFFICIENT → proceed with current stock
- INSUFFICIENT → must acquire more immediately (different work)

Q10 "What is lead time?" is MED VOI because:
- SHORT → order when needed
- LONG → order earlier (same goal, different timing)

Quantity sufficiency determines whether you need to acquire at all. Lead time just affects when you place orders.
