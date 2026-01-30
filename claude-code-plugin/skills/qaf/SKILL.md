---
name: "qaf - Question Analysis Framework"
description: "This framework provides methods for analyzing questions to determine:"
---

# Question Analysis Framework

## Overview
This framework provides methods for analyzing questions to determine:
1. Which questions are foundational (answering them unlocks other answers)
2. Which questions already have rigorous answers in existing research
3. Which questions can be answered deductively vs empirically
4. How questions depend on each other (DAG structure)
5. What analysis methods produce answers with high confidence

## When to Use
- When facing many questions and unsure where to start
- When analyzing philosophical or complex conceptual questions
- During RCI when you've generated many causal chains
- When determining which assumptions to investigate first
- Before committing resources to answering a question

## Output Format
```
answer_documentation: "## Answer: [The question]\n\n**Certainty Level**: [level] (guessing:\
  \ [0-1])\n\n**Derivation**:\n- Premise 1: [statement] (certainty: [level])\n- Premise\
  \ 2: [statement] (certainty: [level])\n- \u2234 Conclusion: [statement]\n\n**Remaining\
  \ Uncertainty**: [what's still unknown]\n"
dependency_graph: "## Question Dependencies\n\nROOT QUESTIONS:\n- Q1: [question]\n\
  - Q2: [question]\n\nDEPENDENCY CHAINS:\nQ3 depends on \u2192 Q1, Q2\nQ4 depends\
  \ on \u2192 Q3\n...\n"
question_classification: '## Question: [The question]


  | Dimension | Level | Implication |

  |-----------|-------|-------------|

  | Foundationality | [1-5] | [What this means] |

  | Prior Art | [1-5] | [Action to take] |

  | Verifiability | [1-5] | [Method to use] |

  | Tractability | [1-5] | [Approach] |

  | Position | [type] | [Priority] |


  **Priority Score**: [calculated]

  **Recommended Action**: [what to do next]

  '

```

---

**Input**: $ARGUMENTS

Apply this procedure to the input provided.