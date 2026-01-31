# Decision Procedure — Turning DCP Procedures into Skills, Software, and Other Artifacts

**Date**: 2026-01-31
**Input**: turning dcp procedures into skills and software projects and elsewhere

---

## STEP 1: Decision Dimensions

**D1: Target Medium**
What form should the output take? A GOSM skill file, a software application, a printed reference card, a training curriculum, an API, a chatbot, etc. This is the most consequential dimension — everything else follows from it.

**D2: Audience Technical Capacity**
Can the end users follow a markdown document? Do they need a GUI? Are they developers who'd prefer code? Are they field workers who need a laminated card? This determines the required level of interface polish.

**D3: Procedure Complexity**
How many steps, branches, and sections does the procedure have? Simple procedures (< 15 steps, linear) can go almost anywhere. Complex procedures (50+ steps, deep branching) require software to be navigable.

**D4: Interaction Model**
Does the procedure require user input at each step (interactive), or can it be read top-to-bottom (static)? Interactive procedures benefit from software; static ones work as documents.

**D5: Data Requirements**
Does the procedure need external data to function (prices, benchmarks, databases, real-time information)? If yes, software is likely necessary. If the procedure is self-contained, any medium works.

**D6: Update Frequency**
How often will the procedure change? Frequently updated procedures need a medium that supports versioning and easy editing. Stable procedures can be printed or embedded.

**D7: Distribution Context**
How will this reach users? Internal team tool, public website, app store, training workshop, CLI plugin, printed manual? This constrains the medium.

**D8: Validation State**
Has the procedure been tested with real users on real decisions? Unvalidated procedures should stay in editable, low-commitment formats. Validated ones can be productized.

**D9: Integration Requirements**
Does this need to connect to other systems (APIs, databases, other tools, other procedures)? If so, software or skill format is necessary.

**D10: Maintenance Ownership**
Who will keep this updated? A developer, a domain expert, a team, nobody? This determines what format is sustainable long-term.

**D11: Fidelity Requirement**
How precisely must the final artifact match the procedure logic? High fidelity (every branch, every warning) requires structured formats. Low fidelity (gist of the approach) can be a summary card.

**D12: Value at Stake**
How consequential are the decisions this procedure guides? High-stakes procedures (medical, financial, safety) need more guardrails, validation, and error-handling than low-stakes ones.

---

## STEP 2: Options per Dimension

### D1: Target Medium
| Option | What it is | Best when |
|---|---|---|
| **GOSM Skill** | A `/skillname` SKILL.md file in the reasoning toolkit | You want AI-assisted execution, the audience uses Claude Code, procedure chains to other skills |
| **Web App** | Interactive website/PWA | Broad audience, needs GUI, no install required |
| **CLI Tool** | Command-line application | Developer audience, scriptable, integrates with pipelines |
| **Mobile App** | Native or hybrid app | Field use, offline needed, push notifications |
| **Printed Flowchart** | Physical or PDF decision tree | No-tech environments, wall poster, training rooms |
| **Spreadsheet/Form** | Google Sheets, Excel, or web form | Low-tech audience, data collection needed, familiar interface |
| **API/Library** | Programmatic interface | Other software needs to call the procedure |
| **Training Module** | Course, workshop, or e-learning | Procedure is part of skill development, not just reference |
| **Chatbot** | Conversational interface | Non-technical users, step-at-a-time guidance, natural language |
| **Checklist Document** | Markdown, PDF, or wiki page | Simple procedures, read-and-follow, easy to maintain |

### D2: Audience Technical Capacity
| Level | Appropriate Formats |
|---|---|
| **Developers** | Skill, CLI, API, any code-based format |
| **Technical non-developers** | Web app, spreadsheet, checklist document |
| **General public** | Web app, mobile app, chatbot, printed flowchart |
| **Field workers** | Printed flowchart, mobile app (offline), laminated card |
| **Mixed/unknown** | Web app (lowest common denominator with most flexibility) |

