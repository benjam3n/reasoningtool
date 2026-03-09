---
name: "usrn - User-Need Reasoning"
description: "Reason about what someone actually needs based on what they said. Surfaces underlying needs, unstated constraints, and what would truly satisfy the request."
---

# User-Need Reasoning

**Input**: $ARGUMENTS

---

## Step 1: Capture the Stated Request

Write down exactly what was asked for, with zero interpretation.

1. Quote or paraphrase the literal request
2. Note the format: question, command, complaint, wish, or comparison
3. Note any specifics given (numbers, names, constraints, deadlines)
4. Note what was NOT specified (left ambiguous or assumed)

```
STATED REQUEST: [exact quote or close paraphrase]
FORMAT: [question / command / complaint / wish / comparison]
SPECIFICS GIVEN: [list]
LEFT UNSPECIFIED: [list]
```

---

## Step 2: Identify the Likely Underlying Need

The stated request is a SOLUTION the person chose. The underlying need is the PROBLEM they're trying to solve.

Ask these questions:
1. Why would someone ask for this? What situation are they in?
2. What problem does this request solve?
3. What would they do with the answer/result?
4. What would "success" look like from their perspective — not the deliverable, but the outcome?

Common patterns:
- "How do I do X?" -> They need outcome Y, and X is the approach they thought of
- "Which is better, A or B?" -> They need to make a decision and want confidence
- "Can you explain X?" -> They're stuck on something that requires understanding X
- "I need X by Friday" -> There's a downstream commitment driving the deadline

```
UNDERLYING NEED: [the real problem or goal]
CONFIDENCE: [high / moderate / low] that this is the real need
REASONING: [why you think this is the underlying need]
```

---

## Step 3: Check Alignment Between Stated and Underlying

Compare the stated request to the underlying need:

| Alignment | Description | Action |
|---|---|---|
| **Matched** | Stated request directly addresses the real need | Proceed as asked |
| **Partial** | Stated request addresses part of the need or addresses it indirectly | Fulfill the request AND address the gap |
| **Mismatched** | Stated request won't actually solve the real problem | Surface the mismatch diplomatically |
| **Unclear** | Can't determine alignment without more information | Ask clarifying questions (Step 6) |

```
ALIGNMENT: [matched / partial / mismatched / unclear]
EXPLANATION: [how the stated request relates to the underlying need]
```

If MATCHED: you can proceed to Step 5 quickly.
If MISMATCHED: this is the most valuable finding — handle carefully in Step 5.

---

## Step 4: Identify Unstated Constraints

People leave out constraints they consider obvious. Surface them:

1. **Time constraints**: Is there a deadline? How urgent is this?
2. **Resource constraints**: Budget, skills, tools, team size?
3. **Social constraints**: Who else is affected? Whose approval is needed?
4. **Quality constraints**: How good does it need to be? What's "good enough"?
5. **Scope constraints**: What's explicitly out of bounds?
6. **Emotional constraints**: Are there options they'd reject for non-rational reasons?

```
LIKELY UNSTATED CONSTRAINTS:
- [constraint] — Confidence: [high / medium / low]
- [constraint] — Confidence: [high / medium / low]
...
```

---

## Step 5: Propose What Would Actually Satisfy the Need

Based on Steps 1-4, propose the response that would genuinely satisfy the person:

1. If alignment is MATCHED: deliver what was asked, enhanced by awareness of unstated constraints
2. If alignment is PARTIAL: deliver what was asked PLUS address the gap
3. If alignment is MISMATCHED: acknowledge the stated request, then reframe around the underlying need

For mismatched cases, use this formula:
- "I can do [stated request], and here's that answer: [answer]."
- "But based on [evidence], it sounds like what you're really trying to do is [underlying need]."
- "If that's right, here's what I'd actually recommend: [better solution]."

```
PROPOSED RESPONSE STRATEGY:
- Address stated request: [yes / acknowledge only]
- Address underlying need: [how]
- Key addition the person didn't ask for but needs: [what]
```

Never ONLY answer the underlying need while ignoring the stated request. That feels dismissive. Always acknowledge what was asked.

---

## Step 6: Verify With the User

If confidence in the underlying need is MODERATE or LOW, verify before investing effort:

Formulate 1-3 clarifying questions that:
1. Are quick to answer (yes/no or one sentence)
2. Distinguish between your hypotheses about the underlying need
3. Don't feel interrogative or presumptuous

```
VERIFICATION QUESTIONS:
1. [question that distinguishes hypothesis A from B]
2. [question that surfaces the most impactful unstated constraint]
...
```

If confidence is HIGH: state your interpretation and invite correction. "It sounds like you're trying to [need] — is that right, or am I off base?"

---

## Integration

Use with:
- `/gu` -> Deep-dive on the goal behind the request
- `/sp` -> Sharpen the request before fulfilling it
- `/per` -> If the response requires persuading the user to reframe
- `/aex` -> Check your own assumptions about what the user needs
