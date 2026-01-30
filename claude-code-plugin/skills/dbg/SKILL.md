---
name: "dbg - Debugging"
description: "Systematic procedure for diagnosing and fixing software bugs using Claude Code's tool capabilities"
context: fork
---

# Debugging

**Input**: $ARGUMENTS

---

## Overview

Systematic procedure for diagnosing and fixing software bugs. This procedure leverages Claude Code's unique capabilities: exhaustive code search, pattern matching across codebase, and direct code execution.

---

## Step 0: Context Assessment

| Factor | Value | Notes |
|--------|-------|-------|
| Urgency | CRITICAL / HIGH / NORMAL | Production down vs development issue |
| Reproducibility | CONSISTENT / INTERMITTENT / RARE | Affects isolation strategy |
| Codebase familiarity | HIGH / LOW | Affects search vs read approach |

**If CRITICAL + CONSISTENT**: Skip to Step 3 (isolate quickly)
**If INTERMITTENT**: Extra logging in Step 2

---

## Step 1: Gather Bug Information

Collect all available information about the bug.

**What to gather**:
1. Error messages and stack traces (exact text)
2. Expected vs actual behavior
3. Environment details (versions, configs)
4. When the bug started (recent changes?)
5. Conditions that trigger the bug

**LLM Execution**:
```
# Read error logs if path known
→ Use Read tool on log files

# Search for error message in codebase
→ Use Grep: pattern="[error message text]"

# Check recent commits for relevant changes
→ Use Bash: git log --oneline -20 -- [relevant_path]

# Find configuration files
→ Use Glob: pattern="**/config*.{json,yaml,yml,toml}"
```

**Output format**:
```
BUG SUMMARY
===========
Error: [exact error message]
Expected: [what should happen]
Actual: [what happens instead]
Environment: [relevant versions/config]
First occurrence: [when/what changed]
Trigger conditions: [how to cause bug]
```

---

## Step 2: Reproduce the Bug

Achieve consistent reproduction of the bug.

**Strategy**:
1. Start with exact reproduction steps from report
2. Simplify to minimal reproduction case
3. Document what IS and ISN'T required to trigger

**LLM Execution**:
```
# Run the failing test/command
→ Use Bash: [command that triggers bug]

# If no command provided, search for tests
→ Use Grep: pattern="test.*[function_name]" type="py" (or relevant type)

# Run specific test
→ Use Bash: pytest [test_path] -v

# If intermittent, add logging
→ Use Edit: Add print/log statements at suspected points
→ Use Bash: Run multiple times, collect logs
```

**Output format**:
```
REPRODUCTION
============
Command: [exact command]
Expected output: [what should appear]
Actual output: [what actually appears]
Reproducible: [YES consistently / YES intermittently / NO]
Minimal case: [simplest trigger]
```

**If cannot reproduce**:
- Request additional environment details from user
- Add logging and ask user to trigger again
- Document as "reproduction blocked" and note what's needed

---

## Step 3: Isolate the Bug Location

Narrow down where the bug occurs.

**Strategies** (use in order of efficiency):
1. **Stack trace analysis**: If stack trace exists, start there
2. **Error message search**: Find where error is raised
3. **Binary search**: Comment out half the code path
4. **Git bisect**: Find introducing commit
5. **Input/output tracing**: Check values at boundaries

**LLM Execution**:
```
# Search for error message origin
→ Use Grep: pattern="[error text or exception type]" output_mode="content"

# Find function definition from stack trace
→ Use Grep: pattern="def [function_name]" output_mode="content"

# Read the suspected file
→ Use Read: [file_path]

# Check git history for suspicious changes
→ Use Bash: git log -p --follow -S "[suspicious_string]" -- [file_path]

# Binary search via commenting (if needed)
→ Use Edit: Comment out suspected section
→ Use Bash: Run test
→ Observe if error persists
→ Use Edit: Restore or narrow down
```

**LLM Alternative to Interactive Debugger**:
Instead of breakpoints, use strategic print statements:
```
# Add diagnostic print statement
→ Use Edit: Add print(f"DEBUG: {variable}={variable!r}") at suspected points

# Run and capture output
→ Use Bash: [command] 2>&1

# Read output
→ Analyze printed values

# Remove debug statements after fix
→ Use Edit: Remove DEBUG prints
```

**Output format**:
```
ISOLATION
=========
Bug location: [file:line]
Function: [function_name]
Confidence: [HIGH/MED/LOW]
Evidence: [what indicates this location]
```

---

## Step 4: Analyze Root Cause

Understand WHY the bug occurs, not just where.

**Analysis approach**:
1. Read code at bug location carefully
2. Trace data flow into the location
3. Apply Five Whys technique
4. Categorize the bug type
5. Check assumptions the code makes

