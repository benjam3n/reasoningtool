---
name: "thnk - Think"
description: Meta-skill for choosing the right thinking approach. Identifies what type of thinking is needed, selects the appropriate framework, applies it, and evaluates output quality.
---

# Think

**Input**: $ARGUMENTS

---

## Step 1: What Kind of Thinking Is Needed?

Read the input and classify the thinking required.

```
INPUT SUMMARY: [One sentence restating what the user needs]

THINKING TYPE NEEDED:
```

| Type | Signal | Match? |
|------|--------|--------|
| **Analytical** | Break something down, understand structure | [yes/no] |
| **Critical** | Test a claim, find flaws, validate | [yes/no] |
| **Creative** | Generate options, find novel solutions | [yes/no] |
| **Strategic** | Plan, prioritize, sequence actions | [yes/no] |
| **Empathetic** | Understand perspectives, feelings, motivations | [yes/no] |
| **Systemic** | Understand how parts interact, feedback loops | [yes/no] |
| **Evaluative** | Judge quality, compare, rank | [yes/no] |

```
PRIMARY THINKING TYPE: [the dominant one]
SECONDARY: [if applicable]
```

---

## Step 2: Select the Right Tool

Based on the thinking type, choose the best skill or framework.

```
FOR THIS THINKING TYPE, THE BEST APPROACH IS:

SKILL: [/skillname] — because [reason it fits]
ALTERNATIVE: [/skillname] — if [condition]
```

If no existing skill fits, define an ad-hoc approach:

```
AD-HOC APPROACH:
1. [Step 1]
2. [Step 2]
3. [Step 3]
```

---

## Step 3: Apply the Thinking

Execute the selected approach against the input.

If a skill was selected:
```
-> INVOKE: /[skillname] $ARGUMENTS
```

If using an ad-hoc approach, execute the steps defined above and show the work.

---

## Step 4: Evaluate Output Quality

After the thinking is complete, assess the result.

```
OUTPUT QUALITY CHECK:
- Does it answer what was actually asked? [yes/no]
- Is it at the right level of depth? [yes/no — too shallow / too deep / right]
- Are there obvious gaps? [list any]
- Would a different thinking type have worked better? [yes/no — which one]
```

---

## Step 5: Iterate If Needed

If the quality check reveals problems:

```
ITERATION NEEDED: [yes/no]
REASON: [what's wrong]
SWITCHING TO: [different approach or deeper pass]
```

If no iteration needed, present the output as the final answer.

---

## Integration

Use with:
- `/meta` -> Get oriented before thinking
- `/sp` -> Improve the question before thinking about it
- `/vldt` -> Validate the output of your thinking
- `/lrnk` -> If the thinking reveals a knowledge gap
