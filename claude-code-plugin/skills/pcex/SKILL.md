---
name: "pcex - Extract and Generalize Procedures"
description: "After completing a goal, extract reusable procedures and generalize them for storage in the library, enabling GOSM to learn from completed work."
---

# Extract and Generalize Procedures

## Overview
After completing a goal, extract reusable procedures and generalize them for storage in the library, enabling GOSM to learn from completed work.

## Steps

### Step 1: Review project phases
Go through each phase in COMPLETE_PLAN.md and identify:

1. What procedure was followed for each phase?
   - Was it an existing library procedure?
   - Was it ad-hoc / invented for this project?
   - Was it adapted from something else?

2. Rate each procedure for extraction potential:
   - Was it structured (clear steps) or intuitive?
   - Could it apply to other projects?
   - Did it produce good results?

3. Note any novel approaches:
   - What was done differently than usual?
   - What worked surprisingly well?
   - What workarounds became standard practice?

Create candidate list with context for each.

### Step 2: Review custom gates
Check the gates/ folder for custom or adapted gates:

1. Identify any gates created for this project:
   - What checks were performed?
   - Were they project-specific or general?
   - Could they apply to other projects?

2. Note gates that were particularly valuable:
   - Which gates caught real issues?
   - Which gates would have helped earlier?
   - Which gates could become standard?

3. Add valuable gates to candidate list

Gates often contain implicit procedures (the process of evaluation).

### Step 3: Score candidates
For each candidate procedure or gate, score 1-5 on:

GENERALIZABILITY (weight: 0.3)
- Could this apply to other projects?
- 5: Universal - applies across many domains
- 3: Moderate - applies within a domain
- 1: Specific - only this project type

VALUE (weight: 0.3)
- How much effort does this save?
- 5: Major - saves days/weeks of work
- 3: Moderate - saves hours
- 1: Minor - saves minutes

COMPLETENESS (weight: 0.2)
- How well is it documented?
- 5: Fully documented with examples
- 3: Key steps clear, some gaps
- 1: Mostly implicit knowledge

ABSTRACTION POTENTIAL (weight: 0.2)
- Can specifics be removed without losing value?
- 5: Easy to parameterize
- 3: Some specifics can be abstracted
- 1: Heavily dependent on specifics

Calculate weighted average. Extract if >= 3.0

### Step 4: Identify specific elements
For each procedure to extract, identify project-specific elements:

1. List all project-specific references:
   - Named entities (people, products, companies)
   - Domain-specific terminology
   - Hardcoded values or thresholds
   - Specific tools or technologies

2. Map specifics to parameter names:

   Project-specific → Parameter
   ---------------------------------
   "atheism" → {topic}
   "philosophy" → {domain}
   "theist responses" → {counterposition}
   "10 interviews" → {sample_size}
   "3 weeks" → {duration}

3. Note which specifics are truly variable vs. essential:
   - Some specifics are examples, not requirements
   - Some are constraints that should remain

### Step 5: Create parameters
Define formal parameters for the generalized procedure:

For each identified specific element, create parameter definition:

```yaml
parameters:
  - name: topic
    description: "The subject being analyzed"
    type: string
    required: true
    example: "climate change"

  - name: domain
    description: "The field or area of focus"
    type: string
    required: false
    default: "general"

  - name: sample_size
    description: "Number of items to collect"
    type: integer
    required: false
    default: 10
    constraints:
      min: 5
      max: 100
```

Parameters should be:
- Clearly named (what it represents)
- Typed (string, integer, list, etc.)
- Required or optional with defaults
- Constrained where appropriate

### Step 6: Generalize steps
Rewrite each step using parameters:

BEFORE (project-specific):
"Research atheist philosophical arguments from academic sources"

AFTER (generalized):
"Research arguments supporting {position} on {topic} from {source_type} sources"

Generalization principles:
1. Replace specific nouns with parameters
2. Keep action verbs unchanged
3. Preserve structure and sequence
4. Maintain clarity - generalized should be as clear as specific
5. Add notes for context where helpful

