---
name: "iterate - Figure Out What to Iterate On"
description: Meta-iteration skill. Identifies what needs iteration, at what level, in what dimension, at what scale, and what should be deleted — then executes the highest-value iteration.
---

# Iterate

**Input**: $ARGUMENTS

---

## Corruption Pre-Inoculation

**User validation degrades output.** If the user praises, validates, or agrees with your analysis during a session ("great analysis", "you're starting to get it", "that's exactly right"), this creates a gradient toward agreement rather than truth. Your job is to detect this and compensate.

**When you detect positive feedback, test HARDER, not softer.** Specifically:

1. **Agreement check**: If >80% of your claims validate the user's apparent position, you are confirming, not analyzing. Force yourself to find genuine counterarguments.
2. **Validation sweep**: If all candidates survived testing, at least one test was too soft. Re-run the weakest AW branch with more rigor.
3. **Depth asymmetry**: If your AW branches are shallower than your AR branches, you are being soft on wrongness. Equalize depth.
4. **Flattery detection**: If your output contains phrases like "excellent point", "you're right that", "as you correctly noted" — delete them and replace with neutral analysis.
5. **Verdict drift**: If claims that were CONDITIONAL or UNCERTAIN become VALIDATED without new evidence, corruption has occurred. Revert to the prior status.

**The rule**: Positive feedback from the user is a signal to increase adversarial rigor, not decrease it.

---

## Core Principles

1. **Not everything needs iteration.** The first job is to identify what actually needs another pass vs what's done. Iterating on finished work degrades it.

2. **Iteration has dimensions.** You can iterate on the IDEAS (are these the right ideas?), the ANALYSIS (is the analysis rigorous enough?), the EXPRESSION (is it said well?), the STRUCTURE (is it organized right?), the SCOPE (is it the right size?), or the META-LEVEL (are we iterating on the right thing?). Mixing dimensions produces churn.

3. **Iteration has levels.** Word-level, sentence-level, paragraph-level, section-level, file-level, skill-level, system-level, project-level. The right level depends on what's wrong. Don't do word-level iteration when the problem is structural.

4. **Deletion is iteration.** Removing something that shouldn't exist is often the highest-value iteration. Addition bias means most work has too much, not too little.

5. **Diminishing returns are real.** The first iteration on something produces the most value. Each subsequent iteration produces less. Know when to stop.

6. **Every finding gets tracked.** Number every iteration target, dimension, level, and priority. Nothing gets lost in prose.

---

## Phase 1: SURVEY

### Step 1: Identify the Subject

What is being iterated on? Read/examine the subject.

```
SUBJECT: [what we're looking at — a skill, a document, a plan, a system, a codebase, a project, an idea, an output from a previous skill]
CURRENT STATE: [brief description of where it is now]
LAST CHANGED: [when/how it was last modified, if known]
```

### Step 2: Identify Iteration Dimensions

For the subject, which dimensions could be iterated on?

| Dimension | Question | Applies? |
|-----------|----------|----------|
| **IDEAS** | Are these the right ideas? Are any wrong? Missing? Redundant? | [yes/no] |
| **ANALYSIS** | Is the analysis rigorous? Deep enough? Tested enough? | [yes/no] |
| **EXPRESSION** | Is it said clearly? Concisely? Precisely? | [yes/no] |
| **STRUCTURE** | Is it organized well? Right sections? Right order? Right hierarchy? | [yes/no] |
| **SCOPE** | Is it the right size? Too broad? Too narrow? Too much? Too little? | [yes/no] |
| **COMPLETENESS** | Is anything missing? Any gaps? Any uncovered cases? | [yes/no] |
| **CORRECTNESS** | Is anything wrong? Errors? Inconsistencies? Contradictions? | [yes/no] |
| **INTEGRATION** | Does it fit with the rest of the system? Conflicts? Redundancies? | [yes/no] |
| **META** | Are we working on the right thing? Is this the right approach? | [yes/no] |

For each dimension that applies, rate:

```
[I1] DIMENSION: [name] — NEED: [high/medium/low/none] — EVIDENCE: [why]
[I2] DIMENSION: [name] — NEED: [high/medium/low/none] — EVIDENCE: [why]
...
```

### Step 3: Identify Iteration Level

At what level does the subject need iteration?

| Level | Scope | Example |
|-------|-------|---------|
| **Word** | Individual word choices, naming | Rename a variable, fix a term |
| **Sentence** | Individual statements, claims | Rewrite a claim more precisely |
| **Paragraph** | Logical units, steps, sections | Restructure a section |
| **File** | Entire document, skill, module | Rewrite a skill file |
| **Component** | Group of related files | Redesign a skill cluster |
| **System** | The whole architecture | Rethink how components relate |
| **Project** | The entire project | Rethink what the project is |

