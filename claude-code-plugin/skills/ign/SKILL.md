---
name: "ign - Decide What to Ignore"
description: "Decide what information, concerns, and possibilities to deliberately ignore. Productive neglect through systematic triage."
---

# Decide What to Ignore

**Input**: $ARGUMENTS

---

## Depth Scaling

Default: 2x. Parse depth from $ARGUMENTS if specified (e.g., "/ign 4x [input]").

| Depth | Min Passes | Min Assessments | Min Reversals | Min Documented |
|-------|-----------|----------------|--------------|---------------|
| 1x    | 1         | 3              | 1            | 3             |
| 2x    | 2         | 5              | 2            | 5             |
| 4x    | 3         | 8              | 4            | 8             |
| 8x    | 4         | 12             | 6            | 12            |
| 16x   | 5         | 18             | 10           | 18            |

These are floors. Go deeper where insight is dense. Compress where it's not.

---

## STEP 0: WHAT TYPE OF TRIAGE IS THIS?

Before starting, identify what you are trying to filter. Read each row and pick the one that best matches your situation.

| You have... | Go to... | Example |
|---|---|---|
| Too many factors in a decision | **SECTION A**: Decision Factor Triage | "Should I take this job?" and you have 30 pros/cons |
| Too many objections or concerns | **SECTION B**: Objection Triage | Someone raised 15 problems with your plan |
| Too much information or data | **SECTION C**: Information Triage | Research produced 200 articles, need to pick 10 |
| Too many possibilities or options | **SECTION D**: Option Triage | Brainstorm produced 40 ideas, need to pick 3 |
| Too many tasks or demands | **SECTION E**: Task/Attention Triage | Your to-do list has 50 items and you have 4 hours |
| General overwhelm, not sure what type | Start at **SECTION A**, it will redirect you |

---

## SECTION A: DECISION FACTOR TRIAGE

*Use when you have too many factors, pros, cons, or considerations for a decision and need to reduce them to a manageable set.*

### Glossary
| Term | Definition |
|---|---|
| Factor | Any piece of information, concern, pro, con, or consideration related to your decision |
| Core objective | The single most important thing you are trying to achieve with this decision |
| Kill criterion | A factor so important that it alone can determine the decision regardless of everything else |
| Signal redundancy | When two or more factors are telling you the same thing in different words |

### Prerequisites
- A written list of all factors you are currently considering (if not written down, write them down first -- every single one, no matter how small)
- Knowledge of what decision you are trying to make (one sentence: "I am trying to decide ___")

---

**Step A1: Write your core objective in one sentence.**

Write: "The single most important outcome I want from this decision is ___."

If you cannot write this sentence, you are not ready to triage. First clarify what you actually want.

*What you should see*: A single sentence with one clear desired outcome. Not two outcomes connected by "and." If you wrote "and," pick the one that matters more.

---

**Step A2: Sort every factor into exactly one of three piles.**

Go through your list item by item. For each factor, ask ONE question:

> "If I learned the answer to this factor right now, would it change my decision?"

- If YES or PROBABLY YES --> put in **Pile 1: Keeps**
- If MAYBE --> put in **Pile 2: Parking Lot**
- If NO or PROBABLY NOT --> put in **Pile 3: Cuts**

Rules:
- Spend no more than 10 seconds per item on this first pass
- Do not deliberate. Go with your first reaction.
- It is fine if Pile 1 is still large. We will reduce it further.

*What you should see*: Three piles. Pile 3 (Cuts) should be at least 30% of your original list. If it is less than 30%, you are being too cautious -- go back and be more aggressive. Ask yourself: "Am I keeping this because it actually matters, or because I am afraid of missing something?"

---

**Step A3: Check the Cuts pile for hidden killers.**

Go through Pile 3 (Cuts) one more time. For each item, ask ONE question:

> "If I completely ignore this, what is the WORST thing that could happen?"

- If the worst case is **catastrophic or irreversible** (you would lose more than 50% of what you care about) --> move to **Pile 1: Keeps**
- If the worst case is **annoying but recoverable** --> leave in Pile 3: Cuts
- If you genuinely cannot imagine a bad outcome --> leave in Pile 3: Cuts

