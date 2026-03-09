---
name: "ratn - Rationale Construction"
description: Builds a clear, compelling rationale for any decision or recommendation. Organizes evidence by strength, addresses counterarguments, and outputs a persuasive but honest case.
---

# Rationale Construction

**Input**: $ARGUMENTS

---

## Step 1: State the Conclusion

Lead with the answer. A rationale works backwards from the conclusion.

```
CONCLUSION: [The decision, recommendation, or position being justified]
AUDIENCE: [Who needs to be convinced?]
STAKES: [What happens if the audience is not convinced?]
```

---

## Step 2: List the Supporting Evidence

Gather all evidence that supports the conclusion.

```
SUPPORTING EVIDENCE:
1. [Evidence 1]
   Type: [DATA / EXPERIENCE / LOGIC / AUTHORITY / ANALOGY]
   Strength: [STRONG / MODERATE / WEAK]
   Source: [Where this evidence comes from]

2. [Evidence 2]
   Type: [DATA / EXPERIENCE / LOGIC / AUTHORITY / ANALOGY]
   Strength: [STRONG / MODERATE / WEAK]
   Source: [Where this evidence comes from]

3. [Evidence 3]
   Type: [DATA / EXPERIENCE / LOGIC / AUTHORITY / ANALOGY]
   Strength: [STRONG / MODERATE / WEAK]
   Source: [Where this evidence comes from]

...

EVIDENCE TYPES PRESENT: [Which types do you have? Which are missing?]
```

---

## Step 3: Organize by Strength

Arrange evidence from strongest to weakest. Lead with your best.

```
EVIDENCE HIERARCHY:
1. [Strongest evidence] — this alone almost justifies the conclusion because: [why]
2. [Second strongest] — this adds significant weight because: [why]
3. [Third strongest] — this reinforces the pattern because: [why]
...
N. [Weakest — include only if it adds something the others don't]

CUMULATIVE CASE: [Is the evidence collectively stronger than any single piece?]
```

---

## Step 4: Address the Strongest Counterargument

Find the best argument against your conclusion and respond to it directly.

```
STRONGEST COUNTERARGUMENT:
[State it as strongly and fairly as possible — steelman it]

RESPONSE:
[Why the conclusion still holds despite this counterargument.
 Options: the counterargument is factually wrong, it's true but
 outweighed, it applies in theory but not in this context,
 or it points to a real risk that can be mitigated.]

REMAINING COUNTERARGUMENTS:
- [Counter 2] — brief response: [why it doesn't change the conclusion]
- [Counter 3] — brief response: [why it doesn't change the conclusion]

HONEST CONCESSION: [What does the opposition get right?
  Acknowledging this makes the rationale more credible.]
```

---

## Step 5: Construct the Rationale

Combine everything into a persuasive but honest narrative.

```
RATIONALE:

[Opening: State the conclusion clearly.]

[Body: Present evidence in order of strength. Connect each piece
 to the conclusion with explicit reasoning — don't just list facts,
 show why they matter.]

[Counterargument: Acknowledge the strongest objection and explain
 why it doesn't change the conclusion.]

[Close: Restate the conclusion with the accumulated weight of evidence
 behind it. If appropriate, state what would change your mind.]
```

```
RATIONALE QUALITY CHECK:
- Persuasive: [Does it move the target audience?]
- Honest: [Does it acknowledge real weaknesses?]
- Complete: [Does it leave obvious questions unanswered?]
- Actionable: [Does it make clear what should happen next?]
```

---

## Integration

Use with:
- `/benf` -> Generate benefit evidence to feed into the rationale
- `/efrt` -> Include effort estimates as part of the case
- `/cand` -> Build rationale for a candidate recommendation
- `/aex` -> Check assumptions embedded in the rationale