### D3: Procedure Complexity
| Complexity | Step Count | Viable Formats |
|---|---|---|
| **Simple** | < 15 steps, mostly linear | Any format works. Checklist is sufficient. |
| **Moderate** | 15-40 steps, some branching | Document, web app, skill |
| **Complex** | 40+ steps, deep branching | Web app, software, skill (document becomes unusable) |
| **Very complex** | Multiple procedures chained | Software or skill system required |

### D4: Interaction Model
| Model | Implications |
|---|---|
| **Static** (read top-to-bottom) | Document, printout, checklist |
| **Interactive** (input needed at each step) | Web app, CLI, chatbot, skill |
| **Hybrid** (some sections static, some interactive) | Web app with mixed modes, skill |

### D5: Data Requirements
| Requirement | Format Constraint |
|---|---|
| **Self-contained** | Any format |
| **Needs reference data** (tables, benchmarks) | Embed in document, or software with database |
| **Needs live data** (prices, APIs, real-time) | Software required |
| **Needs user history** (track decisions over time) | Software with storage required |

### Key Interaction Patterns (D6-D12)
- D6 high frequency + D10 no developer → skill or wiki (easy to edit without code)
- D8 unvalidated + D12 high stakes → stay in editable format, do NOT productize yet
- D9 high integration + D1 any → software or API required
- D7 public distribution + D2 general public → web app or chatbot
- D11 high fidelity + D3 complex → software (documents lose branches)

---

## STEP 3: Hidden Assumptions

**A1: "The procedure is ready to implement."**
People rush from having a DCP output to building software. The DCP output is a first draft — it hasn't been tested on real decisions. Building software around an untested procedure freezes premature logic.

**A2: "More sophisticated medium = better."**
A web app isn't inherently better than a printed flowchart. The best medium is the one your users will actually use. A laminated card on someone's desk beats a beautiful app they never open.

**A3: "The procedure logic is the hard part."**
The DCP already did the logic. The hard part of implementation is UX — making the procedure *feel* navigable, not just *be* correct. Many procedure-to-software translations preserve logic but destroy usability.

**A4: "One output medium is enough."**
Many procedures benefit from multiple formats: a skill for AI-assisted use, a checklist for quick reference, a web app for public access. Don't assume you must pick exactly one.

**A5: "Software will enforce the procedure."**
Software can guide users through steps, but it can't prevent them from lying about inputs, skipping steps mentally, or gaming the system. The procedure must be robust to dishonest or careless inputs.

**A6: "Skills are just for AI."**
A GOSM skill isn't only for Claude Code users. The SKILL.md format is also a well-structured document that humans can read directly. Don't discount the skill format just because the user isn't using Claude.

**A7: "You need a developer to turn a procedure into software."**
Modern no-code tools, form builders, and AI code generation can turn a procedure into a functional web app with minimal coding. The barrier is lower than assumed.

**A8: "The procedure will be used as intended."**
People adapt, skip, and reinterpret procedures. Design the output to be robust to partial use, not just perfect sequential execution.

---

## STEP 4: The Procedure

```
TURNING DCP PROCEDURES INTO IMPLEMENTABLE ARTIFACTS
=====================================================
Decision Procedure v1.0

WHO THIS IS FOR: Anyone who has a DCP procedure output (or any
structured decision flowchart) and wants to turn it into something
people can actually use — a skill, software, document, or other format.

WHAT THIS PRODUCES: A specific implementation plan with chosen
format, scope, and next steps.
```

### STEP 0: What are you trying to do with this procedure?

| If your goal is... | Go to... |
|---|---|
| Make it usable inside Claude Code / GOSM | **SECTION A** (Skill Conversion) |
| Build a software tool (web app, CLI, mobile) | **SECTION B** (Software Project) |
| Create a reference document (PDF, poster, checklist) | **SECTION C** (Document Artifact) |
| Build a training program or workshop | **SECTION D** (Educational Artifact) |
| Embed the logic into an existing system or API | **SECTION E** (Integration) |
| Not sure yet | **SECTION F** (Format Selection) |

---

### SECTION A: Skill Conversion (DCP → GOSM Skill)

