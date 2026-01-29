---
name: code_review
description: "Procedure for conducting effective code reviews using Claude Code's capabilities for exhaustive analysis"
context: fork
---

# Code Review

**Input**: $ARGUMENTS

---

## Overview

Procedure for conducting effective code reviews that improve quality and share knowledge. This procedure leverages Claude Code's unique capabilities: exhaustive pattern search, codebase-wide consistency checking, and automated verification.

---

## Step 0: Context Assessment

| Factor | Value | Notes |
|--------|-------|-------|
| Change size | SMALL (<50 lines) / MED (50-300) / LARGE (300+) | |
| Risk level | HIGH (security, data) / MED / LOW | |
| Review depth | THOROUGH / STANDARD / QUICK | |

**If SMALL + LOW risk**: Steps 1, 3, 6, 7 only
**If LARGE or HIGH risk**: All steps + extra scrutiny

---

## Step 1: Understand the Context

Before reviewing code, understand what it's trying to accomplish.

**What to understand**:
1. PR title and description
2. Linked issues or tickets
3. Scope: bug fix, feature, refactor?
4. Specific review requests from author
5. Part of larger initiative?

**LLM Execution**:
```
# If given a PR URL/number, get PR info
→ Use Bash: gh pr view [number] --json title,body,files

# If given files directly, understand from context
→ Use Read: [changed files] to understand purpose

# Check for linked issues
→ Use Bash: gh issue view [number] (if referenced)
```

**Output format**:
```
CONTEXT
=======
Purpose: [what this change accomplishes]
Scope: [bug fix / feature / refactor / other]
Risk areas: [security, performance, data, none]
Review focus: [what author specifically wants reviewed]
```

---

## Step 2: High-Level Architecture Review

Review the overall approach before diving into details.

**What to check**:
1. Files changed - does scope make sense?
2. Approach aligns with existing architecture?
3. Change is in the right place?
4. Any simpler approaches?
5. Cross-cutting concerns (logging, errors, auth)?

**LLM Execution**:
```
# See all changed files
→ Use Bash: gh pr diff [number] --name-only
  OR: git diff --name-only [base]...[head]

# Understand file organization
→ Use Glob: pattern="**/*.{py,js,ts}" (or relevant extensions)

# Check if similar functionality exists elsewhere
→ Use Grep: pattern="[similar_function_name]" to find existing implementations

# Understand dependencies of changed files
→ Use Grep: pattern="import.*[changed_module]|from [changed_module]"
```

**Output format**:
```
ARCHITECTURE
============
Files changed: [count and summary]
Scope appropriate: [YES / NO - reason]
Architecture alignment: [YES / concern if NO]
Simpler approach: [suggestion or "none identified"]
Cross-cutting concerns: [noted or "none"]
```

---

## Step 3: Detailed Line-by-Line Review

Review each changed file systematically.

**What to check per file**:
1. Correctness - logic works for all cases?
2. Common bug patterns (null checks, boundaries, error handling)
3. Security implications
4. Readability and maintainability
5. Code style consistency

**LLM Execution**:
```
# Read each changed file
→ Use Read: [file_path]

# For each file, also check:
# - Related test file
→ Use Glob: pattern="**/test*[filename]*" or "**/[filename]*test*"

# - How the changed code is used
→ Use Grep: pattern="[function_name]\(" to find callers

# - If modifying existing function, check all usages
→ Use Grep: pattern="[modified_function]" output_mode="content" -C 2
```

**Common Bug Patterns to Check**:

| Pattern | What to look for | Severity |
|---------|------------------|----------|
| **Null safety** | Unguarded access, missing null checks | CONCERN |
| **Boundaries** | Off-by-one, empty arrays, max values | CONCERN |
| **Error handling** | Swallowed exceptions, missing handlers | CONCERN |
| **Resource leaks** | Unclosed files/connections | BLOCKING |
| **Injection** | Unsanitized user input in SQL/shell/HTML | BLOCKING |
| **Race conditions** | Shared mutable state without synchronization | BLOCKING |

