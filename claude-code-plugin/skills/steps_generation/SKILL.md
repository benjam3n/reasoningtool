---
name: steps_generation
description: "Transform a COMPLETE_PLAN into foolproof executable step-by-step instructions"
---

# Steps Generation

## Overview
Transform a COMPLETE_PLAN into foolproof executable step-by-step instructions

## Steps

### Step 1: Extract actions from COMPLETE_PLAN
Read the COMPLETE_PLAN and identify all action items:
1. Read COMPLETE_PLAN.md thoroughly
2. Identify all explicit action items (stated directly)
3. Identify all implicit action items (assumed but not stated)
4. List actions in rough sequence
5. Note dependencies between actions
6. For each action, verify: does this serve the goal-structure?
   (If an action doesn't serve the goals, flag for review)

### Step 2: Decompose into atomic steps
Break compound actions into single atomic steps:
1. For each action, check: does it have multiple verbs?
2. If multiple verbs, split into separate steps
3. Ensure each step has ONE verb, ONE outcome
4. Add implicit steps that were assumed (setup, teardown, validation)
5. Resolve all decision points - no branching allowed in STEPS
   (use decision_tree if complex branching exists)

### Step 3: Establish execution order
Determine valid execution sequence:
1. Build dependency graph from step inputs/outputs
2. Perform topological sort for valid ordering
3. Identify parallel execution opportunities
4. Number steps sequentially
5. Use order_procedure if complex ordering needed

### Step 4: Elaborate each step fully
Apply the step template to each step:
1. Write clear action in imperative form
2. List ALL inputs with sources and formats
3. Define concrete output with format and destination
4. Add verification criteria (observable, pass/fail)
5. Add if_blocked handling (failure modes, resolutions, escalation)

Step template to apply:
```
## Step {N}: {Title}

**Action**: {Exactly what to do - single imperative verb phrase}

**Inputs**:
- {Input 1}: {description} [from: {source}]

**Process**:
1. {Sub-action 1}
2. {Sub-action 2}

**Output**: {What this produces} [format: {format}] [goes to: {destination}]

**Verification**:
- [ ] {Checkable criterion 1}
- [ ] {Checkable criterion 2}

**If blocked**:
- If {problem 1}: {resolution 1}
- If unresolvable: {escalation path}
```

### Step 5: Verify information sufficiency
Run information sufficiency gate on each step:

For each step, verify:
1. Action clear? Could someone unfamiliar execute this?
2. Inputs complete? All inputs listed with sources?
3. Output defined? Concrete and verifiable?
4. Verification checkable? Observable pass/fail?
5. Blockers handled? Common failures addressed?
6. No assumptions? Fully self-contained?

If any check fails, return to Step 4 and fix.

### Step 6: Verify sequence validity
Verify the full sequence is executable:
1. Dependency order: Does each step have inputs available?
2. No gaps: Are any transformation steps missing?
3. Parallelization: Are parallel opportunities correctly marked?
4. Critical path: What's the longest dependency chain?

Fix any issues found and re-verify.

### Step 7: Identify anti-patterns and fix
Scan for common anti-patterns and eliminate them:

Anti-patterns to catch:
- Vague actions: "Handle the authentication" -> specify exactly
- Missing source: "Use the config file" -> specify which file, from where
- Assumed knowledge: "Set up database as usual" -> specify exact commands
- Ambiguous pronouns: "Pass it to the function" -> name the specific thing
- Subjective verification: "Looks correct" -> objective criteria
- Hidden decisions: "Choose appropriate timeout" -> specify exact value
- Multiple actions: "Create and populate and validate" -> split into steps

### Step 8: Verify story coherence
Apply story_coherence_gate to the complete set of steps:

1. Read through all steps as a narrative (the "journey")
2. Check: Does each step connect to the next?
3. Check: Do the steps, taken together, serve the goal-structure?
4. Check: Is this journey necessary? (no unnecessary steps)
5. Check: Is this a valid path to the goals?

If story doesn't cohere:
- Identify which steps break the narrative
- Either remove unnecessary steps or add missing steps
- Re-verify until story coheres

### Step 9: Create document structure
Assemble the final STEPS.md document:
1. Write header with purpose, scope, metadata
2. Include goal-structure summary (what intrinsic goals this serves)
3. Write prerequisites checklist
4. Write glossary of terms (if needed)
5. Write each step using the template
6. Write completion checklist
7. Write rollback procedure (if abandoning partway)

Document structure:
```
# STEPS: {Goal Name}

**Generated from**: COMPLETE_PLAN.md
**Total steps**: {N}
**Estimated duration**: {time}
**Executor type**: {human/AI/team/automated}

## Goal-Structure
This STEPS document serves the following goal chain:
- Intrinsic goal: {e.g., wellbeing}
- Instrumental goals: {chain leading to this plan}
- Immediate goal: {what this plan achieves}

## Prerequisites
- [ ] {Prerequisite 1}

## Glossary
| Term | Definition |

## Steps
{Each step}

## Completion Checklist
- [ ] All steps complete
- [ ] Output artifacts present
- [ ] Goals served (verify against Goal-Structure)

## Rollback Procedure
{If abandoning}
```


## When to Use
- When transforming a COMPLETE_PLAN into executable steps
- When creating instructions that must work for any executor
- When eliminating ambiguity is critical
- When steps must be verifiable and auditable
- When handoff between planning and execution is needed
- When building automated workflows

## Verification
- Each step has exactly one concrete action
- All inputs have explicit sources
- All outputs have explicit formats and destinations
- Verification criteria are observable and objective
- No vague verbs or ambiguous pronouns
- All decision points are pre-resolved
- Sequence passes dependency validation

---

**Input**: $ARGUMENTS

Apply this procedure to the input provided.