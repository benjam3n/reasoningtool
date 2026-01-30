---
name: "sads - Detector Sweep"
description: "Scan files for ambiguity, proxying, bundled questions, undefined terms, hidden conditionals, goal substitution, and conventional bias."
context: fork
---

# Detector Sweep

**Input**: $ARGUMENTS

---

## Overview

Scan a target set of files for:
- Ambiguity and undefined terms
- Proxying and bundled questions
- Hidden conditionals and false dichotomies
- **NEW: Goal substitution patterns (clarification vs substitution)**
- **NEW: Conventional bias (missing unconventional alternatives)**

---

## Steps

### Step 1: Scan for Classic High-Risk Patterns

Scan for:
- parentheticals that hide additional questions
- "if yes/no" scaffolding that bundles conditions
- "or" questions that create false dichotomies
- undefined terms used as if shared
- proxy patterns (formatting used as substitute for validation)

### Step 2: Scan for Goal Substitution Patterns (NEW)

Scan for language that may indicate silent goal substitution:

| Pattern | Example | Risk |
|---------|---------|------|
| "Underlying need" | "What you really need is..." | May replace stated goal |
| "Achievable version" | "A more realistic goal would be..." | May reduce ambition |
| "What you probably mean" | "I think you mean..." | Imposes interpretation |
| "Better framed as" | "This is better understood as..." | Changes goal |
| "The real problem is" | "Your actual problem is..." | Problem substitution |

**For each instance found:**
- Is this CLARIFICATION (same goal, clearer) or SUBSTITUTION (different goal)?
- If SUBSTITUTION: Is consent requested?
- If no consent: Flag for repair

### Step 3: Scan for Conventional Bias (NEW)

Check if ASSUME WRONG branches default to conventional alternatives:

| Pattern | Example | Risk |
|---------|---------|------|
| Only standard solutions | "The options are A, B, or C" (all conventional) | Missing unconventional |
| "Best practices" as only option | "Best practice is to..." | No alternatives considered |
| Industry standard default | "The normal approach is..." | May miss better options |
| No "what if opposite" check | Missing contrarian analysis | Confirmation bias |

**Unconventional alternative check:**
- Does the text include at least one unconventional/surprising option?
- Are "what if the opposite is true" scenarios explored?
- Are there options that would be "embarrassing to suggest but might work"?

### Step 4: Classify Each Issue by Repair Type

For each issue, choose one repair type:

**Classic repairs:**
- split into separate questions
- define term(s)
- add answer-interface (what would count as a check)
- replace proxy with content audit
- move evaluation criteria into explicit checklist

**Substitution repairs:**
- add clarification vs substitution check
- add consent request for substitutions
- preserve original goal statement
- make reframing explicit

**Conventional bias repairs:**
- add unconventional alternative requirement
- add "what if opposite" check
- add embarrassing-but-might-work prompt
- expand option space before narrowing

### Step 5: Prioritize Issues

| Severity | Type | Action |
|----------|------|--------|
| HIGH | Silent substitution without consent | Immediate repair |
| HIGH | Undefined term in decision point | Immediate repair |
| MED | Bundled question | Repair before use |
| MED | Missing unconventional alternatives | Add alternatives |
| LOW | Proxy pattern | Document for later |
| LOW | Minor ambiguity | Note but may accept |

---

## Output Format

```
## Detector Sweep Results: [target]

### Classic Pattern Issues
| Location | Pattern | Severity | Repair |
|----------|---------|----------|--------|
| ... | ... | ... | ... |

### Goal Substitution Issues
| Location | Pattern | Type | Consent? | Repair |
|----------|---------|------|----------|--------|
| ... | ... | CLAR/SUB | Y/N | ... |

### Conventional Bias Issues
| Location | Pattern | Missing | Repair |
|----------|---------|---------|--------|
| ... | ... | [what's missing] | ... |

### Summary
- Classic issues: [count]
- Substitution issues: [count]
- Conventional bias issues: [count]
- Total HIGH severity: [count] (need immediate repair)
```

---

## When to Use
- Before refactoring gates or procedures
- When text feels "rigorous" but is hard to check
- When different readers interpret the same line differently
- **NEW: When auditing goal-related skills for substitution**
- **NEW: When checking ARAW output for conventional bias**

---

## Integration Points
- Related: /self_audit_apply_detectors_and_generators, /gate_as_claim_audit
- Gate: clarification_vs_substitution_gate (for substitution detection)
- ARAW skill: unconventional enforcement section