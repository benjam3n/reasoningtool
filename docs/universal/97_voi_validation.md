# Universal: VOI Validation (97)

**Category**: META - VOI Rating System Validation
**Purpose**: Questions about whether VOI ratings are accurate and how to validate them
**Structure**: Questions ordered by Value of Information (action divergence)
**Note**: This file addresses validation of the VOI rating system itself

---

## VOI Rating = Action Divergence

- **HIGH**: Different answers → completely different action paths
- **MED**: Different answers → same general direction, different approach
- **LOW**: Different answers → same actions, different framing/flavor

---

## Q1: Do HIGH VOI entries actually show action divergence?

[VOI: HIGH - if HIGH entries don't diverge, the rating system is broken]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| HIGHs don't actually diverge | HIGH | Rating system broken | Re-rate everything | Ratings are correct |
| Unknown divergence | HIGH | Can't assess quality | Test divergence | Divergence known |
| HIGHs diverge >80% | LOW | System working | Trust ratings | Some don't diverge |

---

## Q2: What's the cost of a FALSE HIGH rating?

[VOI: HIGH - false HIGHs waste user time on questions that don't matter]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| User ignores real HIGHs (boy-cried-wolf) | HIGH | System trust broken | Fix false HIGHs | Rare occurrence |
| User over-prioritizes minor issue | MED | Effort misdirection | Some misdirection acceptable | Significant misdirection |
| User asks unnecessary questions | LOW | Time waste only | Accept minor inefficiency | More serious cost |

---

## Q3: What's the cost of a FALSE LOW rating (should be HIGH)?

[VOI: HIGH - false LOWs mean user skips critical routing questions]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| User skips critical routing question | HIGH | Sent down wrong path | Fix false LOWs | Skip is recoverable |
| User proceeds with wrong assumption | HIGH | Wasted effort on wrong path | Catch early | Effort is small |
| User deprioritizes important issue | MED | Delayed attention | Some delay acceptable | Critical delay |

---

## Q4: Are VOI ratings based on actual action divergence?

[VOI: HIGH - ratings should reflect real routing power]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Based on intuition, not testing | HIGH | May not reflect reality | Test divergence empirically | Intuition is accurate |
| Based on tested divergence | LOW | Validated | Trust ratings | Actually intuition-based |
| Unknown basis | MED | Can't assess | Investigate basis | Basis known |

---

## Q5: How to validate a HIGH VOI rating?

[VOI: MED - affects validation approach but similar process]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Ask "what would you do if X vs Y?" | MED | Direct test | Implement test | Different validation |
| Track actual user routing | HIGH | Real-world but slow | Build tracking | Faster proxy ok |
| Expert review | LOW | Subjective but quick | Get review | User data needed |

---

## Q6: Does the VOI distribution look right?

[VOI: MED - affects calibration but similar process]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Too many HIGHs (>30%) | MED | Not enough differentiation | Downgrade some | Distribution correct |
| Too few HIGHs (<15%) | MED | Missing critical routers | Upgrade some | Distribution correct |
| 20-25% HIGH | LOW | Good distribution | Proceed | Actually off |

---

## Q7: Are questions ordered correctly by VOI?

[VOI: MED - affects efficiency but still gets to answer]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Wrong order (LOWs before HIGHs) | MED | Inefficient routing | Reorder | Order correct |
| Correct order (HIGHs first) | LOW | Efficient routing | Proceed | Actually wrong order |
| Unknown if correct | MED | May be inefficient | Order review | Order known |

---

## Q8: How often should VOI ratings be re-validated?

[VOI: LOW - maintenance detail]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Annually | LOW | Reasonable | Annual review | More/less frequent |
| After significant usage | LOW | Usage reveals errors | Review after N uses | Time-based better |
| Continuously | LOW | Ideal but expensive | Build tracking | Periodic sufficient |

---

## Summary Statistics

- Total questions: 8
- Total entries: 30
- HIGH VOI: 8 (27%)
- MED VOI: 12 (40%)
- LOW VOI: 10 (33%)

---

## Question Order by Action Divergence

**Ask first (HIGH VOI):**
1. Q1: Do HIGHs actually diverge? - system validity
2. Q2: Cost of false HIGH? - trust erosion
3. Q3: Cost of false LOW? - wrong routing
4. Q4: Based on real divergence? - foundation

**Ask if relevant (MED VOI):**
5. Q5: How to validate? - method
6. Q6: Distribution right? - calibration
7. Q7: Order correct? - efficiency

**Low priority (LOW VOI):**
8. Q8: Re-validation frequency? - maintenance

---

## Key Insight

**VOI validation = checking action divergence.**

The core test: For each HIGH VOI entry, ask "If answer is X, what would you do? If answer is Y, what would you do?"

If the actions are the same → FALSE HIGH, downgrade to MED or LOW.
If the actions are completely different → TRUE HIGH, keep rating.

---

## Validation Procedure

```
For each HIGH-VOI entry:
1. Present scenario to user
2. Ask: "If [Entry A], what would you do?"
3. Ask: "If [Entry B], what would you do?"
4. Score: Same strategy = FALSE HIGH, Different = TRUE HIGH
5. Target: >80% TRUE HIGH rate
6. Re-rate any FALSE HIGHs to MED or LOW
```

---

## Phone Tree Analogy

VOI ratings are like the phone tree routing:
- HIGH VOI = "Press 1 for Billing, Press 2 for Technical Support" - completely different departments
- MED VOI = "Press 1 for Home Internet, Press 2 for Business Internet" - same department, different team
- LOW VOI = "Did you want to hear this in English or Spanish?" - same service, different delivery

If a "HIGH VOI" question doesn't route to different departments, it's mislabeled.
