---
name: assumeright_assumewrong_search
description: "A recursive search strategy that explores possibility space by branching"
---

# Assume Right Assume Wrong Search

## Overview
A recursive search strategy that explores possibility space by branching
on every claim's validity. For each claim/guess, the system explores:

- ASSUME RIGHT: Treat claim as closed (true, no alternatives), explore that world
- ASSUME WRONG: Treat claim as open (false, has alternatives), explore alternatives

This is applied recursively at every level, even to "foundations" that seem certain.
The result is a complete map of possibility space.

## When to Use
- When processing any user input (goals, problems, questions, decisions)
- When a situation seems to have "only one option"
- When you want to stress-test assumptions
- When exploring what could be different

## Output Format
```
action_recommendations:
  description: Suggested next steps based on exploration
  use: Guide user toward action
discovered_alternatives:
  description: Options user didn't know they had
  use: Expand user's choice set
filtered_questions:
  description: Questions for user, filtered by context
  use: Presented to user for confirmation/correction
high_leverage_summary:
  description: Claims where ASSUME WRONG changes everything
  use: Focus user attention on what matters
tree_structure:
  description: Full possibility tree
  use: Internal processing, complete mapping

```

---

**Input**: $ARGUMENTS

Apply this procedure to the input provided.