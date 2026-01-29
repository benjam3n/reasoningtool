# Universal: Invoicing and Billing (72)

**Category**: BUSINESS - Financial Documentation and Payment
**Source**: [O: universal_goal_analysis.yaml lines 2451-2487 invoicing_and_billing category]
**Structure**: One question per entry, VOI-marked with realistic distribution

---

## VOI Rating = Action Divergence

- **HIGH**: Different answers → completely different action paths
- **MED**: Different answers → same general direction, different approach
- **LOW**: Different answers → same actions, different framing/flavor

---

## Q1: Has it been invoiced?
[VOI: HIGH - not invoiced means lost revenue vs tracking payment]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| No, not invoiced | HIGH | Invoice immediately, capture revenue | Invoice now | Already invoiced |
| Unknown if invoiced | HIGH | Invoice audit to find gaps | Invoice audit | Status known |
| Yes, invoiced | LOW | Track payment status | Monitor | Not invoiced |

---

## Q2: Has everything billable been captured?
[VOI: HIGH - missed items mean lost revenue]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| No, items missed | HIGH | Find and bill missed items | Find and bill | All captured |
| Unknown completeness | MED | Completeness audit | Completeness audit | Completeness known |
| Yes, all captured | LOW | Proceed with billing | Proceed | Items missed |

---

## Q3: Are quantities, rates, and calculations correct?
[VOI: HIGH - errors damage reputation and revenue]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Errors exist | HIGH | Fix errors before sending | Fix before sending | All correct |
| Unknown accuracy | MED | Accuracy check needed | Accuracy check | Accuracy known |
| Yes, all correct | LOW | Send invoice | Send | Errors exist |

---

## Q4: How many days overdue are unpaid invoices?
[VOI: HIGH - very overdue requires escalation vs gentle reminder]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Very overdue (30+) | HIGH | Escalate collection efforts | Escalate | Less overdue |
| Unknown overdue status | MED | Overdue check needed | Overdue check | Status known |
| Slightly overdue (1-30) | MED | Gentle follow-up reminder | Gentle follow-up | Different status |
| Not overdue yet | LOW | Monitor, no action yet | Monitor | Already overdue |

---

## Q5: Has follow-up been sent for overdue invoices?
[VOI: HIGH - no follow-up means forgotten debt]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| No, not followed up | HIGH | Follow up immediately | Follow up now | Already followed up |
| Unknown if followed up | MED | Follow-up check needed | Follow-up check | Status known |
| Yes, followed up | LOW | Await response, monitor | Await response | No follow-up |

---

## Q6: Are payment terms defined and agreed?
[VOI: HIGH - no terms means cannot enforce payment]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| No terms defined | HIGH | Define terms before billing | Define terms | Terms defined |
| Terms exist but not agreed | MED | Get formal agreement | Get agreement | Terms agreed |
| Unknown if terms | MED | Terms check needed | Terms check | Terms known |
| Yes, clear agreed terms | LOW | Reference terms, proceed | Reference terms | Terms unclear |

---

## Q7: Are there items, services, or deliverables that should be invoiced?
[VOI: MED - determines if invoicing applies]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, billable items | MED | Invoice process needed | Invoice them | Nothing billable |
| Unknown if billable | MED | Billability check | Billability check | Billability known |
| No, nothing billable | LOW | Skip invoicing | Skip | Items are billable |

---

## Q8: Has the billable item been delivered/completed?
[VOI: MED - delivery status affects whether can invoice]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| No, not yet delivered | MED | Wait for delivery or milestone | Wait for delivery | Already delivered |
| Partially delivered | MED | Milestone billing approach | Milestone billing | Different status |
| Unknown delivery status | MED | Delivery verification needed | Delivery verification | Status known |
| Yes, delivered | LOW | Can invoice | Send invoice | Not delivered |

---

## Q9: Are there outstanding invoices?
[VOI: MED - outstanding invoices need tracking]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, outstanding | MED | Track and follow up | Track and collect | All paid |
| Unknown outstanding | MED | Invoice review needed | Invoice review | Status known |
| No, all paid | LOW | Healthy cash flow, maintain | Maintain | Outstanding exist |

---

## Q10: Are there penalties for late payment or discounts for early?
[VOI: MED - incentives affect collection approach]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, penalties/discounts | MED | Apply incentives in communication | Apply | No penalties/discounts |
| Unknown incentives | LOW | Check terms for incentives | Terms review | Incentives known |
| No incentives | LOW | Standard terms, simple billing | Simple billing | Incentives exist |

---

## Coverage Summary

```
QUESTIONS: 10
ENTRIES: 38

VOI Distribution:
- HIGH: 7 entries (18%)
- MED: 18 entries (47%)
- LOW: 13 entries (35%)
```

---

## Question Order by Action Divergence

**HIGH VOI (ask first - routes to different action paths):**
1. Q1 (Invoiced?) - revenue captured or not
2. Q2 (Complete?) - all items billed
3. Q3 (Accurate?) - correct amounts
4. Q4 (Overdue?) - collection urgency
5. Q5 (Followed up?) - debt remembered
6. Q6 (Terms?) - enforceable or not

**MED VOI (ask second - same direction, different approach):**
7. Q7 (Billable items?) - invoicing applies
8. Q8 (Delivered?) - can invoice yet
9. Q9 (Outstanding?) - tracking needed
10. Q10 (Incentives?) - collection approach

---

## Key Insight

**VOI ≠ financial amount**

**VOI = action divergence**

Q1 "Has it been invoiced?" is HIGH VOI because:
- YES → track payment
- NO → must invoice immediately (different work entirely)

Q10 "Penalties/discounts?" is MED VOI because:
- YES → mention incentives in follow-up
- NO → standard follow-up (same collection process, different messaging)

Invoice status determines whether you've captured revenue at all. Incentives just affect how you communicate about collection.
