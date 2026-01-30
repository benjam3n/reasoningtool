---
name: "pt - Progress Tracking"
description: "Monitor and report project status effectively"
---

# Progress Tracking

## Overview
Monitor and report project status effectively

## Steps

### Step 1: Collect progress data
Gather information on work completed and status:
1. Define what to track (select appropriate for project):
   Work completion:
   - Tasks/stories completed vs. planned
   - Milestones achieved
   - Deliverables produced
   - Features implemented
   Time:
   - Actual hours/effort expended
   - Calendar time elapsed
   - Time remaining estimates
   Cost (if budget is tracked):
   - Actual spending
   - Committed spending
   - Budget remaining
   Quality:
   - Defects found/fixed
   - Test coverage
   - Code review completion
   - User acceptance results
2. Establish collection mechanisms:
   - Daily standups (team verbal updates)
   - Task/issue tracking system updates
   - Time tracking entries
   - Milestone sign-offs
   - Deliverable acceptance
3. Collect from team:
   - Status on assigned tasks
   - Percent complete (caution: be specific about meaning)
   - Hours worked (if tracking effort)
   - Estimated time to complete
   - Blockers or issues
4. Gather from systems:
   - Pull data from project tracking tools
   - Extract from version control (commits, PRs)
   - Collect from CI/CD (builds, deploys)
   - Pull from testing systems (test results)

### Step 2: Calculate progress metrics
Compute quantitative measures of progress:
1. Basic progress metrics:
   Percent Complete (Scope):
   - Completed items / Total items
   - Be specific: completed means done-done (tested, accepted)
   Schedule Performance:
   - Planned work by now vs. actual work completed
   - Days ahead/behind schedule
   - Milestone status (on track/at risk/missed)
   Effort/Burn Rate:
   - Hours/effort consumed vs. planned
   - Current weekly burn rate
   - Effort remaining estimate
2. Velocity metrics (for iterative projects):
   - Points/items completed per sprint
   - Average velocity over last 3-4 sprints
   - Velocity trend (improving, declining, stable)
3. Earned Value basics (for cost-tracked projects):
   Planned Value (PV):
   - Budgeted cost of work scheduled by now
   - What should have been spent based on plan
   Earned Value (EV):
   - Budgeted cost of work actually performed
   - Value of work completed
   Actual Cost (AC):
   - Actual cost of work performed
   - What was actually spent
   Key Indicators:
   - Schedule Variance (SV) = EV - PV
     (positive = ahead, negative = behind)
   - Cost Variance (CV) = EV - AC
     (positive = under budget, negative = over)
   - Schedule Performance Index (SPI) = EV / PV
     (> 1 = ahead, < 1 = behind)
   - Cost Performance Index (CPI) = EV / AC
     (> 1 = under budget, < 1 = over)
4. Calculate forecast:
   - Estimate at Completion (EAC)
   - Estimated completion date based on current pace

### Step 3: Create visualizations
Build visual representations of progress:
1. Burndown chart:
   Shows remaining work over time:
   - Y-axis: Work remaining (points, tasks, hours)
   - X-axis: Time (days, sprints)
   - Ideal line: Straight line from start to target
   - Actual line: Actual remaining work
   Interpretation:
   - Above ideal = behind schedule
   - Below ideal = ahead of schedule
   - Flat sections = no progress (investigate)
   - Upward slope = scope added
2. Burnup chart (alternative):
   Shows work completed and scope over time:
   - Y-axis: Work (points, tasks)
   - X-axis: Time
   - Scope line: Total planned work
   - Completed line: Work done
   Advantage: Shows scope changes explicitly
3. Milestone tracker:
   Visual status of key milestones:
   - Milestone name and target date
   - Status (complete/on-track/at-risk/missed)
   - Color coding for quick assessment
4. Dashboard (for stakeholders):
   - Overall RAG status (Red/Amber/Green)
   - Key metrics at a glance
   - Trend arrows
   - Top issues
5. Keep visualizations simple:
   - One main message per chart
   - Consistent scales and colors
   - Easy to interpret quickly

### Step 4: Identify and manage blockers
Track and resolve impediments to progress:
1. Identify blockers:
   - Issues preventing task completion
   - Dependencies not met
   - Resource constraints
   - Technical problems
   - Decision delays
   - External delays (vendors, approvals)
2. For each blocker, document:
   - Description: What is blocked and why?
   - Impact: What work is affected?
   - Owner: Who is working to resolve?
   - Actions: What's being done?
   - Target resolution date
   - Status: Open/In Progress/Resolved
