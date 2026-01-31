---
name: saadag
description: "Run the detector suite against a target artifact to find ambiguity, proxy substitution, bundled checks, and more."
---

# Apply Detectors + Generators

**Input**: $ARGUMENTS

---

## Overview

Run the detector suite against a target artifact to find ambiguity, proxy substitution, bundled checks, undefined terms, false dichotomies, and hidden conditionals. This is the automated quality scan for procedure/gate text.

## Steps

### Step 1: Ambiguity Detection
Scan for lines where reasonable people would disagree on meaning:

| Pattern | Example | Problem |
|---------|---------|---------|
| Vague quantifiers | "Several", "many", "few" | Different people assign different numbers |
| Undefined adjectives | "Good", "adequate", "appropriate" | No shared standard |
| Pronoun ambiguity | "It should be validated" | What is "it"? |
| Scope ambiguity | "All requirements" | All of WHICH requirements? |
| Temporal ambiguity | "Before proceeding" | Before which step? |

For each found: record the line, the ambiguous element, and suggest a specific rewrite.

### Step 2: Proxy Detection
Scan for places where formatting or process is substituted for content:

| Proxy Pattern | Example | Real Check Needed |
|--------------|---------|-------------------|
| "Document exists" → treated as "content is correct" | "Is there a risk assessment?" | "Does the risk assessment identify the top 3 risks?" |
| "Was reviewed" → treated as "is good" | "Has the plan been reviewed?" | "Did the reviewer find issues? Were they addressed?" |
| "Checklist complete" → treated as "work is done" | "All items checked off" | "Does each checked item have evidence?" |
| "Template followed" → treated as "quality met" | "Used standard template" | "Does the filled template contain substantive content?" |

For each found: record the proxy and propose a content-based check.

### Step 3: Bundled Check Detection
Scan for questions/criteria that combine multiple independent checks:

**Signal words:** "and", "or", "as well as", semicolons, parenthetical additions

**Before:** "Is the goal clear, measurable, and achievable with current resources?"
**After:**
1. "Is the goal clear?" (Can it be stated in one sentence?)
2. "Is the goal measurable?" (What metric and target?)
3. "Is the goal achievable with current resources?" (What resources are needed vs available?)

### Step 4: Undefined Term Detection
Scan for recurring nouns/adjectives used as if their meaning is shared but never defined:

1. Extract all nouns/adjectives used in evaluative positions
2. Flag those that appear 3+ times without definition
3. For each: is the meaning obvious? Would two executors agree on what it means?
4. If not: propose a definition or replace with specific criteria

### Step 5: False Dichotomy Detection
Scan for binary framings that may have more options:

| Pattern | Example | Question to Ask |
|---------|---------|----------------|
| "Is X or Y?" | "Is this a bug or a feature?" | Could it be both? Neither? Something else? |
| "Pass/fail" without gradient | "Does it meet the standard?" | What about partial? Near-miss? Conditional? |
| Yes/no on continuous dimension | "Is the plan complete?" | What % complete? What's missing? |

### Step 6: Hidden Conditional Detection
Scan for criteria that silently assume conditions:

| Pattern | Example | Hidden Condition |
|---------|---------|-----------------|
| "if applicable" | "Address security concerns (if applicable)" | Who decides if applicable? |
| Unstated prerequisites | "Verify test results" | Assumes tests were run |
| Context-dependent | "Use appropriate method" | Depends on context not specified |

### Step 7: Report
```
DETECTOR SUITE RESULTS:
Target: [what was scanned]
Lines scanned: [N]

| Detector | Findings | Severity | Top Priority Fix |
|----------|----------|----------|-----------------|
| Ambiguity | [N] | [H/M/L] | [worst case] |
| Proxy | [N] | [H/M/L] | [worst case] |
| Bundled | [N] | [H/M/L] | [worst case] |
| Undefined | [N] | [H/M/L] | [worst case] |
| False dichotomy | [N] | [H/M/L] | [worst case] |
| Hidden conditional | [N] | [H/M/L] | [worst case] |

Total findings: [N]
Rewrite queue: [ordered list of fixes by priority]
```

## When to Use
- Before refactoring a gate/procedure
- When text feels "rigorous" but is not checkable
- When you want better questions instead of faster answers
- → INVOKE: /saqrc (question rewrite chains) for fixing found issues
- → INVOKE: /sapea (executability audit) for checking if fixes work

## Verification
- [ ] All 6 detectors applied
- [ ] Each finding has specific location and proposed fix
- [ ] Findings prioritized by severity
- [ ] Rewrite queue created for implementation
- [ ] Proxy substitutions identified (most insidious issue)
