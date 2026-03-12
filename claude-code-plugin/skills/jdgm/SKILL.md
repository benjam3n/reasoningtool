---
name: "jdgm - Judgment"
description: Systematic procedure for making good judgments under uncertainty. Separates facts from interpretation, checks calibration against base rates, and produces an explicit confidence level.
output:
  format: "prose"
---

# Judgment

**Input**: $ARGUMENTS

---

## Step 1: Identify What's Being Judged

Be precise about the judgment call. Vague judgments produce vague results.

```
JUDGMENT REQUIRED: [what exactly needs to be decided or assessed]
TYPE: [prediction / evaluation / classification / estimation / selection]
STAKES: [what depends on getting this right]
```

---

## Step 2: Separate Facts from Interpretation

Split what you know into layers:

- **Hard facts**: Directly verifiable, no dispute possible
- **Soft facts**: Generally accepted but could be wrong
- **Interpretations**: Your reading of the facts (others might read differently)
- **Assumptions**: Things you're taking as given without checking

```
FACTS:
- [fact 1] — [hard/soft]
- [fact 2] — [hard/soft]

INTERPRETATIONS:
- [interpretation 1] — based on [which facts]
- [interpretation 2] — based on [which facts]

ASSUMPTIONS:
- [assumption 1] — status: [checked/unchecked]
...
```

RULE: If you can't tell whether something is fact or interpretation, it's interpretation.

---

## Step 3: Check Calibration

Your gut confidence is probably wrong. Correct it.

- **State your initial estimate**: "I'm about [X]% sure that [judgment]"
- **Check the base rate**: How often does this type of thing turn out this way in general?
- **Apply the outside view**: Ignore the specifics for a moment — what would a statistical model predict?
- **Reconcile**: If your inside view and outside view differ, why?

```
CALIBRATION:
- Initial gut: [X]% confident
- Base rate for this type of judgment: [Y]%
- Outside view prediction: [Z]%
- Reconciled estimate: [final]% — because [reasoning for where you landed]
```

---

## Step 4: Consider Reference Class

What is this an instance of? Find the right comparison set.

- What's the most similar past case you can identify?
- What's the typical outcome for cases like this?
- How is this case different from the reference class? (better or worse?)

```
REFERENCE CLASS: [what category this belongs to]
TYPICAL OUTCOME: [what usually happens in this class]
THIS CASE IS DIFFERENT BECAUSE: [specific differences and their direction]
ADJUSTED EXPECTATION: [updated based on differences]
```

SKIP: If this is truly novel with no useful reference class, acknowledge that and proceed with extra caution.

---

## Step 5: Identify What Would Change Your Judgment

Before committing, specify your update conditions.

- What evidence would make you more confident?
- What evidence would make you less confident?
- What single fact, if true, would flip your judgment entirely?

```
WOULD INCREASE CONFIDENCE:
- [evidence 1]
- [evidence 2]

WOULD DECREASE CONFIDENCE:
- [evidence 1]
- [evidence 2]

WOULD FLIP JUDGMENT:
- [the key reversing condition]
```

This step prevents you from becoming unfalsifiable.

---

## Step 6: Make the Call

State the judgment clearly. No hedging into meaninglessness.

```
JUDGMENT: [clear, specific statement]
CONFIDENCE: [X]% — [what this means: "I'd be wrong about [100-X] out of 100 similar calls"]
KEY FACTOR: [the single most important input to this judgment]
WEAKEST POINT: [where this judgment is most likely to be wrong]
```

---

## Step 7: Decision Record

```
WHAT WAS JUDGED: [1-line summary]
JUDGMENT: [the call]
CONFIDENCE: [X]%
BASED ON: [top 2-3 inputs]
WOULD CHANGE IF: [key reversing condition]
REVIEW WHEN: [trigger or date to revisit this judgment]
```

---

## Integration

Use with:
- `/prcp` -> Improve perception before judging
- `/rskl` -> Check the reasoning supporting your judgment
- `/mtcg` -> Monitor for biases during the judgment process
- `/ht` -> Test your judgment as a formal hypothesis
- `/dcp` -> If the judgment feeds into a decision