*What you should see*: 0-3 items moved from Cuts back to Keeps. If you moved more than 3, you are catastrophizing -- most things are not actually catastrophic. Go back and ask: "Has this bad outcome actually happened to anyone I know of?"

---

**Step A4: Deduplicate the Keeps pile.**

Look at Pile 1 (Keeps). Group items that are saying the same thing in different words.

Example: "Good salary" and "strong compensation package" and "pays well" are the same factor expressed three ways. Keep ONE representative item and move the rest to Pile 3 (Cuts).

For each group, keep the version that is most specific and measurable. "Pays $150K+" is better than "pays well."

*What you should see*: Pile 1 reduced by 20-40% through deduplication.

---

**Step A5: Rank the remaining Keeps by decision-flipping power.**

For each item still in Pile 1, score it 1-3:

- **3 = Decision flipper**: This factor alone could change my decision from Option A to Option B (or vice versa)
- **2 = Decision influencer**: This factor shifts my confidence but would not flip the decision alone
- **1 = Decision confirmer**: This factor supports a direction I would likely go anyway

Keep all 3s. Keep all 2s only if you have fewer than 10 items total. Move all 1s to Pile 3 (Cuts).

*What you should see*: 3-7 factors remaining. This is your working set. If you have more than 7, you are still holding too much -- force-rank and cut the bottom items. Research consistently shows that humans cannot effectively weigh more than 7 factors simultaneously.

---

**Step A6: Process the Parking Lot.**

Look at Pile 2 (Parking Lot). For each item, ask:

> "Can I get a definitive answer on this with less than 30 minutes of effort?"

- If YES --> spend the 30 minutes, then sort the result into Keeps or Cuts based on what you learn
- If NO --> move to Pile 3 (Cuts) with a note: "Deferred -- revisit if decision is still unclear after analyzing Keeps"

*What you should see*: Parking Lot is now empty. Everything is either a Keep or a Cut.

---

**Step A7: Aggregate check on Cuts.**

Look at Pile 3 (Cuts) as a whole. Ask ONE question:

> "If ALL of these cut items pointed in the same direction (all saying 'choose Option A' or all saying 'choose Option B'), would that change my decision?"

- If YES --> your cuts are too aggressive. Move the 3-5 most impactful items from Cuts back to Keeps and redo Step A5.
- If NO --> your triage is complete. Proceed with only the Keeps.

*What you should see*: Confidence that even in the worst case, the ignored factors would not overturn your decision.

---

**Step A8: Document what you ignored and why.**

Write one sentence per cut item explaining why it was cut. This is not busywork. It serves two purposes:
1. If your decision goes wrong later, you can check whether an ignored factor was the cause
2. It forces you to articulate the reason, which catches items you cut for bad reasons (e.g., "I cut this because it scares me" is a bad reason)

Format:
```
IGNORED: [Item] -- REASON: [Why it was cut]
```

**Output of Section A**: A list of 3-7 factors to focus on, plus a documented record of what was deliberately ignored and why.

---

## SECTION B: OBJECTION TRIAGE

*Use when someone (or your own inner critic) has raised multiple objections, concerns, or problems with a plan, and you need to decide which ones deserve a response.*

---

**Step B1: List all objections in their raw form.**

Write down every objection exactly as stated. Do not rephrase, soften, or combine them yet.

*What you should see*: A numbered list. If it is fewer than 5, you may not need triage -- just address them all. Proceed to Step B2 only if you have 5 or more objections.

---

**Step B2: Classify each objection.**

For each objection, determine its type by asking these questions in order. Stop at the first YES.

1. "Does this objection identify a way the plan could FAIL ENTIRELY (not just perform worse)?"
   - If YES --> Label: **STRUCTURAL** (a fundamental flaw)
2. "Does this objection identify a real cost or downside that would definitely occur?"
   - If YES --> Label: **TRADE-OFF** (a real price you would pay)
