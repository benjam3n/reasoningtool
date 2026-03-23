---
name: "wawd - What Are We Doing"
description: "Force a full stop and honestly answer what is actually happening right now. Catches drift, confusion, lost purpose, cargo-culting, and the moment when activity replaced thinking."
output:
  format: "prose"
---

# What Are We Doing

**Input**: $ARGUMENTS

---

## Interpretations

Before executing, identify which interpretation matches the user's input:

**Interpretation 1 — Lost the thread**: The user (or their team/project) has been executing for a while and the original purpose has become unclear. They can describe what they're doing but not why. Activity is happening, but nobody can connect it to an outcome.
**Interpretation 2 — Sense of wrongness**: Something feels off. The user can't articulate what's wrong, but they have a growing suspicion that the current path doesn't lead where they think it does. The question is less "what are we doing" and more "should we be doing this at all."
**Interpretation 3 — Post-crisis clarity check**: Something just happened — a failure, a surprise, a shift. The user needs to reassess the entire situation from scratch rather than patching the old plan.
**Interpretation 4 — Accountability mirror**: The user suspects they (or their team) are performing work rather than doing work. Meetings are happening, documents are being produced, processes are being followed — but nothing is actually changing. They want an honest audit of whether the activity is producing results.
**Interpretation 5 — Scope explosion**: The user started with something clear and it has grown into something unrecognizable. They need to find the original thing again, or decide whether the new thing is actually better.
**Interpretation 6 — Multiple things at once**: The user has too many threads going and has lost the ability to say which one matters most. They need triage, not another to-do list.

If ambiguous, ask: "Are you feeling lost about the purpose, suspicious that something is off, recovering from a surprise, questioning whether the work is real, drowning in scope, or juggling too many things?"
If clear from context, proceed with the matching interpretation.

---

## Purpose

This skill exists for the moment when you stop and ask the question that nobody wants to ask: **what are we actually doing right now, and why?**

Most failure doesn't come from making bad decisions. It comes from continuing to execute a plan that stopped making sense three weeks ago. Teams drift. Individuals drift. Projects drift. The drift is invisible because everyone is busy. Busyness feels like progress. This skill interrupts the busyness and forces an honest answer.

---

## Step 1: Stop Everything and Describe

Before analyzing anything, produce a brutally honest snapshot.

**Answer these five questions. No jargon. No aspirational language. Only what is actually true right now.**

```
1. WHAT ARE WE DOING RIGHT NOW?
   [Describe the actual activity happening today — not the plan, not the goal,
   just what people are spending time on]

2. WHAT WERE WE SUPPOSED TO BE DOING?
   [The original intent. If you can't remember it clearly, that's a finding.]

3. WHAT IS THE GAP?
   [Difference between #1 and #2. "None" is a valid answer but a suspicious one.]

4. WHEN DID WE LAST CHECK WHETHER THIS STILL MAKES SENSE?
   [Date or "never" or "I don't remember"]

5. WHAT WOULD WE STOP DOING IF WE WERE HONEST?
   [The thing everyone knows is pointless but nobody will say out loud]
```

If you cannot answer question 1 in one sentence, that is itself the most important finding. You are doing too many things or you don't know what you're doing.

---

## Step 2: Classify the Situation

Based on Step 1, identify which pattern you're in:

### Pattern A: Drift

**Signal**: Question 3 reveals a gradual, unnoticed gap. Nobody decided to change direction — it just happened.

**How it works**: Small decisions accumulate. Each one made sense at the time. None of them were "change the plan." But collectively they moved you somewhere else entirely. Like walking in fog — each step feels straight but you end up miles off course.

**The question to answer**: Is the new direction actually better than the original? Sometimes drift takes you somewhere good by accident. Usually it doesn't.

