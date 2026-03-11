# /action Set up a systematic process for testing 5 skills per day for quality
**Date:** 2026-03-09
**Skill:** /action (Execute a Command)

---

## Routing

**Action extracted:** Set up + systematic process + daily skill testing
**Is this a command?** Yes — this is a multi-step task requiring planning and step generation.
**Executable or needs analysis?** Executable — the goal is clear ("test 5 skills/day for quality"), the domain is known (592 skills in `claude-code-plugin/skills/`), and the executor is known (solo developer).
**Single or multi-step?** Multi-step — requires infrastructure, selection method, test protocol, and tracking.

Routing to: /stg (step generation) + /ata (adjacent tasks) + /to (ordering)

---

## /stg — Steps Generation

### STEPS: Daily Skill Quality Testing Process

**Total steps**: 8 (one-time setup) + 5 (daily routine)
**Estimated duration**: 2-3 hours setup, 30-45 minutes daily
**Executor type**: Solo developer (human + Claude)

### Goal-Structure
- **Intrinsic goal**: Confidence that the skill library actually works and delivers value
- **Instrumental goal**: Identify broken, weak, or redundant skills so they can be fixed or removed
- **Immediate goal**: A repeatable daily process that audits 5 skills and produces actionable quality data

---

### Prerequisites

- [ ] Access to `claude-code-plugin/skills/` directory (592 skills)
- [ ] A place to record results (file, spreadsheet, or database)
- [ ] Clear definition of what "quality" means for a skill (defined in Step 2)

---

### ONE-TIME SETUP STEPS

---

#### Step 1: Generate the Master Skill List

**Action**: Export all 592 skill directory names into a single ordered list file.

**Process**:
1. Run `ls /home/ben/Documents/projects/reasoningtool/claude-code-plugin/skills/` and capture output
2. Write to a tracking file with columns: `skill_name | status | date_tested | quality_score | notes`
3. Randomize the order (so you don't test alphabetically and get bored in the A's)

**Output**: `skill-audit-tracker.csv` [format: CSV] [location: `reasoningtoolpersonal/`]

**Verification**:
- [ ] File contains exactly 592 rows (one per skill)
- [ ] Order is randomized
- [ ] All columns present

**If blocked**:
- If skill count changes before you finish: re-generate the list, mark already-tested ones as done

---

#### Step 2: Define the Quality Rubric

**Action**: Create a scoring rubric that you apply to every skill, every time, identically.

**Process**:
Define these quality dimensions (score each 0-2):

| Dimension | 0 (Fail) | 1 (Partial) | 2 (Pass) |
|-----------|----------|-------------|----------|
| **Parseable** | SKILL.md is malformed, missing sections, or unreadable | Has structure but some sections incomplete | Clean, complete structure |
| **Clear purpose** | Can't tell what this skill does from reading it | Purpose is guessable but not stated well | Purpose is immediately obvious |
| **Actionable steps** | No clear procedure to follow | Has steps but they're vague or assume too much | Steps are concrete and executable |
| **Produces output** | Running it produces nothing useful | Produces something but quality is inconsistent | Reliably produces useful, structured output |
| **Differentiated** | Duplicates another skill or is too generic | Overlaps with others but has some unique value | Clearly distinct purpose that no other skill covers |

**Score range**: 0-10 per skill.
- 8-10: Good — no action needed
- 5-7: Needs improvement — log specific issues
- 0-4: Broken or redundant — flag for rewrite or removal

**Output**: Quality rubric definition [format: section in tracker or separate reference file]

**Verification**:
- [ ] All 5 dimensions defined with concrete 0/1/2 criteria
- [ ] You can score a skill in under 2 minutes using this rubric
- [ ] No subjective "feels good" criteria — everything is observable

---

#### Step 3: Define the Test Protocol

**Action**: Write the exact sequence you follow to test one skill.

**Process**:
For each skill, do this:

1. **Read**: Open `skills/[name]/SKILL.md`. Read completely. (1 min)
2. **Parse check**: Does the file have the expected structure — frontmatter, core principles, steps/phases, failure modes, integration section? Score "Parseable."
3. **Purpose check**: After reading, can you state in one sentence what this skill does and when you'd use it? Score "Clear purpose."
4. **Dry run**: Pick a realistic input and mentally (or actually) run the skill. Do the steps guide you to a result? Score "Actionable steps."
5. **Live test**: Run the skill with a real or realistic input through Claude. Does the output meet the skill's own stated purpose? Score "Produces output."
6. **Overlap check**: Does this skill duplicate another skill you've already tested, or one you know well? Score "Differentiated." (This gets easier over time as you build context.)
7. **Record**: Log scores and notes in the tracker.
8. **Tag**: If score is 0-4, tag as `needs-rewrite` or `candidate-for-removal`. If 5-7, tag as `needs-improvement` with specific notes.

