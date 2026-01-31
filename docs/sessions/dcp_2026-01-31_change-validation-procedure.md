# DCP — Change Validation Procedure for the Reasoning Toolkit

**Date**: 2026-01-31
**Input**: steps to always making sure improvements and not regressions are being made for this project

---

## Decision Type: "Is this change an improvement or a regression?"

This procedure applies every time you modify the Reasoning Toolkit — adding skills, editing existing ones, changing infrastructure, updating the website, or modifying Python code.

---

## STEP 1: Decision Dimensions

What factors determine whether a change is an improvement vs. a regression?

| # | Dimension | Why It Matters |
|---|-----------|---------------|
| 1 | **Skill Integrity** | Do all 355 skills still parse correctly and contain valid SKILL.md files? A missing file or broken frontmatter silently breaks the system. |
| 2 | **Invocation Chain Validity** | Skills chain to other skills via `→ INVOKE: /name`. A renamed or deleted skill breaks every skill that calls it. |
| 3 | **Metadata Consistency** | `skills.json`, `catalog.json`, `skill_registry.yaml` must match the filesystem. Stale metadata means the website and discovery show wrong information. |
| 4 | **Website Build Health** | The Astro site must compile. Broken skill pages, missing data, or template errors make the public site unusable. |
| 5 | **Python Code Correctness** | The ARAW engine (11K lines), storage module, and GOSM runners must not crash on existing session data or standard operations. |
| 6 | **Session Compatibility** | 52 existing sessions with SQLite databases and metadata must remain loadable. Schema changes can silently corrupt historical data. |
| 7 | **Cross-Reference Completeness** | Category skills (orchestrators) must route to skills that actually exist. The routing tables in CLAUDE.md must be accurate. |
| 8 | **Skill Quality** | New or modified skills must meet the structural standard: frontmatter, purpose, steps, output format. Degraded quality spreads through chains. |
| 9 | **Git Cleanliness** | No accidental commits of `.env`, databases, `__pycache__`, or large binaries. The `.gitignore` must be respected. |
| 10 | **Documentation Accuracy** | README skill counts, CLAUDE.md routing tables, and getting-started guides must reflect reality. Stale docs mislead users. |
| 11 | **Backward Compatibility** | Users who have memorized `/skillname` commands must not find them silently renamed or removed without notice. |
| 12 | **Dependency Safety** | Python (`requirements.txt`) and Node (`package.json`) dependencies must not introduce vulnerabilities or break existing functionality. |

---

## STEP 2: Options Per Dimension

| Dimension | GREEN (good) | YELLOW (warning) | RED (broken) |
|-----------|-------------|-------------------|--------------|
| Skill Integrity | All SKILL.md files parse, have frontmatter | Some skills missing descriptions | Missing SKILL.md files, invalid YAML frontmatter |
| Invocation Chains | All `→ INVOKE:` targets exist | Targets exist but have been substantially changed | Target skill deleted or renamed without updating callers |
| Metadata Consistency | JSON/YAML matches filesystem exactly | Minor drift (new skill not yet in JSON) | Major drift — skills.json shows deleted/wrong skills |
| Website Build | `npm run build` succeeds, all pages render | Build succeeds with warnings | Build fails or pages 404 |
| Python Code | All modules import cleanly, core operations work | Deprecation warnings | ImportError, crashes on standard operations |
| Session Compatibility | All 52 sessions load and query correctly | New sessions work, old sessions have minor issues | Old sessions crash or return corrupt data |
| Cross-References | Every router skill points to existing skills | Router points to skill that exists but has changed scope | Router points to nonexistent skill |
| Skill Quality | Frontmatter + purpose + steps + output format | Missing one section | Stub with no content, or instructions that contradict themselves |
| Git Cleanliness | Only intended files staged, .gitignore respected | Untracked files present but not staged | Secrets, databases, or large binaries committed |
| Documentation | All counts, tables, and examples are current | Off by 1-2 skills in count | Major sections describe features that don't exist |
| Backward Compat | All existing skill names work | Skill renamed but old name redirects or is documented | Skill silently removed, users get errors |
| Dependency Safety | All deps at known-good versions | Minor version bumps, no known issues | Known vulnerabilities or breaking changes |

---

## STEP 3: Hidden Assumptions & Common Traps

