# /story Tell the story of someone who used /rca on a recurring problem and finally solved it
**Date:** 2026-03-09
**Skill:** /story (Story)

---

## Step 1: Story Type

**SCENARIO** — Explore a realistic situation through context, events, and consequences. This is a demonstration narrative: it needs to feel like something that actually happened to someone, showing the /rca procedure in action against a real recurring problem.

---

## Step 2: Core

```
CORE:
Theme: The difference between fixing symptoms and finding root causes
Stakes: A team lead's credibility, a product's reliability, and the slow erosion of trust that comes from saying "we fixed it" too many times
Perspective: Nadia, an engineering manager at a mid-size SaaS company
Target emotion: Recognition — the reader should feel the familiar frustration of whack-a-mole problem-solving, then the relief of finally understanding why
```

---

## Step 3: Elements

### Characters
- **Nadia**: Engineering manager, 3 years at the company. Competent, trusted, increasingly frustrated. Believes she runs a disciplined team — that belief is about to get tested.
- **The team**: Five engineers who have each, individually, "fixed" the same category of problem.

### Setting
- A B2B SaaS company. The product is a scheduling platform used by healthcare clinics. Reliability matters — when appointments get dropped, patients don't get seen.

### Conflict
- Person vs system. The problem isn't any one person's mistake. It's a gap in how the team operates that no individual can see from their vantage point.

### Arc
- **Beginning**: A known bug keeps coming back in slightly different forms.
- **Middle**: Nadia stops treating each recurrence as a new incident and runs /rca on the pattern itself.
- **End**: The root cause turns out to be something nobody was looking at. The fix is structural, not technical.

---

## Step 4–5: The Story

---

**The Appointment That Kept Disappearing**

The third time it happened, Nadia didn't slam her laptop shut. She'd learned not to. But she did close her eyes for a four-count breath before opening the incident channel.

`#p1-appt-sync-failure` — the name was getting familiar. A clinic in Tucson had lost sixty-two appointments from their Thursday schedule. Patients showed up to locked doors. The clinic manager's email had the subject line "This is unacceptable" and a body that made the subject line look restrained.

Nadia scrolled through the thread. Raj had already identified the proximate cause: a race condition in the calendar sync module. Two write operations hitting the same time slot within a 40ms window. He'd patched it by 11 AM, added a mutex lock, and pushed a hotfix.

She'd seen this before. Not this exact bug — the last time it was a timezone conversion issue that silently dropped appointments crossing midnight. The time before that, a retry loop that duplicated entries until the database rejected them, then deleted the originals. Three different bugs. Three confident fixes. One pattern: appointments vanish, patients suffer, the team scrambles.

She opened a document and typed at the top: **Why do appointment sync failures keep recurring despite being fixed each time?**

Not "why did the race condition happen." She'd done that. Raj had done that. The question was bigger.

---

She started with what she knew.

The timeline went back eleven months. She pulled every incident tagged `appointment-sync` or `calendar-reliability` from the tracker. There were seven. Seven incidents in eleven months, each investigated independently, each closed with a fix and a green checkmark.

She listed what had changed before each incident. Two were triggered by deploys. One followed a database migration. One appeared after a partner API updated their rate limits. Three had no obvious trigger at all — they'd been latent, waiting.

Then she wrote down what had been tried. Seven fixes by four different engineers. A mutex here. A retry cap there. A validation layer. A timeout extension. Each fix was correct. Each addressed its specific bug. None had prevented the next one.

She stared at the list and wrote: *What makes it better or worse?* The incidents clustered. Three in March, two in June, two now in September. She checked the release calendar. Each cluster followed a sprint where the scheduling module had been touched for a feature addition.

---

She ran the 5 Whys on the pattern, not the instance.

**Why do sync failures keep recurring?**
Because each incident has a different proximate cause — race conditions, timezone bugs, retry failures.

**Why are there so many different ways for sync to fail?**
Because the calendar sync module has grown complex. It handles six partner integrations, three internal calendar formats, and custom scheduling rules per clinic.

**Why is the module so complex?**
Because every new feature and integration has been added to the same monolithic sync function. It started as 200 lines four years ago. It's now 3,400 lines with seventeen conditional branches.