**Bug type categories**:
| Type | Examples |
|------|----------|
| Logic error | Wrong condition, off-by-one, wrong operator |
| State error | Race condition, stale state, mutation side effect |
| Type error | Wrong type, null/undefined, type coercion |
| Boundary error | Edge case, empty input, large input |
| Integration error | API mismatch, version incompatibility |
| Environment error | Missing config, wrong path, permissions |

**LLM Execution**:
```
# Read code at identified location
→ Use Read: [file_path]

# Trace where inputs come from
→ Use Grep: pattern="[variable_name]\s*=" to find assignments

# Check related code for patterns
→ Use Grep: pattern="[similar_pattern]" to find analogous code

# Review data structures
→ Use Grep: pattern="class [ClassName]|def [function]" to understand types
```

**Output format**:
```
ROOT CAUSE ANALYSIS
===================
Root cause: [specific cause]
Bug type: [from categories above]
Why it causes the error: [explanation]
Why it wasn't caught: [testing gap, edge case, etc.]
```

---

## Step 5: Design the Fix

Plan the fix before implementing.

**Design considerations**:
1. Simplest fix that addresses root cause
2. Side effects on other code
3. Regression risk
4. Test requirements

**Fix approach options**:
| Approach | When to use |
|----------|-------------|
| Direct fix | Clear bug, isolated location |
| Defensive fix | Add validation/guards |
| Refactor fix | Bug reveals design problem |
| Workaround | Quick fix now, proper fix later |

**LLM Execution**:
```
# Check for similar patterns that might have same bug
→ Use Grep: pattern="[buggy_pattern]" to find similar code

# Understand dependencies of code being modified
→ Use Grep: pattern="import.*[module]|from [module]" to find usages

# Check test coverage for area
→ Use Grep: pattern="test.*[function_name]" type="py"
```

**Output format**:
```
FIX DESIGN
==========
Approach: [direct/defensive/refactor/workaround]
Change summary: [what will change]
Files affected: [list]
Potential side effects: [list or "none identified"]
Test plan: [how to verify fix]
```

---

## Step 6: Implement and Test the Fix

Apply the fix and verify it works.

**Implementation checklist**:
1. Make minimal code change
2. Follow existing code style
3. Add explanatory comments if fix is non-obvious
4. Write test that would have caught the bug
5. Verify original bug is fixed
6. Run existing tests for regressions

**LLM Execution**:
```
# Apply the fix
→ Use Edit: [specific change]

# Run the previously failing test
→ Use Bash: [test command]
→ Verify: Previously failing now passes

# Run broader test suite
→ Use Bash: pytest [test_directory] or equivalent
→ Verify: No regressions

# If test doesn't exist, create one
→ Use Edit: Add test in appropriate test file

# Run new test
→ Use Bash: [test command for new test]
```

**Output format**:
```
FIX IMPLEMENTATION
==================
Change made: [description]
File(s) modified: [list]

Test results:
- Original bug: [FIXED/STILL PRESENT]
- Regression tests: [PASS/FAIL with details]
- New test added: [YES/NO, test name if yes]
```

---

## Step 7: Document and Prevent

Complete the debugging cycle.

**Documentation**:
1. Clear commit message explaining fix
2. Update relevant docs if behavior changed
3. Note any related code that might need checking
4. Recommend process improvements

**LLM Execution**:
```
# Prepare commit message
# Format: "[type]: Brief summary\n\nRoot cause: ...\nFix: ..."

# Check for similar code that might have same issue
→ Use Grep: pattern="[original_buggy_pattern]"
→ Report: Other locations that may need review
```

**Output format**:
```
DOCUMENTATION
=============
Commit message: [suggested message]
Related code to check: [list or "none"]
Process improvement: [suggestion or "none"]
```

---

## When to Use

- Bug report received from users or QA
- Unexpected system behavior observed
- Test failures that need investigation
- Production incidents requiring diagnosis
- Code behaving differently than expected
- Performance degradation (with adaptation)
- Intermittent failures need root cause

---

## Verification Criteria

| Step | Verification |
|------|--------------|
| Step 1 | Bug info complete (error, expected, actual, conditions) |
| Step 2 | Bug reproducible OR documented as blocked |
| Step 3 | Location isolated to specific file:line |
| Step 4 | Root cause identified with category |
| Step 5 | Fix designed with test plan |
| Step 6 | Tests pass (original fixed, no regressions) |
| Step 7 | Commit message prepared |

**Overall verification**:
- [ ] Bug is reproducible before fix
- [ ] Bug is not reproducible after fix
- [ ] Root cause is clearly documented
- [ ] Fix addresses root cause (not symptoms)
- [ ] Regression test exists for this bug
- [ ] All existing tests pass
- [ ] Similar code checked for same issue

---

## Integration Points

- **Often invoked from**: /pce (problem input), /cor (bug discovered during review)
- **Routes to**: /cor (fix ready for review), /ts (if test gaps identified)
- **Related**: /rc5w, /rca

---

## LLM Debugging Superpowers

Unlike human debuggers, LLM can leverage unique capabilities:

