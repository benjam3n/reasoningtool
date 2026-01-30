---
name: plr
description: "Identify evidence-based, neglected, tractable policies for advocacy campaigns"
---

# Policy Research

## Overview
Identify evidence-based, neglected, tractable policies for advocacy campaigns

## Steps

### Step 1: Source identification and review
Systematically review primary sources for policy candidates:
1. Review Open Philanthropy focus areas for EA-aligned priorities
2. Check Niskanen Center for evidence-based, bipartisan options
3. Review Brookings Institution for research-backed recommendations
4. Check RAND Corporation for policy analysis
5. Review CBO for cost-benefit analyzed policies
6. Check 80,000 Hours problem profiles for high-impact areas
7. Search secondary sources (CRS, GAO, academic journals)

For each promising policy found:
- Note specific actionable recommendation
- Record evidence cited
- Check current advocacy level
- Add to candidates list

### Step 2: Initial screening
Apply quick filters to narrow candidate list:
1. Has specific actionable ask (bill, executive action, regulation)
2. Has some evidence base (not purely theoretical)
3. Not already heavily advocated (check OpenSecrets lobbying data)
4. Plausible path to implementation
5. Aligns with any specified constraints

Mark each candidate as: Promising / Maybe / Unlikely

### Step 3: Deep scoring
Score each filtered candidate on five criteria (1-10 scale):

Evidence (weight 0.25):
- 1-3: Theoretical only
- 4-6: Observational studies
- 7-10: RCTs or meta-analyses
Sources: Google Scholar, CBO reports, CRS reports

Cost-Effectiveness (weight 0.20):
- 1-3: Unclear ROI
- 4-6: Moderate ROI
- 7-10: High ROI (CBO scored)
Sources: CBO cost estimates, academic cost-benefit analyses

Neglectedness (weight 0.20):
- 1-3: Major advocacy already exists
- 4-6: Some advocacy present
- 7-10: Little or no organized advocacy
Check: OpenSecrets lobbying data, news search, think tank activity

Tractability (weight 0.20):
- 1-3: Major opposition, unlikely to pass
- 4-6: Mixed political landscape
- 7-10: Bipartisan potential
Indicators: Recent votes, legislator statements, political climate

Impact (weight 0.15):
- 1-3: Less than 100K affected
- 4-6: 100K to 1M affected
- 7-10: More than 1M affected
Measurement: Population affected, severity, duration

Calculate weighted total for each candidate.

### Step 4: Ranking and selection
Rank candidates by weighted score and select portfolio:
1. Sort by total weighted score (descending)
2. Apply selection criteria:
   - Score 6.0+ overall
   - Clear evidence base
   - Genuinely neglected (neglect score 6+)
   - Specific actionable ask
3. Apply diversity requirements:
   - At least one traditionally "left" policy
   - At least one traditionally "right" policy
   - At least one clearly bipartisan
   - Different congressional committees
4. Select top 3-5 policies balancing score and diversity

### Step 5: Policy brief creation
Create one-page brief for each selected policy:

Structure:
1. The Problem (2-3 sentences on current situation and harm)
2. The Evidence (3 key findings with sources)
3. The Solution (specific policy recommendation, bill number if exists)
4. The Impact (quantified benefits, cost-benefit ratio)
5. Political Landscape (current support, opposition, path forward)
6. Action Requested (specific ask for legislators/staff)
7. Sources (key citations)

Format as professional one-pager suitable for legislative staff.

### Step 6: Evidence compilation
Create detailed evidence summary for each selected policy:
1. Full literature review (key studies with summaries)
2. All relevant CBO/CRS reports
3. Historical voting patterns on similar issues
4. Stakeholder map (supporters, opponents, undecided)
5. Counterarguments and evidence-based rebuttals
6. State-level implementations and outcomes (if applicable)

This serves as reference material for meetings and detailed questions.

### Step 7: Database population
Enter all policy data into advocacy database:
1. Add all candidates to policies table
2. Include all five scores
3. Mark selected policies with status "active"
4. Link brief file paths
5. Record research sources and dates


## When to Use
- Starting a new advocacy project and need to identify what to advocate for
- Evaluating policy opportunities for campaign selection
- Building an evidence-based advocacy portfolio
- Refreshing policy priorities after legislative changes
- Assessing whether to join existing advocacy coalitions
- Preparing grant applications requiring policy rationale

## Verification
- At least 20 policies reviewed across multiple sources
- All candidates scored on all five criteria with documentation
- Selected policies meet 6.0+ threshold
- Diversity requirements met (political, committee)
- One-page briefs are clear, professional, and complete
- Evidence summaries include counterargument rebuttals
- Database fully populated with scoring data

---

**Input**: $ARGUMENTS

Apply this procedure to the input provided.