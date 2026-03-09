---
name: "injc - Injectable Skill Design"
description: Guides the design of skills that can be inserted into other skills as steps — working as both standalone tools and embedded gates/checks within host skills.
---

# Injectable Skill Design

**Input**: $ARGUMENTS

---

## Step 1: Define the Injection Purpose

An injectable skill is a small, focused check or transform that can be dropped into any host skill.

```
SKILL NAME: [abbreviation]
INJECTION ROLE: [gate / check / transform / enrichment]
STANDALONE USE: [what it does when used alone]
INJECTED USE: [what it does when embedded in another skill]
```

| Role | What it does | Example |
|------|-------------|---------|
| **Gate** | Blocks progress if a condition fails | "Are assumptions stated?" |
| **Check** | Adds a verification without blocking | "Flag any logical gaps" |
| **Transform** | Converts one format to another | "Turn list into ranked list" |
| **Enrichment** | Adds information to existing output | "Add confidence levels" |

---

## Step 2: Design Minimal Output

Injectable output must be compact — it gets inserted into another skill's flow.

```
STANDALONE OUTPUT FORMAT:
[Full output with explanation — what the user sees when using directly]

INJECTION OUTPUT FORMAT:
[Minimal output — 1-5 lines that integrate into the host skill's flow]
```

Rule: Injection output should never exceed 5 lines. If it does, it's not injectable — it's a full skill.

---

## Step 3: Design the Gate/Check Logic

Define what the injectable skill evaluates.

```
EVALUATES: [what it looks at]
CRITERIA:
1. [criterion 1]: [pass/fail condition]
2. [criterion 2]: [pass/fail condition]
3. [criterion 3]: [pass/fail condition]

ON PASS: [what happens — usually "proceed"]
ON FAIL: [what happens — flag, block, or redirect]
```

SKIP: If the skill is a transform or enrichment (not a gate/check), skip this step.

---

## Step 4: Design Dual-Mode Behavior

The skill must detect whether it's standalone or injected.

```
MODE DETECTION:
- Standalone: User invokes directly with /[name] [input]
  → Run full analysis, produce complete output
- Injected: Host skill calls → INVOKE: /[name] [intermediate data]
  → Run focused check, produce minimal output

STANDALONE BEHAVIOR:
1. [Full step 1]
2. [Full step 2]
3. [Full step 3]
→ Output: [complete result]

INJECTED BEHAVIOR:
1. [Focused evaluation]
→ Output: [pass/fail + one-line reason]
```

---

## Step 5: Test Inside Host Skills

Verify the skill works inside at least three different host skills.

```
HOST TEST 1:
- Host skill: [name]
- Injection point: [which step]
- Input from host: [what data the host passes]
- Injection output: [what the injectable returns]
- Host continues: [yes/no — does the flow work?]

HOST TEST 2:
- Host skill: [name]
- Injection point: [which step]
- Input from host: [what data the host passes]
- Injection output: [what the injectable returns]
- Host continues: [yes/no]

HOST TEST 3:
- Host skill: [name]
- Injection point: [which step]
- Input from host: [what data the host passes]
- Injection output: [what the injectable returns]
- Host continues: [yes/no]
```

If any test fails, simplify the injection output.

---

## Step 6: Write the Skill File

Produce the complete SKILL.md with dual-mode support.

```
SKILL FILE:

---
name: "[abbreviation] - [Full Name]"
description: [description noting both standalone and injectable use]
---

# [Full Name]

**Input**: $ARGUMENTS

[Steps for standalone mode]

**Injection mode**: When invoked by another skill, output only:
[minimal format specification]

## Integration

Use with:
- [host skill 1] -> Inject at [step]
- [host skill 2] -> Inject at [step]
```

---

## Integration

Use with:
- `/stnl` -> Ensure the injectable also works as a standalone skill
- `/chns` -> Design chain-compatible contracts around the injectable
- `/orcs` -> Orchestrators often use injectables as routing checks
