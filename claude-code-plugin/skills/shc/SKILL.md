---
name: "shc - System Health Check"
description: "Evaluate if the GOSM system needs improvement"
---

# System Health Check

## Overview
Evaluate if the GOSM system needs improvement

## Steps

### Step 1: Gather system telemetry
Collect all available system data for analysis:

1. Execution metrics:
   - Goals processed (attempted, completed, failed)
   - Strategies selected and their outcomes
   - Procedures executed and their success rates
   - Average time to goal completion

2. Quality indicators:
   - User satisfaction signals (if available)
   - Rework rate (how often plans/approaches changed)
   - Error rate by type

3. Coverage data:
   - Domains active vs inactive
   - Procedure library utilization
   - Gate coverage and activation

4. Trend data:
   - Metrics over time (improving? degrading?)
   - Anomalies or sudden changes

### Step 2: Evaluate procedure health
Analyze the health of the procedure library:

1. Success rate analysis:
   - Which procedures succeed most/least?
   - Are failure rates increasing for any procedures?
   - Are there patterns in failures?

2. Coverage analysis:
   - Which domains have good procedure coverage?
   - What operations lack procedures?
   - Are there redundant procedures?

3. Quality analysis:
   - Do procedures produce quality outputs?
   - Are procedures well-documented?
   - Do procedures have proper verification?

4. Usage analysis:
   - Which procedures are most/least used?
   - Are there procedures that should be retired?
   - Are there procedures that need updating?

### Step 3: Evaluate gate health
Analyze the health of gate evaluations:

1. Calibration analysis:
   - Are gates passing when they should?
   - Are gates failing when they should?
   - False positive rate (passes that shouldn't)
   - False negative rate (fails that shouldn't)

2. Coverage analysis:
   - Are all critical decision points gated?
   - Are there missing gates?
   - Are there redundant gates?

3. Accuracy analysis:
   - Do gate outcomes correlate with actual success?
   - Are gate criteria well-defined?
   - Are gate thresholds appropriate?

4. Performance analysis:
   - Are gates adding value or just overhead?
   - Time spent on gate evaluations
   - Gates that consistently rubber-stamp

### Step 4: Evaluate execution efficiency
Analyze how efficiently goals are being achieved:

1. Path efficiency:
   - Average steps to goal completion
   - Unnecessary detours or loops
   - Optimal vs actual path comparison

2. Time efficiency:
   - Time to first meaningful output
   - Time to goal completion
   - Bottleneck identification

3. Resource efficiency:
   - Compute/effort per goal
   - Rework and waste
   - Parallelization opportunities

4. Decision quality:
   - Strategy selection accuracy
   - Procedure selection accuracy
   - Course correction frequency

### Step 5: Evaluate learning and adaptation
Analyze if the system is improving over time:

1. Trend analysis:
   - Is success rate improving?
   - Is efficiency improving?
   - Is quality improving?

2. Learning indicators:
   - Are new procedures being added effectively?
   - Are procedures being refined based on feedback?
   - Is the system adapting to user patterns?

3. Knowledge quality:
   - Is stored knowledge accurate?
   - Is information becoming stale?
   - Are knowledge gaps being filled?

4. Meta-learning:
   - Is the system better at self-assessment?
   - Are health checks leading to improvements?
   - Is the improvement process itself improving?

### Step 6: Assess self-referential integrity
Evaluate if the system can reliably improve itself:

1. Meta-procedure health:
   - Are meta-procedures (like this one) working?
   - Can the system discover new procedures?
   - Can the system refine goals effectively?

2. Self-assessment accuracy:
   - Do health checks identify real problems?
   - Are recommendations actionable?
   - Are improvements actually implemented?

3. Stability analysis:
   - Could self-modification cause instability?
   - Are there safeguards against degradation?
   - Is there a recovery path if improvements fail?

4. Completeness check:
   - Can the system assess all its components?
   - Are there blind spots in self-awareness?
   - What can't the system evaluate about itself?

### Step 7: Calculate overall health
Synthesize dimension scores into overall assessment:

1. Calculate weighted health score:
   - Procedure health: 25%
   - Gate health: 15%
   - Execution efficiency: 25%
   - Learning & adaptation: 20%
   - Self-referential integrity: 15%

2. Determine health status:
   - healthy: score >= 0.8, no critical issues
   - needs_attention: 0.6 <= score < 0.8, or moderate issues
   - critical: score < 0.6, or any critical issues

3. Identify strengths:
   - Dimensions scoring > 0.8
   - Areas showing improvement trend
   - Things working as designed

4. Identify concerns:
   - Dimensions scoring < 0.7
   - Areas showing declining trend
   - Patterns in failures

### Step 8: Generate improvement plan
Create actionable improvement recommendations:

1. Immediate actions (do now):
   - Critical issues that need immediate attention
   - Quick wins with high impact
   - Safety or stability concerns

2. Short-term improvements (this week/month):
   - High-priority procedure gaps
   - Calibration adjustments
   - Efficiency optimizations

3. Long-term roadmap (this quarter):
   - New capabilities to add
   - Major refactoring needed
   - Learning system improvements

4. New procedures needed:
   - Gaps identified during analysis
   - Priority and complexity
   - Dependencies


## When to Use
- Scheduled periodic health assessment (weekly/monthly)
- After a sequence of execution failures
- When system performance seems degraded
- Before major system updates or changes
- When adding new domains or capabilities
- After significant usage period to calibrate
- When procedures consistently fail or produce poor results
- When user satisfaction or trust appears to decline
- After recovering from a critical failure

## Verification
- All health dimensions have been evaluated with scores
- Data gaps are acknowledged and don't invalidate conclusions
- Issues are specific enough to act on
- Recommendations are prioritized by impact and urgency
- Health status matches the evidence
- Self-referential limitations are acknowledged

---

**Input**: $ARGUMENTS

Apply this procedure to the input provided.