| # | Assumption | Reality | Trap |
|---|-----------|---------|------|
| 1 | "I only changed one skill, nothing else is affected" | Skills chain. Changing `/dd` affects `/dcp`, `/gd`, and any skill that invokes `/dd`. | You must trace downstream consumers of any skill you edit. |
| 2 | "The JSON files update automatically" | They don't. `generate_skills_db.py` must be run manually. | Forgetting to regenerate means the website shows stale data. |
| 3 | "If it works for me, it works" | The website, the Claude Code plugin, and the Python CLI are three separate consumers of the same data. | Test all three surfaces, not just the one you're working in. |
| 4 | "Adding a skill can't break anything" | A new skill with a name that collides with an existing shorthand, or that introduces a circular invocation chain, breaks the system. | Check for name collisions and circular references. |
| 5 | "Small edits don't need validation" | A single typo in a `→ INVOKE:` line silently breaks a chain. | Even one-line edits need the chain check. |
| 6 | "The audit script catches everything" | `audit_procedure_library_health.py` checks YAML parseability and duplicates, but does NOT validate invocation chains or cross-reference accuracy. | The audit gives false confidence — it's necessary but not sufficient. |
| 7 | "Git history is my safety net" | True for code, but SQLite databases in `sessions/` are in `.gitignore`. Session data loss is permanent. | Back up session databases independently if they matter. |
| 8 | "README skill count is just cosmetic" | Users use the count to judge completeness and trustworthiness. A wrong count erodes credibility. | Update counts in README/CLAUDE.md if they changed. |

---

## STEP 4: The Procedure

