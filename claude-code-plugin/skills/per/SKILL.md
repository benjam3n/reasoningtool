---
name: "per - Persuasion Design"
description: "Design a persuasive argument or communication. Structures the argument, anticipates objections, and checks for ethical soundness."
output:
  format: "prose"
---

# Persuasion Design

**Input**: $ARGUMENTS

---

## Step 1: Identify the Audience and Their Current Position

Before designing persuasion, understand who you're persuading and where they stand.

1. **Who is the audience?** (specific person, group, archetype)
2. **What do they currently believe** about this topic?
3. **How strongly do they hold** that belief? (casual opinion / considered position / core identity)
4. **What do they care about?** (values, priorities, fears, desires)
5. **What is their relationship to you?** (trust level, authority dynamic)
6. **What has been tried before?** (previous arguments that failed or succeeded)

```
AUDIENCE: [who]
CURRENT POSITION: [what they believe now]
BELIEF STRENGTH: [casual / considered / identity-level]
KEY VALUES: [what they care about most]
TRUST LEVEL: [high / moderate / low / adversarial]
```

IMPORTANT: If belief strength is "identity-level," direct argumentation will likely backfire. Shift strategy to indirect approaches (shared goals, narrative, identity-compatible reframing).

---

## Step 2: Define the Desired Shift

Specify exactly what change you want.

1. What should they believe, feel, or do after your communication?
2. How far is this from their current position?
3. Is a full shift realistic, or should you aim for a partial shift?

```
DESIRED OUTCOME: [specific belief/action change]
SHIFT DISTANCE: [small / moderate / large]
REALISTIC TARGET: [what you can actually achieve in one communication]
```

Rule of thumb: Large shifts rarely happen in one interaction. If the distance is large, design for incremental movement — move them one step, not the whole way.

---

## Step 3: Choose Persuasion Approach

Select primary and secondary approaches based on audience analysis:

| Approach | Best When | Mechanism |
|---|---|---|
| **Logical argument** | Audience values rationality, low emotion | Evidence, reasoning, proof |
| **Emotional appeal** | Decision is personal, stakes feel abstract | Story, vivid imagery, felt consequences |
| **Credibility/authority** | Audience trusts expertise, you have credentials | Expert testimony, track record, social proof |
| **Social proof** | Audience is uncertain, peers matter | Others have done this, consensus, trends |
| **Reciprocity** | You can offer something first | Give before asking |
| **Narrative** | Audience resists direct argument | Story that leads to the conclusion naturally |

```
PRIMARY APPROACH: [approach] — because [reasoning]
SECONDARY APPROACH: [approach] — because [reasoning]
```

---

## Step 4: Structure the Argument

Build the communication using the chosen approach:

1. **Opening**: Meet them where they are. Acknowledge their current position with genuine respect. Never strawman.
2. **Bridge**: Connect their values/concerns to your position. The bridge answers: "Given what YOU care about, here's why this matters."
3. **Core argument**: Present your strongest 2-3 points. More points dilute impact.
4. **Evidence**: Support each point with the type of evidence the audience finds credible (data for analysts, stories for empathizers, examples for pragmatists).
5. **Call to action**: Specific, achievable next step. Not "change your mind" but "try X" or "consider Y."

```
STRUCTURE:
1. OPEN: [how you meet them where they are]
2. BRIDGE: [how you connect their values to your position]
3. POINT 1: [argument] + [evidence]
4. POINT 2: [argument] + [evidence]
5. POINT 3: [argument] + [evidence] (if needed)
6. ACTION: [specific ask]
```

---

## Step 5: Anticipate and Address Objections

For each likely objection:

1. State the objection in the STRONGEST form the audience would use (steelman it)
2. Acknowledge its validity where honest
3. Provide your response
4. Decide: address proactively in the argument, or hold in reserve?

```
OBJECTIONS:
1. "[objection]" — Response: [response] — Handle: [proactive / reserve]
2. "[objection]" — Response: [response] — Handle: [proactive / reserve]
...
```

Proactively address objections that most of the audience will think of. Hold in reserve those that only some will raise.

---

## Step 6: Ethical Soundness Check

Before delivering, verify ethical integrity:

| Check | Pass? |
|---|---|
| Is the core claim true to the best of your knowledge? | [yes/no] |
| Are you presenting evidence honestly (no cherry-picking)? | [yes/no] |
| Would you be comfortable if the audience saw your full reasoning? | [yes/no] |
| Are you respecting the audience's autonomy to disagree? | [yes/no] |
| Is the desired outcome genuinely good for the audience (not just you)? | [yes/no] |
| Are you using emotional appeal to illuminate truth, not to obscure it? | [yes/no] |

If ANY check fails: revise the argument. Persuasion that relies on deception or manipulation is not persuasion — it is coercion. The goal is to help someone see something true, not to trick them into compliance.

```
ETHICS: [PASS / FAIL — if fail, what needs revision]
```

### Persuasion Failure Check

| Failure | Test | Fix |
|---------|------|-----|
| **Cached takes** | Is any argument the default position on this topic — something said in 10,000 other pitches? | Find the argument that's true of THIS specific situation, not the category. |
| **Relativistic hedging** | Does the argument say "some argue X, others Y, truth is somewhere in between"? | That's not persuasion. Take a position. If you're hedging, you haven't found your actual argument yet. |
| **Pre-baked thesis** | Would someone who had never read commentary on this topic reach the same conclusion from the evidence alone? If not, you're recycling consensus, not persuading. | Rebuild the argument from THIS evidence, not from the standard position. |
| **Aspiration as conclusion** | Does the closing say "the future holds great promise" or equivalent? | Delete the last paragraph. If the piece is better without it, the conclusion was filler. End on your strongest concrete point. |

---

## Integration

Use with:
- `/sp` -> Sharpen the persuasive prompt before designing the argument
- `/pw` -> Draft the actual communication after designing the argument
- `/pinf` -> Analyze influence dynamics before attempting persuasion
- `/aex` -> Check your own assumptions about the audience