**A1.** Count the total steps and decision branches in your procedure.
- **< 30 steps, ≤ 3 sections** → This can be a single skill. Go to A3.
- **30-60 steps, 4-6 sections** → This should be a compound skill that chains sub-skills. Go to A2.
- **60+ steps** → This needs to be decomposed into a skill family. Go to A2.

**A2.** Decompose the procedure into skill-sized chunks.
- Each section of your DCP output becomes a candidate sub-skill
- A sub-skill should do ONE thing: classify, evaluate, generate, or decide
- Name each sub-skill with a 2-4 letter abbreviation
- Create a "router" skill that chains them (like DCP itself chains /dd → /se → /aex → /stg → /fla → /pv)
- **What you should see**: A list of 3-8 sub-skills with clear inputs and outputs, plus one orchestrator skill

Go to A3.

**A3.** For each skill (or the single skill), create the SKILL.md file using this template:

```
---
name: "[abbreviation] - [Full Name]"
description: [One-sentence description of what it does]
---

# [Skill Name]

**Input**: $ARGUMENTS

---

## Purpose
[2-3 sentences: what decision this helps with, who it's for]

## Procedure
[Steps from DCP output, reformatted as instructions to an AI executor]

## Output Format
[What the skill produces]
```

**Conversion rules:**
- Replace "Go to Section X" with "→ INVOKE: /skillname"
- Replace "ACTION:" items with direct instructions
- Replace user-facing questions ("Is X true?") with AI-directed analysis prompts ("Assess whether X applies to the input based on [criteria]")
- Keep decision points as conditional logic the AI follows
- **What you should see**: A SKILL.md that reads as instructions an AI would follow, not a flowchart a human would navigate

**A4.** Does the procedure reference external data, databases, or real-time information?
- **No, self-contained** → Go to A5
- **Yes** → Add a "Data Requirements" section to the skill listing what information is needed. The AI will need to ask the user for this or fetch it. Add explicit prompts: "Ask the user for [X]" or "Search for [Y]."

**A5.** Test the skill by running it on 3 different inputs:
- One straightforward case that should follow the main path
- One edge case that should trigger a branch or warning
- One case that might break the procedure (ambiguous, unusual)

- **All 3 produce correct, useful output** → Go to A6
- **1-2 failures** → Fix the failure points. Common fixes: add clarifying prompts, add missing branches, refine classification criteria. Re-test. Then go to A6.
- **All 3 fail** → The procedure likely needs rework before skill conversion. Go back to Step 0 and consider Section C (document) first while you iterate.

**A6.** Place the skill file:
- Single skill: `skills/[abbreviation]/SKILL.md`
- Compound skill: one folder per sub-skill, plus the orchestrator
- Update any skill registries or indexes if your toolkit has them
- **Done.** The skill is live.

---

### SECTION B: Software Project (DCP → Web App, CLI, Mobile)

**B1.** Answer these three questions about your users:
1. Will they use this on a phone, computer, or both?
2. Do they need it offline?
3. Do they need accounts / saved history?

| Phone + Online + No accounts | → Simple web app (single HTML page or static site) |
| Phone + Offline needed | → PWA (Progressive Web App) or native mobile app |
| Computer + Developer audience | → CLI tool |
| Any + Accounts needed | → Web app with backend |
| Any + Saved history needed | → Web app with backend or local storage |

**What you should see**: A specific technology choice, not "it depends."

**B2.** Map procedure steps to UI components:

| Procedure Element | UI Component |
|---|---|
| Classification table (Step 0) | Radio buttons or card selection |
| Binary decision point (Yes/No) | Two-button choice or toggle |
| Multiple-choice decision point | Radio buttons or dropdown |
| ACTION item | Displayed result card with actionable text |
| Section | Page or accordion panel |
| Warning/failure mode | Alert banner or modal |
| Quick reference card | Collapsible summary panel |

Write this mapping out for every step in your procedure.
- **What you should see**: A complete list of screens/components, one per procedure step