**Output**: Test protocol document [format: checklist you can follow mechanically]

**Verification**:
- [ ] Each step takes a known, bounded amount of time
- [ ] A single skill can be tested in 5-8 minutes using this protocol
- [ ] The protocol produces a score, not just a feeling

---

#### Step 4: Set Up the Tracking File

**Action**: Create the actual CSV or Markdown tracking file with all 592 skills pre-loaded.

**Process**:
1. Generate randomized skill list (from Step 1)
2. Create file with columns:

```
skill_name,date_tested,parseable,clear_purpose,actionable_steps,produces_output,differentiated,total_score,status,notes
```

3. Pre-populate all 592 rows with skill names, leaving other columns blank
4. Add a "batch" column that assigns skills to testing days (skills 1-5 = Day 1, 6-10 = Day 2, etc.)

**Output**: `skill-audit-tracker.csv` fully populated with skill names and batch assignments

**Verification**:
- [ ] 592 rows with skill names
- [ ] Batch assignments cover all skills (592 / 5 = ~119 days of testing)
- [ ] File opens cleanly in your preferred editor

**If blocked**:
- If you prefer Markdown over CSV: use a Markdown table, but CSV is easier to sort/filter later

---

#### Step 5: Calculate Your Timeline

**Action**: Know how long this will take so you can commit realistically.

**Process**:
- 592 skills / 5 per day = **119 working days**
- At 5 days/week = **~24 weeks** (~6 months)
- At 7 days/week = **~17 weeks** (~4 months)
- Buffer for rewrites and bad days: add 20% = **~5 months at 7 days/week, ~7 months at 5 days/week**

**Decision to make now**: Are you doing this 5 or 7 days per week? Pick one and commit.

**Verification**:
- [ ] You have a realistic end date in mind
- [ ] The pace (5/day) feels sustainable, not heroic

---

### DAILY ROUTINE STEPS

---

#### Step 6: Daily — Pull Today's Batch

**Action**: Identify which 5 skills you're testing today.

**Process**:
1. Open `skill-audit-tracker.csv`
2. Find the next 5 untested skills (filter by empty `date_tested`)
3. Open each skill's `SKILL.md` in tabs or a reading list
4. Set a timer for 45 minutes (hard stop — do not exceed)

**Output**: 5 skill files open and ready to test

**Verification**:
- [ ] Exactly 5 skills identified
- [ ] Timer is set

**If blocked**:
- If a skill file is missing or empty: score it 0 across the board, note "FILE MISSING", move on
- If you have less than 45 minutes today: test 3 instead of 5, but don't skip the day entirely

---

#### Step 7: Daily — Test Each Skill

**Action**: Apply the test protocol (Step 3) to each of the 5 skills.

**Process**:
For each skill (target: 6-8 minutes each):
1. Read SKILL.md
2. Score all 5 dimensions (0-2 each)
3. Write 1-2 sentence notes on anything notable (good or bad)
4. If score <= 4: write a specific note on what's wrong and what would fix it
5. If score >= 8: note it as a model to reference when fixing others
6. Move to next skill

**Output**: 5 scored rows in the tracker, with notes

**Verification**:
- [ ] All 5 skills scored
- [ ] No dimension left blank
- [ ] Low-scoring skills have actionable notes (not just "bad")

**If blocked**:
- If a skill is too complex to test in 8 minutes: score what you can, note "NEEDS DEEPER REVIEW", move on
- If you're unsure about overlap: score "Differentiated" as 1 and add a note to revisit

---

#### Step 8: Daily — Log and Review

**Action**: Save results and do a 2-minute end-of-session review.

**Process**:
1. Save the tracker file
2. Count today's scores: how many 8+, how many 5-7, how many 0-4?
3. If you found any 0-4 skills: add them to a separate `skills-to-fix.md` list with the specific issue
4. Every 5th day (every 25 skills): scan `skills-to-fix.md` and look for patterns — are the same problems recurring? (e.g., "most skills are missing failure modes sections")

**Output**: Updated tracker + updated fix list

**Verification**:
- [ ] Tracker is saved
- [ ] Fix list is current
- [ ] You know your running totals (X tested, Y good, Z need work)

---

## /ata — Adjacent Tasks

### AND THEN ALSO

**PRIMARY TASK**: Set up daily 5-skill quality testing process

**BEFORE (prerequisites)**:
1. **Decide what "good enough" means at the portfolio level** — After 592 skills are scored, what's your threshold? Do you fix everything below 8? Remove everything below 5? You need this answer before you start, or you'll accumulate a fix list with no plan. (2 minutes to decide now saves hours later.)
2. **Back up the skills directory** — Before you start editing skills based on test results, make sure you have a clean snapshot. You're already in git, so ensure current state is committed.

