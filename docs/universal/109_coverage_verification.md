# Universal: Coverage Verification (109)

**Category**: META - Did We Cover Everything Mentioned
**Source**: Derived from mentioned_coverage_gate skill - the gate that checks if all user-mentioned items were addressed
**Structure**: One question per entry, VOI-marked with realistic distribution

---

## Why This Exists

When users mention multiple items, it's easy to address some and drop others.
This category provides question-guesses for verifying complete coverage.

---

## VOI Rating = Action Divergence

- **HIGH**: Different answers → completely different action paths
- **MED**: Different answers → same general direction, different approach
- **LOW**: Different answers → same actions, different framing/flavor

---

## Q1: Did I extract ALL items the user mentioned?

[VOI: HIGH - determines whether you're addressing user's actual request]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Missed some explicit items | HIGH | Re-extract vs. proceed | Dropped user request | Address wrong items |
| Unknown if complete | HIGH | Verify extraction vs. proceed | May drop items | Proceed with gaps |
| Missed implied items ("etc.") | MED | Expand extraction vs. literal | Incomplete extraction | Partially cover |
| Missed meta-items | MED | Add meta-items vs. content only | User's meta-request ignored | Miss user's actual need |
| Yes, all extracted | LOW | Can proceed vs. recheck | Continue | May have missed items |

---

## Q2: Does my item count match the user's?

[VOI: HIGH - numerical verification catches drops]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| My count is lower | HIGH | Find missing vs. proceed | Definitely dropped items | Miss user requests |
| Counts match exactly | LOW | Verified complete vs. recheck | Proceed | May still miss items |
| My count is higher | LOW | Check if valid expansion | I expanded (okay) | Over-counted |
| Can't count user's items | MED | Ask for clarification vs. guess | Vague input | Guess wrong count |

---

## Q3: Did I check EACH item against existing coverage?

[VOI: HIGH - systematic check catches gaps]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Skipped some checks | HIGH | Check skipped items vs. proceed | Incomplete verification | Claim false coverage |
| Batch-checked (not individual) | MED | Individual check vs. proceed | May miss individual gaps | Miss specific gaps |
| Unknown if checked all | MED | Verify each vs. proceed | Uncertain coverage | Proceed with uncertainty |
| Yes, each checked | LOW | Proceed vs. recheck | Systematic | May have skipped some |

---

## Q4: For each item, do I know WHERE it's covered?

[VOI: HIGH - specific location ensures real coverage vs. vague claims]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| No location known | HIGH | Find or create vs. claim | Not actually covered | Claim coverage without it |
| General location only | MED | Get specific vs. vague | Vague coverage | False confidence |
| Yes, specific file + question | LOW | Can reference vs. verify | Verified location | May be wrong location |
| Multiple locations | LOW | Pick primary vs. keep all | Redundant coverage | May be inconsistent |

---

## Q5: Did I identify ALL gaps?

[VOI: HIGH - missing gaps means incomplete work]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Some gaps missed | HIGH | Re-check for gaps vs. proceed | Incomplete | Leave holes |
| All gaps identified | MED | Proceed to fill vs. recheck | Can fill | Miss gaps |
| No gaps found | MED | Verify no gaps vs. accept | Either complete or blind | False completion |
| Unknown if all gaps | MED | Systematic gap check vs. proceed | May miss some | Proceed with holes |

---

## Q6: Did I fill or explain EVERY gap?

[VOI: HIGH - unaddressed gaps = incomplete work]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Some gaps unaddressed | HIGH | Address remaining vs. claim done | Incomplete | Leave holes |
| All gaps filled | MED | Proceed vs. verify | Complete coverage | May have missed fills |
| All gaps explained | MED | Proceed vs. verify | Justified non-coverage | Explanations may be weak |
| Mixed fill and explain | LOW | Proceed vs. separate | Appropriate handling | May have wrong mix |

---

## Q7: Does final count match initial count?

[VOI: HIGH - count mismatch indicates dropped items]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Final count lower | HIGH | Find missing vs. claim done | Items dropped | Claim completion with gaps |
| Didn't track counts | HIGH | Count now vs. proceed blind | No verification | Can't verify |
| Final count higher | MED | Verify valid expansion | Items expanded | Over-counted |
| Counts match | LOW | No items dropped vs. verify | Complete | Items may have merged |