3. Prioritize blockers:
   - By impact on critical path
   - By number of people/tasks affected
   - By duration if unresolved
4. Escalate appropriately:
   - Blockers that persist without resolution
   - Blockers requiring authority beyond team
   - Blockers with significant schedule impact
   - Define escalation paths and timing
5. Drive resolution:
   - Daily focus on blocker resolution
   - Remove obstacles for the team
   - Involve right people to resolve
   - Track time blockers remain open
6. Learn from patterns:
   - Recurring blocker types
   - Root causes
   - Prevention opportunities

### Step 5: Analyze variances
Understand and explain deviations from plan:
1. Identify variances:
   - Compare actual progress to planned
   - Note schedule variances (ahead/behind)
   - Note effort variances (under/over)
   - Note scope variances (more/less than planned)
2. Analyze causes:
   For negative variances (behind):
   - Underestimation of complexity?
   - Resource issues (availability, skill)?
   - External dependencies?
   - Scope changes?
   - Technical problems?
   - Process inefficiencies?
   For positive variances (ahead):
   - Overestimation?
   - Efficiencies found?
   - Scope reduction?
   - Be cautious: is quality being sacrificed?
3. Assess significance:
   - Is variance within acceptable range?
   - Will variance self-correct or compound?
   - What's the impact on overall objectives?
4. Determine response:
   - Adjust plan (re-baseline)?
   - Add resources?
   - Reduce scope?
   - Accept schedule slip?
   - Implement process improvements?

### Step 6: Prepare status report
Create clear, useful status communication:
1. Status report structure:
   Executive summary:
   - Overall status (RAG)
   - One-line summary of current state
   - Key achievements this period
   - Top issues requiring attention
   Progress section:
   - Work completed this period
   - Milestone status
   - Key metrics and trends
   - Burndown/burnup chart
   Issues and risks:
   - Active blockers
   - Escalations needed
   - Risk updates
   Plan for next period:
   - Planned work
   - Key milestones upcoming
   - Decisions needed
2. Tailor for audience:
   Executive level:
   - High-level status only
   - Focus on outcomes and milestones
   - Key decisions needed
   - Brief (one page or less)
   Management level:
   - More detail on progress and issues
   - Resource and budget status
   - Risks and mitigations
   Team level:
   - Detailed task-level status
   - Daily/weekly coordination
   - Technical issues and solutions
3. Be honest and clear:
   - Report reality, not wishes
   - Bad news early, not late
   - Provide context for numbers
   - Recommend actions, don't just report problems
4. Make it actionable:
   - Clear asks for decisions
   - Specific help needed
   - Next steps defined

### Step 7: Communicate and follow up
Distribute status and drive actions:
1. Distribute status report:
   - Send to appropriate stakeholders
   - Post to project repository
   - Review in status meetings
2. Status meeting best practices:
   - Keep focused and time-boxed
   - Review status, don't create it
   - Focus on exceptions and actions
   - Capture decisions and action items
3. Follow up on actions:
   - Track action items to closure
   - Follow up on blocker resolution
   - Confirm decisions are implemented
   - Update status based on outcomes
4. Solicit feedback:
   - Is reporting useful?
   - Right frequency and detail?
   - Missing information?
   - Adjust based on feedback

### Step 8: Update baseline and forecast
Maintain accurate plans and projections:
1. Update task/activity status:
   - Mark completed items
   - Update remaining estimates
   - Adjust assignments as needed
2. Update forecast:
   - Estimated completion date
   - Estimated final cost
   - Expected final scope
   - Confidence level in forecast
3. Re-baseline if needed:
   Triggers for re-baselining:
   - Significant scope change approved
   - Major replanning occurred
   - Current baseline no longer meaningful
   Re-baseline process:
   - Document reason for re-baseline
   - Get sponsor approval
   - Maintain record of original baseline
   - Update all tracking to new baseline
4. Maintain historical data:
   - Keep records of actuals
   - Preserve variance history
   - Enable future estimation improvement


## When to Use
- Throughout project execution phase
- When stakeholders need visibility into progress
- When projects have schedule or budget constraints
- For distributed or remote teams needing coordination
- When projects have dependencies on other work
- When project health needs to be assessed
- At regular intervals (daily, weekly, monthly)

## Verification
- Progress data is accurate and current
- Metrics are calculated correctly
- Visualizations clearly show status
- Blockers are tracked and being resolved
- Variances are explained with root causes
- Status reports are timely and actionable
- Stakeholders are appropriately informed
- Forecasts are realistic based on actuals

---

**Input**: $ARGUMENTS

Apply this procedure to the input provided.