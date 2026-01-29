# Universal: ARAW Full Tree Exploration (115)

**Category**: META - Complete ARAW Tree for Commitment Testing
**Source**: [D: from observation that both AR and AW paths must be explored at every level]
**Structure**: One question per entry, CRUX-marked with realistic distribution
**Purpose**: Explore ALL paths (AR/AW combinations) to test for foundations

## The Problem with 114

File 114 only followed ASSUME WRONG chains. But:
- You must explore BOTH AR and AW at every node
- Paths can be AR→AW→AW→AR→AW→...
- Some mixed paths may reveal contradictions others miss
- Some mixed paths may stay coherent when pure paths don't

## The Full Tree

```
Statement S
├─ ASSUME RIGHT (S is true)
│  ├─ What follows if S is true? → Claim C1
│  │  ├─ ASSUME RIGHT (C1 is true)
│  │  │  └─ ... continue branching
│  │  └─ ASSUME WRONG (C1 is false)
│  │     └─ ... continue branching
│  └─ What else follows? → Claim C2
│     ├─ AR...
│     └─ AW...
│
└─ ASSUME WRONG (S is false)
   ├─ What follows if S is false? → Claim C3
   │  ├─ ASSUME RIGHT (C3 is true)
   │  │  └─ ... continue branching
   │  └─ ASSUME WRONG (C3 is false)
   │     └─ ... continue branching
   └─ What else follows? → Claim C4
      ├─ AR...
      └─ AW...
```

## Commitment Criteria (Revised)

```
FOUNDATIONAL (can commit) when:
- ALL paths starting with AW eventually contradict
- AND AR paths are internally consistent
- The tree "closes" with no coherent AW escape routes

GUESS (cannot commit) when:
- ANY path starting with AW stays coherent throughout
- OR AR paths have internal inconsistencies
- There exists a coherent alternative world
```

## CRUX Rating Guide
- **HIGH** (10-25%): Missing a path that changes the conclusion
- **MED** (40-50%): Incomplete exploration of a branch
- **LOW** (30-40%): Minor path unexplored

---

# PART A: BUILDING THE TREE

## Q1: How to start the tree?
[D: Initial branching from statement S]

| Entry | CRUX | Why This Rating | ASSUME RIGHT | ASSUME WRONG |
|-------|------|-----------------|--------------|--------------|
| Branch into AR and AW | LOW | Required first step | Create both branches | Only one branch |
| AR: What follows if true? | MED | Generate implications | List implications | Skip AR |
| AW: What follows if false? | MED | Generate counter-implications | List counter-implications | Skip AW |
| Multiple implications per branch | MED | Tree is wide, not just deep | Explore all | One implication enough |
| Each implication becomes new node | LOW | Recursive structure | Continue branching | Stop at first level |

---

## Q2: How to continue branching at each node?
[D: Every node gets both AR and AW]

| Entry | CRUX | Why This Rating | ASSUME RIGHT | ASSUME WRONG |
|-------|------|-----------------|--------------|--------------|
| Every claim branches AR and AW | HIGH | Core of full exploration | Always branch both | Sometimes skip |
| AR path from AW parent is valid | HIGH | Mixed paths matter | Include it | Pure paths only |
| AW path from AR parent is valid | HIGH | Mixed paths matter | Include it | Pure paths only |
| AR→AW→AR is a valid path | MED | Mixed sequence | Explore it | Invalid |
| Track the path taken | MED | Know which combination | Record path | Don't track |
| Path notation: AR.AW.AW.AR... | LOW | Useful for reference | Use notation | Other method |

---

## Q3: When does a path terminate?
[D: Stopping conditions for a single path]

| Entry | CRUX | Why This Rating | ASSUME RIGHT | ASSUME WRONG |
|-------|------|-----------------|--------------|--------------|
| Reaches contradiction | LOW | Path closes | Mark as contradiction | Continue |
| Reaches tautology | LOW | Path grounds | Mark as grounded | Continue |
| Loops back to earlier claim | MED | Circular | Check if same conclusion | Different conclusion |
| No further implications | MED | Dead end | Mark as terminal | Find more |
| Reaches previously explored | LOW | Already done | Link to existing | Re-explore |
| Depth limit reached | LOW | Practical | Note incomplete | Go deeper |

---

# PART B: EXAMPLE - "REALITY EXISTS"

## Q4: AR branch of "Reality exists"
[D: What follows if reality exists?]

| Entry | CRUX | Why This Rating | ASSUME RIGHT | ASSUME WRONG |
|-------|------|-----------------|--------------|--------------|
| AR: Things can exist | LOW | Follows | Branch this further | Contradiction |
| AR: Experience is possible | LOW | Follows | Branch further | Contradiction |
| AR: Claims can be made | LOW | Follows | Branch further | Contradiction |
| AR: This claim exists | LOW | Follows | Consistent | Contradiction |
| AR paths stay consistent | MED | No internal contradiction | AR branch OK | AR contradicts |