**B3.** Determine the data model:
- List every piece of information the user provides during the procedure
- List every piece of information the procedure produces
- These become your data model
- **What you should see**: A list of fields like `{ role: "citizen" | "policymaker" | ..., timeline: "< 1 year" | ... , actions: string[] }`

**B4.** Choose your build approach:

| Your coding ability | Approach |
|---|---|
| **Can code fluently** | Build directly. Use the UI mapping from B2 as your spec. |
| **Some coding ability** | Use a framework with pre-built components (React + component library, or Streamlit/Gradio for Python) |
| **No coding ability** | Use a no-code form builder (Typeform, Tally, Google Forms) for simple procedures; or use AI code generation (paste the procedure + UI mapping, ask for a web app) |
| **Have budget, no time** | Hire a developer. Give them the DCP output + B2 mapping + B3 data model as the spec. |

**B5.** Build the minimum viable version:
- Implement ONLY the main path first (Section A or whatever the most common case is)
- Skip: fancy styling, edge cases, failure modes, worked examples
- **What you should see**: A working tool that handles the most common version of the decision

**B6.** Test with 3 real users:
- Watch them use it (don't explain how)
- Note every point where they hesitate, misunderstand, or get stuck
- Fix those points
- Then add the remaining sections, edge cases, and failure mode warnings

**B7.** Deploy:
- Simple web app → Static hosting (Netlify, Vercel, GitHub Pages)
- CLI → Package manager (npm, pip, brew)
- Mobile → App store or PWA
- **Done.** The software is live.

---

### SECTION C: Document Artifact (DCP → PDF, Poster, Checklist)

**C1.** How will people physically interact with this document?
- **Read on screen** → Markdown or PDF. Go to C2.
- **Print and use at desk** → PDF formatted for letter/A4. Go to C2.
- **Post on a wall** → Large-format flowchart poster. Go to C3.
- **Carry in pocket/field** → Laminated card, pocket reference. Go to C4.

**C2 (Screen/Print Document).**
- Format the DCP output as a clean document
- Add a table of contents if > 3 sections
- Use bold for decision points, indentation for branches
- Add page breaks between sections
- Include the Quick Reference Cards as a standalone final page
- **What you should see**: A document someone can print, staple, and use immediately

**C3 (Wall Poster).**
- Convert the procedure into a visual flowchart
- Use boxes for steps, diamonds for decisions, arrows for flow
- Color-code sections (one color per section)
- Maximum 40 boxes on one poster — if more, split into multiple posters
- Include a legend
- Tools: draw.io, Miro, Lucidchart, or hand-drawn then scanned
- **What you should see**: A flowchart someone can trace with their finger from start to finish

**C4 (Pocket Reference).**
- Extract ONLY the decision points and quick reference cards
- Omit explanations, worked examples, and failure modes
- Fit on a single card (front and back)
- Use the smallest readable font size (8-9pt)
- This is a cheat sheet, not the full procedure — label it as such
- **What you should see**: A card that reminds someone who's already learned the procedure what to do next

**C5.** For all document types: include these elements at the top:
- Title and version number
- Date created
- One-sentence description of what decision this helps with
- "Validation status: Not validated by domain experts" (unless it has been)

**Done.**

---

### SECTION D: Educational Artifact (DCP → Training)

**D1.** What's the learning objective?
- **Teach people to follow the procedure** → Go to D2 (Procedural Training)
- **Teach people to understand WHY the procedure works** → Go to D3 (Conceptual Training)
- **Both** → Do D3 first, then D2

**D2 (Procedural Training).**
- Use the worked examples from the DCP output as training exercises
- Structure: demonstrate the procedure on Example 1, then have learners practice on Example 2 with guidance, then have them solo on Example 3
- Create 5-10 additional practice cases covering different sections/branches
- Include common mistakes as "what would go wrong if..." scenarios
- **What you should see**: A workshop plan with demo, guided practice, and independent practice

**D3 (Conceptual Training).**
- Use the dimensions (Step 1 of DCP) as the conceptual framework
- Each dimension becomes a teaching module: "Why does [dimension] matter?"
- Use the hidden assumptions (Step 3) as discussion prompts
- Use the failure modes (Step 5) as case studies
- **What you should see**: A curriculum outline with one module per key dimension

**Done.**

---

### SECTION E: Integration (DCP → Embed in Existing System)

**E1.** What system are you integrating with?
- **Another software application** → Express the procedure as a function/API: inputs are the user's situation, outputs are recommended actions. Use the data model from B3. Go to E2.
- **A business process** → Express the procedure as a process step: "At stage X, run this procedure. If output is Y, proceed. If output is Z, escalate." Go to E3.
- **Another GOSM skill** → Use the "→ INVOKE: /skillname" pattern. Your procedure becomes a sub-procedure that another skill calls. Go to A1 (Skill Conversion).

**E2 (API Integration).**
- Define the function signature: `function runProcedure(inputs: UserSituation): ActionPlan`
- Implement the decision logic as conditional code (if/else or switch/case matching the procedure's branches)
- Return structured data (action items, warnings, section taken)
- Add input validation matching the procedure's classification step
- **What you should see**: A callable function that takes a situation description and returns a decision

**E3 (Business Process Integration).**
- Identify the exact point in the existing process where this procedure applies
- Define the trigger: "Run this when [specific event]"
- Define the handoff: "This procedure produces [output]. Give that to [next step]."
- Train the people at that process step on the procedure (see Section D)
- **Done.**

---

### SECTION F: Format Selection (Not Sure What to Build)

If you reached here, answer these five questions:

**F1.** Who will use this? Write down 1-3 specific people or roles.

**F2.** When will they use it? Describe the exact moment they'd reach for this tool.

**F3.** What device/context are they in at that moment? (desk, phone, meeting, field, etc.)

**F4.** How often will they use it? (once, weekly, daily, in-the-moment crisis)

**F5.** Do you have the ability/resources to build and maintain software?
- **Yes** → Go to B1
- **No** → Go to C1

Use your answers to route:

| F1: Technical user + F3: At computer + F4: Regularly | → Section A (Skill) or Section B (CLI) |
| F1: Non-technical + F3: At desk + F4: Occasionally | → Section C (Document) |
| F1: Non-technical + F3: On phone + F4: In-the-moment | → Section B (Web App or Mobile) |
| F1: Team of learners + F4: Once (during training) | → Section D (Training) |
| F1: Another system + F4: Automatically | → Section E (Integration) |
| Still unsure | → **Start with Section C (Document). It's the lowest-cost option. If people use it and hit its limits, you'll know exactly which upgrade to build.** |

---

## QUICK REFERENCE CARDS

### Card 1: Format Decision Matrix

| Procedure Complexity | Audience Tech Level | → Best Format |
|---|---|---|
| Simple | Any | Checklist document |
| Simple | Technical | GOSM Skill |
| Moderate | Non-technical | Web app or printed flowchart |
| Moderate | Technical | GOSM Skill or CLI |
| Complex | Non-technical | Web app (document won't work) |
| Complex | Technical | Software + Skill (both) |

### Card 2: Minimum Viable Versions

| Format | MVP Scope | Build Time Benchmark |
|---|---|---|
| GOSM Skill | Single SKILL.md, main path only | Hours |
| Checklist | Formatted markdown, no visuals | Hours |
| Web app (no-code) | Form with conditional logic | Hours to days |
| Web app (coded) | Main path only, no auth | Days |
| CLI tool | Core logic, minimal UX | Days |
| Training workshop | Demo + 3 practice cases | Days |
| Mobile app | PWA wrapper around web app | Days to weeks |
| Full software product | All paths, accounts, analytics | Weeks to months |

### Card 3: The "Start Here" Default

If you can't decide: **make it a GOSM Skill first.** Reasons:
1. Fastest to create (it's just a markdown file)
2. Immediately testable (run `/skillname [input]`)
3. Forces good structure (the skill format is already procedure-shaped)
4. Easy to upgrade later (skill logic → software spec)
5. Documents the procedure even if the software never gets built

---

## COMMON MISTAKES

**1. Building software before validating the procedure.**
The procedure is a hypothesis about how to make this decision. Test it as a document or skill first. Find the errors. Then build software around the corrected version. Software freezes logic; don't freeze wrong logic.

**2. Choosing the medium before understanding the audience.**
"Let's build an app!" No — first: who uses this, when, where, and how? The medium follows from the use context, not from what's exciting to build.

**3. Trying to preserve every branch and warning in every format.**
A pocket reference card cannot contain 60 steps. A wall poster cannot contain worked examples. Match the content to the format's capacity. Multiple formats at different fidelity levels are better than one format that tries to do everything.

**4. Making the skill too literal a translation.**
A GOSM skill is instructions to an AI, not a human flowchart. Don't write "Ask yourself if X is true." Write "Assess whether X applies to the input based on [criteria]." The AI needs analytical instructions, not introspective prompts.

**5. Skipping the test-with-real-users step.**
You know how the procedure works because you wrote it. You'll navigate it perfectly. The test that matters is: can someone who has never seen it get to the right answer? If you skip this, you'll ship something that works for you and confuses everyone else.

**6. Over-engineering the first version.**
The first version should be embarrassingly simple. One path, no edge cases, no polish. If the core logic is wrong, polish is wasted. Ship the skeleton, test it, then add flesh.

**7. Forgetting maintenance.**
Every artifact needs an owner. If nobody will update the web app when the procedure changes, don't build a web app. Build the simplest format that the available maintainer can handle.

---

## WHEN TO OVERRIDE THIS PROCEDURE

1. **The procedure is safety-critical** (medical, aviation, emergency response). Do NOT self-serve. Work with domain experts and follow regulated documentation standards (e.g., ISO, FDA guidance).

2. **The procedure is for a regulated industry.** Legal, financial, and healthcare procedures may have specific format requirements. Check compliance requirements before choosing a medium.

3. **You already have a working implementation** and just need to update it. Don't start from scratch — apply the DCP changes to the existing artifact.

4. **The procedure is evolving rapidly** (still being tested weekly). Stay in the most editable format (markdown skill or Google Doc) until it stabilizes. Don't build software around a moving target.

5. **Someone else has already built this.** Before implementing, search for existing tools that solve the same decision problem. Don't rebuild what exists.

---

## WORKED EXAMPLES

### Example 1: DCP on "Evaluating a Job Offer" → Multiple Formats

**Step 0**: Goal is to make it broadly usable → Section F (Not Sure)
- F1: Job seekers, typically 25-45, mixed technical ability
- F2: When they receive an offer and have days to decide
- F3: At home, on computer or phone
- F4: A few times in their career
- F5: No development resources

**Route**: F1 non-technical + F3 phone/computer + F4 occasionally → Section C (Document) and Section B (Web App) as a stretch goal

**Section C path**: C1 → Read on screen → C2 → Format as PDF with table of contents, bold decision points, Quick Reference on final page.

**Result**: A clean PDF titled "Job Offer Evaluation Procedure v1.0" that someone can download, read through with their offer letter in hand, and reach a decision.

**Stretch**: Later, build a simple web form (Section B, no-code approach) that asks the questions and tallies the scores.

---

### Example 2: DCP on "Debugging Any Software Bug" → GOSM Skill

**Step 0**: Audience uses Claude Code → Section A (Skill Conversion)

- A1: 45 steps, 5 sections → Compound skill. Go to A2.
- A2: Decompose into: `/dbg-classify` (what type of bug?), `/dbg-repro` (reproduce it), `/dbg-isolate` (find the cause), `/dbg-fix` (implement the fix), `/dbg-verify` (confirm it's fixed). Router skill: `/dbg`.
- A3: Create 6 SKILL.md files. Convert "Is the bug reproducible?" → "Attempt to reproduce the bug using the provided steps. Report: reproducible / intermittent / not reproducible."
- A4: Needs access to codebase → Add: "Read the relevant source files" and "Run the test suite."
- A5: Test on a null pointer bug (straightforward), a race condition (edge case), and a "it works on my machine" report (ambiguous). Two pass, one needs a new branch for environment-dependent bugs. Fix added.
- A6: Place in `skills/dbg/`, `skills/dbg-classify/`, etc.

**Result**: A working `/dbg` skill that walks through structured debugging, callable from Claude Code.

---

### Example 3: DCP on "Managing Superintelligence Arrival" → Multiple Outputs

**Step 0**: Multiple goals:
- Make it a reference document for policymakers → Section C
- Make it a GOSM skill for AI-assisted planning → Section A
- Eventually make it an interactive web tool → Section B

**Section C path**: C1 → Print and use at desk → C2 → Format as letter-size PDF. The 6 role-based sections become tabbed pages. Quick Reference Cards become a standalone summary sheet. Include the "Red Flags" card as a one-page pullout.

**Section A path**: A1 → 60+ steps → Skill family. A2 → Decompose: `/si-classify` (what role are you?), `/si-assess` (assess your dimensions), `/si-plan` (generate action items), `/si-review` (quarterly review trigger). A3 → Convert human-facing questions to AI analysis prompts. A5 → Test with three user profiles.

**Section B path** (later): B1 → Phone + online + no accounts → Simple web app. B2 → Step 0 becomes a role-selection screen, each section becomes a wizard with one question per screen, ACTION items become result cards. B4 → AI code generation using the DCP + UI mapping as spec. B5 → Build main path (citizen section) first.

**Result**: Three artifacts from one DCP — a PDF for offline reference, a skill for AI-assisted use, and a web app spec ready to build.

---

## STEP 5: Failure Modes

**F1: Analysis Paralysis on Format Choice.**
*What it looks like*: Spending more time deciding what to build than it would take to build the simplest option.
*Fix*: Default to GOSM Skill (Card 3). Build it. If it's insufficient, you'll know why, and that tells you what to build next.

**F2: Building Software Around Untested Logic.**
*What it looks like*: Weeks of development, then discovering the procedure gives wrong answers.
*Fix*: Always test the procedure as a document or skill BEFORE building software. The procedure must work on paper first.

**F3: Choosing Medium Based on What's Fun to Build.**
*What it looks like*: Building a React app when a Google Doc would serve the audience better.
*Fix*: Re-read Section F. Answer the five questions honestly. Let the audience determine the medium.

**F4: Literal Translation Without Adaptation.**
*What it looks like*: A skill that says "Go to Section B" instead of "→ INVOKE: /skillname". A web app that displays raw markdown.
*Fix*: Each medium has its own idioms. Translate the LOGIC, not the FORMAT. The procedure's structure should inform the artifact, not be copy-pasted into it.

**F5: Trying to Ship Everything at Once.**
*What it looks like*: Building a web app with all sections, all edge cases, all failure warnings, all worked examples before anyone has used it.
*Fix*: MVP = main path only. Ship it. Get feedback. Add the rest iteratively.

**F6: No Maintenance Plan.**
*What it looks like*: A beautiful web app that's wrong 6 months later because the underlying procedure changed.
*Fix*: Before building, answer: "Who will update this, and how?" If the answer is "nobody," build in the simplest possible format.

---

## STEP 6: Validation Check

| Check | Status |
|---|---|
| Can someone with no expertise follow this? | **Pass** — all steps are concrete actions with clear outputs |
| Are all decision points clear? | **Pass** — all binary or explicit multiple choice |
| Does every path lead to a concrete output? | **Pass** — every section ends with a deliverable artifact |
| Are there dead ends or loops? | **Pass** — Section F routes to other sections; all sections terminate |
| Are the actions actually doable? | **Pass** — each step specifies what to do and what success looks like |

---

```
VALIDATION STATUS: This procedure has not been validated by domain
experts. It reflects practical patterns from procedure documentation,
skill authoring, and software development.

Review triggers (re-run this procedure if any occur):
- The GOSM skill format changes
- New no-code tools significantly change the build calculus
- You've completed 5+ conversions and notice missing patterns
```
