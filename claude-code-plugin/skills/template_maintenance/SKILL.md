---
name: template_maintenance
description: Maintain and improve domain templates over time. Track usage, identify gaps, and evolve templates based on experience.
---

# Template Maintenance

**Input**: $ARGUMENTS

---

## Purpose

Keep domain templates effective over time:
- **Track** template usage and outcomes
- **Identify** gaps and improvement opportunities
- **Evolve** templates based on experience
- **Validate** templates remain accurate
- **Retire** outdated templates

---

## Maintenance Operations

### TRACK: Record Template Usage

After using a template, record the outcome:

```
TEMPLATE USAGE LOG: [template name]

SESSION: [date/id]

USAGE DETAILS:
- Template: [name]
- Version: [version]
- Input: [brief description of what was analyzed]
- Skills executed: [which skills from chain were run]

OUTCOME:
- Completed successfully: [Yes/No/Partial]
- Output quality: [1-5 rating]
- User satisfaction: [if known]

OBSERVATIONS:
- What worked well: [list]
- What didn't work: [list]
- Missing dimensions: [any dimensions that should have been included]
- Missing assumptions: [any assumptions that should have been checked]
- Suggested improvements: [list]

LOG ENTRY CREATED: [timestamp]
```

---

### ANALYZE: Review Template Performance

Aggregate usage data to assess template health:

```
TEMPLATE ANALYSIS: [template name]

USAGE STATISTICS:
- Total uses: [N]
- Period: [date range]
- Success rate: [X%]
- Average quality: [X/5]

PATTERN ANALYSIS:

Most used skills:
| Skill | Usage Count | Skip Rate |
|-------|-------------|-----------|
| [skill] | [N] | [X%] |

Most common issues:
| Issue | Frequency | Impact |
|-------|-----------|--------|
| [issue] | [N times] | [HIGH/MED/LOW] |

Dimension coverage:
| Dimension | Used | Useful | Should Add |
|-----------|------|--------|------------|
| [dim] | [X%] | [Y%] | [suggestion] |

Assumption hit rate:
| Assumption | Checked | Was Relevant |
|------------|---------|--------------|
| [assumption] | [X%] | [Y%] |

HEALTH SCORE: [0-100]

RECOMMENDATIONS:
1. [Recommendation based on data]
2. [Recommendation based on data]
```

---

### IMPROVE: Update Template Based on Analysis

Apply improvements to a template:

```
TEMPLATE IMPROVEMENT: [template name]

CURRENT VERSION: [X.Y]
PROPOSED VERSION: [X.Y+1]

CHANGES BASED ON ANALYSIS:

1. DIMENSIONS
   Add: [new dimension] - Reason: [why needed based on usage]
   Remove: [dimension] - Reason: [why not useful]
   Modify: [dimension] - Change: [what to change]

2. ASSUMPTIONS
   Add: [new assumption] - Reason: [frequently relevant but missing]
   Remove: [assumption] - Reason: [rarely relevant]

3. SKILL CHAIN
   Add: [skill] at position [N] - Reason: [why needed]
   Remove: [skill] - Reason: [rarely used or not helpful]
   Reorder: [skill] from [N] to [M] - Reason: [why]

4. TRIGGERS
   Add: [trigger] - Reason: [users expected this to match]
   Remove: [trigger] - Reason: [false positives]

5. OUTPUT FORMAT
   Change: [what to modify]
   Reason: [why]

IMPROVEMENT VALIDATION:
- [ ] Changes address identified issues
- [ ] No breaking changes to existing workflows
- [ ] Version properly incremented
- [ ] Changelog updated

APPLY IMPROVEMENT: [Yes/No]
```

---

### VALIDATE: Check Template Accuracy

Periodically verify template is still valid:

```
TEMPLATE VALIDATION: [template name]

VALIDATION DATE: [date]
LAST VALIDATION: [date]
TEMPLATE VERSION: [version]

VALIDATION CHECKS:

1. SKILL CHAIN VALIDITY
   All skills exist and are accessible?
   | Skill | Exists | Current |
   |-------|--------|---------|
   | [skill] | [Y/N] | [Y/N - has it been updated?] |

2. DIMENSION RELEVANCE
   Are dimensions still the right ones for this domain?
   | Dimension | Still Relevant | Notes |
   |-----------|----------------|-------|
   | [dim] | [Y/N/Partial] | [notes] |

3. ASSUMPTION CURRENCY
   Are default assumptions still valid?
   | Assumption | Still Valid | Changed Context |
   |------------|-------------|-----------------|
   | [assumption] | [Y/N] | [if changed, how] |

4. TRIGGER ACCURACY
   Do triggers still correctly identify this domain?
   | Trigger | Accurate | False Positives | False Negatives |
   |---------|----------|-----------------|-----------------|
   | [trigger] | [Y/N] | [examples] | [examples] |

5. ANALOGY DOMAIN RELEVANCE
   Are suggested analogies still useful?
   | Domain | Still Useful | Better Alternative |
   |--------|--------------|-------------------|
   | [domain] | [Y/N] | [if no, what instead] |

VALIDATION RESULT:
- Overall status: [VALID / NEEDS_UPDATE / DEPRECATED]
- Critical issues: [list]
- Recommended actions: [list]

NEXT VALIDATION: [scheduled date]
```

