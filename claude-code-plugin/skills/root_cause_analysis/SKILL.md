---
name: root_cause_analysis
description: "Systematically trace symptoms back to their underlying root causes using structured diagnostic techniques. Supports context-adaptive variants."
context: fork
---

# Root Cause Analysis

**Input**: $ARGUMENTS

---

## Overview

Systematically trace symptoms back to their underlying root causes using structured diagnostic techniques.

---

## Step 0: Context Detection and Variant Selection

Before full analysis, assess context:

| Factor | Value | Notes |
|--------|-------|-------|
| Time Pressure | URGENT / NEAR / NORMAL | |
| Recurrence risk | HIGH / MED / LOW | Will this happen again? |
| Impact severity | HIGH / MED / LOW | |
| Complexity | SIMPLE / MODERATE / COMPLEX | |

### Variant Selection

| Context | Variant | Steps |
|---------|---------|-------|
| URGENT + need immediate fix | RCA-Lite | 1, 2, 3 (5 Whys only), 7 (immediate action) |
| LOW recurrence + SIMPLE | RCA-Quick | 1, 3, 7 |
| HIGH recurrence + post-mortem | RCA-Full | All 8 steps + cross-incident pattern analysis |
| MODERATE, standard incident | RCA-Standard | All 8 steps |

**RCA-Lite (5 steps)**: For URGENT situations
1. Define problem (Step 1 - abbreviated)
2. Quick evidence (Step 2 - what we know NOW)
3. 5 Whys (Step 3 - fast drill-down)
4. Immediate action (Step 7 - stop the bleeding)
5. Note for follow-up (schedule full RCA later)

**RCA-Quick (3 steps)**: For SIMPLE, non-recurring issues
1. Problem + evidence (Steps 1-2 combined)
2. 5 Whys (Step 3)
3. Corrective action (Step 7)

**RCA-Standard (8 steps)**: Default full procedure

**RCA-Full (8+ steps)**: For HIGH recurrence or post-mortems
- All 8 steps PLUS:
- Cross-incident pattern analysis
- Systemic factor identification
- Empirical validation of root cause hypothesis
- Long-term prevention planning

**Selected variant**: [variant] because [reasoning]

---

## Steps

### Step 1: Define and scope the problem
Clearly articulate what problem you're analyzing:
1. State the problem in specific, observable terms
   - Bad: "The system is slow"
   - Good: "API response time increased from 200ms to 2s starting Tuesday"
2. Quantify the impact (frequency, severity, scope)
3. Establish timeline (when did it start, any patterns?)
4. Identify who/what is affected
5. Distinguish the problem from proposed solutions
   - Bad: "We need more servers"
   - Good: "Server CPU is at 100% during peak hours"
6. Verify this is the real problem worth solving

### Step 2: Gather evidence
Collect facts before theorizing causes:
1. What data exists about the problem?
   - Logs, metrics, error messages
   - User reports, observations
   - Timeline of events
2. What changed before the problem appeared?
   - Deployments, configurations
   - External factors (load, dependencies)
   - Personnel or process changes
3. What has been tried already?
   - Previous fixes and their results
   - Workarounds in use
4. What makes it better or worse?
   - Conditions where it doesn't occur
   - Factors that correlate with severity
5. Separate facts from assumptions
   - Mark each piece of evidence as verified/unverified

### Step 3: Apply 5 Whys technique
Iteratively ask "Why?" to drill from symptom to root cause:

PROCESS:
1. Start with the problem statement
2. Ask "Why did this happen?"
3. For each answer, ask "Why?" again
4. Continue until you reach a root cause
5. Document each level of the chain

GUIDELINES:
- Stay on one causal chain at a time
- Use facts, not speculation (verify each answer)
- If answer is "because someone made a mistake," ask "Why was that mistake possible?"
- If answer is "because we didn't know," ask "Why didn't we know?"
- Stop when you reach something actionable
- Branch if multiple answers exist at any level

EXAMPLE:
Problem: Production outage lasted 4 hours
Why? Alert wasn't noticed for 3 hours
Why? Alert went to email, not pager
Why? Pager alerting wasn't configured for this service
Why? No standard checklist for new service deployment
Why? Deployment process lacks quality gates
ROOT CAUSE: Missing deployment checklist/process

COMMON 5 WHYS PATTERNS:
- Process: Missing process, unclear process, process not followed
- Training: Lack of knowledge, inadequate training
- Tools: Missing tool, tool misconfigured, tool inadequate
- Communication: Information not shared, miscommunication
- Design: Flawed design, missing safeguards, complexity

### Step 4: Apply Ishikawa (Fishbone) analysis
Explore causes across standard categories:

CATEGORIES (6 Ms - adapt to context):

METHODS (Process):
- Are procedures adequate?
- Is the process being followed?
- Are there missing steps?
- Is the sequence correct?

MACHINES (Technology/Tools):
- Is equipment functioning correctly?
- Are tools adequate for the task?
- Is software configured correctly?
- Are there capacity limitations?

MATERIALS (Inputs/Data):
- Are inputs correct and complete?
- Is data quality sufficient?
- Are dependencies reliable?
- Are resources available?

MANPOWER (People):
- Is training adequate?
- Is staffing sufficient?
- Are skills matched to tasks?
- Is communication effective?