3. "Does this objection describe something that MIGHT happen but is uncertain?"
   - If YES --> Label: **RISK** (a possibility, not a certainty)
4. "Does this objection say the plan is not IDEAL compared to some theoretical better plan?"
   - If YES --> Label: **PERFECTIONISM** (letting perfect be the enemy of good)
5. "Does this objection apply to EVERY possible option equally, not just this one?"
   - If YES --> Label: **UNIVERSAL** (not specific to this choice)
6. If none of the above --> Label: **UNCLEAR** (needs clarification before it can be processed)

---

**Step B3: Apply triage rules by type.**

| Type | Rule |
|---|---|
| STRUCTURAL | **NEVER IGNORE.** These must be addressed or the plan must change. |
| TRADE-OFF | **KEEP 3-5 most significant.** Ignore trade-offs that affect less than 10% of the value. |
| RISK | **Keep only if** probability > 20% AND impact > 25% of total value. Otherwise, note and ignore. |
| PERFECTIONISM | **IGNORE ALL.** You are comparing to an option that does not exist. |
| UNIVERSAL | **IGNORE ALL.** If it applies to every option, it cannot help you choose between them. |
| UNCLEAR | **Clarify first.** Ask the objector: "Can you describe specifically what would go wrong?" Then reclassify. |

---

**Step B4: For each kept objection, determine: address or accept?**

For each objection you kept, ask:

> "Can I modify my plan to eliminate or reduce this concern for less than 20% of the plan's total cost/effort?"

- If YES --> **ADDRESS IT** (modify the plan)
- If NO --> **ACCEPT IT** (acknowledge it as a known limitation, proceed anyway)

*What you should see*: A short list of plan modifications and a short list of accepted limitations.

---

**Step B5: Document the ignored objections.**

Same as A8. Write one sentence per ignored objection:
```
IGNORED OBJECTION: [Objection] -- TYPE: [type] -- REASON: [why ignored per triage rules]
```

**Output of Section B**: A plan with modifications for addressable concerns, accepted limitations documented, and a clear record of what was deliberately set aside.

---

## SECTION C: INFORMATION TRIAGE

*Use when you have too many sources, articles, data points, or inputs and need to reduce them to a usable set.*

---

**Step C1: Define your information need in one sentence.**

Write: "I need information that will help me ___."

Be specific. "Understand climate change" is too broad. "Determine whether solar panels will save me money in Phoenix, Arizona over 10 years" is specific enough to filter against.

---

**Step C2: Set your capacity budget.**

How many items can you realistically process? Be honest.

| If you have... | You can realistically process... |
|---|---|
| 1 hour | 5-8 items |
| 1 day | 15-25 items |
| 1 week | 40-60 items |

Write your budget: "I will keep no more than ___ items."

---

**Step C3: First pass -- filter by title/summary only.**

Do NOT read full items yet. Based on title, abstract, or first two sentences only:

For each item, ask: "Does this appear directly relevant to my one-sentence need from Step C1?"

- Clearly YES --> **Pile 1: Read**
- Uncertain --> **Pile 2: Maybe**
- Clearly NO --> **Pile 3: Skip**

Speed: 10-15 seconds per item maximum.

*What you should see*: Pile 3 (Skip) should contain at least 50% of your items. If it does not, your information need from C1 is too broad -- go back and narrow it.

---

**Step C4: Filter the Read pile by source quality.**

For each item in Pile 1, assess the source:

- Does the source have relevant expertise or credentials? (If YES, keep)
- Is the information dated within a relevant time window? (If older than useful, cut)
- Has the information been replicated or corroborated? (If contradicted by multiple other sources, cut)
- Is there a conflict of interest? (If the source profits from you believing them, demote to Pile 2)

---

**Step C5: Filter the Read pile by redundancy.**

Group items by what they are saying. If 5 articles say the same thing, keep the ONE that is:
1. Most recent
2. Most detailed
3. From the most authoritative source

Cut the rest.

---

**Step C6: Fill remaining budget from Maybe pile.**

