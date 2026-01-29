---
name: preference_elicitation
description: Elicit user preferences by presenting concrete trade-offs rather than asking open-ended questions. System does the work by generating options and letting user select.
---

# Preference Elicitation

**Input**: $ARGUMENTS (domain or guess category to elicit preferences for)

---

## Purpose

Discover what the user values by presenting concrete choices rather than asking them to articulate preferences directly.

**Principle**: People reveal preferences through choices better than through descriptions. Present trade-offs, observe selections.

---

## Step 1: Generate Trade-Off Pairs

For the domain/category, generate pairs of options that trade off against each other:

```
TRADE-OFF 1: [dimension being traded]
├── Option A: [high on X, low on Y]
└── Option B: [low on X, high on Y]

TRADE-OFF 2: [dimension being traded]
├── Option A: [high on X, low on Y]
└── Option B: [low on X, high on Y]
```

**Minimum**: Generate 10 trade-off pairs covering different preference dimensions.

---

## Step 2: Preference Dimensions to Cover

| Dimension | Trade-Off | Option A | Option B |
|-----------|-----------|----------|----------|
| Time vs Money | Spend time to save money OR spend money to save time | Time-rich, money-poor | Money-rich, time-poor |
| Risk vs Reward | Lower risk, lower reward OR higher risk, higher reward | Safe, modest gains | Risky, potential big gains |
| Control vs Convenience | Full control, more effort OR less control, easier | DIY, full control | Done-for-you, hands-off |
| Speed vs Quality | Fast, good enough OR slow, excellent | Quick and dirty | Slow and polished |
| Autonomy vs Security | Independent, uncertain OR employed, stable | Freedom, risk | Stability, constraints |
| Public vs Private | Visible, social proof OR hidden, privacy | Build in public | Work in private |
| Generalist vs Specialist | Breadth, flexibility OR depth, expertise | Know many things | Know one thing deeply |
| Short-term vs Long-term | Immediate payoff OR delayed larger payoff | Quick wins | Long-term building |
| Solo vs Team | Work alone, keep all OR work with others, share | Full ownership | Shared effort/reward |
| Scale vs Craft | Many customers, less personal OR few customers, high-touch | Volume | Boutique |

---

## Step 3: Present as Scenarios, Not Abstractions

Don't ask: "Do you prefer risk or safety?"
Instead present: "Would you rather have a 90% chance of making $50K or a 20% chance of making $500K?"

For each trade-off, generate 2-3 concrete scenarios:

```
SCENARIO SET: [trade-off dimension]

Scenario A: [concrete situation embodying option A]
- What happens: [specific outcome]
- You get: [specific benefit]
- You give up: [specific cost]

Scenario B: [concrete situation embodying option B]
- What happens: [specific outcome]
- You get: [specific benefit]
- You give up: [specific cost]

User selects: [A / B / NEITHER / BOTH]
```

---

## Step 4: Infer Preferences from Selections

| Selection | Inferred Preference | Confidence |
|-----------|---------------------|------------|
| Chose A in Scenario 1 | Values X over Y | MEDIUM |
| Chose B in Scenario 2 | Values Y over X | MEDIUM |
| Chose A in Scenario 3 | Confirms: Values X | HIGH |

**Consistency check**: If user chose A in Scenario 1 but B in Scenario 3, and both test the same dimension, probe for context dependence.

---

## Step 5: Generate Preference Profile

```
PREFERENCE PROFILE

Strong Preferences (consistent across scenarios):
├── [preference 1]: [evidence from selections]
├── [preference 2]: [evidence from selections]
└── [preference 3]: [evidence from selections]

Weak Preferences (single selection):
├── [preference 4]: [single evidence]
└── [preference 5]: [single evidence]

Context-Dependent (inconsistent):
├── [preference 6]: Prefers X when [context], Y when [other context]
└── [preference 7]: Prefers X when [context], Y when [other context]

Unknown (not tested):
├── [dimension not covered]
└── [dimension not covered]
```

---

## Step 6: Match Preferences to Options

For a list of options (e.g., methods from guess_generation):

| Option | Matches Preferences | Conflicts With | Fit Score |
|--------|---------------------|----------------|-----------|
| [option 1] | [pref A, pref B] | [pref C] | HIGH/MED/LOW |
| [option 2] | [pref A] | [pref B, pref C] | LOW |
| [option 3] | [pref A, pref B, pref C] | none | HIGH |

**Surface better options**: If an option matches all preferences but user hasn't mentioned it, highlight it.

---

## Step 7: Detect Settling

Signs user is settling on suboptimal option:
1. Chosen option conflicts with stated preferences
2. Unchosen option matches preferences better
3. User hasn't considered high-match options

```
SETTLING DETECTION

User's current choice: [option X]
Preference match: [score]

Better matches not considered:
├── [option Y]: matches [preferences], score [higher]
├── [option Z]: matches [preferences], score [higher]

Why user might be settling:
├── [didn't know about option Y]
├── [assumed constraint that doesn't exist]
├── [first viable option, stopped looking]

Recommendation: Present [option Y, Z] before user commits to [option X]
```

---

## Output Format

```
## PREFERENCE ELICITATION: [domain]

### Trade-Offs Presented
[list of scenario pairs]

### Selections Made
[user's choices]

### Preference Profile
STRONG:
- [preference]: [evidence]

WEAK:
- [preference]: [evidence]

CONTEXT-DEPENDENT:
- [preference]: [when X] vs [when Y]

### Option Matching
| Option | Preference Match | Conflicts | Score |
|--------|------------------|-----------|-------|
| ... | ... | ... | ... |

### Better Options to Consider
[options that match preferences but user hasn't considered]

### Settling Risk
[if user is choosing suboptimally, explain why and present alternatives]
```

---

## Execution Checklist

- [ ] 10+ trade-off pairs generated
- [ ] Concrete scenarios created (not abstractions)
- [ ] User selections collected
- [ ] Preference profile generated
- [ ] Options matched to preferences
- [ ] Better options surfaced
- [ ] Settling detection run

---

## Next Procedure

→ INVOKE: /better_option_check [user's current choice] [preference profile]

---

**Execute now**: Elicit preferences for the domain provided.
