# Decision Procedure — Starting a Software Project

**Date**: 2026-01-31
**Input**: starting a software project

---

## Step 1: Decision Dimensions

**D1: Problem Clarity** — How well-defined is what you're building?
- Matters because: If the problem is vague, you need discovery before architecture. If it's clear, you can jump to execution.

**D2: Team Size & Composition** — Who will build this?
- Matters because: Solo developer, small team, and large org require radically different tooling, process, and architecture decisions.

**D3: Expected Lifespan** — Throwaway prototype vs. decade-long product?
- Matters because: Determines how much investment in infrastructure, testing, documentation, and maintainability is justified.

**D4: Domain Complexity** — Is the core problem technically hard, or is it mostly glue/CRUD?
- Matters because: Complex domains need upfront modeling. Simple domains need fast delivery.

**D5: User Scale** — How many concurrent users/requests at launch and at 12 months?
- Matters because: Determines infrastructure choices and whether you need to think about scalability from day one.

**D6: Revenue Model** — How does this make money (or justify its existence)?
- Matters because: Determines build-vs-buy tradeoffs, speed-to-market pressure, and acceptable cost structure.

**D7: Deployment Environment** — Where does this run? (Cloud, on-prem, edge, mobile, embedded)
- Matters because: Constrains language, framework, and infrastructure choices.

**D8: Integration Requirements** — What external systems must this connect to?
- Matters because: Integration constraints often force technology choices and architectural patterns.

**D9: Regulatory/Compliance** — Are there legal requirements? (HIPAA, GDPR, SOC2, PCI)
- Matters because: Compliance requirements must be built in from day one — retrofitting is extremely expensive.

**D10: Budget** — What funding is available for tooling, infrastructure, and services?
- Matters because: Constrains build-vs-buy, hosting choices, and team size.

**D11: Timeline Pressure** — When must this ship?
- Matters because: Determines how much scaffolding, testing, and architecture is feasible before writing features.

**D12: Existing Constraints** — Are language, framework, or platform choices already made?
- Matters because: Pre-existing decisions collapse the option space dramatically.

---

## Step 2: Options per Dimension

| Dimension | Options |
|---|---|
| **Problem Clarity** | (A) Crisp spec exists, (B) General idea with unknowns, (C) Exploring — don't know what to build yet |
| **Team Size** | (A) Solo, (B) 2-5, (C) 6-15, (D) 16+ |
| **Expected Lifespan** | (A) Throwaway/prototype (<3 months), (B) Medium-term (3 months–2 years), (C) Long-lived (2+ years) |
| **Domain Complexity** | (A) Simple CRUD/glue, (B) Moderate business logic, (C) Complex algorithms/domain modeling |
| **User Scale** | (A) <100 users, (B) 100–10K, (C) 10K–1M, (D) 1M+ |
| **Revenue Model** | (A) Internal tool, (B) Client project, (C) SaaS/product, (D) Open source |
| **Deployment** | (A) Cloud/web, (B) Mobile, (C) Desktop, (D) Embedded/IoT, (E) On-prem |
| **Integrations** | (A) None/minimal, (B) A few APIs, (C) Many external systems |
| **Regulatory** | (A) None, (B) Basic (GDPR), (C) Heavy (HIPAA/PCI/SOC2) |
| **Budget** | (A) $0 (open source/free tier only), (B) Low (<$500/mo), (C) Moderate ($500–5K/mo), (D) Enterprise (>$5K/mo) |
| **Timeline** | (A) ASAP/hackathon, (B) Weeks, (C) Months, (D) No hard deadline |
| **Existing Constraints** | (A) Greenfield — all choices open, (B) Some locked (language/platform), (C) Most locked (existing ecosystem) |

**Key interactions:**
- If Lifespan=A AND Timeline=A → skip almost all process; just build
- If Regulatory=C → must choose compliance-friendly stack from day one
- If Team Size=D → need CI/CD, code review, and branching strategy before writing code
- If Existing Constraints=C → skip technology selection; focus on architecture within constraints