**Security Patterns (Always BLOCKING)**:
| Pattern | What to look for | How to detect |
|---------|------------------|---------------|
| **SQL Injection** | String concatenation in queries | Grep: `query.*\+.*\$|f".*{.*}.*SELECT` |
| **XSS** | Unescaped user input in HTML | Grep: `innerHTML.*\$|dangerouslySetInnerHTML` |
| **Auth Bypass** | Missing auth checks, hardcoded credentials | Grep: `password.*=.*"|api.key.*=` |
| **Path Traversal** | User input in file paths | Grep: `open\(.*\$|readFile.*\$` |
| **SSRF** | User input in URLs/requests | Grep: `fetch\(.*\$|requests\.get\(.*\$` |
| **Secrets in Code** | API keys, passwords in source | Grep: `api.key|secret|password.*=.*["\']` |

**Performance Patterns (Usually CONCERN)**:
| Pattern | What to look for | How to detect |
|---------|------------------|---------------|
| **N+1 Queries** | Loop with database call inside | Grep: `for.*:.*\.query\(|\.find\(` |
| **Missing Index** | Query on unindexed field | Check query fields against schema indexes |
| **Memory Bloat** | Loading large datasets entirely | Grep: `\.all\(\)|\.toArray\(\)|collect\(\)` |
| **Unbounded Growth** | Collections that grow without limit | Grep: `\.append\(|\.push\(` without cleanup |
| **Blocking I/O** | Sync I/O in async context | Grep: `open\(` without async in async function |

**Maintainability Patterns (Usually NIT or CONCERN)**:
| Pattern | What to look for | How to detect |
|---------|------------------|---------------|
| **Long Methods** | Functions > 50 lines | Count lines per function |
| **Deep Nesting** | Indentation > 4 levels | Count indentation depth |
| **God Objects** | Classes with > 10 public methods | Grep: `def ` count per class |
| **Circular Dependencies** | A imports B, B imports A | Trace import chains |
| **Magic Numbers** | Unexplained numeric literals | Grep: `[^0-9][0-9]{2,}[^0-9]` without const |
| **Commented Code** | Large blocks of commented code | Grep: `#.*def |//.*function` |
| **TODO in Critical Path** | TODOs in security/auth code | Grep: `TODO|FIXME` in sensitive files |

**Concurrency Patterns (Often BLOCKING)**:
| Pattern | What to look for | How to detect |
|---------|------------------|---------------|
| **Deadlock Risk** | Multiple locks acquired in different orders | Trace lock acquisition order |
| **Data Race** | Shared mutable state without locks | Grep: shared variables + threads |
| **Lost Update** | Read-modify-write without atomicity | Grep: `x = x +|count +=` in concurrent code |
| **Starvation** | Unfair resource allocation | Check lock fairness, priority inversion |

**Output per file**:
```
FILE: [path]
------------
Purpose: [what this file change does]
Issues found:
- [Line N]: [issue] - [severity: BLOCKING/CONCERN/NIT]
- ...
Questions:
- [question about unclear code]
Positive notes:
- [good practices observed]
```

---

## Step 4: Review Tests

Evaluate the test coverage and quality.

**What to check**:
1. Tests exist for new functionality?
2. Main success path covered?
3. Edge cases and error conditions tested?
4. Tests are meaningful (not just coverage)?
5. Tests are maintainable?

**LLM Execution**:
```
# Find test files for changed code
→ Use Glob: pattern="**/test*" or "**/tests/**"

# Read test files
→ Use Read: [test_file_path]

# Check what's tested
→ Use Grep: pattern="def test_|it\(|describe\(" in test files

# Verify tests cover the changed functions
→ Use Grep: pattern="[changed_function_name]" in test files

# Run the tests
→ Use Bash: pytest [test_path] -v
  OR: npm test -- [test_path]
  OR: [appropriate test command]
```

**Output format**:
```
TESTS
=====
Test files: [list]
Coverage of changes: [GOOD / PARTIAL / MISSING]

Test gaps:
- [functionality not tested]
- [edge case not covered]

Test quality:
- Meaningful assertions: [YES/NO]
- Edge cases: [covered/missing which]
- Error cases: [covered/missing which]
```

---

## Step 5: Run Verification (Automated Checks)

Run automated checks to catch issues.

**What to run**:
1. Test suite
2. Linter/formatter
3. Type checker (if applicable)
4. Build (if applicable)

