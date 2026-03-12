---
name: "curd - Curriculum Design"
description: "Design a structured learning path for any subject. Sequences topics by dependency, selects methods, sets milestones, and estimates time."
output:
  format: "prose"
---

# Curriculum Design

**Input**: $ARGUMENTS

---

## Step 1: Define the Learning Goal

Specify what the learner should be able to DO after completing the curriculum.

1. Write the goal as a concrete capability, not a vague aspiration
   - Bad: "Understand machine learning"
   - Good: "Build, train, and evaluate a supervised ML model on a real dataset"
2. Identify the goal level using Bloom's taxonomy:
   - **Remember**: Recall facts
   - **Understand**: Explain concepts
   - **Apply**: Use in new situations
   - **Analyze**: Break down and examine
   - **Evaluate**: Judge and critique
   - **Create**: Produce original work
3. Define "done" — what artifact or demonstration proves mastery?

```
LEARNING GOAL: [concrete capability statement]
BLOOM LEVEL: [remember / understand / apply / analyze / evaluate / create]
PROOF OF MASTERY: [what the learner produces to prove they're done]
```

---

## Step 2: Assess Starting Knowledge

Determine where the learner is now.

1. What does the learner already know in this domain?
2. What adjacent skills do they have?
3. What is their learning style preference (if known)?
4. How much time can they dedicate (hours/week)?
5. What is their motivation level and source?

```
STARTING POINT: [summary of current knowledge]
AVAILABLE TIME: [hours/week]
GAP SIZE: [rough estimate: small / medium / large]
```

---

## Step 3: Identify Prerequisite Knowledge

Map everything the learner needs to know BEFORE they can reach the goal.

1. List all prerequisite topics
2. For each, note whether the learner already has it
3. Flag any prerequisites that themselves have prerequisites (chains)
4. Identify the longest prerequisite chain — this is the critical path

```
PREREQUISITES:
- [topic] — Status: [known / partial / unknown]
- [topic] — Status: [known / partial / unknown]
...

CRITICAL PATH: [longest chain of unknown prerequisites]
```

---

## Step 4: Sequence Topics by Dependency

Order all topics (prerequisites + core + advanced) into a learning sequence.

Rules:
1. No topic appears before its prerequisites
2. Group related topics into modules/units
3. Interleave theory with practice — never more than 2 theory units without application
4. Place quick wins early to build momentum
5. Place the hardest material in the middle third (not at the start or end)

```
SEQUENCE:
Module 1: [name]
  1.1 [topic] — [estimated hours]
  1.2 [topic] — [estimated hours]
Module 2: [name]
  2.1 [topic] — [estimated hours]
  ...
```

---

## Step 5: Choose Learning Methods

For each topic, select the most effective method.

| Topic Type | Best Methods |
|---|---|
| **Factual knowledge** | Spaced repetition, flashcards, reading |
| **Conceptual understanding** | Explanation, analogy, discussion, teaching others |
| **Procedural skill** | Guided practice, worked examples, drills |
| **Problem-solving** | Projects, case studies, deliberate practice |
| **Creative skill** | Imitation, variation, original production, critique |

For each topic, specify:
- Primary method
- Recommended resources (types, not specific titles unless obvious)
- Estimated practice-to-theory ratio

---

## Step 6: Set Milestones and Assessments

Define checkpoints to verify progress.

1. Place a milestone every 10-20 hours of learning
2. Each milestone should be a concrete deliverable or demonstration
3. Include both formative checks (low stakes, frequent) and summative assessments (higher stakes, less frequent)

```
MILESTONES:
- After Module [X]: [what the learner can demonstrate]
- After Module [Y]: [what the learner can demonstrate]
...
FINAL ASSESSMENT: [the proof-of-mastery artifact from Step 1]
```

---

## Step 7: Estimate Total Time and Create Schedule

1. Sum all topic estimates from Step 4
2. Add 20% buffer for review, getting stuck, and life interruptions
3. Divide by available hours/week to get calendar duration
4. Identify the likely abandonment risk points and add motivational strategies

```
TOTAL ESTIMATED HOURS: [sum + 20% buffer]
CALENDAR DURATION: [weeks at stated pace]
HIGH-RISK DROPOUT POINTS: [where motivation typically drops]
MITIGATION: [strategies to maintain momentum]
```

---

## Integration

Use with:
- `/gu` -> Clarify the learning goal before designing the curriculum
- `/to` -> Break curriculum into actionable task list
- `/rwif` -> Bridge from learning plan to actual study schedule
- `/memk` -> Capture key insights during the learning process