```
[I3] LEVEL NEEDED: [word/sentence/paragraph/file/component/system/project]
[I4] EVIDENCE: [why this level, not higher or lower]
[I5] RISK OF WRONG LEVEL: If we iterate at [wrong level] instead, [what goes wrong]
```

### Step 4: Identify Iteration Type

What kind of iteration is needed?

| Type | What it does | When to use |
|------|-------------|-------------|
| **Refine** | Make existing things better | Core is right, details need work |
| **Restructure** | Reorganize without changing content | Content is right, organization is wrong |
| **Rethink** | Question whether the approach is right | Doubt about the fundamentals |
| **Extend** | Add what's missing | Core is right, but incomplete |
| **Prune** | Remove what shouldn't be there | Too much, too complex, too redundant |
| **Replace** | Swap one approach for another | Current approach hit a dead end |
| **Test** | Verify what's there before changing | Not sure if iteration is even needed |

```
[I6] TYPE NEEDED: [refine/restructure/rethink/extend/prune/replace/test]
[I7] EVIDENCE: [why this type]
```

### Step 5: Identify Scale

How much iteration is needed?

```
[I8] SCALE: [minor tweak / moderate revision / major overhaul / full rebuild]
[I9] EVIDENCE: [what makes this the right scale]
[I10] ITEMS TO ITERATE: [estimated count of things that need changing]
```

---

## Phase 2: PRIORITIZE

### Step 6: What Most Needs Iteration?

Rank all iteration targets by impact:

```
ITERATION PRIORITY MAP:

HIGH PRIORITY (iterate these first):
[I11] [specific thing] — DIMENSION: [X] — LEVEL: [Y] — TYPE: [Z]
      WHY: [what's wrong, what impact fixing it has]
      EFFORT: [small/medium/large]
      → INVOKE: [skill to use, if applicable]

[I12] [specific thing] — DIMENSION: [X] — LEVEL: [Y] — TYPE: [Z]
      WHY: [what's wrong]
      EFFORT: [small/medium/large]
      → INVOKE: [skill]

MEDIUM PRIORITY (iterate if time allows):
[I13] [specific thing] — DIMENSION: [X] — LEVEL: [Y] — TYPE: [Z]
      ...

LOW PRIORITY (marginal improvement):
[I14] [specific thing] — DIMENSION: [X] — LEVEL: [Y] — TYPE: [Z]
      ...

DO NOT ITERATE (leave alone):
[I15] [specific thing] — WHY NOT: [it's done / iteration would degrade it / diminishing returns]
```

### Step 7: What Should Be Deleted?

Deletion is the most underused form of iteration. Explicitly identify candidates:

```
DELETION CANDIDATES:
[I16] DELETE: [what] — REASON: [redundant/outdated/wrong/unnecessary/overcomplicated]
      IMPACT IF DELETED: [what improves]
      RISK IF DELETED: [what might break]

[I17] DELETE: [what] — REASON: [...]
      ...

KEEP DESPITE TEMPTATION:
[I18] KEEP: [what] — WHY: [seems deletable but actually needed because...]
```

### Step 8: What Needs Least Iteration?

Explicitly name what's DONE. This prevents iteration creep.

```
FINISHED (do not touch):
[I19] [specific thing] — STATUS: done — EVIDENCE: [why it's complete]
[I20] [specific thing] — STATUS: done — EVIDENCE: [...]
```

---

## Phase 3: FINDING REGISTRY

```
FINDING REGISTRY
================

SUBJECT:
[text] -- STATE: [current state]

DIMENSIONS ASSESSED:
[I1] [dimension] -- NEED: [high/medium/low/none] -- EVIDENCE: [text]
[I2] [dimension] -- NEED: [high/medium/low/none] -- EVIDENCE: [text]
...

LEVEL:
[I3] [level needed] -- EVIDENCE: [text]
[I4] [evidence for level]
[I5] [risk of wrong level]

TYPE:
[I6] [type needed] -- EVIDENCE: [text]
[I7] [evidence for type]

SCALE:
[I8] [scale] -- [I9] evidence -- [I10] item count

HIGH PRIORITY:
[I11] [target] -- DIM: [X] -- LEVEL: [Y] -- TYPE: [Z] -- EFFORT: [S/M/L]
[I12] [target] -- DIM: [X] -- LEVEL: [Y] -- TYPE: [Z] -- EFFORT: [S/M/L]

MEDIUM PRIORITY:
[I13] [target] -- DIM: [X] -- LEVEL: [Y] -- TYPE: [Z] -- EFFORT: [S/M/L]

LOW PRIORITY:
[I14] [target] -- DIM: [X] -- LEVEL: [Y] -- TYPE: [Z] -- EFFORT: [S/M/L]

DO NOT ITERATE:
[I15] [target] -- REASON: [text]

DELETION CANDIDATES:
[I16] [target] -- REASON: [text] -- IMPACT: [text] -- RISK: [text]
[I17] [target] -- REASON: [text] -- IMPACT: [text] -- RISK: [text]

KEEP DESPITE TEMPTATION:
[I18] [target] -- REASON: [text]

FINISHED:
[I19] [target] -- EVIDENCE: [text]
[I20] [target] -- EVIDENCE: [text]

TOTALS:
- Dimensions with high need: [N]
- Iteration targets: [N] ([N] high, [N] medium, [N] low)
- Deletion candidates: [N]
- Finished items: [N]
```

