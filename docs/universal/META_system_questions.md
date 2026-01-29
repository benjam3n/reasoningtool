# Meta: System Questions About Universal Guess Libraries

**Category**: META - Questions about the guess library system itself
**Purpose**: Document answers found and remaining uncertainties about the universal library structure
**Created**: 2026-01-26
**Structure**: One question per entry, VOI-marked with realistic distribution

---

## VOI Rating = Action Divergence

- **HIGH**: Different answers → completely different action paths
- **MED**: Different answers → same general direction, different approach
- **LOW**: Different answers → same actions, different framing/flavor

---

## Q1: Is the TAXONOMY.md canonical or aspirational?

[VOI: HIGH - determines which file structure to follow]

**ANSWER FOUND**: The TAXONOMY.md is **aspirational/outdated**.

**Evidence**:
- TAXONOMY.md describes files like `20_certainty_knowledge.md`, `40_bias_cognitive.md`
- Actual files follow different naming: `20_learning.md`, `40_behaviors.md`
- PROGRESS.md documents the actual structure:
  - Files 01-20: Core Dimensions (early creation, some need revision)
  - Files 21-61: YAML-mapped categories (map to `universal_goal_analysis.yaml`)
  - Files 62-66: Mathematical categories (later additions)
- The TAXONOMY.md scheme was never fully implemented

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| TAXONOMY.md is canonical | HIGH | Follow TAXONOMY vs. PROGRESS | Using outdated structure = wrong files | Use PROGRESS.md |
| TAXONOMY.md is aspirational | MED | Acknowledged as future plan vs. current | Use actual files | Already implemented |
| TAXONOMY.md is outdated | LOW | Just historical artifact vs. relevant | Ignore TAXONOMY | Still relevant |
| **CONFIRMED: TAXONOMY.md is outdated** | - | PROGRESS.md is canonical | **Use PROGRESS.md** | - |

**Resolution**: Trust PROGRESS.md for actual file structure. TAXONOMY.md should be archived or updated.

---

## Q2: What generation method produces 486 guesses from 72 actual entries?

[VOI: MED - affects expectations but same usage approach]

**ANSWER FOUND**: The "486 guesses" is **inflated/old format**.

**Evidence**:
- PROGRESS.md notes `01_who_agent.md` "Needs revision"
- Files created before revision (01-05, B0) have inflated counts in headers
- Files after revision have accurate counts:
  - `06_why_reason.md` claims 62 → actually has ~62
  - `22_goal_definition.md` claims 55 → actually has 55
- No "expansion mechanism" exists - the counts were simply aspirational

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| 486 includes dynamic expansion | HIGH | Expecting expansion vs. none | Wait for expansion | Count is actual |
| 486 is aspirational (planned) | MED | Planning to add more vs. complete | Plan to expand | Already complete |
| 486 is error (old format) | LOW | Just needs update vs. correct | Fix header | Header is correct |
| **CONFIRMED: Old format error** | - | Early files have wrong counts | **Trust actual entries** | - |

**Resolution**: Trust actual entry count in file, not header. Files 01-05, B0 need revision which will fix counts.

---

## Q3: Are files 01-66 complete or partial?

[VOI: HIGH - determines which files are reliable to use]

**ANSWER FOUND**: **Mixed completion status**.

**Evidence from PROGRESS.md**:
- Files 06-61: Status "Done" (56 files with correct VOI distribution)
- Files 01-05, B0: Status "Needs revision" (content exists but outdated)
- Files 62-66: Mathematical categories, appear complete
- 19 YAML categories still need files (Rate/Accumulation, Structure/Mapping, etc.)

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| All files are complete | HIGH | Use confidently vs. verify | Assuming false completeness | Some incomplete |
| All files are incomplete/draft | MED | Verify everything vs. use | Over-cautious | Most are done |
| Mixed: 56 done, 8 need revision | LOW | Accurate assessment | Use done files | All same status |
| **CONFIRMED: Mixed status** | - | 56 done, 6 need revision, 19 categories missing | **Check PROGRESS.md per file** | - |

**Resolution**: Check PROGRESS.md for per-file status before using. Files 06-61 are reliable.

---

## Q4: Why do some files have "Source" lines and others don't?

[VOI: LOW - affects understanding but same usage]

**ANSWER FOUND**: **Creation order difference**.

**Evidence**:
- Files 21-61 have Source lines: `[O: universal_goal_analysis.yaml lines X-Y]`
- Files 01-20 don't have Source lines
- Files 21-61 were created by mapping to `universal_goal_analysis.yaml` categories
- Files 01-20 were created before this YAML-mapping convention

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Source lines required for validity | MED | Only use 21-61 vs. all | Over-restriction | 01-20 also valid |
| Source lines are helpful context | LOW | Nice to have vs. required | Use source for reference | Source not needed |
| Source lines indicate creation method | LOW | Just metadata vs. validity | Note different origin | Same origin |
| **CONFIRMED: Creation method difference** | - | 21-61 mapped to YAML, 01-20 predated YAML | **Both valid, different origin** | - |

