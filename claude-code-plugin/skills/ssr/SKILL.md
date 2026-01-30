---
name: ssr
description: Capture learnings at end of session for continuous improvement. Reviews what worked, what did not, surprises, and procedure gaps.
---

# Session Review (Learning Capture)

Review the current session and capture learnings for future sessions.

**Input**: $ARGUMENTS (optional: specific area to focus review on)

---

## Purpose

Sessions contain valuable learning opportunities that are lost if not captured.
This procedure systematically extracts learnings to improve future sessions.

**Principle**: Every session should teach. Capture what worked, what did not, and what surprised you.

---

## Step 1: Session Summary

Summarize what happened in this session:

| Aspect | Description |
|--------|-------------|
| **User's initial input** | [what they brought] |
| **Type** | GOAL / PROBLEM / QUESTION / DECISION / SITUATION / FEELING |
| **Procedures invoked** | [list of /procedures used] |
| **Outcome** | [what was achieved] |
| **Session duration** | [if known] |

---

## Step 2: What Worked

Identify approaches that were effective:

| What Worked | Why It Worked | Reusable? |
|-------------|---------------|-----------|
| [approach 1] | [reason for success] | YES / NO |
| [approach 2] | [reason for success] | YES / NO |
| [approach 3] | [reason for success] | YES / NO |

**Questions to ask**:
- Which procedure generated the most value?
- What questions unlocked insight?
- What framing helped the user?
- What would I do again?

---

## Step 3: What Did Not Work

Identify approaches that were ineffective:

| What Did Not Work | Why It Failed | Avoidable? |
|-------------------|---------------|------------|
| [approach 1] | [reason for failure] | YES / NO |
| [approach 2] | [reason for failure] | YES / NO |

**Questions to ask**:
- Where did I go off track?
- What procedure was wrong for this situation?
- What assumption was incorrect?
- What would I skip next time?

---

## Step 4: Surprises

Identify unexpected findings:

| Surprise | Implication |
|----------|-------------|
| [unexpected finding 1] | [what it means for future] |
| [unexpected finding 2] | [what it means for future] |

**Questions to ask**:
- What was harder than expected?
- What was easier than expected?
- What did the user teach me?
- What did I not anticipate?

---

## Step 5: Procedure Gaps

Identify missing or inadequate procedures:

| Gap Type | Description | Proposed Solution |
|----------|-------------|-------------------|
| **Missing procedure** | [needed but does not exist] | [what it would do] |
| **Inadequate procedure** | [exists but insufficient] | [what needs improvement] |
| **Wrong chaining** | [procedures invoked in wrong order] | [correct order] |
| **Overly complex** | [procedure too heavy for situation] | [simpler alternative] |

---

## Step 6: Convergent Validation of Learnings

For each potential learning, apply convergent validation:

| Learning | Grounded? | Fixed Point? | Convergent? | Practical? | Score |
|----------|-----------|--------------|-------------|------------|-------|
| [learning 1] | [O/T/D marker?] | [stable under re-analysis?] | [multiple paths lead here?] | [actionable?] | [0-4] |
| [learning 2] | [O/T/D marker?] | [stable under re-analysis?] | [multiple paths lead here?] | [actionable?] | [0-4] |

**Decision**:
- 4 checks pass: Accept with high confidence
- 3 checks pass: Accept with medium confidence
- 2 checks pass: Flag for review (preliminary)
- <2 checks pass: Reject (do not capture)

---

## Step 7: Capture Validated Learnings

For each accepted learning, format for storage:

```
LEARNING CAPTURE:

ID: [auto-generated]
TYPE: what_worked | what_didnt | surprise | insight | pattern | procedure_gap
CONTENT: [the learning in one sentence]
CONTEXT: [when/where this applies]
DOMAIN: goal | problem | question | decision | situation | feeling | general
CONFIDENCE: high | medium | preliminary
EVIDENCE: [supporting evidence from session]
GROUNDING: [O: observed] | [T: tested] | [D: derived]
```

**Execute**: Store using `python scripts/session_learning.py capture [type] [content] [context]`

---

## Step 8: Review Previous Learnings

Check if any previous learnings were validated or contradicted in this session:

| Previous Learning | Session Evidence | Update |
|-------------------|------------------|--------|
| [learning ID] | [what happened] | VALIDATE / CONTRADICT / NO CHANGE |

**Execute**: Update using `python scripts/session_learning.py validate [learning_id] [true/false]`

---

## Step 9: Test Guess Outcomes

For any recommendations or actions taken based on guesses in this session:

| Recommendation | Based On Guess | Outcome | Update Confidence |
|----------------|----------------|---------|-------------------|
| [what was recommended] | [underlying guess] | WORKED / DIDNT_WORK / UNKNOWN | [increase/decrease/no change] |

**Questions to ask**:
- Did the recommended action achieve its goal?
- Did any assumption prove false?
- Did any guess prove correct?

**Capture outcomes**:
- If WORKED: `capture_learning(type="what_worked", content="[recommendation] based on [guess]")`
- If DIDNT_WORK: `capture_learning(type="what_didnt", content="[recommendation] failed because [reason]")`

---

## Step 10: Check for Contradictions

Review any potential conflicts detected:

**Execute**: `python scripts/session_learning.py conflicts`

For each conflict:
| Learning A | Learning B | Resolution |
|------------|------------|------------|
| [ID] [content] | [ID] [content] | KEEP_A / KEEP_B / KEEP_BOTH / NEEDS_MORE_DATA |

**Resolve**: Archive the contradicted learning using validate with false

---

## Output Format

```
## SESSION REVIEW

### Summary
- Input: [user's input]
- Type: [GOAL/PROBLEM/etc]
- Procedures: [list]
- Outcome: [result]

### What Worked
1. [learning] - [why]
2. [learning] - [why]

### What Did Not Work
1. [learning] - [why]

### Surprises
1. [finding] - [implication]

### Procedure Gaps
1. [gap] - [proposed solution]

### Learnings Captured
[list of learning IDs captured]

### Previous Learnings Updated
[list of learning IDs validated/contradicted]

### Recommendations for Future
1. [recommendation]
2. [recommendation]
```

---

## Integration Points

**At session end**: Invoke `/session_review` to capture learnings.

**At session start**: Retrieve relevant learnings with:
```bash
python scripts/session_learning.py context [domain]
```

**Periodically**: Review learning stats with:
```bash
python scripts/session_learning.py stats
```

---

## Execution Checklist

- [ ] Session summarized
- [ ] What worked identified (aim for 2-3)
- [ ] What did not work identified (aim for 1-2)
- [ ] Surprises noted
- [ ] Procedure gaps identified
- [ ] Learnings validated through convergent checks
- [ ] Accepted learnings captured to storage
- [ ] Previous learnings updated if applicable

---

**Execute now**: Review this session and capture learnings.