```
CHANGE VALIDATION PROCEDURE
============================
For the Reasoning Toolkit project
Follow EVERY time you make a change, before committing.

STEP 0: What type of change is this?
┌─────────────────────────────────────┬──────────────┐
│ Change type                         │ Go to        │
├─────────────────────────────────────┼──────────────┤
│ Adding a new skill                  │ SECTION A    │
│ Editing an existing skill           │ SECTION B    │
│ Deleting or renaming a skill        │ SECTION C    │
│ Changing Python code (src/)         │ SECTION D    │
│ Changing website (website/)         │ SECTION E    │
│ Changing config/docs/README         │ SECTION F    │
│ Multiple types at once              │ Do each      │
│                                     │ applicable   │
│                                     │ section      │
└─────────────────────────────────────┴──────────────┘
After completing your section(s), ALWAYS go to SECTION G.


SECTION A: Adding a New Skill
─────────────────────────────
A1. Create the directory: skills/[name]/SKILL.md
    ✓ You should see: a new directory with one file

A2. Verify the SKILL.md has these required sections:
    □ YAML frontmatter (--- block with name and description)
    □ Purpose section
    □ Steps or procedure
    □ Output format
    → If any are missing: add them before continuing

A3. Check for name collisions:
    → Does any existing skill have this exact name?
    → Does any existing skill have an abbreviation that
       matches this name?
    → If yes to either: choose a different name

A4. If this skill uses → INVOKE: lines:
    → List every skill it invokes
    → For each: does that skill exist in skills/?
    → If any don't exist: either create them or remove
       the invocation
    → Check: does any invoked skill eventually invoke
       THIS skill? (circular reference)
    → If yes: break the cycle

A5. Determine which category skill(s) should route to
    this new skill:
    → Does it fit under /claim, /decide, /viability,
       /evaluate, /diagnose, /search, /want, /how,
       /emotion, /action, /create, /technical, /analyze?
    → If yes: open that category skill and add routing
       for the new skill
    → If no category fits: document it only in
       CLAUDE.md's direct skills table

A6. Regenerate metadata:
    → Run: python scripts/generate_skills_db.py
    ✓ You should see: skills.json updated with your
      new skill entry

A7. Go to SECTION F (to update docs), then SECTION G.


SECTION B: Editing an Existing Skill
─────────────────────────────────────
B1. Before editing, list all skills that INVOKE this skill:
    → Search all SKILL.md files for: INVOKE: /[skillname]
    ✓ You should see: a list of 0 or more calling skills

B2. Make your edit.

B3. If you changed the skill's NAME in frontmatter:
    → Update every calling skill found in B1
    → Update skills.json (regenerate)
    → Update catalog.json
    → Update skill_registry.yaml

B4. If you changed what the skill DOES (its purpose
    or output):
    → For each calling skill from B1:
       Does the caller still make sense with the new
       behavior?
    → If not: update the caller too

B5. If you changed → INVOKE: lines:
    → Do all new targets exist?
    → Are there circular references?

B6. Regenerate metadata:
    → Run: python scripts/generate_skills_db.py

B7. Go to SECTION G.


SECTION C: Deleting or Renaming a Skill
────────────────────────────────────────
C1. Search for ALL references to this skill:
    → Search all SKILL.md files for: /[skillname]
    → Search CLAUDE.md (both root and plugin)
    → Search README.md
    → Search getting-started.astro
    ✓ You should see: every place this skill is mentioned

C2. For each reference found:
    → If renaming: update to new name
    → If deleting: remove the reference or replace with
       alternative skill
    → DO NOT leave dangling references

C3. If deleting: remove the skills/[name]/ directory
    If renaming: rename the directory

C4. Update category/router skills that pointed to this
    skill

C5. Regenerate metadata:
    → Run: python scripts/generate_skills_db.py

C6. Go to SECTION F (to update docs), then SECTION G.


SECTION D: Changing Python Code (src/)
──────────────────────────────────────
D1. Identify what your change affects:
    □ ARAW engine (src/araw/)
    □ Storage (src/storage/)
    □ Runners (src/runners/)
    □ Utilities (src/utilities/)

D2. If you changed ARAW engine:
    → Can you still create a new ARAW session?
    → Can you still load an existing session from
       sessions/?
    → Pick one existing .db file and verify it loads
       without error
    ✓ You should see: no ImportError, no schema errors

D3. If you changed Storage:
    → Run: python -m storage list
    ✓ You should see: list of sessions without errors
    → Run: python -m storage search "test"
    ✓ You should see: search results or empty results,
      no crash

D4. If you changed Runners:
    → Verify gosm_runner.py and gosm_agent.py import
       cleanly:
       python -c "from runners import gosm_runner"
    ✓ You should see: no output (clean import)

D5. If you changed database schema:
    → WARNING: This can break all 52 existing sessions
    → Write a migration script BEFORE deploying
    → Test migration on a COPY of an existing .db file
    → Never modify sessions/*.db in place without backup

D6. Go to SECTION G.


SECTION E: Changing Website (website/)
──────────────────────────────────────
E1. Build the site:
    → Run: cd website && npm run build
    ✓ You should see: build completes with 0 errors

E2. Preview the site:
    → Run: cd website && npm run preview
    → Open in browser
    → Check: skills page loads and shows all skills
    → Check: individual skill pages render
    → Check: graph visualization loads
    → Check: getting-started page is accurate

E3. If skill data changed: verify skills.json was
    regenerated BEFORE building the website
    → The website reads from skills.json at build time
    → Stale JSON = stale website

E4. Go to SECTION G.


SECTION F: Update Documentation
───────────────────────────────
F1. Update skill count in these files if skills were
    added/removed:
    □ README.md (search for the number, e.g., "355")
    □ CLAUDE.md (root)
    □ website/src/pages/getting-started.astro
    □ website/src/pages/skills.astro (if count is shown)

F2. If a new category was added or routing changed:
    □ Update the routing table in CLAUDE.md (root)
    □ Update the routing table in
       claude-code-plugin/CLAUDE.md
    □ Update getting-started.astro

F3. If skill names changed:
    □ Update the "Direct Skills" table in CLAUDE.md


SECTION G: Pre-Commit Validation (ALWAYS DO THIS)
──────────────────────────────────────────────────
G1. Regenerate metadata (if not already done):
    → Run: python scripts/generate_skills_db.py
    ✓ You should see: skills.json is current

G2. Run the health audit:
    → Run: python src/utilities/audit_procedure_library_health.py
    ✓ You should see: no critical errors
    → If errors: fix them before committing

G3. Check invocation chain integrity:
    → Search all SKILL.md files for "INVOKE:"
    → For each target: verify the target directory exists
       in skills/
    → This is NOT automated — you must do it manually or
       write a script

G4. Verify git status:
    → Run: git status
    → Check: no .env, .db, __pycache__, or secrets staged
    → Check: no files in sessions/ staged (gitignored)
    → Check: all intended changes are staged

G5. Build the website (if any skill or metadata changed):
    → Run: cd website && npm run build
    ✓ You should see: 0 errors

G6. Verify Python imports (if src/ changed):
    → Run: python -c "import sys; sys.path.insert(0,'src');
       from araw import araw_engine; from storage import
       session_store"
    ✓ You should see: no errors

G7. Commit with a descriptive message that states
    WHAT changed and WHY.
```

---

## STEP 5: Failure Modes