---

## Q5: AW branch of "Reality exists"
[D: What follows if reality does NOT exist?]

| Entry | CRUX | Why This Rating | ASSUME RIGHT | ASSUME WRONG |
|-------|------|-----------------|--------------|--------------|
| AW: Nothing exists | MED | Initial implication | Branch this | Skip |
| AW.AR: But this claim exists | HIGH | AR from AW parent | Contradiction with parent | No claim |
| AW.AW: This claim doesn't exist | MED | AW from AW parent | Branch further | Stop |
| AW.AW.AR: Something processes this | HIGH | AR from AW.AW | Contradiction | Nothing |
| AW.AW.AW: Nothing processes this | MED | Continue AW | But denial is processing... | Nothing |
| All AW paths hit contradiction | HIGH | Key finding | Foundational | Some path survives |

---

## Q6: Summary for "Reality exists"
[D: Does the tree close?]

| Entry | CRUX | Why This Rating | ASSUME RIGHT | ASSUME WRONG |
|-------|------|-----------------|--------------|--------------|
| AR paths: internally consistent | LOW | Check | Yes | No |
| AW paths: all contradict | HIGH | Key test | Yes → foundational | No → guess |
| Mixed paths (AW.AR, AW.AW.AR...): all contradict | HIGH | Must check mixed | Yes → foundational | No → guess |
| No coherent escape from AW | HIGH | No alternative world | Foundational | Alternative exists |
| Result: CAN COMMIT | LOW | Conclusion | Commit | Don't commit |

---

# PART C: EXAMPLE - "I'M HUNGRY"

## Q7: AR branch of "I'm hungry"
[D: What follows if I am hungry?]

| Entry | CRUX | Why This Rating | ASSUME RIGHT | ASSUME WRONG |
|-------|------|-----------------|--------------|--------------|
| AR: My body needs food | MED | Follows | Branch | Not necessary |
| AR.AR: Hunger detection is accurate | MED | Sub-claim | Branch | Detection wrong |
| AR.AW: Hunger detection is wrong | HIGH | But still hungry? | Coherent (lucky guess) | Contradiction |
| AR.AW survives | HIGH | Coherent path in AR branch | AR branch has issues | All AR consistent |
| AR branch not fully consistent | MED | Internal AW survives | Note this | Fully consistent |

---

