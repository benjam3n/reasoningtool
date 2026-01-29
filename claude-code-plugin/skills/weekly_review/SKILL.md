---
name: weekly_review
description: "Weekly review procedure to maintain visibility across all active projects, identify stalled work, and ensure continuous progress."
---

# Weekly Review

## Overview
Weekly review procedure to maintain visibility across all active projects, identify stalled work, and ensure continuous progress.

## Steps

### Step 1: Gather project status
Review all active projects:

1. List all projects with status != COMPLETE/ARCHIVED

2. For each project, check STATE.md:
   - Last updated date
   - Current phase
   - Health indicator
   - Progress percentage
   - Current blockers

3. Note key metrics:
   - Days since last update
   - Phase progress
   - Any explicit blockers listed

Quick status check (can be automated):
- Run: find projects/ -name "STATE.md" -mtime +7
- This finds projects not updated in 7+ days

### Step 2: Identify issues
Flag projects needing attention using these criteria:

STALLED: STATE.md not updated in >7 days
- These projects are drifting
- Action: Update status or explicitly pause

BLOCKED: Has explicit blocker listed
- Progress cannot continue until resolved
- Action: Escalate or work around blocker

AT RISK: Health indicator is yellow or red
- Project is struggling but not blocked
- Action: Diagnose cause, consider recovery procedure

OFF TRACK: Behind milestone schedule
- Dates slipping from original plan
- Action: Adjust plan or increase focus

For each flagged project:
- Note the specific issue
- Identify potential action
- Estimate effort to address

### Step 3: Update stale projects
For each project with stale STATE.md:

1. Open STATE.md and review current state

2. Update progress indicators:
   - Progress percentages by phase
   - Key metrics if defined
   - Health indicator based on reality

3. Update blockers list:
   - Add any new blockers discovered
   - Remove resolved blockers
   - Note blocker age if persisting

4. Update "Last Updated" timestamp

5. If project is actually paused:
   - Change status to PAUSED
   - Document why paused
   - Set expected resume date if known

Goal: Every active project has STATE.md updated within last 7 days.

### Step 4: Plan coming week
Set focus for the coming week:

1. Review capacity
   - How many hours available for project work?
   - Any scheduled commitments that affect capacity?
   - Energy level and sustainability?

2. Select priority projects (1-3 max)
   - Which projects need attention most?
   - Which are closest to milestone/completion?
   - Which have external dependencies or deadlines?

3. Set specific weekly goals for each priority
   - What concrete deliverable by end of week?
   - What would "good progress" look like?
   - What's the minimum acceptable progress?

4. Schedule time blocks if helpful
   - When will you work on each priority?
   - Are there dependencies between projects?

5. Note dependencies and deadlines
   - External meetings or reviews scheduled?
   - Blockers that must be resolved first?

### Step 5: Retrospect on last week
Review what happened last week:

1. What got completed?
   - List accomplishments
   - Celebrate progress (even small wins)

2. What didn't get done?
   - List items that slipped
   - Identify why they slipped
   - Decide: reschedule, delegate, or drop

3. What worked well?
   - Practices to continue
   - Conditions that helped

4. What didn't work?
   - Obstacles encountered
   - Practices to change
   - Patterns to watch

5. Procedure usage
   - Which procedures were used?
   - Log significant uses for effectiveness tracking

### Step 6: Log procedure usage
If any procedures were used significantly this week:

1. For each procedure used:
   - Which procedure?
   - Which project?
   - What was the outcome?
   - How valuable was it? (HIGH/MEDIUM/LOW)

2. Add entries to PROCEDURE_USAGE.md

3. Note any procedure improvements needed
   - Was anything unclear?
   - Were any steps missing?
   - Did it produce expected output?

This feeds the procedure_effectiveness tracking system.

### Step 7: Generate review document
Compile all findings into weekly review document:

1. Create document using template
2. Fill in all sections:
   - Portfolio Status table
   - Flags section (stalled, blocked, at risk)
   - This Week's Focus (priorities and goals)
   - Last Week Retrospective
   - Notes and observations

3. Save to reviews/ directory or designated location
   - Filename format: YYYY-MM-DD_weekly_review.md

4. Update any project STATE.md files with links to review


## When to Use
- Every week at a consistent scheduled time
- When returning from vacation or extended break
- After completing a major project milestone
- When feeling overwhelmed by multiple projects
- Before starting a new project to assess capacity
- When project status feels unclear or uncertain
- After any significant life or work change that affects capacity

## Verification
- All active projects have current status captured
- Stalled projects are either updated or explicitly paused
- 1-3 priority projects selected with specific goals
- Last week's goals are accounted for
- Review document is saved for future reference
- Time to complete review is reasonable (30-60 min)

---

**Input**: $ARGUMENTS

Apply this procedure to the input provided.