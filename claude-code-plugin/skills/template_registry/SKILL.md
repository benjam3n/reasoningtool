---
name: template_registry
description: Registry for domain templates. Store, retrieve, search, and manage domain-specific configurations.
---

# Template Registry

**Input**: $ARGUMENTS

---

## Purpose

Manage domain templates:
- **Store** new templates
- **Retrieve** templates by name or trigger
- **Search** templates by keyword
- **List** available templates
- **Compare** templates for overlap

---

## Registry Operations

### STORE: Add New Template

```
REGISTRY STORE: [template name]

Template:
[Full template content from /domain_template]

VALIDATION:
- [ ] Has required sections (description, triggers, skill_chain, dimensions)
- [ ] Triggers don't conflict with existing templates
- [ ] Skill chain references valid skills
- [ ] Version number present

STORE RESULT:
Status: [STORED / VALIDATION_FAILED / CONFLICT]
Location: templates/[domain_name].yaml
Conflicts: [any trigger conflicts with existing templates]
```

---

### RETRIEVE: Get Template by Name

```
REGISTRY RETRIEVE: [template name]

SEARCH:
Looking for template: [name]

RESULT:
Status: [FOUND / NOT_FOUND / MULTIPLE_MATCHES]

If FOUND:
[Full template content]

If MULTIPLE_MATCHES:
Candidates:
1. [Template 1] - [brief description]
2. [Template 2] - [brief description]
Select one to retrieve.
```

---

### MATCH: Find Template by Trigger

```
REGISTRY MATCH: [user input]

INPUT: "[user's input text]"

TRIGGER SCAN:
| Template | Trigger Match | Score |
|----------|---------------|-------|
| [Template 1] | [matching trigger] | [0-100] |
| [Template 2] | [matching trigger] | [0-100] |
| [Template 3] | [no match] | 0 |

BEST MATCH:
Template: [name]
Trigger: [which trigger matched]
Confidence: [HIGH/MEDIUM/LOW]

RECOMMENDATION:
[Apply template X / No clear match - ask user / Multiple candidates]
```

---

### LIST: Show All Templates

```
REGISTRY LIST

AVAILABLE TEMPLATES:

| # | Template | Domain | Skills | Last Updated |
|---|----------|--------|--------|--------------|
| 1 | [name] | [domain] | [count] | [date] |
| 2 | [name] | [domain] | [count] | [date] |
| 3 | [name] | [domain] | [count] | [date] |

TOTAL: [N] templates

BY CATEGORY:
- Research: [list]
- Business: [list]
- Technical: [list]
- Creative: [list]
- Other: [list]
```

---

### SEARCH: Find Templates by Keyword

```
REGISTRY SEARCH: [keyword]

SEARCHING FOR: "[keyword]"

MATCHES:

In triggers:
- [Template 1]: trigger "[matching trigger]"
- [Template 2]: trigger "[matching trigger]"

In dimensions:
- [Template 3]: dimension "[matching dimension]"

In description:
- [Template 4]: "[matching text snippet]"

In assumptions:
- [Template 5]: assumption "[matching assumption]"

TOTAL MATCHES: [N]

MOST RELEVANT:
1. [Template] - [why relevant]
2. [Template] - [why relevant]
```

---

### COMPARE: Check Template Overlap

```
REGISTRY COMPARE: [template A] vs [template B]

COMPARING:
- Template A: [name]
- Template B: [name]

OVERLAP ANALYSIS:

Triggers:
| Template A | Template B | Overlap? |
|------------|------------|----------|
| [trigger] | [trigger] | [Yes/No] |

Dimensions:
| Dimension | In A? | In B? | Shared? |
|-----------|-------|-------|---------|
| [dim] | [Y/N] | [Y/N] | [Y/N] |

Skills:
| Skill | In A? | In B? | Order |
|-------|-------|-------|-------|
| [skill] | [Y/N] | [Y/N] | [A:1, B:2] |

Assumptions:
- Shared: [list]
- Only in A: [list]
- Only in B: [list]

OVERLAP SCORE: [0-100%]

RECOMMENDATION:
[Merge templates / Keep separate / One subsumes other]
```

---

### DELETE: Remove Template

```
REGISTRY DELETE: [template name]

DELETING: [template name]

PRE-DELETE CHECK:
- Template exists: [Yes/No]
- Dependencies: [list any templates that reference this one]
- Usage stats: [how often used, if tracked]

CONFIRMATION REQUIRED:
Type "CONFIRM DELETE [template name]" to proceed.

DELETE RESULT:
Status: [DELETED / CANCELLED / NOT_FOUND]
```

---

### UPDATE: Modify Existing Template

```
REGISTRY UPDATE: [template name]

CURRENT VERSION: [version number]

CHANGES:
[Specify what to change]

UPDATED FIELDS:
- [Field 1]: [old value] -> [new value]
- [Field 2]: [old value] -> [new value]

NEW VERSION: [incremented version]

VALIDATION:
- [ ] Changes don't break skill chain
- [ ] Triggers still unique
- [ ] Version incremented

UPDATE RESULT:
Status: [UPDATED / VALIDATION_FAILED]
```

---

## Registry Storage Format

Templates are stored as YAML files:

```
templates/
|-- index.yaml           # Registry index
|-- research/
|   |-- academic.yaml
|   |-- market.yaml
|-- business/
|   |-- consulting.yaml
|   |-- strategy.yaml
|-- technical/
|   |-- software.yaml
|   |-- data_science.yaml
|-- creative/
    |-- writing.yaml
    |-- design.yaml
```

### Index File Structure

```yaml
# templates/index.yaml
version: 1.0
last_updated: [date]
total_templates: [N]

templates:
  - name: academic_research
    path: research/academic.yaml
    triggers: [research, literature, hypothesis]
    version: 1.2

  - name: consulting
    path: business/consulting.yaml
    triggers: [client, engagement, deliverable]
    version: 1.0

trigger_map:
  research: academic_research
  literature: academic_research
  hypothesis: academic_research
  client: consulting
  engagement: consulting
```

---

## Quick Operations

### Quick Match
```
QUICK MATCH: [input]

Best template: [name] ([confidence]%)
Apply with: /apply_template [name]
```

### Quick List
```
QUICK LIST

Templates: [name1], [name2], [name3], ...
Total: [N]
```

---

## Example Session

```
User: I need to do a literature review on machine learning fairness

REGISTRY MATCH: "literature review on machine learning fairness"

TRIGGER SCAN:
| Template | Trigger Match | Score |
|----------|---------------|-------|
| academic_research | "literature review" | 95 |
| data_science | "machine learning" | 60 |
| technical_writing | no match | 0 |

BEST MATCH:
Template: academic_research
Trigger: "literature review"
Confidence: HIGH

RECOMMENDATION:
Apply academic_research template. This will:
1. Extract research assumptions
2. Discover relevant dimensions (methodology, scope, etc.)
3. Enumerate the research space
4. Find methodological analogies
5. Validate MECE coverage
6. Synthesize insights

Proceed? [Yes/No/Show template first]
```

---

## Quality Checklist

Before completing registry operation:
- [ ] Operation type identified (STORE/RETRIEVE/MATCH/etc.)
- [ ] Validation performed where applicable
- [ ] Results clearly formatted
- [ ] Recommendations provided
- [ ] Next steps indicated

---

## Integration

Use with:
- `/domain_template` - Create templates to store
- `/template_maintenance` - Keep templates updated
- All skills referenced in templates
