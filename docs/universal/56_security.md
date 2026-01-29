# Universal: Security (56)

**Category**: CORE - Protection and Security
**Source**: [O: universal_goal_analysis.yaml lines 1973-1985 security category]
**Structure**: One question per entry, VOI-marked with realistic distribution

---

## VOI Rating = Action Divergence

- **HIGH**: Different answers → completely different action paths
- **MED**: Different answers → same general direction, different approach
- **LOW**: Different answers → same actions, different framing/flavor

---

## Q1: Is there anything that needs protection for goal success?
[VOI: HIGH - Critical assets/unknown needs means protection essential vs proceed]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, critical assets | HIGH | Protection essential vs proceed | Protect | No critical assets |
| Unknown protection needs | HIGH | Protection audit vs assume | Protection audit | Needs known |
| Yes, moderate value | MED | Evaluate protection vs proceed | Evaluate | Different value |
| No protection needed | LOW | Nothing at risk either way | Proceed | Protection needed |

---

## Q2: What threatens each protected asset?
[VOI: HIGH - Threats unknown means vulnerable, analysis vs defend against known]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Threats unknown | HIGH | Threat analysis vs defend | Threat analysis | Threats known |
| Some threats known | MED | Investigate more vs defend | Investigate more | More unknown |
| Known threats identified | LOW | Can defend either way | Defend against | Threats unknown |

---

## Q3: What protections are in place?
[VOI: HIGH - Weak/no protections means vulnerable, strengthen vs maintain]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Weak protections | HIGH | Major strengthening vs maintain | Major strengthening | Stronger |
| No protections | HIGH | Create protections vs maintain | Create protections | Protections exist |
| Unknown protections | MED | Protection audit vs assume | Protection audit | Protections known |
| Moderate protections | MED | Strengthen vs maintain | Strengthen | Different level |
| Strong protections | LOW | Well defended either way | Maintain | Weaker than thought |

---

## Q4: Are protections adequate for threats?
[VOI: HIGH - Inadequate/unknown means at risk, major upgrade vs maintain]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| No, inadequate | HIGH | Major upgrade vs maintain | Major upgrade | Adequate |
| Unknown adequacy | HIGH | Adequacy check vs assume | Adequacy check | Adequacy known |
| Partially adequate | MED | Fill gaps vs maintain | Fill gaps | Different level |
| Yes, adequate | LOW | Well matched either way | Maintain | Inadequate |

---

## Q5: What vulnerabilities exist?
[VOI: HIGH - Unknown vulnerabilities means blind spot, scan vs address known]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Unknown if vulnerabilities | HIGH | Vulnerability scan vs assume | Vulnerability scan | Vulnerabilities known |
| Known vulnerabilities | MED | Address them vs accept | Fix vulnerabilities | Unknown vulnerabilities |
| No known vulnerabilities | MED | Stay vigilant vs relax | Stay vigilant | Vulnerabilities exist |

---

## Q6: What would addressing vulnerabilities require?
[VOI: HIGH - Cannot address means accept risk, mitigate differently vs fix]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Cannot address | HIGH | Mitigate differently vs fix | Mitigate differently | Can address |
| Unknown requirements | MED | Requirements analysis vs assume | Requirements analysis | Requirements known |
| Major overhaul | MED | Plan carefully vs quick fix | Plan carefully | Smaller effort |
| Significant effort | MED | Evaluate priority vs quick | Evaluate priority | Different effort |
| Quick fix | LOW | Easy either way | Fix now | Takes longer |

---

## Question Order by Action Divergence

**HIGH VOI (ask first - route to different action paths):**
1. Q1: Needs protection? (Critical/unknown → protect vs proceed)
2. Q4: Adequate? (No/unknown → upgrade vs maintain)
3. Q2: Threats? (Unknown → analysis vs defend)
4. Q3: Protections? (Weak/none → strengthen vs maintain)
5. Q5: Vulnerabilities? (Unknown → scan vs address)
6. Q6: Remediation? (Cannot → mitigate differently vs fix)

**MED/LOW VOI (ask second - refine approach):**
(All questions have HIGH entries, order by criticality)

---

## Key Insight

**VOI ≠ Security Severity**

VOI = Action Divergence

A HIGH VOI security question is one where the answer determines whether you BUILD PROTECTION or PROCEED WITHOUT. "Critical assets needing protection" routes you to "protection essential" - a completely different action than "proceed normally."

A LOW VOI security question like "strong vs moderate protections" doesn't change your fundamental approach - you'll maintain security either way, just with different confidence levels.

---

## Coverage Summary

```
QUESTIONS: 6
ENTRIES: 27

VOI Distribution:
- HIGH: 8 entries (30%)
- MED: 12 entries (44%)
- LOW: 7 entries (26%)

Note: Higher HIGH% because security failures can be catastrophic
```