### Exhaustive Codebase Search
```
LLM can:
- Search entire codebase for error message origin instantly
  → Use Grep: pattern="[exact_error_text]"
- Find ALL usages of a function/variable
  → Use Grep: pattern="[function_name]\("
- Trace ALL import chains
  → Use Grep: pattern="from.*[module]|import [module]"
- Find similar patterns that might have same bug
  → Use Grep: pattern="[buggy_pattern]"
```

### Parallel Investigation
```
LLM can:
- Read multiple suspicious files simultaneously
  → Use Read on all candidate files in parallel
- Run multiple test subsets to isolate
  → Use Bash: pytest [file1] && Use Bash: pytest [file2]
- Check multiple hypotheses at once
  → Add debug prints at multiple locations
```

### Pattern Matching at Scale
```
LLM can:
- Recognize bug patterns from training (millions of bugs seen)
- Cross-reference against known anti-patterns
- Suggest fixes based on similar historical bugs
```

### What LLM Cannot Do (Plan Around These)
| Limitation | Workaround |
|------------|------------|
| Interactive debugger (breakpoints) | Use print statements via Edit + Bash |
| Watch memory in real-time | Add memory logging, read logs |
| Profile performance interactively | Add timing code, run profiler via Bash |
| Step through execution | Strategic prints at each step |

---

## Common Debugging Patterns (LLM Reference)

### Logic Errors
| Pattern | Symptoms | Likely Cause | First Check | LLM Detection |
|---------|----------|--------------|-------------|---------------|
| Off-by-one | Works for most cases, fails at boundaries | Loop bounds, array indexing | `<` vs `<=`, array length | Grep: `range\(.*-1|range\(.*len\(` |
| Wrong operator | Incorrect results, no crash | `=` vs `==`, `and` vs `or` | Conditionals near bug | Grep: `if.*=.*:` (assignment in if) |
| Incorrect order | Partial success, some operations fail | Initialization order, dependencies | Trace execution order | Read code flow |
| Missing case | Works except for edge cases | Incomplete switch/if logic | Enumerate all cases | Count case handling |

### State Errors
| Pattern | Symptoms | Likely Cause | First Check | LLM Detection |
|---------|----------|--------------|-------------|---------------|
| Null/None | TypeError, AttributeError | Missing initialization, failed lookup | Where value is assigned | Grep: `= None|is None` |
| Stale state | Works once, fails on repeat | Mutation, caching | State initialization | Grep: `cache|global|@lru_cache` |
| Race condition | Intermittent, timing-dependent | Shared state, async operations | Concurrent access points | Grep: `async|await|Thread|Lock` |
| Unintended mutation | Correct then wrong | In-place modification | Trace object identity | Grep: `.append\(|.update\(|.pop\(` |

### Type Errors
| Pattern | Symptoms | Likely Cause | First Check | LLM Detection |
|---------|----------|--------------|-------------|---------------|
| Type coercion | Unexpected values, silent failures | Dynamic typing, implicit conversion | Type at assignment | Grep: `int\(|str\(|float\(` |
| Wrong type | TypeError, AttributeError | Expected X got Y | Trace input types | Add: `print(type(x))` |
| Serialization | Data loss, corruption | Object not serializable | Check serialization boundary | Grep: `json.dumps|pickle|serialize` |

### Async/Concurrency Errors
| Pattern | Symptoms | Likely Cause | First Check | LLM Detection |
|---------|----------|--------------|-------------|---------------|
| Forgotten await | Function returns coroutine, not result | Missing await | Check all async calls | Grep: `async def` without matching await |
| Deadlock | Hangs forever | Circular lock dependency | Trace lock acquisition | Grep: `acquire\(|Lock\(` |
| Lost exception | Silent failure in async | Exception in task not awaited | Check task handling | Grep: `create_task|ensure_future` |

### Environment Errors
| Pattern | Symptoms | Likely Cause | First Check | LLM Detection |
|---------|----------|--------------|-------------|---------------|
| Missing config | Works locally, fails deployed | Environment variable unset | Check all env vars | Grep: `os.environ|getenv` |
| Path issues | File not found, import fails | Wrong working directory | Print cwd and paths | Bash: `pwd; ls` |
| Version mismatch | Works in dev, fails in prod | Dependency version differs | Check requirements | Bash: `pip freeze | grep [package]` |
| Permission error | Access denied | File/network permissions | Check actual permissions | Bash: `ls -la [path]` |

### Integration Errors
| Pattern | Symptoms | Likely Cause | First Check | LLM Detection |
|---------|----------|--------------|-------------|---------------|
| API mismatch | Wrong data format, 400 errors | API changed, spec wrong | Check actual vs expected | Read API response |
| Timeout | Slow then fails | Network, slow dependency | Add timing | Bash: `time [command]` |
| Retry exhausted | Works sometimes | Transient failures | Check retry logic | Grep: `retry|attempt|backoff` |
