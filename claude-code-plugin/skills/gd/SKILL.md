---
name: gd
description: "A methodology for decomposing abstract goals into specific, actionable components. Includes clarification vs substitution verification."
context: fork
---

# Goal Decomposition Methodology

**Input**: $ARGUMENTS

---

## Overview

A methodology for decomposing abstract goals into specific, actionable components
while preserving important information about dimensions, tradeoffs, and constraints.

The problem with naive decomposition: "Make the world better" becomes "Make people
happier" - this loses almost everything. What does "better" mean? Better for whom?
In what dimension? At what cost? Who decides?

Good decomposition preserves information, not destroys it. You should be able to
trace from any action back to why it serves the original goal, through explicit
reasoning, without hidden assumptions.

---

## CRITICAL: Decomposition vs Substitution

Decomposition should break down the SAME goal into parts, not replace it with
easier sub-goals that don't add up to the original.

### Step 0: Capture Original and Verify Decomposition

```
ORIGINAL GOAL (verbatim): "[user's exact words]"
```

### Decomposition Integrity Check

After generating sub-goals, verify:

| Check | Pass/Fail |
|-------|-----------|
| Sub-goals together = original goal? | |
| No sub-goal is easier substitution? | |
| Achieving all sub-goals achieves original? | |
| No hidden reduction in scope? | |

**Test**: If user achieved ALL sub-goals but NOT the original as stated, what would happen?
- "They would have achieved it" → VALID decomposition
- "They'd still be missing [X]" → INCOMPLETE decomposition
- "They achieved something different" → SUBSTITUTION

If substitution detected → Use consent template from /goal_refinement

---

## Context-Adaptive Variants

### Decomposition-Lite (URGENT)
- Quick breakdown into 2-3 actionable chunks
- Skip detailed tradeoff analysis
- Focus on "what to do first"

### Decomposition-Standard
- Full procedure with all steps
- Complete tradeoff analysis

### Decomposition-Full (HIGH stakes)
- Full procedure + validation
- Multiple decomposition approaches compared
- Empirical validation of key assumptions

---

## When to Use
- When a goal is abstract or vague
- Before committing to a plan
- When "obvious" decomposition feels too simple
- When you need to understand tradeoffs
- During GOSM Goal Definition (Step 2)

## Output Format
```
structure: '## Goal Decomposition: [Original Goal]


  ### Expanded Definition

  [Full expanded definition with dimensions, scope, timeframe, constraints]


  ### Subgoals

  | Subgoal | Dimension | Enables | Conflicts With | Priority |

  |---------|-----------|---------|----------------|----------|

  | ... | ... | ... | ... | ... |


  ### Subgoal Relationships

  [Graph or list of dependencies and conflicts]


  ### Tradeoff Decisions

  | Conflict | Decision | Reasoning |

  |----------|----------|-----------|

  | ... | ... | ... |


  ### Action Plan

  | Action | Subgoal | Success Criteria | Sequence |

  |--------|---------|------------------|----------|

  | ... | ... | ... | ... |

  '

```

---

**Input**: $ARGUMENTS

Apply this procedure to the input provided.