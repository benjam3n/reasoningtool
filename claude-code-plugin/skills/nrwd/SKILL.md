---
name: "nrwd - Narrow Domain Analysis"
description: Deep analysis within a specific domain. Goes deep not wide, using domain-specific vocabulary, frameworks, and constraints.
---

# Narrow Domain Analysis

**Input**: $ARGUMENTS

---

## Step 1: Identify the Domain

State the specific domain under analysis. Be precise — narrow beats broad.

```
DOMAIN: [The specific domain]
DOMAIN LEVEL: [Field > Subfield > Specialty, as specific as possible]
```

If the input spans multiple domains, pick the primary one. Flag secondary domains for later.

---

## Step 2: Establish Domain Boundaries

Define what is inside and outside this analysis.

```
IN SCOPE:
- [What belongs to this domain]
- [What this analysis will cover]

OUT OF SCOPE:
- [Adjacent domains explicitly excluded]
- [Tangential topics to ignore]

BOUNDARY RATIONALE: [Why these boundaries make sense]
```

---

## Step 3: Go Deep

Analyze the input using domain-specific depth. This is the core of the skill — resist the urge to go wide.

```
DOMAIN-SPECIFIC VOCABULARY:
- [Key term 1]: [precise domain meaning]
- [Key term 2]: [precise domain meaning]

APPLICABLE FRAMEWORKS:
- [Framework 1]: [how it applies here]
- [Framework 2]: [how it applies here]

DEEP ANALYSIS:
[The actual analysis, using domain language and frameworks.
 This should read like it was written by a domain expert,
 not a generalist.]
```

---

## Step 4: Domain-Specific Constraints

Identify constraints that only someone in this domain would know about.

```
DOMAIN CONSTRAINTS:
- [Constraint 1]: [why it matters here]
- [Constraint 2]: [why it matters here]

CONVENTIONS:
- [Convention 1]: [standard practice in this domain]
- [Convention 2]: [standard practice in this domain]

VIOLATIONS: [Does the input violate any domain conventions? If so, flag them.]
```

---

## Step 5: Domain-Appropriate Output

Format the final output the way a domain practitioner would expect to see it.

```
FINDINGS:
[Structured output using the format conventions of the domain.
 E.g., a legal analysis uses IRAC, a medical analysis uses SOAP,
 an engineering analysis uses requirements/specs format.]

DOMAIN CONFIDENCE: [How confident is this analysis given domain norms?]
RECOMMENDED NEXT STEP: [What a domain expert would do next]
```

---

## Integration

Use with:
- `/unvs` -> Test whether findings generalize beyond this domain
- `/ctgp` -> Identify gaps within the domain
- `/skev` -> Evaluate a domain-specific method or procedure
