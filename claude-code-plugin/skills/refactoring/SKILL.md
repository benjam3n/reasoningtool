---
name: refactoring
description: "Procedure for systematically improving code structure without changing behavior"
---

# Refactoring

## Overview
Procedure for systematically improving code structure without changing behavior

## Principles
### Behavior Preservation
{'description': 'Refactoring MUST NOT change what the code does.\nOnly how it does it.\n', 'verification': ['All existing tests still pass', 'All known use cases still work', 'No new bugs introduced']}

### Incremental Changes
{'description': 'Make small changes, one at a time.\nVerify each change before the next.\n', 'benefits': ['Easier to find problems', 'Can stop at any point', 'Reviewable changes']}

### Test Safety Net
{'description': "Tests must exist before refactoring.\nIf they don't, write them first.\n", 'rule': 'Never refactor without tests covering the behavior'}

## Steps

### Step 1: Assess current state
Understand what needs refactoring and why:
1. Identify code smells and problems
2. Understand current behavior
3. Map dependencies and usage
4. Assess test coverage
5. Identify constraints and risks
6. Define clear success criteria

### Step 2: Ensure test coverage
Make sure you have a safety net before refactoring:
1. Review existing tests for the code
2. Identify coverage gaps
3. Write characterization tests for untested behavior
4. Verify tests pass before any changes
5. Consider adding higher-level tests for safety

### Step 3: Plan refactoring approach
Design a safe path to the goal:
1. Break refactoring into small steps
2. Order steps to maintain working state
3. Identify points where you can stop
4. Plan verification between steps
5. Consider parallel change pattern for risky changes
6. Set scope boundary (avoid scope creep)

### Step 4: Execute refactoring
Perform the refactoring incrementally:
1. Make one small change
2. Run tests immediately
3. Commit if tests pass
4. Repeat for next change
5. Stop if tests fail, fix before continuing
6. Take breaks and review progress

### Step 5: Verify behavior preservation
Confirm refactoring didn't change behavior:
1. Run full test suite
2. Review changes for behavior modifications
3. Test manually in key scenarios
4. Check edge cases
5. Verify performance is acceptable
6. Review with another developer

### Step 6: Clean up and document
Finalize the refactoring:
1. Remove any dead code created
2. Update documentation if needed
3. Remove temporary scaffolding
4. Ensure consistent style
5. Write commit messages explaining changes
6. Update team on changes made

### Step 7: Review and learn
Extract lessons from the refactoring:
1. Was the goal achieved?
2. What remaining debt exists?
3. What would we do differently?
4. Should similar code be refactored?
5. Are there process improvements?
6. Document lessons learned


## When to Use
- Code is difficult to understand or modify
- Adding features requires touching many files
- Bugs keep appearing in the same areas
- Code duplication is causing maintenance burden
- Performance optimization needs cleaner structure
- Preparing code for new functionality
- Technical debt is impacting velocity
- Onboarding developers is taking too long

## Verification
- All tests pass after refactoring
- Code behavior is unchanged
- Refactoring goal is achieved
- Code is cleaner/more maintainable
- Changes are reviewed and approved
- Documentation is updated
- Team understands the changes

---

**Input**: $ARGUMENTS

Apply this procedure to the input provided.