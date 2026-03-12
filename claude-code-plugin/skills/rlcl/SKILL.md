---
name: "rlcl - Relational Claim Analysis"
description: Evaluate claims about how things relate. Verify the relationship type, test its strength, and identify its boundaries.
output:
  format: "prose"
---

# Relational Claim Analysis

**Input**: $ARGUMENTS

---

## Step 1: State the Relationship

Extract and formalize what relationship is being claimed.

```
RELATIONAL CLAIM: [A] [relationship] [B]
ENTITY A: [what it is, clearly defined]
ENTITY B: [what it is, clearly defined]
CLAIMED RELATIONSHIP TYPE: [causal / correlational / structural / analogical / hierarchical / oppositional / dependent]
DIRECTION: [A->B / B->A / bidirectional / non-directional]
```

Rules:
- Many relational claims are vague — "X is related to Y" could mean almost anything
- Force precision: what KIND of relationship is being claimed?
- Check direction — "A depends on B" is different from "B depends on A"
- If A or B are poorly defined, the relationship claim can't be evaluated — flag this

---

## Step 2: Check If Both Things Exist as Described

Verify that the entities in the relationship are real and accurately characterized.

```
ENTITY VERIFICATION:
ENTITY A: [name]
- Exists as described? [YES / PARTIALLY / NO]
- Accurate characterization? [YES / DISTORTED / OVERSIMPLIFIED]
- Key nuance missing: [if any]

ENTITY B: [name]
- Exists as described? [YES / PARTIALLY / NO]
- Accurate characterization? [YES / DISTORTED / OVERSIMPLIFIED]
- Key nuance missing: [if any]
```

Rules:
- A relationship between two mischaracterized things is meaningless even if the relationship type is correct
- Watch for strawmanning — one entity described accurately, the other distorted
- Watch for reification — treating abstract concepts as concrete things ("the market wants...")
- If either entity doesn't exist as described, the relational claim fails at the foundation

---

## Step 3: Verify the Relationship Type

Test whether the claimed relationship type is accurate.

```
RELATIONSHIP TYPE ANALYSIS:
CLAIMED: [type]
TESTED ALTERNATIVES:
1. Could it be [alternative type] instead? [assessment]
2. Could it be [alternative type] instead? [assessment]
3. Could it be [alternative type] instead? [assessment]

ACTUAL TYPE: [what the evidence best supports]
MATCH: [CONFIRMED / PARTIALLY CORRECT / WRONG TYPE]
```

Relationship type definitions:
- **Causal**: A produces or prevents B
- **Correlational**: A and B co-occur but neither causes the other
- **Structural**: A and B are parts of the same system
- **Analogical**: A resembles B in specific ways but they're independent
- **Hierarchical**: A contains B, or B is a type of A
- **Oppositional**: A and B are in tension or conflict
- **Dependent**: A requires B to function (or vice versa)

Rules:
- The most common error is claiming causal when the relationship is correlational
- The second most common is claiming analogical when things are actually unrelated
- Test at least 2 alternative relationship types before confirming the claimed one

---

## Step 4: Test the Relationship's Strength

Assess how strong and reliable the relationship is.

```
STRENGTH ASSESSMENT:
- Consistency: Does the relationship hold across different contexts? [ALWAYS / USUALLY / SOMETIMES / RARELY]
- Magnitude: How strong is the connection? [STRONG / MODERATE / WEAK / NEGLIGIBLE]
- Exclusivity: Could A have this relationship with many other things? [EXCLUSIVE / SELECTIVE / COMMON]
- Stability: Does the relationship persist over time? [STABLE / VARIABLE / DETERIORATING]

OVERALL STRENGTH: [STRONG / MODERATE / WEAK / QUESTIONABLE]
```

Rules:
- A relationship that only holds in specific contexts is weaker than one that holds broadly
- A relationship where A connects to many things equally is less meaningful
- Strength and existence are different questions — a weak relationship still exists
- Assess strength with evidence, not intuition

---

## Step 5: Identify Boundaries

Find where the relationship breaks down or stops applying.

```
BOUNDARY CONDITIONS:
THE RELATIONSHIP HOLDS WHEN:
- [Condition 1]
- [Condition 2]

THE RELATIONSHIP BREAKS WHEN:
- [Condition 1]: [What happens to A-B when this occurs]
- [Condition 2]: [What happens to A-B when this occurs]

EDGE CASES:
- [Situation where the relationship is ambiguous]

SCOPE: [The domain within which this relationship claim is valid]
```

Rules:
- Every relationship has boundaries — if you can't find them, you haven't looked
- Boundary conditions are often more informative than the relationship itself
- Overgeneralized relationships (claimed to hold everywhere) are almost always wrong at the edges
- State the valid scope explicitly — this prevents misapplication

---

## Step 6: Verdict

```
RELATIONAL VERDICT:
- Claim: [A] [relationship] [B]
- Relationship exists: [YES / PARTIALLY / NO]
- Type as claimed: [CONFIRMED / DIFFERENT TYPE: ___]
- Strength: [STRONG / MODERATE / WEAK]
- Valid scope: [where it holds]

REFINED STATEMENT: [How the relationship should actually be described]
```

---

## Integration

Use with:
- `/cscl` -> If the relationship is causal, do a full causal analysis
- `/fctl` -> Verify factual claims about the entities in the relationship
- `/mocl` -> If the claim is about a possible relationship, analyze the modal aspect
- `/mtcl` -> If the claim is about how claims relate to each other, use meta-claim analysis
