# Universal: Improvement Cycle (108)

**Status**: SUPERSEDED by 110_commitment_tree.md

**Problems with this approach:**
1. "GROUND" is vague - what does that mean operationally?
2. The "why continue?" gate (UPSTREAM? DIFFERENT? ANSWERABLE? MATTERS?) is too complex
3. This cycle questions forever but never COMMITS to anything
4. No tree structure to build on committed assumptions

**Use 110_commitment_tree.md instead**, which has:
- GIVEN (clearer than GROUND)
- OPEN/CLOSED classification
- CRUX check (simpler than 4-part gate)
- COMMIT → DERIVE → CHECK cycle
- Tree navigation for specific answers

---

**Category**: META - When and How to Improve
**Source**: [D: from question_about_guesses "why continue?" gate + bounded_inquiry termination]
**Structure**: One question per entry, VOI-marked with realistic distribution
**Purpose**: Questions for the question-guess-question improvement cycle (OLD APPROACH)

## Core Cycle (OLD - see 110 for new)

```
1. GROUND: What can be observed without guessing?
2. GUESS: What follows from observations? (generate or select)
3. QUESTION: Apply "why continue?" to question guesses
4. Answer → becomes NEW GUESS → repeat from step 3
5. STOP when criteria hit
```

## VOI Rating = Action Divergence

- **HIGH**: Different answers → completely different action paths
- **MED**: Different answers → same general direction, different approach
- **LOW**: Different answers → same actions, different framing/flavor

---

# PART A: GROUNDING (What can be observed?)

## Q1: What observable facts exist before guessing?

[VOI: HIGH - determines whether to ground in evidence vs. pure guessing]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Nothing observable | HIGH | Start with guesses vs. ground first | Must guess everything = risky | Something is observable |
| User stated preferences | MED | Honor preferences vs. explore | Direct input | Preferences unknown |
| Patterns are visible in data | MED | Follow patterns vs. ignore | Pattern recognition | Patterns are illusory |
| Specific feedback exists | LOW | Use feedback vs. generate | Direct evidence | No feedback, must generate |
| Metrics are available | LOW | Use metrics vs. qualitative | Quantitative ground | Qualitative only |
| Previous decisions documented | LOW | Learn from history vs. fresh | Historical record | No history |
| Comparison available | LOW | Compare against benchmark | Benchmark exists | No benchmark |

---

## Q2: What type of observation is this?

[VOI: HIGH - determines evidence weight and treatment]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Assumption (no evidence) | HIGH | Label as guess, question it vs. trust | Not grounded = it's a guess | It's actually grounded |
| Reported by user | MED | Trust with verification vs. accept | Secondhand but reliable | User misreported |
| Derived from data [D] | MED | Check derivation vs. accept | Calculation from known | Derivation error |
| Inferred (soft evidence) | MED | Treat as guess vs. trust | Uncertain ground | It's actually solid |
| Direct observation [O] | LOW | Trust it vs. question | Strongest evidence | Observation was wrong |
| Tested and confirmed [T] | LOW | High confidence vs. retest | Empirically validated | Test was flawed |

---

# PART B: GUESSING (What follows from observations?)

## Q3: Does a guess already exist for this situation?

[VOI: MED - affects efficiency but same outcome]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Category exists, not entry | MED | Add new entry vs. recategorize | Library has gap | Category wrong |
| No relevant library | MED | Generate fresh vs. search harder | New territory | Library exists, didn't find |
| Unknown if exists | MED | Search first vs. generate | Search before generate | Just generate |
| Exact match in library | LOW | Select it vs. generate new | Reuse existing | Need to generate |
| Similar guess exists | LOW | Adapt existing vs. fresh | Modify to fit | Generate from scratch |
| Multiple candidates | LOW | Evaluate options vs. pick first | Selection problem | Wrong options |

---

## Q4: What type of guess is being made?