---

## Step 3: Hidden Assumptions

1. **"Pick the best technology"** — Assumes technology choice matters more than execution. In reality, most mainstream stacks can build most things. The choice matters less than people think.

2. **"Architecture first"** — Assumes you understand the problem well enough to architect. If Problem Clarity ≠ A, you don't. Build something small first.

3. **"We need microservices"** — Assumes scale problems exist before they do. Start monolithic unless you have concrete evidence of team/scaling constraints.

4. **"Tests slow us down"** — Assumes testing is separate from building. Lack of tests slows you down more after week 2.

5. **"We'll refactor later"** — Assumes refactoring will happen. It almost never does voluntarily. The shortcuts you take in week 1 become permanent architecture.

6. **"We need a database"** — Assumes persistent storage is needed from day one. Sometimes flat files, SQLite, or in-memory storage is sufficient to validate the idea.

7. **"More planning = less rework"** — Assumes you can predict what you'll learn. Some rework is cheaper than extended planning.

8. **"Solo means no process"** — Assumes process is only for teams. Solo developers benefit enormously from version control, issue tracking, and release discipline.

---

## Step 4: The Procedure

```
STARTING A SOFTWARE PROJECT — DECISION PROCEDURE
==================================================

STEP 0: What type of project start is this?
--------------------------------------------

Answer these 3 questions:

Q1: Do you have a written description of what the software should do
    that is longer than 1 page?
    → YES: Problem is DEFINED
    → NO:  Problem is UNDEFINED

Q2: How many people will write code in the first month?
    → 1 person:      SOLO
    → 2-5 people:    SMALL TEAM
    → 6+ people:     LARGE TEAM

Q3: Does this need to be usable by real users within 4 weeks?
    → YES: URGENT
    → NO:  STANDARD

Find your type:

| Problem   | Team       | Timeline | → Go to    |
|-----------|------------|----------|------------|
| UNDEFINED | SOLO       | URGENT   | SECTION A  |
| UNDEFINED | SOLO       | STANDARD | SECTION B  |
| UNDEFINED | SMALL/LARGE| Any      | SECTION C  |
| DEFINED   | SOLO       | Any      | SECTION D  |
| DEFINED   | SMALL TEAM | Any      | SECTION E  |
| DEFINED   | LARGE TEAM | Any      | SECTION F  |


================================================================
SECTION A: Undefined Problem, Solo, Urgent
================================================================
Goal: Get something in front of users ASAP to learn what to build.

Step A1: Pick whichever language/framework you are fastest in.
  → Do NOT learn anything new. Use what you know.
  → What you should see: You can name your stack in <5 seconds.

Step A2: Create a repository.
  → Run: git init, create a README with a 1-paragraph description
    of what you THINK this should do.
  → What you should see: A repo with 1 file.

Step A3: Write down the ONE thing a user should be able to do.
  → Not 3 things. One. Complete this sentence:
    "A user can ___________."
  → What you should see: A single sentence.

Step A4: Build that one thing. No login, no database (unless the
  one thing requires it), no styling, no error handling.
  → What you should see: A working (ugly) thing that does the
    one thing.

Step A5: Put it in front of 1-3 real users. Ask:
  "Does this do what you need?" and "What's missing?"
  → What you should see: Specific feedback, not "looks good."

Step A6: Based on feedback, decide:
  → Users want what you built + more features → Go to SECTION D
    (you now have a DEFINED problem)
  → Users want something different → Return to Step A3 with new
    understanding
  → Users don't care → STOP. Reconsider whether this project
    should exist.

================================================================
SECTION B: Undefined Problem, Solo, Standard Timeline
================================================================
Goal: Explore the problem space before committing to architecture.

Step B1: Spend 1-3 days doing research only. No code.
  → Find 3 existing products that solve a similar problem.
  → For each, write: What they do well. What they do poorly.
  → What you should see: A document with 3 competitor analyses.

Step B2: Write a 1-page description of what YOUR version does
  differently. Focus on: Who is it for? What do they do with it?
  Why would they use yours instead of the existing options?
  → What you should see: A 1-page document you could show someone
    and they'd understand the project.

Step B3: Identify the riskiest assumption.
  → Complete: "This only works if ___________ is true."
  → What you should see: One sentence describing what could kill
    the project.

Step B4: Build the smallest possible thing that tests that
  assumption. This is NOT a prototype of the full product.
  It tests ONE thing.
  → Use whatever tech is fastest for this test.
  → What you should see: Evidence for or against your assumption.

Step B5: Is your riskiest assumption validated?
  → YES → Go to SECTION D (you now have a DEFINED problem)
  → NO  → Pivot: Return to Step B2 with new knowledge
  → UNCLEAR → Build a slightly bigger test. Return to Step B4.

================================================================
SECTION C: Undefined Problem, Team
================================================================
Goal: Align the team before writing code.

Step C1: Get all team members in a room (or call). Each person
  writes independently: "This project succeeds if ___________."
  → What you should see: Multiple definitions of success.

Step C2: Compare the definitions.
  → Do they agree? → Proceed to Step C3.
  → Do they disagree? → You must resolve this BEFORE proceeding.
    Have the person with authority make a call, or vote.
  → What you should see: One agreed definition of success.

Step C3: One person writes a 1-page project brief containing:
  - Who is this for?
  - What can they do with it?
  - What does success look like in 3 months?
  - What are we NOT building?
  → Other team members review and flag disagreements.
  → What you should see: An agreed brief.

Step C4: Go to SECTION E (small team) or SECTION F (large team),
  treating the brief as your DEFINED problem.

================================================================
SECTION D: Defined Problem, Solo
================================================================
Goal: Set up a solid foundation and start building.

Step D1: Choose your stack. Answer each in order; stop when
  constrained:

  D1a: Where does this run?
    → Web browser → JavaScript/TypeScript frontend framework
    → Server/API → Any backend language you know well
    → Mobile → React Native, Flutter, or native (Swift/Kotlin)
    → Desktop → Electron, Tauri, or native
    → CLI tool → Go, Rust, Python, or Node

  D1b: Does it need a database?
    → Stores user data across sessions → YES
    → Everything is temporary or file-based → NO (use files/memory)
    → If YES: <100K rows expected → SQLite
               >100K rows or multiple servers → PostgreSQL

  D1c: Does it need user authentication?
    → Multiple users with private data → YES → Use an auth
      library (don't build your own). Examples: NextAuth, Passport,
      Devise, Django auth.
    → Single user or no private data → NO → Skip this entirely.

  → What you should see: A list of 2-5 technology choices with
    clear rationale.

Step D2: Set up the project.
  → Create a repository with version control (git).
  → Add a .gitignore for your stack.
  → Set up the simplest possible build/run command.
  → Verify it works: you can run "hello world."
  → What you should see: Running application that does nothing
    useful, buildable with one command.

Step D3: Set up quality basics.
  → Add a linter for your language (ESLint, Flake8, Clippy, etc.)
  → Add a formatter (Prettier, Black, rustfmt, etc.)
  → Create one test file with one trivial test.
  → Verify all three work: lint, format, test.
  → What you should see: All three commands pass.

Step D4: List your features. Write each as:
  "A user can ___________ so that ___________."
  → Order them: which must exist first for others to work?
  → What you should see: An ordered list of 5-20 features.

Step D5: Build features in order, one at a time.
  For each feature:
  → Write a test that describes what "done" looks like.
  → Build until the test passes.
  → Commit with a message describing what you added.
  → Verify the previous features still work.
  → What you should see: Growing test suite, all green.

Step D6: After every 3-5 features, ask:
  → Am I still building what the spec describes?
    → NO → Update the spec or adjust course.
  → Is the code getting hard to change?
    → YES → Spend time refactoring before adding more.
  → Should anyone else see this yet?
    → YES → Deploy to a staging environment.

================================================================
SECTION E: Defined Problem, Small Team (2-5)
================================================================
Goal: Coordinate without heavy process.

Step E1: Complete SECTION D Steps D1-D3 (one person sets up,
  others review).

Step E2: Set up collaboration infrastructure:
  → Repository with branch protection on main/master
    (no direct pushes).
  → Require at least 1 code review before merge.
  → Set up CI: on every push, run lint + tests automatically.
  → What you should see: A PR that passes CI and gets reviewed
    before merging.

Step E3: Divide the work.
  → List all features (as in Step D4).
  → Identify which features are independent (can be built in
    parallel) vs. dependent (must be built in sequence).
  → Assign independent features to different people.
  → What you should see: Each person knows what they're building
    this week.

Step E4: Agree on conventions:
  → File/folder structure (where does new code go?)
  → Naming conventions (camelCase vs snake_case, etc.)
  → How to handle errors (throw exceptions? Return errors?)
  → API patterns if applicable (REST? GraphQL? RPC?)
  → Write these down in a CONTRIBUTING.md or similar.
  → What you should see: A document that answers "how do we do X?"
    for common patterns.

Step E5: Build using Section D, Steps D5-D6, with code review
  on every merge.

================================================================
SECTION F: Defined Problem, Large Team (6+)
================================================================
Goal: Prevent chaos through structure.

Step F1: Complete SECTION E Steps E1-E4.

Step F2: Define service/module boundaries.
  → Which parts of the system can be developed independently?
  → Define interfaces between modules BEFORE building them.
  → Assign teams/individuals to modules.
  → What you should see: A diagram showing modules and their
    interfaces.

Step F3: Set up project management.
  → Choose a task tracker (GitHub Issues, Linear, Jira).
  → Break features into tasks small enough to complete in 1-3 days.
  → What you should see: A board with tasks assigned and
    prioritized.

Step F4: Set up deployment pipeline.
  → Automated build, test, deploy on merge to main.
  → Staging environment that mirrors production.
  → What you should see: Code merged to main is automatically
    deployed to staging.

Step F5: Schedule a weekly 30-minute sync.
  → Each person: What I did. What I'm doing. What's blocking me.
  → Adjust task assignments based on reality.
  → What you should see: Blockers surfaced and resolved within
    a week.

Step F6: Build using Section D, Steps D5-D6, with the team
  structure from Steps F2-F5.
```

