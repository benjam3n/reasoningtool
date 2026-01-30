---
name: "sagsca - Gate Schema Consistency Audit"
description: "Identify inconsistent gate field schemas across the library that increase interpretation burden and cause engine integration drift."
---

# Gate Schema Consistency Audit

## Overview
Identify inconsistent gate field schemas across the library that increase interpretation burden and cause engine integration drift.

## Steps

### Step 1: Inventory gate field variants
For each gate file, inventory which fields are used for these concepts:
- ordering: sequence_order vs sequence
- evaluation target: evaluation_prompt vs evaluation_procedure
- definition: description vs purpose vs long_description
- routing: on_pass/on_fail/on_partial/on_skip/on_error (and custom keys)
- triggers: trigger_conditions vs trigger
- meta flags: is_meta/affects_system/skippable/phase/category/tags

Output a table of “concept -> observed field variants -> example files”.

### Step 2: Choose a standard gate schema (non-regression)
For each concept (ordering, evaluation, routing, triggers):
- State the intent of the concept.
- Choose one standard field name.
- State what must be preserved from the non-standard variants.
- Propose a migration mapping (old field -> new field) that preserves meaning.

Do not delete information; move it or rename it.

### Step 3: Apply clarity audits to the chosen standard
Apply:
- library/procedures/core/goal_analysis/analysis_protocol_clarity_and_validity.yaml
- library/procedures/core/goal_analysis/detectors_and_generators.yaml

Goal: the standard schema itself should not smuggle in bundled checks, undefined terms, or hidden conditionals.


## When to Use
- When adding new gate files or new gate fields
- When the engine behaves differently across gate sets (core vs domain vs meta)
- When you want a single “standard gate form” across the library

---

**Input**: $ARGUMENTS

Apply this procedure to the input provided.