[VOI: HIGH - determines validation approach]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Normative (what should be) | HIGH | Surface values vs. verify facts | Values involved = clarify values | It's actually factual |
| Intentional (what they meant) | HIGH | Verify directly vs. accept | Mind-reading = dangerous | Projecting |
| Causal (what causes) | MED | Test mechanism vs. accept | Needs mechanism | Correlation not causation |
| Predictive (what will happen) | MED | Test prediction vs. accept | Needs validation | Prediction fails |
| Modal (what's possible) | MED | Test boundaries vs. accept | Boundary claim | Boundaries wrong |
| Factual (what is) | LOW | Verifiable vs. debate | Check facts | It's actually normative |
| Relational (compared to what) | LOW | Reference point vs. absolute | Clarify reference | Wrong reference |

---

# PART C: QUESTIONING (Why continue?)

## Q5: Is this question UPSTREAM?

[VOI: HIGH - determines whether question leads to root cause vs. tangent]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| No, sideways (related but not causal) | HIGH | Stop this branch vs. pursue | Wrong direction = wasted effort | Actually upstream |
| No, downstream (toward effects) | MED | Reverse direction vs. continue | Wrong direction | Actually upstream |
| Unclear direction | MED | Assess before proceeding vs. proceed | Need to assess | Clear if you look |
| Already at root | MED | Consider stopping vs. go deeper | Termination candidate | Deeper cause exists |
| Yes, toward root causes | LOW | Proceed vs. reconsider | Right direction | Missing the cause |

---

## Q6: Is this question DIFFERENT from previous?

[VOI: HIGH - determines whether pursuing adds value vs. wastes time]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| No, semantically same | HIGH | Stop this branch vs. pursue | Repetitive = stop | Actually different |
| Rephrase of earlier | HIGH | Stop vs. pursue | Loop = stop | Actually new angle |
| Partially overlaps | MED | Decide if worth pursuing vs. pursue | Consider stopping | Worth pursuing |
| Yes, new territory | LOW | Proceed vs. reconsider | Continue questioning | It's actually repetitive |
| Deeper version of same | LOW | Continue drilling vs. stop | Drilling down is OK | Going in circles |

---

## Q7: Is this question ANSWERABLE?

[VOI: HIGH - determines whether to pursue vs. mark as unknown]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| No, unknowable | HIGH | Mark as UNKNOWN, stop vs. pursue | Stop = can't proceed | Actually answerable |
| Yes, but need to gather evidence | MED | Effort required vs. proceed | Decide if worth it | Evidence unavailable |
| No, purely definitional | MED | Accept definition, stop vs. debate | Mark as GROUND | Actually empirical |
| Unknown if answerable | MED | Assess first vs. proceed | Meta-question | Clear if you check |
| Yes, with available evidence | LOW | Proceed to answer vs. defer | Answer it | Evidence doesn't exist |
| Partially (some aspects) | LOW | Answer what's possible vs. skip | Partial answer | Nothing answerable |

---

## Q8: Does the answer MATTER?

[VOI: HIGH - determines whether question is worth asking]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| No, wouldn't inform action | HIGH | Skip vs. pursue | Low value = skip | Actually high value |
| Curiosity only | MED | Skip unless nothing better vs. pursue | Not problem-driven | Problem-relevant |
| Unknown impact | MED | Estimate impact first vs. proceed | Assess impact | Impact is clear |
| Yes, would change strategy | LOW | High leverage, prioritize | High leverage | Wouldn't actually change much |
| Yes, would change approach | LOW | Medium leverage, pursue | Medium leverage | Lower leverage than thought |
| Marginally (would adjust details) | LOW | Deprioritize vs. pursue | Low leverage | Higher leverage than thought |

---

# PART D: STOPPING (When to terminate)

## Q9: Should we stop questioning this branch?

[VOI: HIGH - determines whether to continue or terminate]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, hit UNANSWERABLE | HIGH | Mark and stop vs. pursue | Can't proceed further | Actually answerable |
| Yes, hit REPETITIVE | MED | Stop branch vs. pursue | Same question loop | Actually new |
| Yes, hit SIDEWAYS | MED | Stop and return vs. pursue | Off-track | Actually relevant |
| Yes, stakes require decision | MED | Decide now vs. continue | Practical closure | More time available |
| No, more upstream to explore | LOW | Keep going vs. stop | Continue | Should have stopped |
| Yes, hit LOW-VALUE | LOW | Deprioritize vs. pursue | Not worth effort | Higher value than thought |
| Yes, goal achieved | LOW | Success, accept vs. continue | Accept answer | More to find |
| Unclear | MED | Apply criteria vs. proceed | Assess | Clear if checked |

---

## Q10: What is the termination state?

[VOI: MED - affects closure type but same decision to stop]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Goal unachievable in scope (bounded failure) | MED | Accept limitation vs. expand | Scoped closure | Actually achievable |
| Stakes require decision now | MED | Decide with available vs. wait | Practical closure | Could wait |
| No termination criteria met | MED | Continue vs. force stop | Keep going | Should have stopped |
| Goal achieved (success) | LOW | Accept result vs. continue | Complete | Goal not actually achieved |
| Remaining questions out of scope | LOW | Defer out-of-scope vs. expand | Scoped completion | In-scope questions remain |
| Multiple criteria met | LOW | Strong stop vs. continue | Overdetermined | Premature stop |

---

## Q11: What happens with the answer/guess?

[VOI: MED - affects disposition but same answer found]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Becomes action | MED | Execute action vs. defer | Implementation | Wrong action |
| Becomes ground (accepted as true) | MED | Build on it vs. question | Foundation | Shouldn't be ground |
| Becomes new guess | LOW | Question the answer vs. accept | Continues cycle | Should be action |
| Marked as unknown | LOW | Accept uncertainty vs. pursue | Acknowledged gap | Actually answerable |
| Deferred for later | LOW | Record for future vs. address | Out of current scope | Should address now |
| Discarded (low value) | LOW | Discard vs. keep | Not worth keeping | Higher value than thought |

---

# PART E: CONVERGENT VALIDATION

## Q12: Do multiple independent criteria agree?

[VOI: HIGH - determines whether to accept or investigate divergence]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Criteria diverge | HIGH | Investigate divergence vs. pick one | Uncertainty = investigate | Pick one and proceed |
| No criteria applied | HIGH | Apply criteria vs. proceed | Unvalidated = risky | No validation needed |
| Only one criterion checked | MED | Add criteria vs. accept | Weak validation | One is enough |
| Criteria themselves are uncertain | MED | Address meta-level first vs. proceed | Meta-uncertainty | Criteria are solid |
| All criteria converge | LOW | Accept vs. question | Strong validation | Criteria wrong |
| Most criteria converge | LOW | Accept with notes vs. investigate | Good validation | Dissenting criterion important |

---

## Coverage Summary

```
QUESTIONS: 12
ENTRIES: 72

VOI Distribution:
- HIGH: 17 entries (24%)
- MED: 30 entries (42%)
- LOW: 25 entries (35%)

HIGH-VOI Entries (check first):
- Q1: Nothing observable - must guess everything
- Q2: Assumption with no evidence - it's a guess
- Q4: Normative or Intentional - values or mind-reading
- Q5: No, sideways - wrong direction
- Q6: No, repetitive - loop detected
- Q7: No, unknowable - can't proceed
- Q8: No, wouldn't inform action - skip
- Q12: Criteria diverge - investigate

THE CYCLE:
1. GROUND with Q1-Q2 (what's observable?)
2. GUESS with Q3-Q4 (select or generate)
3. QUESTION with Q5-Q8 (why continue?)
4. STOP with Q9-Q10 (when to terminate)
5. DISPOSE with Q11 (what happens with answer)
6. VALIDATE with Q12 (convergent check)

STOP SIGNALS:
- Q5: Not upstream
- Q6: Repetitive
- Q7: Unanswerable
- Q8: Low value
- Q9: Any termination criterion
- Q10: Goal achieved OR bounded failure OR stakes OR scope
```

---

## Question Order by Action Divergence

**HIGH VOI (Ask First - Changes Approach Entirely)**
1. Q1: Observable facts - ground vs. guess
2. Q2: Observation type - evidence weight
3. Q4: Guess type - validation approach
4. Q5: Upstream - root cause vs. tangent
5. Q6: Different - new value vs. loop
6. Q7: Answerable - pursue vs. stop
7. Q8: Matters - worth asking vs. skip
8. Q9: Should stop - terminate vs. continue
9. Q12: Criteria agree - accept vs. investigate

**MED VOI (Ask Second - Refine Approach)**
10. Q3: Guess exists - efficiency
11. Q10: Termination state - closure type
12. Q11: Answer disposition - next action

---

## Key Insight

**VOI ≠ Question Importance**. A question can be important but LOW VOI if the answer doesn't change what you do next.

**VOI = Action Divergence**. HIGH VOI means: if you answer this wrong, you'll waste effort on dead-end branches or miss critical grounding.