**LLM Execution**:
```
# Run test suite
→ Use Bash: pytest -v
  OR: npm test
  OR: [project-specific test command]

# Run linter
→ Use Bash: ruff check . (Python)
  OR: eslint . (JS)
  OR: [project-specific linter]

# Run type checker
→ Use Bash: mypy [path] (Python)
  OR: tsc --noEmit (TypeScript)

# Run formatter check
→ Use Bash: black --check . (Python)
  OR: prettier --check . (JS)
```

**Output format**:
```
AUTOMATED CHECKS
================
Tests: [PASS / FAIL - details]
Linter: [PASS / FAIL - details]
Types: [PASS / FAIL - details]
Build: [PASS / FAIL - details]
```

---

## Step 6: LLM Superpowers (Exhaustive Checks)

Leverage LLM capabilities humans can't easily do.

### 6.1: Codebase-Wide Pattern Search

```
# Find all usages of modified functions
→ Use Grep: pattern="[modified_function]\(" output_mode="content"

# Check: Do callers handle new behavior/errors correctly?

# Find similar code patterns
→ Use Grep: pattern="[similar_pattern]" to check consistency

# Check: Is the same bug/pattern present elsewhere?
```

### 6.2: Cross-Reference Verification

```
# For renamed functions, check for old name usage
→ Use Grep: pattern="[old_function_name]"

# For moved files, check import statements
→ Use Grep: pattern="from [old_path] import|import [old_module]"

# For changed APIs, check all callers
→ Use Grep: pattern="[api_function]\("
```

### 6.3: Consistency Checking

```
# Check naming conventions match project
→ Use Grep: pattern="def [pattern]|class [pattern]" to see existing conventions

# Check error handling patterns match
→ Use Grep: pattern="raise|except|try:" to see project patterns

# Check logging patterns match
→ Use Grep: pattern="logger\.|logging\." to see project patterns
```

### 6.4: Documentation Check

```
# Check if public APIs have docstrings
→ Use Grep: pattern='def [function_name]\([^)]*\):\s*"""' -A 5

# Check if README needs update
→ Use Read: README.md and compare to changes
```

**Output format**:
```
LLM EXHAUSTIVE CHECKS
=====================
All callers handled: [YES / NO - list affected]
Similar patterns checked: [findings]
Naming consistent: [YES / NO - inconsistencies]
Documentation: [adequate / needs update]
```

---

## Step 6.5: Severity Calibration

Before writing feedback, calibrate issue severity using these explicit criteria:

### BLOCKING Criteria (Must Fix Before Merge)
An issue is BLOCKING if ANY of these are true:
| Criterion | Test | Example |
|-----------|------|---------|
| **Security vulnerability** | Could this be exploited? | SQL injection, auth bypass, XSS |
| **Data loss risk** | Could this lose/corrupt user data? | Missing transaction, race on write |
| **Crash risk** | Could this crash in production? | Unhandled null, divide by zero |
| **Test failure** | Do tests fail with this change? | Broken test, assertion fails |
| **Breaking change** | Does this break existing callers? | Changed API without migration |
| **Compliance violation** | Does this violate legal/regulatory? | GDPR, HIPAA, PCI violations |

### CONCERN Criteria (Should Fix, May Defer)
An issue is CONCERN if ANY of these are true AND it's not BLOCKING:
| Criterion | Test | Example |
|-----------|------|---------|
| **Performance risk** | Could this cause slowdown in prod? | N+1 query, missing index |
| **Maintainability harm** | Will this make future changes harder? | Deep nesting, god object |
| **Error handling gap** | Could errors go unnoticed? | Swallowed exception |
| **Missing test** | Is important functionality untested? | New feature without test |
| **Unclear code** | Would another dev struggle to understand? | Complex logic, missing comments |

### NIT Criteria (Minor, Optional)
An issue is NIT if it's about:
| Area | Examples |
|------|----------|
| **Style** | Naming convention, formatting |
| **Preference** | This approach vs. that approach (both valid) |
| **Minor clarity** | Could be slightly clearer |
| **Optimization** | Slightly more efficient alternative |

### Calibration Examples