---

### RETIRE: Deprecate Outdated Template

Remove templates that are no longer useful:

```
TEMPLATE RETIREMENT: [template name]

RETIREMENT REASON:
[ ] Superseded by: [new template name]
[ ] Domain no longer relevant
[ ] Merged into: [other template name]
[ ] Low usage (< [N] uses in [period])
[ ] Consistently poor outcomes
[ ] Other: [specify]

RETIREMENT PROCESS:

1. USAGE CHECK
   Recent usage: [N] times in last [period]
   Active users: [if known]
   Dependencies: [templates or workflows that use this]

2. MIGRATION PATH
   If superseded: Redirect to [new template]
   If merged: Content incorporated into [template]
   If deprecated: Alternative recommendation [suggestion]

3. ARCHIVE
   Archive location: templates/archive/[template_name]_[date].yaml
   Preserve: [what to keep for reference]

4. NOTIFICATION
   Users to notify: [if applicable]
   Deprecation notice: [message]

RETIREMENT STATUS:
- [ ] Usage checked
- [ ] Migration path defined
- [ ] Template archived
- [ ] Index updated
- [ ] Notifications sent (if applicable)

RETIREMENT COMPLETE: [Yes/No]
```

---

### REPORT: Template Health Dashboard

Overview of all templates:

```
===================================================
TEMPLATE HEALTH REPORT
Generated: [date]
===================================================

SUMMARY:
- Total templates: [N]
- Healthy: [N] ([X%])
- Needs attention: [N] ([X%])
- Deprecated: [N]

===================================================

TEMPLATE STATUS:

| Template | Version | Uses | Health | Last Validated | Action |
|----------|---------|------|--------|----------------|--------|
| [name] | [ver] | [N] | [Good/Warning/Critical] | [date] | [None/Update/Validate/Retire] |

===================================================

NEEDS ATTENTION:

1. [Template name]
   Issue: [what's wrong]
   Recommended: [action]

2. [Template name]
   Issue: [what's wrong]
   Recommended: [action]

===================================================

RECENT CHANGES:
- [date]: [template] updated to v[X]
- [date]: [template] created
- [date]: [template] retired

===================================================

UPCOMING MAINTENANCE:
- [date]: [template] due for validation
- [date]: [template] usage review

===================================================
```

---

## Maintenance Schedule

Recommended maintenance cadence:

| Activity | Frequency | Trigger |
|----------|-----------|---------|
| Usage logging | Every use | Automatic |
| Performance analysis | Monthly | Scheduled |
| Validation | Quarterly | Scheduled |
| Improvement | As needed | Analysis findings |
| Health report | Monthly | Scheduled |
| Retirement review | Quarterly | Low usage |

---

## Example: Improving Academic Research Template

```
TEMPLATE IMPROVEMENT: academic_research

CURRENT VERSION: 1.0
PROPOSED VERSION: 1.1

CHANGES BASED ON ANALYSIS:

1. DIMENSIONS
   Add: "Publication venue" [journal, conference, book, thesis]
   Reason: 15 of 20 recent uses needed this dimension

2. ASSUMPTIONS
   Add: "Reproducibility is possible"
   Reason: Emerged as critical in 8 uses

3. SKILL CHAIN
   Add: /dependency_extraction after /space_enumeration
   Reason: Research often has task dependencies

4. TRIGGERS
   Add: "systematic review"
   Reason: 5 users expected this to match

IMPROVEMENT VALIDATION:
- [x] Changes address identified issues
- [x] No breaking changes
- [x] Version incremented to 1.1
- [x] Changelog updated

APPLY IMPROVEMENT: Yes
```

---

## Quality Checklist

Before completing maintenance:
- [ ] Operation type clear (TRACK/ANALYZE/IMPROVE/VALIDATE/RETIRE)
- [ ] Data gathered or generated
- [ ] Analysis performed where applicable
- [ ] Recommendations specific and actionable
- [ ] Changes validated before applying
- [ ] Records updated

---

## Integration

Use with:
- `/domain_template` - Create templates to maintain
- `/template_registry` - Store and retrieve templates
- Learning infrastructure - Feed improvements into self-improvement pipeline
