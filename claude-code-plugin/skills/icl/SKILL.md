---
name: "icl - Intentional Claim Analysis"
description: Evaluate claims about what someone wants or intends. Check behavioral evidence, stated vs revealed preferences, and alternative intentions.
output:
  format: "prose"
---

# Intentional Claim Analysis

**Input**: $ARGUMENTS

---

## Step 1: State the Intentional Claim

Extract the claim about someone's intentions, desires, or goals.

```
INTENTIONAL CLAIM: [Subject] wants/intends/aims to [stated intention]
SUBJECT: [who — individual, organization, group]
CLAIMED INTENTION: [what they allegedly want or intend]
CLAIM SOURCE: [self-reported / attributed by others / inferred from behavior]
SPECIFICITY: [precise goal / vague aspiration / hidden agenda claim]
```

Rules:
- Distinguish between wants (desires), intends (plans), and aims (goals with action)
- Self-reported intentions have different credibility than attributed ones
- "They want to..." is a claim about someone's inner state — inherently harder to verify than behavioral claims
- If the claim is about a group, note that groups don't have unified intentions — individuals within them do

---

## Step 2: Check Behavioral Evidence

Compare the claimed intention against observable behavior.

```
BEHAVIORAL EVIDENCE:
ACTIONS CONSISTENT WITH CLAIMED INTENTION:
1. [Action]: [How it supports the claim]
2. [Action]: [How it supports the claim]

ACTIONS INCONSISTENT WITH CLAIMED INTENTION:
1. [Action]: [How it contradicts the claim]
2. [Action]: [How it contradicts the claim]

ACTIONS ABSENT (expected if intention were real):
1. [Expected action not taken]: [Why you'd expect it]

BEHAVIORAL VERDICT: [CONSISTENT / MIXED / INCONSISTENT]
```

Rules:
- Actions speak louder than statements — always check behavior
- A single inconsistent action doesn't disprove intention (people have competing priorities)
- But a pattern of inconsistent actions seriously undermines the claim
- Absent actions can be as telling as present ones — what WOULD they do if they really intended this?

---

## Step 3: Check Stated vs. Revealed Preferences

Compare what the subject says they want with what their choices actually reveal.

```
PREFERENCE ANALYSIS:
STATED PREFERENCE: [What they say they want]
REVEALED PREFERENCE: [What their actual choices/resource allocation shows]

ALIGNMENT: [ALIGNED / PARTIALLY ALIGNED / MISALIGNED]

IF MISALIGNED:
- Possible explanations:
  1. [They're deceiving others — strategic misrepresentation]
  2. [They're deceiving themselves — self-serving narrative]
  3. [Constraints prevent acting on real intention]
  4. [Intention changed but statements haven't caught up]
- Most likely explanation: [assessment]
```

Rules:
- Where people spend their time and money reveals more than what they say
- Misalignment is common and not always dishonest — constraints and competing priorities are real
- Organizations are especially prone to stated/revealed preference gaps (mission statements vs. budgets)
- Ask: "If I could only see their actions and not hear their words, what would I conclude?"

---

## Step 4: Identify Alternative Intentions

Generate other intentions that would explain the same observable behavior.

```
ALTERNATIVE INTENTIONS:
1. [Alternative intention]: [How it explains the same evidence]
   - Plausibility: [HIGH / MEDIUM / LOW]
   - Explains evidence better than claimed intention? [YES / NO / EQUALLY]

2. [Alternative intention]: [How it explains the same evidence]
   - Plausibility: [HIGH / MEDIUM / LOW]
   - Explains evidence better? [YES / NO / EQUALLY]

3. [Alternative intention]: [How it explains the same evidence]
   - Plausibility: [HIGH / MEDIUM / LOW]
   - Explains evidence better? [YES / NO / EQUALLY]
```

Rules:
- Generate at least 3 alternatives before assessing — premature closure is the main error
- Include mundane alternatives (laziness, inertia, habit) not just dramatic ones (conspiracy, malice)
- The simplest intention that explains the behavior is usually correct
- Multiple intentions can coexist — people often want several things simultaneously

---

## Step 5: Assess Credibility

Deliver a judgment on the intentional claim.

```
CREDIBILITY ASSESSMENT:
- Claim: [Subject] intends [intention]
- Behavioral consistency: [CONSISTENT / MIXED / INCONSISTENT]
- Stated/revealed alignment: [ALIGNED / MISALIGNED]
- Best alternative intention: [what else could explain the behavior]
- Alternative is more plausible? [YES / NO / EQUALLY PLAUSIBLE]

VERDICT: [CREDIBLE / PLAUSIBLE / UNCERTAIN / DOUBTFUL / NOT CREDIBLE]

CONFIDENCE: [HIGH / MEDIUM / LOW]

REASONING: [2-3 sentences explaining the verdict]

WHAT TO WATCH: [Observable behaviors that would confirm or disconfirm the intention going forward]
```

Rules:
- CREDIBLE = behavioral evidence strongly supports the claimed intention
- PLAUSIBLE = evidence is compatible but not conclusive
- UNCERTAIN = evidence is too thin or mixed to judge
- DOUBTFUL = evidence points away from the claimed intention
- NOT CREDIBLE = behavior clearly contradicts the claimed intention
- Always suggest what to watch — intentions are revealed over time

---

## Integration

Use with:
- `/fctl` -> Verify factual claims about the subject's behavior
- `/ncl` -> If the claim is "they should want X," analyze the normative aspect
- `/rlcl` -> If the claim is about how intentions relate to outcomes, analyze the relationship
- `/mtcl` -> If the claim is about claims about intentions, use meta-claim analysis
