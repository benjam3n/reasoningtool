---
name: "ops - Optical Pooled Screening"
description: "Procedure for designing and executing optical pooled screening experiments in functional genomics."
---

# Optical Pooled Screening

**Input**: $ARGUMENTS

---

## Overview

Optical pooled screening combines CRISPR perturbations with high-content imaging to study gene function at scale. This procedure guides experiment design, library selection, imaging strategy, and analysis. Enables screening thousands of genetic perturbations while preserving spatial and morphological information.

## Steps

### Step 1: Define the Biological Question
1. What phenotype or process are you studying?
2. What perturbation type? (CRISPRi, CRISPRa, knockout, base editing)
3. What readout captures your phenotype? (morphology, localization, reporter, marker expression)
4. What is the expected effect size? (determines required cell numbers)
5. What controls are needed? (non-targeting, positive controls, pathway controls)

### Step 2: Design the Library
1. Select gene targets based on question (whole-genome, focused pathway, validation)
2. Number of guides per gene (3-5 recommended for redundancy)
3. Total library size = genes x guides/gene + controls
4. Library format: plasmid pool or synthetic
5. Include barcode sequences for in-situ readout

### Step 3: Plan the Imaging Strategy
1. Channels needed:
   - Barcode readout (FISH or in-situ sequencing)
   - Phenotype markers (antibodies, reporters, dyes)
   - Cell segmentation (membrane, nuclear markers)
2. Imaging modality: widefield, confocal, or high-content automated
3. Resolution required for phenotype detection
4. Fields of view needed: cells/guide x guides x coverage factor
5. Z-stacks needed? Time-lapse?

### Step 4: Execute the Screen
1. Transduce cells with library at low MOI (aim for single integration)
2. Select and expand transduced cells
3. Apply experimental conditions if applicable
4. Fix, stain, and prepare for imaging
5. Acquire images systematically (automated preferred)
6. Perform barcode readout (sequential FISH rounds or in-situ sequencing)

### Step 5: Analyze Results
1. **Segmentation**: identify individual cells
2. **Barcode assignment**: link each cell to its perturbation
3. **Feature extraction**: quantify phenotype per cell
4. **Quality filtering**: remove low-quality cells, ambiguous barcodes
5. **Statistical analysis**: compare each perturbation to controls
   - Account for multiple testing
   - Use appropriate statistical test for phenotype type
6. **Hit calling**: identify significant perturbations

### Step 6: Validate Hits
1. Confirm top hits with individual guide validation
2. Use orthogonal assays to verify phenotype
3. Check for guide-specific vs gene-specific effects
4. Place hits in biological context (pathways, networks)
5. Design follow-up experiments

```
SCREEN SUMMARY:
Question: [biological question]
Library: [N genes, N guides, perturbation type]
Readout: [phenotype measured]
Scale: [N cells screened]

Hits: [N significant at FDR < 0.05]
Top hits:
1. [gene] — Effect: [description] — Confidence: [high/medium]
2. [gene] — Effect: [description] — Confidence: [high/medium]

Validation status: [N validated / N tested]
Next steps: [follow-up experiments]
```

## When to Use
- Functional genomics screens requiring spatial/morphological readouts
- When pooled screening is preferred over arrayed format
- Gene-phenotype mapping at scale
- Drug target discovery with cellular phenotyping

## Verification
- [ ] Biological question clearly defined
- [ ] Library designed with adequate guides/gene and controls
- [ ] Imaging strategy captures required phenotype
- [ ] MOI optimized for single integration
- [ ] Analysis accounts for multiple testing
- [ ] Top hits validated with orthogonal approaches
