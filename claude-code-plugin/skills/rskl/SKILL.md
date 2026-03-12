---
name: "rskl - Reasoning Skills"
description: Meta-procedure for improving reasoning quality. Identifies the reasoning type in use, checks for common errors, and verifies logical structure.
output:
  format: "prose"
---

# Reasoning Skills

**Input**: $ARGUMENTS

---

## Step 1: Extract the Reasoning

Identify the core argument or reasoning chain in the input.

```
CLAIM/CONCLUSION: [what's being argued or concluded]
PREMISES:
1. [premise 1]
2. [premise 2]
...
REASONING CHAIN: [premise 1] + [premise 2] → [conclusion]
```

If the reasoning is implicit, make it explicit. State what's being assumed.

---

## Step 2: Classify the Reasoning Type

Identify which type(s) of reasoning are being used:

| Type | Structure | Example |
|------|-----------|---------|
| **Deductive** | If all premises true, conclusion must be true | All X are Y. Z is X. Therefore Z is Y. |
| **Inductive** | Specific observations → general rule | Every X I've seen does Y, so all X do Y. |
| **Abductive** | Best explanation for observed facts | Y happened. X would explain Y. So probably X. |
| **Analogical** | Similar case → similar outcome | X worked for A, B is like A, so X will work for B. |

```
REASONING TYPE: [deductive / inductive / abductive / analogical / mixed]
CONFIDENCE IN CLASSIFICATION: [high / medium / low]
```

---

## Step 3: Check for Type-Specific Errors

Apply the error checklist for the identified type:

**Deductive errors:**
- Invalid logical form (affirming the consequent, denying the antecedent)
- Hidden premises that are false
- Equivocation (same word used with different meanings)
- Scope errors (some vs. all)

**Inductive errors:**
- Small or biased sample
- Cherry-picked observations
- Hasty generalization
- Ignoring counterexamples

**Abductive errors:**
- Not considering alternative explanations
- Assuming the most interesting explanation is the most likely
- Ignoring base rates
- Conflating explanation with evidence

**Analogical errors:**
- Surface similarity without structural similarity
- Ignoring relevant differences between cases
- Over-extending the analogy

```
ERRORS FOUND:
- [error type]: [specific instance in this reasoning]
...

NO ERRORS FOUND: [if clean, state why it holds up]
```

---

## Step 4: Verify Premises

For each premise, assess:

- **True**: well-established, verifiable
- **Plausible**: reasonable but not verified
- **Questionable**: could easily be false
- **False**: demonstrably wrong

```
PREMISE AUDIT:
1. [premise 1] → [true/plausible/questionable/false] — [why]
2. [premise 2] → [true/plausible/questionable/false] — [why]
...
```

---

## Step 5: Check Logical Structure

Even if premises are true, does the conclusion actually follow?

- Does the conclusion go beyond what the premises support?
- Are there unstated assumptions bridging premises to conclusion?
- Could the premises be true and the conclusion false?
- Is the reasoning reversible (does it work backwards)?

```
STRUCTURAL ASSESSMENT:
- Conclusion follows from premises: [yes / partially / no]
- Gap between premises and conclusion: [none / small / large]
- Unstated assumptions needed: [list any]
```

---

## Step 6: Find the Weakest Link

Identify the single point where this reasoning is most likely to break.

```
WEAKEST LINK: [the specific premise, inference step, or assumption most likely to fail]
WHY: [what would cause it to break]
IMPACT: [if it breaks, what happens to the conclusion]
```

---

## Step 7: Reasoning Verdict

```
ORIGINAL REASONING: [1-line summary]
TYPE: [classification]
ERRORS: [list or "none found"]
WEAKEST LINK: [identified above]
OVERALL STRENGTH: [strong / moderate / weak / broken]
RECOMMENDATION: [accept / accept with caveats / revise / reject]
```

If weak or broken, suggest how to repair it.

---

## Integration

Use with:
- `/prcp` -> Improve the observations your reasoning is built on
- `/jdgm` -> Make a judgment call when reasoning is inconclusive
- `/mtcg` -> Monitor whether you're reasoning or rationalizing
- `/aex` -> Examine assumptions found in Step 4
- `/ht` -> Test the conclusion as a hypothesis
