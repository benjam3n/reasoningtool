---
name: dimension_discovery
description: Identify the key dimensions that define a problem space, enabling comprehensive enumeration. Use before space_enumeration for novel domains.
---

# Dimension Discovery

**Input**: $ARGUMENTS

---

## Purpose

Before generating a comprehensive list, you need to know the **dimensions** that define the space. This skill identifies those dimensions for any domain.

**Dimensions** are independent axes of variation. For "types of vehicles":
- Dimension 1: Power source (gas, electric, human, hybrid)
- Dimension 2: Medium (land, water, air, space)
- Dimension 3: Purpose (personal, commercial, military, recreational)

With dimensions identified, `/space_enumeration` can systematically cover the space.

---

## When to Use

| Situation | Use This Skill |
|-----------|----------------|
| Novel domain with no known structure | YES |
| Generating comprehensive list | YES (before `/space_enumeration`) |
| Domain structure already known | SKIP (use known dimensions directly) |
| Simple enumeration | SKIP (overkill) |

---

## The Process

### Step 1: Seed with Examples

Start with 5-10 concrete examples of what you're trying to enumerate.

```
EXAMPLES FOR: [domain]
1. [example 1]
2. [example 2]
3. [example 3]
...
```

**Why examples first?** Dimensions emerge from comparing examples.

---

### Step 2: Compare for Differences

For each pair of examples, ask: "What makes these different?"

```
COMPARING: [example A] vs [example B]
Differences:
- [difference 1] -> Potential dimension: [name]
- [difference 2] -> Potential dimension: [name]
```

---

### Step 3: Apply Universal Dimensions

Check these universal dimensions (apply to almost any domain):

| Dimension | Question | Example Values |
|-----------|----------|----------------|
| **WHO** | Who is involved? | Individual, team, organization, society |
| **WHAT** | What type/category? | Domain-specific types |
| **WHEN** | What time frame? | Immediate, short-term, long-term, recurring |
| **WHERE** | What location/context? | Local, regional, global, virtual |
| **WHY** | What purpose/goal? | Primary, secondary, indirect |
| **HOW** | What method/approach? | Manual, automated, hybrid |
| **HOW MUCH** | What scale/degree? | Small, medium, large, extreme |

For each: Does this dimension create meaningful variation in [domain]?

---

### Step 4: Identify Domain-Specific Dimensions

Beyond universal dimensions, what's unique to this domain?

```
DOMAIN-SPECIFIC DIMENSIONS FOR: [domain]

1. [Dimension name]
   - What it captures: [explanation]
   - Possible values: [value1, value2, value3, ...]
   - Why it matters: [importance]

2. [Dimension name]
   ...
```

---

### Step 5: Validate Independence

Dimensions should be **independent** (not redundant):

```
INDEPENDENCE CHECK:
- Can [Dimension A] vary while [Dimension B] stays constant?
- If NO -> Dimensions may be correlated, consider merging
- If YES -> Dimensions are independent, keep both
```

---

### Step 6: Validate Completeness

Do the dimensions cover the examples?

```
COMPLETENESS CHECK:
For each example:
  - [Example 1]: Dim1=[value], Dim2=[value], Dim3=[value] [x]
  - [Example 2]: Dim1=[value], Dim2=[value], Dim3=[value] [x]

Any example that doesn't fit? -> Missing dimension
```

---

### Step 7: Output Dimensions

```
DIMENSIONS DISCOVERED FOR: [domain]

| # | Dimension | Values | Validation |
|---|-----------|--------|------------|
| 1 | [name] | [v1, v2, v3, ...] | Covers examples [x] |
| 2 | [name] | [v1, v2, v3, ...] | Independent [x] |
| 3 | [name] | [v1, v2, v3, ...] | Meaningful variation [x] |

TOTAL SPACE SIZE: [D1 values] × [D2 values] × [D3 values] = [N] combinations

NOTES:
- [Any caveats about dimension interactions]
- [Any "other" category needed for edge cases]
```

---

## Example: Dimensions for "Software Testing Types"

### Step 1: Examples
1. Unit tests
2. Integration tests
3. Load tests
4. Security penetration tests
5. User acceptance tests
6. Regression tests

### Step 2: Compare
- Unit vs Integration -> **Scope** (single unit vs multiple units)
- Load vs Security -> **Focus** (performance vs security)
- User acceptance vs Regression -> **Purpose** (validation vs verification)

### Step 3: Universal Dimensions
- WHO: Developer, QA, User, Automated
- WHEN: Development, Pre-release, Post-release, Continuous
- HOW: Manual, Automated, Hybrid

### Step 4: Domain-Specific
- **Scope**: Unit, Component, Integration, System, End-to-end
- **Focus**: Functional, Performance, Security, Usability, Reliability
- **Automation level**: Manual, Semi-automated, Fully automated

### Step 5-6: Validate
All examples fit. Dimensions are independent.

### Step 7: Output

| # | Dimension | Values |
|---|-----------|--------|
| 1 | Scope | Unit, Component, Integration, System, E2E |
| 2 | Focus | Functional, Performance, Security, Usability, Reliability |
| 3 | Timing | Development, Pre-release, Post-release, Continuous |
| 4 | Automation | Manual, Semi-automated, Fully automated |

TOTAL SPACE: 5 × 5 × 4 × 3 = 300 combinations

---

## Quality Checklist

Before completing:
- [ ] At least 5 seed examples used
- [ ] Universal dimensions checked
- [ ] Domain-specific dimensions identified
- [ ] Independence validated
- [ ] All examples covered by dimensions
- [ ] Space size calculated

---

## Next Steps

After dimension discovery:
1. Use `/space_enumeration` to generate comprehensive list
2. Use `/mece_validation` to verify coverage