If you are under your capacity budget from C2, pull items from Pile 2 (Maybe) to fill the gap. Prioritize items that cover angles NOT already represented in your Read pile.

---

**Step C7: Read your final set and note what is missing.**

After processing your filtered set, ask: "Is there a perspective or data type that I expected to find but did not?"

If YES --> do a targeted search for that specific gap. Do NOT reopen the full unfiltered set.

**Output of Section C**: A curated reading list within your budget, biased toward quality and diversity of perspective.

---

## SECTION D: OPTION TRIAGE

*Use when brainstorming has produced too many ideas or options and you need to reduce to a shortlist.*

---

**Step D1: Confirm your selection criteria.**

Write 2-3 criteria that a good option must satisfy. These should come from your core objective.

Example: "A good option must (1) be implementable within 3 months, (2) cost less than $50K, and (3) address the customer's primary complaint."

If you do not have criteria, you are not ready to triage. First clarify what you want.

---

**Step D2: Mandatory cut -- remove non-starters.**

Go through every option. For each one, check it against your criteria from D1:

- Does it FAIL any single criterion with no realistic way to fix that? --> **CUT**
- Does it pass all criteria or could be modified to pass? --> **KEEP**

This should remove 40-60% of options.

---

**Step D3: Group similar options.**

Look for options that are variations on the same basic approach. Group them. From each group, keep only the strongest version (the one that best satisfies your criteria).

Example: If you have "hire a freelancer," "hire a contractor," and "hire a part-time employee," these are all variations of "bring in outside help." Keep the version that best fits your criteria and cut the rest.

---

**Step D4: Apply the 3-5 rule.**

You should now have a shortlist. If it is longer than 5, force-rank by your criteria and cut everything below 5th place.

Why 5? Research on decision quality shows that comparing more than 5 options simultaneously degrades decision quality. The cognitive overhead of additional options outweighs the marginal benefit of having more choices.

---

**Step D5: Sanity check -- is the best discarded option better than your worst kept option?**

Look at the top item you cut. Compare it to the bottom item you kept. Is the cut item actually better?

- If YES --> swap them
- If NO --> your triage is complete

**Output of Section D**: 3-5 options for deeper evaluation.

---

## SECTION E: TASK/ATTENTION TRIAGE

*Use when you have more demands on your time than you have time.*

---

**Step E1: List everything claiming your attention.**

Write it all down. Every task, request, worry, and "I should really..." item.

---

**Step E2: Apply the Eisenhower Filter (modified).**

For each item, answer two questions:

Question 1: "If I do not do this in the next 48 hours, will something BAD happen that I cannot easily fix?"
- YES = **Urgent**
- NO = **Not Urgent**

Question 2: "Does completing this item move me toward my most important goal for this month?"
- YES = **Important**
- NO = **Not Important**

| | Important | Not Important |
|---|---|---|
| **Urgent** | DO NOW (Schedule first) | QUICK HANDLE (Spend max 15 min, delegate, or defer with a note) |
| **Not Urgent** | SCHEDULE (Put on calendar for a specific time this week) | **IGNORE** (Cross it off. It does not belong on your list.) |

---

**Step E3: For items you are ignoring, use the "newspaper test."**

For each item you marked IGNORE, ask:

> "If I never did this and someone found out, would it be embarrassing or harmful?"

- If YES --> it might actually be Important. Re-evaluate Question 2.
- If NO --> confirm the cut. Cross it off with confidence.

---

**Step E4: Communicate your cuts.**

If any ignored items involve other people (requests from colleagues, social obligations), send a brief message:

"I have decided not to pursue [item] at this time because I am focusing on [core priority]. I wanted to let you know directly rather than just not responding."

This takes 2 minutes and prevents the ignored item from generating additional attention-demands (follow-up emails, resentment, etc.).

**Output of Section E**: A task list with no more than 3-5 items for today, scheduled important items for the week, and everything else explicitly crossed off.

---

## QUICK REFERENCE CARDS

### The Five Filters (Apply in Order)

