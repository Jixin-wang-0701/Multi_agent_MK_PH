**Request addressed:**  
Summary of evidence support for metabolomics‑anchored hypotheses and MK‑secretory gene expression, based on the Cycle‑3 local data context and metabolomics‑to‑mechanism evidence package.  This assessment distinguishes direct user‑data results from inferences, notes missing measurements, and classifies evidence strength.  Public‑dataset analysis yielded no interpretable results; all public‑data claims remain unsupported.

---

### 1.  Methionine → AMD1/polyamine Axis (top‑ranked shortlist chain)

**Metabolite → enzyme → gene → MK expression chain evaluated:**  
- **Metabolite:** methionine, strongly up in PH‑MKs vs Control‑MKs (log2FC +3.26).  
- **KEGG link:** AMD1 (S‑adenosylmethionine decarboxylase) is a pathway‑neighbour gene in cysteine/methionine metabolism and methionine salvage (ec:4.1.1.50).  This is **not** a direct compound‑enzyme link; methionine is not the immediate substrate of AMD1.  The path is: methionine → SAM → decarboxylated SAM (dcSAM) via AMD1.  
- **Gene expression:** *Amd1* is MK‑enriched (enrichment log2 1.35) and strongly PH‑up in MKs (log2FC +1.77, p=6.6e‑06).  This constitutes **direct support** for MK‑specific induction.  
- **Literature:** Two PubMed hits (PMID 38965534, 28658205) link AMD1 to polyamine metabolism and eIF5A hypusination in cancer contexts; no direct PH‑ or MK‑specific literature.  **Indirect support** only.

**Evidence status:**  
- **Direct support:** MK methionine accumulation and MK *Amd1* up‑regulation.  
- **Inferred support:** Polyamine (spermidine/spermine) synthesis, eIF5A hypusination, downstream immune or vascular effects.  Spermidine/spermine were not measured in MKs or lung tissue (explicit gap).  
- **Contradictory evidence:** None.  
- **Missing evidence:** Absolute lack of spermidine/spermine measurements; no direct assay of AMD1 enzymatic activity or dcSAM levels in MKs; no measurement of eIF5A hypusination.

**Downstream axis specificity:**  
Only a broad downstream axis can be supported.  Candidate axes include:  
- Immune‑mediated / T‑helper‑like (polyamine modulation of T‑cell differentiation, e.g., Th17‑like tone)  
- Macrophage/monocyte or neutrophil inflammatory (polyamine‑driven NLRP3 or arginase polarisation)  
- Direct vascular‑wall activation (polyamine sensing by endothelial/smooth muscle receptors)  
- EV/stromal remodelling (polyamine‑laden vesicles).  

All specific examples (Th17, IL‑17, spermidine, specific receptors) remain **provisional** because no direct data link MK polyamines to a particular immune subset or cytokine.  The axis is **unresolved** without product‑level and spatial validation.

**Public dataset status:** No usable public dataset.  GSE289322 analysis failed due to identifier mismatch; no metadata‑derived expression support.  Claims of whole‑lung transcriptomic support for this axis are unsupported.

---

### 2.  Methionine → AMD2 Axis

**Chain similar to AMD1 but with *Amd2*:**  
- *Amd2* is expressed at lower levels (MK pct 4.37%) but still MK‑enriched (log2 0.931) and PH‑up (log2FC 2.175, p=0.0235).  
- Direct support is weaker (lower expression, fewer literature hits).  Same pathway‑neighbour logic.  
- Same missing spermidine/spermine data, same broad‑axis classification.

**Evidence summary for this chain:**  
- **Direct support:** methionine up, *Amd2* up.  
- **Inferred:** polyamine synthesis, downstream axes.  
- **Overall:** Redundant with AMD1; AMD1 is the stronger candidate due to higher expression and significance.

---

### 3.  Inosine → Pnp/Nt5c2 Purine Catabolism Axis

