---
name: eda
description: "Maintain project continuity through event monitoring and automated state management"
---

# Event-Driven Automation

## Overview
Maintain project continuity through event monitoring and automated state management

## Steps

### Step 1: Initialize state tracking
Create or validate the STATE.md file structure:

Required sections:
1. Current State - active phase and entry time
2. Waiting For - pending items with deadlines
3. Scheduled Actions - time-based triggers
4. Recent Events - log of processed events
5. Context for Resume - information for next session

If STATE.md exists, validate structure.
If not, create from template.

SAFETY: State file must be in allowed project directory.
Never create state files in system directories.

### Step 2: Read current state
Load complete context for decision-making:

1. Read STATE.md:
   - Current phase/state
   - Pending items and deadlines
   - Scheduled actions due
   - Recent history

2. Read project context:
   - COMPLETE_PLAN.md if exists
   - DECISION_TREE.md if exists
   - Stakeholder database

3. Identify what's changed:
   - Time elapsed since last activity
   - Scheduled actions now due
   - External inputs received

SAFETY: Only read files in project directory.
Validate file contents before processing.

### Step 3: Check for trigger events
Monitor all configured trigger sources:

EMAIL TRIGGERS:
- Check inbox for new messages
- Match sender to stakeholder database
- Classify response type (positive/negative/question/redirect/OOO)
- Extract key information

TIME TRIGGERS:
- Compare scheduled actions to current time
- Identify all actions now due
- Check deadline proximity

DATA TRIGGERS:
- Check external data sources if configured
- Compare to previous values
- Identify significant changes

MANUAL TRIGGERS:
- Human explicitly resumed project
- Explicit command received

SAFETY: Use only configured, approved data sources.
Rate-limit external checks to prevent abuse.
Log all trigger checks with timestamps.

### Step 4: Process email responses
For each email event, process according to classification:

POSITIVE (will support):
- Extract commitment details
- Update stakeholder status to "engaged"
- Queue: send draft letter/next steps
- Log positive response

NEGATIVE (decline):
- Log response and reason if given
- Update stakeholder status to "declined"
- Remove from active outreach
- Check if fallback stakeholder needed

QUESTION (needs answer):
- Parse each question
- Generate accurate answers from project data
- Queue response for approval
- Keep stakeholder in "engaged" status

REDIRECT (contact someone else):
- Extract new contact information
- Add to stakeholder database
- Queue outreach to new contact
- Thank original contact

OUT OF OFFICE:
- Note return date
- Schedule follow-up for return + 1 day
- Update stakeholder status

SAFETY: All generated responses require human approval.
Never auto-send without explicit approval configuration.

### Step 5: Process time triggers
For each due scheduled action:

FOLLOW-UP DUE:
- Check stakeholder status (still waiting?)
- Generate appropriate follow-up
- Queue for approval or auto-send if configured

DEADLINE APPROACHING:
- Calculate time remaining
- Assess current progress
- Generate alert if behind schedule
- Recommend acceleration or pivot

GATE ASSESSMENT DUE:
- Gather gate criteria
- Evaluate current state against criteria
- Generate gate assessment report
- Recommend pass/fail/conditional

PHASE DEADLINE REACHED:
- Assess phase completion
- Document what was achieved
- Recommend phase transition or extension

SAFETY: Escalate to human if deadline at risk.
Never silently miss important deadlines.

### Step 6: Update state machine
Apply state transitions based on events:

For each event, check state machine rules:
1. What state are we currently in?
2. Does this event trigger a transition?
3. If yes, what's the new state?
4. What entry actions for new state?

Update STATE.md:
- New current state (if changed)
- Waiting-for list (add/remove items)
- Scheduled actions (add new, remove completed)
- Recent events log (append new events)

Document transition:
- Old state -> New state
- Trigger event
- Timestamp
- Any conditions or notes

SAFETY: Validate all transitions against defined rules.
Log unexpected transitions for human review.

### Step 7: Generate next actions
Based on new state, determine what happens next:

AUTONOMOUS ACTIONS (can proceed without approval):
- Update internal tracking
- Log events and decisions
- Generate drafts for review
- Schedule future checks

APPROVAL-REQUIRED ACTIONS:
- External communications
- Resource commitments
- State changes with external impact
- Anything flagged as sensitive

HUMAN-REQUIRED ACTIONS:
- Decisions requiring judgment
- Situations outside decision tree
- Escalations and exceptions
- Creative or strategic choices

For each action:
- Describe what needs to happen
- Explain why it's needed
- Provide draft/recommendation
- Indicate urgency level

SAFETY: Default to requiring approval for external actions.
Only auto-execute if explicitly configured and safe.

### Step 8: Execute safe actions
Execute actions that are safe for autonomous execution:

INTERNAL UPDATES:
- Save updated STATE.md
- Update stakeholder database
- Log all events and decisions
- Schedule next triggers

DRAFT GENERATION:
- Create response drafts
- Prepare follow-up emails
- Generate reports

MONITORING SETUP:
- Schedule next event check
- Set deadline reminders
- Configure alerts

SAFETY: Only execute actions explicitly allowed.
Log everything for audit trail.
Never execute external actions without approval.

### Step 9: Queue for approval
Prepare approval requests for human review:

For each approval-required action:
1. Summarize what action is proposed
2. Explain the context and reasoning
3. Show the draft content (if applicable)
4. Indicate deadline/urgency
5. Provide approve/reject/modify options

Format for easy review:
- One clear summary per action
- Draft content visible
- Easy approve/reject mechanism
- Option to modify before approving

SAFETY: Make it easy for human to understand and decide.
Never rush approval on sensitive actions.
Provide full context for informed decision.

### Step 10: Generate alerts and summary
Create summary for human awareness:

ALERTS (need attention):
- Deadlines at risk
- Unexpected responses
- Errors or failures
- Escalation triggers

SUMMARY (FYI):
- What happened since last check
- Current state overview
- Pending items status
- Next scheduled actions

RECOMMENDATIONS:
- Suggested next steps
- Decision points approaching
- Optimization opportunities

SAFETY: Surface important information clearly.
Don't bury critical alerts in noise.

### Step 11: Document for continuity
Ensure next session has full context:

Update "Context for Resume" section:
- What we're doing (brief summary)
- What we're waiting for (pending items)
- Next decision point (what triggers action)
- Key information (anything session needs)

Save audit log:
- All events processed
- All decisions made
- All state changes
- All actions taken

SAFETY: State must be recoverable from files alone.
Document everything needed to resume without memory.


## When to Use
- Projects requiring stakeholder responses (email, calls)
- Multi-day or multi-week execution timelines
- Tasks with time-based triggers (follow-ups, deadlines)
- Workflows with multiple concurrent threads
- When human availability is limited
- Projects with well-defined state transitions
- Competition or deadline-driven work
- Coordinating activities across multiple stakeholders

## Verification
- State file is valid and complete
- All trigger sources checked
- Events properly classified and processed
- State transitions follow defined rules
- External actions have human approval
- Audit trail is complete
- Context preserved for next session
- No deadlines silently missed

---

**Input**: $ARGUMENTS

Apply this procedure to the input provided.