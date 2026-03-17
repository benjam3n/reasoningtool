---
name: "fix - Fix It"
description: "Take something broken, bad, or underperforming — diagnose what's wrong, then fix it in place. Works on code, skills, documents, plans, processes, or anything with a quality gap."
output:
  format: "prose"
---

# Fix

**Input**: $ARGUMENTS

---

## Interpretations

Before executing, identify what's being fixed:

**Interpretation 1 — Code**: Something in the codebase is broken, buggy, or underperforming. Read it, find the problems, fix them.
**Interpretation 2 — Skill/document**: A skill file, plan, doc, or structured text is low quality, outdated, or wrong. Diagnose the quality gap, rewrite.
**Interpretation 3 — Output**: Something produced in this conversation (analysis, categorization, generation) was bad. Identify why, redo it properly.
**Interpretation 4 — Process/approach**: The way something is being done is wrong. Identify the failure pattern, propose and implement the fix.

If ambiguous: look at context. If the user just ran a skill and said "fix it," they mean the output. If they point at a file, they mean that file. If still unclear, ask: "What specifically needs fixing?"

---

## Core Principles

1. **Read before diagnosing.** Never guess what's wrong. Read the actual thing. All of it.
2. **Diagnose before fixing.** Name the specific problems. Don't just rewrite blindly — know WHY it's broken so the fix is targeted.
3. **Fix in place.** Edit the actual file/thing. Don't create a new one alongside it unless the user asks.
4. **Verify the fix.** After fixing, check that the problems are actually resolved and nothing new broke.
5. **Minimum necessary change.** Fix what's wrong. Don't refactor what's working. Don't add features. Don't "improve" adjacent code.
6. **Say what you did.** Report the specific problems found and the specific fixes applied.

---

## Step 1: Read the Thing

Read the entire target. If it's a file, read the file. If it's output, review the output. If it's a directory, scan the directory.

While reading, note:
- What is this supposed to do/be?
- What is it actually doing/being?
- Where is the gap?

---

## Step 2: Diagnose

List every specific problem. Number them.

```
PROBLEMS FOUND:
[P1] [specific problem] — SEVERITY: critical/serious/minor
[P2] [specific problem] — SEVERITY: critical/serious/minor
[P3] [specific problem] — SEVERITY: critical/serious/minor
...
```

### Problem Types

| Type | Signal | Example |
|------|--------|---------|
| **Wrong** | Produces incorrect results | Logic error, bad data, false claim |
| **Missing** | Something essential isn't there | Missing step, missing check, missing case |
| **Excess** | Something unnecessary is present | Dead code, redundant sections, padding |
| **Weak** | Present but insufficient | Vague instructions, shallow analysis, soft tests |
| **Stale** | Was right, now outdated | Old references, deprecated patterns, wrong counts |
| **Misaligned** | Works but serves wrong goal | Solves the wrong problem, optimizes wrong metric |
| **Fragile** | Works now but breaks easily | Hardcoded values, missing error handling, tight coupling |

### Quality Check: Is the Diagnosis Real?

- Can you point to the specific line/section/element that's broken?
- If you removed or changed it, would the thing measurably improve?
- Would someone else independently identify this as a problem?

If you can't answer yes to all three, it's not a real problem — drop it.

---

## Step 3: Plan the Fix

For each problem, state the fix. One sentence each.

```
FIXES:
[P1] → [what to change]
[P2] → [what to change]
[P3] → [what to change]
```

### Fix Priority

1. Critical problems first (thing is broken/wrong)
2. Serious problems second (thing is weak/missing)
3. Minor problems last (thing is suboptimal)

If fixing one problem resolves others, note the cascade.

---

## Step 4: Execute the Fix

Apply all fixes. Use Edit for targeted changes, Write for full rewrites when >50% needs changing.

**For code:** Edit the files. Run tests if available.
**For skills/docs:** Rewrite the broken sections. Preserve what works.
**For output:** Re-execute the skill or analysis with corrections.
**For processes:** Write the corrected process, noting what changed and why.

---

## Step 5: Verify

After fixing, check:

- [ ] Every numbered problem is resolved
- [ ] No new problems introduced
- [ ] The thing now does what it's supposed to do
- [ ] The fix is minimal (didn't over-engineer)

If verification fails, go back to Step 2 with the new state.

---

## Step 6: Report

```
FIXED: [what was fixed]

PROBLEMS FOUND: [N]
  Critical: [N]
  Serious: [N]
  Minor: [N]

CHANGES MADE:
- [P1]: [one-line summary of fix]
- [P2]: [one-line summary of fix]
...

VERIFIED: [yes/no — if no, what remains]
```

---

## Depth Scaling

| Depth | Read | Diagnose | Fix | Verify |
|-------|------|----------|-----|--------|
| 1x | Skim target | Top 1-2 problems | Quick fix | Spot check |
| 2x | Full read | All problems listed | Fix all | Check each problem resolved |
| 4x | Full read + context (related files, usage) | Problems + root causes | Fix + prevent recurrence | Check + regression test |
| 8x | Full read + context + history (git blame, prior versions) | Problems + patterns + comparison to best examples | Fix + restructure if needed | Full verification + comparison to quality bar |

Default: 2x.

---

## Anti-Failure Checks

| Failure Mode | Signal | Fix |
|-------------|--------|-----|
| **Blind rewrite** | Rewrote everything without diagnosing | Stop. List problems first. Then fix only those. |
| **Cosmetic fix** | Changed formatting/wording but core problems remain | Check: did you fix the SUBSTANCE or just the SURFACE? |
| **Over-fix** | Added features, refactored working code, "improved" beyond scope | Revert extras. Fix only what was broken. |
| **Diagnosis without fix** | Listed problems but didn't change anything | Execute Step 4. The point is to FIX, not just diagnose. |
| **Wrong target** | Fixed something adjacent to the actual problem | Re-read the user's input. What did THEY say was broken? |
| **New bugs** | Fix introduced new problems | Verify step should catch this. If it didn't, verification was too shallow. |

---

## Integration

- After `/fix`: user may want `/araw` to verify the fix holds up, or `/cls` to check against criteria
- `/diagnose` → `/fix`: diagnose finds the cause, fix applies the solution
- `/fix` differs from `/diagnose`: diagnose is about FINDING what's wrong. Fix is about MAKING IT RIGHT. Fix includes diagnosis as Step 2 but the goal is the repair, not the analysis.

---

**Execute now.**
