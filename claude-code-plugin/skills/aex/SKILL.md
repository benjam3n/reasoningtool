---
name: aex
description: Extract hidden assumptions from any content. Surfaces what must be true for claims to hold, enabling deeper analysis.
---

# Assumption Extraction

**Input**: $ARGUMENTS

---

## Purpose

Every claim, plan, or argument rests on **hidden assumptions**—things that must be true for the claim to hold. This skill extracts those assumptions, making implicit beliefs explicit.

**Why this matters**:
- Hidden assumptions are often where claims fail
- Making assumptions explicit enables testing them
- Assumptions reveal worldview and blind spots

---

## Assumption Types

| Type | Description | Example |
|------|-------------|---------|
| **Causal** | X causes Y | "Marketing -> Sales" assumes causation |
| **Existence** | X exists | "The market" assumes a defined market exists |
| **Stability** | X won't change | "Current trends continue" assumes stability |
| **Access** | We can reach/use X | "Use the API" assumes API access |
| **Capability** | We/they can do X | "Team will deliver" assumes capability |
| **Value** | X is good/desirable | "Growth is good" assumes growth is valued |
| **Knowledge** | We/they know X | "Users understand" assumes knowledge |
| **Resources** | X resources available | "Budget exists" assumes funding |
| **Permission** | Allowed to do X | "We can change" assumes authority |
| **Timing** | X timing is correct | "Now is the time" assumes timing |

---

## The Extraction Process

### Step 1: Identify the Core Claims

Parse the input into distinct claims:

```
INPUT: [original content]

CORE CLAIMS IDENTIFIED:
1. [Claim 1]
2. [Claim 2]
3. [Claim 3]
...

TOTAL CLAIMS: [N]
```

---

### Step 2: For Each Claim, Extract Assumptions

Apply the assumption extraction questions:

```
CLAIM: [claim text]

EXTRACTION QUESTIONS:

1. CAUSAL: What must cause what for this to work?
   -> [assumption]

2. EXISTENCE: What must exist that isn't proven?
   -> [assumption]

3. STABILITY: What must stay the same?
   -> [assumption]

4. ACCESS: What must we be able to reach/use?
   -> [assumption]

5. CAPABILITY: What must someone be able to do?
   -> [assumption]

6. VALUE: What must be considered good/desirable?
   -> [assumption]

7. KNOWLEDGE: What must someone know?
   -> [assumption]

8. RESOURCES: What resources must be available?
   -> [assumption]

9. PERMISSION: What must we be allowed to do?
   -> [assumption]

10. TIMING: What timing must be correct?
    -> [assumption]
```

---

### Step 3: Rate Assumption Hiddenness

How obvious is each assumption?

| Level | Description | Action |
|-------|-------------|--------|
| **Surface** | Explicitly stated or obvious | Note for completeness |
| **Shallow** | Easily inferred | Flag for verification |
| **Deep** | Non-obvious, requires analysis | Highlight for attention |
| **Buried** | Counter-intuitive, easy to miss | Critical to surface |

```
ASSUMPTION HIDDENNESS RATING:

| Assumption | Type | Hiddenness | Risk if Wrong |
|------------|------|------------|---------------|
| [Assumption 1] | Causal | Deep | High |
| [Assumption 2] | Stability | Surface | Low |
| [Assumption 3] | Capability | Buried | Critical |
...
```

---

### Step 4: Identify Assumption Dependencies

Some assumptions depend on others:

```
ASSUMPTION DEPENDENCIES:

[Assumption A]
    |-- requires [Assumption B]
            |-- requires [Assumption C]

DEPENDENCY CHAINS:
1. [A] -> [B] -> [C] (if C fails, A and B fail)
2. [D] -> [E]

ROOT ASSUMPTIONS (no dependencies):
- [C]
- [E]
- [F]

Note: Root assumptions are most critical to verify
```

---

### Step 5: Categorize by Testability

```
TESTABILITY ASSESSMENT:

IMMEDIATELY TESTABLE (can verify now):
- [Assumption X]: Test by [method]
- [Assumption Y]: Test by [method]

TESTABLE WITH EFFORT (requires work):
- [Assumption Z]: Would need [what] to test

UNTESTABLE (must accept or reject):
- [Assumption W]: Cannot test because [reason]
  -> Decision: [accept/reject/assume for now]

ALREADY TESTED (evidence exists):
- [Assumption V]: [evidence source]
```