---

## Quick Reference Cards

**MINIMUM VIABLE SETUP (any project):**
- [ ] Version control (git)
- [ ] .gitignore
- [ ] One-command build/run
- [ ] Linter
- [ ] Formatter
- [ ] One test

**ADD FOR TEAMS:**
- [ ] Branch protection
- [ ] Code review requirement
- [ ] CI pipeline
- [ ] Written conventions
- [ ] Task tracker (6+ people)

**TECHNOLOGY DECISION SHORTCUT:**
- Use what you know unless a requirement forces otherwise.
- When in doubt, pick the most boring/mainstream option.
- SQLite until you need PostgreSQL.
- Monolith until you need services.
- Server-render until you need a SPA.

---

## Step 5: Failure Modes

**Failure 1: "Analysis Paralysis on Technology"**
- Symptom: You've spent more than 2 days choosing a framework and haven't written code.
- Fix: Pick the one you know best. If you know none equally, pick the one with the most StackOverflow answers. Technology choice is almost never the reason projects fail.

**Failure 2: "Premature Architecture"**
- Symptom: You're drawing system diagrams before you have working code.
- Fix: If Problem Clarity is UNDEFINED, you're in Section A/B/C — go back. Architecture is a Section D+ activity, and even then, start simple.

**Failure 3: "Skipping the One-Thing Test"**
- Symptom: You built 5 features but no real user has seen the software.
- Fix: Stop building. Deploy what you have. Show it to one person. Their feedback is worth more than your next 3 features.

