# Universal: Adversarial vs Neutral Environment (127)

**Category**: META - Is Something Optimizing Against You?
**Source**: Game theory, competition, security
**Structure**: Questions ordered by Value of Information (action divergence)

---

## VOI Rating = Action Divergence

- **HIGH**: Different answers → completely different action paths
- **MED**: Different answers → same general direction, different approach
- **LOW**: Different answers → same actions, different framing/flavor

---

## Q1: Is there an adversary actively working against us?

[VOI: HIGH - adversary = game theory; no adversary = optimization]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Active adversary | HIGH | Game-theoretic thinking | Anticipate counter-moves | Optimized against, defeated |
| Unknown if adversary | MED | May be naive | Adversary detection | Either paranoid or naive |
| No adversary | LOW | Simple optimization | Optimize freely | Paranoid when unnecessary |

---

## Q2: Is the adversary adapting to our strategy?

[VOI: HIGH - adaptive adversary requires dynamic strategy]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Adversary adapts | HIGH | Must evolve | Unpredictable/dynamic | Static against adaptive, countered |
| Unknown if adapts | MED | May be countered | Adaptation testing | Either countered or over-complex |
| Adversary static | LOW | Can predict | Exploit fixed strategy | Think static when adaptive |

---

## Q3: Is this zero-sum, negative-sum, or positive-sum?

[VOI: HIGH - determines cooperation vs competition]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Zero-sum | HIGH | Pure competition | Competitive strategy | Cooperate when should compete |
| Unknown sum | MED | May miss opportunity | Sum analysis | Either compete or cooperate wrongly |
| Negative-sum | HIGH | Both can lose | Seek exit or change game | Stay in destructive competition |
| Positive-sum | HIGH | Mutual gain possible | Seek cooperation | Compete when could cooperate |

---

## Q4: Does revealing our strategy help or hurt?

[VOI: HIGH - transparency can be strength or weakness]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Revelation hurts | HIGH | Secrecy needed | Hide strategy | Countered through revelation |
| Unknown effect | MED | May be exploited | Revelation analysis | Either reveal harmfully or hide unnecessarily |
| Revelation helps | HIGH | Commitment value | Announce strategy | Hide when should reveal |

---

## Q5: Can we change the game rather than play it?

[VOI: HIGH - game change often better than optimal play]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Can change game | HIGH | Meta-move available | Change game | Play bad game when could change |
| Unknown if changeable | MED | May miss opportunity | Game-change analysis | Either tilt windmills or miss meta-move |
| Game fixed | LOW | Must play | Optimize within rules | Seek impossible change |

---

## Q6: Are there coalitions forming?

[VOI: MED - coalition dynamics affect strategy]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Coalitions forming | MED | Alliance matters | Form/counter coalition | Isolated, ganged up on |
| Unknown coalition state | MED | May be outmaneuvered | Coalition analysis | Either miss alliance or miss threat |
| No coalitions | LOW | Individual play | Individual strategy | Miss coalition opportunity/threat |

---

## Q7: Is there information asymmetry?

[VOI: MED - information advantage can be decisive]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| We have info advantage | MED | Exploit advantage | Use information edge | Waste advantage |
| Unknown asymmetry | MED | May be disadvantaged | Information analysis | Either waste edge or be exploited |
| Adversary has info advantage | MED | Disadvantaged | Reduce asymmetry | Act on false confidence |
| Symmetric information | LOW | Level playing field | No info strategy | Miss asymmetry |

---

## Q8: What are the adversary's incentives?

[VOI: MED - understanding incentives predicts behavior]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Incentives unknown | MED | Can't predict | Incentive discovery | Surprised by behavior |
| Incentives misaligned | MED | Conflict inherent | Manage conflict | Expect cooperation |
| Incentives aligned | LOW | Potential cooperation | Seek alignment | Fight when could cooperate |

---

## Q9: Is this a repeated game?

[VOI: LOW - affects strategy but similar analysis]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Repeated game | LOW | Reputation matters | Build reputation | Burn bridges |
| Unknown if repeated | LOW | May misjudge stakes | Repetition analysis | Either burn bridges or over-invest |
| One-shot game | LOW | No future consequences | Optimize this round | Over-invest in reputation |

---

## Q10: Are there enforceable agreements possible?

[VOI: LOW - affects coordination but similar analysis]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Enforceable agreements | LOW | Contract possible | Seek agreement | Fight when could contract |
| Unknown enforceability | LOW | May miss opportunity | Enforcement analysis | Either miss agreement or unenforceable deal |
| No enforcement possible | LOW | Must self-enforce | Rely on self-interest | Trust unenforceable agreement |

---

## Summary Statistics

- Total questions: 10
- Total entries: 41
- HIGH VOI: 11 (27%)
- MED VOI: 16 (39%)
- LOW VOI: 14 (34%)

---

## Question Order by Action Divergence

**Ask first (HIGH VOI):**
1. Q1: Active adversary? - game theory vs optimization
2. Q2: Adversary adapts? - static vs dynamic strategy
3. Q3: Zero/negative/positive-sum? - compete vs cooperate
4. Q4: Reveal strategy? - transparency effects
5. Q5: Change the game? - meta-moves

**Ask if relevant (MED VOI):**
6. Q6: Coalitions? - alliance dynamics
7. Q7: Information asymmetry? - info advantage
8. Q8: Adversary incentives? - prediction

**Low priority (LOW VOI):**
9. Q9: Repeated game? - reputation
10. Q10: Enforceable agreements? - contracts

---

## Key Insight

**VOI ≠ game-theoretic sophistication. VOI = action divergence.**

"Are there enforceable agreements?" is interesting but has LOW VOI - you do similar analysis regardless.

"Is there an adversary actively working against us?" has HIGH VOI - adversary means every choice must anticipate countermoves.

---

## The Strategy Switch

**No adversary**: Optimize against nature. Find the best solution. Nature doesn't adapt.

**Adversary present**: Optimize against intelligence. Expect counter-moves. Your "best" strategy gets exploited.

Naive optimization in adversarial environments = predictable = defeated.

Key heuristic: If your strategy would fail if the adversary knew it, you're being too predictable.

The deepest insight: Most people under-detect adversaries (assume cooperation when facing competition) AND over-detect adversaries (assume competition when cooperation is available).

Ask: Is this actually adversarial, or am I projecting conflict?