**Resolution**: Source lines indicate YAML mapping. Files without Source lines are still valid, just created differently.

---

## Q5: What triggers use of universal vs. domain-specific?

[VOI: HIGH - determines how to invoke correct library]

**ANSWER FOUND**: **Keyword matching**.

**Evidence from `guess_library.py`**:
```python
def lookup_library(user_input):
    user_words = set(re.findall(r'\w+', user_input.lower()))
    for library in index["libraries"]:
        keywords = set(kw.lower() for kw in library["keywords"])
        overlap = len(user_words & keywords)
        if overlap > best_score:
            best_match = library
```
- Tokenizes user input
- Compares against library keywords in `index.json`
- Returns library with highest keyword overlap (≥1 match required)
- Domain libraries: "software", "code", "research", "engineering", etc.
- Universal files: Used when no domain keyword match found

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Automatic detection | MED | Relying on automation vs. manual | Trust keyword match | Manual selection needed |
| Manual selection | LOW | User chooses vs. automatic | User selects library | Automatic works |
| **CONFIRMED: Keyword matching** | - | Best overlap wins | **Include keywords in input** | - |

**Resolution**: Include domain keywords in user input for automatic selection. Use `python scripts/guess_library.py lookup "user input"` to check which library matches.

---

## Q6: How are VOI ratings validated?

[VOI: HIGH - determines confidence level in ratings]

**PARTIAL ANSWER**: Framework exists, but **no empirical validation**.

**Evidence found**:
- VOI framework documented in TEMPLATE_unbundled_v2.md
- Target distribution: 10-25% HIGH, 40-50% MED, 30-40% LOW
- "Action Divergence" column forces explicit reasoning
- Validation checklist exists for manual review

**Evidence NOT found**:
- No empirical testing of whether ASSUME RIGHT/ASSUME WRONG actually diverge
- No user study data
- No automated validation
- No feedback loop from actual usage

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| VOI ratings are empirically validated | HIGH | Trust ratings blindly vs. question | False confidence | No validation exists |
| VOI ratings are expert-assigned | MED | Trust with caveats vs. blind | Some rigor | Automated rating |
| VOI ratings are heuristic only | LOW | Appropriately modest | Treat as guidance | Ratings are proven |
| VOI ratings need validation | MED | Improvement needed vs. sufficient | Build validation | Already validated |
| **CURRENT: Heuristic without validation** | - | Expert assignment, no testing | **Use as guidance, not truth** | - |

**Gap remains**: No validation procedure or data exists.

---

## Coverage Summary

```
QUESTIONS: 6
STATUS:
- Fully answered: 5 questions (Q1-Q5)
- Partially answered: 1 question (Q6)

CONFIRMED FINDINGS:
1. TAXONOMY.md is outdated - use PROGRESS.md
2. Guess counts in early files are wrong - trust actual entries
3. 56 files done, 6 need revision, 19 categories missing
4. Source lines indicate YAML-mapping, not validity
5. Keyword matching triggers domain selection
6. VOI ratings are heuristic, unvalidated (GAP)

ACTION ITEMS:
- Archive or update TAXONOMY.md
- Fix header counts in files 01-05, B0
- Create 19 missing YAML category files
- Build VOI validation procedure (GAP)
```

---

## Question Order by Action Divergence

**HIGH VOI (Ask First - Determines Correct Usage)**
1. Q1: Taxonomy status - which structure to follow
2. Q3: File completion - which files are reliable
3. Q5: Library selection - how to get right library
4. Q6: Rating validation - how much to trust ratings

**MED/LOW VOI (Ask Second - Understanding)**
5. Q2: Count discrepancy - expectations
6. Q4: Source lines - context

---

## Key Insight

**VOI ≠ Complexity**. A simple metadata question can be LOW VOI if it doesn't change how you use the system.

**VOI = Action Divergence**. HIGH VOI means: if you're wrong about this system aspect, you'll use the wrong files or wrong ratings.

---

## Remaining Gap: VOI Validation

**What's missing**: A procedure to validate that VOI ratings are correct.

**Proposed validation approach**:
1. For each HIGH-VOI entry, ask: "Does ASSUME RIGHT vs ASSUME WRONG actually produce different strategies?"
2. Test with real users: Present scenario, flip assumption, check if strategy changes
3. Track: Rate of agreement between rated VOI and observed divergence
4. Adjust ratings based on evidence

**Until validated**: Treat VOI as informed guidance, not proven fact.