**Metabolite direction critical:**  
- MK inosine is slightly decreased (log2FC –0.34), not elevated.  Whole‑lung inosine and adenosine are unchanged (FDR >0.5).  
- This contradicts an adenosine‑accumulation model; instead it supports accelerated degradation.

**KEGG enzyme‑gene links:**  
- **Pnp** (purine nucleoside phosphorylase): direct compound‑enzyme for inosine (ec:2.4.2.1).  Strongly PH‑up in MKs (log2FC +1.739, p=3.81e‑06) despite modest MK enrichment (log2 –1.217, meaning expression lower than other cells overall, but the PH shift is significant within MKs).  
- **Nt5c2** (cytosolic 5′‑nucleotidase): direct enzyme (ec:3.1.3.5); PH‑up log2FC +2.879, p=2e‑04.  
- Both are direct compound‑enzyme links, strengthening the evidence for purine nucleotide degradation.

**Evidence status:**  
- **Direct support:** MK *Pnp* and *Nt5c2* up‑regulation; MK inosine decrease (which, while modest, is directionally consistent with increased catabolism).  
- **Inferred:** Production of hypoxanthine/xanthine/uric acid; generation of ROS via xanthine oxidase; downstream immune activation.  None of these downstream products were measured in MKs or perivascular space (**explicit gap**).  
- **Literature:** No direct PH‑ or MK‑specific literature.  General literature supports purine catabolites (uric acid, ROS) as immune danger signals.  **Indirect support.**  
- **Negative evidence:** Whole‑lung inosine and adenosine unchanged, meaning the effect is likely localised to MKs/perivascular niche.

**Downstream axis specificity:** Broad axis only.  Candidate axes:  
- Immune‑mediated (NLRP3 inflammasome activation via uric acid/ROS)  
- Macrophage/monocyte inflammatory (xanthine oxidase‑derived ROS)  
- Purinergic receptor signalling on vascular or immune cells  
- Direct oxidative stress on vascular wall.  

All specific mediators (NLRP3, IL‑1β, xanthine oxidase, A2B receptor) are provisional because direct metabolite measurements of hypoxanthine/xanthine/uric acid are absent, and the cellular source of ROS is not confirmed.

**Public dataset status:** No support; GSE289322 analysis yielded no relevant gene matches.

---

### 4.  Retinoic Acid → Cyp26b1 Axis

**Shortlisted but lower rank:**  
- Metabolite: retinoic acid strongly up (log2FC +3.44) in PH‑MKs vs Control‑MKs.  
- KEGG: Cyp26b1 (cytochrome P450 26B1) is a pathway‑neighbour gene in retinol metabolism (ec:1.14.14.-).  Not a direct compound‑enzyme; retinoic acid is a substrate of CYP26 enzymes, but the link is one step removed in KEGG mapping.  
- Gene expression: Cyp26b1 is MK‑enriched (log2 0.728) but its PH‑up log2FC (+0.912) is not statistically significant (p=0.253).  
- Literature: none retrieved.  
- **Overall evidence strength is weak** – the gene differential is not significant, and no direct enzyme link or literature support.  This axis does not meet the strong evidence bar set for the primary hypotheses.  It may be considered for future exploration but is not robust for cycle‑3 hypotheses.

---

### 5.  Conditional Matricellular/Secretome Axis (Thbs1, Pdgfb, Tgfb1)