```
FILTER 1: RELEVANCE    -- "Does this connect to my actual goal?"         --> If NO: Cut
FILTER 2: IMPACT       -- "Would this change my decision/outcome?"       --> If NO: Cut
FILTER 3: REDUNDANCY   -- "Do I already have this signal from another source?" --> If YES: Cut
FILTER 4: REVERSIBILITY -- "Can I revisit this later if needed?"         --> If YES: Safe to defer
FILTER 5: ASYMMETRY    -- "Is the downside of ignoring catastrophic?"    --> If YES: Keep regardless
```

### The Two Critical Questions

Before ignoring ANYTHING, ask:
1. "Am I ignoring this because it does not matter, or because it is uncomfortable?"
2. "If I am wrong about ignoring this, what is the worst that happens?"

If the answer to #1 is "uncomfortable" --> **Do not ignore. Investigate.**
If the answer to #2 is "catastrophic" --> **Do not ignore. Keep.**

### The 7-Item Rule

You should end any triage process with no more than 7 items in your "keep" set. If you have more than 7, you have not triaged -- you have just reorganized. Go back and cut harder.

---

## COMMON MISTAKES

**Mistake 1: Confusing "uncomfortable" with "unimportant."**
The most important things to pay attention to are often the ones you least want to look at. If you notice you are ignoring something because it makes you anxious, that is a signal to investigate, not to dismiss. The procedure addresses this in Step A2 (the 10-second rule prevents overthinking) and the Two Critical Questions.

**Mistake 2: Keeping everything "just in case."**
This is not caution; it is a failure to triage. Every item you keep dilutes your attention on every other item. If you kept 20 factors for a decision, you did not make a 20-factor decision -- you made a muddled mess. The cost of keeping is invisible but real.

**Mistake 3: Ignoring low-probability, high-consequence items.**
The procedure explicitly checks for this (Step A3, Filter 5), but people still skip it. A 2% chance of losing everything is not ignorable just because it is unlikely. Always run the asymmetry check.

**Mistake 4: Cutting based on a single pass.**
The procedure uses multiple passes for a reason. Your first instinct about what to ignore is often wrong. The three-pile system (Keep / Parking Lot / Cut) with subsequent review catches errors that a single yes/no pass would miss.

**Mistake 5: Not documenting what you ignored.**
If you cannot say WHY you ignored something, you did not make a deliberate choice -- you just forgot about it. Documentation (Steps A8, B5) is what separates productive neglect from negligence.

**Mistake 6: Treating triage as permanent.**
Triage is for NOW. What you ignore today may need attention tomorrow. The "Parking Lot" and documented cuts exist so you can revisit if circumstances change. Set a specific date to review your cuts (e.g., "I will review my ignored items list on the 15th").

**Mistake 7: Ignoring what you cannot control without planning for it.**
"I cannot control the weather" does not mean "I should ignore the weather." Uncontrollable factors that have high impact need a contingency plan, not dismissal. The controllability dimension is about how you respond (act vs. plan around), not whether to pay attention.

**Mistake 8: Filtering information before understanding the shape of the space.**
If you start cutting before you have seen the full landscape, you might cut the only representative of an important category. Steps C3-C5 are deliberately ordered: first filter by relevance, then by quality, THEN by redundancy -- because you need to see what is redundant before you can cut duplicates.

---

## WHEN TO OVERRIDE THIS PROCEDURE

Stop following this procedure and seek expert help when:

1. **You are in a domain where errors are irreversible and costly** (medical decisions, legal proceedings, structural engineering, financial decisions over $100K). This procedure helps you focus, but it is not a substitute for domain expertise when stakes are high. Consult a professional who knows which factors actually matter.

2. **You keep going back and forth on the same items.** If you have moved something between Keep and Cut three or more times, you do not have a triage problem -- you have an information problem. You need more data about that specific item, not a better filtering method.

3. **The domain is completely novel to you.** If you have never encountered this type of decision before and have no relevant experience, your relevance and impact judgments will be unreliable. Find someone who has made this type of decision before and ask them: "What are the 3 things that actually matter here?" Use their answer as your starting filter.

