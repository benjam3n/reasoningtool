---
name: "spec - Speculative Analysis"
description: "Rigorous procedure for exploring speculative and 'what if' ideas. Assesses plausibility, prerequisites, implications, and falsifiability."
---

# Speculative Analysis

**Input**: $ARGUMENTS

---

## Step 1: State the Speculation Clearly

Articulate the speculative idea in precise terms.

1. Write it as a single declarative statement
   - Bad: "What if AI gets really smart?"
   - Good: "What if general-purpose AI systems exceed human cognitive ability across all domains by 2035?"
2. Identify the type of speculation:
   - **Technological**: A future capability or invention
   - **Social**: A shift in human behavior or institutions
   - **Scientific**: An undiscovered law or phenomenon
   - **Personal**: A hypothetical life path or decision outcome
   - **Counterfactual**: An alternate history ("what if X had happened instead?")
3. Note the time horizon (if applicable)

```
SPECULATION: [precise statement]
TYPE: [technological / social / scientific / personal / counterfactual]
HORIZON: [timeframe or N/A]
```

---

## Step 2: Identify Prerequisites

List everything that would need to be true for this speculation to hold.

1. **Necessary conditions**: What MUST be true?
2. **Enabling conditions**: What would make it much more likely?
3. **Blocking conditions**: What must NOT be true?

For each prerequisite:
- State it clearly
- Note whether it is currently true, plausible, or implausible
- Note any dependencies between prerequisites (does A require B first?)

```
PREREQUISITES:
1. [prerequisite] — Status: [true / plausible / implausible]
2. [prerequisite] — Status: [true / plausible / implausible]
...
```

---

## Step 3: Assess Plausibility of Each Prerequisite

For each prerequisite from Step 2:

1. What evidence exists for or against it?
2. What is the base rate for similar things being true?
3. Are there known mechanisms that would support it?
4. Are there known barriers that would block it?

Rate each: **HIGH** (>70%), **MODERATE** (30-70%), **LOW** (<30%)

The overall plausibility cannot exceed the weakest necessary condition. If any necessary prerequisite is LOW, the speculation is LOW regardless of other factors.

---

## Step 4: Explore Implications If True

Assuming the speculation IS true, trace consequences:

1. **First-order effects**: What changes immediately and directly?
2. **Second-order effects**: What do those changes cause?
3. **Third-order effects**: What emerges from the second-order changes?
4. **Who benefits?** Who is harmed?
5. **What becomes possible** that wasn't before?
6. **What becomes impossible** or obsolete?

Flag any implications that are themselves speculative vs. near-certain given the premise.

---

## Step 5: Identify How to Test or Falsify

Design ways to check whether the speculation is on track:

1. **Leading indicators**: What early signs would suggest this is becoming true?
2. **Falsification criteria**: What evidence would conclusively disprove it?
3. **Key milestones**: What intermediate events should happen along the way?
4. **Observable predictions**: What specific, checkable predictions does this generate?

```
TESTABLE PREDICTIONS:
- By [date/condition]: [specific observable outcome]
- If FALSE, we would expect: [specific counter-evidence]
```

---

## Step 6: Rate Overall Plausibility

Synthesize into a final assessment:

```
PLAUSIBILITY RATING: [HIGH / MODERATE / LOW / VERY LOW]

REASONING:
- Strongest support: [what makes this most plausible]
- Weakest link: [the prerequisite or assumption most likely to fail]
- Key uncertainty: [what we most need to learn]

VERDICT: [One-sentence summary of whether this speculation deserves
          serious consideration, casual interest, or dismissal]
```

---

## Integration

Use with:
- `/ht` -> Formally test the most critical prerequisite
- `/se` -> Explore the solution space if the speculation is true
- `/rwif` -> Design real-world actions based on the speculation
- `/sp` -> Sharpen the speculative question before analysis