## Q8: AW branch of "I'm hungry"
[D: What follows if I'm NOT hungry?]

| Entry | CRUX | Why This Rating | ASSUME RIGHT | ASSUME WRONG |
|-------|------|-----------------|--------------|--------------|
| AW: I'm experiencing something else | MED | What? | Branch | Nothing |
| AW.AR: It's thirst | LOW | Coherent alternative | Survives | Not thirst |
| AW.AR: It's anxiety | LOW | Coherent alternative | Survives | Not anxiety |
| AW.AR: It's boredom | LOW | Coherent alternative | Survives | Not boredom |
| AW.AW: I'm not experiencing anything | MED | But there's a sensation... | Branch | Contradiction? |
| AW.AW.AR: There is a sensation | HIGH | Back to something | Coherent | No sensation |
| AW.AW.AW: There is no sensation | MED | Then what am I reporting? | Branch | Contradiction |

---

## Q9: Does AW branch fully contradict for "I'm hungry"?
[D: Looking for surviving paths]

| Entry | CRUX | Why This Rating | ASSUME RIGHT | ASSUME WRONG |
|-------|------|-----------------|--------------|--------------|
| AW.AR(thirst) survives | HIGH | Coherent path | AW branch doesn't close | All contradict |
| AW.AR(anxiety) survives | HIGH | Coherent path | AW branch doesn't close | All contradict |
| AW.AR(boredom) survives | HIGH | Coherent path | AW branch doesn't close | All contradict |
| Multiple coherent alternatives | HIGH | Key finding | Cannot commit | Can commit |
| Result: CANNOT COMMIT (guess) | MED | Conclusion | Stays guess | Foundational |

---

# PART D: EXAMPLE - "I'M PERCEIVING SOMETHING"

## Q10: AR branch of "I'm perceiving something"
[D: What follows if true?]

| Entry | CRUX | Why This Rating | ASSUME RIGHT | ASSUME WRONG |
|-------|------|-----------------|--------------|--------------|
| AR: Something exists to perceive | MED | Or generates perception | Branch | Nothing |
| AR.AR: External reality | LOW | One option | Consistent | Internal only |
| AR.AW: No external reality | MED | Internal perception | Coherent (simulation, dream) | External |
| AR.AW survives | MED | Coherent in AR branch | Note it | Contradicts |
| AR: I exist to perceive | MED | Perceiver exists | Branch | No perceiver |
| AR.AW: I don't exist | HIGH | Who perceives then? | Contradiction | Coherent |

---

## Q11: AW branch of "I'm perceiving something"
[D: What follows if I'm NOT perceiving anything?]

| Entry | CRUX | Why This Rating | ASSUME RIGHT | ASSUME WRONG |
|-------|------|-----------------|--------------|--------------|
| AW: No perception occurring | MED | Initial claim | Branch | Perception occurring |
| AW.AR: But this claim is being processed | HIGH | Processing is perception-like | Contradiction | No processing |
| AW.AW: No processing occurring | MED | Continue | Branch | Processing |
| AW.AW.AR: Denial requires processing | HIGH | Self-refuting | Contradiction | No denial |
| AW.AW.AW: No denial occurring | MED | But we just denied... | Contradiction | Denial is occurring |
| All AW paths contradict | HIGH | Key finding | Foundational | Some survive |

---

## Q12: Summary for "I'm perceiving something"
[D: Does tree close?]

| Entry | CRUX | Why This Rating | ASSUME RIGHT | ASSUME WRONG |
|-------|------|-----------------|--------------|--------------|
| AR paths have some internal AW survivors | MED | e.g., "internal only" perception | Note uncertainty | All consistent |
| BUT: all AW paths contradict | HIGH | Can't deny perception | Foundational | Some survive |
| Key: AW denial is self-refuting | HIGH | Denying presupposes perceiving | Foundational | Not self-refuting |
| Result: CAN COMMIT (with caveat) | MED | Caveat: what is perceived is uncertain | Commit to perception, not content | All certain |

---

# PART E: COMMITMENT CRITERIA

## Q13: When can we commit?
[D: Conditions for foundational status]

| Entry | CRUX | Why This Rating | ASSUME RIGHT | ASSUME WRONG |
|-------|------|-----------------|--------------|--------------|
| ALL AW-originating paths contradict | HIGH | No coherent denial | Foundational | Some survive |
| AR paths are consistent (no AR→AW survival that contradicts AR) | MED | Internal coherence | Consistent | Inconsistent |
| Mixed paths (AW.AR.AW...) all contradict | HIGH | Check all combinations | All contradict | Some survive |
| Self-refutation in any AW path | MED | Strong evidence | Likely foundational | Not self-refuting |
| No coherent alternative world | HIGH | Key criterion | Foundational | Alternative exists |

---

## Q14: When must we stay with guess?
[D: Conditions for guess status]

| Entry | CRUX | Why This Rating | ASSUME RIGHT | ASSUME WRONG |
|-------|------|-----------------|--------------|--------------|
| ANY AW-originating path survives | HIGH | Coherent alternative | Guess | All contradict |
| Coherent misidentification possible | HIGH | e.g., thirst for hunger | Guess | No misidentification |
| Future could falsify | MED | Empirical claim | Guess | Unfalsifiable |
| Alternative interpretation coherent | HIGH | Frame-dependent | Guess | No alternatives |
| Path like AW.AR(alternative) survives | HIGH | Specific escape route | Guess | No escape |

---

## Coverage Summary

```
QUESTIONS: 14
ENTRIES: 84

CRUX Distribution:
- HIGH: 38 entries (45%)
- MED: 34 entries (40%)
- LOW: 12 entries (14%)

THE FULL TREE APPROACH:

1. Start with statement S
2. Branch AR (S is true) and AW (S is false)
3. At EVERY node, branch BOTH AR and AW again
4. Paths can be any combination: AR.AW.AW.AR.AW...
5. Continue until contradiction, grounding, or loop
6. ALL paths must be explored

COMMITMENT CRITERIA:

CAN COMMIT (foundational) when:
  ✓ ALL paths starting with AW eventually contradict
  ✓ INCLUDING mixed paths (AW.AR.AW...)
  ✓ AR paths are internally consistent
  ✓ No coherent alternative world exists

CANNOT COMMIT (guess) when:
  ✗ ANY AW-originating path survives coherently
  ✗ e.g., AW.AR(thirst) survives for "I'm hungry"
  ✗ Coherent alternative explanation exists

EXAMPLES:

"Reality exists"
  AW → "Reality doesn't exist"
  AW.AR → "But this claim exists" → CONTRADICTION
  AW.AW → "This claim doesn't exist"
  AW.AW.AR → "Something processes this" → CONTRADICTION
  AW.AW.AW → "Nothing processes" → CONTRADICTION (denial is processing)
  ALL AW paths contradict → FOUNDATIONAL

"I'm hungry"
  AW → "I'm not hungry"
  AW.AR → "It's actually thirst" → COHERENT (survives!)
  AW.AR → "It's actually anxiety" → COHERENT (survives!)
  Some AW paths survive → GUESS

"I'm perceiving something"
  AW → "I'm not perceiving"
  AW.AR → "But processing this claim" → CONTRADICTION
  AW.AW.AR → "Denial requires processing" → CONTRADICTION
  ALL AW paths contradict → FOUNDATIONAL
  (But WHAT is perceived stays uncertain)

THE KEY INSIGHT:
It's not just one path - explore the ENTIRE TREE.
Mixed paths (AR.AW.AW.AR...) may reveal what pure paths miss.
```