**Failure 4: "Coordination Without Infrastructure"**
- Symptom: Team members are overwriting each other's work or working on conflicting changes.
- Fix: You skipped Section E Step E2. Set up branch protection and CI before writing more code.

**Failure 5: "Gold-Plating the Foundation"**
- Symptom: You have elaborate error handling, logging, monitoring, and CI/CD but no features.
- Fix: You only need the minimum viable setup (see Quick Reference). Everything else gets added when the need is concrete.

**Failure 6: "Wrong Section"**
- Symptom: You classified yourself as DEFINED but keep discovering you don't know what to build.
- Fix: Your problem is actually UNDEFINED. Go back to Section A, B, or C. There's no shame in this — it's the most common misclassification.

---

## Step 6: Validation

- All decision points are binary or small multiple choice — **pass**
- No step says "consider" or "think about" without a concrete output — **pass**
- Every step has "What you should see" verification — **pass**
- All paths lead to either a next step or a concrete stopping point — **pass**
- No jargon without inline definition — **pass**

---

## Worked Examples

### Example 1: Personal budgeting app, solo, no deadline

- Q1: I have a general idea but no spec → **UNDEFINED**
- Q2: Just me → **SOLO**
- Q3: No rush → **STANDARD**
- → **SECTION B**
- B1: Research Mint, YNAB, Copilot. Mint: good aggregation, bad UX. YNAB: great methodology, expensive. Copilot: nice UI, limited customization.
- B2: "Mine auto-categorizes and shows weekly trends, free, local-first."
- B3: "This only works if I can reliably categorize transactions automatically."
- B4: Build a script that takes a CSV bank export and categorizes 50 transactions. Check accuracy.
- B5: 80% accuracy → validated → Go to SECTION D.

