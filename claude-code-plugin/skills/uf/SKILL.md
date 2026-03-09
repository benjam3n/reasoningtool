---
name: "uf - Useful For"
description: "Given a skill or method, map its best-fit use cases, failure conditions, limits, and alternative skills with explicit switch conditions."
---

# UF - Useful For

**Input**: $ARGUMENTS

---

## Core Principles

1. **Every tool has a sweet spot.** A skill that's excellent for one situation is mediocre for another. The sweet spot isn't "what it can do" — it's "what it does BETTER than alternatives."

2. **Failure cases are more useful than success cases.** Knowing when a skill works is helpful. Knowing when it FAILS is essential — it prevents wasted effort and wrong-tool choices.

3. **Alternatives exist for every skill.** No skill is the only option. For every use case, there are 2-3 alternative skills that could work. The switch condition — "use X instead when Y" — is the most actionable output.

4. **Limits are not failures.** A skill that handles 3-person decisions but not 30-person decisions isn't failing — it has a scope limit. Limits define the boundary of appropriate use.

5. **Use cases are typed.** "Useful for decisions" is too vague. WHAT KIND of decisions? Binary vs multi-option, reversible vs irreversible, urgent vs deliberate. Specificity makes the mapping actionable.

---

## Phase 1: Target Identification

```
[U1] TARGET: [skill id or method name]
[U2] DESCRIPTION: [what this skill/method does — from SKILL.md or user description]
[U3] CORE_FUNCTION: [the ONE thing this skill does better than anything else]
[U4] INPUT_TYPE: [what it takes as input]
[U5] OUTPUT_TYPE: [what it produces]
```

If the target is a skill: read its SKILL.md to understand its actual mechanics.
If the target is a method/framework: describe its core operation.

---

## Phase 2: Best-Fit Use Cases

Map the situations where this skill is the RIGHT choice:

```
[U-N] USE_CASE: [specific situation]
  WHY_THIS_SKILL: [what makes this skill better than alternatives for this case]
  EXAMPLE: [concrete example of this use case]
  FIT: [excellent | good]
```

### Use Case Dimensions

For each use case, specify:
- **Input type**: What kind of input makes this skill shine
- **Complexity**: Simple vs complex problems
- **Urgency**: Quick decisions vs deep deliberation
- **Certainty**: How much is known when invoked
- **Scale**: Small vs large scope

---

## Phase 3: Failure Cases and Limits

### Failure Cases (skill produces bad output)

```
[U-N] FAILURE: [situation where this skill fails]
  WHY_FAILS: [what about this situation breaks the skill's assumptions]
  SIGNAL: [how you'd know you're in a failure case]
  INSTEAD: /[alternative-id] — [why the alternative works here]
```

### Limits (skill works but suboptimally)

```
[U-N] LIMIT: [boundary of effective use]
  WHAT_HAPPENS: [how performance degrades past this limit]
  THRESHOLD: [where approximately the limit is]
  WORKAROUND: [how to extend past the limit, if possible]
```

### Anti-Patterns (common misuses)

```
[U-N] ANTI_PATTERN: [common wrong application]
  WHY_TEMPTING: [why people try this]
  WHY_WRONG: [why it doesn't work]
  INSTEAD: /[alternative-id]
```

---

## Phase 4: Alternative Mapping

For each use case, identify what ELSE could work:

```
[U-N] ALTERNATIVE: /[skill-id] — [name]
  OVERLAPS_ON: [which use cases both skills handle]
  USE_THIS_WHEN: [specific condition favoring the target skill]
  USE_ALTERNATIVE_WHEN: [specific condition favoring the alternative]
  KEY_DIFFERENCE: [the fundamental distinction]
```

### Switch Conditions

The most actionable output — explicit "if X then use Y":

```
[U-N] SWITCH CONDITIONS:
  USE /target WHEN: [condition 1], [condition 2]
  USE /alt-1 INSTEAD WHEN: [condition]
  USE /alt-2 INSTEAD WHEN: [condition]
  USE /alt-3 INSTEAD WHEN: [condition]
```

---

## Phase 5: Output

```
USEFUL FOR
==========

TARGET: /[id] — [name]
CORE FUNCTION: [one sentence]

BEST FIT (use this skill when):
  1. [use case] — WHY: [what makes this the right choice]
  2. [use case] — WHY: [reason]
  3. [use case] — WHY: [reason]

FAILURE CASES (don't use when):
  1. [situation] — USE INSTEAD: /[alt] — WHY: [reason]
  2. [situation] — USE INSTEAD: /[alt] — WHY: [reason]

LIMITS:
  1. [limit] — DEGRADES AT: [threshold]
  2. [limit] — DEGRADES AT: [threshold]

SWITCH CONDITIONS:
  USE /target WHEN: [conditions]
  USE /alt-1 INSTEAD WHEN: [condition]
  USE /alt-2 INSTEAD WHEN: [condition]

ANTI-PATTERNS:
  1. [common misuse] — USE INSTEAD: /[alt]

READY FOR:
- /cmp /target vs /alt — to compare specific alternatives
- /dtse [function] — to find other skills in this space
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Only success cases** | No failure cases or limits listed | Every skill has failure cases. Find at least 2 |
| **Vague use cases** | "Good for decisions" without specificity | Which kind of decisions? Under what conditions? |
| **No alternatives** | Skill presented as the only option | Every skill has 2-3 alternatives. Find them |
| **No switch conditions** | Alternatives listed without "when to switch" | The whole point is knowing WHEN to use each |
| **Title-based analysis** | Assessment based on skill name, not actual SKILL.md content | Read the actual skill before mapping |
| **All positive** | No anti-patterns or limits identified | Users misuse every skill. Find the common misuses |

---

## Depth Scaling

| Depth | Min Use Cases | Min Failure Cases | Min Alternatives | Switch Conditions |
|-------|--------------|------------------|-----------------|------------------|
| 1x | 3 | 1 | 2 | 1 |
| 2x | 5 | 3 | 3 | 3 |
| 4x | 8 | 5 | 5 | 5 |
| 8x | 12 | 8 | 8 | All pairs |

Default: 2x. These are floors.

---

## Pre-Completion Checklist

- [ ] Target skill read/understood (not just named)
- [ ] Core function stated in one sentence
- [ ] Best-fit use cases are specific (not "good for analysis")
- [ ] Failure cases identified with alternative routing
- [ ] Limits specified with thresholds
- [ ] Anti-patterns identified (common misuses)
- [ ] Alternatives mapped with explicit switch conditions
- [ ] Switch conditions are actionable ("when X, use Y")

---

## Integration

- Use from: `/dtse` (after finding a skill, understand its applicability)
- Complementary: `/cmp` (compare specific alternatives in depth)
- Complementary: `/dtse` (find a skill, then /uf to understand it)
- Differs from `/dtse`: dtse finds skills; uf analyzes a specific skill's applicability
- Differs from `/cmp`: cmp compares options; uf maps one skill's full territory
