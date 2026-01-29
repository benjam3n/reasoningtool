# ARAW-Math: Systematic Mathematical Reasoning

**Purpose**: Apply ARAW methodology to mathematical work.

**⚠️ PARADIGM NOTE**: This SKILL file primarily addresses the **verification/proof paradigm** of mathematics (catching errors, proving claims, checking work). Mathematics has other paradigms that may better serve certain goals:

| Paradigm | Values | Use When |
|----------|--------|----------|
| **Verification** (this file) | Proofs, precision, error-catching | Checking work, reviewing papers, formal proofs |
| **Exploration** | Intuition, patterns, conjectures | Mathematical discovery, problem understanding |
| **Insight** | Understanding, elegance, connections | Learning, teaching, research |
| **Approximation** | Useful answers, good enough | Applied math, engineering, estimation |

**Before using this SKILL, ask**: Which paradigm fits your goal?
- If verification/proof → proceed with this SKILL
- If exploration/insight → adapt the process or question whether formal ARAW structure helps
- If approximation → consider whether precision-focused approach fits

---

## STAGE 0: Paradigm Check (DO THIS FIRST)

**Before applying ARAW to math, question whether the verification paradigm is appropriate.**

```
PARADIGM ARAW:
├── ASSUME RIGHT → Verification paradigm is appropriate
│   ├── Goal IS to check correctness
│   ├── Goal IS to find errors
│   ├── Goal IS to prove a claim formally
│   └── → Proceed with SKILL-math as written
│
└── ASSUME WRONG → Verification paradigm may not fit
    ├── Goal might be understanding, not proving
    │   └── Consider: What would help user understand?
    ├── Goal might be exploration, not verification
    │   └── Consider: What questions would explore the space?
    ├── Goal might be intuition, not formalism
    │   └── Consider: What builds intuition about why this is true?
    └── → Adapt process OR acknowledge this SKILL doesn't fit
```

**If paradigm doesn't fit**, either:
1. Acknowledge limitation and suggest what would help
2. Adapt the ARAW questions for user's actual paradigm
3. Use general ARAW instead of SKILL-math

---

## When to Use (Verification Paradigm)

- Developing new proofs (formal)
- Reviewing mathematical papers
- Selecting proof strategies
- Checking your own work for errors
- Validating conjectures against counterexamples

## Depth Guide

| Task | Recommended Depth | Time Investment |
|------|-------------------|-----------------|
| Quick proof check | 1x | 15-20 min |
| Proof development | 2x | 30-60 min |
| Paper review | 3x | 1-2 hours |
| Major theorem | 4x | 2-4 hours |

---

## Process (Verification Paradigm)

### STAGE 1: Problem/Claim Analysis

State the mathematical claim, then explore:

```
CLAIM: "[Mathematical statement to prove]"
│
├── ASSUME RIGHT → Claim is true
│   ├── What does this imply?
│   │   ├── Immediate consequences
│   │   ├── Connections to known results
│   │   └── Generalizations that might also be true
│   ├── What tools likely apply?
│   │   ├── Similar problems that were solved
│   │   ├── Techniques from the area
│   │   └── Structures that match
│   ├── What's the expected form of proof?
│   │   ├── Direct / Contradiction / Induction / Construction
│   │   └── What would each approach need?
│   └── What are the key cases?
│       └── List all cases that must be handled
│
└── ASSUME WRONG → Claim might be false or unprovable
    ├── What would a counterexample look like?
    │   ├── Structure of potential counterexample
    │   ├── Where to look for one
    │   └── Edge cases to test
    ├── What weaker claim might be true?
    │   ├── Additional hypotheses needed?
    │   ├── Restricted domain where it holds?
    │   └── Asymptotic or approximate version?
    ├── Why might proof be hard/impossible?
    │   ├── Known barriers in the area
    │   ├── Independence results
    │   └── Computational complexity issues
    └── What's the dual/contrapositive claim?
        └── Sometimes easier to work with
```

**Output from Stage 1:**
- Confidence in claim's truth
- Candidate proof strategies
- Potential counterexample structures
- Weaker claims to fall back on

---

### STAGE 2: Proof Strategy Selection

For each candidate proof approach:

```
STRATEGY: "[Proof approach - e.g., induction on n]"
│
├── ASSUME RIGHT → This strategy will work
│   ├── What are the key steps?
│   │   └── Outline the proof structure
│   ├── What lemmas are needed?
│   │   └── List dependencies
│   ├── What's the hard part?
│   │   └── Identify where this will be difficult
│   └── What's the base case / starting point?
│
└── ASSUME WRONG → This strategy might fail
    ├── Why might this approach not work?
    │   ├── Known obstructions
    │   ├── Missing pieces
    │   └── Complexity of required lemmas
    ├── What would cause it to fail?
    │   └── Red flags to watch for
    └── What's the alternative?
        └── Other strategies to try if this fails
```

**Selection criteria:**
- Prefer strategies where AW branches are weak
- Have backup strategies ready
- Note warning signs for each approach

---

### STAGE 3: Step-by-Step Verification

For each step in the proof:

```
STEP: "[Proof step - e.g., 'By Lemma 3.2, X implies Y']"
│
├── ASSUME RIGHT → Step is valid
│   ├── What exactly does this establish?
│   │   └── Be precise about what's proven
│   ├── What does it depend on?
│   │   ├── Previous steps
│   │   ├── Hypotheses
│   │   └── External results cited
│   └── Is the citation/reference correct?
│       └── Does the cited result actually say this?
│
└── ASSUME WRONG → Step might be flawed
    ├── What's the weakest part?
    │   └── Where is this most likely to break?
    ├── What counterexample would break this step?
    │   └── Even hypothetical
    ├── What hidden assumptions are being made?
    │   ├── Implicit hypotheses
    │   ├── Unstated conditions
    │   └── "Obviously" statements
    └── Does this step actually follow?
        └── Is there a gap in the logic?
```

