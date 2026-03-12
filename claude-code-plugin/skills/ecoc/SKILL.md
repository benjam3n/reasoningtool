---
name: "ecoc - Ethical Code of Conduct"
description: Create a practical code of ethics for a person, team, or organization — one that handles real edge cases, not just platitudes.
output:
  format: "prose"
---

# Ethical Code of Conduct

**Input**: $ARGUMENTS

---

## Step 1: Identify the Domain

Who is this code for and what do they do?

```
ENTITY: [Person / Team / Organization]
DOMAIN: [What they do — e.g., software development, healthcare, consulting]
SCOPE: [Internal conduct only / External-facing / Both]
AUDIENCE: [Who will read and follow this code]
POWER DYNAMICS: [Who has power over whom in this context]
```

---

## Step 2: Surface Key Ethical Tensions

Every domain has recurring ethical friction points. Identify the top 5-7 tensions.

```
TENSIONS:
1. [Tension] — e.g., "Speed vs. thoroughness in code review"
2. [Tension] — e.g., "Client confidentiality vs. public safety"
3. [Tension] — e.g., "Individual recognition vs. team credit"
4. [Tension]
5. [Tension]
```

For each tension: Who gets hurt when this goes wrong? What does the failure mode look like?

---

## Step 3: Draft Principles

For each tension, write a principle that takes a clear position. Good principles are:
- **Actionable** — someone can tell if they're following it
- **Specific** — it applies to this domain, not all of humanity
- **Directional** — when values conflict, it says which wins

```
PRINCIPLE 1: [Title]
Statement: [One sentence]
Means: [Concrete behavior this requires]
Doesn't mean: [Common misinterpretation]

PRINCIPLE 2: [Title]
Statement: [One sentence]
Means: [Concrete behavior]
Doesn't mean: [Misinterpretation]
...
```

Aim for 5-8 principles. More than 10 and nobody will remember them.

---

## Step 4: Edge Case Testing

Test each principle against hard scenarios. If a principle gives a bad answer, revise it.

| Principle | Edge Case | Result | Revision Needed? |
|-----------|-----------|--------|-------------------|
| [P1] | [Scenario where it's hard to follow] | [What happens] | [Yes/No — fix] |
| [P1] | [Scenario where it conflicts with another principle] | [What happens] | [Yes/No — fix] |
| [P2] | [Hard scenario] | [Result] | [Yes/No] |

For each principle, test at least:
- A case where following it is costly
- A case where it conflicts with another principle
- A case where someone could game it

---

## Step 5: Conflict Resolution Protocol

When principles conflict with each other (they will), establish priority:

```
HIERARCHY:
1. [Highest-priority principle — the one that wins when others conflict]
2. [Second priority]
...

ESCALATION: When principles conflict and priority isn't clear:
- Step 1: [Who decides]
- Step 2: [What information they need]
- Step 3: [How the decision is documented]
```

---

## Step 6: Refine and Format

Produce the final code in a usable format.

```
CODE OF ETHICS: [Entity Name]

PURPOSE: [One sentence on why this code exists]

PRINCIPLES:

1. [TITLE]: [Statement]
   In practice: [What this looks like day-to-day]

2. [TITLE]: [Statement]
   In practice: [What this looks like]

...

WHEN PRINCIPLES CONFLICT: [Brief hierarchy or escalation process]

ENFORCEMENT: [How violations are handled — not punitive, but accountable]

REVIEW: [When and how this code gets updated]
```

---

## Step 7: Stress Test

Final check — does this code survive contact with reality?

- [ ] Can someone new understand it in under 5 minutes?
- [ ] Does it handle the hardest case in this domain?
- [ ] Is there an escape hatch for genuinely unprecedented situations?
- [ ] Does it protect the least powerful person in the system?
- [ ] Would you follow it yourself?

---

## Integration

Use with:
- `/vcl` -> To clarify values before codifying them
- `/eth` -> For deeper ethical analysis on specific tensions
- `/mdr` -> When a specific principle creates a moral dilemma
- `/obv` -> To check if the code is missing obvious failure modes