**DURING (parallel)**:
1. **Build a "model skill" reference** — As you test, you'll find skills that score 9-10. Bookmark 3-5 of these as templates for when you rewrite the bad ones. Don't wait until you need them.

**AFTER (follow-ups — required)**:
1. **Schedule a weekly fix session** — Testing without fixing is just generating a to-do list. Block 1-2 hours per week to actually rewrite or remove the worst-scoring skills from that week's batch.
2. **Review patterns at the 50-skill mark** — After 10 days, you'll have enough data to see systemic issues. Are 60% of skills missing failure modes? Is one category consistently weak? Pattern detection changes your strategy from "fix one at a time" to "fix the template."

**OPTIONAL (consider)**:
1. **Automated structure check** — Write a script that checks each SKILL.md for required sections (frontmatter, steps, failure modes, integration). This could pre-score the "Parseable" dimension for all 592 skills in seconds, letting you focus manual effort on the harder dimensions. VALUE: Saves ~1 min per skill (10 hours total). COST: 30-60 minutes to write.
2. **Priority ordering by usage** — Instead of random order, test the most-used skills first (the category skills, the ones listed in CLAUDE.md). This front-loads the highest-impact fixes. VALUE: Fixes the skills users hit most. COST: 15 minutes to reorder the list.
3. **Tag skills by category** — As you test, tag each skill with its category (decision, analysis, writing, meta, etc.). This enables category-level quality reports later. VALUE: Enables "which category is weakest?" analysis. COST: 10 seconds per skill during testing.

**EXECUTION ORDER**:
Back up repo → Define quality threshold → (Optional: run automated structure check) → (Optional: reorder by usage priority) → Generate master list → Define rubric → Define protocol → Create tracker → Calculate timeline → BEGIN DAILY ROUTINE → [every 5th day: pattern review] → [weekly: fix session]

---

## /to — Execution Order Summary

```
PARALLEL SCHEDULE:

Phase 1 — Setup (one-time, ~2 hours):
  [ ] Back up / commit current state
  [ ] Define portfolio-level quality threshold
  [ ] Define quality rubric (Step 2)
  [ ] Define test protocol (Step 3)

Phase 2 — Infrastructure (one-time, ~30 min):
  [ ] Generate master skill list (Step 1)
  [ ] (Optional) Reorder by usage priority
  [ ] Create tracking file (Step 4)
  [ ] Calculate timeline (Step 5)
  [ ] (Optional) Write automated structure-check script

Phase 3 — Daily routine (ongoing, ~45 min/day):
  [ ] Pull today's batch (Step 6)
  [ ] Test each skill (Step 7)
  [ ] Log and review (Step 8)

Phase 4 — Weekly maintenance (ongoing, ~1-2 hours/week):
  [ ] Fix or remove worst-scoring skills from the week
  [ ] At 50-skill mark: full pattern review

--- DONE when all 592 tested ---
```

**Critical path**: Phase 1 → Phase 2 → Phase 3 (repeating) + Phase 4 (weekly)
**Minimum calendar time**: ~119 working days + fix sessions
**Bottleneck**: The human (you). This is a solo, manual process. The constraint is consistency, not complexity.

---

## Completion Report

**What was done**: Generated a complete, executable daily process for auditing 592 skills at 5/day, including:
- A 5-dimension quality rubric with concrete scoring criteria
- A per-skill test protocol (6-8 minutes per skill)
- A daily routine (pull batch, test, log) bounded to 45 minutes
- A tracking infrastructure (CSV with batch assignments)
- Timeline calculation (~5-7 months to completion)
- Adjacent tasks: weekly fix sessions, pattern reviews, optional automation

**What remains**:
- Execute Phase 1 (define rubric and protocol — the content is above, just formalize it)
- Execute Phase 2 (create the actual tracker file)
- Start Phase 3 tomorrow

**Adjacent tasks identified**:
- Back up repo before starting edits
- Define portfolio-level quality threshold (what % quality triggers what action)
- Schedule weekly fix sessions (testing without fixing is waste)
- Consider automated parseable-check script (saves ~10 hours over full audit)
- Consider front-loading high-usage skills (category routers, CLAUDE.md-listed skills)

---

### Follow-Up Routing

- **"Create the tracker file for me"** → /action (direct execution)
- **"Write the automated structure check"** → /action or /create
- **"Which skills should I test first?"** → /ro (reorder by priority)
- **"Is this rubric good enough?"** → /evaluate
- **"What could go wrong with this process?"** → /fla (failure anticipation)
- **"What am I likely to find?"** → /fut (anticipate outcomes)
