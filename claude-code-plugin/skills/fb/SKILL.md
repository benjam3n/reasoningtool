---
name: "fb - Filtered Feedback Generation"
description: Generate filtered feedback for self-improvement loops. Only accepts well-grounded, high-leverage items to prevent error accumulation.
context: fork
---

# Filtered Feedback Generation

Analyze the current session and generate filtered feedback for self-improvement.

## Filtering Criteria

Based on three GOSM procedures:

### 1. Leverage Scoring (leverage_point_discovery.yaml)
LEVERAGE = value × defensibility × scalability
- value: Impact if resolved (0-1)
- defensibility: Protected from invalidation (0-1)
- scalability: Broadly applicable (0-1)

### 2. Selection Filters (selection.yaml)
- Implementation readiness (feasibility > 0.3)
- Risk tolerance (high risk needs high leverage)
- Reversibility (irreversible needs stronger validation)

### 3. Convergent Validation (convergent_validation.yaml)
Four independent checks:
- is_grounded: Has [O], [T], or [D] marker
- is_fixed_point: Stable under re-analysis
- is_convergent: Multiple paths lead here
- is_practical: Passes real-world filters

**Decision Protocol:**
- 4 checks pass → Accept with high confidence
- 3 checks pass → Accept with moderate confidence
- 2 checks pass → Flag for review
- <2 checks pass → Reject

## Output Format

### ACCEPTED (feed back into system)
For each accepted item:
```
TYPE: goal | problem | question | decision | assumption
CONTENT: [the item]
LEVERAGE: [0-1 score]
CONVERGENT_SCORE: [0-4]
GROUNDING: [O/T/D marker]
```

### FLAGGED (needs review)
Items with 2 checks passing - list for optional review.

### REJECTED (do not feed back)
Items that failed filtering - excluded to prevent error accumulation.

## Instructions

1. Review all outputs from the current session
2. Score each potential feedback item
3. Apply the filtering criteria
4. Only accept items that pass convergent validation
5. Format accepted items as new GOSM inputs