4. **You feel RELIEF after cutting something.** Relief is a warning sign. It suggests you cut the item because it was stressful, not because it was unimportant. Revisit any cut that made you feel noticeably relieved.

5. **Your triage results in keeping only items that confirm your existing preference.** If every "Keep" item supports Option A and every "Cut" item supported Option B, you did not triage -- you rationalized. Redo the process with someone who disagrees with you.

6. **Time pressure is extreme (less than 1 hour for a major decision).** Under extreme time pressure, this procedure is too slow. Instead: ask one person you trust "What are the TWO things I should focus on?" and ignore everything else.

---

## WORKED EXAMPLES

### Example 1: Choosing a City to Relocate To

**Situation**: Mara has a list of 22 factors she is considering for choosing a city: cost of living, weather, job market, distance from family, nightlife, public transit, school quality, crime rate, restaurant scene, hiking access, cultural events, political climate, tax rates, diversity, healthcare quality, airport proximity, walkability, housing market trends, internet speed, dog-friendliness, water quality, and proximity to the ocean.

**Executing Section A (Decision Factor Triage):**

**Step A1**: "The single most important outcome I want from this decision is finding a city where I can build a stable, fulfilling life for the next 5+ years."

**Step A2** (10 seconds per item):
- Pile 1 (Keeps): Cost of living, job market, distance from family, school quality, crime rate, healthcare quality, housing market trends, weather, public transit, walkability
- Pile 2 (Parking Lot): Tax rates, diversity, airport proximity, political climate
- Pile 3 (Cuts): Nightlife, restaurant scene, hiking access, cultural events, internet speed, dog-friendliness, water quality, proximity to ocean

**Step A3** (Check Cuts for hidden killers):
- Internet speed: Worst case? Mara works remotely -- if internet is unreliable, she cannot work. MOVE TO KEEPS.
- All others: worst case is mild disappointment, easily recoverable. Stay in Cuts.

**Step A4** (Deduplicate Keeps):
- "Cost of living" and "housing market trends" overlap significantly --> keep "cost of living" (more directly actionable)
- "Public transit" and "walkability" overlap --> combine as "daily transportation without a car"
- Keeps now: Cost of living, job market, distance from family, school quality, crime rate, healthcare quality, weather, transportation, internet reliability

**Step A5** (Rank by decision-flipping power):
- 3 (Decision flippers): Job market, cost of living, distance from family
- 2 (Influencers): School quality, crime rate, internet reliability
- 1 (Confirmers): Healthcare quality, weather, transportation

With 6 items at score 2+, Mara keeps those 6. The three score-1 items move to Cuts.

**Step A6** (Parking Lot): Tax rates -- can check in 5 minutes on a comparison website. Result: tax difference between top cities is <$2K/year. Not a decision flipper. CUT. Diversity, airport proximity, political climate -- cannot assess in 30 minutes without deeper research. CUT with note to revisit.

**Step A7** (Aggregate check on Cuts): "If weather, healthcare, transportation, nightlife, restaurants, hiking, cultural events, taxes, diversity, airport, politics, dog-friendliness, water quality, ocean proximity ALL pointed to the same city, would that change my decision?" Mara considers: these are all "nice to have" quality-of-life factors. Together they might shift her preference between two otherwise equal cities, but they would not override job market + cost of living + family distance. TRIAGE COMPLETE.

**Final working set**: Job market, cost of living, distance from family, school quality, crime rate, internet reliability.

---

### Example 2: Responding to Feedback on a Business Plan

**Situation**: Jonas presented his business plan to a panel of 8 advisors and received 19 pieces of feedback. He has limited time before the investor meeting and needs to decide which feedback to act on.

**Executing Section B (Objection Triage):**

**Step B1**: All 19 objections listed verbatim.