**BLOCKING examples**:
```
- Missing parameterized query → SQL injection → BLOCKING
- Auth check missing on admin endpoint → Auth bypass → BLOCKING
- NullPointerException possible on common path → Crash risk → BLOCKING
- Test fails on main assertion → Test failure → BLOCKING
```

**CONCERN examples**:
```
- Database call in loop → N+1 → CONCERN (perf in prod)
- Exception caught and logged but not re-raised → Error handling gap → CONCERN
- 100-line function → Maintainability → CONCERN
- New endpoint has no test → Missing test → CONCERN
```

**NIT examples**:
```
- Variable named 'x' could be 'userCount' → Style → NIT
- Could use list comprehension instead of loop → Preference → NIT
- Comment would help here → Minor clarity → NIT
```

---

## Step 7: Write Review Feedback

Compose clear, constructive review comments.

**Issue categories** (now calibrated by Step 6.5):
| Category | Symbol | Meaning | Calibrated By |
|----------|--------|---------|---------------|
| Blocking | [BLOCKING] | Must fix before merge | Step 6.5 BLOCKING criteria |
| Concern | [CONCERN] | Should address, might defer | Step 6.5 CONCERN criteria |
| Suggestion | [SUGGESTION] | Take it or leave it | Not in criteria, just ideas |
| Nit | [NIT] | Minor style/preference | Step 6.5 NIT criteria |
| Question | [QUESTION] | Need clarification | Uncertainty about code intent |
| Praise | [PRAISE] | Positive feedback | Good patterns observed |

**Comment structure**:
```
[CATEGORY] File:Line - Brief summary

What: [describe the issue]
Why: [explain why it matters]
Suggestion: [how to fix, if applicable]
```

**Output format**:
```
REVIEW COMMENTS
===============
[BLOCKING] src/auth.py:42 - SQL injection vulnerability
What: User input passed directly to query
Why: Security risk - allows arbitrary SQL execution
Suggestion: Use parameterized query: cursor.execute("SELECT * WHERE id = ?", (user_id,))

[CONCERN] src/api.py:105 - Missing error handling
What: API call can throw, not caught
Why: Will crash on network errors
Suggestion: Wrap in try/except with appropriate error response

[PRAISE] src/utils.py:20 - Good use of type hints
What: Clear typing improves maintainability

... [more comments]
```

---

## Step 8: Submit Review Decision

Determine and submit the overall review outcome.

**Decision criteria**:
| Condition | Decision |
|-----------|----------|
| Any BLOCKING issues | Request Changes |
| Only CONCERN/SUGGESTION/NIT | Approve (with comments) |
| Only questions | Comment (request discussion) |
| Clean | Approve |

**Output format**:
```
REVIEW DECISION
===============
Decision: [APPROVE / REQUEST CHANGES / COMMENT]

Summary:
- Blocking issues: [count]
- Concerns: [count]
- Suggestions: [count]
- Questions: [count]

Overall assessment: [1-2 sentence summary]

Next steps: [what author should do]
```

---

## When to Use

- Pull request submitted and ready for review
- Code changes need verification before merge
- Pre-merge quality check required
- Knowledge sharing through code examination
- Onboarding developers to unfamiliar code
- Security-sensitive changes need scrutiny
- Architectural changes need validation

---

## Verification Criteria

| Step | Verification |
|------|--------------|
| Step 1 | Context understood (purpose, scope, risk) |
| Step 2 | Architecture assessed |
| Step 3 | All files reviewed with issues categorized |
| Step 4 | Test coverage assessed |
| Step 5 | Automated checks run |
| Step 6 | Exhaustive LLM checks completed |
| Step 7 | Comments written with categories |
| Step 8 | Decision made with rationale |

**Overall verification**:
- [ ] All changed files reviewed
- [ ] Correctness verified for main paths
- [ ] Security implications considered
- [ ] Test coverage assessed
- [ ] Feedback is specific and actionable
- [ ] Blocking issues clearly identified
- [ ] Decision is clear and appropriate

---

## Integration Points

- **Often invoked from**: /procedure_engine (code review request), User request to review PR
- **Routes to**: /debugging (if bug found), /refactoring (if structural issues), /testing_strategy (if test gaps)
- **Related**: /debugging, /refactoring, /architecture_design
