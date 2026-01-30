---
name: dmt
description: Create domain-specific skill configurations. Pre-configure skill chains, dimensions, and patterns for specific domains like research, consulting, or engineering.
---

# Domain Template

**Input**: $ARGUMENTS

---

## Purpose

Create a **domain-specific template** that pre-configures:
- Which skills to use and in what order
- Domain-specific dimensions for enumeration
- Common assumptions to check
- Relevant analogy domains
- Standard output formats

Templates accelerate work by encoding domain expertise into reusable configurations.

---

## Template Structure

Every domain template includes:

```yaml
DOMAIN TEMPLATE: [domain name]
version: [1.0]
created: [date]
last_updated: [date]

# What this domain is about
description: |
  [Brief description of the domain and what problems it addresses]

# When to use this template
triggers:
  - [keyword or phrase that indicates this domain]
  - [another trigger]

# Skills to run and in what order
skill_chain:
  - skill: [skill_name]
    config: [any domain-specific config]
  - skill: [skill_name]
    config: [any domain-specific config]

# Pre-defined dimensions for this domain
dimensions:
  - name: [dimension name]
    values: [list of common values]
  - name: [dimension name]
    values: [list of common values]

# Common assumptions to always check
default_assumptions:
  - [assumption that's often hidden in this domain]
  - [another common assumption]

# Domains that provide useful analogies
analogy_domains:
  - domain: [domain name]
    why: [why this domain is relevant]
  - domain: [domain name]
    why: [why this domain is relevant]

# Standard output format for this domain
output_format: |
  [Template for how results should be structured]

# Domain-specific vocabulary
vocabulary:
  [term]: [definition in this domain's context]
  [term]: [definition]
```

---

## The Template Creation Process

### Step 1: Domain Analysis

Understand the domain deeply:

```
DOMAIN ANALYSIS: [domain name]

CORE ACTIVITIES:
What do practitioners in this domain actually do?
1. [Activity 1]
2. [Activity 2]
3. [Activity 3]

KEY DECISIONS:
What decisions do they make?
1. [Decision type 1]
2. [Decision type 2]

COMMON PROBLEMS:
What problems do they face?
1. [Problem 1]
2. [Problem 2]

SUCCESS CRITERIA:
How is success measured?
1. [Metric/criteria 1]
2. [Metric/criteria 2]

FAILURE MODES:
How do things typically go wrong?
1. [Failure mode 1]
2. [Failure mode 2]
```

---

### Step 2: Identify Domain Dimensions

What are the key dimensions for enumeration in this domain?

```
DOMAIN DIMENSIONS: [domain name]

| Dimension | Values | Why Important |
|-----------|--------|---------------|
| [Dim 1] | [v1, v2, v3...] | [why this matters] |
| [Dim 2] | [v1, v2, v3...] | [why this matters] |
| [Dim 3] | [v1, v2, v3...] | [why this matters] |

DIMENSION RELATIONSHIPS:
- [Dim 1] often constrains [Dim 2]
- [Dim 3] is independent of others

PRIMARY DIMENSION: [which dimension is most important]
```

---

### Step 3: Map Domain Assumptions

What assumptions are commonly hidden in this domain?

```
DOMAIN ASSUMPTIONS: [domain name]

ALWAYS CHECK (common blind spots):
1. [Assumption] - Type: [causal/existence/etc.]
   Why hidden: [why people miss this]

2. [Assumption] - Type: [type]
   Why hidden: [why people miss this]

DOMAIN-SPECIFIC ASSUMPTIONS:
1. [Assumption unique to this domain]
2. [Another domain-specific assumption]

ASSUMPTION CLUSTERS:
- [Theme]: [list of related assumptions]
- [Theme]: [list of related assumptions]
```

---

### Step 4: Select Analogy Domains

Which other domains provide useful perspectives?

```
ANALOGY MAPPING: [domain name]

| Source Domain | Structural Match | Key Insights Available |
|---------------|------------------|------------------------|
| [Domain 1] | [what matches] | [what we can learn] |
| [Domain 2] | [what matches] | [what we can learn] |
| [Domain 3] | [what matches] | [what we can learn] |

PRIMARY ANALOGIES (most useful):
1. [Domain]: [why especially relevant]
2. [Domain]: [why especially relevant]

ANTI-ANALOGIES (misleading):
1. [Domain]: [why it seems relevant but isn't]
```

---

### Step 5: Design Skill Chain

What skills should run, in what order?