---

## Q8: Did the user repeat any request?

[VOI: HIGH - repetition signals missed items]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| User repeated item | HIGH | Address repeated item vs. ignore | I missed it before | Miss again |
| User asked "did you consider X?" | HIGH | Address X explicitly vs. vague | Probably missed X | Ignore signal |
| Unknown if repeated | MED | Check for patterns vs. proceed | May have missed | Miss repeated requests |
| No repetition | LOW | Probably complete vs. verify | Proceed | May have missed without knowing |

---

## Q9: Did I address any META-requests about the items?

[VOI: HIGH - meta-requests are often the actual need]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Meta-request missed | HIGH | Address meta vs. content only | Ignored user's actual need | User unsatisfied |
| Unknown if meta exists | MED | Check for meta vs. proceed | May have missed | Miss important request |
| No meta-requests | LOW | Content only needed | Only content needed | Miss meta-level |
| Meta-request addressed | LOW | Complete vs. verify | Proceed | May have missed meta |

---

## Q10: Am I CONFIDENT in complete coverage?

[VOI: HIGH - low confidence signals need for verification]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Low confidence | HIGH | Do not declare complete vs. claim | Likely gaps | Claim completion with gaps |
| Medium confidence | MED | Additional check vs. proceed | Some uncertainty | Either over or under confident |
| Can't assess confidence | MED | Systematic verification vs. guess | Unknown state | Random confidence |
| High confidence | LOW | Likely complete vs. verify | Declare complete | Overconfident |

---

## Q11: Would the USER say I covered everything?

[VOI: HIGH - user perception is ground truth for coverage]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| User might disagree | HIGH | Clarify before declaring vs. claim | Misalignment | User sees gaps I don't |
| User would see gaps | HIGH | Fill gaps vs. claim | Definitely incomplete | Claim false completion |
| Unknown user perspective | MED | Ask user vs. assume | Can't verify | Proceed with uncertainty |
| Yes, user would agree | MED | Aligned understanding | Complete | My understanding may differ |

---

## Q12: Have I saved this verification work for future use?

[VOI: MED - affects efficiency but same current outcome]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Not saved | MED | Consider saving vs. discard | Lost work | Redo similar work |
| Yes, saved as procedure/skill | LOW | Reusable vs. one-time | Future value | May not be found |
| Saved as question-guesses | LOW | Queryable vs. lost | Future value | May not be invoked |
| Saving not applicable | LOW | One-time use | Proceed | May have reuse value |

---

## Summary Statistics

- Total questions: 12
- Total entries: 52
- HIGH VOI: 18 (35%)
- MED VOI: 19 (37%)
- LOW VOI: 15 (29%)

---

## Question Order by Action Divergence

**HIGH VOI (Ask First - Catches Critical Gaps)**
1. Q1: All items extracted - addressing right request
2. Q2: Count match - numerical verification
3. Q7: Final count match - items dropped
4. Q8: User repeated - missed signal
5. Q3: Each item checked - systematic coverage
6. Q4: Location known - real vs. vague coverage
7. Q5: All gaps identified - completeness
8. Q6: Gaps addressed - incomplete work
9. Q9: Meta-requests - actual user need
10. Q10: Confidence level - verification trigger
11. Q11: User perception - ground truth

**MED VOI (Ask Second - Refine Approach)**
12. Q12: Saved for reuse - efficiency

---

## Key Insight

**VOI ≠ Coverage Importance**. Coverage is always important. But some checks are HIGH VOI because wrong answers lead to claiming false completion.

**VOI = Action Divergence**. HIGH VOI means: if you answer this wrong, you'll either miss items entirely or falsely claim completeness.

---

## Usage Note

This category should be invoked:
1. After any multi-item user request
2. When user repeats a request (signal of missed item)
3. Before declaring work complete
4. After `/space_discovery` to verify all aspects addressed

→ Pairs with: `/mentioned_coverage_gate` skill (the procedure)
→ Pairs with: `100_coverage_strategy.md` (how to cover)
→ Pairs with: `99_space_size.md` (what needs covering)