**Step B2** (Classify each):
- "Your revenue projections assume 40% year-over-year growth with no explanation" --> STRUCTURAL (could cause the plan to fail)
- "You have not addressed what happens if your main supplier goes bankrupt" --> RISK
- "The marketing budget seems low" --> TRADE-OFF
- "You should use a different font for the slides" --> PERFECTIONISM
- "Starting a business is risky in any economy" --> UNIVERSAL
- "I am not sure your team has enough experience in this specific market" --> STRUCTURAL
- "What about competitor X entering the space?" --> RISK
- "Your pricing might be too high" --> TRADE-OFF
- "You should have a mobile app from day one" --> PERFECTIONISM
- (10 more classified similarly)

**Step B3** (Apply triage rules):
- 2 STRUCTURAL items: KEEP BOTH (must address)
- 4 TRADE-OFF items: Keep the 3 most significant (marketing budget, pricing, customer support costs). Cut one about office space costs (<5% of budget).
- 5 RISK items: Keep 2 (supplier risk: probability ~15% but impact would be catastrophic, so keep; competitor entry: probability ~40% and high impact, so keep). Cut 3 (niche regulatory change: <5% probability; technology obsoletion in 1 year: <10%; key hire leaving: real but unactionable in a plan document).
- 3 PERFECTIONISM items: CUT ALL
- 2 UNIVERSAL items: CUT ALL
- 3 UNCLEAR items: Jonas emails the advisors for clarification

**Step B4** (Address or accept):
- Revenue projections: ADDRESS (add explanation and sensitivity analysis -- 2 hours of work)
- Team experience gap: ADDRESS (add advisory board members with market expertise -- 1 day to confirm commitments)
- Marketing budget: ACCEPT (acknowledge as a known limitation; plan to revisit after first revenue)
- Pricing: ADDRESS (add competitor pricing comparison table -- 1 hour)
- Supplier risk: ADDRESS (add backup supplier section -- 30 minutes)
- Competitor entry: ACCEPT (acknowledge in risk section; plan says "our moat is ___")
- Customer support costs: ACCEPT (note as a scaling concern for Year 2)

**Final output**: 3 plan modifications (revenue justification, advisory board, pricing comparison, supplier backup), 3 accepted limitations documented, 12 items explicitly ignored with reasons.

---

### Example 3: Research Overload for a Term Paper

**Situation**: Priya is writing a 3,000-word paper on the economic effects of remote work. Her initial literature search returned 147 results.

**Executing Section C (Information Triage):**

**Step C1**: "I need information that will help me determine the measurable economic effects of remote work adoption on urban commercial real estate markets in the US between 2020-2025."

**Step C2**: She has 2 days for research. Budget: 20 items maximum.

**Step C3** (Title/abstract scan, 15 seconds each -- about 35 minutes total):
- Pile 1 (Read): 31 items (titles clearly about remote work + commercial real estate + economic data)
- Pile 2 (Maybe): 42 items (about remote work OR real estate but not clearly both)
- Pile 3 (Skip): 74 items (about remote work culture, productivity, residential real estate, non-US markets, pre-2020 data)

50% in Skip pile. Threshold met.

**Step C4** (Source quality on 31 Read items):
- Cut 4: Published before 2020 (pre-pandemic data, not relevant to the 2020-2025 window)
- Cut 3: From commercial real estate industry marketing materials (conflict of interest -- they profit from office occupancy narratives)
- Cut 2: Blog posts with no citations
- Remaining: 22 items

**Step C5** (Redundancy check):
- 6 articles about NYC office vacancy rates --> keep 2 (most recent + most comprehensive)
- 4 articles citing the same Stanford study --> keep 1 (the Stanford study itself)
- Remaining: 16 items

**Step C6** (Fill from Maybe pile to reach budget of 20):
- Priya notices no items about secondary/tertiary cities (all about major metros). Pulls 3 items from Maybe pile that cover smaller markets.
- Priya notices no items from the employer/corporate perspective on cost savings. Pulls 1 item.
- Total: 20 items. Budget met.

**Step C7** (Gap check after reading): "I have nothing about the tax revenue implications for city governments." Targeted search for that specific topic yields 2 strong results. She swaps out her 2 weakest items to maintain the 20-item budget.

**Final output**: 20 curated sources covering major metros, secondary cities, employer cost data, and municipal tax implications.
