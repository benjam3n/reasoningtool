---
name: "ata - And Then Also"
description: Expand a request with all implied adjacent actions that should also be done, then order them.
---

# ATA - And Then Also

**Input**: $ARGUMENTS

---

## Steps

1. Parse primary request.
2. Enumerate implied adjacent tasks.
3. Mark required vs optional.
4. Order by dependency and ROI.

## Output

Primary task plus ordered "and then also" tasks.
