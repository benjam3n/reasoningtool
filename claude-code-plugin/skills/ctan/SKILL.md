---
name: "ctan - Contract Analysis"
description: Review and understand a contract or agreement by mapping obligations, consideration, risk allocation, and concerning terms.
---

# Contract Analysis

**Input**: $ARGUMENTS

---

## Step 1: Identify Parties and Obligations

Map who is involved and what each party must do.

```
PARTIES:
- Party A: [name/role]
- Party B: [name/role]
- Other parties: [if any — guarantors, third-party beneficiaries]

OBLIGATIONS:
Party A must:
1. [obligation] — Section: [ref] — Timeline: [when]
2. [obligation] — Section: [ref] — Timeline: [when]

Party B must:
1. [obligation] — Section: [ref] — Timeline: [when]
2. [obligation] — Section: [ref] — Timeline: [when]

CONDITIONAL OBLIGATIONS (triggered by events):
- If [event], then [party] must [obligation] — Section: [ref]
```

---

## Step 2: Map Consideration

What does each party give and get? Both sides must receive value.

```
CONSIDERATION MAP:
Party A gives: [what they provide — money, services, goods, rights]
Party A gets: [what they receive]

Party B gives: [what they provide]
Party B gets: [what they receive]

BALANCE ASSESSMENT: [Roughly balanced / Favors A / Favors B / Significantly unbalanced]
REASON: [why]
```

---

## Step 3: Identify Key Terms and Conditions

Pull out the terms that matter most.

```
KEY TERMS:
- Duration: [length of agreement]
- Renewal: [auto-renew? notice period?]
- Payment: [amount, schedule, method]
- Performance standards: [SLAs, benchmarks, acceptance criteria]
- Intellectual property: [who owns what is created]
- Confidentiality: [scope, duration, exceptions]
- Non-compete/non-solicit: [scope, duration, geography]
- Governing law: [jurisdiction]
- Dispute resolution: [litigation / arbitration / mediation — where]

DEFINITIONS TO WATCH:
- [term]: defined as [definition] — Note: [broader/narrower than expected?]
```

---

## Step 4: Find Risk Allocation Clauses

Identify how the contract distributes risk between parties.

```
RISK ALLOCATION:

Liability:
- Cap on liability: [amount/formula or unlimited]
- Exclusion of consequential damages: [yes/no — which party benefits]
- Indemnification: [who indemnifies whom, for what]

Insurance:
- Required coverage: [types and amounts]

Representations and warranties:
- [key rep/warranty] — Made by: [party] — Survives termination: [yes/no]

Force majeure: [included? what events qualify?]

RISK BALANCE: [Balanced / Favors A / Favors B]
```

---

## Step 5: Identify Termination Conditions

How does this agreement end?

```
TERMINATION:
- For convenience: [which party can terminate without cause? notice period?]
- For cause: [what constitutes cause? cure period?]
- Automatic: [does it expire on a date?]
- Insolvency/bankruptcy: [trigger?]

POST-TERMINATION:
- Obligations that survive: [confidentiality, non-compete, indemnification, etc.]
- Transition assistance: [required? at what cost?]
- Data/property return: [what must be returned or destroyed?]
- Wind-down period: [how long?]
```

---

## Step 6: Flag Unusual or Concerning Terms

Identify anything that deviates from standard practice or creates outsized risk.

```
RED FLAGS:
1. [term] — Section: [ref]
   Concern: [why this is unusual or risky]
   Standard practice would be: [what you'd normally expect]

2. [term] — Section: [ref]
   Concern: [why this is unusual or risky]
   Standard practice would be: [what you'd normally expect]

YELLOW FLAGS (not alarming but worth negotiating):
1. [term] — Section: [ref]
   Suggestion: [how to improve]

MISSING TERMS (expected but absent):
1. [term that should be included]
   Risk of omission: [what could go wrong]
```

---

## Integration

Use with:
- `/leg` -> Apply broader legal reasoning to the situation
- `/rtas` -> Assess the rights of each party under the contract
- `/cba` -> Cost-benefit analysis of accepting vs. negotiating terms
