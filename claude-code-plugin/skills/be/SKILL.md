---
name: "be - Bandit Exploration Orderings"
description: "Orderings from multi-armed bandit algorithms for balancing exploration of unknown options with exploitation of known good ones."
---

# Bandit Exploration Orderings

**Input**: $ARGUMENTS

---

## Overview

When you have multiple options with uncertain payoffs, you face the explore-exploit tradeoff: try new things (explore) or stick with what works (exploit). Multi-armed bandit algorithms provide principled orderings for this tradeoff.

## Core Principle

Early on, explore broadly. As information accumulates, shift toward exploiting the best-known options. The optimal balance depends on how many decisions remain.

## Ordering Rules

### Rule 1: Epsilon-Greedy — Mostly Exploit, Sometimes Explore
- With probability (1-ε): choose the best-known option
- With probability ε: choose randomly among all options
- Start with high ε (~0.3), decrease over time
- **When**: simple problems, many decisions, low cost of exploration

### Rule 2: Upper Confidence Bound (UCB) — Optimism Under Uncertainty
- Score each option: estimated value + uncertainty bonus
- Choose the option with highest score
- Uncertainty bonus decreases as you sample more
- **When**: want principled exploration, can estimate confidence intervals

### Rule 3: Thompson Sampling — Sample from Beliefs
- Maintain a probability distribution over each option's value
- Sample from each distribution, choose highest sample
- Naturally balances: uncertain options get explored, good options get exploited
- **When**: can maintain Bayesian beliefs, want adaptive exploration

### Rule 4: Successive Elimination — Remove Losers
- Give each option minimum samples
- Eliminate options that are statistically worse than the best
- Concentrate remaining budget on survivors
- **When**: want to identify the best option efficiently

## Application Procedure

### Step 1: Frame as Bandit Problem
1. What are the "arms" (options)?
2. What is the "reward" (payoff)?
3. How many "pulls" (decisions) do you have?
4. Is exploration costly? Risky?

### Step 2: Choose Strategy
- Few decisions remaining → exploit (little time to benefit from exploration)
- Many decisions → explore (information has long-term value)
- High variance between options → explore more (bigger upside from finding the best)
- Low cost of failure → explore freely

### Step 3: Execute and Update
1. Choose option per strategy
2. Observe outcome
3. Update beliefs about that option
4. Repeat with updated beliefs

## Anti-Patterns
- Pure exploitation (never trying new things — stuck on local optimum)
- Pure exploration (never committing — wasting known-good options)
- Exploring when you're out of time to benefit from what you learn

## When to Use
- A/B testing and optimization
- Resource allocation across uncertain options
- Career decisions (try new roles vs deepen current)
- Any sequential decision with learning

## Verification
- [ ] Options and payoffs identified
- [ ] Time horizon considered
- [ ] Exploration budget appropriate for remaining decisions
- [ ] Beliefs updated after each observation
