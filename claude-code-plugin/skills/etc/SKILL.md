---
name: "etc - Expand the Etcetera"
description: Expand "etc" tails into explicit items using pattern continuation, then stop at a defined completeness rule.
---

# ETC - Expand the Etcetera

**Input**: $ARGUMENTS

---

## Steps

1. Extract explicit list head.
2. Infer the hidden continuation rule.
3. Enumerate likely omitted items.
4. Stop when completeness criterion is met.

## Output

Expanded explicit list plus continuation rule and stop condition.