**Why hasn't it been refactored?**
Because each time it breaks, the fix is small — a patch, a guard clause, a lock. Nobody sees the cumulative complexity because each engineer only debugs their slice.

**Why does nobody see the cumulative complexity?**
Because there's no ownership of the module as a whole. It's shared code. Five engineers have committed to it in the last year. None of them own it. The incident post-mortems close when the specific bug is fixed — nobody's post-mortem has ever scoped beyond the single incident.

She underlined the last answer twice.

---

She pulled up the Ishikawa categories and worked through them.

**Methods**: Post-mortems were scoped to single incidents. No process existed to look across incidents for patterns. The definition of "resolved" was "this specific bug won't happen again," not "this category of failure won't happen again."

**Tools**: The incident tracker had no way to link related incidents. Each lived in its own ticket. The seven failures looked like seven unrelated problems because the tooling presented them that way.

**People**: Not a skills issue. Every engineer who'd patched the module was competent. But there was no module owner — nobody whose job it was to understand the sync system end-to-end. Knowledge was fragmented across five people who each understood their own fix but not the whole.

**Measurement**: They tracked mean-time-to-resolution per incident. That number looked good — usually under four hours. What they didn't track was recurrence rate by subsystem. The metric that would have screamed at them didn't exist.

---

Three root causes surfaced.

First: **no module ownership**. Shared code with no steward meant nobody held the full picture. Complexity accumulated invisibly.

Second: **incident scoping was too narrow**. Post-mortems asked "why did this fail?" but never "why does this keep failing?" The process stopped one level too early.

Third: **no cross-incident pattern tracking**. The tooling and metrics made each failure look novel. The recurrence was invisible to anyone who didn't manually dig through eleven months of tickets, which is exactly what nobody had done until today.

She ranked them. Module ownership was the deepest — fix that, and someone would naturally catch the other two. But all three needed action.

---

She brought it to the Monday sync. No slides. Just the document.

"We've fixed this bug seven times," she said. "Every fix was correct. The problem is that we've been fixing leaves and the root is still growing."

She proposed three changes. First, assign a module steward for calendar sync — Raj volunteered. His job wasn't to write all the code but to review every change, hold the mental model of the whole system, and flag when complexity was creeping. Second, modify the post-mortem template: add a required field — *"Is this a recurrence of a previous failure pattern? If yes, link related incidents and analyze the pattern, not just the instance."* Third, add a subsystem recurrence dashboard. Simple. How many P1s per module per quarter. The number would either go down or it wouldn't.

The refactor happened over six weeks. Raj broke the 3,400-line function into four bounded modules with explicit contracts between them. Not because anyone told him to, but because once he owned it and read the whole thing end-to-end, the seams were obvious. The guard clauses and patches his teammates had added were correct individually and incoherent collectively — three of them partially duplicated each other's logic, and one masked a failure mode that another was trying to surface.

---

The next quarter, appointment sync had zero P1 incidents. Not because the code was perfect. Raj caught two potential issues in code review before they shipped — he could see them because he held the full context. One was exactly the kind of bug that would have become incident number eight.

The quarter after that, Nadia noticed something else. The post-mortem template change had spread. Other teams had started asking "is this a recurrence?" on their own incidents. Two of them found patterns they'd been patching for months.

She went back to her document and added one line at the bottom:

*The root cause was never the code. It was that nobody was looking at the right level.*

---

## Step 6: Reflection

```
STORY ANALYSIS:
Theme: Symptom-fixing vs. root-cause-finding — the difference between resolving an incident and resolving a pattern
Key insight: The /rca procedure's power isn't in the 5 Whys or the fishbone diagram alone — it's in the discipline of asking "what is the real problem?" before asking "what is the fix?" Nadia's breakthrough was scoping the RCA to the pattern (recurring sync failures) instead of the instance (this week's race condition).
Connection to input: The story demonstrates /rca's Interpretation 2 (recurring pattern diagnosis) and shows why the technique's insistence on evidence-gathering before theorizing, and its multiple analytical lenses (5 Whys, Ishikawa), catch what ad-hoc debugging misses.
What the story tests: The assumption that competent people fixing bugs correctly should eventually make the bugs stop. The story shows that individual competence without structural awareness produces an endless cycle of correct but insufficient fixes.
```