```
SKILL CHAIN: [domain name]

STANDARD WORKFLOW:

Phase 1: Understanding
|-- /dimension_discovery (if dimensions unknown)
|-- /assumption_extraction

Phase 2: Exploration
|-- /space_enumeration
|-- /assumption_inversion
|-- /cross_domain_analogy (with pre-selected domains)

Phase 3: Validation
|-- /mece_validation
|-- /dependency_extraction (if procedural)
|-- /procedure_validation (if procedural)

Phase 4: Synthesis
|-- /insight_synthesis

SKIP CONDITIONS:
- Skip /dimension_discovery if: [condition]
- Skip /dependency_extraction if: [condition]

DOMAIN-SPECIFIC ADDITIONS:
- Add [skill] when: [condition]
```

---

### Step 6: Define Output Format

What should the final output look like?

```
OUTPUT FORMAT: [domain name]

STANDARD SECTIONS:
1. [Section 1 name]
   - [What goes here]
   - [Format requirements]

2. [Section 2 name]
   - [What goes here]
   - [Format requirements]

REQUIRED ELEMENTS:
- [ ] [Element that must be present]
- [ ] [Another required element]

OPTIONAL SECTIONS:
- [Section]: Include when [condition]

EXAMPLE OUTPUT:
[Minimal example of well-formatted output]
```

---

### Step 7: Compile Template

```
===================================================
DOMAIN TEMPLATE: [domain name]
===================================================
version: 1.0
created: [date]

DESCRIPTION:
[What this domain covers and when to use this template]

TRIGGERS:
- [keyword/phrase]
- [keyword/phrase]
- [keyword/phrase]

===================================================

SKILL CHAIN:
1. /[skill] - [purpose in this domain]
2. /[skill] - [purpose in this domain]
3. /[skill] - [purpose in this domain]
...

===================================================

DIMENSIONS:
1. [Dimension]: [values]
2. [Dimension]: [values]
3. [Dimension]: [values]

===================================================

DEFAULT ASSUMPTIONS TO CHECK:
- [Assumption 1]
- [Assumption 2]
- [Assumption 3]

===================================================

ANALOGY DOMAINS:
- [Domain 1]: [why relevant]
- [Domain 2]: [why relevant]

===================================================

OUTPUT FORMAT:
[Template structure]

===================================================

VOCABULARY:
- [Term]: [domain-specific meaning]
- [Term]: [domain-specific meaning]

===================================================

USAGE:
To apply this template:
1. [Step 1]
2. [Step 2]
3. [Step 3]

===================================================
```

---

## Example: Research Domain Template

```
===================================================
DOMAIN TEMPLATE: Academic Research
===================================================
version: 1.0
created: 2026-01-28

DESCRIPTION:
For academic research projects: literature reviews, hypothesis
generation, methodology design, and research synthesis.

TRIGGERS:
- "research question"
- "literature review"
- "hypothesis"
- "methodology"
- "academic paper"

===================================================

SKILL CHAIN:
1. /assumption_extraction - Surface hidden research assumptions
2. /dimension_discovery - Identify research dimensions
3. /space_enumeration - Map the research space
4. /cross_domain_analogy - Find methodological analogies
5. /mece_validation - Ensure complete coverage
6. /insight_synthesis - Generate research insights

===================================================

DIMENSIONS:
1. Methodology: [quantitative, qualitative, mixed, theoretical]
2. Scope: [case study, comparative, longitudinal, cross-sectional]
3. Data source: [primary, secondary, archival, experimental]
4. Analysis: [statistical, thematic, content, discourse]
5. Contribution: [empirical, theoretical, methodological, practical]

===================================================

DEFAULT ASSUMPTIONS TO CHECK:
- The research question is novel
- Data is accessible and sufficient
- Methodology matches research question
- Results will be publishable
- Timeline is realistic
- Ethics approval obtainable

===================================================

ANALOGY DOMAINS:
- Medicine: Rigorous methodology, peer review, evidence standards
- Law: Argument construction, precedent, burden of proof
- Engineering: Systematic problem-solving, validation

===================================================

OUTPUT FORMAT:
1. Research Question (refined)
2. Key Assumptions (with validity assessment)
3. Methodology Options (with trade-offs)
4. Gap Analysis (what's missing in literature)
5. Recommended Approach (with rationale)

===================================================
```

---

## Quality Checklist

Before completing template:
- [ ] Domain thoroughly analyzed
- [ ] Dimensions identified and validated
- [ ] Common assumptions documented
- [ ] Analogy domains selected and justified
- [ ] Skill chain designed with skip conditions
- [ ] Output format specified
- [ ] Template compiled in standard structure
- [ ] Example output provided
- [ ] Triggers defined for activation

---

## Integration

Use with:
- `/template_registry` - Register and retrieve templates
- `/template_maintenance` - Update templates based on usage
- All skills in the template's skill chain