**Action**:
1. Map the drift: list the 5 key decisions that moved you from original → current
2. For each: was this a conscious choice or did it just happen?
3. Evaluate the current position on its own merits — not as a deviation from the plan, but as a place to be
4. Decide: recommit to original, commit to current, or chart a new course
- → INVOKE: /sid $ARGUMENTS if the current situation needs fresh classification

---

### Pattern B: Cargo Culting

**Signal**: Question 5 has an obvious answer that everyone knows. Activities are happening because they've always happened, not because they produce results.

**How it works**: Someone once did X and it worked. X became a process. The process became a ritual. The ritual persists long after the conditions that made X work have changed. Nobody questions it because "that's how we do things."

**The question to answer**: For each major activity, can you trace a direct line from the activity to a result? Not a theoretical line — an actual observed result.

**Action**:
1. List every recurring activity (meetings, reports, reviews, processes)
2. For each: what result does this produce? (Not "what is it supposed to produce" — what does it actually produce?)
3. Activities with no traceable result: stop them for two weeks. See if anyone notices.
4. Activities with results: are the results still needed?
- → INVOKE: /pbtc on any justification for keeping an activity — is the justification genuine or pre-baked?

---

### Pattern C: Lost Purpose

**Signal**: Question 2 gets vague answers or disagreement. Nobody can state the purpose in one sentence, or different people state different purposes.

**How it works**: Purpose erodes gradually. It starts clear. Then edge cases appear. Then the edge cases become the focus. Then someone new joins and inherits the edge cases without the original context. Within a year, nobody remembers why.

**The question to answer**: If we started this today with everything we now know, would we start it at all? And if yes, would we do it this way?

**Action**:
1. Have every stakeholder independently write the purpose in one sentence
2. Compare the sentences. The divergence IS the finding.
3. If they converge: the purpose is clear, the execution drifted. Go to Pattern A.
4. If they diverge: the purpose was never clear, or it changed and nobody agreed on the new one.
5. Re-derive the purpose from first principles:
   - What problem does this solve?
   - Who has that problem?
   - How do we know they have it?
   - What happens if we do nothing?
- → INVOKE: /gu on the restated purpose to validate it

---

### Pattern D: Activity Theater

**Signal**: Question 1 produces a long list of activities. Question 4 reveals no recent checkpoint. People are busy but cannot point to what changed because of their busyness.

**How it works**: Organizations and individuals optimize for legibility over results. Meetings produce meeting notes. Documents produce more documents. Processes produce compliance artifacts. Everything looks productive. Nothing moves. The theater is not malicious — it emerges because visible activity is safer than invisible thinking.

**The question to answer**: If we deleted every artifact produced in the last month, what would be lost? Not theoretically — actually lost, as in someone would need it and not have it.

**Action**:
1. List everything produced in the last week/sprint/month
2. For each artifact: who consumed it? What did they do differently because of it?
3. If the answer is "nobody" or "nothing" — it's theater
4. Calculate the ratio: artifacts that changed a decision vs. artifacts that were produced
5. If ratio is below 20% — the work is mostly theater
- → INVOKE: /sdc $ARGUMENTS to check for self-deception about the value of the activity

---

### Pattern E: Scope Monster

**Signal**: Question 3 reveals the gap is large and growing. The current work bears little resemblance to what was originally planned.

**How it works**: Everything is connected to everything. Once you start pulling a thread, adjacent problems reveal themselves. Each one seems worth solving. Each addition is individually justified. Collectively they transform a focused effort into an everything-project that will never finish.

**The question to answer**: What is the smallest version of this that would matter?

**Action**:
1. List everything currently in scope
2. Force-rank by: "If we could only do ONE thing, which one?"
3. The answer to #2 is the project. Everything else is a different project.
4. For items 2-N: are any of these blocking item 1? If yes, they stay. If no, they leave.
5. Restate the scope in one sentence. If you can't, it's still too big.
- → INVOKE: /awtlytrn $ARGUMENTS to find the minimum viable version

---

### Pattern F: Plate Spinning