MEASUREMENT (Metrics/Monitoring):
- Are we measuring the right things?
- Is monitoring adequate?
- Are thresholds correct?
- Is feedback timely?

ENVIRONMENT (Context):
- Are external factors involved?
- Is the operating environment suitable?
- Are there competing priorities?
- Are there organizational constraints?

For each category:
1. Brainstorm potential causes
2. Check each against evidence
3. Mark as confirmed/possible/ruled out

### Step 5: Apply Fault Tree Analysis
Build top-down logic tree of how failure occurred:

PROCESS:
1. Place the problem (top event) at the root
2. Identify immediate causes using logic gates:
   - AND gate: All sub-causes must be true for parent
   - OR gate: Any sub-cause can trigger parent
3. For each immediate cause, identify its causes
4. Continue until reaching basic events (root causes)

EXAMPLE FAULT TREE:
Top Event: "Customer charged incorrectly"
  OR gate:
  ├── "Price calculation wrong"
  │   AND gate:
  │   ├── "Discount not applied"
  │   └── "Item was on sale"
  ├── "Wrong item scanned"
  │   OR gate:
  │   ├── "Barcode mismatch"
  │   └── "Manual entry error"
  └── "System error"
      AND gate:
      ├── "Database sync failed"
      └── "No validation check"

BENEFITS:
- Shows logical relationships between causes
- Identifies which combinations of causes are necessary
- Reveals single points of failure
- Helps prioritize: AND gates need all causes fixed; OR gates need any one

### Step 6: Synthesize and prioritize root causes
Combine findings from all techniques:

1. Consolidate causes from 5 Whys, Fishbone, and Fault Tree
2. Remove duplicates and merge related causes
3. For each potential root cause, assess:
   - Confidence: How certain are we this is a cause? (High/Medium/Low)
   - Evidence: What facts support or refute this?
   - Impact: How much does this contribute to the problem?
   - Actionability: Can we actually address this cause?

4. Classify causes:
   - Root causes: Fundamental causes that, if fixed, prevent recurrence
   - Contributing factors: Made the problem worse but aren't root causes
   - Symptoms: Effects of the problem, not causes

5. Prioritize by: Confidence x Impact x Actionability

6. Identify cause patterns:
   - Are multiple root causes related?
   - Is there a systemic issue underlying multiple causes?

### Step 7: Develop corrective actions
For each root cause, identify corrective actions:

ACTION TYPES:
- Immediate: Stop the bleeding right now
- Corrective: Fix the specific instance
- Preventive: Ensure it never happens again
- Systemic: Address underlying patterns

For each action:
1. Describe the specific change
2. Link to which root cause(s) it addresses
3. Estimate effort and timeline
4. Identify owner/responsible party
5. Define success criteria

PRIORITIZATION:
- Address high-confidence, high-impact root causes first
- Quick wins before long-term fixes
- Preventive actions over repeated corrective actions

AVOID:
- Actions that only address symptoms
- Actions that create new problems
- "Try harder" or "be more careful" (not systemic fixes)

### Step 8: Create verification plan
Define how to verify the analysis is correct:

1. For each root cause:
   - What evidence would confirm this is truly a root cause?
   - What would disprove it?
   - How can we test it?

2. For the overall analysis:
   - If we fix the identified root causes, will the problem be solved?
   - How will we know the fix worked?
   - What metrics will we monitor?
   - How long until we can confirm success?

3. Define monitoring:
   - Leading indicators that show fix is working
   - Lagging indicators that confirm problem is solved
   - Triggers for reopening the analysis if problem returns

4. Plan for the fix failing:
   - If the fix doesn't work, what does that tell us?
   - What alternative causes should we investigate?


## When to Use
- After a failure or incident to prevent recurrence
- When symptoms keep recurring despite fixes
- When the cause of a problem is unclear
- During post-mortems and retrospectives
- When debugging complex system issues
- Before investing in solutions (to ensure you're solving the right problem)
- When multiple potential causes need systematic evaluation
- For quality improvement initiatives
- When pattern of failures suggests systemic issues

## Verification
- [ ] Context assessed and appropriate variant selected
- [ ] Problem statement is specific and solution-neutral
- [ ] Evidence was gathered before theorizing causes
- [ ] Multiple RCA techniques applied (unless RCA-Lite/Quick)
- [ ] Each root cause is supported by evidence
- [ ] Root causes are actionable (not just "bad luck" or "human error")
- [ ] Corrective actions address root causes, not just symptoms
- [ ] Verification plan exists to confirm the analysis
- [ ] If RCA-Full: predictions logged for calibration

---

## Niche Documentation

### Where This Skill Works Best
- After failures or incidents (post-mortem analysis)
- Recurring problems that persist despite fixes
- Complex issues with multiple potential causes
- When prevention is more valuable than just fixing
- High-stakes situations where understanding "why" matters

### Where This Skill Struggles
- Time-critical situations (use RCA-Lite)
- Simple, obvious problems (use RCA-Quick)
- Problems with no data/evidence available
- Pure future planning (no past incident to analyze)
- When cause is already known (jump to corrective action)

### Integration Points
- Often invoked from: /problem_identification, /failure_recovery
- Routes to: /failure_anticipation (prevent future), /procedure_improvement
- Related: /root_cause_5_whys, /systems_analysis, /debugging