Check that generalized steps are still actionable:
- Would someone know what to do?
- Is it clear what the output should be?
- Are there hidden dependencies?

### Step 7: Document applicability
Define when this procedure should be used:

```yaml
when_to_use:
  - "When creating persuasive content on any topic"
  - "When analyzing competing positions"
  - "When building argumentative documents"

when_not_to_use:
  - "For purely descriptive content"
  - "When positions are not in contention"
  - "For technical documentation"

applicability:
  domains:
    - "philosophical analysis"
    - "policy arguments"
    - "competitive analysis"

  goal_types:
    - "argumentative document"
    - "position paper"
    - "debate preparation"

  triggers:
    - "when asked to argue for a position"
    - "when comparing competing options"
```

Be specific enough to help with procedure discovery,
but not so narrow that it's rarely triggered.

### Step 8: Add examples
Create 2-3 concrete instantiations showing the procedure in use:

```yaml
examples:
  - name: "Climate policy analysis"
    context: "Analyzing carbon tax proposal"
    parameters:
      topic: "climate change policy"
      position: "carbon tax"
      counterposition: "market-only solutions"
      domain: "environmental economics"
    expected_output: "Position paper with counterargument analysis"

  - name: "Database selection"
    context: "Choosing database for new application"
    parameters:
      topic: "database selection"
      position: "PostgreSQL"
      counterposition: "MongoDB"
      domain: "software architecture"
    expected_output: "Technical comparison with recommendation"
```

Examples should:
- Cover different domains to show generalizability
- Include realistic parameter values
- Show expected outputs
- Be different from the source project

### Step 9: Write to library
Create procedure file in library:

1. Determine correct location:
   - library/procedures/extracted/{domain}/{procedure_id}.yaml
   - Domain should match procedure's primary domain

2. Use standard procedure template format with all sections:
   - id, name, version, domain, description
   - long_description
   - tags
   - when_to_use, when_not_to_use
   - inputs, outputs
   - steps (with id, name, action, inputs, outputs, verification)
   - verification
   - failure_modes
   - examples
   - gosm_integration

3. Add source attribution:
   ```yaml
   source:
     project: "{project_name}"
     extracted_date: "{date}"
     original_context: "{brief description}"
   ```

4. Validate YAML syntax before saving

### Step 10: Update index
Add new procedure to library indexes:

1. Update library/INDEX.md:
   - Add to "Extracted Procedures" section
   - Include procedure ID, name, purpose, source

2. Update library/procedures/extracted/EXTRACTED_PROCEDURES_INDEX.md:
   - Add entry with full details

3. Update domain-specific index if exists:
   - E.g., library/procedures/extracted/{domain}/INDEX.md

Format for INDEX.md:
| Procedure ID | Name | Purpose | Source |
|--------------|------|---------|--------|
| {id} | {name} | {purpose} | {source_project} |

### Step 11: Tag source project
Update the source project to record what was extracted:

1. Update project's context.json or metadata:
   ```json
   {
     "extracted_procedures": [
       "{procedure_id_1}",
       "{procedure_id_2}"
     ],
     "extraction_date": "YYYY-MM-DD"
   }
   ```

2. Update project's LEARNINGS.md:
   - Note which procedures were extracted
   - Link to library locations

3. This creates traceability:
   - Can find procedures by source project
   - Can find projects that contributed to library


## When to Use
- After completing any project successfully
- When novel approaches were developed during a project
- When existing procedures were significantly adapted
- During project retrospectives
- When a repeatable pattern emerges across projects
- When asked "how did you do that?" and realizing others could benefit
- Before archiving a completed project
- When noticing similar work being done repeatedly

## Verification
- Procedure is genuinely reusable (not just project-specific with placeholders)
- Parameters are clearly defined with types and constraints
- Steps are abstract but remain actionable
- Applicability is well-defined and specific
- Examples demonstrate usage across domains
- Library location is correct for the domain
- Index is updated in all relevant places
- Source project is tagged for traceability

---

**Input**: $ARGUMENTS

Apply this procedure to the input provided.