**Signal**: The user can name 5+ things they're "working on" but has made meaningful progress on zero of them in the last week.

**How it works**: Starting things feels productive. Finishing things is hard. So you start more things. Each new thing creates the dopamine of a new beginning without requiring the discipline of an ending. Eventually you're maintaining 12 things and advancing none.

**The question to answer**: If you could only work on one thing for the next two weeks, which one? (And: why haven't you been doing that?)

**Action**:
1. List every active thread
2. For each: last meaningful progress? (Date, not "recently")
3. Sort into: FINISH (close to done), KILL (won't finish, stop pretending), PARK (valid but not now)
4. You get a maximum of 3 in FINISH. Everything else is KILL or PARK.
5. For each KILL: what's the cost of abandoning it? (Usually much less than you think)
- → INVOKE: /to $ARGUMENTS to organize what remains

---

## Step 3: The Honesty Tests

After classifying, run these regardless of pattern:

### Test 1: The Stranger Test
If a competent stranger walked in and observed what you're doing for a day — with no context, no history, no relationships — what would they say you're doing? Would their description match yours?

### Test 2: The Results Test
Point to one concrete result from the last two weeks that would not have happened without your effort. Not an activity. Not a deliverable. A result — something in the world that changed.

### Test 3: The Obituary Test
If this project/effort ended today, what would the one-sentence summary be? "We spent 6 months and..." what?

### Test 4: The Energy Test
When you think about the work, do you feel energy or obligation? Energy usually means the work matters. Obligation usually means you're maintaining something that should have ended.

```
HONESTY TEST RESULTS:

Stranger Test: A stranger would say we are [doing what]
Results Test: Concrete result from last two weeks: [what, or "none"]
Obituary Test: "We spent [time] and [what]"
Energy Test: [energy / obligation / dread / numbness]
```

---

## Step 4: Verdict and Next Move

```
WHAT ARE WE DOING:
[One honest sentence]

WHAT SHOULD WE BE DOING:
[One honest sentence — may be the same, may be very different]

THE GAP:
[What needs to change — or "no gap, carry on"]

PATTERN:
[Drift / Cargo Culting / Lost Purpose / Activity Theater / Scope Monster / Plate Spinning]

RECOMMENDED ACTION:
[Specific, concrete next step — not "think about it" but "do X by Y"]
```

---

## Quick Version

For when you just need a 30-second gut check:

```
WAWD QUICK CHECK:

1. What am I doing right now? [one sentence]
2. Why? [one sentence]
3. Is it working? [yes/no/don't know]
4. If "don't know" — how would I tell?
5. What would I do differently if I started today?
```

If your answer to #5 is different from #1, you have drift. Address it.

---

## Quality Checklist

Before completing:
- [ ] Five snapshot questions answered honestly (Step 1)
- [ ] Pattern identified with evidence (Step 2)
- [ ] Pattern-specific actions provided
- [ ] All four honesty tests applied (Step 3)
- [ ] Verdict states what IS happening and what SHOULD happen (Step 4)
- [ ] Recommended action is specific and concrete

---

## Integration

- **Use from**: /meta (when the user needs orientation), /lost (when the user is stuck), /cnfsd (when confusion is about purpose, not content), /panic (after the panic subsides and reality needs assessment)
- **Routes to**: /sid (fresh situation classification), /pbtc (check justifications for current path), /sdc (self-deception about value of work), /gu (validate restated purpose), /awtlytrn (find minimum viable scope), /to (organize remaining work), /decide (when a real choice emerges)
- **Differs from**: /sid (sid asks "what is happening"; wawd asks "what are we doing about it and should we be"), /meta (meta orients to available tools; wawd audits current activity), /statous (statous resumes prior work; wawd questions whether to continue it)
- **Complementary**: /pbtc (is our justification for the current path pre-baked?), /ecal (is our confidence in the current path calibrated?), /sid (what is actually happening vs what we think is happening?)