**Common issues ARAW catches:**
- "Clearly" / "Obviously" hiding real work
- Unstated assumptions about objects
- Misapplied theorems (wrong hypotheses)
- Missing cases
- Incorrect scope of quantifiers

---

### STAGE 4: Result Validation

After proof is complete:

```
RESULT: "[The proven theorem]"
│
├── ASSUME RIGHT → Proof is complete and correct
│   ├── What exactly was proven?
│   │   └── State precisely - often less than claimed
│   ├── What are the implications?
│   │   └── Consequences of this result
│   ├── What generalizations might work?
│   │   └── Stronger results to try
│   └── Is this the best possible result?
│       └── Or can hypotheses be weakened?
│
└── ASSUME WRONG → Proof might be incomplete
    ├── What cases weren't covered?
    │   └── Go back to case analysis
    ├── What assumptions weren't justified?
    │   └── Check each "let" and "suppose"
    ├── What steps were hand-wavy?
    │   └── "It can be shown that..."
    └── What's the scope actually proven?
        └── For all X, or for some X?
```

---

## Error Taxonomy: What ARAW Catches

| Error Type | ARAW Detection Method |
|------------|----------------------|
| Hidden assumptions | Claim identification surfaces all dependencies |
| Missing cases | AW asks "what cases exist?" |
| Proof gaps | AW on each step asks "does this follow?" |
| Wrong generalization | AW tests scope: "for ALL X?" |
| Misapplied theorems | AW asks "does cited result actually say this?" |
| Circular reasoning | Dependency tracking reveals cycles |
| Quantifier errors | Precise claim statement catches ∀/∃ swaps |
| Off-by-one errors | AW on base cases and boundaries |

---

## Quick Reference: ARAW Questions for Math

**For conjectures:**
- What would a counterexample look like?
- What weaker version is definitely true?
- What's blocking the proof?

**For proof strategies:**
- What's the hard part of this approach?
- What would make this fail?
- What's the backup plan?

**For proof steps:**
- Does this actually follow from the previous?
- What's hidden in "clearly" or "obviously"?
- What cases does this cover?

**For completed proofs:**
- What exactly was proven (precisely)?
- What cases might have been missed?
- Is the scope claim accurate?

---

## Example A: Verification Paradigm (Error-Catching)

**Claim**: "Every continuous function on [0,1] attains its maximum"

```
ASSUME RIGHT → Claim is true
├── This is the Extreme Value Theorem
├── Standard proof uses compactness of [0,1]
├── Key steps: continuous image of compact is compact,
│   compact subset of ℝ has max
└── Well-known result

ASSUME WRONG → Let's check anyway
├── What if [0,1] weren't compact?
│   └── Open interval (0,1): f(x) = x has no max
│   └── Hypothesis is necessary
├── What if f weren't continuous?
│   └── f(x) = x for x < 1, f(1) = 0: no max at value 1
│   └── Hypothesis is necessary
├── What's actually needed?
│   └── Compact domain + continuous function
│   └── Works for any compact metric space
└── Common errors in proofs:
    ├── Assuming max exists, then finding it (circular)
    ├── Only showing sup exists, not that it's attained
    └── Missing: continuous image of compact is closed and bounded
```

**Value in verification paradigm**: Clarifies what's essential and what errors to avoid.

---

## Example B: Insight Paradigm (Understanding)

**Same claim, different paradigm**: "Every continuous function on [0,1] attains its maximum"

```
ASSUME RIGHT → This captures something real
├── What is this really about?
│   ├── Continuous = no jumps → can't "sneak past" a value
│   ├── Bounded interval = nowhere to escape to
│   └── Together: function is "trapped" and must hit its highest value
├── What does this connect to?
│   ├── Intermediate Value Theorem (same "trapped" intuition)
│   ├── Compactness (the formal capture of "can't escape")
│   └── Optimization (why calculus works on closed intervals)
└── What's the PICTURE?
    └── Draw continuous curve on closed box → must have high point

ASSUME WRONG → This intuition might be misleading
├── When does "trapped" intuition fail?
│   ├── Infinite dimensions (function spaces)
│   ├── Non-Hausdorff spaces (weird topology)
│   └── When "continuous" means something different
└── What's the deeper principle?
    └── Compactness + Hausdorff → "finite-like" behavior
```

**Value in insight paradigm**: Understanding WHY it's true, not just that it is.

**Notice**: Different paradigm → different ARAW questions → different insights. The verification example catches errors; the insight example builds understanding. Neither is wrong; they serve different goals.

---

## Integration with Main ARAW

ARAW-Math is a specialization of the main ARAW skill. Key differences:

| Aspect | Main ARAW | ARAW-Math |
|--------|-----------|-----------|
| Focus | General claims | Mathematical claims |
| AR use | What follows | Proof strategy |
| AW use | Alternatives | Counterexamples, gaps |
| Commitment | Confidence levels | Proven vs conjectured |
| Output | Analysis | Proof or error report |

You can invoke as: `/araw-math [theorem or proof]`

Or use main ARAW with math focus: `/araw 2x [claim] --focus=math`

---

## Checklist Before Finishing

- [ ] Claim precisely stated
- [ ] Proof strategy selected via AR/AW comparison
- [ ] Each step checked with ASSUME WRONG
- [ ] All cases identified and covered
- [ ] Hidden assumptions made explicit
- [ ] Scope of result correctly stated
- [ ] Citations verified (if applicable)
- [ ] Counterexample search done even if proof seems complete
