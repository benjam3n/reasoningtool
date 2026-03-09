---
name: "rtas - Rights Assessment"
description: Identify and evaluate rights in a situation by mapping all parties, determining applicable rights, assessing respect, and identifying remedies.
---

# Rights Assessment

**Input**: $ARGUMENTS

---

## Step 1: Identify All Parties

Map every person or entity with a stake in this situation.

```
PARTIES:
1. [party] — Role: [their role in the situation]
2. [party] — Role: [their role in the situation]
3. [party] — Role: [their role in the situation]

ABSENT PARTIES (affected but not present):
- [party] — How affected: [description]

POWER DYNAMICS:
- [who holds more power and why]
```

---

## Step 2: Determine Applicable Rights

For each party, identify what rights they hold and where those rights come from.

```
RIGHTS MAP:

Party: [name]
| Right | Source | Type | Status |
|-------|--------|------|--------|
| [right] | [law/contract/policy/moral norm] | Legal / Contractual / Moral | Active / Conditional / Expired |
| [right] | [law/contract/policy/moral norm] | Legal / Contractual / Moral | Active / Conditional / Expired |

Party: [name]
| Right | Source | Type | Status |
|-------|--------|------|--------|
| [right] | [law/contract/policy/moral norm] | Legal / Contractual / Moral | Active / Conditional / Expired |
| [right] | [law/contract/policy/moral norm] | Legal / Contractual / Moral | Active / Conditional / Expired |

RIGHTS CATEGORIES CONSIDERED:
- [ ] Constitutional/fundamental rights
- [ ] Statutory rights (from legislation)
- [ ] Contractual rights (from agreements)
- [ ] Property rights (ownership, use, access)
- [ ] Employment rights (if applicable)
- [ ] Privacy rights
- [ ] Intellectual property rights
- [ ] Moral/ethical rights (not legally enforceable but relevant)
```

---

## Step 3: Assess Whether Rights Are Being Respected

For each identified right, evaluate the current situation.

```
RIGHTS ASSESSMENT:

1. Right: [description]
   Holder: [party]
   Status: [RESPECTED / VIOLATED / AT RISK / UNCLEAR]
   Evidence: [what indicates this status]
   By whom: [who is responsible for respecting/violating]

2. Right: [description]
   Holder: [party]
   Status: [RESPECTED / VIOLATED / AT RISK / UNCLEAR]
   Evidence: [what indicates this status]
   By whom: [who is responsible for respecting/violating]

SUMMARY:
- Rights being respected: [count]
- Rights being violated: [count]
- Rights at risk: [count]
- Rights unclear: [count]
```

---

## Step 4: Identify Conflicts Between Rights

Rights often collide. Map the tensions.

```
RIGHTS CONFLICTS:

1. CONFLICT: [Party A's right to X] vs. [Party B's right to Y]
   Nature: [why these rights are in tension]
   Precedent/hierarchy: [does one right generally take priority?]
   Resolution framework: [how this type of conflict is typically resolved]

2. CONFLICT: [right] vs. [right]
   Nature: [why these rights are in tension]
   Precedent/hierarchy: [does one right generally take priority?]
   Resolution framework: [how this type of conflict is typically resolved]

BALANCING FACTORS:
- Proportionality: [is the infringement proportional to the goal?]
- Necessity: [is there a less restrictive alternative?]
- Legitimacy: [is the purpose of the infringement legitimate?]
```

---

## Step 5: Determine Remedies Available

For violated or at-risk rights, what can be done?

```
REMEDIES:

For [violated right]:
  SELF-HELP: [actions the rights-holder can take independently]
  NEGOTIATION: [how to address through direct engagement]
  FORMAL COMPLAINT: [internal processes — HR, ombudsman, grievance]
  EXTERNAL COMPLAINT: [regulatory bodies, agencies]
  LEGAL ACTION: [court, arbitration, mediation]

  RECOMMENDED PATH: [which remedy to pursue first]
  COST/BENEFIT: [effort and risk vs. likely outcome]
  TIME SENSITIVITY: [any deadlines — statute of limitations, notice periods]

PREVENTIVE MEASURES (for at-risk rights):
1. [measure] — Protects: [right] — Implementation: [how]
```

---

## Integration

Use with:
- `/leg` -> Apply legal reasoning to complex rights questions
- `/ctan` -> Analyze contracts that define or limit rights
- `/csb` -> Build consensus when rights conflict between parties
