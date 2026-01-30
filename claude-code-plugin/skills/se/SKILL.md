---
name: se
description: Generate comprehensive lists by systematically covering all dimensions. Ensures nothing is missed through structured enumeration.
---

# Space Enumeration

**Input**: $ARGUMENTS

---

## Purpose

Generate a **comprehensive list** by systematically covering all dimensions of a problem space. This ensures nothing is missed.

**Prerequisites**:
- Dimensions identified (use `/dimension_discovery` if unknown)
- Granularity level specified

---

## Granularity Levels

Before enumeration, specify the desired granularity:

| Level | Description | When to Use |
|-------|-------------|-------------|
| **EXHAUSTIVE** | Every combination | Small spaces (<100), formal specs |
| **REPRESENTATIVE** | Key examples per dimension | Medium spaces (100-1000) |
| **TOP-N** | Most important N items | Large spaces, quick overview |
| **DIMENSION-ONLY** | Just list dimensions and values | Very large spaces, framework |

---

## The Process

### Step 1: Confirm Dimensions

List the dimensions you'll enumerate across:

```
DIMENSIONS FOR: [topic]

1. [Dimension 1]: [value1, value2, value3, ...]
2. [Dimension 2]: [value1, value2, value3, ...]
3. [Dimension 3]: [value1, value2, value3, ...]

TOTAL SPACE: [N1] × [N2] × [N3] = [Total] combinations
GRANULARITY: [EXHAUSTIVE / REPRESENTATIVE / TOP-N / DIMENSION-ONLY]
```

---

### Step 2: Choose Enumeration Strategy

Based on granularity and space size:

| Space Size | Strategy |
|------------|----------|
| < 50 | Full Cartesian product |
| 50-500 | Dimension-by-dimension with pruning |
| 500-5000 | Representative sampling per dimension |
| > 5000 | Hierarchical (top-level dimensions, then drill down) |

---

### Step 3A: Full Enumeration (Small Spaces)

For EXHAUSTIVE on small spaces, enumerate all combinations:

```
FULL ENUMERATION: [topic]

| # | Dim1 | Dim2 | Dim3 | Description |
|---|------|------|------|-------------|
| 1 | v1 | v1 | v1 | [what this combination means] |
| 2 | v1 | v1 | v2 | [what this combination means] |
| 3 | v1 | v2 | v1 | [what this combination means] |
...
```

**Pruning**: Mark combinations that don't make sense as N/A:
```
| 4 | v1 | v2 | v2 | N/A - [reason this combination is invalid] |
```

---

### Step 3B: Dimension-by-Dimension (Medium Spaces)

For REPRESENTATIVE on medium spaces:

```
DIMENSION-BY-DIMENSION: [topic]

## Dimension 1: [name]
For each value, list key items:

### [Value 1]
- [Item 1.1]
- [Item 1.2]
- [Item 1.3]

### [Value 2]
- [Item 2.1]
- [Item 2.2]

[Continue for all dimensions]
```

---

### Step 3C: Hierarchical (Large Spaces)

For TOP-N on large spaces:

```
HIERARCHICAL ENUMERATION: [topic]

## Level 1: [Primary Dimension]

### [Category 1]
Top items:
1. [Most important]
2. [Second most]
3. [Third most]

### [Category 2]
Top items:
1. [Most important]
...

## Level 2: Drill-down on [specific area]
[More detailed enumeration of one branch]
```

---

### Step 4: Cross-Dimensional Check

After initial enumeration, check for items that span dimensions:

```
CROSS-DIMENSIONAL ITEMS:
- [Item X] spans [Dim1:value] AND [Dim2:value] - classify under: [primary]
- [Item Y] doesn't fit any dimension - add to "Other" category
```

---

### Step 5: Gap Check

Verify no dimension is under-represented:

```
COVERAGE CHECK:

| Dimension | Values | Items per Value | Gap? |
|-----------|--------|-----------------|------|
| [Dim 1] | 5 | 3, 4, 2, 5, 3 | No |
| [Dim 2] | 3 | 8, 2, 1 | Yes - [value 3] under-covered |

ACTION: Add items for [Dim 2, value 3]
```

---

### Step 6: Organize Output

Choose organization by:
- **By dimension** (good for reference)
- **By priority** (good for action)
- **By relationship** (good for understanding)
- **Alphabetical** (good for lookup)

```
COMPREHENSIVE LIST: [topic]
Organization: [chosen method]

[Organized list with clear structure]

---
METADATA:
- Total items: [N]
- Dimensions covered: [list]
- Granularity: [level]
- Gaps identified: [any]
- Items in "Other": [N]
```

---

## Example: Software Requirements Types

**Input**: Enumerate all types of requirements for a software project

### Step 1: Dimensions
1. **Stakeholder**: End user, Admin, Developer, Operator, Business
2. **Type**: Functional, Non-functional, Constraint, Assumption
3. **Priority**: Must have, Should have, Could have, Won't have

TOTAL: 5 × 4 × 4 = 80 combinations
GRANULARITY: REPRESENTATIVE

### Step 2: Strategy
Dimension-by-dimension with representative items

### Step 3: Enumeration

## By Type

### Functional Requirements
- **End user**: Login, search, purchase, view history
- **Admin**: User management, content moderation, reporting
- **Developer**: API access, webhook integration, SDK usage
- **Operator**: Deployment, monitoring, backup, scaling
- **Business**: Revenue tracking, conversion analytics

### Non-Functional Requirements
- **Performance**: Response time < 200ms, 1000 concurrent users
- **Security**: Encryption, authentication, audit logging
- **Reliability**: 99.9% uptime, automated failover
- **Usability**: Accessibility WCAG 2.1, mobile responsive
- **Maintainability**: Code coverage > 80%, documentation

### Constraints
- **Technical**: Must use PostgreSQL, must run on AWS
- **Regulatory**: GDPR compliance, SOC2 certification
- **Business**: Launch by Q3, budget under $500k

### Assumptions
- Users have modern browsers
- Internet connectivity available
- English language primary

### Step 4-5: Checks
All dimensions covered. No major gaps.

### Step 6: Output
[Organized list as shown above]

---

## Quality Checklist

Before completing:
- [ ] Dimensions confirmed or discovered
- [ ] Granularity level specified
- [ ] Appropriate strategy chosen for space size
- [ ] All dimensions represented
- [ ] Cross-dimensional items handled
- [ ] Gap check completed
- [ ] Output organized clearly
- [ ] Metadata included

---

## Next Steps

After enumeration:
1. Use `/mece_validation` to verify MECE-ness
2. Use `/dependency_extraction` if items have dependencies
3. Use `/topological_ordering` if items need sequencing