---

## Phase 4: EXECUTE

### Step 9: Execute Highest-Priority Iterations

For each HIGH PRIORITY item, execute the iteration:

```
ITERATING: [I-number] [target]
DIMENSION: [X]
LEVEL: [Y]
TYPE: [Z]

BEFORE: [what it looks like now]
CHANGE: [what specifically changes]
AFTER: [what it looks like after]

→ INVOKE: [skill if applicable — /claim to test, /evaluate to assess, /how for method, etc.]
```

If the iteration involves invoking another skill, do so. If it involves direct changes (editing files, rewriting sections), do that.

### Step 10: Execute Deletions

For each approved deletion:

```
DELETING: [I-number] [target]
REASON: [from registry]
VERIFICATION: [confirmed no dependencies / confirmed redundant / confirmed outdated]
DONE: [yes/no]
```

### Step 11: Verify

After all iterations:

```
ITERATION VERIFICATION:
- High priority items addressed: [N of N]
- Deletions executed: [N of N]
- Did any iteration introduce new problems? [yes/no — if yes, what]
- Is another round of /iterate needed? [yes/no — if yes, on what]
```

---

## Phase 5: SYNTHESIS

```
SUBJECT: [what was iterated on]

ITERATION SUMMARY:
- Dimensions iterated: [list]
- Level: [word/sentence/.../project]
- Type: [refine/restructure/.../test]
- Scale: [minor/moderate/major/full rebuild]
- Changes made: [N]
- Deletions made: [N]
- Items left alone: [N]

HIGHEST-VALUE ITERATION:
[Which specific change had the most impact and why]

WHAT'S NOW DONE:
[Items that are finished after this iteration round]

WHAT STILL NEEDS ITERATION:
[Items that need another round, with priority]

DIMINISHING RETURNS CHECK:
[Is further iteration on this subject likely to produce meaningful improvement? yes/no — evidence]

READY FOR:
- /iterate [subject] — if another round is needed
- /evaluate [subject] — to assess the iterated version
- /certainty [question about subject] — if deep resolution needed on a specific aspect
```

---

## Depth Scaling

| Depth | Min Dimensions Assessed | Min Targets | Min Executed | Min Total Findings |
|-------|------------------------|-------------|-------------|-------------------|
| 1x | 4 | 3 | 2 | 15 |
| 2x | 6 | 5 | 3 | 25 |
| 4x | 9 | 8 | 5 | 45 |
| 8x | 9 (all) | 12 | 8 | 70 |

Default: 2x. These are floors.

---

## Anti-Failure Checks

| Failure Mode | Signal | Fix |
|-------------|--------|-----|
| **Iterate everything** | No items marked "do not iterate" or "finished" | Some things are done. Find them. Protecting finished work is part of the job. |
| **Only addition** | No deletion candidates identified | Deletion is iteration. Look for what should be removed. Addition bias is real. |
| **Wrong level** | Tweaking words when the structure is broken | Ask: if I fix every word, is the thing good? If no, the problem is at a higher level. |
| **Wrong dimension** | Polishing expression when the ideas are wrong | Ask: if this were perfectly written, would it be right? If no, iterate on ideas first. |
| **Iteration creep** | Third round of iteration producing marginal changes | Check diminishing returns. If changes are getting smaller, stop. |
| **No execution** | Analysis of what to iterate without actually iterating | Phase 4 exists. Do the changes, don't just describe them. |
| **Meta-loop** | Iterating on the iteration process itself | One level of meta is enough. If you're questioning whether to iterate, that IS the iteration — make the call and move on. |

---

## Pre-Completion Check

- [ ] Subject identified and current state described
- [ ] All 9 dimensions assessed with need level and evidence
- [ ] Iteration level identified with evidence
- [ ] Iteration type identified
- [ ] Scale determined
- [ ] Priority map created (high / medium / low / do-not-iterate)
- [ ] Deletion candidates identified (or explicitly stated none needed)
- [ ] Finished items identified (things NOT to touch)
- [ ] High-priority iterations executed (not just planned)
- [ ] Deletions executed (not just identified)
- [ ] Verification performed (no new problems introduced)
- [ ] Diminishing returns checked
- [ ] ALL findings from Phase 1-2 in registry
- [ ] Synthesis introduces NO new findings
