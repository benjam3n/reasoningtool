---
name: cppd
description: "Analyze patterns across completed GOSM projects to improve the system."
---

# Cross-Project Pattern Detection

**Input**: $ARGUMENTS

---

## Overview

Analyze patterns across completed GOSM projects to improve the system. This is a standalone procedure — run it when you want to learn from accumulated experience, not as part of every project.

## Steps

### Step 1: Gather Project Data
Collect information from completed projects:

For each project:
1. Goal: what was the objective?
2. Outcome: success / partial / failure
3. Duration: planned vs actual
4. Strategy: what approach was used?
5. Procedures invoked: which skills were used?
6. Surprises: what was unexpected?
7. Key lessons: what was learned?

Minimum sample: 5 projects for basic patterns, 10+ for reliable patterns.

### Step 2: Detect Success Patterns
Look across successful projects:

| Pattern Category | Question | Finding |
|-----------------|----------|---------|
| Common procedures | Which procedures appear in most successes? | |
| Common sequences | Is there a typical order of procedures? | |
| Early indicators | What happened early in successful projects? | |
| Goal characteristics | What kinds of goals succeed most often? | |
| Strategy types | Which strategy types work best? | |
| Resource patterns | How were resources allocated in successes? | |

### Step 3: Detect Failure Patterns
Look across failed or struggling projects:

| Pattern Category | Question | Finding |
|-----------------|----------|---------|
| Missing procedures | Which procedures were NOT used that should have been? | |
| Common failures | What went wrong repeatedly? | |
| Early warnings | Were there signs of failure that were ignored? | |
| Goal characteristics | What kinds of goals fail most often? | |
| Procedure misapplication | Were procedures used incorrectly? | |
| Gaps | What situations had no applicable procedure? | |

### Step 4: Detect System-Level Patterns

**Procedure effectiveness:**
- Which procedures consistently produce useful output?
- Which procedures are invoked but don't change outcomes?
- Which procedures are underused (available but rarely invoked)?
- Which situations have no good procedure?

**Goal patterns:**
- Average goal completion rate
- Most common goal types
- Goal types with highest/lowest success rates
- Common reasons for goal abandonment

**Process patterns:**
- Average number of procedures per project
- Most common procedure sequences
- Where do projects get stuck?
- What triggers project restarts?

### Step 5: Generate Improvements
From detected patterns, identify:

1. **Procedure improvements:**
   - Which procedures need revision based on usage data?
   - What new procedures should be created for gaps?
   - Which procedures should be retired (never useful)?

2. **Routing improvements:**
   - Are category skills routing to the right content skills?
   - Are there common misroutes?
   - Should routing rules be updated?

3. **Process improvements:**
   - Should certain procedures be mandatory for certain goal types?
   - Should gate criteria be tightened or loosened?
   - Are there missing gates?

4. **Meta improvements:**
   - Is the pattern detection itself finding useful patterns?
   - Is the sample size sufficient?
   - Are there biases in which projects get completed vs abandoned?

### Step 6: Report
```
CROSS-PROJECT PATTERN DETECTION:
Projects analyzed: [N]
Period: [date range]

Success patterns:
1. [pattern] — seen in [N] of [M] successes
2. [pattern]

Failure patterns:
1. [pattern] — seen in [N] of [M] failures
2. [pattern]

System health:
- Procedure utilization: [% of procedures used at least once]
- Goal completion rate: [%]
- Most valuable procedure: [name] — [why]
- Biggest gap: [what's missing]

Recommended improvements:
1. [improvement] — expected impact: [H/M/L]
2. [improvement]

Priority: [which improvement to make first and why]
```

## When to Use
- After completing 5+ projects
- Quarterly review
- When system seems stuck or ineffective
- Before major GOSM changes
- → INVOKE: /iterate for acting on detected improvements
- → INVOKE: /ret (retrospective) for single-project learning

## Verification
- [ ] Sufficient project sample (5+ minimum)
- [ ] Both success and failure patterns analyzed
- [ ] System-level patterns detected (not just project-level)
- [ ] Improvements are specific and actionable
- [ ] Priority based on expected impact