**Not a metabolite‑to‑enzyme chain per se, but hinges on AMD1‑eIF5A control.**  
- **Gene expression data is direct:** *Thbs1*, *Pdgfb*, and *Tgfb1* are confirmed MK‑expressed, MK‑enriched, and PH‑up in MKs (Seurat table).  This is **direct support** for their up‑regulation in hypoxic MKs.  
- **Metabolic link:** The chain methionine → AMD1 → polyamines → eIF5A hypusination → enhanced translation of these factors is **inferred**.  Spermidine and eIF5A hypusination are not measured.  eIF5A‑dependent translation of these specific mRNAs has not been demonstrated in MKs.  
- **Public data:** No validation from public datasets.  
- **Broad axis:** Direct vascular‑wall/matrix remodelling.  Candidate mechanisms include:  
  - PDGF‑B → smooth muscle hyperplasia  
  - TSP‑1 → TGF‑β activation → perivascular fibrosis  
  - TGF‑β1 → fibroblast activation.  
  The exact combinatorial effect remains speculative; the evidence supports a direction but not a single dominant pathway.

---

### 6.  Other Metabolic Chains (Not Prioritized)

- Methionine → Dnmt3b: Dnmt3b lacks significant MK enrichment (log2 0.193) and its PH‑up log2FC (+1.59) is not significant (p=0.212).  **Weak support.**  
- Retinoic acid → Cyp1a1: Cyp1a1 is a direct compound‑enzyme (ec:1.14.14.1) and is PH‑up (log2FC +2.787, p=0.0221) but MK enrichment is negative (–0.739), meaning it is not MK‑specific.  **Weak as an MK‑specific mechanism.**  
- Tryptophan → Cyp1a1, Aldh2, etc.: Similar issues of enrichment specificity.  Not currently robust.

---

### 7.  Overall Summary for Downstream Agents

**Strongly supported claims:**
- Lung MKs accumulate methionine and up‑regulate *Amd1* under hypoxia (direct metabolite + gene data).  
- *Pnp* and *Nt5c2* are strongly up‑regulated in PH‑MKs, and inosine is not elevated, indicating purine catabolic flow (direct enzyme‑gene data, directional metabolite support).  
- *Thbs1*, *Pdgfb*, *Tgfb1* are MK‑enriched and further increased in PH‑MKs (direct gene expression).  

**Weakly supported claims:**
- Spermidine/spermine accumulation, eIF5A hypusination, and translational control of matricellular factors by polyamines (inferred only).  
- Retinoic acid → Cyp26b1 as an MK‑specific mechanism (gene differential not significant).  

**Unsupported claims:**
- Direct secretion of polyamines or purine catabolites by MKs in the perivascular space (no secretion assays).  
- Any specific immune cell subset (Th17, macrophages, NLRP3) as the direct responder (no spatial or receptor evidence).  
- Adenosine accumulation or A2B‑mediated signalling from MKs (contradicted by metabolite data).  
- Public‑dataset validation of any of these pathways (no usable public datasets).  

**Claims requiring further validation:**
- MK spatial proximity to perivascular immune cells or vascular wall cells.  
- Functional requirement of MK‑derived AMD1 or PNP for vascular remodelling in vivo.  
- Direct measurement of downstream metabolites: spermidine, spermine, hypoxanthine, xanthine, uric acid in MKs and perivascular fluid.  

**Reasoning gaps that hypothesis writers should not skip:**
- The AMD1–polyamine axis lacks product‑level evidence; hypotheses must explicitly state that spermidine/spermine are assumed to be elevated based on enzyme/substrate up‑regulation.  
- The Pnp axis must acknowledge that the primary catabolites (hypoxanthine/xanthine) are inferred from the combination of Pnp up‑regulation and inosine decrease, but not measured.  
- The matricellular secretome axis relies on the untested hypothesis that AMD1/eIF5A controls translation of *Thbs1*, *Pdgfb*, and *Tgfb1*; alternative regulatory mechanisms could be at play.  
- All hypotheses should maintain **direction‑level resolution** and label specific downstream cell types, cytokines, and receptors as provisional until direct evidence is obtained.  

This assessment confirms that the Cycle‑3 evidence package provides strong anchoring for the three required hypothesis axes, but none of the chains are resolved to a specific mechanistic bridge.  The generation agents’ outputs appropriately stay at the direction‑level and acknowledge the gaps.