| # | Failure | How to Recognize | What to Do |
|---|---------|-----------------|------------|
| 1 | **Orphaned invocation** — a skill calls `/xyz` but `/xyz` was deleted | You'll see it only when a user hits that chain. No error at rest. | Run G3 (chain integrity check) every time. Consider automating this as a script. |
| 2 | **Stale skills.json** — forgot to regenerate after adding a skill | Website shows old skill count or missing skill page. | Make G1 a non-negotiable step. Consider a git pre-commit hook that runs `generate_skills_db.py`. |
| 3 | **Circular invocation** — Skill A invokes B, B invokes A | Claude enters an infinite loop when the skill is used. | Before adding any `→ INVOKE:` line, trace the full chain to confirm no cycles. |
| 4 | **Silent schema break** — changed a SQLite column, old sessions crash | Error appears only when loading a specific old session. | Never change schema without a migration. Test against the oldest session. |
| 5 | **Count mismatch** — README says "355 skills" but there are now 358 | Users notice and lose trust. Easy to miss because it's a manual update. | After adding/removing skills, search all docs for the old count. |
| 6 | **Category router gap** — new skill fits a category but wasn't added to the router | Users who enter via category skills never discover the new skill. | A5 in Section A explicitly requires this. |
| 7 | **Partial rename** — renamed skill directory but missed references in 3 other skills | Those 3 skills break when they try to invoke the old name. | C1 requires exhaustive search. Use `grep -r "/oldname" skills/` to be thorough. |
| 8 | **Website build succeeds but pages are wrong** — skills.json was stale when Astro built | Pages exist but show wrong descriptions or missing skills. | Always regenerate JSON *before* building the website, not after. |
| 9 | **Dependency regression** — npm or pip update breaks build | Website fails to build or Python scripts crash after update. | Pin dependency versions. Don't update dependencies as part of a content change. |

---

## QUICK REFERENCE CARD

```
BEFORE EVERY COMMIT:
  1. python scripts/generate_skills_db.py
  2. python src/utilities/audit_procedure_library_health.py
  3. Grep all SKILL.md files for INVOKE targets → verify each exists
  4. git status → no secrets, no .db files, no __pycache__
  5. cd website && npm run build (if skills/metadata changed)
  6. python -c "from araw import araw_engine" (if src/ changed)
  7. Update skill counts in README/CLAUDE.md if they changed
```

## COMMON MISTAKES

1. Editing a skill without checking what invokes it (breaks callers)
2. Forgetting to run `generate_skills_db.py` (stale website/metadata)
3. Renaming a skill but only updating 2 of 5 references
4. Changing SQLite schema without a migration script
5. Committing with stale skill counts in documentation
6. Adding an `→ INVOKE:` to a skill that doesn't exist yet
7. Building the website before regenerating skills.json
8. Testing only in Claude Code but not checking the website

## WHEN TO OVERRIDE THIS PROCEDURE

- **Emergency hotfix for a broken production website**: Skip to Section E + G5, deploy, then come back and do the full procedure.
- **Experimental branch that won't be merged**: You can skip G5 (website build) but still do G1-G4 and G6.
- **The procedure itself is wrong**: If you find a step that doesn't match reality, fix THIS procedure first (it's a living document), then follow the updated version.

## WORKED EXAMPLES

### Example 1: Adding a new skill `/xyz`

1. Create `skills/xyz/SKILL.md` with frontmatter, purpose, steps, output format
2. It invokes `/se` and `/dd` — both exist, no circular refs ✓
3. It fits under `/analyze` category — open `/analyze/SKILL.md`, add routing for `/xyz`
4. Run `python scripts/generate_skills_db.py` — skills.json now has 356 entries ✓
5. Update README.md: "355" → "356"
6. Update CLAUDE.md routing tables if applicable
7. Run health audit — no errors ✓
8. Grep for `INVOKE:` — all targets valid ✓
9. `git status` — only intended files staged ✓
10. `cd website && npm run build` — success ✓
11. Commit: "Add /xyz skill for [purpose]"

### Example 2: Renaming `/analysis` to `/analyze`

1. Search all SKILL.md files for `/analysis` — found in 4 skills
2. Update all 4 calling skills to use `/analyze`
3. Rename directory: `skills/analysis/` → `skills/analyze/`
4. Update CLAUDE.md routing table (both copies)
5. Update README.md
6. Regenerate skills.json
7. Run health audit
8. Grep for `/analysis` across entire project — 0 results ✓
9. Build website
10. Commit: "Rename /analysis skill to /analyze"

### Example 3: Modifying the ARAW engine

1. Change made in `src/araw/araw_engine.py`
2. `python -c "from araw import araw_engine"` — imports cleanly ✓
3. Load an existing session DB — works ✓
4. `python -m storage list` — works ✓
5. No schema changes, no metadata changes
6. `git status` — only the one file staged ✓
7. Commit: "Fix [specific issue] in ARAW engine"

---

**Validation status**: This procedure has not been validated by domain experts. It was derived from analysis of the project's actual structure, build scripts, and recent git history. It should be tested against 5-10 real changes before being considered reliable.

**Recommended next step**: Automate G3 (invocation chain integrity check) as a script, since it's the highest-risk manual step. Consider adding it alongside `generate_skills_db.py` as a pre-commit check.