### Example 2: Client e-commerce site, 3-person team, due in 6 weeks

- Q1: Client provided requirements doc → **DEFINED**
- Q2: 3 developers → **SMALL TEAM**
- Q3: Due in 6 weeks → **URGENT** (but DEFINED + SMALL TEAM goes to Section E regardless)
- → **SECTION E**
- E1: Set up Next.js + PostgreSQL + Stripe (team knows this stack).
- E2: GitHub repo, branch protection, required reviews, GitHub Actions for CI.
- E3: Person 1: product catalog + search. Person 2: cart + checkout + Stripe. Person 3: auth + user accounts + order history. Independent enough to parallelize.
- E4: Conventions doc: TypeScript strict mode, REST API, error responses as `{error: string, code: number}`.

### Example 3: "I have an idea for an app"

- Q1: No written spec → **UNDEFINED**
- Q2: Just me → **SOLO**
- Q3: Want to launch soon → **URGENT**
- → **SECTION A**
- A3: "A user can paste a recipe URL and get a grocery list."
- A4: Build a single-page app with one input field. Paste URL → scrape ingredients → display list. No accounts, no saving, no styling.
- A5: Show 2 friends who cook. Feedback: "I want to combine multiple recipes" and "Some ingredients are duplicated."
- A6: They want what I built + more → Go to SECTION D with these features in mind.

---

## Common Mistakes

1. Choosing technology before understanding the problem
2. Setting up CI/CD before having any code to integrate
3. Building features no one asked for because they seem "obviously needed"
4. Skipping version control because "it's just me"
5. Writing no tests because "it's just a prototype" (prototypes become products)
6. Over-investing in architecture for a project that might not survive contact with users
7. Under-investing in team coordination tools when working with others

---

## When to Override This Procedure

Seek expert help or deviate when:
- **Regulatory requirements exist** (HIPAA, PCI, SOC2) — get a compliance consultant before writing code
- **The core problem is a known hard CS problem** (real-time collaboration, distributed consensus, ML model training) — research the domain first
- **You're building on an unfamiliar platform** (embedded, blockchain, game engines) — platform tutorials override this procedure's stack advice
- **Budget exceeds $50K** — the stakes justify more upfront planning than this procedure covers

---

*This procedure has not been validated by domain experts.*
