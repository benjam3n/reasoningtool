---
name: smc
description: "An exhaustive inventory of search methods found in nature, science, technology, and human systems."
---

# Comprehensive Search Methods Catalog

**Input**: $ARGUMENTS

---

## Overview

An exhaustive inventory of search methods found in nature, science, technology, and human systems. Understanding these methods enables borrowing strategies across domains.

Meta-question: Is intelligence just "how well you can search"?

## Steps

### Step 1: Identify the Search Problem
1. What are you searching FOR? (solution, information, option, path, configuration)
2. What is the search SPACE? (finite/infinite, discrete/continuous, structured/unstructured)
3. What CONSTRAINTS exist? (time, resources, access, knowledge)
4. What does SUCCESS look like? (exact match, good enough, optimal, novel)

### Step 2: Catalog of Search Methods by Domain

**Exhaustive / Systematic:**
- Brute force enumeration — try everything
- Grid search — sample at regular intervals
- Branch and bound — eliminate provably bad regions
- Backtracking — try, fail, undo, try different path
- Dynamic programming — break into overlapping subproblems

**Heuristic / Guided:**
- Hill climbing — always move toward improvement
- Simulated annealing — accept worse moves early, fewer later
- Tabu search — remember where you've been, don't repeat
- Beam search — keep top-N candidates, expand all
- A* / best-first — use estimated distance to guide exploration

**Evolutionary / Population:**
- Genetic algorithms — mutate, crossover, select
- Particle swarm — each agent influenced by personal and group best
- Ant colony — pheromone trails reinforce good paths
- Differential evolution — perturb using differences between candidates

**Probabilistic / Statistical:**
- Monte Carlo — random sampling
- Bayesian optimization — model the objective, sample where uncertain
- MCMC (Markov Chain Monte Carlo) — random walk biased toward good regions
- Thompson sampling — sample from posterior, act on sample
- Random restart — run local search many times from random starts

**Adversarial / Game-Theoretic:**
- Minimax — assume opponent plays optimally
- Alpha-beta pruning — skip branches that can't affect outcome
- Nash equilibrium search — find stable strategy profiles
- Regret minimization — minimize worst-case regret over time

**Learning / Adaptive:**
- Reinforcement learning — reward good paths, punish bad ones
- Active learning — query the most informative examples
- Curriculum learning — start easy, increase difficulty
- Transfer learning — apply learned search strategy to new domain

**Biological / Natural:**
- Chemotaxis — follow gradient (bacteria)
- Lévy flights — short local searches + occasional long jumps (foraging)
- Stigmergy — modify environment to guide future search (ants, termites)
- Immune system — generate random antibodies, amplify matches
- Neural search — pattern completion from partial cues (brain)

**Social / Human:**
- Ask an expert — skip search, use someone else's result
- Crowdsourcing — distribute search across many agents
- Market mechanisms — price signals aggregate distributed information
- Gossip protocols — spread information through local exchanges
- Institutional memory — search organizational records

**Constraint-Based:**
- SAT solvers — systematic logical constraint satisfaction
- Linear programming — optimize within linear constraints
- Constraint propagation — eliminate impossible values before searching

### Step 3: Match Methods to Problem Characteristics

| Problem Characteristic | Best Methods |
|----------------------|-------------|
| Small search space | Exhaustive, branch and bound |
| Large smooth space | Hill climbing, gradient descent |
| Large rugged space | Simulated annealing, genetic algorithms |
| Unknown landscape | Bayesian optimization, random restart |
| Adversarial | Minimax, regret minimization |
| Time-constrained | Heuristic, beam search, ask expert |
| Need diversity | Population-based, random restart |
| Need optimality proof | Branch and bound, LP, exhaustive |
| Sequential decisions | RL, MCTS, bandit methods |
| Social/organizational | Crowdsource, expert, market |

### Step 4: Apply to Input
1. Classify the input's search problem (from Step 1)
2. Match to appropriate methods (from Step 3)
3. For each recommended method:
   - How would it apply concretely?
   - What resources does it require?
   - What are its failure modes?
4. Recommend primary method + backup

### Step 5: Cross-Domain Transfer
1. Is the input's domain using only its "native" search methods?
2. What methods from OTHER domains might apply?
3. Which cross-domain transfer is most promising?
4. → INVOKE: /cda (cross-domain analogy) if transfer looks productive

### Step 6: Report
```
SEARCH METHOD ANALYSIS:
Problem type: [classification]
Search space: [size, structure, smoothness]
Constraints: [time, resources, knowledge]

Recommended methods:
1. [Primary] — why it fits, how to apply
2. [Backup] — when to switch to this
3. [Cross-domain] — borrowed from [domain], novel application

Methods to AVOID: [which and why]
```

## When to Use
- Stuck on a problem and need a new approach
- Want to systematically consider all search strategies
- Looking for cross-domain inspiration
- Designing an algorithm or process

## Verification
- [ ] Search problem clearly characterized
- [ ] Multiple method categories considered
- [ ] Methods matched to problem characteristics
- [ ] Cross-domain transfer explored
- [ ] Failure modes of recommended methods noted