---

### Step 6: Generate Assumption Map

```
===================================================
ASSUMPTION MAP: [topic]
===================================================

CLAIM 1: [claim text]
|-- [Assumption 1.1] (Type: Causal, Hidden: Deep)
|-- [Assumption 1.2] (Type: Existence, Hidden: Surface)
|-- [Assumption 1.3] (Type: Capability, Hidden: Buried) [!]️ HIGH RISK

CLAIM 2: [claim text]
|-- [Assumption 2.1] (Type: Stability, Hidden: Shallow)
|-- [Assumption 2.2] (Type: Resources, Hidden: Deep)

[Continue for all claims]

===================================================

SUMMARY STATISTICS:
- Total claims analyzed: [N]
- Total assumptions extracted: [M]
- By type: Causal [X], Existence [Y], Stability [Z], ...
- By hiddenness: Surface [A], Shallow [B], Deep [C], Buried [D]
- High-risk assumptions: [count]

===================================================

PRIORITY ASSUMPTIONS (most critical to verify):

1. [Assumption] - Type: [type], Risk: HIGH
   Why critical: [reason]
   How to test: [method]

2. [Assumption] - Type: [type], Risk: HIGH
   Why critical: [reason]
   How to test: [method]

3. [Assumption] - Type: [type], Risk: MEDIUM
   Why critical: [reason]
   How to test: [method]

===================================================
```

---

## Quick Extraction (Abbreviated)

For fast assumption surfacing:

```
QUICK ASSUMPTION EXTRACTION: [topic]

Claim: [main claim]

Must be true:
[ ] [Causal assumption]
[ ] [Existence assumption]
[ ] [Stability assumption]
[ ] [Capability assumption]
[ ] [Resource assumption]

Most hidden: [which one]
Most risky if wrong: [which one]
```

---

## Example: "We should expand to the European market"

### Claims
1. We should expand (action is good)
2. European market is the target (location choice)
3. Expansion is possible (capability exists)

### Assumption Extraction

**Claim 1: "We should expand"**
- CAUSAL: Expansion -> growth/profit
- VALUE: Growth is desirable
- TIMING: Now is the right time
- STABILITY: Current success will continue

**Claim 2: "European market"**
- EXISTENCE: A viable European market exists for us
- ACCESS: We can enter this market
- KNOWLEDGE: We understand European customers
- PERMISSION: Regulations allow entry

**Claim 3: "Expansion is possible"**
- CAPABILITY: We can execute international expansion
- RESOURCES: We have capital, people, time
- STABILITY: Our core business won't suffer

### Assumption Map Output

```
PRIORITY ASSUMPTIONS:

1. "We understand European customers" - Knowledge, BURIED
   Why critical: Product-market fit depends on this
   How to test: Customer research, pilot market

2. "Our core business won't suffer" - Stability, DEEP
   Why critical: Expansion could drain resources
   How to test: Capacity analysis, scenario modeling

3. "Regulations allow entry" - Permission, SHALLOW
   Why critical: Could block entire plan
   How to test: Legal review, compliance check
```

---

## Assumption Extraction Patterns

### For Plans/Strategies
Focus on: Capability, Resources, Timing, Stability

### For Arguments/Claims
Focus on: Causal, Existence, Knowledge, Value

### For Predictions
Focus on: Stability, Causal, Timing

### For Decisions
Focus on: Value, Access, Permission, Capability

---

## Quality Checklist

Before completing:
- [ ] All core claims identified
- [ ] Each claim analyzed with 10 extraction questions
- [ ] Hiddenness rated for each assumption
- [ ] Dependencies mapped
- [ ] Testability assessed
- [ ] Priority assumptions identified
- [ ] Assumption map generated

---

## Integration

Use with:
- `/assumption_inversion` -> Invert assumptions to find blind spots
- `/araw` -> Test assumptions with Assume Right / Assume Wrong
- `/cross_domain_analogy` -> Find where assumptions differ in other domains
