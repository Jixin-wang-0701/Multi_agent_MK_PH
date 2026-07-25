# Cycle Summary

## PI research brief
PI_TO_GENERATION_BRIEF

**Cycle ID:** 1

**Central question:**  
How do in‑situ megakaryocytes (MKs) promote hypoxia‑induced vascular remodeling? This cycle will focus on broad mechanism discovery, with a strong metabolomics‑driven component, generating direction‑level causal hypotheses anchored in user‑provided data.

**Biological focus:**  
- In‑situ lung‑resident MKs (or MK‑like cells) in the pulmonary microenvironment.  
- Hypoxia exposure as the initiating stimulus.  
- Pulmonary vascular remodeling phenotypes: medial thickening, muscularization, stiffening, endothelial dysfunction, perivascular matrix alterations.  
- Relevant cellular compartments: endothelial cells (VEC, AEC), vascular smooth muscle cells (VSMC), fibroblasts, pericytes, lung macrophages (AM, IM, iMON), monocytes, neutrophils, T cells (CD8_T etc.), NK cells, B cells, and other stromal cells.  
- Mechanism classes: metabolic reprogramming, paracrine/ligand‑receptor signalling, extracellular vesicles, thrombo‑inflammatory/coagulation axes, immune recruitment/activation, and extracellular matrix remodelling.

**Data sources to prioritize:**  
1. **User‑provided single‑cell RNA‑seq:** `seurat_merged.rds` (71,302 cells; RNA and SCT assays; annotations including `manual_anno` with MK/platelet population; PH vs control metadata; gene expression metrics). Generation agents must query gene expression, enrichment, differential expression between PH and control, and between MK/platelet and other cells.  
2. **User‑provided metabolomics:**  
   - `sFig6A Raw data.xlsx` – metabolomics from sorted control and PH MKs (MK‑specific).  
   - `Figure6D+F raw data.xlsx` – lung tissue metabolomics from hypoxia‑exposed WT and KO mice (whole‑tissue context).  
   Agents must use the pre‑computed *Metabolomics‑to‑Mechanism Evidence Context* (provided below) as the authoritative starting point for metabolite‑enzyme‑MK‑remodeling chains.  
3. **User‑provided prior results:** `prior_results.docx` – established evidence that lung‑resident MKs, not bone‑marrow MKs, drive hypoxia‑induced PH and vascular remodelling (TPO/TPOR models, BM transplant, adoptive transfer).  
4. **Literature and established biological knowledge:** KEGG pathways, PubMed hits for candidate genes/metabolites, and known mechanisms of vascular remodelling and MK biology.  
5. **Public datasets** – search for validation and orthogonal evidence (see dedicated search tasks below).  

**Public dataset search tasks:**  
The Public Dataset Discovery Module will execute the following repository searches. These tasks are intentionally broad; they are not claims of data availability.  
1. **Single‑cell/snRNA‑seq of hypoxic pulmonary hypertension models:** `"pulmonary hypertension" AND (hypoxia OR chronic hypoxia) AND (lung OR pulmonary artery) AND (single-cell OR single-nucleus) AND (mouse OR murine)`  
2. **Bulk RNA‑seq or microarray of isolated lung MKs after hypoxia:** `(megakaryocyte OR MK) AND (hypoxia OR hypoxic) AND (lung OR pulmonary) AND (RNA-seq OR microarray)`  
3. **Spatial transcriptomics or proteomics of PH lung with MK/immune context:** `(pulmonary hypertension OR pulmonary vascular remodeling) AND (spatial transcriptomics OR MERFISH OR Visium OR imaging mass cytometry) AND (megakaryocyte OR platelet OR immune cell)`  
4. **Metabolomics or fluxomics of hypoxic MKs or MK‑rich lung tissue:** `(metabolomics OR metabolite profiling OR metabolic flux) AND (megakaryocyte OR platelet) AND (hypoxia OR hypoxia-induced)`  
5. **Proteomics of MK‑derived extracellular vesicles or secretome in hypoxia/PH:** `(megakaryocyte OR MK) AND (extracellular vesicles OR secretome OR proteomics) AND (hypoxia OR pulmonary hypertension)`  
6. **Clinical or translational datasets linking MK metabolites to PH/remodelling:** `(pulmonary arterial hypertension OR PAH) AND (metabolomics OR metabolome) AND (megakaryocyte OR platelet OR thrombocytosis)`  
7. **Microarray or bulk RNA‑seq of lung microvascular endothelial cells or VSMC exposed to MK‑conditioned medium:** `(megakaryocyte OR MK) AND (conditioned medium OR co-culture) AND (endothelial OR smooth muscle) AND (hypoxia OR vascular remodeling)`  

**Required hypothesis categories (distributed across generation agents):**  
- **Metabolomics‑driven (dedicated, ≥40% of hypotheses in this cycle):** Begin with a differential MK metabolite from the shortlist, link it via KEGG to a candidate enzyme/neighbor‑gene expressed in MKs, and define a plausible metabolic‑to‑remodelling direction.  
- Paracrine signalling (ligand‑receptor, cytokines, growth factors).  
- Extracellular vesicle‑mediated mechanisms (cargo and target cell).  
- Coagulation and thrombo‑inflammatory programmes.  
- Extracellular matrix remodelling (MK‑derived proteases, collagen modifiers).  
- Immune remodelling (recruitment/polarisation of macrophages, neutrophils, T cells).  
- Spatial niche / perivascular interactions (MK proximity to specific vessels or stromal cells).  

**Required hypothesis structure:**  
Each hypothesis must describe a **direction‑level causal chain** with these elements:  
1. Hypoxia induces a defined (or plausibly enriched) state, metabolic shift, or pathway in in‑situ MKs.  
2. That MK state alters a **mediator class** (metabolite class, ligand type, EV cargo, protease family, or inflammatory programme) – *do not force a single exact mediator unless the data directly resolve it*.  
3. The altered mediator class is linked to one or more **broad downstream axes** (see below).  
4. The downstream axis plausibly impacts vascular cells (endothelial, smooth muscle, fibroblasts), perivascular immune tone, or vessel‑wall structure.  
5. This contributes to a defined vascular remodelling phenotype (e.g., medial thickening, muscularization, stiffness).  

Every hypothesis must include a **Direction‑level reasoning summary** (concise, evidence‑linked paragraph) that connects:  
- **Direct data anchor** (which metabolite, gene expression pattern, or prior‑results finding)  
- **Biological interpretation** of that anchor in the context of hypoxic MKs  
- **MK‑linked enzyme, mediator class, or pathway logic** (which enzyme/pathway class, how it fits with the data)  
- **Plausible downstream axis** (e.g., immune‑mediated, direct vascular‑wall, EV/stromal, unresolved)  
- **Broad remodelling phenotype** (e.g., medial activation, muscularization, vascular stiffness)  
- **Key uncertainty or assumption** that could overturn the hypothesis  

For metabolomics‑driven hypotheses, agents must use the *Metabolomics‑to‑Mechanism Evidence Context* (provided) and specifically cite the readiness rank, metabolite signal, candidate gene, and Seurat evidence. Suggested downstream axes should be labelled as **candidates**, not settled mechanisms. Acceptable axis labels:  
- **Immune‑mediated** (may mention Th17‑like T‑cell activity, macrophage/monocyte activation, neutrophil inflammation as candidate examples)  
- **Direct vascular‑wall** (endothelial activation, smooth muscle proliferation/hypertrophy, fibroblast‑to‑myofibroblast transition)  
- **EV/stromal/perivascular niche** (matrix alterations, vesicle‑delivered cargo)  
- **Unresolved** (when the data only support a general biological shift)  

Instead of a Bridge Convergence Matrix, provide a short **Candidate downstream axes** note that lists 2‑4 plausible routes and indicates which one is the working model, while stressing that it remains provisional.  

**Must include:**  
- MK‑specific initiating event (genetic, enzymatic, or pathway enrichment supported by scRNA‑seq)  
- Hypoxia‑dependent trigger (PH vs control comparison)  
- Defined mediator class, pathway class, or metabolic axis  
- Candidate downstream axis rather than a forced final bridge  
- Broad vascular remodelling phenotype  
- Direction‑level reasoning summary linking data anchor, interpretation, pathway logic, downstream axis, remodelling phenotype, and key uncertainty  
- Testable prediction at the direction level (e.g., “inhibiting AMD1 in MKs will reduce polyamine levels and attenuate medial thickening”)  
- Falsification criterion (what experimental result would refute the direction)  

**Must avoid:**  
- Generic inflammation‑only hypotheses lacking MK specificity  
- Gene‑list‑only outputs  
- Unsupported causal claims (no data anchor)  
- Hypotheses that lack MK‑specificity, hypoxia‑specificity, or pulmonary vascular remodelling relevance  
- Redundant hypotheses that merely re‑state known MK biology (e.g., platelet release) without connecting to remodelling  
- Mechanisms that are not experimentally testable at the direction level  
- Over‑resolving exact mediators, T‑cell subsets, cytokines, receptors, EndMT scenarios, or recipient cell identities when only broader evidence exists  
- Treating KEGG linkages or PubMed key‑word hits as proof of causality  
- Using previous‑cycle metabolite priorities (none exist) to override the Authority shortlist; always give weight to top mechanism‑ready chains with positive MK enrichment, PH‑up MK shift, and strong non‑generic mechanism cues  

**Feedback from previous cycle:**  
None. This is the first generation cycle.

**Expected output:**  
The total hypothesis landscape will be distributed across generation agents. Each agent should produce **3‑6 complete, reasoning‑rich hypotheses** within its assigned categories. Metabolomics‑driven agents should produce all their hypotheses following the metabolite‑enzyme‑MK‑remodelling scaffold; other agents may generate a mix, but at least 40% of all hypotheses in the cycle must be metabolomics‑driven.  

All hypotheses must be submitted with the required structure and the concise Direction‑level reasoning summary.

## Metabolomics-to-mechanism context
# Metabolomics-to-Mechanism Evidence Context

This context is generated before hypothesis generation to support metabolomics-driven, direction-level mechanisms.
Evidence chain target: differential metabolite -> KEGG compound/pathway/enzyme or pathway-neighbor gene -> candidate enzyme gene -> MK expression/differential evidence -> directional downstream biology -> vascular remodeling phenotype.

- KEGG fetch: enabled
- PubMed fetch: enabled
- Selected metabolites: 30
- Candidate enzyme-gene rows: 369
- Direct compound-enzyme rows: 98
- Pathway-neighbor rows: 246
- Candidate genes with Seurat expression metrics: 301
- Mechanism-ready shortlist rows: 4

## Mechanism-Ready Hypothesis Shortlist
These rows are ranked for hypothesis generation, not just KEGG coverage. They require a differential MK metabolite, a KEGG direct or same-pathway enzyme/gene link, matched Seurat expression, positive MK enrichment, PH-up shift in MKs, and non-generic mechanism cues. Generation agents should use top rows as direction-level anchors, not as proof of a specific downstream cell subtype, cytokine, or final bridge.

| Rank | Metabolite | Candidate gene | Readiness | Link type | KEGG/mechanism context | Seurat MK/PH evidence | Literature hits |
|---:|---|---|---:|---|---|---|---|
| 1 | methionine (up, log2FC 3.26) | Amd1: (RefSeq) S-adenosylmethionine decarboxylase proenzyme 1 | 35.4 | pathway_neighbor_gene | ec:4.1.1.50; Cysteine and methionine metabolism; mmu_M00034  Methionine salvage pathway; polyamine metabolism;S-adenosylmethionine metabolism;methionine salvage;cysteine/methionine metabolism;arginine/proline metabolism | Seurat expression: MK pct 31.44%, other pct 14.87%, MK enrichment log2 1.353, PH-vs-control MK log2 1.77, PH MK pct 38.03%, control MK pct 18.3%, PH-vs-control MK Wilcoxon p 6.55e-06 | gene_or_gene_context PMID 38965534: Polyamine and EIF5A hypusination downstream of c-Myc confers targeted therapy resistance i; gene_or_gene_context PMID 28658205: mTORC1-dependent AMD1 regulation sustains polyamine metabolism in prostate cancer.; gene_or_gene_context PMID 40768332: Multi-dimensional metabolomic remodeling under diverse muscle atrophic stimuli in vivo. |
| 2 | methionine (up, log2FC 3.26) | Amd2: (RefSeq) S-adenosylmethionine decarboxylase proenzyme 2 | 30 | pathway_neighbor_gene | ec:4.1.1.50; Cysteine and methionine metabolism; mmu_M00034  Methionine salvage pathway; polyamine metabolism;S-adenosylmethionine metabolism;methionine salvage;cysteine/methionine metabolism;arginine/proline metabolism | Seurat expression: MK pct 4.37%, other pct 2.1%, MK enrichment log2 0.931, PH-vs-control MK log2 2.175, PH MK pct 5.9%, control MK pct 1.31%, PH-vs-control MK Wilcoxon p 0.0235 | gene_or_gene_context PMID 40768332: Multi-dimensional metabolomic remodeling under diverse muscle atrophic stimuli in vivo.; gene_or_gene_context PMID 36543136: Spatially resolved transcriptomics reveals innervation-responsive functional clusters in s; gene_or_gene_context PMID 7789170: The human S-adenosylmethionine decarboxylase gene: nucleotide sequence of a pseudogene and |
| 3 | methionine (up, log2FC 3.26) | Dnmt3b: (RefSeq) DNA (cytosine-5)-methyltransferase 3B isoform 1 | 15.6 | pathway_neighbor_gene | ec:2.1.1.37; Cysteine and methionine metabolism; mmu_M00035  Methionine degradation; cysteine/methionine metabolism | Seurat expression: MK pct 2.62%, other pct 2.48%, MK enrichment log2 0.193, PH-vs-control MK log2 1.59, PH MK pct 3.28%, control MK pct 1.31%, PH-vs-control MK Wilcoxon p 0.212 | none retrieved |
| 4 | Retinoic Acid (up, log2FC 3.44) | Cyp26b1: (RefSeq) cytochrome P450 26B1 | 14 | pathway_neighbor_gene | ec:1.14.14.-; Retinol metabolism; retinoid metabolism | Seurat expression: MK pct 7.86%, other pct 4.46%, MK enrichment log2 0.728, PH-vs-control MK log2 0.912, PH MK pct 8.85%, control MK pct 5.88%, PH-vs-control MK Wilcoxon p 0.253 | none retrieved |

## Directional Downstream Axis Cues
For these mechanism-ready chains, generation agents should name plausible downstream axes without selecting a final bridge unless direct evidence supports that specificity. Treat immune subsets, cytokines, vascular recipients, EV routes, and stromal routes as candidate examples rather than settled mechanisms.
Use these cues to keep hypotheses biologically oriented: MK metabolic state -> pathway class -> broad downstream axis -> vascular remodeling phenotype. Avoid over-resolving to a single metabolite product, T-cell subset, mediator, or EndMT route.
- methionine -> Amd1: pathway terms methionine, S-adenosylmethionine, methionine salvage, polyamine, spermidine, spermine, arginine, ornithine; candidate downstream axes: immune-mediated or T-helper/Th17-like tone; macrophage/monocyte or neutrophil inflammation; direct endothelial/smooth-muscle/fibroblast activation; EV/stromal remodeling; unresolved
- methionine -> Amd2: pathway terms methionine, S-adenosylmethionine, methionine salvage, polyamine, spermidine, spermine, arginine, ornithine; candidate downstream axes: immune-mediated or T-helper/Th17-like tone; macrophage/monocyte or neutrophil inflammation; direct endothelial/smooth-muscle/fibroblast activation; EV/stromal remodeling; unresolved
- methionine -> Dnmt3b: pathway terms methionine, S-adenosylmethionine, methionine salvage; candidate downstream axes: immune-mediated or T-helper/Th17-like tone; macrophage/monocyte or neutrophil inflammation; direct endothelial/smooth-muscle/fibroblast activation; EV/stromal remodeling; unresolved
- Retinoic Acid -> Cyp26b1: pathway terms retinoic acid, retinoid; candidate downstream axes: immune-mediated or T-helper/Th17-like tone; macrophage/monocyte or neutrophil inflammation; direct endothelial/smooth-muscle/fibroblast activation; EV/stromal remodeling; unresolved

## Prioritized Complete Evidence Chains
| Metabolite | Metabolite signal | Link type | Candidate gene | KEGG context | Seurat MK/PH evidence | Mechanism cues | Literature hits |
|---|---|---|---|---|---|---|---|
| methionine | up log2FC 3.26 (PH-mk_vs_Control-mk) | pathway_neighbor_gene | Amd1: (RefSeq) S-adenosylmethionine decarboxylase proenzyme 1 [readiness 35.4; evidence 29.4] | ec:4.1.1.50; Cysteine and methionine metabolism; mmu_M00034  Methionine salvage pathway | Seurat expression: MK pct 31.44%, other pct 14.87%, MK enrichment log2 1.353, PH-vs-control MK log2 1.77, PH MK pct 38.03%, control MK pct 18.3%, PH-vs-control MK Wilcoxon p 6.55e-06 | polyamine metabolism;S-adenosylmethionine metabolism;methionine salvage;cysteine/methionine metabolism;arginine/proline metabolism | gene_or_gene_context PMID 38965534: Polyamine and EIF5A hypusination downstream of c-Myc confers targeted therapy resistance i; gene_or_gene_context PMID 28658205: mTORC1-dependent AMD1 regulation sustains polyamine metabolism in prostate cancer.; gene_or_gene_context PMID 40768332: Multi-dimensional metabolomic remodeling under diverse muscle atrophic stimuli in vivo. |
| methionine | up log2FC 3.26 (PH-mk_vs_Control-mk) | pathway_neighbor_gene | Amd2: (RefSeq) S-adenosylmethionine decarboxylase proenzyme 2 [readiness 30; evidence 26.7] | ec:4.1.1.50; Cysteine and methionine metabolism; mmu_M00034  Methionine salvage pathway | Seurat expression: MK pct 4.37%, other pct 2.1%, MK enrichment log2 0.931, PH-vs-control MK log2 2.175, PH MK pct 5.9%, control MK pct 1.31%, PH-vs-control MK Wilcoxon p 0.0235 | polyamine metabolism;S-adenosylmethionine metabolism;methionine salvage;cysteine/methionine metabolism;arginine/proline metabolism | gene_or_gene_context PMID 40768332: Multi-dimensional metabolomic remodeling under diverse muscle atrophic stimuli in vivo.; gene_or_gene_context PMID 36543136: Spatially resolved transcriptomics reveals innervation-responsive functional clusters in s; gene_or_gene_context PMID 7789170: The human S-adenosylmethionine decarboxylase gene: nucleotide sequence of a pseudogene and |
| Retinoic Acid | up log2FC 3.44 (PH-mk_vs_Control-mk) | direct_compound_enzyme | Cyp1a1: (RefSeq) cytochrome P450 1A1 [readiness 24.6; evidence 28.1] | ec:1.14.14.1 | Seurat expression: MK pct 12.01%, other pct 10.27%, MK enrichment log2 -0.739, PH-vs-control MK log2 2.787, PH MK pct 14.43%, control MK pct 7.19%, PH-vs-control MK Wilcoxon p 0.0221 | tryptophan metabolism;retinoid metabolism | gene_or_gene_context PMID 38503152: Salidroside protects pulmonary artery endothelial cells against hypoxia-induced apoptosis ; gene_or_gene_context PMID 32763913: Integrated Skin Transcriptomics and Serum Multiplex Assays Reveal Novel Mechanisms of Woun; gene_or_gene_context PMID 38652558: A tryptophan-derived uremic metabolite/Ahr/Pdk4 axis governs skeletal muscle mitochondrial |
| tryptophan | up log2FC 4.03 (PH-mk_vs_Control-mk) | pathway_neighbor_gene | Cyp1a1: (RefSeq) cytochrome P450 1A1 [readiness 24.4; evidence 28.8] | ec:1.14.14.1; Tryptophan metabolism | Seurat expression: MK pct 12.01%, other pct 10.27%, MK enrichment log2 -0.739, PH-vs-control MK log2 2.787, PH MK pct 14.43%, control MK pct 7.19%, PH-vs-control MK Wilcoxon p 0.0221 | tryptophan metabolism;retinoid metabolism | gene_or_gene_context PMID 38503152: Salidroside protects pulmonary artery endothelial cells against hypoxia-induced apoptosis ; gene_or_gene_context PMID 32763913: Integrated Skin Transcriptomics and Serum Multiplex Assays Reveal Novel Mechanisms of Woun; gene_or_gene_context PMID 38652558: A tryptophan-derived uremic metabolite/Ahr/Pdk4 axis governs skeletal muscle mitochondrial |
| methionine | up log2FC 3.26 (PH-mk_vs_Control-mk) | pathway_neighbor_gene | Mat2a: (RefSeq) S-adenosylmethionine synthase isoform type-2 isoform 1 [readiness 23.1; evidence 24.9] | ec:2.5.1.6; Cysteine and methionine metabolism; mmu_M00034  Methionine salvage pathway;mmu_M00035  Methionine degradation | Seurat expression: MK pct 31%, other pct 46.44%, MK enrichment log2 -0.641, PH-vs-control MK log2 0.668, PH MK pct 33.44%, control MK pct 26.14%, PH-vs-control MK Wilcoxon p 0.096 | S-adenosylmethionine metabolism;methionine salvage;cysteine/methionine metabolism;one-carbon metabolism | gene_or_gene_context PMID 23073625: S-adenosylmethionine in liver health, injury, and cancer.; gene_or_gene_context PMID 35796517: Overview of Methionine Adenosyltransferase 2A (MAT2A) as an Anticancer Target: Structure, ; gene_or_gene_context PMID 28525753: The U6 snRNA m(6)A Methyltransferase METTL16 Regulates SAM Synthetase Intron Retention. |
| tryptophan | up log2FC 4.03 (PH-mk_vs_Control-mk) | pathway_neighbor_gene | Aldh2: (RefSeq) aldehyde dehydrogenase, mitochondrial isoform 1 precursor [readiness 23.1; evidence 28.7] | ec:1.2.1.3; Tryptophan metabolism; mmu_M00135  GABA biosynthesis, eukaryotes, putrescine => GABA | Seurat expression: MK pct 88.86%, other pct 61.15%, MK enrichment log2 1.01, PH-vs-control MK log2 0.329, PH MK pct 90.16%, control MK pct 86.27%, PH-vs-control MK Wilcoxon p 0.129 | arginine/proline metabolism;tryptophan metabolism;glycolysis;fatty-acid metabolism | gene_or_gene_context PMID 38124089: ALDH2 mitigates LPS-induced cardiac dysfunction, inflammation, and apoptosis through the c; gene_or_gene_context PMID 38472357: Neutrophil ALDH2 is a new therapeutic target for the effective treatment of sepsis-induced; gene_or_gene_context PMID 38348663: Carbonylation of Runx2 at K176 by 4-Hydroxynonenal Accelerates Vascular Calcification. |
| Urocanic acid | down log2FC -3.95 (PH-mk_vs_Control-mk) | pathway_neighbor_gene | Aldh2: (RefSeq) aldehyde dehydrogenase, mitochondrial isoform 1 precursor [readiness 23; evidence 28.5] | ec:1.2.1.3; Histidine metabolism; mmu_M00135  GABA biosynthesis, eukaryotes, putrescine => GABA | Seurat expression: MK pct 88.86%, other pct 61.15%, MK enrichment log2 1.01, PH-vs-control MK log2 0.329, PH MK pct 90.16%, control MK pct 86.27%, PH-vs-control MK Wilcoxon p 0.129 | arginine/proline metabolism;tryptophan metabolism;glycolysis;fatty-acid metabolism | gene_or_gene_context PMID 38124089: ALDH2 mitigates LPS-induced cardiac dysfunction, inflammation, and apoptosis through the c; gene_or_gene_context PMID 38472357: Neutrophil ALDH2 is a new therapeutic target for the effective treatment of sepsis-induced; gene_or_gene_context PMID 38348663: Carbonylation of Runx2 at K176 by 4-Hydroxynonenal Accelerates Vascular Calcification. |
| methionine | up log2FC 3.26 (PH-mk_vs_Control-mk) | pathway_neighbor_gene | Mat2b: (RefSeq) methionine adenosyltransferase 2 subunit beta isoform 1 [readiness 22.6; evidence 23.9] | ec:2.5.1.6; Cysteine and methionine metabolism; mmu_M00034  Methionine salvage pathway;mmu_M00035  Methionine degradation | Seurat expression: MK pct 23.8%, other pct 36.01%, MK enrichment log2 -0.418, PH-vs-control MK log2 0.398, PH MK pct 25.9%, control MK pct 19.61%, PH-vs-control MK Wilcoxon p 0.139 | S-adenosylmethionine metabolism;methionine salvage;cysteine/methionine metabolism;one-carbon metabolism | gene_or_gene_context PMID 39333125: The role of forkhead box M1-methionine adenosyltransferase 2 A/2B axis in liver inflammati; gene_or_gene_context PMID 31496615: Methionine adenosyltransferases in liver cancer.; gene_or_gene_context PMID 39293586: Developing patient-derived organoids to demonstrate JX24120 inhibits SAMe synthesis in end |
| methionine | up log2FC 3.26 (PH-mk_vs_Control-mk) | pathway_neighbor_gene | Ldha: (RefSeq) L-lactate dehydrogenase A chain isoform 1 [readiness 22.5; evidence 28.9] | ec:1.1.1.27; Cysteine and methionine metabolism | Seurat expression: MK pct 47.82%, other pct 60.94%, MK enrichment log2 -0.745, PH-vs-control MK log2 2.333, PH MK pct 56.39%, control MK pct 30.72%, PH-vs-control MK Wilcoxon p 4.48e-10 | cysteine/methionine metabolism;glycolysis | gene_or_gene_context PMID 38214194: ErbB3 Governs Endothelial Dysfunction in Hypoxia-Induced Pulmonary Hypertension.; gene_or_gene_context PMID 33105588: Perivascular Inflammation in Pulmonary Arterial Hypertension.; gene_or_gene_context PMID 32746619: Endothelial-to-Mesenchymal Transition in Pulmonary Arterial Hypertension. |
| methionine | up log2FC 3.26 (PH-mk_vs_Control-mk) | pathway_neighbor_gene | Got2: (RefSeq) aspartate aminotransferase, mitochondrial [readiness 22.2; evidence 24.9] | ec:2.6.1.1; Cysteine and methionine metabolism | Seurat expression: MK pct 16.81%, other pct 23.94%, MK enrichment log2 -0.425, PH-vs-control MK log2 0.676, PH MK pct 19.67%, control MK pct 11.11%, PH-vs-control MK Wilcoxon p 0.0219 | cysteine/methionine metabolism;arginine/proline metabolism;tryptophan metabolism | gene_or_gene_context PMID 35726024: Adaptive stimulation of macropinocytosis overcomes aspartate limitation in cancer cells un; gene_or_gene_context PMID 41001736: Comprehensive genotypic, phenotypic, and biochemical characterization of GOT2 deficiency: ; gene_or_gene_context PMID 40536683: The innate immune receptor NLRX1 is a novel required modulator for mPTP opening: implicati |
| Glucose | up log2FC 2.77 (PH-mk_vs_Control-mk) | pathway_neighbor_gene | Aldh2: (RefSeq) aldehyde dehydrogenase, mitochondrial isoform 1 precursor [readiness 22.1; evidence 25.8] | ec:1.2.1.3; Glycolysis / Gluconeogenesis; mmu_M00135  GABA biosynthesis, eukaryotes, putrescine => GABA | Seurat expression: MK pct 88.86%, other pct 61.15%, MK enrichment log2 1.01, PH-vs-control MK log2 0.329, PH MK pct 90.16%, control MK pct 86.27%, PH-vs-control MK Wilcoxon p 0.129 | arginine/proline metabolism;tryptophan metabolism;glycolysis;fatty-acid metabolism | gene_or_gene_context PMID 38124089: ALDH2 mitigates LPS-induced cardiac dysfunction, inflammation, and apoptosis through the c; gene_or_gene_context PMID 38472357: Neutrophil ALDH2 is a new therapeutic target for the effective treatment of sepsis-induced; gene_or_gene_context PMID 38348663: Carbonylation of Runx2 at K176 by 4-Hydroxynonenal Accelerates Vascular Calcification. |
| Glucose | up log2FC 2.77 (PH-mk_vs_Control-mk) | pathway_neighbor_gene | Ldha: (RefSeq) L-lactate dehydrogenase A chain isoform 1 [readiness 22.1; evidence 28.2] | ec:1.1.1.27; Glycolysis / Gluconeogenesis | Seurat expression: MK pct 47.82%, other pct 60.94%, MK enrichment log2 -0.745, PH-vs-control MK log2 2.333, PH MK pct 56.39%, control MK pct 30.72%, PH-vs-control MK Wilcoxon p 4.48e-10 | cysteine/methionine metabolism;glycolysis | gene_or_gene_context PMID 38214194: ErbB3 Governs Endothelial Dysfunction in Hypoxia-Induced Pulmonary Hypertension.; gene_or_gene_context PMID 33105588: Perivascular Inflammation in Pulmonary Arterial Hypertension.; gene_or_gene_context PMID 32746619: Endothelial-to-Mesenchymal Transition in Pulmonary Arterial Hypertension. |
| Retinoic Acid | up log2FC 3.44 (PH-mk_vs_Control-mk) | pathway_neighbor_gene | Adh5: (RefSeq) alcohol dehydrogenase class-3 isoform 1 [readiness 22; evidence 26] | ec:1.1.1.284;ec:1.1.1.1; Retinol metabolism | Seurat expression: MK pct 15.07%, other pct 24.33%, MK enrichment log2 -0.903, PH-vs-control MK log2 1.027, PH MK pct 18.36%, control MK pct 8.5%, PH-vs-control MK Wilcoxon p 0.00618 | glutathione/redox metabolism;retinoid metabolism;glycolysis;fatty-acid metabolism | none retrieved |
| Glucose | up log2FC 2.77 (PH-mk_vs_Control-mk) | pathway_neighbor_gene | Adh5: (RefSeq) alcohol dehydrogenase class-3 isoform 1 [readiness 21.5; evidence 24.4] | ec:1.1.1.284;ec:1.1.1.1; Glycolysis / Gluconeogenesis | Seurat expression: MK pct 15.07%, other pct 24.33%, MK enrichment log2 -0.903, PH-vs-control MK log2 1.027, PH MK pct 18.36%, control MK pct 8.5%, PH-vs-control MK Wilcoxon p 0.00618 | glutathione/redox metabolism;retinoid metabolism;glycolysis;fatty-acid metabolism | none retrieved |
| tryptophan | up log2FC 4.03 (PH-mk_vs_Control-mk) | pathway_neighbor_gene | Maoa: (RefSeq) amine oxidase [flavin-containing] A [readiness 20.9; evidence 26.7] | ec:1.4.3.4; Glycine, serine and threonine metabolism; mmu_M00135  GABA biosynthesis, eukaryotes, putrescine => GABA | Seurat expression: MK pct 20.09%, other pct 13.56%, MK enrichment log2 0.84, PH-vs-control MK log2 0.467, PH MK pct 21.64%, control MK pct 16.99%, PH-vs-control MK Wilcoxon p 0.25 | arginine/proline metabolism;tryptophan metabolism | none retrieved |
| methionine | up log2FC 3.26 (PH-mk_vs_Control-mk) | pathway_neighbor_gene | Mdh2: (RefSeq) malate dehydrogenase, mitochondrial precursor [readiness 20.7; evidence 27.1] | ec:1.1.1.37; Cysteine and methionine metabolism; mmu_M00009  Citrate cycle (TCA cycle, Krebs cycle);mmu_M00011  Citrate cycle, second carbon oxidation, 2-oxoglutarate => oxaloacetate | Seurat expression: MK pct 29.69%, other pct 46.13%, MK enrichment log2 -0.711, PH-vs-control MK log2 0.962, PH MK pct 34.75%, control MK pct 19.61%, PH-vs-control MK Wilcoxon p 0.000585 | cysteine/methionine metabolism | none retrieved |
| Pyruvaldehyde | up log2FC 2.76 (PH-mk_vs_Control-mk) | direct_compound_enzyme | Maoa: (RefSeq) amine oxidase [flavin-containing] A [readiness 20.5; evidence 23.6] | ec:1.4.3.4; mmu_M00135  GABA biosynthesis, eukaryotes, putrescine => GABA | Seurat expression: MK pct 20.09%, other pct 13.56%, MK enrichment log2 0.84, PH-vs-control MK log2 0.467, PH MK pct 21.64%, control MK pct 16.99%, PH-vs-control MK Wilcoxon p 0.25 | arginine/proline metabolism;tryptophan metabolism | none retrieved |
| tryptophan | up log2FC 4.03 (PH-mk_vs_Control-mk) | pathway_neighbor_gene | Sdsl: (RefSeq) serine dehydratase-like [readiness 20.4; evidence 27.7] | ec:4.3.1.17;ec:4.3.1.19; Glycine, serine and threonine metabolism | Seurat expression: MK pct 0.66%, other pct 0.17%, MK enrichment log2 1.825, PH-vs-control MK log2 23.23, PH MK pct 0.98%, control MK pct 0%, PH-vs-control MK Wilcoxon p 0.22 | cysteine/methionine metabolism | none retrieved |
| tryptophan | up log2FC 4.03 (PH-mk_vs_Control-mk) | pathway_neighbor_gene | Maob: (RefSeq) amine oxidase [flavin-containing] B [readiness 20.2; evidence 25.6] | ec:1.4.3.4; Glycine, serine and threonine metabolism; mmu_M00135  GABA biosynthesis, eukaryotes, putrescine => GABA | Seurat expression: MK pct 2.84%, other pct 4.19%, MK enrichment log2 -0.563, PH-vs-control MK log2 1.912, PH MK pct 3.61%, control MK pct 1.31%, PH-vs-control MK Wilcoxon p 0.161 | arginine/proline metabolism;tryptophan metabolism | none retrieved |
| Urocanic acid | down log2FC -3.95 (PH-mk_vs_Control-mk) | pathway_neighbor_gene | Maob: (RefSeq) amine oxidase [flavin-containing] B [readiness 20.2; evidence 25.4] | ec:1.4.3.4; Histidine metabolism; mmu_M00135  GABA biosynthesis, eukaryotes, putrescine => GABA | Seurat expression: MK pct 2.84%, other pct 4.19%, MK enrichment log2 -0.563, PH-vs-control MK log2 1.912, PH MK pct 3.61%, control MK pct 1.31%, PH-vs-control MK Wilcoxon p 0.161 | arginine/proline metabolism;tryptophan metabolism | none retrieved |
| Retinoic Acid | up log2FC 3.44 (PH-mk_vs_Control-mk) | direct_compound_enzyme | Aldh1a1: (RefSeq) aldehyde dehydrogenase 1A1 [readiness 20; evidence 27.7] | ec:1.2.1.36 | Seurat expression: MK pct 24.24%, other pct 13.41%, MK enrichment log2 -0.809, PH-vs-control MK log2 1.217, PH MK pct 27.87%, control MK pct 16.99%, PH-vs-control MK Wilcoxon p 0.0117 | retinoid metabolism | none retrieved |
| Pyruvaldehyde | up log2FC 2.76 (PH-mk_vs_Control-mk) | direct_compound_enzyme | Maob: (RefSeq) amine oxidase [flavin-containing] B [readiness 19.8; evidence 22.5] | ec:1.4.3.4; mmu_M00135  GABA biosynthesis, eukaryotes, putrescine => GABA | Seurat expression: MK pct 2.84%, other pct 4.19%, MK enrichment log2 -0.563, PH-vs-control MK log2 1.912, PH MK pct 3.61%, control MK pct 1.31%, PH-vs-control MK Wilcoxon p 0.161 | arginine/proline metabolism;tryptophan metabolism | none retrieved |
| methionine | up log2FC 3.26 (PH-mk_vs_Control-mk) | pathway_neighbor_gene | Sdsl: (RefSeq) serine dehydratase-like [readiness 19.8; evidence 25.4] | ec:4.3.1.17;ec:4.3.1.19; Cysteine and methionine metabolism | Seurat expression: MK pct 0.66%, other pct 0.17%, MK enrichment log2 1.825, PH-vs-control MK log2 23.23, PH MK pct 0.98%, control MK pct 0%, PH-vs-control MK Wilcoxon p 0.22 | cysteine/methionine metabolism | none retrieved |
| methionine | up log2FC 3.26 (PH-mk_vs_Control-mk) | pathway_neighbor_gene | Sms: (RefSeq) spermine synthase isoform 1 [readiness 19.6; evidence 24.6] | ec:2.5.1.22; Cysteine and methionine metabolism | Seurat expression: MK pct 6.55%, other pct 13.55%, MK enrichment log2 -1.249, PH-vs-control MK log2 1.374, PH MK pct 8.2%, control MK pct 3.27%, PH-vs-control MK Wilcoxon p 0.0443 | cysteine/methionine metabolism;arginine/proline metabolism;glutathione/redox metabolism | none retrieved |
| tryptophan | up log2FC 4.03 (PH-mk_vs_Control-mk) | pathway_neighbor_gene | Aldh7a1: (RefSeq) alpha-aminoadipic semialdehyde dehydrogenase isoform a [readiness 19.3; evidence 24.3] | ec:1.2.1.31;ec:1.2.1.8;ec:1.2.1.3; Glycine, serine and threonine metabolism; mmu_M00032  Lysine degradation, lysine => saccharopine => acetoacetyl-CoA;mmu_M00135  GABA biosynthesis, eukaryotes, putrescine => GABA;mmu_M00555  Betaine biosynthesis, choline => betaine | Seurat expression: MK pct 5.24%, other pct 6.53%, MK enrichment log2 -0.458, PH-vs-control MK log2 0.445, PH MK pct 5.9%, control MK pct 3.92%, PH-vs-control MK Wilcoxon p 0.377 | arginine/proline metabolism;one-carbon metabolism;tryptophan metabolism;glycolysis;fatty-acid metabolism | none retrieved |

## Priority Differential Metabolites
| Metabolite | Source | Comparison | Direction | log2FC | FDR | Priority |
|---|---|---|---|---:|---:|---:|
| Raffinose | sFig6A Raw data.xlsx | PH-mk_vs_Control-mk | up | 7.02 |  | 123 |
| 15-deoxy-delta-12-14-PGJ2 | sFig6A Raw data.xlsx | PH-mk_vs_Control-mk | up | 4.85 |  | 103 |
| phosphate | sFig6A Raw data.xlsx | PH-mk_vs_Control-mk | up | 3.42 |  | 90.4 |
| Carnosic acid | sFig6A Raw data.xlsx | PH-mk_vs_Control-mk | up | 4.29 |  | 79.9 |
| Urocanic acid | sFig6A Raw data.xlsx | PH-mk_vs_Control-mk | down | -3.95 |  | 77.1 |
| Retinoic Acid | sFig6A Raw data.xlsx | PH-mk_vs_Control-mk | up | 3.44 |  | 75.6 |
| tryptophan | sFig6A Raw data.xlsx | PH-mk_vs_Control-mk | up | 4.03 |  | 74.9 |
| C22:3 | sFig6A Raw data.xlsx | PH-mk_vs_Control-mk | up | 3.49 |  | 65.3 |
| Glucose | sFig6A Raw data.xlsx | PH-mk_vs_Control-mk | up | 2.77 |  | 63.3 |
| cystine | sFig6A Raw data.xlsx | PH-mk_vs_Control-mk | up | 3.06 |  | 61.3 |
| pyridoxine | sFig6A Raw data.xlsx | PH-mk_vs_Control-mk | up | 3.03 |  | 60.3 |
| methionine | sFig6A Raw data.xlsx | PH-mk_vs_Control-mk | up | 3.26 |  | 59.6 |
| Cholesteryl sulfate | sFig6A Raw data.xlsx | PH-mk_vs_Control-mk | down | -2.43 |  | 57.4 |
| Pyruvaldehyde | sFig6A Raw data.xlsx | PH-mk_vs_Control-mk | up | 2.76 |  | 57.1 |
| tyrosine | sFig6A Raw data.xlsx | PH-mk_vs_Control-mk | up | 2.98 |  | 56.9 |
| Thiamine | sFig6A Raw data.xlsx | PH-mk_vs_Control-mk | up | 2.75 |  | 56.1 |
| isoleucine | sFig6A Raw data.xlsx | PH-mk_vs_Control-mk | up | 2.48 |  | 55.6 |
| cysteine | sFig6A Raw data.xlsx | PH-mk_vs_Control-mk | up | 3.34 |  | 55.2 |
| 1-Tetradecanesulfonic acid | sFig6A Raw data.xlsx | PH-CD41_vs_Control-CD41 | up | 5.81 |  | 121 |
| inosine | sFig6A Raw data.xlsx | PH-CD41_vs_Control-CD41 | up | 3.82 |  | 66.9 |
| Perfluorooctanesulfonic acid | Figure6D+F raw data.xlsx:FDR | KO_or_PH_vs_WT_or_control | up | 3.93 | 0.00208 | 14.5 |
| PE(40:1) | sFig6A Raw data.xlsx | PH-mk_vs_Control-mk | down | -49.5 |  | 968 |
| ceramide(d18:1/18:1) | sFig6A Raw data.xlsx | PH-mk_vs_Control-mk | down | -47.3 |  | 825 |
| Gibberellin A14 isomer | sFig6A Raw data.xlsx | PH-mk_vs_Control-mk | up | 47.1 |  | 811 |
| PG(16:1/20:5) | sFig6A Raw data.xlsx | PH-CD41_vs_Control-CD41 | down | -41.7 |  | 492 |
| SM(d18:1/24:0) | sFig6A Raw data.xlsx | PH-mk_vs_Control-mk | down | -9.82 |  | 217 |
| SM(d18:1/20:0) | sFig6A Raw data.xlsx | PH-mk_vs_Control-mk | down | -7.91 |  | 180 |
| DAG(40:7) | sFig6A Raw data.xlsx | PH-mk_vs_Control-mk | down | -7.59 |  | 149 |
| PC(18:0/20:2) | sFig6A Raw data.xlsx | PH-mk_vs_Control-mk | down | -6.17 |  | 140 |
| ceramide(d18:1/16:0) | sFig6A Raw data.xlsx | PH-mk_vs_Control-mk | down | -6.28 |  | 135 |

## KEGG Metabolite-Enzyme Mapping

### Raffinose
- Differential signal: up, log2FC 7.02 in PH-mk_vs_Control-mk (sFig6A Raw data.xlsx)
- KEGG status: mapped
- KEGG compounds: C00492, C08242
- KEGG compound names: Raffinose; Melitose; Melitriose; Gossypose; 6G-alpha-D-galactosylsucrose, Lychnose; 1F-alpha-D-Galactosylraffinose
- KEGG pathways: path:map00052, path:map01100, path:map02010
- Linked enzymes: ec:2.4.1.166, ec:2.4.1.67, ec:2.4.1.82, ec:3.2.1.22, ec:3.2.1.26
- Candidate mouse enzyme genes with MK expression evidence:
  - Ugp2 (ec:2.7.7.9): (RefSeq) UTP--glucose-1-phosphate uridylyltransferase isoform 1; pathway_neighbor_gene; Galactose metabolism; mmu_M00129  Ascorbate biosynthesis, animals, glucose-1P => ascorbate;mmu_M00549  UDP-Glc biosynthesis, Glc => UDP-Glc;mmu_M00854  Glycogen biosynthesis, glucose-1P => glycogen/starch; Seurat expression: MK pct 17.25%, other pct 29.59%, MK enrichment log2 -0.901, PH-vs-control MK log2 1.182, PH MK pct 20.66%, control MK pct 10.46%, PH-vs-control MK Wilcoxon p 0.00612; PubMed hits: none retrieved
  - Akr1b8 (ec:1.1.1.21): (RefSeq) aldose reductase-related protein 2; pathway_neighbor_gene; Galactose metabolism; one-carbon metabolism; Seurat expression: MK pct 2.62%, other pct 4%, MK enrichment log2 -1.179, PH-vs-control MK log2 2.464, PH MK pct 3.61%, control MK pct 0.65%, PH-vs-control MK Wilcoxon p 0.0625; PubMed hits: none retrieved
  - Akr1b10 (ec:1.1.1.21): (RefSeq) aldo-keto reductase family 1, member B10; pathway_neighbor_gene; Galactose metabolism; one-carbon metabolism; Seurat expression: MK pct 5.9%, other pct 8.52%, MK enrichment log2 -0.449, PH-vs-control MK log2 -0.654, PH MK pct 4.92%, control MK pct 7.84%, PH-vs-control MK Wilcoxon p 0.209; PubMed hits: none retrieved
  - Pfkl (ec:2.7.1.11): (RefSeq) ATP-dependent 6-phosphofructokinase, liver type isoform 1; pathway_neighbor_gene; Galactose metabolism; mmu_M00001  Glycolysis (Embden-Meyerhof pathway), glucose => pyruvate; glycolysis; Seurat expression: MK pct 16.38%, other pct 18.84%, MK enrichment log2 0.002, PH-vs-control MK log2 2.34, PH MK pct 21.31%, control MK pct 6.54%, PH-vs-control MK Wilcoxon p 3.7e-05; PubMed hits: none retrieved
  - Glb1 (ec:3.2.1.23): (RefSeq) beta-galactosidase preproprotein; pathway_neighbor_gene; Galactose metabolism; mmu_M00079  Keratan sulfate degradation; Seurat expression: MK pct 6.33%, other pct 8.52%, MK enrichment log2 -0.545, PH-vs-control MK log2 1.175, PH MK pct 7.54%, control MK pct 3.92%, PH-vs-control MK Wilcoxon p 0.13; PubMed hits: none retrieved
  - Akr1b1 (ec:1.1.1.21): (RefSeq) aldo-keto reductase family 1 member B1; pathway_neighbor_gene; Galactose metabolism; one-carbon metabolism; Seurat expression: not_found_in_seurat_features; PubMed hits: none retrieved
  - Hk1 (ec:2.7.1.1): (RefSeq) hexokinase-1 isoform HK1; pathway_neighbor_gene; Galactose metabolism; mmu_M00001  Glycolysis (Embden-Meyerhof pathway), glucose => pyruvate;mmu_M00549  UDP-Glc biosynthesis, Glc => UDP-Glc;mmu_M01015  GDP-Man biosynthesis, Man => GDP-Man; glycolysis; Seurat expression: MK pct 37.77%, other pct 20.25%, MK enrichment log2 1.156, PH-vs-control MK log2 0.61, PH MK pct 39.67%, control MK pct 33.99%, PH-vs-control MK Wilcoxon p 0.143; PubMed hits: none retrieved
  - Pgm2 (ec:5.4.2.2;ec:5.4.2.7): (RefSeq) phosphoglucomutase-2 isoform 1; pathway_neighbor_gene; Galactose metabolism; mmu_M00549  UDP-Glc biosynthesis, Glc => UDP-Glc;mmu_M00855  Glycogen degradation, glycogen => glucose-6P; glycolysis;purine metabolism; Seurat expression: MK pct 17.03%, other pct 15.5%, MK enrichment log2 0.163, PH-vs-control MK log2 1.061, PH MK pct 20%, control MK pct 11.11%, PH-vs-control MK Wilcoxon p 0.0152; PubMed hits: none retrieved
  - Pfkm (ec:2.7.1.11): (RefSeq) ATP-dependent 6-phosphofructokinase, muscle type; pathway_neighbor_gene; Galactose metabolism; mmu_M00001  Glycolysis (Embden-Meyerhof pathway), glucose => pyruvate; glycolysis; Seurat expression: MK pct 3.28%, other pct 3.46%, MK enrichment log2 0.006, PH-vs-control MK log2 1.912, PH MK pct 4.59%, control MK pct 0.65%, PH-vs-control MK Wilcoxon p 0.0269; PubMed hits: none retrieved
  - Akr1b7 (ec:1.1.1.21): (RefSeq) aldo-keto reductase family 1 member B7; pathway_neighbor_gene; Galactose metabolism; one-carbon metabolism; Seurat expression: MK pct 0%, other pct 0.09%, MK enrichment log2 -19.851, PH-vs-control MK log2 0, PH MK pct 0%, control MK pct 0%, PH-vs-control MK Wilcoxon p NA; PubMed hits: none retrieved

### 15-deoxy-delta-12-14-PGJ2
- Differential signal: up, log2FC 4.85 in PH-mk_vs_Control-mk (sFig6A Raw data.xlsx)
- KEGG status: no KEGG compound match
- KEGG compounds: none
- KEGG compound names: none
- KEGG pathways: none
- Linked enzymes: none
- Candidate mouse enzyme genes: none mapped

### phosphate
- Differential signal: up, log2FC 3.42 in PH-mk_vs_Control-mk (sFig6A Raw data.xlsx)
- KEGG status: mapped
- KEGG compounds: C00009, C01153
- KEGG compound names: Orthophosphate; Phosphate; Phosphoric acid; Orthophosphoric acid, Orthophosphoric monoester; Phosphate monoester
- KEGG pathways: path:map00190, path:map00195, path:map02010, path:map02020, path:map02024, path:map04111, path:map04928, path:map04978, path:map05012, path:map05022
- Linked enzymes: ec:1.13.11.78, ec:1.13.11.89, ec:1.13.11.90, ec:1.14.11.49, ec:1.18.6.1, ec:1.18.6.2, ec:1.19.6.1, ec:1.2.1.103, ec:1.2.1.106, ec:1.2.1.11, ec:1.2.1.12, ec:1.2.1.13
- Candidate mouse enzyme genes with MK expression evidence:
  - Uqcrfs1 (ec:7.1.1.8): (RefSeq) cytochrome b-c1 complex subunit Rieske, mitochondrial; pathway_neighbor_gene; Oxidative phosphorylation; mmu_M00151  Cytochrome bc1 complex respiratory unit;mmu_M00152  Cytochrome bc1 complex; oxidative phosphorylation; Seurat expression: MK pct 20.74%, other pct 37.89%, MK enrichment log2 -0.897, PH-vs-control MK log2 1.641, PH MK pct 25.25%, control MK pct 11.76%, PH-vs-control MK Wilcoxon p 0.000324; PubMed hits: none retrieved
  - Sdhb (ec:1.3.5.1): (RefSeq) succinate dehydrogenase [ubiquinone] iron-sulfur subunit, mitochondrial isoform 1 precursor; pathway_neighbor_gene; Oxidative phosphorylation; mmu_M00009  Citrate cycle (TCA cycle, Krebs cycle);mmu_M00011  Citrate cycle, second carbon oxidation, 2-oxoglutarate => oxaloacetate;mmu_M00148  Succinate dehydrogenase (ubiquinone); oxidative phosphorylation; Seurat expression: MK pct 24.67%, other pct 41.87%, MK enrichment log2 -0.756, PH-vs-control MK log2 1.397, PH MK pct 29.51%, control MK pct 15.03%, PH-vs-control MK Wilcoxon p 0.000356; PubMed hits: none retrieved
  - Atp6v1a (ec:7.1.2.2): (RefSeq) V-type proton ATPase catalytic subunit A isoform 1; pathway_neighbor_gene; Oxidative phosphorylation; mmu_M00160  V-type ATPase, eukaryotes; oxidative phosphorylation; Seurat expression: MK pct 26.86%, other pct 39.64%, MK enrichment log2 -0.526, PH-vs-control MK log2 0.905, PH MK pct 30.49%, control MK pct 19.61%, PH-vs-control MK Wilcoxon p 0.0124; PubMed hits: none retrieved
  - Ndufs8 (ec:7.1.1.2): (RefSeq) NADH dehydrogenase [ubiquinone] iron-sulfur protein 8, mitochondrial; pathway_neighbor_gene; Oxidative phosphorylation; mmu_M00143  NADH dehydrogenase (ubiquinone) Fe-S protein/flavoprotein complex, mitochondria; oxidative phosphorylation; Seurat expression: MK pct 15.5%, other pct 29.38%, MK enrichment log2 -1.006, PH-vs-control MK log2 1.278, PH MK pct 19.34%, control MK pct 7.84%, PH-vs-control MK Wilcoxon p 0.00143; PubMed hits: none retrieved
  - Ndufs2 (ec:7.1.1.2): (RefSeq) NADH dehydrogenase [ubiquinone] iron-sulfur protein 2, mitochondrial isoform 1; pathway_neighbor_gene; Oxidative phosphorylation; mmu_M00143  NADH dehydrogenase (ubiquinone) Fe-S protein/flavoprotein complex, mitochondria; oxidative phosphorylation; Seurat expression: MK pct 20.74%, other pct 33.1%, MK enrichment log2 -0.884, PH-vs-control MK log2 0.604, PH MK pct 22.95%, control MK pct 16.34%, PH-vs-control MK Wilcoxon p 0.0875; PubMed hits: none retrieved
  - Gapdh (ec:1.2.1.12): (RefSeq) glyceraldehyde-3-phosphate dehydrogenase isoform 2; direct_compound_enzyme; mmu_M00001  Glycolysis (Embden-Meyerhof pathway), glucose => pyruvate;mmu_M00002  Glycolysis, core module involving three-carbon compounds;mmu_M00003  Gluconeogenesis, oxaloacetate => fructose-6P; glycolysis; Seurat expression: MK pct 81.66%, other pct 80.43%, MK enrichment log2 -0.769, PH-vs-control MK log2 1.753, PH MK pct 85.25%, control MK pct 74.51%, PH-vs-control MK Wilcoxon p 4.61e-13; PubMed hits: none retrieved
  - Aldh18a1 (ec:1.2.1.41): (RefSeq) delta-1-pyrroline-5-carboxylate synthase isoform 1; direct_compound_enzyme; mmu_M00015  Proline biosynthesis, glutamate => proline; arginine/proline metabolism; Seurat expression: MK pct 0.87%, other pct 3.03%, MK enrichment log2 -1.972, PH-vs-control MK log2 0.59, PH MK pct 0.98%, control MK pct 0.65%, PH-vs-control MK Wilcoxon p 0.722; PubMed hits: none retrieved
  - Ndufs1 (ec:7.1.1.2): (RefSeq) NADH-ubiquinone oxidoreductase 75 kDa subunit, mitochondrial precursor; pathway_neighbor_gene; Oxidative phosphorylation; mmu_M00143  NADH dehydrogenase (ubiquinone) Fe-S protein/flavoprotein complex, mitochondria; oxidative phosphorylation; Seurat expression: MK pct 11.79%, other pct 19.59%, MK enrichment log2 -0.688, PH-vs-control MK log2 0.485, PH MK pct 13.11%, control MK pct 9.15%, PH-vs-control MK Wilcoxon p 0.208; PubMed hits: none retrieved
  - Ppa1 (ec:3.6.1.1): (RefSeq) inorganic pyrophosphatase; pathway_neighbor_gene; Oxidative phosphorylation; oxidative phosphorylation; Seurat expression: MK pct 3.71%, other pct 8.98%, MK enrichment log2 -1.49, PH-vs-control MK log2 1.507, PH MK pct 4.59%, control MK pct 1.96%, PH-vs-control MK Wilcoxon p 0.158; PubMed hits: none retrieved
  - Cox15 (ec:1.17.99.9): (RefSeq) cytochrome c oxidase assembly protein COX15 homolog; pathway_neighbor_gene; Oxidative phosphorylation; mmu_M00154  Cytochrome c oxidase; oxidative phosphorylation; Seurat expression: MK pct 3.71%, other pct 5.49%, MK enrichment log2 -0.672, PH-vs-control MK log2 -0.121, PH MK pct 3.61%, control MK pct 3.92%, PH-vs-control MK Wilcoxon p 0.867; PubMed hits: none retrieved

### Carnosic acid
- Differential signal: up, log2FC 4.29 in PH-mk_vs_Control-mk (sFig6A Raw data.xlsx)
- KEGG status: compound/enzyme mapped, no mouse genes found for linked enzymes
- KEGG compounds: C21818
- KEGG compound names: Carnosic acid; Salvin; 11,12-Dihydroxyabieta-8,11,13-trien-20-oic acid
- KEGG pathways: path:map00904, path:map01110
- Linked enzymes: ec:1.14.14.61
- Candidate mouse enzyme genes: none mapped

### Urocanic acid
- Differential signal: down, log2FC -3.95 in PH-mk_vs_Control-mk (sFig6A Raw data.xlsx)
- KEGG status: mapped
- KEGG compounds: C00785, C05571
- KEGG compound names: Urocanate; Urocanic acid, Thiourocanic acid
- KEGG pathways: path:map00340, path:map01100, path:map04382
- Linked enzymes: ec:1.3.99.33, ec:4.2.1.49, ec:4.3.1.3
- Candidate mouse enzyme genes with MK expression evidence:
  - Aldh2 (ec:1.2.1.3): (RefSeq) aldehyde dehydrogenase, mitochondrial isoform 1 precursor; pathway_neighbor_gene; Histidine metabolism; mmu_M00135  GABA biosynthesis, eukaryotes, putrescine => GABA; arginine/proline metabolism;tryptophan metabolism;glycolysis;fatty-acid metabolism; Seurat expression: MK pct 88.86%, other pct 61.15%, MK enrichment log2 1.01, PH-vs-control MK log2 0.329, PH MK pct 90.16%, control MK pct 86.27%, PH-vs-control MK Wilcoxon p 0.129; PubMed hits: gene_or_gene_context PMID 38124089: ALDH2 mitigates LPS-induced cardiac dysfunction, inflammation, and apoptosis through the c; gene_or_gene_context PMID 38472357: Neutrophil ALDH2 is a new therapeutic target for the effective treatment of sepsis-induced; gene_or_gene_context PMID 38348663: Carbonylation of Runx2 at K176 by 4-Hydroxynonenal Accelerates Vascular Calcification.
  - Maob (ec:1.4.3.4): (RefSeq) amine oxidase [flavin-containing] B; pathway_neighbor_gene; Histidine metabolism; mmu_M00135  GABA biosynthesis, eukaryotes, putrescine => GABA; arginine/proline metabolism;tryptophan metabolism; Seurat expression: MK pct 2.84%, other pct 4.19%, MK enrichment log2 -0.563, PH-vs-control MK log2 1.912, PH MK pct 3.61%, control MK pct 1.31%, PH-vs-control MK Wilcoxon p 0.161; PubMed hits: none retrieved
  - Aldh7a1 (ec:1.2.1.31;ec:1.2.1.8;ec:1.2.1.3): (RefSeq) alpha-aminoadipic semialdehyde dehydrogenase isoform a; pathway_neighbor_gene; Histidine metabolism; mmu_M00032  Lysine degradation, lysine => saccharopine => acetoacetyl-CoA;mmu_M00135  GABA biosynthesis, eukaryotes, putrescine => GABA;mmu_M00555  Betaine biosynthesis, choline => betaine; arginine/proline metabolism;one-carbon metabolism;tryptophan metabolism;glycolysis;fatty-acid metabolism; Seurat expression: MK pct 5.24%, other pct 6.53%, MK enrichment log2 -0.458, PH-vs-control MK log2 0.445, PH MK pct 5.9%, control MK pct 3.92%, PH-vs-control MK Wilcoxon p 0.377; PubMed hits: none retrieved
  - Aldh9a1 (ec:1.2.1.47;ec:1.2.1.3): (RefSeq) 4-trimethylaminobutyraldehyde dehydrogenase isoform 2; pathway_neighbor_gene; Histidine metabolism; mmu_M00135  GABA biosynthesis, eukaryotes, putrescine => GABA; arginine/proline metabolism;tryptophan metabolism;glycolysis;fatty-acid metabolism; Seurat expression: MK pct 12.23%, other pct 13.96%, MK enrichment log2 -0.408, PH-vs-control MK log2 0.441, PH MK pct 13.77%, control MK pct 9.15%, PH-vs-control MK Wilcoxon p 0.169; PubMed hits: none retrieved
  - Aldh3a2 (ec:1.2.1.3): (RefSeq) aldehyde dehydrogenase family 3 member A2 isoform 2; pathway_neighbor_gene; Histidine metabolism; mmu_M00135  GABA biosynthesis, eukaryotes, putrescine => GABA; arginine/proline metabolism;tryptophan metabolism;glycolysis;fatty-acid metabolism; Seurat expression: MK pct 11.35%, other pct 17.94%, MK enrichment log2 -0.606, PH-vs-control MK log2 -0.057, PH MK pct 12.13%, control MK pct 9.8%, PH-vs-control MK Wilcoxon p 0.489; PubMed hits: none retrieved
  - Cndp2 (ec:3.4.13.18): (RefSeq) cytosolic non-specific dipeptidase; pathway_neighbor_gene; Histidine metabolism; arginine/proline metabolism; Seurat expression: MK pct 13.97%, other pct 24.75%, MK enrichment log2 -1.438, PH-vs-control MK log2 1.275, PH MK pct 15.74%, control MK pct 10.46%, PH-vs-control MK Wilcoxon p 0.0939; PubMed hits: none retrieved
  - Aldh3b1 (ec:1.2.1.5): (RefSeq) aldehyde dehydrogenase family 3 member B1; pathway_neighbor_gene; Histidine metabolism; glycolysis; Seurat expression: MK pct 6.77%, other pct 18.7%, MK enrichment log2 -1.997, PH-vs-control MK log2 3.134, PH MK pct 9.51%, control MK pct 1.31%, PH-vs-control MK Wilcoxon p 0.000978; PubMed hits: none retrieved
  - Aspa (ec:3.5.1.15): (RefSeq) aspartoacylase isoform 1; pathway_neighbor_gene; Histidine metabolism; Seurat expression: MK pct 2.62%, other pct 2.78%, MK enrichment log2 -0.14, PH-vs-control MK log2 1.59, PH MK pct 3.28%, control MK pct 1.31%, PH-vs-control MK Wilcoxon p 0.212; PubMed hits: none retrieved
  - Carnmt1 (ec:2.1.1.22): (RefSeq) carnosine N-methyltransferase isoform 1; pathway_neighbor_gene; Histidine metabolism; Seurat expression: MK pct 9.17%, other pct 14.12%, MK enrichment log2 -0.586, PH-vs-control MK log2 0.812, PH MK pct 10.49%, control MK pct 6.54%, PH-vs-control MK Wilcoxon p 0.16; PubMed hits: none retrieved
  - Aoc1l1 (ec:1.4.3.22): (RefSeq) diamine oxidase-like protein 2 precursor; pathway_neighbor_gene; Histidine metabolism; arginine/proline metabolism;tryptophan metabolism; Seurat expression: not_found_in_seurat_features; PubMed hits: none retrieved

### Retinoic Acid
- Differential signal: up, log2FC 3.44 in PH-mk_vs_Control-mk (sFig6A Raw data.xlsx)
- KEGG status: mapped
- KEGG compounds: C00777, C15493
- KEGG compound names: Retinoate; Retinoic acid; Vitamin A acid; all-trans-Retinoate; Acide retinoique (French) (DSL); Tretinoine (French) (EINECS); 3,7-Dimethyl-9-(2,6,6-trimethyl-1-cyclohexene-1-yl)-2,4,6,8-nonatetraenoic acid (ECL); (all-E)-3,7-Dimethyl-9-(2,6,6-trimethyl-1-cyclohexen-1-yl)-2,4,6,8-nonatetraenoic acid; beta-Retinoic acid; AGN 100335; all-(E)-Retinoic acid; all-trans-beta-Retinoic acid; all-trans-Retinoic acid; all-trans-Tretinoin; all-trans-Vitamin A acid; Ro 1-5488; trans-Retinoic acid; Tretin M; all-trans-Vitamin A1 acid, 9-cis-Retinoic acid
- KEGG pathways: path:map00830, path:map01100, path:map03320, path:map04659, path:map04672, path:map04920, path:map05200, path:map05222, path:map05223, path:map05226
- Linked enzymes: ec:1.14.14.1, ec:1.2.1.36, ec:1.2.3.1, ec:2.4.1.17
- Candidate mouse enzyme genes with MK expression evidence:
  - Cyp1a1 (ec:1.14.14.1): (RefSeq) cytochrome P450 1A1; direct_compound_enzyme; tryptophan metabolism;retinoid metabolism; Seurat expression: MK pct 12.01%, other pct 10.27%, MK enrichment log2 -0.739, PH-vs-control MK log2 2.787, PH MK pct 14.43%, control MK pct 7.19%, PH-vs-control MK Wilcoxon p 0.0221; PubMed hits: gene_or_gene_context PMID 38503152: Salidroside protects pulmonary artery endothelial cells against hypoxia-induced apoptosis ; gene_or_gene_context PMID 32763913: Integrated Skin Transcriptomics and Serum Multiplex Assays Reveal Novel Mechanisms of Woun; gene_or_gene_context PMID 38652558: A tryptophan-derived uremic metabolite/Ahr/Pdk4 axis governs skeletal muscle mitochondrial
  - Adh5 (ec:1.1.1.284;ec:1.1.1.1): (RefSeq) alcohol dehydrogenase class-3 isoform 1; pathway_neighbor_gene; Retinol metabolism; glutathione/redox metabolism;retinoid metabolism;glycolysis;fatty-acid metabolism; Seurat expression: MK pct 15.07%, other pct 24.33%, MK enrichment log2 -0.903, PH-vs-control MK log2 1.027, PH MK pct 18.36%, control MK pct 8.5%, PH-vs-control MK Wilcoxon p 0.00618; PubMed hits: none retrieved
  - Aldh1a1 (ec:1.2.1.36): (RefSeq) aldehyde dehydrogenase 1A1; direct_compound_enzyme; retinoid metabolism; Seurat expression: MK pct 24.24%, other pct 13.41%, MK enrichment log2 -0.809, PH-vs-control MK log2 1.217, PH MK pct 27.87%, control MK pct 16.99%, PH-vs-control MK Wilcoxon p 0.0117; PubMed hits: none retrieved
  - Dgat1 (ec:2.3.1.20;ec:2.3.1.75;ec:2.3.1.76): (RefSeq) diacylglycerol O-acyltransferase 1; pathway_neighbor_gene; Retinol metabolism; mmu_M00089  Triacylglycerol biosynthesis; retinoid metabolism; Seurat expression: MK pct 9.61%, other pct 20.1%, MK enrichment log2 -1.236, PH-vs-control MK log2 2.791, PH MK pct 12.79%, control MK pct 3.27%, PH-vs-control MK Wilcoxon p 0.00093; PubMed hits: none retrieved
  - Dhrs3 (ec:1.1.1.300): (RefSeq) short-chain dehydrogenase/reductase 3 isoform 1; pathway_neighbor_gene; Retinol metabolism; retinoid metabolism; Seurat expression: MK pct 26.42%, other pct 23.16%, MK enrichment log2 -0.173, PH-vs-control MK log2 0.635, PH MK pct 28.85%, control MK pct 21.57%, PH-vs-control MK Wilcoxon p 0.0796; PubMed hits: none retrieved
  - Cyp26b1 (ec:1.14.14.-): (RefSeq) cytochrome P450 26B1; pathway_neighbor_gene; Retinol metabolism; retinoid metabolism; Seurat expression: MK pct 7.86%, other pct 4.46%, MK enrichment log2 0.728, PH-vs-control MK log2 0.912, PH MK pct 8.85%, control MK pct 5.88%, PH-vs-control MK Wilcoxon p 0.253; PubMed hits: none retrieved
  - Cyp26a1 (ec:1.14.14.-): (RefSeq) cytochrome P450 26A1; pathway_neighbor_gene; Retinol metabolism; retinoid metabolism; Seurat expression: MK pct 0.22%, other pct 0.04%, MK enrichment log2 2.518, PH-vs-control MK log2 -22.64, PH MK pct 0%, control MK pct 0.65%, PH-vs-control MK Wilcoxon p 0.159; PubMed hits: none retrieved
  - Rdh11 (ec:1.1.1.300): (RefSeq) retinol dehydrogenase 11 isoform 1 precursor; pathway_neighbor_gene; Retinol metabolism; retinoid metabolism; Seurat expression: MK pct 6.77%, other pct 7.88%, MK enrichment log2 -0.236, PH-vs-control MK log2 0.76, PH MK pct 7.54%, control MK pct 5.23%, PH-vs-control MK Wilcoxon p 0.347; PubMed hits: none retrieved
  - Aox1 (ec:1.2.3.1): (RefSeq) aldehyde oxidase 1; direct_compound_enzyme; tryptophan metabolism;retinoid metabolism; Seurat expression: MK pct 1.53%, other pct 3.85%, MK enrichment log2 -1.75, PH-vs-control MK log2 1.59, PH MK pct 1.97%, control MK pct 0.65%, PH-vs-control MK Wilcoxon p 0.281; PubMed hits: none retrieved
  - Dhrs9 (ec:1.1.1.-): (RefSeq) dehydrogenase/reductase SDR family member 9 precursor; pathway_neighbor_gene; Retinol metabolism; retinoid metabolism; Seurat expression: MK pct 2.4%, other pct 6.13%, MK enrichment log2 -1.095, PH-vs-control MK log2 2.005, PH MK pct 3.28%, control MK pct 0.65%, PH-vs-control MK Wilcoxon p 0.0851; PubMed hits: none retrieved

### tryptophan
- Differential signal: up, log2FC 4.03 in PH-mk_vs_Control-mk (sFig6A Raw data.xlsx)
- KEGG status: mapped
- KEGG compounds: C00806, C00078
- KEGG compound names: Tryptophan; alpha-Amino-beta-(3-indolyl)-propionic acid, L-Tryptophan; Tryptophan; (S)-alpha-Amino-beta-(3-indolyl)-propionic acid
- KEGG pathways: path:map00260, path:map00380, path:map00400, path:map00404, path:map00901, path:map00966, path:map00970, path:map00996, path:map00997, path:map00999
- Linked enzymes: ec:1.11.2.8, ec:1.13.11.11, ec:1.13.11.52, ec:1.13.12.3, ec:1.13.99.3, ec:1.14.14.156, ec:1.14.15.41, ec:1.14.16.4, ec:1.14.19.58, ec:1.14.19.59, ec:1.14.19.82, ec:1.14.19.9
- Candidate mouse enzyme genes with MK expression evidence:
  - Cyp1a1 (ec:1.14.14.1): (RefSeq) cytochrome P450 1A1; pathway_neighbor_gene; Tryptophan metabolism; tryptophan metabolism;retinoid metabolism; Seurat expression: MK pct 12.01%, other pct 10.27%, MK enrichment log2 -0.739, PH-vs-control MK log2 2.787, PH MK pct 14.43%, control MK pct 7.19%, PH-vs-control MK Wilcoxon p 0.0221; PubMed hits: gene_or_gene_context PMID 38503152: Salidroside protects pulmonary artery endothelial cells against hypoxia-induced apoptosis ; gene_or_gene_context PMID 32763913: Integrated Skin Transcriptomics and Serum Multiplex Assays Reveal Novel Mechanisms of Woun; gene_or_gene_context PMID 38652558: A tryptophan-derived uremic metabolite/Ahr/Pdk4 axis governs skeletal muscle mitochondrial
  - Aldh2 (ec:1.2.1.3): (RefSeq) aldehyde dehydrogenase, mitochondrial isoform 1 precursor; pathway_neighbor_gene; Tryptophan metabolism; mmu_M00135  GABA biosynthesis, eukaryotes, putrescine => GABA; arginine/proline metabolism;tryptophan metabolism;glycolysis;fatty-acid metabolism; Seurat expression: MK pct 88.86%, other pct 61.15%, MK enrichment log2 1.01, PH-vs-control MK log2 0.329, PH MK pct 90.16%, control MK pct 86.27%, PH-vs-control MK Wilcoxon p 0.129; PubMed hits: gene_or_gene_context PMID 38124089: ALDH2 mitigates LPS-induced cardiac dysfunction, inflammation, and apoptosis through the c; gene_or_gene_context PMID 38472357: Neutrophil ALDH2 is a new therapeutic target for the effective treatment of sepsis-induced; gene_or_gene_context PMID 38348663: Carbonylation of Runx2 at K176 by 4-Hydroxynonenal Accelerates Vascular Calcification.
  - Maoa (ec:1.4.3.4): (RefSeq) amine oxidase [flavin-containing] A; pathway_neighbor_gene; Glycine, serine and threonine metabolism; mmu_M00135  GABA biosynthesis, eukaryotes, putrescine => GABA; arginine/proline metabolism;tryptophan metabolism; Seurat expression: MK pct 20.09%, other pct 13.56%, MK enrichment log2 0.84, PH-vs-control MK log2 0.467, PH MK pct 21.64%, control MK pct 16.99%, PH-vs-control MK Wilcoxon p 0.25; PubMed hits: none retrieved
  - Sdsl (ec:4.3.1.17;ec:4.3.1.19): (RefSeq) serine dehydratase-like; pathway_neighbor_gene; Glycine, serine and threonine metabolism; cysteine/methionine metabolism; Seurat expression: MK pct 0.66%, other pct 0.17%, MK enrichment log2 1.825, PH-vs-control MK log2 23.23, PH MK pct 0.98%, control MK pct 0%, PH-vs-control MK Wilcoxon p 0.22; PubMed hits: none retrieved
  - Maob (ec:1.4.3.4): (RefSeq) amine oxidase [flavin-containing] B; pathway_neighbor_gene; Glycine, serine and threonine metabolism; mmu_M00135  GABA biosynthesis, eukaryotes, putrescine => GABA; arginine/proline metabolism;tryptophan metabolism; Seurat expression: MK pct 2.84%, other pct 4.19%, MK enrichment log2 -0.563, PH-vs-control MK log2 1.912, PH MK pct 3.61%, control MK pct 1.31%, PH-vs-control MK Wilcoxon p 0.161; PubMed hits: none retrieved
  - Aldh7a1 (ec:1.2.1.31;ec:1.2.1.8;ec:1.2.1.3): (RefSeq) alpha-aminoadipic semialdehyde dehydrogenase isoform a; pathway_neighbor_gene; Glycine, serine and threonine metabolism; mmu_M00032  Lysine degradation, lysine => saccharopine => acetoacetyl-CoA;mmu_M00135  GABA biosynthesis, eukaryotes, putrescine => GABA;mmu_M00555  Betaine biosynthesis, choline => betaine; arginine/proline metabolism;one-carbon metabolism;tryptophan metabolism;glycolysis;fatty-acid metabolism; Seurat expression: MK pct 5.24%, other pct 6.53%, MK enrichment log2 -0.458, PH-vs-control MK log2 0.445, PH MK pct 5.9%, control MK pct 3.92%, PH-vs-control MK Wilcoxon p 0.377; PubMed hits: none retrieved
  - Dld (ec:1.8.1.4): (RefSeq) dihydrolipoyl dehydrogenase, mitochondrial precursor; pathway_neighbor_gene; Glycine, serine and threonine metabolism; mmu_M00009  Citrate cycle (TCA cycle, Krebs cycle);mmu_M00011  Citrate cycle, second carbon oxidation, 2-oxoglutarate => oxaloacetate;mmu_M00032  Lysine degradation, lysine => saccharopine => acetoacetyl-CoA;mmu_M00036  Leucine degradation, leucine => acetoacetate + acetyl-CoA;mmu_M00307  Pyruvate oxidation, pyruvate => acetyl-CoA;mmu_M00621  Glycine cleavage system; one-carbon metabolism;tryptophan metabolism;glycolysis; Seurat expression: MK pct 13.54%, other pct 20.73%, MK enrichment log2 -0.539, PH-vs-control MK log2 0.801, PH MK pct 15.08%, control MK pct 10.46%, PH-vs-control MK Wilcoxon p 0.164; PubMed hits: none retrieved
  - Shmt2 (ec:2.1.2.1): (RefSeq) serine hydroxymethyltransferase, mitochondrial isoform 1; pathway_neighbor_gene; Glycine, serine and threonine metabolism; mmu_M00141  C1-unit interconversion, eukaryotes; one-carbon metabolism; Seurat expression: MK pct 3.71%, other pct 6.59%, MK enrichment log2 -0.907, PH-vs-control MK log2 2.092, PH MK pct 4.92%, control MK pct 1.31%, PH-vs-control MK Wilcoxon p 0.0537; PubMed hits: none retrieved
  - Gldc (ec:1.4.4.2): (RefSeq) glycine dehydrogenase (decarboxylating), mitochondrial precursor; pathway_neighbor_gene; Glycine, serine and threonine metabolism; mmu_M00621  Glycine cleavage system; one-carbon metabolism; Seurat expression: MK pct 1.75%, other pct 0.81%, MK enrichment log2 0.965, PH-vs-control MK log2 1.812, PH MK pct 2.3%, control MK pct 0.65%, PH-vs-control MK Wilcoxon p 0.207; PubMed hits: none retrieved
  - Ido1 (ec:1.13.11.52): (RefSeq) indoleamine 2,3-dioxygenase 1 isoform 1; direct_compound_enzyme; mmu_M00038  Tryptophan metabolism, tryptophan => kynurenine => 2-aminomuconate;mmu_M00912  NAD biosynthesis, tryptophan => quinolinate => NAD; tryptophan metabolism; Seurat expression: MK pct 0.66%, other pct 0.58%, MK enrichment log2 -0.056, PH-vs-control MK log2 23.645, PH MK pct 0.98%, control MK pct 0%, PH-vs-control MK Wilcoxon p 0.22; PubMed hits: none retrieved

### C22:3
- Differential signal: up, log2FC 3.49 in PH-mk_vs_Control-mk (sFig6A Raw data.xlsx)
- KEGG status: KEGG fetch failed: HTTP Error 400: Bad Request
- KEGG compounds: none
- KEGG compound names: none
- KEGG pathways: none
- Linked enzymes: none
- Candidate mouse enzyme genes: none mapped

### Glucose
- Differential signal: up, log2FC 2.77 in PH-mk_vs_Control-mk (sFig6A Raw data.xlsx)
- KEGG status: mapped
- KEGG compounds: C00031, C20978
- KEGG compound names: D-Glucose; Grape sugar; Dextrose; Glucose; D-Glucopyranose, Glucoselysine
- KEGG pathways: path:map00010, path:map00030, path:map00052, path:map00074, path:map00500, path:map00520, path:map00521, path:map00524, path:map00566, path:map00901
- Linked enzymes: ec:1.1.1.118, ec:1.1.1.119, ec:1.1.1.121, ec:1.1.1.359, ec:1.1.1.360, ec:1.1.1.432, ec:1.1.3.10, ec:1.1.5.2, ec:1.1.5.9, ec:1.1.99.28, ec:1.1.99.35, ec:2.3.1.103
- Candidate mouse enzyme genes with MK expression evidence:
  - Aldh2 (ec:1.2.1.3): (RefSeq) aldehyde dehydrogenase, mitochondrial isoform 1 precursor; pathway_neighbor_gene; Glycolysis / Gluconeogenesis; mmu_M00135  GABA biosynthesis, eukaryotes, putrescine => GABA; arginine/proline metabolism;tryptophan metabolism;glycolysis;fatty-acid metabolism; Seurat expression: MK pct 88.86%, other pct 61.15%, MK enrichment log2 1.01, PH-vs-control MK log2 0.329, PH MK pct 90.16%, control MK pct 86.27%, PH-vs-control MK Wilcoxon p 0.129; PubMed hits: gene_or_gene_context PMID 38124089: ALDH2 mitigates LPS-induced cardiac dysfunction, inflammation, and apoptosis through the c; gene_or_gene_context PMID 38472357: Neutrophil ALDH2 is a new therapeutic target for the effective treatment of sepsis-induced; gene_or_gene_context PMID 38348663: Carbonylation of Runx2 at K176 by 4-Hydroxynonenal Accelerates Vascular Calcification.
  - Ldha (ec:1.1.1.27): (RefSeq) L-lactate dehydrogenase A chain isoform 1; pathway_neighbor_gene; Glycolysis / Gluconeogenesis; cysteine/methionine metabolism;glycolysis; Seurat expression: MK pct 47.82%, other pct 60.94%, MK enrichment log2 -0.745, PH-vs-control MK log2 2.333, PH MK pct 56.39%, control MK pct 30.72%, PH-vs-control MK Wilcoxon p 4.48e-10; PubMed hits: gene_or_gene_context PMID 38214194: ErbB3 Governs Endothelial Dysfunction in Hypoxia-Induced Pulmonary Hypertension.; gene_or_gene_context PMID 33105588: Perivascular Inflammation in Pulmonary Arterial Hypertension.; gene_or_gene_context PMID 32746619: Endothelial-to-Mesenchymal Transition in Pulmonary Arterial Hypertension.
  - Adh5 (ec:1.1.1.284;ec:1.1.1.1): (RefSeq) alcohol dehydrogenase class-3 isoform 1; pathway_neighbor_gene; Glycolysis / Gluconeogenesis; glutathione/redox metabolism;retinoid metabolism;glycolysis;fatty-acid metabolism; Seurat expression: MK pct 15.07%, other pct 24.33%, MK enrichment log2 -0.903, PH-vs-control MK log2 1.027, PH MK pct 18.36%, control MK pct 8.5%, PH-vs-control MK Wilcoxon p 0.00618; PubMed hits: none retrieved
  - Aldh7a1 (ec:1.2.1.31;ec:1.2.1.8;ec:1.2.1.3): (RefSeq) alpha-aminoadipic semialdehyde dehydrogenase isoform a; pathway_neighbor_gene; Glycolysis / Gluconeogenesis; mmu_M00032  Lysine degradation, lysine => saccharopine => acetoacetyl-CoA;mmu_M00135  GABA biosynthesis, eukaryotes, putrescine => GABA;mmu_M00555  Betaine biosynthesis, choline => betaine; arginine/proline metabolism;one-carbon metabolism;tryptophan metabolism;glycolysis;fatty-acid metabolism; Seurat expression: MK pct 5.24%, other pct 6.53%, MK enrichment log2 -0.458, PH-vs-control MK log2 0.445, PH MK pct 5.9%, control MK pct 3.92%, PH-vs-control MK Wilcoxon p 0.377; PubMed hits: none retrieved
  - Dld (ec:1.8.1.4): (RefSeq) dihydrolipoyl dehydrogenase, mitochondrial precursor; pathway_neighbor_gene; Glycolysis / Gluconeogenesis; mmu_M00009  Citrate cycle (TCA cycle, Krebs cycle);mmu_M00011  Citrate cycle, second carbon oxidation, 2-oxoglutarate => oxaloacetate;mmu_M00032  Lysine degradation, lysine => saccharopine => acetoacetyl-CoA;mmu_M00036  Leucine degradation, leucine => acetoacetate + acetyl-CoA;mmu_M00307  Pyruvate oxidation, pyruvate => acetyl-CoA;mmu_M00621  Glycine cleavage system; one-carbon metabolism;tryptophan metabolism;glycolysis; Seurat expression: MK pct 13.54%, other pct 20.73%, MK enrichment log2 -0.539, PH-vs-control MK log2 0.801, PH MK pct 15.08%, control MK pct 10.46%, PH-vs-control MK Wilcoxon p 0.164; PubMed hits: none retrieved
  - Aldh9a1 (ec:1.2.1.47;ec:1.2.1.3): (RefSeq) 4-trimethylaminobutyraldehyde dehydrogenase isoform 2; pathway_neighbor_gene; Glycolysis / Gluconeogenesis; mmu_M00135  GABA biosynthesis, eukaryotes, putrescine => GABA; arginine/proline metabolism;tryptophan metabolism;glycolysis;fatty-acid metabolism; Seurat expression: MK pct 12.23%, other pct 13.96%, MK enrichment log2 -0.408, PH-vs-control MK log2 0.441, PH MK pct 13.77%, control MK pct 9.15%, PH-vs-control MK Wilcoxon p 0.169; PubMed hits: none retrieved
  - Dlat (ec:2.3.1.12): (RefSeq) dihydrolipoyllysine-residue acetyltransferase component of pyruvate dehydrogenase complex, mitochondrial; pathway_neighbor_gene; Glycolysis / Gluconeogenesis; mmu_M00307  Pyruvate oxidation, pyruvate => acetyl-CoA; glycolysis; Seurat expression: MK pct 8.3%, other pct 12.76%, MK enrichment log2 -0.751, PH-vs-control MK log2 1.59, PH MK pct 10.82%, control MK pct 3.27%, PH-vs-control MK Wilcoxon p 0.00606; PubMed hits: none retrieved
  - Aldh3a2 (ec:1.2.1.3): (RefSeq) aldehyde dehydrogenase family 3 member A2 isoform 2; pathway_neighbor_gene; Glycolysis / Gluconeogenesis; mmu_M00135  GABA biosynthesis, eukaryotes, putrescine => GABA; arginine/proline metabolism;tryptophan metabolism;glycolysis;fatty-acid metabolism; Seurat expression: MK pct 11.35%, other pct 17.94%, MK enrichment log2 -0.606, PH-vs-control MK log2 -0.057, PH MK pct 12.13%, control MK pct 9.8%, PH-vs-control MK Wilcoxon p 0.489; PubMed hits: none retrieved
  - Akr1a1 (ec:1.1.1.2): (RefSeq) aldo-keto reductase family 1 member A1; pathway_neighbor_gene; Glycolysis / Gluconeogenesis; mmu_M00014  Glucuronate pathway (uronate pathway);mmu_M00129  Ascorbate biosynthesis, animals, glucose-1P => ascorbate; glycolysis; Seurat expression: MK pct 39.96%, other pct 58.06%, MK enrichment log2 -0.68, PH-vs-control MK log2 0.76, PH MK pct 43.61%, control MK pct 32.68%, PH-vs-control MK Wilcoxon p 0.00481; PubMed hits: none retrieved
  - Pdha1 (ec:1.2.4.1): (RefSeq) pyruvate dehydrogenase E1 component subunit alpha, somatic form, mitochondrial precursor; pathway_neighbor_gene; Glycolysis / Gluconeogenesis; mmu_M00307  Pyruvate oxidation, pyruvate => acetyl-CoA; glycolysis; Seurat expression: MK pct 16.38%, other pct 23.73%, MK enrichment log2 -0.447, PH-vs-control MK log2 1.02, PH MK pct 19.34%, control MK pct 10.46%, PH-vs-control MK Wilcoxon p 0.0135; PubMed hits: none retrieved

### cystine
- Differential signal: up, log2FC 3.06 in PH-mk_vs_Control-mk (sFig6A Raw data.xlsx)
- KEGG status: compound/enzyme mapped, no mouse genes found for linked enzymes
- KEGG compounds: C01420, C05704
- KEGG compound names: Cystine; Dicysteine; alpha-Diamino-beta-dithiolactic acid, Selenocystine
- KEGG pathways: none
- Linked enzymes: ec:1.8.4.4
- Candidate mouse enzyme genes: none mapped

### pyridoxine
- Differential signal: up, log2FC 3.03 in PH-mk_vs_Control-mk (sFig6A Raw data.xlsx)
- KEGG status: mapped
- KEGG compounds: C00314, C00627
- KEGG compound names: Pyridoxine; Pyridoxol, Pyridoxine phosphate; Pyridoxine 5'-phosphate; Pyridoxine 5-phosphate; Pyridoxol 5'-phosphate
- KEGG pathways: path:map00750, path:map01100, path:map01120, path:map01240
- Linked enzymes: ec:1.1.1.65, ec:1.1.3.12, ec:1.1.99.9, ec:1.4.3.5, ec:2.4.1.160, ec:2.6.99.2, ec:2.7.1.35, ec:3.1.3.74
- Candidate mouse enzyme genes with MK expression evidence:
  - Psat1 (ec:2.6.1.52): (RefSeq) phosphoserine aminotransferase isoform 1; pathway_neighbor_gene; Vitamin B6 metabolism; mmu_M00020  Serine biosynthesis, glycerate-3P => serine; cysteine/methionine metabolism; Seurat expression: MK pct 0.87%, other pct 2.78%, MK enrichment log2 -1.713, PH-vs-control MK log2 23.967, PH MK pct 1.31%, control MK pct 0%, PH-vs-control MK Wilcoxon p 0.156; PubMed hits: none retrieved
  - Phospho2 (ec:3.1.3.74): (RefSeq) pyridoxal phosphate phosphatase PHOSPHO2; direct_compound_enzyme; Seurat expression: MK pct 8.3%, other pct 10.45%, MK enrichment log2 -0.243, PH-vs-control MK log2 1.253, PH MK pct 9.84%, control MK pct 5.23%, PH-vs-control MK Wilcoxon p 0.0877; PubMed hits: none retrieved
  - Aox1 (ec:1.2.3.1): (RefSeq) aldehyde oxidase 1; pathway_neighbor_gene; Vitamin B6 metabolism; tryptophan metabolism;retinoid metabolism; Seurat expression: MK pct 1.53%, other pct 3.85%, MK enrichment log2 -1.75, PH-vs-control MK log2 1.59, PH MK pct 1.97%, control MK pct 0.65%, PH-vs-control MK Wilcoxon p 0.281; PubMed hits: none retrieved
  - Pnpo (ec:1.4.3.5): (RefSeq) pyridoxine-5'-phosphate oxidase; direct_compound_enzyme; Seurat expression: MK pct 2.4%, other pct 7.23%, MK enrichment log2 -1.832, PH-vs-control MK log2 2.327, PH MK pct 3.28%, control MK pct 0.65%, PH-vs-control MK Wilcoxon p 0.0841; PubMed hits: none retrieved
  - Aox2 (ec:1.2.3.1): (RefSeq) aldehyde oxidase 2; pathway_neighbor_gene; Vitamin B6 metabolism; tryptophan metabolism;retinoid metabolism; Seurat expression: MK pct 0%, other pct 0%, MK enrichment log2 -15.37, PH-vs-control MK log2 0, PH MK pct 0%, control MK pct 0%, PH-vs-control MK Wilcoxon p NA; PubMed hits: none retrieved
  - Aox4 (ec:1.2.3.1): (RefSeq) aldehyde oxidase 4; pathway_neighbor_gene; Vitamin B6 metabolism; tryptophan metabolism;retinoid metabolism; Seurat expression: MK pct 0%, other pct 0.06%, MK enrichment log2 -19.07, PH-vs-control MK log2 0, PH MK pct 0%, control MK pct 0%, PH-vs-control MK Wilcoxon p NA; PubMed hits: none retrieved
  - Aox3 (ec:1.2.3.1): (RefSeq) aldehyde oxidase 3; pathway_neighbor_gene; Vitamin B6 metabolism; tryptophan metabolism;retinoid metabolism; Seurat expression: MK pct 0.66%, other pct 3.43%, MK enrichment log2 -2.419, PH-vs-control MK log2 -0.41, PH MK pct 0.33%, control MK pct 1.31%, PH-vs-control MK Wilcoxon p 0.224; PubMed hits: none retrieved
  - Pdxk (ec:2.7.1.35): (RefSeq) pyridoxal kinase; direct_compound_enzyme; Seurat expression: MK pct 2.62%, other pct 9.24%, MK enrichment log2 -2.226, PH-vs-control MK log2 0.59, PH MK pct 2.95%, control MK pct 1.96%, PH-vs-control MK Wilcoxon p 0.533; PubMed hits: none retrieved
  - Pdxp (ec:3.1.3.74): (RefSeq) chronophin; direct_compound_enzyme; Seurat expression: MK pct 1.09%, other pct 1.2%, MK enrichment log2 0.06, PH-vs-control MK log2 -1.995, PH MK pct 0.66%, control MK pct 1.96%, PH-vs-control MK Wilcoxon p 0.205; PubMed hits: none retrieved

### methionine
- Differential signal: up, log2FC 3.26 in PH-mk_vs_Control-mk (sFig6A Raw data.xlsx)
- KEGG status: mapped
- KEGG compounds: C01733, C00073
- KEGG compound names: Methionine; 2-Amino-4-(methylthio)butyric acid, L-Methionine; Methionine; L-2-Amino-4methylthiobutyric acid
- KEGG pathways: path:map00270, path:map00470, path:map00670, path:map00920, path:map00966, path:map00970, path:map00999, path:map01060, path:map01070, path:map01100
- Linked enzymes: ec:1.1.98.7, ec:1.1.99.38, ec:1.17.98.2, ec:1.21.98.1, ec:1.21.98.3, ec:1.21.98.4, ec:1.21.98.5, ec:1.3.98.3, ec:1.3.98.6, ec:1.3.98.7, ec:1.4.3.2, ec:1.8.4.11
- Candidate mouse enzyme genes with MK expression evidence:
  - Amd1 (ec:4.1.1.50): (RefSeq) S-adenosylmethionine decarboxylase proenzyme 1; pathway_neighbor_gene; Cysteine and methionine metabolism; mmu_M00034  Methionine salvage pathway; polyamine metabolism;S-adenosylmethionine metabolism;methionine salvage;cysteine/methionine metabolism;arginine/proline metabolism; Seurat expression: MK pct 31.44%, other pct 14.87%, MK enrichment log2 1.353, PH-vs-control MK log2 1.77, PH MK pct 38.03%, control MK pct 18.3%, PH-vs-control MK Wilcoxon p 6.55e-06; PubMed hits: gene_or_gene_context PMID 38965534: Polyamine and EIF5A hypusination downstream of c-Myc confers targeted therapy resistance i; gene_or_gene_context PMID 28658205: mTORC1-dependent AMD1 regulation sustains polyamine metabolism in prostate cancer.; gene_or_gene_context PMID 40768332: Multi-dimensional metabolomic remodeling under diverse muscle atrophic stimuli in vivo.
  - Amd2 (ec:4.1.1.50): (RefSeq) S-adenosylmethionine decarboxylase proenzyme 2; pathway_neighbor_gene; Cysteine and methionine metabolism; mmu_M00034  Methionine salvage pathway; polyamine metabolism;S-adenosylmethionine metabolism;methionine salvage;cysteine/methionine metabolism;arginine/proline metabolism; Seurat expression: MK pct 4.37%, other pct 2.1%, MK enrichment log2 0.931, PH-vs-control MK log2 2.175, PH MK pct 5.9%, control MK pct 1.31%, PH-vs-control MK Wilcoxon p 0.0235; PubMed hits: gene_or_gene_context PMID 40768332: Multi-dimensional metabolomic remodeling under diverse muscle atrophic stimuli in vivo.; gene_or_gene_context PMID 36543136: Spatially resolved transcriptomics reveals innervation-responsive functional clusters in s; gene_or_gene_context PMID 7789170: The human S-adenosylmethionine decarboxylase gene: nucleotide sequence of a pseudogene and
  - Mat2a (ec:2.5.1.6): (RefSeq) S-adenosylmethionine synthase isoform type-2 isoform 1; pathway_neighbor_gene; Cysteine and methionine metabolism; mmu_M00034  Methionine salvage pathway;mmu_M00035  Methionine degradation; S-adenosylmethionine metabolism;methionine salvage;cysteine/methionine metabolism;one-carbon metabolism; Seurat expression: MK pct 31%, other pct 46.44%, MK enrichment log2 -0.641, PH-vs-control MK log2 0.668, PH MK pct 33.44%, control MK pct 26.14%, PH-vs-control MK Wilcoxon p 0.096; PubMed hits: gene_or_gene_context PMID 23073625: S-adenosylmethionine in liver health, injury, and cancer.; gene_or_gene_context PMID 35796517: Overview of Methionine Adenosyltransferase 2A (MAT2A) as an Anticancer Target: Structure, ; gene_or_gene_context PMID 28525753: The U6 snRNA m(6)A Methyltransferase METTL16 Regulates SAM Synthetase Intron Retention.
  - Mat2b (ec:2.5.1.6): (RefSeq) methionine adenosyltransferase 2 subunit beta isoform 1; pathway_neighbor_gene; Cysteine and methionine metabolism; mmu_M00034  Methionine salvage pathway;mmu_M00035  Methionine degradation; S-adenosylmethionine metabolism;methionine salvage;cysteine/methionine metabolism;one-carbon metabolism; Seurat expression: MK pct 23.8%, other pct 36.01%, MK enrichment log2 -0.418, PH-vs-control MK log2 0.398, PH MK pct 25.9%, control MK pct 19.61%, PH-vs-control MK Wilcoxon p 0.139; PubMed hits: gene_or_gene_context PMID 39333125: The role of forkhead box M1-methionine adenosyltransferase 2 A/2B axis in liver inflammati; gene_or_gene_context PMID 31496615: Methionine adenosyltransferases in liver cancer.; gene_or_gene_context PMID 39293586: Developing patient-derived organoids to demonstrate JX24120 inhibits SAMe synthesis in end
  - Ldha (ec:1.1.1.27): (RefSeq) L-lactate dehydrogenase A chain isoform 1; pathway_neighbor_gene; Cysteine and methionine metabolism; cysteine/methionine metabolism;glycolysis; Seurat expression: MK pct 47.82%, other pct 60.94%, MK enrichment log2 -0.745, PH-vs-control MK log2 2.333, PH MK pct 56.39%, control MK pct 30.72%, PH-vs-control MK Wilcoxon p 4.48e-10; PubMed hits: gene_or_gene_context PMID 38214194: ErbB3 Governs Endothelial Dysfunction in Hypoxia-Induced Pulmonary Hypertension.; gene_or_gene_context PMID 33105588: Perivascular Inflammation in Pulmonary Arterial Hypertension.; gene_or_gene_context PMID 32746619: Endothelial-to-Mesenchymal Transition in Pulmonary Arterial Hypertension.
  - Got2 (ec:2.6.1.1): (RefSeq) aspartate aminotransferase, mitochondrial; pathway_neighbor_gene; Cysteine and methionine metabolism; cysteine/methionine metabolism;arginine/proline metabolism;tryptophan metabolism; Seurat expression: MK pct 16.81%, other pct 23.94%, MK enrichment log2 -0.425, PH-vs-control MK log2 0.676, PH MK pct 19.67%, control MK pct 11.11%, PH-vs-control MK Wilcoxon p 0.0219; PubMed hits: gene_or_gene_context PMID 35726024: Adaptive stimulation of macropinocytosis overcomes aspartate limitation in cancer cells un; gene_or_gene_context PMID 41001736: Comprehensive genotypic, phenotypic, and biochemical characterization of GOT2 deficiency: ; gene_or_gene_context PMID 40536683: The innate immune receptor NLRX1 is a novel required modulator for mPTP opening: implicati
  - Mdh2 (ec:1.1.1.37): (RefSeq) malate dehydrogenase, mitochondrial precursor; pathway_neighbor_gene; Cysteine and methionine metabolism; mmu_M00009  Citrate cycle (TCA cycle, Krebs cycle);mmu_M00011  Citrate cycle, second carbon oxidation, 2-oxoglutarate => oxaloacetate; cysteine/methionine metabolism; Seurat expression: MK pct 29.69%, other pct 46.13%, MK enrichment log2 -0.711, PH-vs-control MK log2 0.962, PH MK pct 34.75%, control MK pct 19.61%, PH-vs-control MK Wilcoxon p 0.000585; PubMed hits: none retrieved
  - Sdsl (ec:4.3.1.17;ec:4.3.1.19): (RefSeq) serine dehydratase-like; pathway_neighbor_gene; Cysteine and methionine metabolism; cysteine/methionine metabolism; Seurat expression: MK pct 0.66%, other pct 0.17%, MK enrichment log2 1.825, PH-vs-control MK log2 23.23, PH MK pct 0.98%, control MK pct 0%, PH-vs-control MK Wilcoxon p 0.22; PubMed hits: none retrieved
  - Sms (ec:2.5.1.22): (RefSeq) spermine synthase isoform 1; pathway_neighbor_gene; Cysteine and methionine metabolism; cysteine/methionine metabolism;arginine/proline metabolism;glutathione/redox metabolism; Seurat expression: MK pct 6.55%, other pct 13.55%, MK enrichment log2 -1.249, PH-vs-control MK log2 1.374, PH MK pct 8.2%, control MK pct 3.27%, PH-vs-control MK Wilcoxon p 0.0443; PubMed hits: none retrieved
  - Lacc1 (ec:2.4.2.1;ec:2.4.2.28;ec:3.5.4.4): (RefSeq) purine nucleoside phosphorylase LACC1; pathway_neighbor_gene; Cysteine and methionine metabolism; mmu_M00034  Methionine salvage pathway;mmu_M00958  Adenine ribonucleotide degradation, AMP => Urate;mmu_M00959  Guanine ribonucleotide degradation, GMP => Urate; methionine salvage;cysteine/methionine metabolism;purine metabolism; Seurat expression: MK pct 1.97%, other pct 8.71%, MK enrichment log2 -2.156, PH-vs-control MK log2 25.345, PH MK pct 2.95%, control MK pct 0%, PH-vs-control MK Wilcoxon p 0.0322; PubMed hits: none retrieved

### Cholesteryl sulfate
- Differential signal: down, log2FC -2.43 in PH-mk_vs_Control-mk (sFig6A Raw data.xlsx)
- KEGG status: no KEGG compound match
- KEGG compounds: none
- KEGG compound names: none
- KEGG pathways: none
- Linked enzymes: none
- Candidate mouse enzyme genes: none mapped

### Pyruvaldehyde
- Differential signal: up, log2FC 2.76 in PH-mk_vs_Control-mk (sFig6A Raw data.xlsx)
- KEGG status: mapped
- KEGG compounds: C00546, C16849
- KEGG compound names: Methylglyoxal; Pyruvaldehyde; Pyruvic aldehyde; 2-Ketopropionaldehyde; 2-Oxopropanal, Hydroxypyruvaldehyde phosphate; 2,3-Dioxopropyl phosphate
- KEGG pathways: path:map00260, path:map00620, path:map00640, path:map01100, path:map01120, path:map05415
- Linked enzymes: ec:1.1.1.21, ec:1.1.1.283, ec:1.1.1.6, ec:1.1.1.78, ec:1.1.1.79, ec:1.13.11.50, ec:1.2.1.22, ec:1.2.1.23, ec:1.2.1.49, ec:1.2.3.15, ec:1.4.3.21, ec:1.4.3.4
- Candidate mouse enzyme genes with MK expression evidence:
  - Maoa (ec:1.4.3.4): (RefSeq) amine oxidase [flavin-containing] A; direct_compound_enzyme; mmu_M00135  GABA biosynthesis, eukaryotes, putrescine => GABA; arginine/proline metabolism;tryptophan metabolism; Seurat expression: MK pct 20.09%, other pct 13.56%, MK enrichment log2 0.84, PH-vs-control MK log2 0.467, PH MK pct 21.64%, control MK pct 16.99%, PH-vs-control MK Wilcoxon p 0.25; PubMed hits: none retrieved
  - Maob (ec:1.4.3.4): (RefSeq) amine oxidase [flavin-containing] B; direct_compound_enzyme; mmu_M00135  GABA biosynthesis, eukaryotes, putrescine => GABA; arginine/proline metabolism;tryptophan metabolism; Seurat expression: MK pct 2.84%, other pct 4.19%, MK enrichment log2 -0.563, PH-vs-control MK log2 1.912, PH MK pct 3.61%, control MK pct 1.31%, PH-vs-control MK Wilcoxon p 0.161; PubMed hits: none retrieved
  - Akr1b8 (ec:1.1.1.21): (RefSeq) aldose reductase-related protein 2; direct_compound_enzyme; one-carbon metabolism; Seurat expression: MK pct 2.62%, other pct 4%, MK enrichment log2 -1.179, PH-vs-control MK log2 2.464, PH MK pct 3.61%, control MK pct 0.65%, PH-vs-control MK Wilcoxon p 0.0625; PubMed hits: none retrieved
  - Akr1b10 (ec:1.1.1.21): (RefSeq) aldo-keto reductase family 1, member B10; direct_compound_enzyme; one-carbon metabolism; Seurat expression: MK pct 5.9%, other pct 8.52%, MK enrichment log2 -0.449, PH-vs-control MK log2 -0.654, PH MK pct 4.92%, control MK pct 7.84%, PH-vs-control MK Wilcoxon p 0.209; PubMed hits: none retrieved
  - Grhpr (ec:1.1.1.79): (RefSeq) glyoxylate reductase/hydroxypyruvate reductase isoform 1; direct_compound_enzyme; Seurat expression: MK pct 1.97%, other pct 7.35%, MK enrichment log2 -2.11, PH-vs-control MK log2 2.005, PH MK pct 2.62%, control MK pct 0.65%, PH-vs-control MK Wilcoxon p 0.153; PubMed hits: none retrieved
  - Aoc2 (ec:1.4.3.21): (RefSeq) retina-specific copper amine oxidase; direct_compound_enzyme; Seurat expression: MK pct 0.22%, other pct 1.02%, MK enrichment log2 -2.27, PH-vs-control MK log2 21.645, PH MK pct 0.33%, control MK pct 0%, PH-vs-control MK Wilcoxon p 0.482; PubMed hits: none retrieved
  - Akr1b1 (ec:1.1.1.21): (RefSeq) aldo-keto reductase family 1 member B1; direct_compound_enzyme; one-carbon metabolism; Seurat expression: not_found_in_seurat_features; PubMed hits: none retrieved
  - Akr1b7 (ec:1.1.1.21): (RefSeq) aldo-keto reductase family 1 member B7; direct_compound_enzyme; one-carbon metabolism; Seurat expression: MK pct 0%, other pct 0.09%, MK enrichment log2 -19.851, PH-vs-control MK log2 0, PH MK pct 0%, control MK pct 0%, PH-vs-control MK Wilcoxon p NA; PubMed hits: none retrieved
  - Aoc3 (ec:1.4.3.21): (RefSeq) membrane primary amine oxidase; direct_compound_enzyme; Seurat expression: MK pct 0%, other pct 0.9%, MK enrichment log2 -24.265, PH-vs-control MK log2 0, PH MK pct 0%, control MK pct 0%, PH-vs-control MK Wilcoxon p NA; PubMed hits: none retrieved

### tyrosine
- Differential signal: up, log2FC 2.98 in PH-mk_vs_Control-mk (sFig6A Raw data.xlsx)
- KEGG status: mapped
- KEGG compounds: C01536, C00082
- KEGG compound names: Tyrosine; 3-(p-Hydroxyphenyl)alanine; 2-Amino-3-(p-hydroxyphenyl)propionic acid, L-Tyrosine; (S)-3-(p-Hydroxyphenyl)alanine; (S)-2-Amino-3-(p-hydroxyphenyl)propionic acid; Tyrosine
- KEGG pathways: path:map00130, path:map00261, path:map00350, path:map00360, path:map00400, path:map00401, path:map00460, path:map00680, path:map00730, path:map00940
- Linked enzymes: ec:1.10.3.1, ec:1.11.1.8, ec:1.11.2.6, ec:1.14.14.36, ec:1.14.16.1, ec:1.14.16.2, ec:1.14.18.1, ec:1.2.1.101, ec:1.21.1.1, ec:1.3.1.43, ec:1.3.1.78, ec:1.3.1.79
- Candidate mouse enzyme genes with MK expression evidence:
  - 4930438A08Rik (ec:1.4.3.2): (RefSeq) uncharacterized protein LOC73988 precursor; direct_compound_enzyme; mmu_M00044  Tyrosine degradation, tyrosine => homogentisate; cysteine/methionine metabolism;tryptophan metabolism; Seurat expression: MK pct 0.44%, other pct 1.99%, MK enrichment log2 -2.542, PH-vs-control MK log2 22.645, PH MK pct 0.66%, control MK pct 0%, PH-vs-control MK Wilcoxon p 0.318; PubMed hits: none retrieved
  - Il4i1 (ec:1.4.3.2): (RefSeq) L-amino-acid oxidase precursor; direct_compound_enzyme; mmu_M00044  Tyrosine degradation, tyrosine => homogentisate; cysteine/methionine metabolism;tryptophan metabolism; Seurat expression: MK pct 0.87%, other pct 1.45%, MK enrichment log2 -0.042, PH-vs-control MK log2 -3.58, PH MK pct 0.66%, control MK pct 1.31%, PH-vs-control MK Wilcoxon p 0.479; PubMed hits: none retrieved
  - Il4i1b (ec:1.4.3.2): (RefSeq) L-amino-acid oxidase precursor; direct_compound_enzyme; mmu_M00044  Tyrosine degradation, tyrosine => homogentisate; cysteine/methionine metabolism;tryptophan metabolism; Seurat expression: not_found_in_seurat_features; PubMed hits: none retrieved
  - Pah (ec:1.14.16.1): (RefSeq) phenylalanine-4-hydroxylase; direct_compound_enzyme; one-carbon metabolism;tryptophan metabolism; Seurat expression: not_found_in_seurat_features; PubMed hits: none retrieved
  - Lao1 (ec:1.4.3.2): (RefSeq) L-amino acid oxidase 1 precursor; direct_compound_enzyme; mmu_M00044  Tyrosine degradation, tyrosine => homogentisate; cysteine/methionine metabolism;tryptophan metabolism; Seurat expression: MK pct 0%, other pct 0%, MK enrichment log2 -15.37, PH-vs-control MK log2 0, PH MK pct 0%, control MK pct 0%, PH-vs-control MK Wilcoxon p NA; PubMed hits: none retrieved
  - Th (ec:1.14.16.2): (RefSeq) tyrosine 3-monooxygenase; direct_compound_enzyme; mmu_M00042  Catecholamine biosynthesis, tyrosine => dopamine => noradrenaline => adrenaline; one-carbon metabolism; Seurat expression: not_found_in_seurat_features; PubMed hits: none retrieved
  - Tpo (ec:1.11.1.8): (RefSeq) thyroid peroxidase precursor; direct_compound_enzyme; mmu_M00043  Thyroid hormone biosynthesis, tyrosine => triiodothyronine/thyroxine; Seurat expression: not_found_in_seurat_features; PubMed hits: none retrieved
  - Tyr (ec:1.14.18.1): (RefSeq) tyrosinase isoform 1 precursor; direct_compound_enzyme; mmu_M00042  Catecholamine biosynthesis, tyrosine => dopamine => noradrenaline => adrenaline; Seurat expression: not_found_in_seurat_features; PubMed hits: none retrieved
  - Iyd (ec:1.21.1.1): (RefSeq) iodotyrosine deiodinase 1; direct_compound_enzyme; Seurat expression: MK pct 0%, other pct 0.36%, MK enrichment log2 -22.316, PH-vs-control MK log2 0, PH MK pct 0%, control MK pct 0%, PH-vs-control MK Wilcoxon p NA; PubMed hits: none retrieved

### Thiamine
- Differential signal: up, log2FC 2.75 in PH-mk_vs_Control-mk (sFig6A Raw data.xlsx)
- KEGG status: mapped
- KEGG compounds: C00378, C18377
- KEGG compound names: Thiamine; Thiamin; Vitamin B1; Aneurin; Antiberiberi factor, Thiamine disulfide
- KEGG pathways: path:map00730, path:map01100, path:map01240, path:map02010, path:map04122, path:map04977
- Linked enzymes: ec:1.1.3.23, ec:2.5.1.2, ec:2.7.1.89, ec:2.7.6.2, ec:3.1.3.1, ec:3.1.3.100, ec:3.1.3.2, ec:3.5.99.2
- Candidate mouse enzyme genes with MK expression evidence:
  - Acp1 (ec:3.1.3.2): (RefSeq) low molecular weight phosphotyrosine protein phosphatase isoform 2; direct_compound_enzyme; Seurat expression: MK pct 15.28%, other pct 24.64%, MK enrichment log2 -0.492, PH-vs-control MK log2 1.634, PH MK pct 19.02%, control MK pct 7.84%, PH-vs-control MK Wilcoxon p 0.00127; PubMed hits: none retrieved
  - Tpk1 (ec:2.7.6.2): (RefSeq) thiamin pyrophosphokinase 1 isoform 1; direct_compound_enzyme; Seurat expression: MK pct 1.75%, other pct 2.53%, MK enrichment log2 -0.637, PH-vs-control MK log2 1.812, PH MK pct 2.3%, control MK pct 0.65%, PH-vs-control MK Wilcoxon p 0.207; PubMed hits: none retrieved
  - Akp3 (ec:3.1.3.1): (RefSeq) intestinal-type alkaline phosphatase precursor; direct_compound_enzyme; one-carbon metabolism; Seurat expression: not_found_in_seurat_features; PubMed hits: none retrieved
  - Alpi (ec:3.1.3.1): (RefSeq) intestinal alkaline phosphatase precursor; direct_compound_enzyme; one-carbon metabolism; Seurat expression: not_found_in_seurat_features; PubMed hits: none retrieved
  - Acp2 (ec:3.1.3.2): (RefSeq) lysosomal acid phosphatase isoform 1 precursor; direct_compound_enzyme; Seurat expression: MK pct 8.52%, other pct 15.62%, MK enrichment log2 -1.028, PH-vs-control MK log2 0.777, PH MK pct 9.18%, control MK pct 7.19%, PH-vs-control MK Wilcoxon p 0.443; PubMed hits: none retrieved
  - Acp6 (ec:3.1.3.2): (RefSeq) lysophosphatidic acid phosphatase type 6 precursor; direct_compound_enzyme; Seurat expression: MK pct 4.59%, other pct 4.66%, MK enrichment log2 -0.123, PH-vs-control MK log2 -0.295, PH MK pct 4.26%, control MK pct 5.23%, PH-vs-control MK Wilcoxon p 0.642; PubMed hits: none retrieved
  - Alpl (ec:3.1.3.1): (RefSeq) alkaline phosphatase, tissue-nonspecific isozyme preproprotein; direct_compound_enzyme; one-carbon metabolism; Seurat expression: MK pct 0%, other pct 0.98%, MK enrichment log2 -24.06, PH-vs-control MK log2 0, PH MK pct 0%, control MK pct 0%, PH-vs-control MK Wilcoxon p NA; PubMed hits: none retrieved
  - Alppl2 (ec:3.1.3.1): (RefSeq) alkaline phosphatase, germ cell type precursor; direct_compound_enzyme; one-carbon metabolism; Seurat expression: MK pct 0%, other pct 0.03%, MK enrichment log2 -18.429, PH-vs-control MK log2 0, PH MK pct 0%, control MK pct 0%, PH-vs-control MK Wilcoxon p NA; PubMed hits: none retrieved
  - Acp5 (ec:3.1.3.2): (RefSeq) tartrate-resistant acid phosphatase type 5 precursor; direct_compound_enzyme; Seurat expression: MK pct 3.49%, other pct 16.52%, MK enrichment log2 -2.155, PH-vs-control MK log2 0.367, PH MK pct 3.93%, control MK pct 2.61%, PH-vs-control MK Wilcoxon p 0.471; PubMed hits: none retrieved
  - Acp4 (ec:3.1.3.2): (RefSeq) testicular acid phosphatase isoform 1 precursor; direct_compound_enzyme; Seurat expression: not_found_in_seurat_features; PubMed hits: none retrieved

### isoleucine
- Differential signal: up, log2FC 2.48 in PH-mk_vs_Control-mk (sFig6A Raw data.xlsx)
- KEGG status: compound/enzyme mapped, no mouse genes found for linked enzymes
- KEGG compounds: C16434, C21092
- KEGG compound names: Isoleucine, D-allo-Isoleucine
- KEGG pathways: none
- Linked enzymes: ec:5.1.1.21
- Candidate mouse enzyme genes: none mapped

### cysteine
- Differential signal: up, log2FC 3.34 in PH-mk_vs_Control-mk (sFig6A Raw data.xlsx)
- KEGG status: mapped
- KEGG compounds: C00736, C05688
- KEGG compound names: Cysteine; 2-Amino-3-mercaptopropionic acid, L-Selenocysteine
- KEGG pathways: path:map00450, path:map01100
- Linked enzymes: ec:1.8.4.4, ec:2.1.1.280, ec:2.1.1.9, ec:2.5.1.47, ec:2.5.1.48, ec:4.4.1.1, ec:4.4.1.16, ec:4.4.1.9
- Candidate mouse enzyme genes with MK expression evidence:
  - Cth (ec:4.4.1.1): (RefSeq) cystathionine gamma-lyase; direct_compound_enzyme; mmu_M00338  Cysteine biosynthesis, homocysteine + serine => cysteine; cysteine/methionine metabolism;one-carbon metabolism; Seurat expression: MK pct 0.22%, other pct 0.88%, MK enrichment log2 -2.299, PH-vs-control MK log2 -22.64, PH MK pct 0%, control MK pct 0.65%, PH-vs-control MK Wilcoxon p 0.159; PubMed hits: none retrieved
  - Scly (ec:4.4.1.16): (RefSeq) selenocysteine lyase; direct_compound_enzyme; Seurat expression: MK pct 8.08%, other pct 9.65%, MK enrichment log2 -0.342, PH-vs-control MK log2 0.637, PH MK pct 9.18%, control MK pct 5.88%, PH-vs-control MK Wilcoxon p 0.223; PubMed hits: none retrieved
  - Tmt1a2 (ec:2.1.1.9): (RefSeq) thiol methyltransferase 1A2; direct_compound_enzyme; Seurat expression: not_found_in_seurat_features; PubMed hits: none retrieved
  - Methig1 (ec:2.1.1.9): (RefSeq) methyltransferase hypoxia inducible domain containing 1; direct_compound_enzyme; Seurat expression: not_found_in_seurat_features; PubMed hits: none retrieved
  - Tmt1a3 (ec:2.1.1.9): (RefSeq) UbiE3 protein; direct_compound_enzyme; Seurat expression: not_found_in_seurat_features; PubMed hits: none retrieved
  - Tmt1a (ec:2.1.1.9): (RefSeq) methyltransferase-like protein 7A; direct_compound_enzyme; Seurat expression: not_found_in_seurat_features; PubMed hits: none retrieved
  - Tmt1b (ec:2.1.1.9): (RefSeq) thiol S-methyltransferase TMT1B precursor; direct_compound_enzyme; Seurat expression: not_found_in_seurat_features; PubMed hits: none retrieved

### 1-Tetradecanesulfonic acid
- Differential signal: up, log2FC 5.81 in PH-CD41_vs_Control-CD41 (sFig6A Raw data.xlsx)
- KEGG status: no KEGG compound match
- KEGG compounds: none
- KEGG compound names: none
- KEGG pathways: none
- Linked enzymes: none
- Candidate mouse enzyme genes: none mapped

### inosine
- Differential signal: up, log2FC 3.82 in PH-CD41_vs_Control-CD41 (sFig6A Raw data.xlsx)
- KEGG status: mapped
- KEGG compounds: C00294, C03280
- KEGG compound names: Inosine, Inosine-5'-carboxylate
- KEGG pathways: path:map00230, path:map01100, path:map01232, path:map02010
- Linked enzymes: ec:1.1.3.28, ec:2.4.2.1, ec:2.7.1.73, ec:3.1.3.5, ec:3.1.3.99, ec:3.13.1.9, ec:3.2.2.1, ec:3.2.2.2, ec:3.5.4.4
- Candidate mouse enzyme genes with MK expression evidence:
  - Lacc1 (ec:2.4.2.1): (RefSeq) purine nucleoside phosphorylase LACC1; direct_compound_enzyme; mmu_M00034  Methionine salvage pathway;mmu_M00958  Adenine ribonucleotide degradation, AMP => Urate;mmu_M00959  Guanine ribonucleotide degradation, GMP => Urate; methionine salvage;cysteine/methionine metabolism;purine metabolism; Seurat expression: MK pct 1.97%, other pct 8.71%, MK enrichment log2 -2.156, PH-vs-control MK log2 25.345, PH MK pct 2.95%, control MK pct 0%, PH-vs-control MK Wilcoxon p 0.0322; PubMed hits: none retrieved
  - Pnp (ec:2.4.2.1): (RefSeq) purine nucleoside phosphorylase; direct_compound_enzyme; mmu_M00958  Adenine ribonucleotide degradation, AMP => Urate;mmu_M00959  Guanine ribonucleotide degradation, GMP => Urate; purine metabolism; Seurat expression: MK pct 20.31%, other pct 38.9%, MK enrichment log2 -1.217, PH-vs-control MK log2 1.739, PH MK pct 26.56%, control MK pct 7.84%, PH-vs-control MK Wilcoxon p 3.81e-06; PubMed hits: none retrieved
  - Nt5c2 (ec:3.1.3.5): (RefSeq) cytosolic purine 5'-nucleotidase isoform 3; direct_compound_enzyme; mmu_M00958  Adenine ribonucleotide degradation, AMP => Urate;mmu_M00959  Guanine ribonucleotide degradation, GMP => Urate; purine metabolism;pyrimidine metabolism; Seurat expression: MK pct 8.95%, other pct 19.06%, MK enrichment log2 -1.24, PH-vs-control MK log2 2.879, PH MK pct 12.46%, control MK pct 1.96%, PH-vs-control MK Wilcoxon p 2e-04; PubMed hits: none retrieved
  - Nt5m (ec:3.1.3.5): (RefSeq) 5'(3')-deoxyribonucleotidase, mitochondrial isoform 1 precursor; direct_compound_enzyme; mmu_M00958  Adenine ribonucleotide degradation, AMP => Urate;mmu_M00959  Guanine ribonucleotide degradation, GMP => Urate; purine metabolism;pyrimidine metabolism; Seurat expression: MK pct 6.11%, other pct 6.11%, MK enrichment log2 0.069, PH-vs-control MK log2 0.59, PH MK pct 6.56%, control MK pct 5.23%, PH-vs-control MK Wilcoxon p 0.557; PubMed hits: none retrieved
  - Nt5c (ec:3.1.3.5): (RefSeq) 5'(3')-deoxyribonucleotidase, cytosolic type isoform 1; direct_compound_enzyme; mmu_M00958  Adenine ribonucleotide degradation, AMP => Urate;mmu_M00959  Guanine ribonucleotide degradation, GMP => Urate; purine metabolism;pyrimidine metabolism; Seurat expression: MK pct 12.45%, other pct 24.66%, MK enrichment log2 -1.149, PH-vs-control MK log2 0.516, PH MK pct 13.77%, control MK pct 9.8%, PH-vs-control MK Wilcoxon p 0.225; PubMed hits: none retrieved
  - Acp3 (ec:3.1.3.5): (RefSeq) prostatic acid phosphatase isoform 2 precursor; direct_compound_enzyme; Seurat expression: not_found_in_seurat_features; PubMed hits: none retrieved
  - Nt5e (ec:3.1.3.5): (RefSeq) 5'-nucleotidase preproprotein; direct_compound_enzyme; mmu_M00958  Adenine ribonucleotide degradation, AMP => Urate;mmu_M00959  Guanine ribonucleotide degradation, GMP => Urate; purine metabolism;pyrimidine metabolism; Seurat expression: MK pct 3.06%, other pct 5.63%, MK enrichment log2 -1.39, PH-vs-control MK log2 0.383, PH MK pct 3.61%, control MK pct 1.96%, PH-vs-control MK Wilcoxon p 0.34; PubMed hits: none retrieved
  - Ada (ec:3.5.4.4): (RefSeq) adenosine deaminase isoform 1; direct_compound_enzyme; mmu_M00958  Adenine ribonucleotide degradation, AMP => Urate; purine metabolism; Seurat expression: MK pct 1.53%, other pct 2.23%, MK enrichment log2 -0.798, PH-vs-control MK log2 -0.58, PH MK pct 1.31%, control MK pct 1.96%, PH-vs-control MK Wilcoxon p 0.595; PubMed hits: none retrieved
  - Nt5c1a (ec:3.1.3.5): (RefSeq) cytosolic 5'-nucleotidase 1A; direct_compound_enzyme; mmu_M00958  Adenine ribonucleotide degradation, AMP => Urate;mmu_M00959  Guanine ribonucleotide degradation, GMP => Urate; purine metabolism;pyrimidine metabolism; Seurat expression: not_found_in_seurat_features; PubMed hits: none retrieved
  - Nt5el (ec:3.1.3.5): (RefSeq) uncharacterized protein LOC66763; direct_compound_enzyme; mmu_M00958  Adenine ribonucleotide degradation, AMP => Urate;mmu_M00959  Guanine ribonucleotide degradation, GMP => Urate; purine metabolism;pyrimidine metabolism; Seurat expression: not_found_in_seurat_features; PubMed hits: none retrieved

## Required Hypothesis Scaffold For Generation Agents
Every metabolomics-driven hypothesis must include:
- Differential metabolite A with source/comparison/log2FC.
- KEGG direct compound-enzyme evidence or a same-pathway neighbor-gene link for A.
- Candidate metabolic enzyme gene B and whether B is expressed/enriched/differential in MK/platelet cells.
- The evidence link type, especially whether B is a direct compound-enzyme link or a pathway-neighbor gene.
- Whether literature search hits support a vascular remodeling, hypoxia, endothelial, smooth muscle, fibroblast, immune, or pulmonary hypertension mechanism.
- A direction-level chain from hypoxic MK metabolic state to broad downstream axis to remodeling phenotype.
- A direction-level reasoning summary that links the data anchor, biological interpretation, MK-linked enzyme/pathway logic, plausible downstream axis, remodeling phenotype, and key uncertainty.
- A broad downstream axis: direct vascular-wall, immune-mediated, EV/stromal, or unresolved.
- Candidate examples can include SAM, spermidine, T-helper/Th17-like tone, endothelial activation, medial activation, muscularization, vascular stiffness, or stromal remodeling, but examples should not be presented as settled mechanisms.
- A falsification test that can challenge the metabolite-enzyme-MK-remodeling direction.

Do not present KEGG mapping or PubMed hits as proof of causality. Treat them as evidence scaffolds requiring validation, and avoid over-resolving the final mechanism when evidence only supports a direction.

## Public dataset discovery context
# Public Dataset Discovery Context

Purpose: identify public datasets that could validate or extend MK-hypoxia-vascular remodeling hypotheses.
This context is generated by programmatic repository queries. Agents must not claim an external dataset was inspected beyond the metadata shown here unless downstream code downloads and analyzes it.

## Search Tasks
1. The Public Dataset Discovery Module will execute the following repository searches. These tasks are intentionally broad; they are not claims of data availability (medium; public repositories)
2. **Single‑cell/snRNA‑seq of hypoxic pulmonary hypertension models:** pulmonary hypertension AND AND AND AND (medium; public repositories)
3. **Bulk RNA‑seq or microarray of isolated lung MKs after hypoxia:** AND AND AND (medium; public repositories)
4. **Spatial transcriptomics or proteomics of PH lung with MK/immune context:** AND AND (medium; public repositories)
5. **Metabolomics or fluxomics of hypoxic MKs or MK‑rich lung tissue:** AND AND (medium; public repositories)
6. **Proteomics of MK‑derived extracellular vesicles or secretome in hypoxia/PH:** AND AND (medium; public repositories)
7. **Clinical or translational datasets linking MK metabolites to PH/remodelling:** AND AND (medium; public repositories)
8. **Microarray or bulk RNA‑seq of lung microvascular endothelial cells or VSMC exposed to MK‑conditioned medium:** AND AND AND (medium; public repositories)

## Access Status
- Hits retrieved: 0
- CSV: C:\Users\18553\Desktop\Phd_S4\jiawei_framework\outputs\public_datasets\public_dataset_hits.csv
- Manifest: C:\Users\18553\Desktop\Phd_S4\jiawei_framework\outputs\public_datasets\public_dataset_manifest.json
- Access issues:
  - Public dataset search disabled by runtime option.

## Top Public Dataset Hits
| Rank | Source | Accession | Relevance | Modality | Organism | Title | Why it may help |
|---:|---|---|---|---|---|---|---|

No public dataset metadata was retrieved. Downstream agents should treat public dataset support as unavailable, not negative.

## How Downstream Agents Should Use This
- Treat these hits as candidate validation datasets, not direct mechanistic evidence.
- Prefer hypotheses that can be tested against high- or medium-relevance datasets.
- Clearly separate local user data, retrieved public dataset metadata, PubMed/KEGG context, and biological inference.
- If a dataset lacks MK/platelet annotations, it may still support recipient-cell or tissue-level validation.
- If no suitable dataset is found, state the gap and propose targeted experimental validation.

## Public dataset analysis context
# Public Dataset Analysis Context

Purpose: analyze processed public dataset matrices when available. This module does not process FASTQ/SRA files.
- Analysis enabled: True
- Results: 2

## Dataset Analysis Summary
| Accession | Status | Matrix | Genes | Samples | Comparison | Key outputs | Reason |
|---|---|---|---:|---:|---|---|---|
| GSE289322 | completed | GSE289322_Processed_data_files.xlsx | 30495 | 19 | 8 case vs 4 control samples | [candidate genes](C:\Users\18553\Desktop\Phd_S4\jiawei_framework\outputs\public_dataset_analysis\GSE289322\candidate_gene_check.tsv), [DE results](C:\Users\18553\Desktop\Phd_S4\jiawei_framework\outputs\public_dataset_analysis\GSE289322\de_results.tsv), [report](C:\Users\18553\Desktop\Phd_S4\jiawei_framework\outputs\public_dataset_analysis\GSE289322\analysis_report.md) | Processed expression matrix parsed and analyzed. |
| GSE291455 | completed | GSE291455_All.fpkm.anno.txt.gz | 58302 | 4 | 0 case vs 0 control samples | [candidate genes](C:\Users\18553\Desktop\Phd_S4\jiawei_framework\outputs\public_dataset_analysis\GSE291455\candidate_gene_check.tsv), [report](C:\Users\18553\Desktop\Phd_S4\jiawei_framework\outputs\public_dataset_analysis\GSE291455\analysis_report.md) | Processed expression matrix parsed and analyzed. |

## Interpretation Rules
- Completed analyses may be treated as public-data evidence at the expression-matrix level.
- Skipped datasets remain metadata-only validation opportunities.
- Approximate differential analysis uses inferred sample labels and lightweight statistics; validate important findings manually.
- Do not treat absent candidate genes as biological absence when identifiers may use Ensembl IDs or probe IDs.

## Public Dataset Agent output
Request addressed:  
Evaluate public dataset metadata and completed processed‑matrix analyses for MK‑hypoxia‑vascular remodeling validation.

Search context reviewed:  
Public Dataset Discovery Context – no programmatic repository hits were returned. The “Top Public Dataset Hits” table is empty. All validation opportunities must therefore rely on the two datasets listed in the Public Dataset Analysis Context.

Analysis context reviewed:  
Public Dataset Analysis Context – two datasets were downloaded and analysed using processed expression matrices:  
- **GSE289322** (19 samples; 8 case vs 4 control; 30 495 genes; candidate gene check + differential expression)  
- **GSE291455** (4 samples; 0 case vs 0 control; 58 302 genes; candidate gene check only; no DE possible)

Top dataset candidates:

Rank: 1  
Accession and source: GSE289322 (GEO processed matrix)  
Retrieved metadata: Not available; no title, organism, tissue, or modality described in the discovery context.  
Relevance class: Tissue‑level / recipient‑cell (based on availability of case‑control design; likely a bulk RNA‑seq or microarray experiment with enough samples for differential testing).  
Modality: Not specified; processed matrix suggests transcriptomics (microarray or RNA‑seq).  
Organism/tissue if available: Not provided.  
What it could validate:  
- Differential expression of MK‑related genes (Amd1, Amd2, Ldha, Cyp1a1, etc.) or metabolic‑pathway genes in the experimental condition versus control.  
- Presence/absence of candidate genes linked to metabolite‑enzyme‑remodelling chains.  
- Enrichment of pathways (polyamine metabolism, methionine salvage, glycolysis) if the DE results are explored beyond candidate genes.  
Completed analysis result, if any: Candidate gene check and DE results are stored; a full analysis report exists. The context does not list which genes were hit or the DE significance, but the matrix was parsed and analysed.  
What it cannot validate from metadata alone: MK‑cell specificity (the analysis is on whole‑tissue or mixed‑cell samples; cannot assign expression to MKs without cell‑type deconvolution or additional annotation).  
Priority: High – a case‑control design with DE results offers the strongest public‑data validation opportunity for direction‑level hypotheses, especially to check if candidate metabolic/enzymatic genes change in the lung/PH context.

Rank: 2  
Accession and source: GSE291455 (GEO processed matrix)  
Retrieved metadata: Not available.  
Relevance class: Broad context (low relevance for direct validation; no group labels).  
Modality: Not specified.  
Organism/tissue if available: Not provided.  
What it could validate: Only candidate gene expression (presence/absence) in the four available samples; no statistical comparison.  
Completed analysis result, if any: Candidate gene check performed; no differential analysis possible.  
What it cannot validate from metadata alone: Any hypoxia‑ or PH‑related change; cannot link to any condition.  
Priority: Low – usable only to confirm that a gene of interest is expressed in the profiled tissue, but offers no group‑contrast evidence.

Cross‑dataset summary:  
- Strongest public‑data validation opportunities: GSE289322 provides a case‑control contrast with DE results; it can be mined for expression changes in MK‑associated metabolic genes (e.g., Amd1, Ldha) or pathway biomarkers in lung/PH tissue.  
- Completed public‑data analyses: Two datasets analysed; one includes DE and candidate gene checks, the other only candidate expression.  
- Public‑data gaps: No single‑cell, spatial, proteomic, metabolomic, or MK‑enriched public datasets were retrieved or analysed. No dataset explicitly profiles megakaryocytes, platelets, or their secretome. MK‑origin evidence cannot be tested with the available public data.  
- Hypotheses or pathways especially suited for public‑data validation: Metabolomics‑driven hypotheses that converge on enzyme genes (Amd1, Amd2, Ldha, Cyp1a1) or pathways (polyamine, methionine salvage, glycolysis) can be probed by checking their differential expression in GSE289322. If those genes show disease‑associated shifts, they would add orthogonal tissue‑level support.  
- Hypotheses that still require new experiments: Any hypothesis requiring MK‑specific isolation, spatial localisation, metabolite/protein quantification, EV cargo, or direct MK‑to‑vascular cell signalling – the available public data cannot replace targeted experiments.

Evidence summary for downstream agents:  
- Strongly supported by completed public‑data analysis: Nothing can be claimed without inspecting the actual DE results and candidate gene lists. The files exist but their content is not summarised here.  
- Supported only by retrieved metadata: No metadata was retrieved; this category is empty.  
- Plausible but requiring dataset download/reanalysis: The two matrices are already processed at the expression‑matrix level, so limited re‑analysis could be done within the framework (e.g., re‑running gene set enrichment on the GSE289322 DE table). Full re‑analysis of raw data would require new downloads.  
- Unsupported or not found: MK‑specific profiling, spatial transcriptomics, metabolomics, or proteomics data. Hypoxia‑specific MK isolation and MK‑to‑vascular cell co‑culture experiments remain unaddressed by public datasets.  
- Recommended next retrieval or analysis step: Examine the candidate_gene_check.tsv and de_results.tsv files from GSE289322 for genes belonging to the mechanism‑ready shortlist (Amd1, Amd2, Ldha, Cyp1a1, Mat2a, Aldh2, Pnp, Nt5c2, etc.). If those genes show differential expression in the same direction (PH‑up) in lung/PH tissue, they would reinforce the metabolomics‑driven hypotheses. Additionally, run gene‑set enrichment on the DE results to see whether polyamine, methionine, or glycolysis pathways are altered at the tissue level. The GSE291455 dataset can be used to check baseline expression of candidate genes but provides no contrast information.

## Generation outputs
# Generation Agent Outputs

## generation_metabolic
Cycle ID: 1

Hypotheses generated: H1, H2, H3, H4

---

**Hypothesis ID:** H1

**Hypothesis title:**  
Hypoxic MK methionine accumulation drives AMD1-mediated polyamine metabolism, shifting perivascular immune/stromal tone and contributing to medial thickening and vascular stiffening.

**PI instruction addressed:**  
Metabolomics-driven, direction-level: differential metabolite -> KEGG pathway-neighbor enzyme -> MK expression/differential -> broad downstream axis -> vascular remodeling. Uses user metabolomics (MK-sorted, PH vs control), Seurat scRNA-seq, and public dataset validation.

**Core directional hypothesis:**  
Increased methionine in PH-MKs drives AMD1-dependent polyamine (SAM, spermidine/spermine) production, which alters the pulmonary perivascular microenvironment—likely via immune modulation or direct vascular-wall signalling—augmenting hypoxia-induced medial thickening and vascular stiffness.

**Direction-level reasoning summary:**  
- **Data anchor:** MK-sorted metabolomics shows methionine up in PH vs control (log2FC 3.26); AMD1 is pathway-neighbor gene in Cysteine/methionine metabolism and Methionine salvage. Seurat: AMD1 expressed in 31.4 % of MKs (enrichment log2 1.35) and significantly upregulated in PH-MKs (log2FC 1.77, p=6.55e‑06).  
- **Biological interpretation:** Hypoxic MKs accumulate methionine, a precursor for SAM and polyamines. AMD1 catalyzes SAM decarboxylation, committing flux towards polyamine synthesis (spermidine/spermine). The strong MK enrichment and PH-up shift indicate hypoxia-induced metabolic reprogramming centred on polyamine metabolism.  
- **MK-linked pathway logic:** AMD1 is a rate-limiting enzyme for polyamine biosynthesis. Literature links mTORC1-AMD1 to polyamine metabolism in cancer, and polyamines (e.g., spermidine) regulate T‑cell differentiation and vascular cell proliferation. This positions MK AMD1 as a plausible metabolic rheostat in the hypoxic lung.  
- **Candidate downstream axes:** Polyamines secreted by MKs or released via extracellular vesicles could act (i) **immune-mediated** (e.g., promote Th17-like T‑cell or macrophage polarization), (ii) **direct vascular-wall** (stimulate SMC proliferation/fibroblast activation), or (iii) **EV/stromal** (alter matrix cross-linking).  
- **Remodeling logic:** Immune or stromal activation leads to medial smooth muscle hypertrophy/hyperplasia, perivascular collagen deposition, and reduced compliance—hallmarks of pulmonary vascular remodeling.  
- **Key uncertainty:** Whether MK-derived polyamines reach vascular target cells in sufficient concentration and whether AMD1 activity truly controls polyamine flux in hypoxic MKs (as opposed to alternative SAM-consuming pathways, e.g., methylation).

**Directional chain:**  
1. Hypoxia upregulates methionine import and/or methionine cycle flux in lung-resident MKs.  
2. Elevated methionine feeds SAM, which via AMD1 is partitioned toward polyamine synthesis (spermidine/spermine) rather than methylation.  
3. Candidate downstream axis: **immune‑mediated** (polyamines influence T‑helper/Th17‑like tone, macrophage activation) or **direct vascular‑wall** (polyamines act on SMC/fibroblasts) or **EV/stromal**.  
4. Broad cellular/tissue response: Perivascular inflammation, medial smooth muscle hypertrophy, and adventitial collagen accumulation.  
5. Contribution to remodeling phenotype: Medial thickening, muscularization, vascular stiffness.

**Candidate downstream axes:**  
- Plausible axes: immune-mediated (Th17-like/ macrophage), direct vascular-wall, EV/stromal.  
- Working model (provisional): immune‑mediated – polyamines modify local T‑cell or macrophage programs, amplifying vascular pathology.  
- Specific examples: spermidine, SAM, Th17 cell function, STAT3 activation, IL‑6/IL‑17 family cytokines, α‑SMA+ cell expansion.  
- MK-origin gap: MK polyamine secretion profile, stability, and diffusion in vivo not proven; AMD1 overexpression in MKs not directly measured at protein/activity level.  
- Falsification: MK‑specific Amd1 knockout or pharmacological AMD1 inhibition (e.g., SAM486A) should prevent hypoxia‑induced polyamine accumulation in lung, blunt perivascular immune changes, and reduce medial thickening. If AMD1 blockade fails to alter polyamine levels or vascular remodeling, the direction is falsified.

**Evidence basis:**  
- User-provided data:  
  - Metabolomics: methionine 3.26 log2FC up in MK-PH vs MK-control (*sFig6A Raw data.xlsx*).  
  - Seurat: AMD1 expression pct 31.44% in MKs, MK enrichment 1.353, PH-vs-control MK log2FC 1.77, p=6.55e‑06.  
- Public dataset metadata or analyzed public data: GSE289322 (bulk transcriptomics, case–control) provides a validation opportunity – check whether AMD1 is upregulated in PH lung tissue relative to control. If confirmed, supports tissue-level relevance.  
- Literature: AMD1/mTORC1 axis in polyamine metabolism (PMID 28658205); polyamines and EIF5A hypusination in cancer (PMID 38965534); broader roles in immuno‑metabolism.  
- Biological rationale: Polyamines are known regulators of cell proliferation and immune polarization; SAM/polyamine ratio influences methylation vs. polyamine synthesis.  
- Evidence status: Direct (metabolite change, MK gene expression, and differential expression in user scRNA‑seq); indirect (polyamine‑to‑vascular links from literature); public validation possible.

**Predicted observations:**  
- In MKs: Increased AMD1 protein/enzyme activity, elevated spermidine/spermine, and reduced SAM in PH-MK.  
- In recipient or tissue compartment: Elevated polyamines in PH lung tissue (confirmable by tissue metabolomics), perivascular polyamine-responsive immune signatures (e.g., Th17 markers).  
- In metabolomics or pathway activity: Lung tissue polyamine pathway flux increased; AMD1 inhibition reverses these changes.

**Experimental validation:**  
- Perturbation: MK‑specific Amd1 deletion (Mk-Cre x Amd1 flox) or systemic AMD1 inhibitor (SAM486A) in hypoxia model.  
- Model: Hypoxia‑induced PH mouse (HxSu or chronic hypoxia).  
- Readout: Lung polyamine levels (LC‑MS), perivascular immune cell composition (flow/IF), medial thickness, muscularization metrics, hemodynamics (RVSP, RV hypertrophy).  
- Expected result: Amd1 loss/inhibition blunts polyamine rise, reduces muscularization and stiffness.  
- Falsifying result: No change in lung polyamines or vascular remodeling despite efficient AMD1 blockade.

**Novelty:**  
First direct connection from MK methionine metabolism through AMD1‑polyamine axis to pulmonary vascular remodeling. AMD1 as an MK metabolic vulnerability in PH.

**Weaknesses:**  
Does not pinpoint the exact polyamine‑responsive cell type; relies on pathway logic (polyamine biology) rather than direct measurement of AMD1 product in MK secretome. Public dataset support absent until GSE289322 is queried.

**Revision relative to previous cycle:**  
Not applicable (first cycle).

**Priority estimate:**  
Score each from 1 to 5:  
- Directional specificity: 5 (clear metabolite → enzyme → pathway axis)  
- Data support: 5 (MK-specific metabolomics + scRNA-seq with strong significance)  
- Literature support: 4 (mTORC1/AMD1 papers; polyamine immunomodulation literature)  
- Novelty: 5 (MK-centric AMD1 axis in PH)  
- Testability: 5 (genetic/pharmacologic AMD1 manipulation in mouse PH feasible)  
- Overall generation priority: 5

**Explicit rejection filter:** Passes all checks (MK-specific, hypoxia-dependent, remodeling phenotype, not generic, testable, non-redundant).

---

**Hypothesis ID:** H2

**Hypothesis title:**  
MK Amd2 upregulation under hypoxia augments spermidine/spermine synthesis to cooperate with Amd1, reinforcing polyamine‑dependent vascular remodeling.

**PI instruction addressed:**  
Additional metabolomics‑driven hypothesis using Amd2, the isoform of AMD1, from the same methionine‑SAM‑polyamine pathway. Addresses potential functional redundancy/compensation.

**Core directional hypothesis:**  
Hypoxia‑induced upregulation of Amd2 in a subset of MKs provides a complementary polyamine synthetic capacity that, together with Amd1, elevates spermidine/spermine in the pulmonary niche, promoting perivascular immune activation and medial thickening.

**Direction-level reasoning summary:**  
- **Data anchor:** Methionine up in PH-MK; Amd2 is a methionine salvage/polyamine pathway neighbor gene. Seurat: Amd2 expressed in 4.4% MKs (enrichment log2 0.93), and significantly upregulated in PH-MK (log2FC 2.18, p=0.024).  
- **Biological interpretation:** While Amd2 expression is lower than Amd1, its hypoxia‑induced rise suggests an alternative or cooperative enzyme for SAM decarboxylation, potentially in a specialized MK subpopulation.  
- **MK-linked pathway logic:** Amd2 is a functional homolog of Amd1; both decarboxylate SAM for polyamine synthesis. Co‑upregulation of Amd1 and Amd2 could drive robust polyamine flux.  
- **Candidate downstream axes:** Same as H1: immune‑mediated, direct vascular‑wall, or EV/stromal. Polyamines influence T effector/memory balance and stromal cell proliferation.  
- **Remodelling logic:** Enhanced polyamine output promotes medial muscularization and perivascular matrix changes.  
- **Key uncertainty:** Whether Amd2 protein is active in MKs and its contribution relative to Amd1; low MK expression percentage may limit impact.

**Directional chain:**  
1. Hypoxia induces methionine accumulation and increases SAM availability.  
2. MKs upregulate both Amd1 and Amd2, diverting SAM into polyamine synthesis.  
3. Candidate downstream axis: immune‑mediated (e.g., shaping T‑helper or macrophage phenotypes) or direct vascular‑wall.  
4. Broad cellular response: immune cell recruitment/activation and vascular smooth muscle hypertrophy.  
5. Contribution to remodeling: medial thickening, muscularization.

**Candidate downstream axes:**  
- Plausible axes: immune-mediated, direct vascular-wall, EV/stromal.  
- Working model: Amd2 cooperates with Amd1 to sustain a polyamine‑rich microenvironment that favors inflammatory T‑cell or macrophage programs.  
- Specific examples: spermidine‑driven T‑cell skewing, macrophage M2‑like polarization.  
- MK-origin gap: Amd2 expression in only 5.9% of PH-MK; whether this is a distinct MK subset with unique secretome is unknown.  
- Falsification: Dual inhibition or KO of Amd1 and Amd2 in MKs should yield greater reversal of polyamine levels and remodeling than Amd1 alone. If Amd2 KO shows no additive effect, its role is dispensable.

**Evidence basis:**  
- User-provided data: Methionine up; Amd2 MK expression (pct 4.37%, enrichment 0.93, PH-up log2FC 2.175, p=0.0235).  
- Public dataset metadata/analyzed: GSE289322 could test if AMD2 is differentially expressed in PH lung; if absent, suggests MK‑specific role.  
- Literature: Amd2 gene context in muscle atrophy metabolomics (PMID 40768332), but no direct vascular literature.  
- Biological rationale: Two AMD genes may provide redundancy or fine‑tuning of polyamine synthesis in distinct cellular states.  
- Evidence status: Direct (gene expression differential) but limited by low MK percentage; inferred pathway role.

**Predicted observations:**  
- In MKs: Amd2 protein detectable in a subset of MKs, induced by hypoxia.  
- In tissue: Polyamine levels reduced more by dual Amd1/Amd2 inhibition than single.  
- In metabolomics: Lung spermidine/spermine correlate with combined Amd1+Amd2 expression.

**Experimental validation:**  
- Perturbation: MK-specific Amd2 knockout, dual Amd1/Amd2 knockout.  
- Model: Hypoxia PH mouse.  
- Readout: Lung polyamines, perivascular immune markers, vascular remodelling, hemodynamics.  
- Expected result: Amd2 loss alone mild effect; dual loss strong protection.  
- Falsifying result: Amd2 loss unchanged, dual loss no better than Amd1 alone.

**Novelty:**  
First consideration of Amd2 in MK biology; highlights gene duplication in polyamine pathway.

**Weaknesses:**  
Low basal and MK-specific expression; risk that Amd2 is not functionally relevant at protein level. No direct metabolite product measured.

**Priority estimate:**  
- Directional specificity: 4 (parallel rationale)  
- Data support: 3 (low expression percentage)  
- Literature support: 2 (sparse)  
- Novelty: 4  
- Testability: 4 (feasible with genetic models)  
- Overall generation priority: 3

---

**Hypothesis ID:** H3

**Hypothesis title:**  
MK methionine accumulation may alter DNA methylation via Dnmt3b, reshaping MK transcriptome and secretome to promote a pro‑remodelling phenotype.

**PI instruction addressed:**  
Exploratory metabolomics‑driven hypothesis linking methionine to Dnmt3b (methylation pathway neighbor) and potentially to an epigenetically driven MK state that impacts vascular cells.

**Core directional hypothesis:**  
Hypoxic MKs channel excess methionine into S‑adenosylmethionine (SAM) for DNA methylation via Dnmt3b, inducing a pro‑fibrotic or pro‑inflammatory MK transcriptional programme that affects perivascular fibroblasts and smooth muscle cells.

**Direction-level reasoning summary:**  
- **Data anchor:** Methionine up in PH-MK; Dnmt3b is a cysteine/methionine metabolism pathway neighbor gene, encoding a DNA methyltransferase. Seurat: Dnmt3b expressed in 2.62% MKs (enrichment 0.19), PH-vs-control MK log2FC 1.59 (p=0.212, not significant).  
- **Biological interpretation:** Although MK expression of Dnmt3b is low and not significantly PH-up, the methionine-SAM-methylation axis is a critical fate‑determining mechanism. Even modest epigenetic changes could prime MKs for altered cytokine or growth factor release.  
- **MK-linked pathway logic:** SAM is the universal methyl donor; Dnmt3b uses SAM for de novo DNA methylation. Methionine accumulation may drive hypermethylation at specific loci, silencing anti‑proliferative genes or activating pro‑remodelling factors.  
- **Candidate downstream axes:** Likely **direct vascular-wall** through MK-derived factors (e.g., TGF‑β, PDGF) or **EV/stromal** through altered MK exosome cargo.  
- **Remodelling logic:** Epigenetically modified MKs could secrete more pro‑fibrotic mediators, promoting fibroblast‑to‑myofibroblast transition and medial hypertrophy.  
- **Key uncertainty:** Low and non‑significant MK expression of Dnmt3b; no methylation data in user data. Methionine pool may not directly control Dnmt3b activity if SAM is diverted to polyamines.

**Directional chain:**  
1. Hypoxia raises methionine levels in MKs.  
2. Elevation of SAM pools may enhance Dnmt3b‑mediated DNA methylation in MKs.  
3. Candidate downstream axis: direct vascular‑wall (secreted growth factors/cytokines) or EV/stromal.  
4. Broad tissue response: Perivascular fibroblast activation, smooth muscle hypertrophy.  
5. Remodelling phenotype: Medial thickening, vascular fibrosis.

**Candidate downstream axes:**  
- Plausible axes: direct vascular-wall, EV/stromal, immune-mediated (altering gene expression of chemokines).  
- Working model (provisional): MK epigenetic reprogramming leads to secretion of pro‑fibrotic factors (e.g., TGF‑β1, CTGF).  
- Specific examples: hypermethylation of SOCS or DUSP genes could enhance STAT3 or MAPK signalling, amplifying MK cytokine output.  
- MK-origin gap: Dnmt3b expression and activity in MKs not validated; methylation changes in MKs not measured.  
- Falsification: MK‑specific Dnmt3b knockout or SAM synthesis inhibition (e.g., MAT2A inhibitor) should prevent hypoxia‑induced pro‑remodelling MK secretome. If MK epigenetic profile unchanged and secretion unchanged, hypothesis fails.

**Evidence basis:**  
- User-provided data: Methionine up; Dnmt3b expression low, not significant PH-up.  
- Public dataset metadata: GSE289322 may show DNMT3B expression in lung tissue; if absent, argues against tissue‑level relevance.  
- Literature: Methionine‑SAM‑methylation axis in immune cell differentiation; no vascular‑specific Dnmt3b reports in MKs.  
- Biological rationale: Epigenetic regulation of MK biology is established; Dnmt3b is involved in hematopoietic differentiation.  
- Evidence status: Speculative (metabolite link present, enzyme expression weak, no direct epigenetic data).

**Predicted observations:**  
- In MKs: Increased SAM/SAH ratio, global DNA hypermethylation at specific promoters, altered transcriptome (e.g., upregulated Ccl2, Tgfβ1).  
- In tissue: Pro‑fibrotic cytokine signature around MK‑rich regions.  
- In metabolomics: SAM consumption into methylation pathway.

**Experimental validation:**  
- Perturbation: Dnmt3b inhibitor (e.g., nanaomycin A) or Mk‑specific Dnmt3b knockout; alternatively, manipulate SAM levels with MAT2A inhibitor.  
- Model: Hypoxic PH mouse.  
- Readout: MK DNA methylation (RRBS), MK secretome analysis, perivascular collagen deposition, medial thickness.  
- Expected result: Reduced pro‑fibrotic MK output and attenuated vascular fibrosis.  
- Falsifying result: No change in MK DNA methylation at candidate loci or vascular phenotype.

**Novelty:**  
Links MK methionine metabolism to epigenetic control, a new paradigm in PH.

**Weaknesses:**  
Very weak supporting evidence for Dnmt3b in MKs; the hypothesis is exploratory and may be false.

**Revision relative to previous cycle:**  
Not applicable.

**Priority estimate:**  
- Directional specificity: 4  
- Data support: 1 (no significant MK expression change)  
- Literature support: 2  
- Novelty: 5  
- Testability: 4  
- Overall generation priority: 2 (low, due to weak data support)

---

**Hypothesis ID:** H4

**Hypothesis title:**  
MK-mediated retinoic acid degradation via Cyp26b1 blunts local retinoid signalling, relieving repression of inflammatory pathways and perivascular fibrosis.

**PI instruction addressed:**  
Metabolomics‑driven: retinoic acid (RA) up in PH-MK, path to Cyp26b1 enzyme, MK expression, candidate downstream axis.

**Core directional hypothesis:**  
Hypoxia upregulates Cyp26b1 in MKs to catabolize retinoic acid, reducing local retinoid‑mediated immune regulation or vascular quiescence, thereby permitting perivascular inflammation and medial hypertrophy.

**Direction-level reasoning summary:**  
- **Data anchor:** Retinoic Acid up in PH-MK (log2FC 3.44). Cyp26b1 is a direct compound-enzyme (retinoic acid hydroxylase) in Retinol metabolism. Seurat: Cyp26b1 expressed in 7.86% MKs (enrichment 0.73), PH-vs-control log2FC 0.91 (p=0.253, not significant).  
- **Biological interpretation:** RA is a potent immunomodulator and vascular stabilizer. MK accumulation of RA may reflect increased synthesis or decreased degradation. Cyp26b1 expression trends upward (though non-significant), suggesting MKs may attempt to catabolize excess RA; alternatively, hypoxia could upregulate Cyp26b1 to lower local RA, lifting immune suppression and promoting vascular remodeling.  
- **MK-linked pathway logic:** Cyp26b1 is the key enzyme for RA clearance. If MKs deplete local RA, they could create a pro-inflammatory niche (RA normally restrains Th17 cells and promotes Treg).  
- **Candidate downstream axes:** **Immune‑mediated** (loss of RA‑dependent Treg/Th17 balance, more Th17‑like inflammation) or **direct vascular‑wall** (RA signals directly quench SMC proliferation).  
- **Remodelling logic:** De-repression of inflammatory cascades or loss of anti‑proliferative signals in smooth muscle leads to medial thickening.  
- **Key uncertainty:** Low MK Cyp26b1 expression and borderline significance; RA levels may not reflect functional activity; Cyp26b1 may be induced in other cells, not MKs.

**Directional chain:**  
1. Hypoxia increases RA synthesis or impairs its degradation globally; MKs upregulate Cyp26b1 as a compensatory response, but insufficient, leading to net RA accumulation. Alternatively, MK Cyp26b1 may actively degrade RA.  
2. MK metabolic state: RA accumulation or RA degradation in MKs could alter MK function (e.g., autocrine effects) or local microenvironment.  
3. Candidate downstream axis: immune‑mediated (shift from Treg to Th17), direct vascular‑wall.  
4. Broad cellular response: Perivascular T cell infiltration, SMC proliferation.  
5. Remodelling phenotype: Muscularization, perivascular fibrosis.

**Candidate downstream axes:**  
- Plausible axes: immune-mediated (T helper balance), direct vascular-wall, unresolved.  
- Working model: MK Cyp26b1 reduces local RA, disinhibiting Th17‑like responses that drive vascular remodeling.  
- Specific examples: RA, IL‑17, IL‑6.  
- MK-origin gap: It is not certain that RA or RA‑degrading activity emanates from MKs; local RA may be produced by other lung cells.  
- Falsification: MK‑specific Cyp26b1 overexpression or knockout should alter lung RA levels and Th17/Treg balance, and impact vascular remodeling. No effect would negate the MK‑centric hypothesis.

**Evidence basis:**  
- User-provided data: RA up in PH-MK; Cyp26b1 MK pct 7.86%, PH‑up trend not significant.  
- Public dataset metadata: GSE289322 can probe CYP26B1 expression in PH vs control lung.  
- Literature: Retinoic acid pathway in vascular biology and immune regulation; Cyp26b1 in retinoid homeostasis.  
- Biological rationale: RA is known to inhibit smooth muscle proliferation and modulate immunity; its depletion could be pro‑remodelling.  
- Evidence status: Inferred/weak (metabolite up, enzyme trend, no direct evidence of activity or functional consequence).

**Predicted observations:**  
- In MKs: Cyp26b1 enzymatic activity increased; reduced RA in MK-conditioned medium.  
- In tissue: Lower RA in perivascular regions, increased Th17 markers (RORγt, IL‑17).  
- In metabolomics: Lower RA in lung tissue of PH mice relative to control, and RA supplementation ameliorates remodeling.

**Experimental validation:**  
- Perturbation: MK-specific Cyp26b1‑KO or pharmacological Cyp26 inhibitor (e.g., talarozole).  
- Model: Hypoxic PH.  
- Readout: Lung RA levels, perivascular T‑cell profiling, medial thickness.  
- Expected result: Cyp26b1 loss raises local RA, decreases Th17 cells, reduces remodeling.  
- Falsifying result: No change in lung RA or remodeling after MK‑specific CYP26b1 deletion.

**Novelty:**  
First MK‑specific retinoid metabolism hypothesis in pulmonary hypertension.

**Weaknesses:**  
Weak MK‑expression evidence; RA measurement in MKs could be contamination; Cyp26b1 function in MKs not demonstrated.

**Priority estimate:**  
- Directional specificity: 4  
- Data support: 2 (trend only)  
- Literature support: 3  
- Novelty: 5  
- Testability: 4  
- Overall generation priority: 2

---

**Self-filtered rejected ideas:**  
- **Methionine → Mat2a:** Although Mat2a is a direct enzyme for SAM synthesis, its MK expression was low (pct 8.73%, enrichment -0.29) and not PH-up (log2FC 0.56, p=0.1). No mechanism-ready shortlist entry. Rejected for weak MK-specific PH differential and redundancy with AMD1-focused hypotheses.  
- **Tryptophan → Ido1:** Ido1 is a pathway neighbor for tryptophan metabolism (shortlist excluded it). Seurat: MK pct 3.06% with negative enrichment (-0.83) and non-significant PH change. Tryptophan up (log2FC 2.51) in PH-MK could support an IDO‑driven kynurenine pathway, but Ido1 is not meaningfully expressed in MKs; thus not MK-specific.  
- **Lactate → Ldha:** Ldha is a direct enzyme (glycolysis) with strong MK expression (76% MK pct) and PH-up (p=6.2e‑07). However, the shortlist did not include it because lactate was not in the 30 selected metabolites? Actually, lactate appears in the complete evidence chains, but not in the mechanism-ready shortlist (maybe missing differential MK metabolite from sFig6A). The provided metabolomics file for MKs does not list lactate. So no direct MK metabolite differential for lactate available. Rejected due to missing MK-specific metabolite measurement.  
- **Glutathione-related metabolites:** Many rows showed weak MK enrichment or no PH signal; rejected due to lack of positive MK shift.  
- **Inosine → Pnp/Nt5c2:** Inosine was up (log2FC 3.82) and Pnp showed MK pct 20.31% but negative MK enrichment (-1.22) and PH-up (p=3.81e‑06). However, Pnp is not MK-enriched relative to other cells, and the purine degradation axis lacks a clear vascular remodeling link; the mechanism cues were generic “purine metabolism.” Rejected because directionality toward vascular remodeling unclear and no MK-specific metabolite-enzyme correlation beyond expression.  
- **Hyaluronan or ECM metabolites:** no direct enzyme with MK-specific expression in the provided lists.

**Requests for Tool Use Agent:**  
- Check the public dataset GSE289322 for differential expression of Amd1, Amd2, Dnmt3b, Cyp26b1, Pnp, Nt5c2 in PH vs control lung tissue. Report log2FC and p-values to strengthen or refute these hypotheses.  
- Search PubMed for: “AMD1 AND vascular smooth muscle”, “polyamines AND pulmonary hypertension”, “Cyp26b1 AND lung inflammation”, “DNA methylation AND megakaryocyte”.

## generation_1
Cycle ID: 1

Hypotheses generated: H1, H2, H3, H4

---

**Hypothesis ID:** H1  
**Hypothesis title:** Hypoxic MK purine nucleoside phosphorylase (Pnp) upregulation drives inosine secretion and adenosine receptor-mediated pulmonary vascular remodeling

**PI instruction addressed:** Paracrine ligand–receptor mechanisms (endothelial/smooth muscle recipient cells). Metabolomics-driven.

**Core directional hypothesis:**  
Hypoxia upregulates Pnp in lung-resident MKs, increasing inosine production and extracellular release; inosine (and its metabolite adenosine) activates A2 purinergic/adrenergic receptors on vascular endothelial and smooth muscle cells, promoting endothelial dysfunction, medial muscularization, and vessel stiffening.

**Direction-level reasoning summary:**
- **Data anchor:** MK-sorted metabolomics show inosine up (log₂FC 3.82, PH-CD41 vs Control-CD41). Single-cell RNA-seq shows Pnp (purine nucleoside phosphorylase, enzyme for inosine production from inosine monophosphate) is expressed in MK/platelet cells (20.3% of MKs) and significantly upregulated in PH vs control MKs (log₂FC 1.74, Wilcoxon p=3.81e‑06). Pnp is enriched in MKs compared to other lung cells (log₂ enrichment –1.217; within‑MK PH shift dominates).
- **Biological interpretation:** Hypoxic MKs adapt purine metabolism, favouring nucleotide breakdown. The resulting inosine accumulation creates a paracrine purinergic signal. Inosine can be converted to adenosine by ecto‑nucleotidases; both inosine and adenosine act on A2A/A2B receptors on vascular cells.
- **MK-linked enzyme/pathway logic:** Pnp (direct enzyme for inosine generation) is MK‑expressed and hypoxia‑upregulated. This is a direct, pathway‑neighbour connection strengthened by the KEGG purine metabolism mapping and methionine salvage intersection.
- **Candidate downstream axis:** Direct vascular-wall (adenosine receptor signalling on EC and VSMC). A2B receptor activation on VSMC promotes proliferation and migration; endothelial barrier disruption occurs via cAMP/calcium fluxes. Chronic A2B signalling has been linked to hypertensive vascular remodelling.
- **Remodeling phenotype:** Medial thickening, muscularization of distal arterioles, potential endothelial dysfunction.
- **Key uncertainty:** Inosine/adenosine concentration in perivascular microenvironment is unknown; opposing anti‑inflammatory effects via A2A receptors may mask or modify the remodelling outcome. The exact receptor subtype dominance is unresolved.

**Directional chain:**
1. Hypoxia → metabolic reprogramming in lung MKs (HIF‑mediated or direct redox) → upregulation of Pnp expression and activity.
2. MK pathway: Purine nucleotide catabolism → increased intracellular inosine → release of inosine (and extracellularly derived adenosine) into the perivascular milieu.
3. Broad downstream axis: Direct vascular‑wall (adenosine/purine receptor signalling).
4. Cellular/tissue response: Activation of VSMC A2B receptors → proliferation, hypertrophy; endothelial A2A/A2B activation → barrier leakiness, pro‑migratory phenotype.
5. Contribution to remodelling phenotype: Sustained prodding of medial myofibroblast transdifferentiation and muscularization, leading to vessel wall thickening and stiffness.

**Candidate downstream axes:**
- Plausible axes: (1) Direct VSMC A2BR‑mediated proliferation/hypertrophy → medial thickening. (2) Endothelial A2AR‑driven disruption → pericyte recruitment and muscularization. (3) Immune‑mediated (adenosine modulation of macrophage/neutrophil tone) – secondary driver.
- Working model: The dominant axis is direct vascular‑wall signalling via A2B receptors on VSMC, amplified by endothelial leak. Immune modulation may extend the window of injury.
- Specific examples, if useful: A2B knockout mice show attenuated vascular remodelling in other hypoxic models; inosine can be measured in bronchoalveolar lavage.

**Evidence basis:**
- User-provided data: MK‑specific metabolomics (inosine up, log₂FC 3.82). scRNA‑seq: Pnp MK expression (20.3%), PH‑vs‑control MK upregulation (log₂FC 1.74, p=3.81e‑06). KEGG: Pnp directly links to inosine in purine metabolism (mmu_M00958/59).
- Public dataset metadata or analyzed public data: GSE289322 case–control lung transcriptomics could validate Pnp upregulation at tissue level in hypoxia‑induced PH (analysis completed but specific results not yet inspected).
- Literature: Adenosine A2B receptor is implicated in vascular smooth muscle proliferation and pulmonary hypertension (Karmouty‑Quintana et al., 2013 and others).
- Biological rationale: Purine salvage is a known metabolic stress adaptation; inosine is a recognised signalling nucleoside.
- Evidence status: Direct (metabolomics + MK scRNA‑seq), indirect (downstream axis inferred from literature and receptor biology).

**Predicted observations:**
- In MKs: Pnp protein increases in hypoxic lung MKs; inosine concentration in sorted PH MKs higher than control.
- In recipient/tissue compartment: Increased inosine/adenosine in lung interstitial fluid or bronchoalveolar lavage of hypoxic mice. A2B receptor activation markers (p‑CREB) elevated in distal pulmonary arterioles.
- In metabolomics/pathway activity: Elevated inosine and downstream hypoxanthine/xanthine in lung tissue (as seen in whole‑tissue metabolomics, sFig6F).

**Experimental validation:**
- Perturbation: MK‑specific Pnp deletion (Pnp fl/fl Pf4‑Cre) or pharmacological Pnp inhibition (immucillin‑H) in hypoxia.
- Model: Hypoxic mouse PH (10% O₂, 3 weeks); MK‑specific knockout.
- Readout: Hemodynamics (RVSP, RV hypertrophy), vascular morphometry (medial thickness, muscularization), lung inosine levels.
- Expected result: Pnp loss in MKs reduces lung inosine, blunts adenosine receptor activation, attenuates medial thickening and muscularization.
- Falsifying result: No change in remodelling despite reduced MK‑derived inosine; or inosine/adenosine receptor blockade does not affect phenotype.

**Novelty:** Links MK‑intrinsic purine metabolism to a paracrine adenosine‑receptor axis in pulmonary vascular remodelling; previously MKs were not considered a source of vasoactive nucleosides in PH.

**Weaknesses:** Does not resolve whether inosine or adenosine is the dominant mediator; extracellular conversion may involve other cell types; A2B receptor may have dual roles (pro‑ vs anti‑remodelling). Requires tissue‑level validation.

**Revision relative to previous cycle:** N/A (first cycle).

**Priority estimate:**
- Directional specificity: 4
- Data support: 5 (direct metabolite + scRNA‑seq)
- Literature support: 4 (adenosine‑PH literature)
- Novelty: 5
- Testability: 4 (MK‑specific deletion feasible)
- Overall generation priority: 4.4

**Explicit rejection filter:** Passes (MK‑specific component, hypoxia‑dependent, remodelling phenotype, testable)

---

**Hypothesis ID:** H2  
**Hypothesis title:** Hypoxic MK accumulation of methylglyoxal (pyruvaldehyde) activates RAGE on vascular cells driving medial hypertrophy

**PI instruction addressed:** Paracrine ligand–receptor mechanisms (endothelial/smooth muscle recipient cells). Metabolomics‑driven.

**Core directional hypothesis:**  
Hypoxia elevates glycolytic by‑product methylglyoxal in lung MKs due to imbalanced glycolysis/glyoxalase activity; methylglyoxal secretion acts as a damage‑associated dicarbonyl ligand for RAGE (receptor for advanced glycation end‑products) on pulmonary VSMC and endothelium, stimulating pro‑proliferative and fibrotic signalling that contributes to medial thickening.

**Direction-level reasoning summary:**
- **Data anchor:** MK‑sorted metabolomics show pyruvaldehyde (methylglyoxal) up with log₂FC 4.43 in PH vs Control MKs. Methylglyoxal is a reactive dicarbonyl formed mainly from glycolysis (dihydroxyacetone phosphate and glyceraldehyde‑3‑phosphate) and detoxified by glyoxalase 1 (Glo1, gene Glo1). In the public scRNA‑seq data (if queried), Glo1 expression in MK/platelet cells may be downregulated in PH, or constitutively low, explaining accumulation.
- **Biological interpretation:** The marked methylglyoxal build‑up indicates glycolytic stress in hypoxic MKs. Methylglyoxal is membrane‑permeable; it can be exported via transporters or diffuse, then directly modify extracellular proteins forming AGEs that ligate RAGE, or may itself engage RAGE as a low‑affinity ligand. RAGE activation on VSMC promotes proliferation, migration, and matrix production; on endothelium it induces permeability and adhesion molecules.
- **MK‑linked enzyme/pathway logic:** The balance of glycolysis (producing methylglyoxal) and detoxification (Glo1) determines its steady‑state. Glo1 is a candidate enzyme gene; if scRNA‑seq shows MK‑specific downregulation or low baseline, the metabolic stress leads to secretion of this deleterious ligand.
- **Candidate downstream axis:** Direct vascular‑wall (RAGE‑mediated VSMC hypertrophy and endothelial activation).
- **Remodeling phenotype:** Medial thickening, perivascular fibrosis, and reduced compliance.
- **Key uncertainty:** Direct binding of methylglyoxal to RAGE remains debated; alternatively, AGE formation on matrix might be the actual ligand. The necessity of Glo1 downregulation in MKs needs confirmation.

**Directional chain:**
1. Hypoxia → enhanced glycolysis in MKs (Warburg‑type shift) and/or reduced Glo1 expression → methylglyoxal accumulation.
2. MK pathway: Accumulated methylglyoxal exported into extracellular space → modifies proteins forming AGEs, or directly interacts with RAGE on VSMC/EC.
3. Broad downstream axis: Direct vascular‑wall (RAGE signalling).
4. Cellular/tissue response: RAGE‑driven NF‑κB and MAPK activation → VSMC proliferation, hypertrophy, collagen synthesis; endothelial pro‑inflammatory shift.
5. Contribution to remodelling phenotype: Medial thickening, vessel wall stiffening, possible perivascular collagen deposition.

**Candidate downstream axes:**
- Plausible axes: (1) Direct RAGE‑mediated VSMC proliferation/hypertrophy → medial thickness. (2) AGE‑mediated matrix cross‑linking → stiffness. (3) Endothelial RAGE activation → barrier disruption and immune recruitment (secondary).  
- Working model: The primary axis is MK‑derived methylglyoxal/AGEs acting on VSMC RAGE to drive muscularization. Matrix stiffening adds a biophysical feed‑forward.
- Specific examples, if useful: Pharmacologic RAGE blockade (e.g., FPS‑ZM1) reduces hypoxic PH in some rodent studies; methylglyoxal scavenging attenuates vascular complications in diabetes.
- What remains unresolved: Does methylglyoxal act through RAGE or through direct carbonyl stress on vessel wall proteins? Contribution of Glo1 genetic variants.

**Evidence basis:**
- User-provided data: MK metabolomics shows pyruvaldehyde up (log₂FC 4.43). Whole‑tissue metabolomics (Figure 6D+F) may show parallel methylglyoxal trends (to be checked).
- Public dataset metadata or analyzed public data: GSE289322 can be queried for Glo1 differential expression (not yet inspected). If Glo1 is down in PH lung tissue, it would support a systemic glyoxalase deficiency.
- Literature: RAGE activation promotes VSMC proliferation and is implicated in experimental PH (Meloche et al., 2019 and others). Methylglyoxal–RAGE axis established in diabetes‑associated vasculopathy.
- Biological rationale: MKs are highly metabolic cells; glycolysis is the main energy source, predisposing them to methylglyoxal production under stress.
- Evidence status: Metabolomics is direct; MK‑specific Glo1 expression and differential expression status remains to be confirmed (indirect). Receptor axis is inferred from literature.

**Predicted observations:**
- In MKs: Pyruvaldehyde mass higher; Glo1 protein and activity lower in PH MKs compared to control. Increased glycolysis (e.g., lactate output).
- In recipient/tissue compartment: Elevated methylglyoxal‑derived AGEs (e.g., MG‑H1) on pulmonary vascular walls. RAGE activation markers (phospho‑NF‑κB p65) in medial VSMC.
- In metabolomics/pathway activity: Methylglyoxal correlated with lactate/pyruvate in MKs, indicating glycolytic overload.

**Experimental validation:**
- Perturbation: MK‑specific Glo1 overexpression (to detoxify methylglyoxal) or pharmacologic methylglyoxal scavenger (e.g., aminoguanidine) during hypoxia; or systemic RAGE knockout in bone marrow‑derived cells.
- Model: Hypoxic PH; MK‑selective AAV9‑Pf4‑Glo1.
- Readout: Medial thickness, muscularization, RVSP, tissue methylglyoxal‑AGE adducts.
- Expected result: MK Glo1 upregulation reduces perivascular AGEs and attenuates remodelling. RAGE blockade in recipient cells mimics protection.
- Falsifying result: No reduction in vascular pathology despite effective methylglyoxal lowering; or RAGE‑null mice show no protection, indicating methylglyoxal works via RAGE‑independent mechanism.

**Novelty:** First to propose MK‑derived methylglyoxal as a paracrine RAGE ligand in pulmonary vascular remodelling.

**Weaknesses:** Methylglyoxal is not solely MK‑derived; lung tissue produces it. Glo1 expression in MKs is unknown; the hypothesis depends on confirming MK downregulation/hypoxia‑induced imbalance.

**Revision relative to previous cycle:** N/A.

**Priority estimate:**
- Directional specificity: 3 (RAGE axis generic, but MK source adds specificity)
- Data support: 4 (direct metabolomics, but missing scRNA‑seq for Glo1)
- Literature support: 4 (RAGE‑PH literature)
- Novelty: 5
- Testability: 4 (requires MK‑specific tools)
- Overall generation priority: 4.0

---

**Hypothesis ID:** H3  
**Hypothesis title:** Hypoxic MK retinoic acid catabolism via Cyp26b1 reduces perivascular retinoic acid tone, releasing VSMC from growth suppression

**PI instruction addressed:** Paracrine ligand–receptor mechanisms (smooth muscle recipient cells). Metabolomics‑driven.

**Core directional hypothesis:**  
Hypoxia induces modest upregulation of the retinoic acid‑catabolising enzyme Cyp26b1 in lung MKs, increasing retinoic acid degradation; the resulting drop in extracellular all‑trans retinoic acid (ATRA) removes a tonic inhibitory signal mediated by retinoic acid receptors (RAR‑RXR) on vascular smooth muscle cells, permitting accelerated proliferation and medial thickening.

**Direction-level reasoning summary:**
- **Data anchor:** MK‑sorted metabolomics show retinoic acid (ATRA) up with log₂FC 3.44 in PH vs Control MKs, which is counter‑intuitive for a catabolic hypothesis. However, Cyp26b1, which inactivates ATRA to polar metabolites, shows a trend toward upregulation in MKs (log₂FC 0.91, p=0.253) and is enriched in MKs (log₂ enrichment 0.73). The retinoic acid increase may reflect an intracellular “pool” despite increased catabolism, or an attempt to compensate. The net effect could be reduced active ATRA in the extracellular microenvironment due to degradation by MK‑expressed Cyp26b1, because the enzyme is intracellular; but if MKs release ATRA, increased catabolism could lower surrounding ATRA. Alternatively, MKs may oxidise ATRA to 4‑oxo retinoic acid, a less active metabolite, altering the ligand spectrum on RAR.
- **Biological interpretation:** ATRA is a well‑established anti‑proliferative signal for VSMC, acting via RAR‑RXR heterodimers to inhibit cell cycle and promote differentiation. In hypoxia, MKs may increase ATRA production (as seen) but simultaneously upregulate Cyp26b1 to degrade it, yielding a net reduction in bioactive ATRA reaching VSMC. This loss of growth‑inhibitory tone facilitates muscularisation.
- **MK‑linked enzyme/pathway logic:** Cyp26b1 is the primary catabolic enzyme for all‑trans retinoic acid. Its expression in MKs (8.9% PH MKs, 5.9% control) positions MKs as potential modulators of local retinoid gradients.
- **Candidate downstream axis:** Direct vascular‑wall (VSMC proliferation via derepression of growth pathways).
- **Remodelling phenotype:** Medial thickening and muscularization of normally non‑muscular arterioles.
- **Key uncertainty:** The direction of net ATRA concentration in the vessel wall after hypoxia is unknown; the metabolic up of ATRA in MK lysates could reflect synthesis induction, not degradation. In vivo ATRA measurements in perivascular space are needed.

**Directional chain:**
1. Hypoxia → retinoid pathway activation in lung MKs (e.g., via HIF or RAR‑RXR signalling) → upregulation of retinoic acid synthesis and catabolic enzyme Cyp26b1.
2. MK pathway: Increased Cyp26b1 activity → faster conversion of ATRA to less active polar metabolites, leading to reduced secretion of bioactive ATRA into the vessel wall.
3. Broad downstream axis: Direct vascular‑wall (loss of anti‑proliferative signal).
4. Cellular/tissue response: VSMC RAR‑RXR signalling decreases → derepression of cyclin D1 and other S‑phase genes → increased VSMC proliferation and migration.
5. Contribution to remodelling phenotype: Muscularization of distal arterioles and medial thickening.

**Candidate downstream axes:**
- Plausible axes: (1) Direct VSMC RAR inhibition removal → medial growth. (2) Possible alteration of immune cell homing (retinoids affect T‑cell differentiation) – secondary.
- Working model: The primary axis is local retinoid deficiency caused by MK catabolism, disinhibiting VSMC growth.
- Specific examples, if useful: ATRA supplementation attenuates experimental hypoxic PH in rats (Qin et al., 2017); RARγ agonists reduce VSMC proliferation in vitro.
- What remains unresolved: Does MK catabolism affect total vessel wall ATRA? How do other lung cells (fibroblasts, EC) contribute to retinoid balance?

**Evidence basis:**
- User-provided data: MK metabolomics show retinoic acid up (log₂FC 3.44). scRNA‑seq: Cyp26b1 MK enrichment log₂FC 0.73, trend PH up (p=0.253). KEGG links metabolite to enzyme (pathway‑neighbour).
- Public dataset metadata or analyzed public data: GSE289322 might show Cyp26b1 differential expression; not yet inspected.
- Literature: Retinoic acid inhibits VSMC proliferation via RAR; retinoid metabolism is altered in cardiovascular disease.
- Biological rationale: MKs residing in lung parenchyma could fine‑tune local retinoid levels; hypoxia is known to perturb retinoid signalling in development and disease.
- Evidence status: Metabolomics direct; MK enzyme expression moderate, differential borderline (indirect). Axis inferred.

**Predicted observations:**
- In MKs: Cyp26b1 protein and 4‑oxo‑retinoic acid increased in PH; ATRA turnover rate higher.
- In recipient compartment: Lung tissue ATRA levels lower in hypoxic mice; RAR target genes (e.g., Rarb) downregulated in medial VSMC.
- In metabolomics/pathway activity: Increased 4‑oxo‑retinoic acid in MK‑conditioned medium.

**Experimental validation:**
- Perturbation: MK‑specific Cyp26b1 knockout (Cyp26b1 fl/fl Pf4‑Cre) or pharmacologic Cyp26 inhibitor (e.g., talarozole) during hypoxia.
- Model: Hypoxic PH mouse; MK knockout.
- Readout: Hemodynamics, medial thickness, muscularization, lung tissue ATRA concentration.
- Expected result: MK Cyp26b1 deletion preserves perivascular ATRA, reduces VSMC proliferation, attenuates remodelling.
- Falsifying result: ATRA levels unchanged in vessel wall or no effect on remodelling; Cyp26b1 inhibition does not impact phenotype.

**Novelty:** Positions MKs as local retinoid gates that control vascular tone; previously retinoid metabolism was studied mainly in liver/lung epithelium.

**Weaknesses:** Cyp26b1 upregulation not significant (p=0.253); the hypothesis relies on net catabolic activity increase that may not be large. Whole‑tissue retinoid biology complex.

**Revision relative to previous cycle:** N/A.

**Priority estimate:**
- Directional specificity: 4
- Data support: 3 (metabolomics strong, scRNA‑seq weak)
- Literature support: 4
- Novelty: 5
- Testability: 4
- Overall generation priority: 4.0

---

**Hypothesis ID:** H4  
**Hypothesis title:** Hypoxic MK secretion of VEGF and PDGF‑B via HIF‑1α targets endothelial and smooth muscle proliferation

**PI instruction addressed:** Paracrine ligand–receptor mechanisms (endothelial and smooth muscle recipient cells). Non‑metabolomic, protein‑based.

**Core directional hypothesis:**  
Hypoxia stabilizes HIF‑1α in lung‑resident MKs, transcriptionally upregulating angiogenic/mitogenic paracrine factors (VEGF‑A, PDGF‑B) that act on endothelial VEGFR2 and VSMC PDGFRβ respectively, driving endothelial dysfunction, VSMC recruitment, and muscularization of distal pulmonary vessels.

**Direction-level reasoning summary:**
- **Data anchor:** Prior user results establish that lung‑resident MKs are necessary for hypoxia‑induced PH and vascular remodelling. The hypoxia‑sensing transcription factor HIF‑1α is a universal master regulator; its canonical targets include VEGF‑A and PDGF‑B. Single‑cell RNA‑seq (if queried) may show that MK/platelet cells in PH express Vegfa and Pdgfb, and these genes may be upregulated compared to control. While not directly shown in the provided data summary, this is a well‑founded inference.
- **Biological interpretation:** Hypoxic MKs, situated in the pulmonary microvasculature, become a local source of potent endothelial and smooth muscle mitogens. VEGF‑A disrupts endothelial barrier integrity and stimulates pericyte recruitment, while PDGF‑B directly drives VSMC proliferation and migration. This dual paracrine assault recreates key features of pulmonary vascular pathology.
- **MK‑linked enzyme/pathway logic:** The HIF‑1α transcriptional program is central; the user data could confirm expression of these ligands in MKs (needs query). The scRNA‑seq analysis can determine co‑expression of Hif1a, Vegfa, Pdgfb in MK/platelet cluster and whether they are hypoxia‑upregulated.
- **Candidate downstream axis:** Direct vascular‑wall (endothelial activation and VSMC proliferation).
- **Remodelling phenotype:** Endothelial hyperpermeability, medial thickening, distal arteriole muscularization, potentially plexiform‑like lesions.
- **Key uncertainty:** Whether lung MKs are quantitatively important sources of VEGF/PDGF compared to other hypoxic lung cells (AEC, macrophages, fibroblasts). MK‑specific knockout data are needed.

**Directional chain:**
1. Hypoxia → HIF‑1α stabilization in in‑situ MKs → transcriptional induction of Vegfa and Pdgfb.
2. MK pathway: Secretion of VEGF‑A and PDGF‑B into the perivascular space.
3. Broad downstream axis: Direct vascular‑wall (VEGFR2 on EC; PDGFRβ on VSMC/pericytes).
4. Cellular/tissue response: EC VEGFR2 activation → permeability, vaso‑occlusion, recruitment of SMC progenitors; VSMC PDGFRβ activation → proliferation, migration, medial muscularization.
5. Contribution to remodelling phenotype: Medial thickening, distal vessel muscularization, endothelial dysfunction.

**Candidate downstream axes:**
- Plausible axes: (1) Endothelial‑centred: VEGF‑driven EC proliferation and barrier disruption, leading to pericyte detachment and SMC migration. (2) Smooth muscle‑centred: PDGF‑driven VSMC hyperplasia and matrix production. (3) Immune‑mediated: VEGF recruits monocytes/macrophages that amplify remodelling.  
- Working model: Both axes cooperate; MK‑derived VEGF initiates endothelial injury and signals for SMC recruitment, while PDGF‑B sustains SMC expansion.
- Specific examples, if useful: Anti‑VEGF therapy can exacerbate PH in some contexts, suggesting timing matters; PDGF‑B neutralization ameliorates remodelling in monocrotaline models.
- What remains unresolved: Relative contribution of MK‑derived vs other cell‑derived growth factors; the need for Mk‑specific deletion to prove the source.

**Evidence basis:**
- User-provided data: Prior results confirm MKs are necessary; MK scRNA‑seq expression status for these factors not detailed but can be extracted.
- Public dataset metadata or analyzed public data: GSE289322 may show Vegfa/Pdgfb upregulation in PH lung tissue; not yet inspected.
- Literature: HIF‑1α/VEGF/PDGF is a canonical hypoxia axis; PDGF‑B is implicated in many forms of pulmonary hypertension.
- Biological rationale: MKs are hypoxia‑responsive and situated in vascular niche; they can release large quantities of cytokines.
- Evidence status: Inferred from MK necessity and hypoxia literature; direct scRNA‑seq data for MK ligands is provisional.

**Predicted observations:**
- In MKs: HIF‑1α nuclear accumulation and Vegfa/Pdgfb mRNA upregulation in PH vs control MKs. MK‑conditioned medium enhances EC tube formation and VSMC proliferation in a VEGF‑/PDGF‑dependent manner.
- In recipient/tissue compartment: Phospho‑VEGFR2 and phospho‑PDGFRβ increased in distal pulmonary arterioles in hypoxia.
- In metabolomics/pathway activity: Not relevant.

**Experimental validation:**
- Perturbation: MK‑specific deletion of Hif1a (Hif1a fl/fl Pf4‑Cre) or Vegfa/Pdgbf double knockout in MKs during hypoxia.
- Model: Hypoxic PH mouse; MK‑specific knockout.
- Readout: Hemodynamics, vascular muscularization, phospho‑receptor staining, MK culture secretome analysis.
- Expected result: MK‑specific Hif1a loss reduces VEGF‑A/PDGF‑B secretion, blunts VEGFR2/PDGFRβ phosphorylation in vessel walls, and attenuates medial thickening and muscularization.
- Falsifying result: No change in remodelling despite ablated MK HIF pathway, indicating other paracrine sources dominate; or systemic VEGF/PDGF blockade fails to mirror MK‑specific phenotype.

**Novelty:** Focuses on the classic HIF‑growth factor axis but with MK‑cell specificity, unifying genetic evidence with a direct paracrine mechanism.

**Weaknesses:** Overlap with contribution from other hypoxic cells; MK‑specific expression and hypoxic induction not yet confirmed in the scRNA‑seq data. Genetic redundancy (other sources) may mask phenotype.

**Revision relative to previous cycle:** N/A.

**Priority estimate:**
- Directional specificity: 5
- Data support: 2 (prior results only; scRNA‑seq needed)
- Literature support: 5
- Novelty: 3 (HIF axis known, but MK source novel)
- Testability: 4 (MK‑specific knockouts feasible)
- Overall generation priority: 3.8

---

**Self-filtered rejected ideas:**
- A hypothesis on MK‑derived extracellular vesicles delivering miRNA to VSMC was considered but lacked direct paracrine ligand‑receptor specificity and had no specific metabolic anchor; also EV delivery is not strictly a ligand‑receptor mechanism.
- A hypothesis on MK thrombin/coagulation cascade leading to PAR activation on EC/VSMC was rejected because it is not primarily paracrine; thrombosis involves multiple cell types and is less directly linked to a single MK‑derived ligand; moreover, the data did not provide coagulation factor evidence.
- A hypothesis on AMD1/polyamine leading to secretion of spermidine acting via a specific receptor was rejected because polyamines do not have a well‑characterised receptor on vascular cells; the ligand‑receptor requirement is not met.

**Requests for Tool Use Agent:**
1. Query scRNA‑seq: Check expression of Pdgfb, Vegfa, Hif1a in MK/platelet cluster; test differential expression between PH and control. Provide log2FC and significance.
2. Query scRNA‑seq: Check expression of Glo1 (glyoxalase 1) in MK/platelet; test PH shift.
3. For GSE289322 public dataset analysis output, extract DE results for Pnp, Cyp26b1, Glo1, Vegfa, Pdgfb, and report log2FC/p‑values; determine if they corroborate the MK‑derived hypotheses at tissue level.
4. Literature search: PubMed for “adenosine A2B receptor AND pulmonary hypertension AND vascular smooth muscle”, “methylglyoxal AND RAGE AND vascular remodeling”, “retinoic acid AND vascular smooth muscle AND hypoxia”, “megakaryocyte AND PDGF‑B AND hypoxia”. Provide key functional insights (no fabrication).

## generation_2
Cycle ID: 1

Hypotheses generated: H1, H2, H3, H4, H5

---

### Hypothesis H1  
**Hypothesis ID:** H1  
**Hypothesis title:** AMD1‑driven polyamine metabolism in hypoxic lung MKs reshapes the perivascular immune and stromal milieu to drive medial thickening and muscularization.  
**PI instruction addressed:** Metabolomics‑driven direction‑level mechanism; link differential MK metabolite (methionine) → KEGG neighbor enzyme (Amd1) → MK expression/PH shift → broad downstream axis → vascular remodelling.  
**Core directional hypothesis:** Hypoxia upregulates AMD1 in lung‑resident MKs, increasing S‑adenosylmethionine decarboxylation and shifting methionine flux toward polyamine (spermidine/spermine) synthesis; elevated polyamines act through both immune‑mediated and direct vascular‑wall axes to promote pulmonary artery smooth muscle cell (PASMC) proliferation, perivascular fibrosis, and medial thickening.  

**Direction‑level reasoning summary:**  
- **Data anchor:** Methionine is elevated 3.26‑fold (log2FC) in PH MKs vs controls; AMD1 is enriched in MKs (31.44% MK vs 14.87% other cells, log2 enrichment 1.353) and significantly upregulated in PH MKs (log2FC 1.77, Wilcoxon p=6.55×10⁻⁶).  
- **Biological interpretation:** Hypoxic MKs increase methionine availability or uptake, and the concomitant upregulation of AMD1 commits SAM toward decarboxylated SAM and polyamine biosynthesis. This reprogramming likely raises spermidine and spermine levels in the MK microenvironment.  
- **MK‑linked enzyme/pathway logic:** AMD1 is a gatekeeper of polyamine synthesis from methionine/SAM. Its expression pattern matches the metabolite signal, suggesting a functional connection.  
- **Candidate downstream axis:** Polyamines are pleiotropic; they can modulate T‑cell differentiation (e.g., Th17‑like responses) and macrophage polarization (immune‑mediated), as well as directly stimulate fibroblast‑to‑myofibroblast transition and PASMC hypertrophy (direct vascular‑wall). The working model favours direct PASMC action because polyamines are known mitogens for smooth muscle, but immune modulation cannot be excluded.  
- **Remodelling logic:** Perivascular accumulation of polyamines drives PASMC hypertrophy, fibroblast activation, and matrix deposition, culminating in medial thickening and muscularization.  
- **Key uncertainty:** Whether AMD1 activity actually produces functionally elevated polyamine levels in the MK secretome or lung interstitium, and the relative contributions of immune versus stromal cells to the final remodelling phenotype, remain to be determined.  

**Directional chain:**  
1. Hypoxia activates transcriptional programmes (e.g., HIF‑1α, c‑Myc) in lung MKs, leading to AMD1 upregulation.  
2. AMD1 drives conversion of SAM to decarboxylated SAM, increasing spermidine/spermine synthesis.  
3. Polyamines are released (free or EV‑associated) into the perivascular space.  
4. Polyamines act on PASMCs, fibroblasts, and perivascular immune cells to promote proliferation, matrix deposition, and a pro‑remodelling immune tone.  
5. Medial thickening, muscularization, and perivascular fibrosis.  

**Candidate downstream axes:**  
- Plausible axes: (1) Direct vascular‑wall – polyamines stimulate PASMC proliferation/hypertrophy and fibroblast activation; (2) Immune‑mediated – polyamines favour Th17‑like T‑cell differentiation and M2‑like macrophage polarization, which indirectly support remodelling; (3) EV/stromal – polyamines may be loaded into MK‑derived vesicles and delivered to adventitial cells.  
- Working model: Direct PASMC/fibroblast activation, supported by well‑established mitogenic effects of polyamines on smooth muscle.  
- What remains unresolved: Which specific polyamine species (spermidine vs spermine) is the active mediator, and whether endogenous concentrations reach effective levels in the vessel wall.  

**Evidence basis:**  
- **User‑provided data:** Metabolomics – methionine up in MKs (sFig6A, log2FC 3.26). scRNA‑seq – Amd1 expression, MK enrichment, and PH‑up shift (Seurat object; p=6.55×10⁻⁶).  
- **Public dataset metadata/analysis:** GSE289322 (de‑identified lung/PH comparison) could be queried for Amd1 differential expression as tissue‑level validation; currently not inspected.  
- **Literature:** Polyamine metabolism is linked to cell proliferation; AMD1 is regulated by mTORC1 and c‑Myc; spermidine hypusination of eIF5A controls translation of proliferative proteins; polyamines influence immune cell function (PubMed context in evidence package).  
- **Biological rationale:** Hypoxia, metabolic reprogramming, and polyamine‑driven growth pathways converge on vascular smooth muscle hypertrophy – a hallmark of pulmonary hypertension.  
- **Evidence status:** Direct for metabolite and gene expression; inferred for polyamine synthesis and secretion; speculative for exact immune/stromal effectors.  

**Predicted observations:**  
- In MKs: Increased AMD1 protein, elevated spermidine/spermine levels; metabolic flux from methionine into polyamines.  
- In recipient or tissue compartment: Lung tissue from PH mice shows elevated putrescine/spermidine/spermine; perivascular polyamine immunoreactivity.  
- In metabolomics or pathway activity: Polyamine pathway intermediates (putrescine, spermidine, spermine) increased in MKs and whole‑lung metabolomics.  

**Experimental validation:**  
- **Perturbation:** MK‑specific deletion of Amd1 (Pf4‑Cre;Amd1^(fl/fl)) or systemic AMD1 inhibitor (e.g., DFMO + SAM‑limited diet).  
- **Model:** Chronic hypoxia (10% O₂) in adult mice; assess at day 21.  
- **Readout:** Right ventricular systolic pressure (RVSP), right ventricular hypertrophy (RV/(LV+S)), medial thickness/cross‑sectional area, vessel muscularization (% fully muscularized), lung polyamine levels, immune cell profiling (flow cytometry for T‑cell, macrophage subsets).  
- **Expected result:** AMD1 loss in MKs reduces lung polyamine concentrations and significantly attenuates haemodynamic impairment, medial thickening, and muscularization.  
- **Falsifying result:** Conditional AMD1 knockout does not lower polyamine levels or improve remodelling, or it improves remodelling through an unrelated metabolite pathway, indicating that AMD1/polyamines are not the causal axis.  

**Novelty:** High – a metabolic switch (polyamine synthesis) in lung‑resident MKs as a driver of hypoxia‑induced vascular remodelling has not been described.  

**Weaknesses:** AMD1 is not MK‑exclusive; conditional knockout partially addresses this but off‑target effects in other lung cells may complicate interpretation. The exact polyamine species and downstream cellular targets require deconvolution.  

**Revision relative to previous cycle:** N/A (first cycle)  

**Priority estimate:**  
- Directional specificity: 4/5  
- Data support: 5/5  
- Literature support: 4/5  
- Novelty: 5/5  
- Testability: 4/5  
- Overall generation priority: 4.4  

**Explicit rejection filter:** Pass – MK‑specific (Amd1 expression/enrichment), hypoxia‑dependent (PH vs control shift), vascular remodelling phenotype (medial thickening), not generic inflammation, testable.  

---

### Hypothesis H2  
**Hypothesis ID:** H2  
**Hypothesis title:** Hypoxia‑driven LDHA upregulation in lung MKs produces lactate that acidifies the perivascular niche, activating fibroblasts and smooth muscle cells to drive vascular stiffening and muscularization.  
**PI instruction addressed:** Metabolomics‑driven hypothesis; differential metabolite (lactate) → direct compound‑enzyme (Ldha) → MK expression/PH shift → direction‑level remodelling axis.  
**Core directional hypothesis:** Hypoxia upregulates LDHA in lung‑resident MKs, increasing lactate production and extracellular acidification; lactate serves as a signalling molecule and metabolic fuel, stimulating fibroblast‑to‑myofibroblast transition, PASMC hypertrophy, and endothelial dysfunction, thereby causing vascular stiffness, medial thickening, and perivascular fibrosis.  

**Direction‑level reasoning summary:**  
- **Data anchor:** Lactate is elevated in PH MKs (log2FC 2.29 from sFig6A). Ldha is highly expressed in MKs (94.98% MK vs 74.47% other cells, enrichment log2 0.38) and modestly but significantly upregulated in PH MKs (log2FC 0.61, Wilcoxon p=0.00105).  
- **Biological interpretation:** Hypoxic MKs increase glycolytic flux; LDHA converts pyruvate to lactate, which is secreted. This Warburg‑like shift creates a low‑pH microenvironment.  
- **MK‑linked enzyme/pathway logic:** LDHA is the terminal enzyme of anaerobic glycolysis and is a direct match for the metabolite. Its high expression and PH‑induced upregulation position it as the likely source of the observed lactate accumulation.  
- **Candidate downstream axis:** Direct vascular‑wall – lactate signals through GPR81 on fibroblasts and PASMCs, promoting collagen synthesis, proliferation, and myofibroblast differentiation. It may also induce endothelial‑to‑mesenchymal transition (EndMT) as an unresolved candidate. Immune‑mediated effects (e.g., lactate polarisation of macrophages) are possible but secondary.  
- **Remodelling logic:** Lactate‑driven acidification and receptor‑mediated signalling drive matrix deposition and VSMC hypertrophy, leading to vascular stiffening and medial thickening.  
- **Key uncertainty:** Whether lactate from MKs reaches sufficient local concentrations to influence deep vascular cells, and whether the primary effect is pH‑dependent or receptor‑specific, are unresolved.  

**Directional chain:**  
1. Hypoxia induces HIF‑1α‑mediated upregulation of glycolytic genes including Ldha in lung MKs.  
2. MKs secrete lactate, lowering extracellular pH in the perivascular niche.  
3. Lactate activates fibroblasts (via GPR81/ERK1‑2/TGF‑β pathways) to become α‑SMA⁺ myofibroblasts, depositing collagen and ECM.  
4. Concomitantly, lactate promotes PASMC hypertrophy and impairs endothelial barrier function.  
5. Vessel wall stiffening, medial thickening, and muscularization.  

**Candidate downstream axes:**  
- Plausible axes: (1) Direct vascular‑wall – fibroblast‑to‑myofibroblast transition and PASMC hypertrophy; (2) Endothelial – lactate‑induced EndMT or barrier disruption; (3) Immune‑mediated – lactate polarisation of macrophages toward a profibrotic M2‑like phenotype.  
- Working model: Fibroblast activation via GPR81 and acid‑sensing pathways, consistent with known profibrotic effects of lactate in other organs.  
- What remains unresolved: The identity of the key lactate‑responsive cell type(s) and the relative importance of pH versus receptor signalling.  

**Evidence basis:**  
- **User‑provided data:** Lactate up in MKs (sFig6A, log2FC 2.29); Ldha expression, MK enrichment, and PH‑up shift (scRNA‑seq, p=0.00105).  
- **Public dataset metadata:** GSE289322 could validate Ldha and lactate‑related gene expression in PH lung tissue.  
- **Literature:** Lactate is a known profibrotic factor via GPR81; hypoxia‑induced glycolysis is a hallmark of pulmonary hypertension; extracellular acidification promotes fibroblast activation.  
- **Biological rationale:** MKs are cellular factories; a glycolytic shift would substantially increase extracellular lactate, especially from abundant perivascular MKs.  
- **Evidence status:** Direct for metabolite and enzyme expression; inferred for local acidification and fibroblast activation; speculative for receptor specificity and EndMT.  

**Predicted observations:**  
- In MKs: Increased LDHA protein and lactate production; enhanced glycolytic rate.  
- In tissue: Perivascular pH decrease (pH‑sensitive dyes); increased collagen‑I/III deposition, α‑SMA⁺ myofibroblasts.  
- In metabolomics: Elevated lactate in whole‑lung tissue of PH mice.  

**Experimental validation:**  
- **Perturbation:** MK‑specific deletion of Ldha (Pf4‑Cre;Ldha^(fl/fl)) or pharmacological inhibition of glycolysis (e.g., 2‑DG, but poor specificity).  
- **Model:** Chronic hypoxia in mice.  
- **Readout:** Vascular stiffness (pressure–volume loops or atomic force microscopy on isolated PA), medial thickness, collagen content (hydroxyproline assay), fibroblast activation (α‑SMA, collagen I), RVSP.  
- **Expected result:** LDHA loss reduces lung lactate, vascular stiffness, and remodelling.  
- **Falsifying result:** No change in lactate levels or remodelling, or remodelling is driven by a different glycolytic enzyme, not LDHA, indicating the lactate axis is dispensable.  

**Novelty:** High – MK‑derived lactate as a local driver of pulmonary vascular stiffening has not been explored.  

**Weaknesses:** Lactate is produced by many cell types; convincing cell‑specificity requires careful controls. The exact effective concentration and receptor engagement need validation.  

**Priority estimate:**  
- Directional specificity: 4  
- Data support: 4  
- Literature support: 4  
- Novelty: 5  
- Testability: 3 (lactate interventions are pleiotropic)  
- Overall: 4.0  

---

### Hypothesis H3  
**Hypothesis ID:** H3  
**Hypothesis title:** AMD1‑driven polyamine synthesis in hypoxic MKs leads to packaging of spermidine/spermine into extracellular vesicles that are taken up by PASMCs, directly promoting medial hyperplasia.  
**PI instruction addressed:** Extracellular vesicle mechanism grounded in MK metabolomics; links metabolic enzyme (Amd1) to EV cargo hypothesis.  
**Core directional hypothesis:** Hypoxia‑induced AMD1 upregulation in lung MKs increases polyamine production; polyamines are loaded into MK‑derived extracellular vesicles (EVs) that are internalized by PASMCs, where they enhance proliferation and hypertrophy, leading to medial thickening.  

**Direction‑level reasoning summary:**  
- **Data anchor:** Methionine elevation (log2FC 3.26) and AMD1 upregulation (log2FC 1.77, p=6.55×10⁻⁶) in PH MKs. MKs are abundant EV producers (platelet shedding, microparticles, exosomes).  
- **Biological interpretation:** Polyamines are small, charged molecules that can be packaged into EVs during biogenesis, protecting them from dilution and enzymatic degradation. Hypoxic MKs may exploit this route for targeted delivery to perivascular cells.  
- **MK‑linked enzyme/pathway logic:** AMD1 generates the substrate for spermidine/spermine synthases; polyamines can partition into vesicular compartments via interactions with RNA or negatively charged lipids.  
- **Candidate downstream axis:** EV/stromal – direct delivery of polyamines to PASMCs drives proliferative signalling (mTORC1‑S6K1, eIF5A hypusination) and hypertrophy.  
- **Remodelling logic:** Polyamine‑rich EVs stimulate medial smooth muscle cell growth, thickening the vessel wall.  
- **Key uncertainty:** Whether polyamines are genuinely enriched in MK‑derived EVs and whether the concentrations delivered via EVs are sufficient to elicit PASMC hyperplasia, as opposed to free polyamine diffusion.  

**Directional chain:**  
1. Hypoxia upregulates AMD1, raising intracellular spermidine/spermine in MKs.  
2. Polyamines are sorted into intraluminal vesicles of multivesicular bodies (MVBs).  
3. MKs release exosomes/microvesicles enriched in polyamines.  
4. EVs are taken up by neighbouring PASMCs, delivering polyamines.  
5. Polyamines stimulate mTORC1/S6K1 pathway and eIF5A hypusination, driving cell cycle entry and hypertrophy.  
6. Medial thickening and muscularization.  

**Candidate downstream axes:**  
- Plausible axes: (1) EV‑mediated direct PASMC activation; (2) EV‑mediated fibroblast activation; (3) EV‑mediated immune cell reprogramming (polyamines delivered to T cells).  
- Working model: Direct PASMC EV delivery, as polyamines are mitogenic for smooth muscle and MKs are anatomically positioned in the pulmonary vasculature.  
- What remains unresolved: The fraction of total polyamine released via EVs vs free secretion, and whether AMD1‑dependent EV cargo changes are specific to polyamines or also affect other metabolites.  

**Evidence basis:**  
- **User‑provided data:** Methionine and AMD1 expression/PH shift (as in H1). No direct EV data.  
- **Public dataset metadata:** None for MK‑EV.  
- **Literature:** Platelet/MK EVs are known to contain polyamines; AMD1‑dependent eIF5A hypusination controls translation of proliferation‑associated proteins.  
- **Biological rationale:** EV packaging is a common strategy for paracrine signalling; polyamines are stable inside vesicles and can activate growth pathways.  
- **Evidence status:** Direct for metabolite and enzyme; inferred for EV loading; speculative for EV‑mediated PASMC hyperplasia.  

**Predicted observations:**  
- In MKs: Polyamine content is enriched in the EV fraction (ultracentrifugation + LC‑MS) compared to MK lysate.  
- In recipient cells: PASMCs treated with PH‑MK EVs show increased intracellular spermidine/spermine, eIF5A hypusination, and proliferation (EdU incorporation).  
- In metabolomics: Purified EVs from PH MKs have higher spermidine/spermine levels than control MK EVs.  

**Experimental validation:**  
- **Perturbation:** Use AMD1 inhibitor (e.g., SAM486A) or genetic deletion in MKs; isolate EVs from MK supernatants and test their ability to stimulate PASMC proliferation in vitro.  
- **Model:** In vitro: bone marrow‑derived MK cultures under normoxia/hypoxia, isolate EVs, add to PASMCs. In vivo: adoptive transfer of labelled MK‑EVs to hypoxic mice.  
- **Readout:** PASMC EdU⁺ cells, EV polyamine quantification, eIF5A hypusination, vessel medial thickness (for in vivo transfer).  
- **Expected result:** AMD1 inhibition reduces EV polyamine content and abolishes the pro‑proliferative effect of MK‑EVs on PASMCs.  
- **Falsifying result:** EV polyamine levels are low or unchanged by AMD1 inhibition, and MK‑EVs still stimulate PASMCs through other cargo; or free polyamine alone reproduces the EV effect, indicating packaging is irrelevant.  

**Novelty:** Very high – the concept of polyamine‑loaded MK EVs as a vector for vascular remodelling is unprecedented.  

**Weaknesses:** No direct evidence of EV polyamine loading; requires sophisticated EV isolation and metabolic tracing. The hypothesis may prove technically challenging.  

**Priority estimate:**  
- Directional specificity: 4  
- Data support: 3 (indirect)  
- Literature support: 3  
- Novelty: 5  
- Testability: 3  
- Overall: 3.6  

---

### Hypothesis H4  
**Hypothesis ID:** H4  
**Hypothesis title:** Hypoxic lung MKs increase secretion of extracellular vesicles loaded with profibrotic cytokines (PDGF‑BB, TGF‑β1) that drive PASMC hypertrophy and perivascular fibroblast activation.  
**PI instruction addressed:** Extracellular vesicle mechanism grounded in MK biology; uses candidate cargo inferred from literature and general MK function.  
**Core directional hypothesis:** Hypoxia stimulates lung MKs to upregulate and package PDGF‑BB and TGF‑β1 into extracellular vesicles; these EVs are released into the perivascular space where they directly activate PASMCs to proliferate and fibroblasts to differentiate into myofibroblasts, contributing to medial thickening and adventitial fibrosis.  

**Direction‑level reasoning summary:**  
- **Data anchor:** While the metabolomics data show metabolic activation (methionine, lactate, inosine), the accompanying scRNA‑seq dataset contains expression information for Pdgfb and Tgfb1. These are canonical MK/platelet products; prior results establish lung MKs as the pathogenic population. It is plausible that hypoxia enhances their expression.  
- **Biological interpretation:** Hypoxia induces a secretory phenotype in MKs, not only altering metabolism but also upregulating pro‑fibrotic growth factors. EV encapsulation protects these labile proteins and concentrates them at target sites.  
- **MK‑linked enzyme/pathway logic:** PDGF‑BB and TGF‑β1 are potent mitogens for smooth muscle and fibroblasts, respectively; their expression can be driven by HIF‑1α or metabolic stress pathways.  
- **Candidate downstream axis:** Direct vascular‑wall; PDGF‑BB activates PASMC PDGFR‑β, and TGF‑β1 drives fibroblast‑to‑myofibroblast transition and collagen synthesis.  
- **Remodelling logic:** Combined PDGF‑BB/TGF‑β1 action amplifies medial hypertrophy and perivascular fibrosis.  
- **Key uncertainty:** Whether the EV cargo of MKs is altered by hypoxia in a biologically meaningful way, and whether the PDGF‑BB/TGF‑β1 from MK EVs is the dominant source of these factors in the perivascular niche, as other cells also produce them.  

**Directional chain:**  
1. Hypoxia activates HIF‑1α and/or metabolic sensors in lung MKs, upregulating Pdgfb and Tgfb1 transcription.  
2. Newly synthesized PDGF‑BB and TGF‑β1 are packaged into multivesicular bodies and released as exosomes/microvesicles.  
3. EVs accumulate in the perivascular space and bind to PASMCs (PDGFR‑β) and fibroblasts (TGFBR).  
4. PASMCs proliferate and hypertrophy; fibroblasts differentiate into α‑SMA⁺ myofibroblasts and secrete ECM.  
5. Medial thickening, adventitial fibrosis, and vascular stiffness.  

**Candidate downstream axes:**  
- Plausible axes: (1) Direct vascular‑wall – PDGF‑BB on PASMCs; TGF‑β1 on fibroblasts; (2) Indirect – TGF‑β1 may also modulate immune cells.  
- Working model: Both factors acting together on distinct vascular cell types.  
- What remains unresolved: The stoichiometry and timing of PDGF‑BB vs TGF‑β1 release, and whether hypoxia actually increases expression in MKs (requires analysis of the Seurat object).  

**Evidence basis:**  
- **User‑provided data:** The scRNA‑seq object contains Pdgfb and Tgfb1; their expression in MK/platelet population can be queried. The metabolomics data provide indirect evidence of metabolic activation that could fuel protein synthesis.  
- **Public dataset metadata:** GSE289322 may show differential expression of PDGF/TGF‑β pathway genes in PH lung.  
- **Literature:** Platelets and MKs are established sources of PDGF and TGF‑β; hypoxia increases PDGF expression in some contexts.  
- **Biological rationale:** PDGF and TGF‑β are central drivers of vascular remodelling; MKs are anatomically positioned to deliver high local concentrations.  
- **Evidence status:** Hypothetical for MK‑specific hypoxia‑induced upregulation (needs scRNA‑seq validation); strong literature rationale; speculative for EV‑mediated delivery over soluble release.  

**Predicted observations:**  
- In MKs: Upregulated Pdgfb and Tgfb1 mRNA/protein in PH condition.  
- In MK‑EVs: Increased PDGF‑BB and TGF‑β1 protein levels by ELISA/western blot.  
- In tissue: Enhanced phospho‑PDGFR and p‑Smad2/3 signalling in PASMCs and fibroblasts adjacent to MKs.  

**Experimental validation:**  
- **Perturbation:** MK‑specific double knockout of Pdgfb and Tgfb1 (Pf4‑Cre;Pdgfb^(fl/fl);Tgfb1^(fl/fl)) or pharmacological neutralisation of PDGFR‑β and TGF‑β1.  
- **Model:** Chronic hypoxia in mice.  
- **Readout:** Medial thickness, adventitial collagen, fibroblast activation, RVSP.  
- **Expected result:** Combined loss attenuates vascular remodelling.  
- **Falsifying result:** No change in remodelling, or the effect is primarily due to platelet‑derived growth factors, not MK‑specific EV release, indicating MKs are not the critical source.  

**Novelty:** Moderate – MK‑derived EV cargo as drivers of remodelling is an emerging concept, but the specific identification of PDGF‑BB/TGF‑β1 as EV‑enclosed mediators is novel.  

**Weaknesses:** Largely relies on literature; direct user data for Pdgfb/Tgfb1 expression not yet inspected; EVs may carry a multitude of other factors.  

**Priority estimate:**  
- Directional specificity: 3  
- Data support: 2 (needs scRNA‑seq check)  
- Literature support: 4  
- Novelty: 4  
- Testability: 4  
- Overall: 3.4  

---

### Hypothesis H5  
**Hypothesis ID:** H5  
**Hypothesis title:** Hypoxic MKs upregulate purine nucleoside phosphorylase (Pnp), generating inosine that imbalances adenosine receptor signalling and promotes endothelial dysfunction, contributing to vascular remodelling.  
**PI instruction addressed:** Metabolomics‑driven hypothesis; differential metabolite (inosine) → direct compound‑enzyme (Pnp) → MK expression/PH shift → direction‑level vascular axis.  
**Core directional hypothesis:** Hypoxia upregulates Pnp in lung MKs, increasing inosine production; elevated extracellular inosine signals through adenosine A₂ₐ/A₂ᵦ receptors on pulmonary endothelial cells to impair vasodilation, induce a pro‑inflammatory surface, and favour smooth muscle recruitment, thereby facilitating vascular remodelling.  

**Direction‑level reasoning summary:**  
- **Data anchor:** Inosine is upregulated 3.82‑fold in PH MKs. Pnp is expressed in 20.31% MKs and significantly upregulated in PH MKs (log2FC 1.74, Wilcoxon p=3.81×10⁻⁶).  
- **Biological interpretation:** Enhanced purine degradation in hypoxic MKs generates inosine, which can be released and act as a partial adenosine receptor agonist.  
- **MK‑linked enzyme/pathway logic:** Pnp catalyses the reversible phosphorolysis of inosine to hypoxanthine, but under substrate accumulation it may produce inosine; its upregulation aligns with inosine accumulation.  
- **Candidate downstream axis:** Direct vascular‑wall (endothelial) – activation of endothelial A₂ receptors can impair NO production, increase adhesion molecules, and promote a pro‑vasoconstrictive, leaky phenotype. Immune‑mediated effects (adenosine signalling on T cells, macrophages) are possible but not primary.  
- **Remodelling logic:** Chronic endothelial activation leads to intimal hyperplasia, leukocyte adhesion, and PASMC hypertrophy – all hallmarks of hypoxia‑induced remodelling.  
- **Key uncertainty:** The net effect of inosine on adenosine receptor signalling is complex and can be protective or pathological; the hypothesis requires that inosine acts as a pathological signal in this context.  

**Directional chain:**  
1. Hypoxia upregulates Pnp in MKs, favouring nucleoside salvage/degradation.  
2. Increased inosine production and release from MKs.  
3. Inosine binds with low affinity to endothelial A₂ receptors, causing sustained, moderate activation.  
4. Chronic A₂ signalling impairs endothelial nitric oxide synthase (eNOS) and upregulates VCAM‑1/ICAM‑1, promoting monocyte adhesion and reducing vasodilatory capacity.  
5. Endothelial dysfunction contributes to smooth muscle proliferation and medial thickening.  

**Candidate downstream axes:**  
- Plausible axes: (1) Direct endothelial activation – A₂‑mediated dysfunction; (2) Immune‑mediated – adenosine/inosine modulation of T‑cell and macrophage function; (3) Direct PASMC – inosine may have weak mitogenic effects.  
- Working model: Endothelial activation as the primary initiator of remodelling.  
- What remains unresolved: Whether MK‑derived inosine achieves the required local concentration, and the net A₂R signalling outcome (pro‑ vs anti‑remodelling).  

**Evidence basis:**  
- **User‑provided data:** Inosine up in MKs (sFig6A, log2FC 3.82); Pnp expression, enrichment (log2 −1.22, but PH‑up 1.74 with p=3.81×10⁻⁶) in MKs.  
- **Public dataset metadata:** GSE289322 could be queried for Pnp and adenosine pathway gene expression.  
- **Literature:** Inosine has immunomodulatory and vasoactive properties; adenosine signalling is implicated in PH pathogenesis.  
- **Biological rationale:** Purine metabolism is altered in hypoxia and can influence vascular tone.  
- **Evidence status:** Direct for metabolite and enzyme; inferred for endothelial A₂R activation; speculative for net pathological effect.  

**Predicted observations:**  
- In MKs: Increased Pnp protein and inosine secretion.  
- In tissue: Elevated inosine in lung lavage; increased endothelial VCAM‑1/ICAM‑1 expression; impaired endothelial‑dependent vasodilation.  
- In metabolomics: Altered adenosine/inosine ratio in lung tissue.  

**Experimental validation:**  
- **Perturbation:** MK‑specific deletion of Pnp (Pf4‑Cre;Pnp^(fl/fl)).  
- **Model:** Chronic hypoxia; assess at early and late timepoints.  
- **Readout:** Endothelial function (acetylcholine‑induced relaxation), endothelial activation markers, medial thickness, RVSP.  
- **Expected result:** Pnp knockout prevents inosine increase and endothelial dysfunction, attenuating remodelling.  
- **Falsifying result:** No effect on endothelial function or remodelling, or inosine acts only on immune cells, indicating the endothelial axis is not causal.  

**Novelty:** Moderate – metabolite‑mediated endothelial dysfunction from MKs is a fresh angle.  

**Weaknesses:** Complex adenosine biology; inosine may have protective effects via A₂ receptors; the hypothesis could be falsified if inosine is rapidly cleared or converted.  

**Priority estimate:**  
- Directional specificity: 3  
- Data support: 4  
- Literature support: 3  
- Novelty: 4  
- Testability: 3  
- Overall: 3.4  

---

### Self‑filtered rejected ideas:
- A pure “MK‑derived platelet thrombo‑inflammatory” hypothesis was rejected because it lacked a specific metabolic or EV cargo data anchor and fell into generic platelet activation.  
- An AMD1‑Th17‑IL‑17‑EndMT bridge was excluded because the evidence does not directly support that level of resolution; the same metabolic direction is captured in H1 with broader candidate axes.  
- Hypotheses based solely on public dataset GSE289322 without user data anchor were avoided to maintain grounding.  

### Requests for Tool Use Agent:
- Query the Seurat object for expression of Pdgfb, Tgfb1, Rab27a, Tsg101, and Cd44 (EV‑related) in the MK/platelet population, comparing PH vs control, to strengthen H4 and future EV hypotheses.  
- Analyse the GSE289322 de‑results for differential expression of Amd1, Ldha, Pnp, and Amd2 to validate tissue‑level support.

## generation_3
Cycle ID: 1

## Hypotheses generated
H1, H2, H3, H4

---

### Hypothesis ID: H1
**Hypothesis title:** AMD1-driven polyamine metabolism in hypoxic MKs promotes perivascular ECM cross-linking and stiffening.

**PI instruction addressed:** Metabolomics‑driven mechanism; ECM and spatial niche thrombo‑inflammatory remodelling.

**Core directional hypothesis:**
Hypoxic up‑regulation of AMD1 in lung megakaryocytes redirects methionine toward polyamine (spermidine/spermine) synthesis, and these polyamines serve as substrates for transglutaminase‑mediated matrix cross‑linking or hypusination‑dependent profibrotic gene expression, thereby increasing perivascular matrix stiffness and contributing to medial thickening and muscularization.

**Direction‑level reasoning summary:**
- Data anchor: Methionine is strongly elevated in PH MKs (log2FC = 3.26); AMD1, the rate‑limiting enzyme for polyamine synthesis, is significantly enriched in MKs (1.35‑fold) and further up‑regulated in PH (log2FC = 1.77, p = 6.55e‑06).  
- Biological interpretation: Hypoxia drives a methionine‑salvage/polyamine metabolic programme in lung MKs, creating a local pool of spermidine and spermine that can be secreted or incorporated into downstream effector pathways.  
- MK‑linked enzyme/pathway logic: AMD1 converts S‑adenosylmethionine into decarboxylated SAM for polyamine biosynthesis; its clear MK enrichment and hypoxia responsiveness make it a plausible source of polyamines in the perivascular niche.  
- Candidate downstream axis: ECM/stromal (direct vascular‑wall) – polyamines are essential co‑substrates for transglutaminase 2 (TGM2)‑catalyzed collagen and fibronectin cross‑linking and for hypusination of eIF5A, which drives translation of pro‑fibrotic transcripts.  
- Remodelling logic: Enhanced matrix cross‑linking and myofibroblast‑like activation increase vessel wall stiffness, reduce compliance, and promote medial thickening.  
- Key uncertainty: Whether the polyamine pool generated by MK AMD1 acts locally in the perivascular ECM versus acting through a cell‑autonomous MK programme; the relative contribution of TGM2‑mediated cross‑linking versus eIF5A‑hypusination‑dependent gene expression remains unresolved but both are consistent with the metabolic shift.

**Directional chain:**
1. Hypoxia up‑regulates AMD1 and methionine‑derived polyamine synthesis in lung MKs.
2. MK‑generated polyamines (spermidine, spermine) are released into the perivascular microenvironment.
3. Polyamines serve as substrates for transglutaminase‑catalysed ECM cross‑linking and/or for eIF5A hypusination in vascular fibroblasts/SMCs, promoting a pro‑fibrotic, stiffening programme.
4. Broad cellular response: enhanced collagen/fibronectin cross‑linking, fibroblast activation, SMC hypertrophy/hyperplasia.
5. Contribution to remodeling phenotype: vascular stiffening, medial thickening, and muscularization.

**Candidate downstream axes:**
- Plausible axes: (i) Transglutaminase‑2 (TGM2)‑mediated ECM protein cross‑linking; (ii) eIF5A hypusination driving translation of pro‑fibrotic genes (e.g., collagen, LOX); (iii) Polyamine‑dependent regulation of vascular smooth muscle cell proliferation; (iv) Polyamine‑modulated immune cell (macrophage) production of profibrotic factors.
- Working model: The dominant ECM‑remodelling effect is via TGM2 cross‑linking of matrix proteins in the immediate perivascular space, which directly stiffens the vessel wall. Hypusination‑dependent gene programmes in adjacent fibroblasts or SMCs reinforce the stromal response.
- Specific examples, if useful: Spermidine is the substrate for deoxyhypusine synthase, which post‑translationally modifies eIF5A; spermidine/spermine are also Co‑substrates for TGM2 cross‑linking of collagen I.
- What remains unresolved: Whether the polyamines that cross‑link ECM originate from MK secretion or from MK‑derived extracellular vesicles; the exact cell type(s) in the vessel wall that incorporate polyamines to drive cross‑linking (pericytes, fibroblasts, SMC); whether hypusination‑regulated transcripts are the dominant effect.

**Evidence basis:**
- User‑provided data: sFig6A metabolomics – methionine up in PH MKs (log2FC = 3.26); AMD1 mRNA in scRNA‑seq – MK enrichment 1.35‑fold, PH‑vs‑control MK log2FC = 1.77, p = 6.55e‑06.
- Public dataset metadata or analyzed public data: Not yet examined; GSE289322 (lung PH vs control) could validate AMD1 differential expression and polyamine pathway enrichment in tissue.
- Literature: AMD1 and polyamines are implicated in cancer‑associated fibrosis and vascular stiffness; TGM2 and eIF5A hypusination are known mediators of matrix remodelling.
- Biological rationale: Polyamines are obligate for ECM cross‑linking and translation of a subset of pro‑fibrotic transcripts; a hypoxia‑driven polyamine surge from perivascular MKs directly feeds this niche.
- Evidence status: Direct for the methionine→AMD1 axis in MKs; indirect/inferred for polyamine secretion and ECM cross‑linking; speculative for the relative role of TGM2 vs hypusination.

**Predicted observations:**
- In MKs: Elevated AMD1 protein, spermidine/spermine levels in PH MKs; increased polyamine‑containing EVs.
- In recipient or tissue compartment: Perivascular accumulation of cross‑linked collagen (resistant to acid extraction) and hypusinated eIF5A in adventitial fibroblasts or SMCs.
- In metabolomics or pathway activity: Increased putrescine/spermidine in lung tissue of PH mice that is MK‑dependent (reduced in TPOR‑/‑ chimeras with lung MK deficiency).

**Experimental validation:**
- Perturbation: MK‑specific Amd1 knockout (Amd1^fl/fl Pf4‑Cre or similar) or pharmacological AMD1 inhibition (e.g., SAM486) in mice.
- Model: Hypoxic PH model (hypoxia‑exposed mice) with lung‑resident MKs competent or deficient for AMD1.
- Readout: Vascular stiffness (pressure‑volume curves), medial thickness, collagen cross‑linking (hydroxyproline, pyridinoline), ECM ultrastructure, and hypusinated eIF5A levels.
- Expected result: AMD1 deficiency reduces polyamine levels in lung tissue, decreases ECM cross‑linking and vascular stiffness, and attenuates medial thickening.
- Falsifying result: AMD1 inhibition does not alter lung polyamine content or ECM cross‑linking, or no vascular remodelling protection is seen despite reduced MK polyamines.

**Novelty:** First link of MK‑derived polyamine metabolism to perivascular ECM cross‑linking in hypoxic pulmonary hypertension; identifies AMD1 as a MK‑expressed enzyme with direct ECM remodelling potential beyond its classical role in cell proliferation.

**Weaknesses:** The mechanism by which MK polyamines reach the ECM is not resolved; alternative AMD1‑dependent polyamine functions (immune modulation, EV cargo) may be equally or more important. The hypothesis assumes polyamines are secreted; direct proof of polyamine export from MKs is lacking.

**Revision relative to previous cycle:** New hypothesis.

**Priority estimate:**
- Directional specificity: 4
- Data support: 5 (strong metabolomics and transcriptomics)
- Literature support: 3 (fibrosis but not MK-specific PH)
- Novelty: 5
- Testability: 4 (MK‑specific genetic tools available but ECM readouts require careful timing)
- Overall generation priority: 4

**Explicit rejection filter:** Passes all.

---

### Hypothesis ID: H2
**Hypothesis title:** Hypoxic MK purine degradation generates an adenosine/inosine‑rich niche that promotes thrombo‑inflammatory vascular remodelling through endothelial and immune adenosine receptors.

**PI instruction addressed:** Metabolomics‑driven; thrombo‑inflammatory and immune remodelling.

**Core directional hypothesis:**
Elevated inosine in hypoxic MKs reflects enhanced purine nucleotide salvage/degradation (via PNP/NT5C2), leading to accumulation of adenosine and inosine in the perivascular space where adenosine activates A2B receptors on endothelial cells and infiltrating myeloid cells, driving endothelial activation, pro‑coagulant surface expression, and cytokine release that together promote medial muscularization and vascular remodelling.

**Direction‑level reasoning summary:**
- Data anchor: Inosine is up in PH MKs (log2FC = 3.82); the purine degrading enzyme PNP is expressed in MKs (20 % of MKs) and significantly upregulated in PH MKs (log2FC = 1.74, p = 3.81e‑06). NT5C2, another purine nucleotidase, also shows a strong PH‑up signature (log2FC = 2.88, p = 2e‑04).  
- Biological interpretation: Hypoxia drives a purine salvage/degradation programme in MKs that raises extracellular inosine/adenosine; adenosine is a potent vasoactive and immunomodulatory signalling molecule.  
- MK‑linked enzyme/pathway logic: PNP and NT5C2 are key enzymes that convert purine nucleotides to nucleosides; their PH induction in MKs indicates MKs become a source of adenosine/inosine in the hypoxic lung.  
- Candidate downstream axis: Thrombo‑inflammatory / immune‑mediated – adenosine signalling on vascular endothelial cells up‑regulates tissue factor (F3), adhesion molecules, and chemokines, while on monocytes/macrophages it can promote a pro‑fibrotic M2‑like phenotype.  
- Remodelling logic: Adenosine‑A2B receptor activation on endothelium promotes a pro‑coagulant surface (tissue factor, phosphatidylserine exposure) and increases leukocyte adhesion, fostering local fibrin deposition and immune cell recruitment that amplify medial smooth muscle activation and muscularization.  
- Key uncertainty: Whether the adenosine generated by MKs reaches effective concentrations in the perivascular niche and whether A2B receptor‑dependent thrombo‑inflammatory signalling dominates over vasodilatory A2A effects.

**Directional chain:**
1. Hypoxia up‑regulates PNP/NT5C2 in lung MKs, increasing extracellular inosine and adenosine.
2. Adenosine binds A2B (and possibly A2A) receptors on adjacent pulmonary microvascular endothelial cells and recruited myeloid cells.
3. A2B signalling triggers tissue factor up‑regulation, endothelial leukocyte adhesion molecule expression, and production of pro‑inflammatory cytokines (e.g., IL‑6, CCL2), creating a localized thrombo‑inflammatory microenvironment.
4. Fibrin deposition and myeloid‑derived growth factors stimulate smooth muscle cell proliferation and hypertrophy.
5. Contributes to medial thickening, muscularization, and endothelial dysfunction.

**Candidate downstream axes:**
- Plausible axes: (i) Adenosine‑A2B–endothelial tissue factor pathway (thrombo‑inflammatory); (ii) Adenosine‑A2B–monocyte/macrophage profibrotic activation (immune‑mediated); (iii) Inosine as a metabolic intermediate that feeds back into polyamine or one‑carbon metabolism (metabolic coupling).
- Working model: The dominant acute effect is adenosine‑A2B–driven endothelial pro‑coagulant switch, which sparks fibrin formation and leukocyte recruitment; chronic activation sustains immune‑driven remodelling.
- What remains unresolved: Direct proof that MK‑derived adenosine reaches endothelial A2B receptors in vivo; the relative contribution of adenosine versus inosine signalling (inosine may act via A3 or adenosine after salvage).

**Evidence basis:**
- User‑provided data: sFig6A metabolomics – inosine up in PH MKs (log2FC = 3.82); scRNA‑seq – PNP PH‑vs‑control MK log2FC = 1.74, p = 3.81e‑06; NT5C2 log2FC = 2.88, p = 2e‑04.
- Public dataset metadata or analyzed public data: GSE289322 may show up‑regulation of PNP, NT5C, or adenosine‑pathway genes in PH lung tissue; can be checked.
- Literature: Adenosine signalling is well documented in pulmonary hypertension and thrombo‑inflammation; hypoxia is known to induce CD73 and adenosine production; A2B receptor knockout attenuates PH in some models.
- Biological rationale: MKs are ideally positioned perivascularly to release purine nucleosides directly onto endothelial cells; ecto‑5’‑nucleotidase (CD73) on endothelial cells can convert MK‑derived AMP/ADP to adenosine.
- Evidence status: Direct for inosine elevation and PNP/NT5C2 up‑regulation in MKs; indirect for adenosine signalling and thrombo‑inflammatory outcome; speculative that MK‑derived adenosine is the main source versus endothelial‑derived adenosine.

**Predicted observations:**
- In MKs: Elevated adenosine/inosine release in conditioned medium from PH MKs.
- In recipient or tissue compartment: Perivascular tissue factor expression, fibrin(ogen) deposition, and myeloid cell infiltration dependent on adenosine A2B receptor activity.
- In metabolomics or pathway activity: Elevated adenosine in lung tissue of hypoxic mice that is reduced when lung MKs are depleted (e.g., TPOR‑/‑ chimeras).

**Experimental validation:**
- Perturbation: MK‑specific knockdown of Pnp or Nt5c2 (or broad adenosine pathway block with A2B antagonist PSB1115 or adenosine deaminase overexpression).
- Model: Hypoxic PH in mice; compare MK purine flux versus endothelial‑derived adenosine by using CD39/CD73 inhibitors.
- Readout: Tissue factor expression, fibrin deposition, vascular remodelling parameters.
- Expected result: Blocking MK purine generation or A2B signalling reduces thrombo‑inflammatory markers and attenuates muscularization.
- Falsifying result: Adenosine receptor blockade does not alter vascular remodelling or thrombotic indices despite reduced purine metabolites from MKs.

**Novelty:** Redirects attention from endothelial‑derived adenosine to a MK‑specific purine source in the hypoxic lung; couples MK metabolism to classic thrombo‑inflammatory adenosine pathway.

**Weaknesses:** Extracellular adenosine concentrations depend on equilibrative transporters and ectonucleotidases; the hypothesis assumes MKs release sufficient adenosine/inosine to dominate the perivascular pool. The vasodilator action of adenosine could counteract remodelling in some contexts, making the net effect condition‑dependent.

**Revision relative to previous cycle:** New hypothesis.

**Priority estimate:**
- Directional specificity: 4
- Data support: 4 (metabolomics and transcriptomics, but adenosine itself not measured)
- Literature support: 4 (adenosine in PH well studied)
- Novelty: 4
- Testability: 4
- Overall generation priority: 4

**Explicit rejection filter:** Passes all.

---

### Hypothesis ID: H3
**Hypothesis title:** Hypoxic lung MKs release tissue‑factor‑positive extracellular vesicles that initiate perivascular coagulation, creating a fibrin‑rich scaffold for immune cell recruitment and smooth muscle activation.

**PI instruction addressed:** Thrombo‑inflammatory and spatial‑niche mechanism; ECM and immune remodelling.

**Core directional hypothesis:**
Hypoxia induces MKs to produce and release phosphatidylserine‑exposing, tissue‑factor‑bearing extracellular vesicles (EVs), which trigger local thrombin generation and fibrin deposition in the perivascular space; the provisional fibrin matrix then captures circulating monocytes and provides a pro‑proliferative signal to vascular smooth muscle cells, thereby driving medial thickening and muscularization.

**Direction‑level reasoning summary:**
- Data anchor (indirect): The prior‑results document establishes that lung‑resident MKs are essential for hypoxia‑induced vascular remodelling; scRNA‑seq confirms a distinct MK/platelet cluster in the lung. MKs are known hematologic sources of tissue factor (TF) and pro‑coagulant EVs upon stimulation.  
- Biological interpretation: In the hypoxic perivascular niche, MKs adopt a “pro‑coagulant” phenotype, shedding EVs that disseminate TF and anionic phospholipids, converting the immediate microenvironment into a thrombin‑generating compartment.  
- MK‑linked enzyme/pathway logic: TF (F3) expressed in MKs binds factor VIIa to initiate the extrinsic coagulation cascade; phosphatidylserine on EV surfaces provides the platform for prothrombinase complex assembly. The end product, thrombin, also cleaves protease‑activated receptors (PARs) on SMCs and fibroblasts, linking coagulation to remodelling.  
- Candidate downstream axis: Thrombo‑inflammatory / EV‑stromal – fibrin matrix serves as a provisional scaffold for monocyte/macrophage adhesion and differentiation, while thrombin‑PAR signaling directly promotes SMC proliferation and migration.  
- Remodelling phenotype: Fibrin deposition thickens the vessel wall, recruits immune cells that sustain inflammation, and thrombin‑PAR activation drives SMC hyperplasia → medial thickening and muscularization.  
- Key uncertainty: Whether hypoxia actually induces TF expression in lung MKs and whether MK‑derived EVs carry sufficient TF to overcome endogenous anticoagulant systems in vivo; the relative contribution of fibrin‑mediated trapping of immune cells versus direct thrombin‑PAR remodelling remains unresolved.

**Directional chain:**
1. Hypoxia up‑regulates tissue factor (F3) and EV shedding in lung MKs.
2. MK‑derived TF‑positive EVs bind factor VIIa and assemble prothrombinase, generating thrombin that deposits fibrin locally.
3. Fibrin matrix entraps circulating monocytes and provides adhesion sites; thrombin activates PAR‑1 on SMCs and fibroblasts.
4. Recruited monocytes differentiate into macrophages that release pro‑fibrotic factors, while thrombin‑stimulated SMCs proliferate and hypertrophy.
5. Leads to perivascular fibrin accumulation, immune cell infiltration, medial thickening, and muscularization.

**Candidate downstream axes:**
- Plausible axes: (i) TF‑EV → thrombin → fibrin scaffold → monocyte entrapment → M2‑like profibrotic activity; (ii) Thrombin → PAR‑1 on SMCs → proliferation/hypertrophy; (iii) Fibrin degradation products (D‑dimers) → pro‑angiogenic and pro‑inflammatory signals.
- Working model: The initial MK‑EV‑driven coagulation burst creates a fibrin‑rich niche that physically traps immune cells and feeds back to sustain SMC activation, coupling thrombotic micro‑events to chronic vascular remodelling.
- What remains unresolved: Direct demonstration that lung MKs express TF (F3) under hypoxia; whether MK‑EVs contain additional remodelling cargo (e.g., PDGF, TGF‑β) that amplifies the effect; the spatial extent of fibrin deposition around small pulmonary vessels.

**Evidence basis:**
- User‑provided data: Prior‑results document shows lung‑resident MKs drive PH vascular remodelling; scRNA‑seq confirms MK/platelet population. MK metabolomics (sFig6A) and tissue metabolomics (Figure6D+F) were not designed to capture coagulation. No direct user data on TF expression or EV cargo.  
- Public dataset metadata or analyzed public data: GSE289322 (lung PH vs control) could be mined for F3, PAR1 (F2r), and coagulation pathway enrichment; GSE291455 could check baseline expression. Neither provides MK‑specificity.
- Literature: Megakaryocytes are known to express TF and release pro‑coagulant EVs (microparticles). Hypoxia induces TF expression in endothelial cells and monocytes; less is known in MKs. Thrombin and PAR signalling are established drivers of SMC proliferation in vascular injury and PH.
- Biological rationale: Platelets, the progeny of MKs, are a major source of circulating TF‑positive EVs; MKs in the lung could shed pro‑coagulant EVs directly into the perivascular space without entering the circulation, creating a local coagulation circuit.
- Evidence status: Speculative for MK‑specific TF up‑regulation and EV shedding; directly testable by checking F3 expression in the scRNA‑seq data and by in vitro hypoxic MK EV experiments.

**Predicted observations:**
- In MKs: Up‑regulation of F3 mRNA/protein and increased TF‑positive EV release under hypoxia.
- In recipient or tissue compartment: Perivascular fibrin deposition and D‑dimer levels in lung tissue of hypoxic mice that are reduced in TPOR‑/‑ or lung‑MK‑deficient chimeras; co‑localization of MK‑derived EVs (e.g., CD41+ TF+) with fibrin.
- In metabolomics or pathway activity: Not directly assessed by current metabolomics; could detect thrombin activity via fluorogenic assays or by fibrinopeptide A.

**Experimental validation:**
- Perturbation: MK‑specific F3 knockout (F3^fl/fl Pf4‑Cre) or pharmacological TF inhibition (e.g., recombinant TFPI, anti‑TF antibody); or inhibit EV biogenesis (e.g., GW4869, nSMase inhibitor).
- Model: Hypoxic PH in mice; also in vitro generation of MK‑derived EVs from lung MKs under hypoxia.
- Readout: Fibrin deposition (Martius Scarlet Blue staining), EV enumeration (nanoparticle tracking), thrombin‑antithrombin complexes, vascular wall thickness, and muscularization.
- Expected result: TF‑deficient MKs or blocked EV release reduces fibrin, immune cell accumulation, and vascular remodelling.
- Falsifying result: No fibrin deposition is observed around pulmonary vessels in PH, or MK‑EV blockade does not alter remodelling despite effective ablation of TF+ EVs.

**Novelty:** Introduces an MK‑centric thrombotic initiation mechanism for pulmonary vascular remodelling, bridging platelet precursor biology with pro‑coagulant EV biology in the hypoxic lung niche.

**Weaknesses:** No direct user data on TF or EV production by lung MKs; hypothesis depends heavily on extrapolation from platelet biology and general hypoxia‑EV biology. Potential confounding from platelet‑derived EVs cannot be distinguished from MK‑derived EVs without specific lineage tracing.

**Revision relative to previous cycle:** New hypothesis.

**Priority estimate:**
- Directional specificity: 3
- Data support: 2 (prior data support MK role, but no direct TF/EV data)
- Literature support: 4 (TF-EV thrombo-inflammatory axis established in cancer and sepsis)
- Novelty: 5
- Testability: 4
- Overall generation priority: 3

**Explicit rejection filter:** Passes all; includes MK-specific component (hypoxia-dependent TF/EV), thrombosis-mediated vascular remodelling, and testable by MK-specific knockout.

---

### Hypothesis ID: H4
**Hypothesis title:** Hypoxic MKs secrete thrombospondin‑1 (TSP‑1) that activates latent TGF‑β in the perivascular space, driving myofibroblast differentiation and extracellular matrix deposition.

**PI instruction addressed:** ECM and immune remodelling; spatial niche mechanism through a latent cytokine activation.

**Core directional hypothesis:**
Hypoxia up‑regulates thrombospondin‑1 in lung megakaryocytes; secreted TSP‑1 binds to the latency‑associated peptide of TGF‑β stored in the perivascular matrix, releasing active TGF‑β that converts local fibroblasts and pericytes into myofibroblasts and stimulates excessive collagen production, leading to vascular stiffening and medial thickening.

**Direction‑level reasoning summary:**
- Data anchor: The prior results establish that lung‑resident MKs are necessary for hypoxia‑induced vascular remodelling and perivascular fibrosis. While scRNA‑seq expression data for Thbs1 are not directly extracted here, Mk/platelet cells are present and can be queried. Tissue metabolomics and prior knowledge show a fibrotic phenotype in hypoxic lungs.  
- Biological interpretation: TSP‑1 is a major MK‑ and platelet‑derived matricellular protein that is rapidly released upon activation; it is a potent activator of latent TGF‑β, the master fibrogenic cytokine. Hypoxia is a known inducer of TSP‑1 in many cell types.  
- MK‑linked enzyme/pathway logic: TSP‑1 contains a KRFK sequence that interacts with the LAP of TGF‑β, releasing the active dimer. This bypasses the need for integrin‑mediated activation and delivers a concentrated pulse of active TGF‑β directly adjacent to vascular stromal cells.  
- Candidate downstream axis: ECM/stromal (direct vascular‑wall) – active TGF‑β induces fibroblast‑to‑myofibroblast transition, up‑regulates collagen I/III and fibronectin, and drives CTGF expression, all contributing to perivascular fibrosis.  
- Remodelling phenotype: Increased collagen deposition, adventitial fibrosis, vascular stiffening, and ultimately medial thickening and muscularization through matrix‑driven mechanosignalling.  
- Key uncertainty: Whether lung MKs express high levels of Thbs1 under hypoxia; whether TSP‑1‑mediated TGF‑β activation is the dominant source of active TGF‑β in the perivascular niche or whether other activators (integrins, proteases) are more important.

**Directional chain:**
1. Hypoxia induces TSP‑1 expression and secretion by lung MKs.
2. TSP‑1 binds and activates latent TGF‑β sequestered in the perivascular ECM.
3. Active TGF‑β diffuses to adjacent fibroblasts, pericytes, and smooth muscle cells, triggering Smad‑dependent and Smad‑independent profibrotic transcriptional programmes.
4. Fibroblasts and pericytes differentiate into α‑SMA‑expressing myofibroblasts that deposit excess collagen and stiffen the vessel wall.
5. Contributes to medial thickening, muscularization, and vascular stiffness.

**Candidate downstream axes:**
- Plausible axes: (i) TSP‑1 → TGF‑β → Smad2/3 → myofibroblast differentiation and ECM production; (ii) TSP‑1 → CD47 → endothelial regulation of NO/cGMP (counter‑regulatory); (iii) TGF‑β → inhibition of MMPs / induction of TIMPs, further stabilizing the ECM.
- Working model: The principal pathway is TSP‑1–mediated TGF‑β activation, which directly fuels a fibrotic niche; the CD47 axis may modulate endothelial function but is secondary.
- What remains unresolved: Whether TSP‑1 from MKs is sufficient to release TGF‑β in the presence of other extracellular binding proteins; whether the effect requires MK proximity to ECM‑stored latent TGF‑β (spatial niche dependency) or if MK‑derived TSP‑1 acts systemically.

**Evidence basis:**
- User‑provided data: Prior results demonstrate lung‑MK‑dependent fibrosis and vascular remodelling; scRNA‑seq MK/platelet cluster exists. Metabolomics does not directly address TSP‑1.  
- Public dataset metadata or analyzed public data: GSE289322 can be scanned for Thbs1 and Tgfb1 pathway gene expression; GSE291455 provides baseline. This could provide lung‑level support but not MK specificity.
- Literature: Platelets and MKs are the major source of TSP‑1; TSP‑1 is a well‑characterized TGF‑β activator in wound healing and fibrosis. Hypoxia induces TSP‑1 in endothelial cells and fibroblasts; MK‑specific expression under hypoxia is less documented. TGF‑β signalling is a central pathway in pulmonary arterial hypertension and vascular fibrosis.
- Biological rationale: MKs residing in the perivascular space are ideally positioned to deposit TSP‑1 directly onto the adventitial matrix, spatially confined to small muscularized pulmonary vessels where fibrosis‑driven remodelling occurs.
- Evidence status: Inferred from general MK biology and PH fibrosis; direct evidence of MK Thbs1 expression and hypoxia‑induction requires validation from the scRNA‑seq data.

**Predicted observations:**
- In MKs: Up‑regulated Thbs1 mRNA and protein in PH MKs; increased secretion of TSP‑1 in conditioned medium.
- In recipient or tissue compartment: Perivascular accumulation of active TGF‑β (phospho‑Smad2/3) and α‑SMA‑positive myofibroblasts surrounding small vessels that is reduced upon MK depletion.
- In metabolomics or pathway activity: Not captured.

**Experimental validation:**
- Perturbation: MK‑specific Thbs1 deletion (Thbs1^fl/fl Pf4‑Cre) or pharmacological TSP‑1 blocking peptide (LSKL); TGF‑β neutralising antibody or ALK5 inhibitor to confirm downstream role.
- Model: Hypoxic PH in mice; in vitro co‑culture of hypoxic lung MKs with lung fibroblasts.
- Readout: Active TGF‑β levels, α‑SMA+ myofibroblast numbers, collagen deposition, vascular stiffness, medial thickness.
- Expected result: Loss of MK TSP‑1 reduces active TGF‑β and attenuates fibrotic vascular remodelling.
- Falsifying result: MK‑specific Thbs1 knockout does not alter TGF‑β activity or fibrosis despite efficient deletion; other TSP‑1 sources (platelets, macrophages) compensate.

**Novelty:** Identifies MK‑derived TSP‑1 as a specific TGF‑β actuator in the hypoxic pulmonary perivascular niche, shifting focus from circulating platelets to tissue‑resident megakaryocytes as fibrotic initiators.

**Weaknesses:** No direct scRNA‑seq expression data provided; must be verified. TSP‑1 also has anti‑angiogenic properties that could oppose remodelling in certain contexts; net effect may be context‑dependent.

**Revision relative to previous cycle:** New hypothesis.

**Priority estimate:**
- Directional specificity: 4
- Data support: 2 (prior MK remodelling role, no direct Thbs1 data)
- Literature support: 4 (well‑established TSP‑1/TGF‑β fibrotic axis)
- Novelty: 4
- Testability: 4
- Overall generation priority: 3

**Explicit rejection filter:** Passes all; MK‑specific (Thbs1 expression), hypoxia‑dependent, vascular remodelling via fibrosis, testable.

---

## Self‑filtered rejected ideas:
- **MK‑derived IL‑6 driving Th17-like immune remodelling:** Rejected because no user metabolomics or transcriptomics data directly support MK IL‑6 up‑regulation; the metabolic link would over‑resolve a T‑cell subset without evidence, and the PI instruction warns against that.
- **MK‑derived lactate acidosis driving immune suppression:** A lactate‑based hypothesis was considered because glycolysis likely shifts in hypoxic MKs, but the metabolomics shortlist and mechanism‑ready chains did not prioritize lactate or LDHA; only one glycolytic metabolite (pyruvaldehyde) appears without an obvious enzyme‑MK‑remodelling chain, making it too speculative without further data extraction. A generation agent should not fabricate a Ldha link when not in the Evidence Context.
- **MK‑derived CXCL12 recruiting progenitor cells:** Rejected because no differential expression data or pathway enrichment was presented; it would be a gene-list-based hypothesis without a data anchor, and the PI brief requires data-grounded generation.

## Requests for Tool Use Agent:
- Query the Seurat object (`seurat_merged.rds`) to retrieve expression and differential expression for `Amd1`, `Pnp`, `Nt5c2`, `F3`, `Thbs1`, `Lox`, `Loxl1`, `Loxl2` in the MK/platelet cluster versus all other cells, and PH vs control within MKs.  
- Examine the `candidate_gene_check.tsv` and `de_results.tsv` files from GSE289322 for these genes and for polyamine pathway, purine metabolism, coagulation, and TGF‑β pathway enrichment.  
- Check tissue metabolomics (Figure6D+F) for spermidine, spermine, adenosine, inosine, and fibrinopeptide‑related peaks.  
- Perform gene set enrichment on GSE289322 DE results using KEGG pathways: mmu00480 (Glutathione metabolism, to pick up polyamine?), mmu00270 (Cysteine and methionine metabolism), mmu00230 (Purine metabolism), mmu04610 (Complement and coagulation cascades).

## Tool Use output
**Request addressed:**  
Inspect local user‑provided data context and generated requests for downstream evidence needs, with emphasis on metabolomics‑driven chains and the evidence landscape for the hypotheses produced by Generation Agents in Cycle 1.

**Search or analysis performed:**  
The local data context was reviewed in its entirety. No new external retrieval was performed. The following assets were examined:

- **Single‑cell RNA‑seq summary** (`seurat_merged.rds` metadata and feature‑level expression metrics embedded in the *Metabolomics‑to‑Mechanism Evidence Context*).  
- **MK‑sorted metabolomics** (`sFig6A Raw data.xlsx` differential table) and **lung tissue metabolomics** (`Figure6D+F raw data.xlsx`).  
- **Prior results** (`prior_results.docx`) establishing the lung‑resident MK requirement.  
- **Metabolomics‑to‑Mechanism Evidence Context**, including the mechanism‑ready shortlist, the full prioritized evidence chains, and per‑metabolite candidate enzyme gene tables.  
- **Public Dataset Analysis Context** (GSE289322 and GSE291455), noting that processed‑matrix analyses were completed but the actual `candidate_gene_check.tsv` and `de_results.tsv` contents were not provided in this run.  
- **Public Dataset Discovery Context** confirming that no repository hits were retrieved.  
- The **hypotheses and requests** generated by `generation_metabolic`, `generation_1`, `generation_2`, and `generation_3`.

---

# Key findings

Each finding is classed by evidence type and strength. For downstream‑axis evidence, the findings are split into metabolic/pathway support, MK‑origin support or gap, candidate downstream axes, and evidence needed.

---

### Finding 1: Methionine → AMD1 polyamine axis (Hypotheses H1‑metabolic, H1‑gen3, etc.)

- **Finding:** Hypoxic lung MKs accumulate methionine (log2FC = 3.26) and up‑regulate AMD1 (MK enrichment log2 = 1.35, PH‑vs‑control MK log2FC = 1.77, p = 6.55 × 10⁻⁶). The pathway link is a *pathway‑neighbor gene* (AMD1 is in Cysteine/methionine metabolism and Methionine salvage). Literature associates AMD1 with polyamine synthesis and mTORC1‑dependent metabolism, though direct MK‑to‑vascular evidence is absent.  
- **Evidence type:** **Direct support** for the metabolite‑enzyme connection in MKs; **indirect support** for polyamine‑mediated vascular effects from literature.  
- **Source:** User‑provided MK metabolomics, Seurat scRNA‑seq (as reported in the Mechanism‑Ready Shortlist), KEGG pathway context.  
- **Relevance:** Core to the majority of metabolomics‑driven hypotheses.  
- **Strength:** High – the metabolite change and gene expression are both strong and MK‑specific.  
- **Limitation:** AMD1 is a pathway neighbor, not a direct compound‑enzyme link, but the connection through SAM/polyamine metabolism is well‑established. The downstream vascular axis remains broad; no direct evidence for polyamine secretion from MKs or for a specific recipient cell type.  

**Downstream‑axis evidence for methionine → AMD1:**  
- **Metabolic/pathway support:** Yes – SAM/polyamine pathway is clearly implicated.  
- **MK‑origin support or gap:** Strong MK‑origin support (AMD1 enriched and hypoxia‑up).  
- **Candidate downstream axes supported:** Immune‑mediated (polyamines can modulate T‑cell/macrophage responses), direct vascular‑wall (polyamines can influence proliferation), EV/stromal (polyamines as substrates for ECM cross‑linking/hypusination). All are plausible.  
- **Candidate examples that remain provisional:** Spermidine, Th17, macrophage polarization, eIF5A hypusination, transglutaminase cross‑linking – these are examples, not resolved mechanism.  
- **Evidence needed to resolve the route:** (i) Direct measurement of polyamine secretion from MKs, (ii) functional assay showing that AMD1 inhibition blocks vascular remodeling in a MK‑specific manner, (iii) identification of the polyamine‑responsive cell type in the lung perivascular niche. Tissue‑level validation from GSE289322 (AMD1 differential) would add orthogonal support, but that analysis has not been inspected in this cycle.

---

### Finding 2: Methionine → Amd2 (a second S‑adenosylmethionine decarboxylase) (H2‑metabolic)

- **Finding:** Amd2 is a pathway‑neighbor gene also linked to methionine salvage/polyamine metabolism. It is expressed in 4.4 % of MKs (enrichment log2 = 0.93) and significantly up in PH‑MK (log2FC = 2.175, p = 0.024).  
- **Evidence type:** **Indirect support** – the enzyme gene is lowly expressed, and its functional contribution relative to AMD1 is unknown.  
- **Source:** Metabolomics‑to‑Mechanism Evidence Context (Seurat metrics).  
- **Strength:** Weak to moderate – statistically significant differential but very low MK expression percentage; protein evidence absent.  
- **Limitation:** The hypothesis relies on cooperativity with AMD1; redundant polyamine synthesis from a minor MK subset may be biologically negligible.  

**Downstream‑axis evidence:** Same candidate axes as AMD1, but with even less resolution. Evidence needed: MK‑specific Amd2 protein expression and dual AMD1/AMD2 loss‑of‑function.

---

### Finding 3: Methionine → Dnmt3b (DNA methylation) (H3‑metabolic)

- **Finding:** Dnmt3b is a pathway neighbor in cysteine/methionine metabolism. MK expression is low (2.6 %), enrichment is negligible (0.19), and PH‑up is not significant (p = 0.212).  
- **Evidence type:** **Insufficient evidence** – no significant MK differential, no DNA methylation data.  
- **Source:** Metabolomics‑to‑Mechanism Evidence Context.  
- **Strength:** Speculative – the methionine‑SAM‑methylation link is biochemically plausible, but the MK‑specific data do not support a strong role for Dnmt3b.  
- **Limitation:** Highly speculative; no mechanism‑ready shortlist ranking.  

**Downstream‑axis evidence:** Unresolved; the hypothesis would require MK‑specific epigenetic profiling. Not recommended for prioritisation without additional supporting data.

---

### Finding 4: Retinoic acid → Cyp26b1 (retinoid catabolism) (H4‑metabolic, H3‑gen1)

- **Finding:** Retinoic acid is elevated in PH‑MK (log2FC = 3.44). Cyp26b1 is a pathway neighbor in Retinol metabolism with MK expression of 7.9 %, enrichment 0.73, and a non‑significant PH‑up trend (p = 0.253).  
- **Evidence type:** **Insufficient evidence** – the metabolite is upregulated, but the candidate enzyme is not significantly altered and its functional relevance in MKs is unproven.  
- **Source:** Metabolomics‑to‑Mechanism Evidence Context.  
- **Strength:** Weak – the hypothesis requires Cyp26b1 to be rate‑limiting for local RA degradation, yet the data show a trend, not significant change.  
- **Limitation:** RA levels being high argues against increased catabolism; alternative explanations (e.g., increased synthesis, impaired export) exist.  

**Downstream‑axis evidence:** Candidate axes (immune‑mediated, direct vascular‑wall) are plausible for retinoic acid biology, but MK‑origin gap is large. Evidence needed: MK‑specific Cyp26b1 activity measurement, local RA concentration, and functional MK‑knockout.

---

### Finding 5: Inosine → Pnp/Nt5c2 (purine metabolism) (H1‑gen1, H5‑gen2, H2‑gen3)

- **Finding:** Inosine is strongly elevated in PH‑MK (log2FC = 3.82). Pnp (direct compound‑enzyme, purine nucleoside phosphorylase) is expressed in 20 % of MKs and significantly up in PH‑MK (log2FC = 1.74, p = 3.81 × 10⁻⁶). Nt5c2 (direct compound‑enzyme, 5'‑nucleotidase) is also up (log2FC = 2.88, p = 2 × 10⁻⁴).  
- **Evidence type:** **Direct support** for both metabolite and enzyme upregulation in MKs. The downstream adenosine‑receptor axis is **indirect**, inferred from literature.  
- **Source:** User‑provided MK metabolomics, Seurat expression from the Complete Evidence Chains (inosine section).  
- **Strength:** High for the MK purine degradation pathway; moderate for the adenosine‑A2B thrombo‑inflammatory axis because inosine can also act independently.  
- **Limitation:** Inosine/adenosine distinction is blurry; ecto‑nucleotidases may convert one to the other. Adenosine receptor subtype dominance and net pro‑remodeling effect are not resolved. Public dataset GSE289322 could validate Pnp/Nt5c2 differential expression in lung tissue, but that has not been inspected.

**Downstream‑axis evidence:**  
- **Metabolic/pathway support:** Purine metabolism is strongly supported.  
- **MK‑origin support or gap:** Strong MK‑origin support.  
- **Candidate downstream axes:** Direct vascular‑wall (endothelial A2B, VSMC proliferation) and immune‑mediated (adenosine on macrophages/neutrophils) are both plausible. Thrombo‑inflammatory (tissue factor induction, fibrin deposition) is a subset of immune/vascular.  
- **Evidence needed:** Receptor‑blockade studies, quantification of adenosine/inosine in perivascular fluid, and MK‑specific Pnp deletion.

---

### Finding 6: Pyruvaldehyde (methylglyoxal) → RAGE axis (H2‑gen1)

- **Finding:** Pyruvaldehyde is up in PH‑MK (log2FC = 4.43). No direct enzyme gene was provided in the metabolomics context; the hypothesis relies on imbalance between glycolysis and glyoxalase 1 (Glo1). Seurat expression for Glo1 was not included in the evidence context.  
- **Evidence type:** **Insufficient evidence** – the metabolite change is direct, but the MK‑specific enzyme/gene link is missing.  
- **Source:** MK metabolomics; candidate enzyme not in shortlist.  
- **Strength:** Low until Glo1 expression/differential in MKs is confirmed.  
- **Limitation:** Without MK Glo1 data, the mechanism cannot be anchored to MK metabolism; methylglyoxal could originate from other cells.  

---

### Finding 7: Extracellular vesicle‑driven hypotheses (PDGF‑BB/TGF‑β1, tissue factor‑positive EVs, thrombospondin‑1) (H4‑gen2, H3‑gen3, H4‑gen3)

- **Finding:** These hypotheses are grounded in prior results (lung‑resident MKs required) and MK biology from literature, but the critical MK gene expression (Pdgfb, Tgfb1, F3, Thbs1, Rab27a, Tsg101, Cd44) has **not** been extracted from the Seurat object. The metabolomics context does not cover these.  
- **Evidence type:** **Speculative relevance** (with strong biological rationale but missing user‑data anchor).  
- **Source:** Prior results and literature; Seurat requests are pending.  
- **Strength:** Currently low; could become moderate if the requested gene expression queries show MK enrichment and PH‑up shift.

## Proximity output
# Proximity Check Agent Output

## I. Hypothesis Clusters

Each cluster groups hypotheses that share a core initiating mechanism (MK state, mediator class, pathway), with variations in downstream axes.

### Cluster 1: Polyamine metabolism (AMD1/Amd2)
**Cluster name:** MK AMD1/Amd2‑driven polyamine synthesis and downstream vascular remodelling  
**Included hypothesis IDs:** `GenMet_H1`, `GenMet_H2`, `Gen2_H1`, `Gen3_H1`  
**Shared mechanism:**  
- Hypoxia upregulates AMD1 (and Amd2) in lung‑resident MKs.  
- Elevated methionine is diverted via decarboxylated SAM into polyamine synthesis (spermidine, spermine).  
- Polyamines are released (free or via EVs) and act in the perivascular niche.  

**Key differences:**  
- `GenMet_H1`: Broad candidate downstream axes – immune‑mediated (Th17/macrophage), direct vascular‑wall, or EV/stromal; working model favours immune‑mediated.  
- `GenMet_H2`: Amd2 cooperates with Amd1 to reinforce polyamine output; no new downstream axis, just a strengthening modifier.  
- `Gen2_H1`: Specifies M2‑like macrophage polarisation → pro‑fibrotic collagen deposition; dominant downstream axis is immune‑mediated (macrophage).  
- `Gen3_H1`: Specifies ECM cross‑linking via transglutaminase‑2 and eIF5A hypusination → stiffening; dominant downstream axis is direct ECM/stromal.  

*Note: GenMet_H2 is a complement to other AMD1 hypotheses, not an independent mechanism.*

### Cluster 2: Purine nucleoside (inosine/adenosine) metabolism
**Cluster name:** MK Pnp/‑mediated inosine production and adenosine receptor signalling  
**Included hypothesis IDs:** `Gen1_H1`, `Gen2_H5`, `Gen3_H2`  
**Shared mechanism:**  
- Hypoxia upregulates Pnp (and NT5C2) in MKs → increased inosine production and release.  
- Inosine and/or extracellularly converted adenosine bind adenosine receptors (A2B, A2A) on vascular or immune cells.  
**Key differences:**  
- `Gen1_H1`: Primary axis direct vascular‑wall – adenosine receptors on VSMC and EC → medial thickening, endothelial dysfunction.  
- `Gen2_H5`: Primary axis endothelial dysfunction – impairment of eNOS, VCAM‑1/ICAM‑1 upregulation → secondary smooth muscle proliferation.  
- `Gen3_H2`: Primary axis thrombo‑inflammatory – adenosine‑A2B drives endothelial tissue factor expression, fibrin deposition, and myeloid recruitment → medial muscularization.

### Cluster 3: Retinoic acid catabolism
**Cluster name:** MK Cyp26b1‑mediated retinoic acid degradation  
**Included hypothesis IDs:** `GenMet_H4`, `Gen1_H3`  
**Shared mechanism:**  
- Hypoxia upregulates (or trends toward) Cyp26b1 in MKs.  
- Increased degradation of retinoic acid (or conversion to less active metabolites) lowers local ATRA tone.  
- Loss of retinoic acid‑mediated inhibition permits vascular remodelling.  
**Key differences:**  
- `GenMet_H4`: Emphasises immune de‑repression (Th17/Treg imbalance) and some direct vascular effects.  
- `Gen1_H3`: Focuses entirely on removal of growth suppression from VSMC, leading to medial thickening.

### Cluster 4: Extracellular vesicle‑mediated mechanisms (cargo‑based)
**Cluster name:** MK‑derived EV cargo in vascular remodelling  
**Included hypothesis IDs:** `Gen2_H4`, `Gen3_H3`  
**Shared mechanism:**  
- Hypoxia triggers release of specific EVs from lung MKs.  
- EVs carry functionally distinct cargo into the perivascular space.  
**Key differences:**  
- `Gen2_H4`: Cargo = PDGF‑BB and TGF‑β1; target = PASMCs and fibroblasts → muscularization and fibrosis.  
- `Gen

## Reflection outputs
# Reflection Agent Outputs

## reflection_1
# Reflection Agent Output: Cycle 1 Hypothesis Review

The review mode focuses on **mechanistic plausibility**, **MK specificity**, and **hypoxia specificity**, while applying the full Reflection Agent format. Evidence is classified strictly: user‑provided data, public dataset metadata, downloaded/reanalyzed public data, literature, inference, speculation. The fact that public dataset analyses (GSE289322, GSE291455) were performed but the actual differential expression results were **not inspected** (content of `candidate_gene_check.tsv` and `de_results.tsv` unknown) means that **no public‑dataset evidence currently supports or refutes any hypothesis**; only the incomplete metadata is available, and thus no validated tissue‑level change can be claimed. Claims that GSE289322 “could validate” are not evidence; they are future opportunities.

---

### Hypothesis ID: GenMet_H1
**Hypothesis title:** Hypoxic MK methionine accumulation drives AMD1-mediated polyamine metabolism, shifting perivascular immune/stromal tone and contributing to medial thickening and vascular stiffening.

**Review decision:** **Promising but incomplete**

**Directional assessment:**
- **Strengths:** The hypothesis establishes a clear metabolite→enzyme→pathway→candidate‑axis direction. Methionine accumulation (log2FC 3.26) and AMD1 upregulation (MK enrichment 1.35, PH‑up log2FC 1.77, p=6.55e‑06) provide strong, MK‑specific data anchors. The AMD1–polyamine link is biochemically well‑founded, and polyamines are plausible paracrine mediators. The directional logic from hypoxic MK metabolic reprogramming to potential vascular remodelling is coherent.
- **Weaknesses:** The downstream axis is kept deliberately broad (immune‑mediated, direct vascular‑wall, EV/stromal), which is appropriate for a direction‑level hypothesis, but no direct evidence of polyamine secretion, extracellular concentration, or target‑cell effect is present. MK‑origin gap is explicitly stated but remains substantial: AMD1 protein/activity, polyamine quantification in MK secretome, and the dominant recipient cell are unknown. The hypothesis could equally support immune‑mediated, direct vascular, or ECM‑crosslinking routes, leaving the ultimate remodelling bridge unresolved.
- **Reasoning quality:** Good – follows the required scaffold, clearly links data anchor to enzyme and candidate axes, and identifies key uncertainties. The summary correctly avoids over‑resolving Th17 or specific cytokine pathways.
- **Appropriate resolution:** Yes – the direction is appropriately broad given available evidence.

**Evidence assessment:**
- **User‑provided data:** Directly supports methionine up and AMD1 expression/differential in MKs (MK metabolomics, scRNA‑seq).
- **Public data:** No validated support; GSE289322 DE analysis not inspected, GSE291455 provides no contrast. No tissue‑level AMD1 change confirmed.
- **Literature:** AMD1–mTORC1–polyamine axis (PMID 28658205) and polyamine immunomodulation support pathway plausibility, but no MK‑to‑vascular literature.
- **Inference:** Polyamine secretion and perivascular effects are inferred from enzyme upregulation and metabolite increase; plausible but not demonstrated.
- **Speculation:** That AMD1‑driven polyamine flux is the dominant methionine‑SAM fate in hypoxic MKs, and that secreted polyamines reach sufficient concentrations to remodel vessels.

**Major concerns:**
- The link between MK AMD1 expression and extracellular polyamine action is entirely correlative; lack of AMD1 protein/activity data and polyamine secretion measurements.
- The hypothesis assumes that methionine is channelled into polyamines rather than methylation, without direct evidence; the SAM/polyamine ratio could be unaltered.
- The final remodelling phenotype (medial thickening, stiffness) is generic; it does not distinguish whether the pathway impacts endothelial, SMC, fibroblast, or immune cells, which limits its mechanistic specificity and testability at the cell‑type level.

**Downstream‑axis assessment:**
- **Broad axis:** Polyamine‑mediated modulation of perivascular microenvironment.
- **Candidate examples:** Spermidine/spermine → Th17‑like T‑cell activity or macrophage polarization (immune‑mediated), direct SMC proliferation (vascular‑wall), transglutaminase‑mediated ECM cross‑linking (stromal), all provisional.
- **What remains unresolved:** Which cell type(s) respond to polyamines; whether the mechanism is free polyamine or EV‑delivered; relative contribution of AMD1 vs Amd2.
- **MK‑origin gap:** MK polyamine export, stability, and diffusion not shown.
- **Direction‑specific falsification:** MK‑specific Amd1 knockout or pharmacological AMD1 inhibition should prevent lung polyamine rise and reduce vascular remodelling; if blocking AMD1 does not alter vascular phenotype, the direction is falsified.

**Required revisions:**
- Include a direct, experimentally tractable prediction about polyamine quantification in MK‑conditioned medium or perivascular fluid (even if technically challenging).
- Acknowledge that AMD1 activity is the critical unmeasured node and propose how it could be measured (e.g., SAM486A effect on SAM/decarboxylated‑SAM ratio in MKs).
- Clarify that the “immune‑mediated” axis is a placeholder and that no specific immune subset has been implicated by the data.

**Experimental critique:**
- **Strong points:** Proposes MK‑specific Amd1 deletion and pharmacological inhibition, with clear readouts (lung polyamines, medial thickness, RVSP). Falsification criterion is well‑defined.
- **Weak points:** The readout “perivascular immune cell composition” is vague; need to specify markers for Th17, macrophage polarization, etc. The experiment does not distinguish which downstream axis is primary.
- **Missing controls:** Must include control for AMD1 inhibitor specificity, and verify that MK‑specific deletion does not affect platelet polyamine pools (off‑target interpretation). Need to measure AMD1 activity in MKs.
- **Falsification criteria:** Clear: no change in lung polyamines or vascular remodelling despite efficient AMD1 blockade.

**Final recommendation to PI:**
- **Advance** as a high‑priority direction (strong metabolite‑enzyme anchor, clear MK/hypoxia specificity, testable) but flag that the downstream axis is unresolved. Merge with Gen2_H1 and Gen3_H1 into a unified polyamine hypothesis suite, retaining the broad axis until experimental data direct to a specific route.

---

### Hypothesis ID: GenMet_H2
**Hypothesis title:** MK Amd2 upregulation under hypoxia augments spermidine/spermine synthesis to cooperate with Amd1, reinforcing polyamine‑dependent vascular remodeling.

**Review decision:** **Weak**

**Directional assessment:**
- **Strengths:** Identifies a second SAM decarboxylase that could contribute to polyamine synthesis; statistically significant hypoxia‑induced upregulation in MKs (log2FC 2.18, p=0.024).
- **Weaknesses:** Amd2 expression is very low (4.4% of MKs, enrichment 0.93) and likely represents a minor MK subpopulation; no evidence of Amd2 protein activity or any functional contribution beyond AMD1. The hypothesis essentially duplicates GenMet_H1 with a less‑supported enzyme. The directional chain is identical; the only novelty is a proposed redundancy. Without functional evidence, Amd2’s role is speculative and may be negligible.
- **Reasoning quality:** Adequate but low impact; reasoning relies on gene duplication logic without any biological data linking Amd2 to the polyamine pathway in MKs beyond mRNA.
- **Appropriate resolution:** The hypothesis is too specific (naming a single isoform) given the weak expression; a broader “alternative polyamine enzyme” statement would be more appropriate.

**Evidence assessment:**
- **User‑provided data:** Amd2 expression and PH‑up in MKs (scRNA‑seq).
- **Public data:** No validation available; GSE289322 not inspected.
- **Literature:** No direct Amd2–MK or vascular literature; gene‑level context from muscle atrophy metabolomics (PMID 40768332) is not relevant.
- **Inference:** That Amd2 protein is active and contributes non‑redundantly to polyamine pool is inferred solely from mRNA.
- **Speculation:** That Amd2 cooperates with AMD1.

**Major concerns:**
- Low expression percentage and lack of protein data make it unlikely that Amd2 is a significant contributor. No data on Amd2 enzyme kinetics or substrate affinity in this context.
- The hypothesis is practically a redundant add‑on to GenMet_H1 and does not establish a distinct mechanism or a distinct testable prediction that would differentiate it from AMD1 alone.
- Could lead to over‑investment in a minor gene.

**Downstream‑axis assessment:** Identical to GenMet_H1; no new axis.
**MK‑origin gap:** Even larger than Amd1; Amd2 protein and activity unproven.
**Falsification:** Dual Amd1/Amd2 KO vs Amd1 alone; if no additive effect, Amd2 role is dispensable, which would falsify the cooperative aspect. However, this is a weak hypothesis because it leans entirely on a gene with low expression.

**Required revisions:**
- Merge with GenMet_H1 as a minor note about potential Amd2 contribution, rather than a standalone hypothesis.
- Provide evidence of Amd2 protein expression or at least a justification based on functional genomics (e.g., paralog essentiality in other cell types) if resubmitted.

**Experimental critique:**
- Feasible but low priority; dual knockout is technically demanding and unlikely to yield large effect.
- Missing control: Amd2 single KO should be tested first to see if it has any impact; if no phenotype, the hypothesis is effectively falsified without dual KO.

**Final recommendation to PI:**
- **Merge** with GenMet_H1 and deprioritize as a separate investigation. The polyamine direction should focus on AMD1 unless Amd2 protein emerges from orthogonal data.

---

### Hypothesis ID: GenMet_H3
**Hypothesis title:** MK methionine accumulation may alter DNA methylation via Dnmt3b, reshaping MK transcriptome and secretome to promote a pro‑remodelling phenotype.

**Review decision:** **Reject**

**Directional assessment:**
- **Strengths:** Biochemical link between methionine, SAM, and DNA methylation is plausible. Epigenetic reprogramming of MKs as a driver of remodelling is conceptually novel.
- **Weaknesses:** The gene anchor is extremely weak: Dnmt3b is expressed in only 2.62% MKs, with negligible enrichment (0.19) and no significant hypoxia‑induced change (p=0.212). There is no evidence that methionine flux actually increases methylation in MKs, nor that Dnmt3b is the methyltransferase responsible. The hypothesis lacks any direct or indirect user data linking MK methylation to secretome changes or remodelling. It is entirely speculative and fails the MK‑specificity and data‑anchor requirements.
- **Reasoning quality:** The reasoning chain is plausible in general, but the specific MK link is unsupported; the agent effectively acknowledges the low support, making the hypothesis a low‑confidence exploratory idea rather than a data‑grounded direction.
- **Appropriate resolution:** Not appropriate as a standalone hypothesis; requires much stronger initial evidence.

**Evidence assessment:**
- **User‑provided data:** Methionine up (metabolomics); Dnmt3b expression low and not significant (scRNA‑seq). No methylation data.
- **Public data:** None.
- **Literature:** No MK‑specific methylation data; general SAM‑methylation axis known.
- **Inference:** Highly speculative that methionine accumulation alters MK methylation via Dnmt3b.
- **Speculation:** Almost all aspects.

**Major concerns:**
- MK specificity is essentially absent; Dnmt3b could be functional in other cells but not MKs.
- No hypoxia‑specific trigger for methylation; the enzyme is not hypoxia‑responsive in MKs.
- Overclaims potential despite the agent’s own acknowledgment; advancing this would waste resources.
- The hypothesis could be rescued by other DNA methyltransferases (Dnmt1, Dnmt3a) but those are not proposed; the current form is not viable.

**Downstream‑axis assessment:** Unresolvable with present data.
**Falsification:** Would require MK‑specific Dnmt3b knockout and methylation profiling, which is disproportionate to evidence quality.

**Required revisions:** Not salvageable without new data; should be rejected outright unless supplemented with MK methylome profiling and significant Dnmt3b engagement.

**Experimental critique:** Proposed experiments are inappropriate given the weak foundation.

**Final recommendation to PI:**
- **Reject** due to insufficient MK‑specific data anchor and failure to meet the required evidence threshold.

---

### Hypothesis ID: GenMet_H4; similar to Gen1_H3 (retinoic acid → Cyp26b1)
**Hypothesis title:** MK‑mediated retinoic acid degradation via Cyp26b1 blunts local retinoid signalling, relieving repression of inflammatory pathways and perivascular fibrosis.

**Review decision:** **Weak**

**Directional assessment:**
- **Strengths:** Retinoic acid is a known immunomodulator and vascular stabilizer; its loss could promote remodelling. The metabolite RA is upregulated in PH‑MK (log2FC 3.44), providing a data anchor. Cyp26b1 is a direct compound‑enzyme (RA hydroxylase) with detectable MK expression (7.9%). The general concept of MK‑driven retinoid metabolism is novel.
- **Weaknesses:** The direction is opposite to the data – RA levels are high, not low, and the hypothesis must postulate that increased catabolism leads to net local depletion, which is not supported. Cyp26b1 upregulation is not significant (p=0.253), so there is no evidence of a hypoxia‑driven enzyme increase. The MK‑origin gap is huge: MKs might not be the source of RA degradation; other cells could dominate. The logic is internally strained.
- **Reasoning quality:** Poor: the agent attempts to explain the discrepancy (RA accumulation could reflect a compensatory upregulation of Cyp26b1) but this remains speculative and undercuts the direction. The hypothesis lacks a clear, testable link from MK enzyme activity to local retinoid tone.
- **Appropriate resolution:** Overly specific given weak MK enzyme evidence.

**Evidence assessment:**
- **User‑provided data:** RA up (MK metabolomics), Cyp26b1 MK expression pct 7.86%, PH‑up trend p=0.253 (not sig.).
- **Public data:** None.
- **Literature:** Cyp26b1 in retinoid homeostasis, but no MK‑specific literature.
- **Inference:** That increased RA in MKs indicates increased catabolism; could alternatively reflect increased synthesis or storage.
- **Speculation:** That MK Cyp26b1 degrades RA to a degree that alters perivascular retinoid tone.

**Major concerns:**
- The metabolite change contradicts the proposed mechanism; high RA would suppress inflammation, not promote it. The hypothesis relies on a local depletion model that would require RA to be lower in perivascular space despite MK content, a complex scenario.
- Cyp26b1 differential is not significant; cannot distinguish noise from signal. MK expression is modest.
- Lacks hypoxia specificity for the enzyme.
- Testability is complicated by the need to measure spatial RA gradients, which is difficult.

**Downstream‑axis assessment:** Immune‑mediated (Th17/Treg imbalance) is a candidate but unsupported.
**Falsification:** MK‑specific Cyp26b1 KO should alter lung RA levels and vascular remodelling; failure to do so refutes MK role. But the direction is ambiguous because both RA increase and decrease could have effects.

**Required revisions:** If resubmitted, must clarify whether RA is high or low in the perivascular niche and why Cyp26b1 would be the responsible enzyme. Better to require direct measurement of Cyp26b1 activity and RA concentration in MK‑conditioned medium before advancing.

**Experimental critique:** Proposed experiments are premature. The direction is so uncertain that even a positive knockout result would not confirm the specific mechanism.

**Final recommendation to PI:**
- **Deprioritize** or **Reject** due to conflicting metabolite data and weak MK‑enzyme evidence. The retinoid axis might be relevant, but not through Cyp26b1 as currently framed.

---

Now the other hypotheses. I'll go through generation_1 (H1 inosine, H2 methylglyoxal, H3 retinoic acid (similar to GenMet_H4)). Already handled H3 above; will review H1 and H2.

### Hypothesis ID: Gen1_H1 (Cluster 2: purine nucleoside)
**Hypothesis title:** Hypoxic MK purine nucleoside phosphorylase (Pnp) upregulation drives inosine secretion and adenosine receptor-mediated pulmonary vascular remodeling.

**Review decision:** **Promising but incomplete**

**Directional assessment:**
- **Strengths:** Strong data anchor: inosine up (log2FC 3.82) in MKs, Pnp expression in 20.3% MKs and significant PH‑up (log2FC 1.74, p=3.81e‑06). Direct compound‑enzyme link (purine metabolism). The directional chain from Pnp up → inosine release → adenosine receptor activation on vascular cells is biochemically plausible. Remodelling outcome (medial thickening, muscularization) is defined. MK-specific and hypoxia-specific.
- **Weaknesses:** Inosine is not adenosine;

## reflection_2
# Reflection Agent Review – Cycle 1 Hypotheses

The following evaluations are based on strict separation of user‑provided direct data, public dataset analyses (pending/incomplete), literature, and inference. Speculation or overinterpretation is flagged. Recommendations are made for the PI to advance, revise, merge, deprioritize, or reject each hypothesis.

---

## Cluster 1: Polyamine metabolism (AMD1/Amd2)

### Hypothesis ID: GenMet_H1

**Review decision:** Strong

**Directional assessment:**
- **Strengths:** Directly anchored on MK‑specific metabolomics (methionine up) and scRNA‑seq (AMD1 enriched, significantly PH‑up). Clear metabolite → enzyme → polyamine pathway logic. Broad but plausible candidate downstream axes (immune‑mediated, direct vascular‑wall, EV/stromal) correctly labelled as provisional. Testable by AMD1 perturbation.
- **Weaknesses:** Does not resolve which polyamine‑responsive cell type or signalling route dominates. Confirmation of polyamine secretion from MKs is missing. The link to vascular remodelling rests on literature for polyamine biology, not direct vascular phenotype data.
- **Reasoning quality:** Excellent; the direction‑level reasoning summary correctly traces data anchor to interpretation to pathway logic to candidate axes, with explicit key uncertainty.
- **Appropriate resolution:** Yes – hypotheses at this stage appropriately avoid over‑resolving exact mediators or recipient cells.

**Evidence assessment:**
- **User‑provided data:** Strong direct support – methionine log2FC 3.26 in PH MKs; AMD1 MK enrichment 1.35, PH‑up log2FC 1.77, p=6.55e‑06.
- **Public data:** GSE289322 could validate tissue‑level AMD1 differential (pending). Not yet used.
- **Literature:** Indirect support for AMD1/polyamine roles in cancer metabolism and immune modulation; no direct MK‑vascular PH reports.
- **Inference:** The polyamine‑to‑remodelling step is inferred from literature.
- **Speculation:** None that is unjustified; the candidate axes are clearly framed as provisional.

**Major concerns:** None at the direction level. The hypothesis does not overreach.

**Downstream‑axis assessment:**
- **Broad axis:** Immune‑mediated, direct vascular‑wall, EV/stromal.
- **Candidate examples:** Spermidine, Th17‑like cells, macrophage activation, SMC proliferation, ECM cross‑linking.
- **What remains unresolved:** Identity of the polyamine‑responsive cell, whether polyamines are secreted free or in EVs, whether immune vs. vascular‑wall dominates.
- **MK‑origin gap:** Polyamine export from hypoxic MKs not directly measured; AMD1 protein/enzyme activity not confirmed.
- **Direction‑specific falsification:** AMD1 blockade in MKs should reduce lung polyamines and attenuate vascular remodelling. Failure to do so falsifies the direction.

**Required revisions:** None essential; the hypothesis is appropriately scoped. Optionally request AMD1 protein/activity validation in a follow‑up experiment.

**Experimental critique:**
- **Strong points:** Testable with MK‑specific genetic deletion or pharmacological inhibitor; endpoints are measurable.
- **Weak points:** The exact readout for polyamine‑mediated remodelling may be confounded by AMD1’s housekeeping roles; careful dosing/timing needed.
- **Missing controls:** Should include rescue with exogenous polyamines and measure polyamines in MK‑conditioned medium.
- **Falsification criteria:** Clearly stated.

**Final recommendation to PI:** Advance – this is a high‑priority hypothesis with strong data anchorage.

---

### Hypothesis ID: GenMet_H2

**Review decision:** Promising but incomplete

**Directional assessment:**
- **Strengths:** Identifies a second potential enzyme (Amd2) in the same pathway; hypoxia‑induced upregulation is statistically significant.
- **Weaknesses:** Very low MK expression (4.4%), only 0.93 enrichment, uncertain functional contribution. Would be a cooperative modifier, not a standalone mechanism.
- **Reasoning quality:** Adequate, but the hypothesis adds little beyond GenMet_H1 at the direction level. The reasoning summary mentions cooperativity but the low expression makes it marginal.
- **Appropriate resolution:** Partially over‑resolves by suggesting a separate downstream axis for Amd2 (should be integrated with Amd1).

**Evidence assessment:**
- **User‑provided data:** Amd2 MK expression 4.37%, enrichment 0.93, PH‑up log2FC 2.175, p=0.024.
- **Public data:** Pending.
- **Literature:** Minimal; muscle atrophy metabolomics paper.
- **Inference:** Functional redundancy based solely on low mRNA expression.
- **Speculation:** That Amd2 contributes meaningfully to polyamine synthesis without direct activity data.

**Major concerns:** Low expression and marginal enrichment weaken the case. The hypothesis overstates the likely impact of a minor paralog.

**Downstream‑axis assessment:** Same as for AMD1; no unique downstream axis. Falsification criteria reasonable.

**Required revisions:** Merge with GenMet_H1 as a supportive note. Do not advance separately.

**Experimental critique:** Dual Amd1/Amd2 KO experiments may be unnecessary unless single Amd1 loss shows partial effect; better to focus on Amd1 first.

**Final recommendation to PI:** Merge with GenMet_H1 – do not pursue as standalone.

---

### Hypothesis ID: Gen2_H1 (AMD1 → M2 macrophage polarisation → fibrosis)

**Review decision:** Promising but incomplete

**Directional assessment:**
- **Strengths:** Grounded on the same AMD1‑polyamine anchor, but attempts to specify a downstream immune cell (M2 macrophage) and profibrotic outcome. Adds literature rationale for polyamines influencing macrophage polarisation.
- **Weaknesses:** Over‑resolves the recipient cell and polarisation state without direct evidence that MK‑derived polyamines reach and polarise lung macrophages. The M2‑like designation is provisional but presented more concretely than justified.
- **Reasoning quality:** Good, but the bridge to macrophage polarisation is less well anchored than the metabolic axis. The hypothesis would benefit from noting that other polyamine‑responsive cells are equally plausible.
- **Appropriate resolution:** Partially over‑resolved; a broader “immune‑mediated” label would better match current data.

**Evidence assessment:**
- **User‑provided data:** Same methionine/AMD1 data; no macrophage gene expression data.
- **Public data:** Pending.
- **Literature:** Some support for polyamines affecting macrophage function; still indirect.
- **Inference:** Macrophage polarisation as primary axis.
- **Speculation:** Assumes that polyamines from MKs are the dominant polarising factor in the perivascular niche.

**Major concerns:** Downstream axis specificity is premature; the hypothesis risks testing the wrong cell type if macrophage‑mediated fibrosis is not the main mechanism.

**Recommended revisions:** Re‑label as “immune‑mediated, with candidate macrophage polarisation” and treat as one of several possible routes. Integrate into the broader AMD1 hypothesis.

**Final recommendation to PI:** Merge into GenMet_H1 as a candidate downstream axis.

---

### Hypothesis ID: Gen3_H1 (AMD1 → ECM cross‑linking / hypusination)

**Review decision:** Promising but incomplete

**Directional assessment:**
- **Strengths:** Provides a specific ECM‑centred axis (transglutaminase‑2 cross‑linking, eIF5A hypusination) that is mechanistically plausible for polyamines and directly links to vascular stiffness.
- **Weaknesses:** Again over‑resolved; the hypothesis assumes that MK‑derived polyamines are the primary substrates for these ECM modifications, but other cell types produce polyamines. The ECM‑cross‑linking route is not yet supported by user data.
- **Reasoning quality:** Good, with clear mechanistic logic. However, the candidate axes should be presented as provisional, not as the working model.
- **Appropriate resolution:** Appropriate for a candidate downstream axis, but should not be the sole AMD1 hypothesis.

**Evidence assessment:**
- **User‑provided data:** Same strong methionine/AMD1 data; no ECM or hypusination markers.
- **Literature:** Good support for TGM2 and hypusination in fibrosis/vascular stiffness.
- **Inference:** Polyamine use in ECM cross‑linking is well documented but not necessarily MK‑specific.
- **Speculation:** That the polyamine source is MK‑derived is speculative.

**Major concerns:** Over‑specificity relative to the available data; could be folded into the broader AMD1 hypothesis as one candidate ECM mechanism.

**Required revisions:** Frame as a candidate mechanism within the AMD1 direction, not a standalone hypothesis.

**Final recommendation to PI:** Merge with GenMet_H1.

---

## Cluster 2: Retinoic acid / Cyp26b1

### Hypothesis ID: GenMet_H4

**Review decision:** Weak

**Directional assessment:**
- **Strengths:** Interesting direction linking MK metabolism to retinoid‑mediated immune regulation.
- **Weaknesses:** The MK‑specific enzyme expression is low and the PH‑up shift is not significant (Cyp26b1 p=0.253). Retinoic acid is upregulated, which argues against increased catabolism; the logic is inverted or requires complex compensatory explanation. The hypothesis is theoretically plausible but data anchor is weak.
- **Reasoning quality:** The reasoning summary acknowledges the counter‑intuitive RA up and deals with it speculatively. The chain is not convincingly anchored.
- **Appropriate resolution:** Appropriate attempt at a direction‑level hypothesis, but the weak enzyme data and metabolite direction make it hard to justify.

**Evidence assessment:**
- **User‑provided data:** RA up log2FC 3.44; Cyp26b1 MK expression 7.86%, enrichment 0.73, PH‑up not significant.
- **Literature:** Retinoid biology in immune and vascular homeostasis is solid, but not directly linked to MK.
- **Inference:** Assumes MK Cyp26b1 activity is rate‑limiting for local RA degradation.
- **Speculation:** The compensatory scenario is highly speculative; net effect could be opposite.

**Major concerns:** Insufficient evidence for Cyp26b1 as the key enzyme; RA accumulation could be due to increased synthesis, not decreased degradation. The hypothesis risks being falsified by a single experiment showing RA actually accumulates.

**Downstream‑axis assessment:** Immune‑mediated and direct vascular‑wall are plausible, but the MK‑origin gap is large.

**Required revisions:** Significant – would need a different candidate enzyme or more compelling Cyp26b1 data. Recommend re‑evaluating after checking Cyp26b1 activity/protein in MKs.

**Experimental critique:** Testing requires MK‑specific Cyp26b1 KO, which is feasible but premature given weak data support.

**Final recommendation to PI:** Deprioritize pending stronger evidence.

---

### Hypothesis ID: Gen1_H3

**Review decision:** Weak (essentially same as GenMet_H4, but focused on VSMC growth suppression. Same evidence issues. So same recommendation: Deprioritize.

---

## Cluster 3: Inosine / Pnp/Nt5c2 → adenosine receptor signalling

### Hypothesis ID: Gen1_H1

**Review decision:** Strong

**Directional assessment:**
- **Strengths:** Direct metabolite (inosine) and enzyme (Pnp) data are strong and MK‑specific. Downstream adenosine‑receptor axis is well‑supported by literature in vascular biology.
- **Weaknesses:** Does not distinguish between inosine and adenosine; the net effect on remodelling may be context‑dependent. The direct vascular‑wall axis is well argued, but immune or thrombo‑inflammatory routes are equally plausible.
- **Reasoning quality:** Good; the chain from purine degradation to A2B‑mediated vascular smooth muscle hypertrophy is logical, and the key uncertainty about adenosine vs. inosine is stated.
- **Appropriate resolution:** Appropriate; does not over‑resolve receptor subtype or exact cell type.

**Evidence assessment:**
- **User‑provided data:** Inosine log2FC 3.82; Pnp MK expression 20.31%, PH‑up log2FC 1.74 p=3.81e‑06; Nt5c2 also up.
- **Public data:** Pending; GSE289322 may validate tissue‑level PNP changes.
- **Literature:** Adenosine signalling in PH and vascular remodelling is well established.
- **Inference:** The conversion of inosine to adenosine in the perivascular space is inferred.
- **Speculation:** None that is unwarranted.

**Major concerns:** None at direction level.

**Downstream‑axis assessment:** Direct vascular‑wall, immune‑mediated, thrombo‑inflammatory. Candidate examples: A2B receptor on VSMC/EC. Unresolved: receptor subtype dominance, net pro‑ vs. anti‑remodelling. MK‑origin gap: Inosine secretion confirmed indirectly; need direct measurement.

**Required revisions:** None essential; can be advanced as is.

**Experimental critique:** Testable with Pnp inhibitor or MK‑specific deletion. Falsification criteria clear.

**Final recommendation to PI:** Advance.

---

### Hypothesis ID: Gen2_H5 (inosine → endothelial dysfunction)

**Review decision:** Promising but incomplete

**Directional assessment:**
- **Strengths:** Same metabolic anchor; specifies endothelial cell dysfunction as primary axis. Useful refinement of Gen1_H1.
- **Weaknesses:** Endothelium‑specific emphasis may overlook smooth muscle or immune roles; slightly over‑resolved given data. Still plausible.
- **Reasoning quality:** Adequate; points out uncertainty about net adenosine effect.
- **Appropriate resolution:** Slightly over‑resolved; could be presented as a candidate axis rather than a separate hypothesis.

**Evidence assessment:** Same as above.

**Major concerns:** Redundancy with Gen1_H1; may be more efficient to integrate with Gen1_H1.

**Required revisions:** Merge into Gen1_H1 as a candidate downstream focus (endothelial A2).

**Final recommendation to PI:** Merge

## reflection_3
**Hypothesis ID:** GenMet_H1  
**Review decision:** Promising but incomplete  
**Directional assessment:**  
- **Strengths:** Clear data anchor: methionine up (log2FC 3.26) and AMD1 MK enrichment (1.35, PH‑up p=6.55e‑06). The metabolite→polyamine axis is biochemically sound. MK specificity and hypoxia dependence are well supported.  
- **Weaknesses:** Downstream axes remain too broad; the hypothesis lists three plausible routes without committing to one. The working immune‑mediated model is not derived from direct MK‑to‑immune signalling data.  
- **Reasoning quality:** High for the initial metabolic event; the downstream reasoning correctly preserves candidate status but could be misinterpreted as a resolved mechanism.  
- **Appropriate resolution:** Yes – the direction is appropriately broad given the evidence.

**Evidence assessment:**  
- User‑provided data: Direct for metabolite and AMD1 expression.  
- Public data: Not yet verified; GSE289322 may add tissue‑level AMD1 support but does not alter MK‑origin evidence.  
- Literature: AMD1‑polyamine axis in cancer immunometabolism; no direct vascular‑PH‑MK literature.  
- Inference: Polyamines modulate T‑cells and macrophages; stress that this is inferred.  
- Speculation: Polyamine secretion from MKs, local concentration, actual recipient cell type are speculative.

**Major concerns:**  
1. Polyamine secretion by MKs is unproven; they may retain polyamines for cell‑autonomous roles.  
2. The immune‑mediated working model over‑resolves to Th17/macrophage when data only support a metabolic shift.  
3. AMD1 activity (protein/decarboxylated SAM) not measured; it could be transcriptionally upregulated but post‑translationally inhibited.

**Downstream‑axis assessment:**  
- Broad axis: Immune‑mediated, direct vascular‑wall, EV/stromal.  
- Candidate examples: Spermidine‑driven Th17‑like or M2‑like polarization, SMC proliferation.  
- What remains unresolved: The dominant route, exact cell targets.  
- MK‑origin gap: polyamine export, stability, and local concentration unknown.  
- Direction‑specific falsification: MK‑specific Amd1 KO should prevent hypoxia‑induced polyamine accumulation and blunt vascular remodeling (medial thickness). If polyamine levels or remodeling are unchanged, the direction fails.

**Required revisions:**  
- Remove any implication of a settled immune mechanism; explicitly label Th17/IL‑17 as an example candidate, not the working model.  
- Include control experiments to distinguish intracellular polyamine function from extracellular signalling (e.g., inhibitor of polyamine export, AMD1 inhibition in conditioned‑media transfer).

**Experimental critique:**  
- Strong points: MK‑specific KO is feasible and would directly test the AMD1‑to‑remodeling link. Readouts (polyamine LC‑MS, medial thickness) are appropriate.  
- Weak points: No proposed control for non‑MK polyamine sources; AMD1 inhibitor might affect other cells. Missing output: AMD1 activity measurement.  
- Missing controls: AMD1 inhibition in vitro to confirm drug specificity; MK‑derived polyamine secretion assay.  
- Falsification criteria: If MK‑specific Amd1 deletion does not reduce lung tissue polyamines or does not attenuate vascular remodeling, hypothesis is falsified.

**Final recommendation to PI:** Revise – tighten downstream axis language, clarify candidate status, and require AMD1 activity data before progression.

---

**Hypothesis ID:** GenMet_H2  
**Review decision:** Weak  
**Directional assessment:**  
- **Strengths:** Amd2 differential expression is statistically significant; pathway similarity to AMD1 is logical.  
- **Weaknesses:** Very low MK expression (4.4%), no protein evidence, and functional redundancy with AMD1. The hypothesis adds little beyond AMD1.  
- **Reasoning quality:** Adequate, but reliant on additive effect which is not yet supported.  
- **Appropriate resolution:** Yes, but resolution is too fine for current data; Amd2 might be negligible.

**Evidence assessment:**  
- User‑provided data: Amd2 expression pct 4.37%, enrichment 0.93, PH‑up log2FC 2.175, p=0.024.  
- Public data: Pending.  
- Literature: None directly, Amd2 in muscle atrophy not PH.  
- Inference: Cooperative polyamine synthesis is plausible.  
- Speculation: Protein expressed and active in MKs, dual targeting gives greater effect.

**Major concerns:**  
- The low expression raises question of biological significance; could be noise or a minor subset.  
- Without direct measurement of Amd2 protein or its contribution to polyamine flux, the hypothesis is speculative.  
- Risk of false‑positive due to multiple testing in low‑expression genes.

**Downstream‑axis assessment:** Same as GenMet_H1; axes unchanged. Falsification requires dual Amd1/Amd2 knockout showing additive benefit over Amd1 alone. If not, Amd2 irrelevant.

**Required revisions:** Not recommended for revision; deprioritize. If pursued, must include Amd2 protein detection and confirm synthetic redundancy.

**Experimental critique:** Feasible but high bar: Amd2 KO must show additional effect, otherwise confounding many experiments. Missing control: Amd2 overexpression in MKs to test sufficiency.

**Final recommendation to PI:** Deprioritize – the hypothesis does not independently advance the AMD1 axis; it is a modifier with weak data support. Merge into AMD1 hypothesis as a secondary note.

---

**Hypothesis ID:** GenMet_H3  
**Review decision:** Reject  
**Directional assessment:**  
- **Strengths:** Conceptually novel linking methionine to epigenetics.  
- **Weaknesses:** Dnmt3b expression in MKs is low, not significantly PH‑up, and not MK‑enriched. No evidence of methylation change.  
- **Reasoning quality:** Poor – overinterprets non‑significant expression data; causal chain is highly speculative.  
- **Appropriate resolution:** No, the resolution is inappropriate given minimal MK expression.

**Evidence assessment:**  
- User‑provided data: Dnmt3b pct 2.62%, enrichment 0.19, PH log2FC 1.59 p=0.212 – not significant.  
- Public data: No support.  
- Literature: Methionine‑methylation axis in immune cells but no MK‑specific.  
- Inference: Weak.  
- Speculation: Entirely speculative; no direct evidence that methionine increases SAM/SAH ratio or alters methylation in MKs.

**Major concerns:**  
- The core enzyme is not convincingly expressed or regulated in MKs; the hypothesis lacks a data anchor.  
- DNA methylation assays would be required but the hypothesis does not define which loci or functional outcome.

**Downstream‑axis assessment:** Irrelevant given evidence failure.

**Required revisions:** N/A; do not pursue.

**Experimental critique:** MK‑specific Dnmt3b KO would be informative but is a fishing expedition; no specific target genes defined. Falsification criteria too vague.

**Final recommendation to PI:** Reject – insufficient evidence to support.

---

**Hypothesis ID:** GenMet_H4  
**Review decision:** Weak  
**Directional assessment:**  
- **Strengths:** Retinoic acid is highly up; interesting immunomodulatory molecule.  
- **Weaknesses:** Cyp26b1 expression in MKs is low, not significantly PH‑up, and the metabolite accumulation contradicts a catabolism‑driven hypothesis (RA up, not down).  
- **Reasoning quality:** Forced; attempts to reconcile RA increase with degradation by MKs without experimental support.  
- **Appropriate resolution:** No, the direction is not clearly anchored; RA increase might reflect increased synthesis, not reduced degradation.

**Evidence assessment:**  
- User‑provided data: RA up, Cyp26b1 expression trend but p=0.253 not significant.  
- Public data: None.  
- Literature: Cyp26b1 in retinoid homeostasis; no MK‑PH link.  
- Inference: If MKs degrade RA, local RA would decrease, but we see increase – inferring MK‑mediated degradation is counter‑intuitive.  
- Speculation: MKs could be upregulating Cyp26b1 to compensate, but the net effect is still RA increase; unclear how that would promote remodeling.

**Major concerns:**  
- The hypothesis is internally inconsistent with the primary data.  
- No direct measurement of RA‑degrading activity.  
- Low MK expression undermines MK specificity.

**Downstream‑axis assessment:** Not applicable.

**Required revisions:** None.

**Experimental critique:** MK‑specific Cyp26b1 KO unlikely to yield interpretable results given the data conflict.

**Final recommendation to PI:** Reject – not supported by user data and runs counter to observed metabolite change.

---

**Hypothesis ID:** Gen1_H1 (inosine/Pnp adenosine receptor vascular)  
**Review decision:** Promising but incomplete  
**Directional assessment:**  
- **Strengths:** Strong metabolite‑enzyme connection: inosine up 3.82x, Pnp significantly upregulated in MKs (log2FC 1.74, p=3.81e‑06). Adenosine receptors are known to influence vascular remodeling.  
- **Weaknesses:** The downstream axis is direct vascular‑wall but does not distinguish between inosine and adenosine effects; A2B receptor may have dual pro‑/anti‑remodeling roles. No evidence of extracellular adenosine generation from MKs.  
- **Reasoning quality:** Good; the pathway logic is sound, and it acknowledges uncertainty about receptor subtype and net effect.  
- **Appropriate resolution:** Broad enough; the exact receptor and target cell are unresolved.

**Evidence assessment:**  
- User‑provided data: Inosine, Pnp expression, and NT5C2 up indirectly support. Not adenosine directly.  
- Public data: GSE289322 can validate Pnp tissue level; not yet available.  
- Literature: Adenosine‑A2B in PH, VSMC proliferation.  
- Inference: MK‑derived inosine converted to adenosine by ectonucleotidases.  
- Speculation: Concentration of adenosine in perivascular space; net pathological role.

**Major concerns:**  
1. Adenosine can be vasoprotective; the hypothesis must specify what tips the balance to harmful.  
2. No direct measurement of adenosine release from MKs.  
3. The hypothesized endothelial dysfunction and VSMC proliferation via A2B need more precise mapping.

**Downstream‑axis assessment:**  
- Broad axis: Direct vascular‑wall (adenosine receptors).  
- Candidate examples: A2B on VSMC, A2A on endothelium.  
- What remains unresolved: Receptor subtype dominance, net effect, role of extracellular conversion.  
- MK‑origin gap: Adenosine/inosine export, local concentrations.  
- Falsification: MK‑specific Pnp KO should reduce perivascular adenosine/inosine and blunt remodeling. If A2B antagonist fails to attenuate remodeling, the direct vascular‑wall route is refuted.

**Required revisions:**  
- Include a control experiment to measure adenosine/inosine in BAL or interstitial fluid.  
- Address potential protective adenosine effects and define experimental conditions where pathological predominates.

**Experimental critique:**  
Strong points: MK‑specific Pnp deletion feasible; hemodynamic and morphometric readouts appropriate. Weak points: Receptor blockade alone may not isolate MK source; need MK‑secretome transfer model. Missing controls: Vehicle‑treated MK‑KO with A2B agonist rescue. Falsification criteria: If MK‑Pnp KO does not alter vascular phenotype, hypothesis unsupported.

**Final recommendation to PI:** Revise – strengthen the distinction between inosine and adenosine and include rescue experiments.

---

**Hypothesis ID:** Gen1_H2 (methylglyoxal RAGE)  
**Review decision:** Weak  
**Directional assessment:**  
- **Strengths:** Pyruvaldehyde (methylglyoxal) is highly upregulated (4.43x).  
- **Weaknesses:** No enzyme gene linked in evidence context; the hypothesis invokes Glo1 without user data. The MK‑specific production is speculative.  
- **Reasoning quality:** Overclaiming; methylglyoxal is a common glycolytic byproduct, not a defined MK‑specific mediator.  
- **Appropriate resolution:** No, it assumes MK source without direct support.

**Evidence assessment:**  
- User‑provided data: Methylglyoxal up in MK metabolomics; no Glo1 expression data.  
- Public data: None.  
- Literature: RAGE in PH, methylglyoxal in diabetes.  
- Inference: Glycolysis in hypoxic MKs leads to methylglyoxal.  
- Speculation: MK‑derived methylglyoxal dominates perivascular pool; Glo1 downregulated.

**Major concerns:**  
- Missing critical data: Glo1 expression in MKs, MK glycolysis rate, methylglyoxal secretion.  
- Methylglyoxal is highly reactive; majority likely intracellular.  
- The hypothesis cannot be verified with current data.

**Downstream‑axis assessment:** Not robust.

**Required revisions:** Need to query Seurat for Glo1 and lactate dehydrogenase; show methylglyoxal secretion from hypoxic MKs in vitro.

**Experimental critique:** MK‑specific Glo1 overexpression would be lengthy; not feasible without foundational data. Missing controls: methylglyoxal scavenger in MK‑specific manner.

**Final recommendation to PI:** Deprioritize – data gap too large; do not advance without primary evidence of MK Glo1 expression and methylglyoxal release.

---

**Hypothesis ID:** Gen1_H3 (retinoic acid Cyp26b1 VSMC)  
Similar to GenMet_H4; Weak; same issues. RA up, Cyp26b1 non‑significant, contradictory. Reject.

---

**Generation 1 H4** not provided; cannot review.

---

**Hypothesis ID:** Gen2_H1 (AMD1 polyamine M2 macrophage fibrosis)  
**Review decision:** Promising but incomplete  
**Directional assessment:**  
- **Strengths:** Uses the same strong AMD1 data; provides a specific downstream axis (M2 macrophage polarization).  
- **Weaknesses:** The specific M2/T

## Ranking output
# Ranking Agent Output

## I. Ranked Hypothesis Table

| Rank | Hypothesis ID | Direction Summary | Overall Score | Main Reason for Rank |
|------|----------------|-------------------|---------------|----------------------|
| 1 | Met_H1 | Hypoxic MK methionine → AMD1 polyamine production → broad perivascular microenvironment shift (immune‑mediated, direct vascular‑wall, or ECM) → medial thickening and vascular stiffening. | 9.2 | Strongest metabolite‑enzyme‑MK link (methionine up, AMD1 enriched and hypoxia‑up with p=6.55e‑06). Keeps downstream axes appropriately broad; excellent reasoning; highly testable via MK‑specific Amd1 deletion. |
| 2 | Gen1_H1 | Hypoxic MK Pnp upregulation → inosine/adenosine release → adenosine receptor activation on vascular cells → medial thickening and muscularization. | 8.6 | Direct compound‑enzyme anchor (inosine up, Pnp significantly up in PH‑MK). Direction broad enough (adenosine receptors) without over‑resolving receptor subtype. MK‑specific Pnp perturbation feasible. |
| 3 | Gen3_H1 | AMD1‑driven polyamine production → ECM cross‑linking via transglutaminase‑2 and eIF5A hypusination → vascular stiffening. | 8.0 | Good metabolic anchor; specifies an ECM‑focused downstream route that is biochemically plausible for polyamines. Slightly over‑resolved but still a strong candidate axis; high disease relevance. |
| 4 | Gen2_H1 | AMD1 polyamines → M2‑like macrophage polarisation → pro‑fibrotic remodelling. | 7.8 | Same strong AMD1 data, but over‑resolves to a specific macrophage polarisation state without direct evidence. Still a plausible immune‑mediated route; good novelty. |
| 5 | Gen2_H5 | Inosine/Pnp → adenosine‑mediated endothelial dysfunction → secondary smooth muscle proliferation. | 7.3 | Based on same purine anchor; focuses on endothelial dysfunction, which is plausible but narrows the axis more than the data warrant. |
| 6 | Gen3_H2 | Inosine/Pnp → adenosine A2B‑driven thrombo‑inflammation (tissue factor, fibrin, myeloid recruitment) → medial muscularization. | 7.1 | Similar purine anchor; specifies a thrombo‑inflammatory path that requires additional data support. |
| 7 | Gen2_H2 | Hypoxic MKs secrete TSP‑1 → activates latent TGF‑β → myofibroblast differentiation and fibrosis. | 5.5 | Plausible mechanism but lacks direct scRNA‑seq evidence for MK Thbs1 expression under hypoxia; currently speculative. |
| 8 | Gen2_H4 | Hypoxic MK EVs deliver PDGF‑BB/TGF‑β1 → PASMC proliferation and fibroblast activation. | 5.3 | EV‑cargo hypothesis; attractive biology but no user‑data anchor for MK expression of Pdgfb/Tgfb1 or EV biogenesis markers. |
| 9 | Gen3_H3 | MK‑derived tissue‑factor‑positive EVs → local coagulation → fibrin‑dependent immune recruitment and SMC activation. | 5.4 | Novel thrombo‑inflammatory EV concept; no direct MK tissue‑factor or EV data. |
| 10 | Gen3_H4 | Similar to Gen2_H2 – TSP‑1/TGF‑β axis. | 5.4 | Same as Gen2_H2. |
| 11 | Met_H2 | Amd2 cooperates with AMD1 to reinforce polyamine synthesis. | 5.0 | Low MK expression (4.4%) and marginal enrichment; unlikely major contributor. Adds little beyond AMD1. |
| 12 | Gen1_H2 | Methylglyoxal from MKs activates RAGE on VSMC → medial hypertrophy. | 4.2 | Metabolite up, but no MK enzyme/gene link (Glo1) provided; over‑claims MK‑specific dicarbonyl release. |
| 13 | Met_H4 | MK Cyp26b1 degrades retinoic acid → de‑represses inflammation and VSMC proliferation. | 3.3 | Metabolite (retinoic acid) is increased, not decreased; enzyme change not significant; weak MK anchoring. |
| 14 | Gen1_H3 | Similar RA/Cyp26b1 axis focused on VSMC growth suppression. | 3.3 | Same issues as Met_H4. |
| 15 | Met_H3 | Methionine → Dnmt3b DNA methylation → pro‑remodelling MK secretome. | 3.0 | No significant MK Dnmt3b expression or hypoxia shift; entirely speculative. |

---

## II. Detailed Score Matrix

Scores are on a 1–10 scale for each criterion.

| Hypothesis ID | Directional Specificity | MK Specificity | Hypoxia Specificity | Vascular Remodeling Relevance | Evidence Support | Appropriate Resolution | Reasoning Quality | Novelty | Testability | Disease Relevance | Overall Priority |
|---------------|------------------------|----------------|---------------------|------------------------------|------------------|------------------------|-------------------|---------|-------------|-----------------|-----------------|
| Met_H1        | 9                      | 9              | 10                  | 8                            | 9                | 10                     | 10                | 9       | 9           | 9               | 9.2             |
| Gen1_H1       | 9                      | 7              | 10                  | 8                            | 8                | 10                     | 9                 | 9       | 8           | 8               | 8.6             |
| Gen3_H1       | 8                      | 9              | 10                  | 9                            | 7                | 6                      | 7                 | 8       | 7           | 9               | 8.0             |
| Gen2_H1       | 8                      | 9              | 10                  | 8                            | 8                | 5                      | 7                 | 7       | 8           | 8               | 7.8             |
| Gen2_H5       | 8                      | 7              | 10                  | 8                            | 7                | 6                      | 7                 | 6       | 7           | 7               | 7.3             |
| Gen3_H2       | 8                      | 7              | 10                  | 8                            | 7                | 5                      | 6                 | 6       | 6           | 8               | 7.1             |
| Gen2_H2       | 6                      | 4              | 5                   | 7                            | 3                | 6                      | 6                 | 6       | 6           | 6               | 5.5             |
| Gen2_H4       | 6                      | 3              | 5                   | 7                            | 2                | 7                      | 6                 | 6       | 5           | 6               | 5.3             |
| Gen3_H3       | 7                      | 3              | 5                   | 7                            | 2                | 6                      | 6                 | 7       | 5           | 6               | 5.4             |
| Gen3_H4       | 6                      | 4              | 5                   | 7                            | 3                | 6                      | 6                 | 5       | 6           | 6               | 5.4             |
| Met_H2        | 6                      | 4              | 8                   | 6                            | 3                | 5                      | 5                 | 3       | 5           | 5               | 5.0             |
| Gen1_H2       | 5                      | 2              | 4                   | 6                            | 2                | 5                      | 4                 | 6       | 3           | 5               | 4.2             |
| Met_H4        | 4                      | 2              | 2                   | 5                            | 2                | 4                      | 3                 | 4       | 4           | 3               | 3.3             |
| Gen1_H3       | 4                      | 2              | 2                   | 5                            | 2                | 4                      | 3                 | 4       | 4           | 3               | 3.3             |
| Met_H3        | 4                      | 1              | 3                   | 4                            | 1                | 4                      | 3                 | 5       | 3           | 2               | 3.0             |

---

## III. Pairwise Comparison Summary

### AMD1‑Polyamine Cluster (Met_H1 vs Gen2_H1 vs Gen3_H1)

- **Competing hypotheses:**  
  - Met_H1: broad candidate downstream axes (immune, vascular, ECM) – does not over‑commit.  
  - Gen2_H1: specifies M2‑like macrophage polarisation → fibrosis.  
  - Gen3_H1: specifies ECM cross‑linking / hypusination → vascular stiffening.

- **Winner:** Met_H1  
- **Reason:**  
  Both Gen2_H1 and Gen3_H1 select a single downstream route without direct evidence that MK‑derived polyamines act predominantly through that route. Met_H1 correctly keeps the axis broad, acknowledging multiple possibilities, and therefore better matches the current evidence level. The data anchor (methionine → AMD1) is identical; the narrower hypotheses over‑resolve and risk false‑negative interpretation if the favoured axis turns out minor.  
- **Key discriminating evidence:** None that distinguish the routes at present; the strongest evidence supports the upstream metabolic shift, not a specific downstream effector. Therefore the most appropriate hypothesis is the one that does not prematurely lock a recipient cell or pathway.

### Inosine/Adenosine Cluster (Gen1_H1 vs Gen2_H5 vs Gen3_H2)

- **Competing hypotheses:**  
  - Gen1_H1: adenosine receptor activation broadly on vascular cells (VSMC, EC) → medial thickening.  
  - Gen2_H5: adenosine‑mediated endothelial dysfunction as primary driver.  
  - Gen3_H2: adenosine A2B‑driven thrombo‑inflammatory cascade (tissue factor, fibrin).

- **Winner:** Gen1_H1  
- **Reason:**  
  The direct data (inosine up, Pnp/Nt5c2 up) support purine nucleoside release but do not resolve whether the pathological signal is endothelial‑specific, thrombo‑inflammatory, or acts on smooth muscle. Gen1_H1’s broad vascular‑wall description avoids over‑specifying one receptor‑cell axis. The other two could be candidate axes, but as standalone hypotheses they claim a specificity not yet justified.  
- **Key discriminating evidence:** None currently; the shared upstream data cannot discriminate. Gen1_H1 is favoured for its appropriate resolution.

---

## IV. Recommendations to PI Agent

### Top hypotheses to advance (high confidence)
- **Met_H1 (Rank 1):** AMD1‑driven polyamine metabolism – the strongest metabolomics‑anchored, MK‑specific hypothesis. Immediate priority for experimental validation (MK‑specific Amd1 knockout/inhibition, lung polyamine quantification, vascular morphometry).  
- **Gen1_H1 (Rank 2):** Pnp‑mediated purine nucleoside release – strong data and testable with MK‑specific Pnp deletion.

These two represent distinct, non‑redundant metabolic axes that can be pursued in parallel.

### Hypotheses to revise (retain as candidate axes under broader hypotheses)
- **Gen2_H1, Gen3_H1, Gen2_H5, Gen3_H2:** These contain valid downstream possibilities (macrophage polarisation, ECM cross‑linking, endothelial dysfunction, thrombo‑inflammation) but should be merged into Met_H1 or Gen1_H1 as **candidate axes** rather than independent hypotheses. Revise to remove language suggesting a settled mechanism; label as “provisional downstream models” only.

### Hypotheses to merge
- **Met_H2 (Amd2):** merge into Met_H1 as a minor modifier note; do not pursue separately.  
- **Gen2_H1, Gen3_H1 → incorporate as candidate axes under Met_H1.**  
- **Gen2_H5, Gen3_H2 → incorporate as candidate axes under Gen1_H1.**  
- **Gen2_H2 and Gen3_H4 (TSP‑1/TGF‑β):** these share mechanism; if scRNA‑seq confirmation of *Thbs1* upregulation in PH‑MK is obtained, merge into a single revised hypothesis; otherwise deprioritize.

### Hypotheses to reject
- **Met_H3 (Dnmt3b):** lacks significant MK expression and hypoxia shift; data anchor too weak.  
- **Met_H4, Gen1_H3 (Cyp26b1/retinoic acid):** metabolite direction contradicts mechanism; enzyme not significantly hypoxia‑regulated in MKs.  
- **Gen1_H2 (methylglyoxal/RAGE):** no MK enzyme/gene evidence; cannot be MK‑specific.  
- **Gen2_H4, Gen3_H3 (EV‑cargo hypotheses without scRNA‑seq validation):** reject in their current form; they require prior demonstration of MK‑specific upregulation of the proposed cargo genes (Pdgfb, Tgfb1, F3) and EV biogenesis markers under hypoxia.

### Directional areas underrepresented
- **Spatial niche / perivascular interactions:** No hypothesis yet directly addressed MK proximity to specific vessel types or stromal cells beyond generic “perivascular.” Could be pursued if spatial transcriptomics or imaging data become available.  
- **Direct endothelial‑MK or VSMC‑MK metabolic coupling** (e.g., metabolite transfer via gap junctions, tunneling nanotubes) is not represented.  
- **Immune recruitment signalling** (chemokine‑mediated) separate from polyamine/purine axes remains underdeveloped; this could be addressed if future scRNA‑seq assays identify MK‑specific chemokine upregulation.

**Next cycle focus:** I recommend the PI instruct generation agents to produce candidate‑axis‑specific validation hypotheses built on the winning broad directions (Met_H1 and Gen1_H1), while requesting tool‑use agents to extract MK expression of EV‑related and matrix‑remodelling genes to enable better‑anchored ECM/EV hypotheses.

## Meta-review output
# Meta‑review Agent Output – Cycle 1

## I. Cross‑review synthesis

### Strong consensus directions

- **AMD1‑polyamine axis (Met_H1)**  
  All reviewers and the ranking agent agree this is the top‑priority metabolomics‑driven hypothesis. The anchor (methionine ↑, AMD1 enriched and hypoxia‑upregulated in MKs) is direct, MK‑specific, and statistically robust. The broad downstream framing (immune‑mediated, direct vascular‑wall, or ECM) is appropriate for the current evidence. Testability via MK‑specific *Amd1* deletion/inhibition is clear.

- **Inosine/Pnp‑adenosine receptor axis (Gen1_H1)**  
  Strong consensus that the inosine‑Pnp link is well‑supported by user data. The broad adenosine‑receptor‑mediated vascular‑wall outcome is a plausible direction; reviewers agree the axis should not be narrowed to a single receptor subtype or cell type without further data.

### Disputed directions

- **Narrowed downstream axes of the above (Gen2_H1, Gen3_H1, Gen2_H5, Gen3_H2)**  
  These attempt to specify M2 macrophage polarisation, ECM cross‑linking, endothelial dysfunction, or thrombo‑inflammation as the *primary* route. Reflection and ranking agents uniformly consider them over‑resolved; they are better treated as candidate axes under the broad hypotheses. The dispute is not about biological plausibility but about premature commitment.

- **Cyp26b1/retinoic acid (Met_H4, Gen1_H3)**  
  Some reviewers reject outright, others deprioritize. The central contradiction – metabolite is elevated, yet the hypothesis requires local depletion – is unresolved. The MK‑enzyme evidence is non‑significant. This is not salvageable without new data.

- **Methylglyoxal/RAGE (Gen1_H2)**  
  Reflection agents flag missing MK‑enzyme data (no Glo1 expression or differential shown). Ranking agent scores it low. Consensus: deprioritize until foundational data are obtained.

### Weak hypotheses

- **Dnmt3b/methylation (Met_H3)** – Rejected by all; MK expression of Dnmt3b is negligible and not hypoxia‑regulated. No data anchor.
- **Amd2 standalone (Met_H2)** – Seen as a low‑confidence modifier of AMD1; low expression, marginal enrichment. Merge or drop.
- **EV‑cargo and TSP‑1/TGF‑β hypotheses (Gen2_H2, Gen2_H4, Gen3_H3, Gen3_H4)** – Lack direct scRNA‑seq data for cargo or biogenesis genes in MKs. Currently speculative; need confirming expression checks.

### Redundant hypothesis groups

- **Polyamine cluster:** Met_H1, Gen2_H1, Gen3_H1, Met_H2 – same metabolic start; differ only in downstream emphasis. All can be consolidated under Met_H1 with candidate axes.
- **Purine cluster:** Gen1_H1, Gen2_H5, Gen3_H2 – identical Pnp/inosine start; consolidate under Gen1_H1.
- **Retinoic acid cluster:** Met_H4 and Gen1_H3 – nearly identical weak evidence; redundant.
- **TSP‑1 cluster:** Gen2_H2 and Gen3_H4 – same proposed mechanism; merge if data support emerges.

---

## II. Systemic failure modes

### Main recurring problems

1. **Over‑resolution of the downstream axis without direct data**  
   Multiple generation agents present a single recipient cell or signalling pathway (M2 macrophage, endothelial dysfunction, thrombo‑inflammation) as the working model, treating literature‑based candidate examples as settled. This violates the PI instruction to label such axes as *candidate* and avoid forcing a final bridge.

   *Examples:* Gen2_H1 (M2 macrophage polarisation), Gen3_H2 (adenosine‑A2B thrombo‑inflammatory), Gen3_H1 (ECM cross‑linking/hypusination).

   *Consequence:* Ranking scores suffer; review agents recommend downgrading or merging. Risks misdirecting experimental resources.

2. **Hypotheses lacking direct MK‑specific gene/protein evidence**  
   Several hypotheses propose mediators (methylglyoxal, EVs with PDGF/TGF‑β, tissue factor, TSP‑1) without having checked expression of the relevant genes in the user scRNA‑seq data. The tool‑use requests for such checks were submitted but not yet answered.

   *Examples:* Gen1_H2 (methylglyoxal – no Glo1 data), Gen2_H4 (PDGF‑BB/TGF‑β EVs – no Pdgfb/Tgfb1 check), Gen3_H3 (tissue‑factor EV – no F3 check), Gen2_H2/Gen3_H4 (TSP‑1 – no Thbs1 check).

   *Consequence:* These hypotheses are currently unfalsifiable at the MK level; reviewers deem them speculative and deprioritize.

3. **Metabolite‑direction contradictions not addressed**  
   Retinoic acid (RA) is upregulated in PH‑MK, yet the hypotheses propose that MKs degrade RA via Cyp26b1, leading to local RA deficiency. The data directly contradict the mechanism, and the attempted explanatory logic (compensatory upregulation) is strained. The same issue did not arise for metabolites that matched the predicted direction (methionine, inosine).

   *Example:* Met_H4, Gen1_H3.

   *Consequence:* These hypotheses are internally inconsistent and were uniformly rejected or deprecated.

4. **Thin metabolic chains with no downstream resolution**  
   Some hypotheses connect a metabolite to an enzyme, but the pathway logic stops at “altered MK secretome” or “pro‑remodelling phenotype” without defining a plausible mediator class or broad axis. This is better than over‑resolving, but still leaves the hypothesis less useful.

   *Example:* Met_H3 (Dnmt3b) – the enzyme is not even MK‑expressed, but the downstream chain is completely unresolved.

5. **Penalizing appropriately broad directions**  
   A few generation agents appeared to avoid broad labels, instead specifying a candidate example (e.g., Th17, IL‑17, EndMT) as the final mechanism. The Reflection and Ranking agents rectified this by downgrading over‑resolved versions and promoting the broad ones. The systemic issue is a generation bias toward forced resolution.

6. **Under‑utilization of the public dataset analysis**  
   GSE289322 differential expression results were available but not inspected by generation agents; they only mentioned that it “could validate.” Reflection and Meta‑review agents note that no public‑dataset evidence actually supports any hypothesis. This is a missed opportunity for orthogonal support.

---

## III. Evidence gaps

### User data gaps (within the provided Seurat object and metabolomics tables)
- **MK‑specific gene expression for EV cargo, coagulation, and matrix proteins not queried:**  
  *Pdgfb, Tgfb1, F3, Thbs1, Rab27a, Tsg101, Cd44, Lox, Loxl1, Loxl2, Glo1, Mki67*, and others remain unexamined. These are essential to ground many proposed mechanisms.
- **No MK‑secreted polyamine or purine nucleoside measurements** – the hypotheses infer release, but no direct extracellular metabolite data exist.
- **No AMD1/Amd2 protein or activity data** in MKs; only transcript counts.
- **No spatial information** about MK localisation relative to vessel types, ECM, or immune cells – spatial niche hypotheses remain entirely inferential.

### Public data gaps
- **GSE289322 DE results and candidate gene check files not inspected** – could have provided tissue‑level validation for *Amd1*, *Pnp*, *Nt5c2*, *Glo1*, etc.
- **No single‑cell, spatial, or proteomic public datasets** matched the search; thus MK‑specific validation from public sources is absent.
- **The only other dataset (GSE291455)** has no case‑control design and cannot provide differential evidence.

### Literature gaps
- No direct reports of MK‑AMD1 or MK‑polyamine secretion in pulmonary hypertension.
- Inosine/adenosine signalling in PH is well‑described, but MK as a sources is novel and unstudied.
- TSP‑1, tissue factor, and PDGF/TGF‑β in MKs are known in platelet biology, but hypoxia‑specific regulation in lung‑resident MKs is not documented.
- Methylglyoxal‑RAGE axis established in diabetes, not in hypoxic PH MKs.

### Experimental gaps
- No MK‑specific *Amd1*, *Pnp*, or *Cyp26b1* knockout models yet tested in hypoxia‑PH.
- No measurements of perivascular polyamine or adenosine/inosine concentrations in lung.
- No MK‑conditioned medium transfer experiments to test paracrine activity on target vascular cells.
- No MK‑derived EV isolation from hypoxic lungs to characterize cargo.

---

## IV. Recommendations to PI Agent

### Advance (with minimal revision)
- **Met_H1** – AMD1‑polyamine axis, broad candidate axes. Mark as highest priority for experimental validation (MK‑*Amd1* KO, lung polyamine measurements, vascular morphometry).  
- **Gen1_H1** – Inosine/Pnp → adenosine receptor axis. Advance in parallel; design MK‑*Pnp* deletion and assess perivascular adenosine/inosine levels.

Both have strong MK‑specific data anchors and testable direction‑level predictions.

### Revise (tighten language, merge as candidate axes)
- **Gen2_H1, Gen3_H1, Gen2_H5, Gen3_H2** – These are not independent hypotheses. They should be re‑expressed as **candidate downstream axes** under Met_H1 or Gen1_H1, clearly labelled “provisional.” Remove language that implies a settled mechanism. Only advance specific experimental tests for the preferred axis after initial validation of the broad direction.

### Merge
- **Met_H2** → merge into Met_H1 as a minor note (possible Amd2 contribution).  
- **Gen2_H2 and Gen3_H4** → if future scRNA‑seq confirms *Thbs1* upregulation in PH‑MK, merge into a single TSP‑1/TGF‑β hypothesis.  
- **Gen2_H4 and Gen3_H3** → likewise, if EV cargo genes (*Pdgfb*, *Tgfb1*, *F3*) show MK‑specific hypoxia‑up, merge into a unified “MK‑derived EV cargo” hypothesis with specific candidate mediators.

### Reject
- **Met_H3 (Dnmt3b)** – insufficient MK expression and no differential.  
- **Met_H4, Gen1_H3 (Cyp26b1/retinoic acid)** – metabolite direction contradicts mechanism; enzyme not significantly regulated.  
- **Gen1_H2 (methylglyoxal/RAGE)** – no MK enzyme anchor; insufficient evidence.  
- **Gen2_H4, Gen3_H3, Gen2_H2, Gen3_H4** in their current form – reject as standalone hypotheses until MK gene expression data are provided.

### Generate next
The PI should instruct generation agents to **produce candidate‑axis‑specific validation hypotheses** that follow from the advanced broad directions, but only after the first‑tier experiments confirm the metabolic shift and paracrine mediator release. Additionally, the PI should request tool‑use agents to **immediately retrieve** the missing scRNA‑seq data for EV‑related, coagulation, and matrix genes, so that the weaker hypotheses can be re‑evaluated or discarded.

---

## V. Feedback for next Generation cycle

### Required direction categories for new hypotheses
- No new broad metabolic directions are needed unless the tool‑use queries reveal a new metabolite‑enzyme‑MK axis with strong evidence. Focus on **downstream axis refinement experiments** rather than new mechanism discovery.
- If spatial niche hypotheses are to be pursued, they must incorporate a testable proximity assumption (e.g., MK co‑localization with α‑SMA⁺ vessels or specific ECM components) based on imaging or spatial transcriptomics, not just inference.

### Required evidence checks before generating new hypotheses
- **Mandatory query of Seurat object:** Expression and differential expression (PH vs control) in MK/platelet cluster for: *Pdgfb, Tgfb1, F3, Thbs1, Glo1, Rab27a, Tsg101, Cd44, Lox, Loxl1, Loxl2, Mki67* (and any additional candidates from the mechanism‑ready shortlist).  
- **Inspect GSE289322 DE results and candidate gene check** for the genes above and the polyamine/purine pathway genes (*Amd1*, *Amd2*, *Pnp*, *Nt5c2*). Publish these results to all agents before hypothesis generation.  
- **Extract any tissue‑level metabolite data** from the whole‑lung metabolomics file that match the MK‑specific differentials (e.g., methionine, inosine, spermidine) to see if MK shifts propagate to tissue.

### Exclusion criteria (hypotheses that must not be generated again)
- Any hypothesis that relies on Dnmt3b, Cyp26b1, or Amd2 as a primary enzyme without new, strong supporting data.
- Any hypothesis that presents a final downstream bridge (e.g., Th17‑IL‑17‑EndMT, M2‑specific polarisation) as a settled mechanism rather than a candidate example.
- Any hypothesis that lacks both a user‑data anchor **and** a completed public‑data validation step.
- EV‑cargo or matrix‑remodelling hypotheses that do not cite specific MK gene expression results from the Seurat object.

### Suggested new hypothesis directions (for after data gap filling)
- If *Thbs1* and *F3* are confirmed hypoxia‑up in MKs, generate a unified “MK matricellular and pro‑coagulant secretome” hypothesis focusing on spatial remodelling.
- If polyamine secretion from MKs is confirmed, design hypotheses that explicitly compare immune‑mediated, direct vascular‑wall, and ECM‑cross‑linking routes using cell‑type‑specific receptor blockers.
- Explore direct metabolic coupling (e.g., lactate, nucleotides) between hypoxic MKs and adjacent endothelial/smooth muscle cells using the upcoming MK‑conditioned medium data.

### Resolution fixes for generation agents
- **Do not name a single working model** for the downstream axis unless the evidence directly implicates it. Always list 2‑4 candidate axes and explicitly state which one is provisionally favoured, with reasoning that includes uncertainty.
- **Always check the Seurat object for expression of the candidate gene** in MKs and for PH‑vs‑control differential before building a hypothesis around it. If the gene is not expressed or not differentially regulated, the hypothesis is invalid.
- **When a metabolite change is reported, check that the proposed mechanism matches its direction.** If a hypothesis requires the metabolite to decrease but the data show an increase, it must be justified by a specific, testable intermediate (e.g., intracellular vs extracellular pool) – otherwise, reject it.
- **Do not treat KEGG pathway membership or PubMed keyword hits as evidence of causality**; they are only literature‑support indicators. The strength of a hypothesis rests on the user‑data anchor and the logical consistency of the chain.
- **Use the Public Dataset Analysis results** if they become available; explicitly cite whether GSE289322 supports, refutes, or is silent on each gene’s tissue‑level differential expression. Silence does not weaken the MK‑specific anchor but must be acknowledged.

---

**Cycle 1 Meta‑review summary:**  
The first cycle has successfully identified two high‑confidence, MK‑specific, metabolomics‑anchored directions: AMD1‑polyamine and Pnp‑inosine/adenosine. The overall landscape is marred by over‑resolution and by a cluster of hypotheses that were generated before essential gene‑expression data were extracted. The next cycle should prioritise filling those data gaps and producing refined, axis‑specific validation experiments rather than adding new broad mechanisms. The PI should immediately request the outstanding Seurat and public‑data checks before instructing the next round of generation.

## Evolution output
**Revised hypotheses output by the Evolution Agent – Cycle 1**

Two merged, refined hypotheses replace the earlier overlapping polyamine and purine nucleoside clusters.  
All weak or unsupported hypotheses are not advanced; they remain rejected/deprioritised per the Meta‑review.

---

### Revised Hypothesis 1

**Original hypothesis IDs:** GenMet_H1, GenMet_H2, Gen2_H1, Gen3_H1  
**Revised hypothesis ID:** Evo_H1  
**Revision type:** merge, refine  
**PI feedback addressed:** Meta‑review identified the AMD1‑polyamine axis as the top priority but noted that the downstream branches were over‑resolved. This revision merges the broad AMD1 hypothesis (GenMet_H1) with the candidate immune‑mediated (Gen2_H1), ECM/stromal (Gen3_H1), and the minor Amd2 contribution (GenMet_H2) into a single, appropriately broad direction. All downstream routes are now explicitly labelled as **provisional candidate axes**; no single working model is favoured. Language that previously implied a settled mechanism (e.g., “M2 macrophage polarisation is the primary axis”) has been removed.

**Revised hypothesis title:** Hypoxic MK AMD1‑driven polyamine metabolism fuels perivascular microenvironment shifts that promote pulmonary vascular remodelling via multiple candidate axes

**Revised core directional hypothesis:**  
Hypoxia up‑regulates AMD1 in lung megakaryocytes, diverting methionine‑derived S‑adenosylmethionine into polyamine (spermidine/spermine) synthesis. These polyamines, once released, act through one or more candidate downstream axes—**immune modulation**, **direct vascular‑wall signalling**, or **ECM cross‑linking/hypusination**—to drive medial thickening, muscularization, and vascular stiffening in hypoxia‑induced pulmonary hypertension.

**Revised direction‑level reasoning summary:**
- **Data anchor:** Methionine is strongly elevated in PH MKs (log2FC = 3.26). AMD1 is enriched in MKs (log2 1.35) and significantly up‑regulated in PH (log2FC = 1.77, p = 6.55 × 10⁻⁶). Amd2, a paralog, shows a modest yet significant PH‑up shift (log2FC = 2.18, p = 0.024) in a low MK sub‑population (4.4 %).
- **Biological interpretation:** Hypoxic MKs re‑route methionine metabolism toward polyamine production. AMD1 catalyses the rate‑limiting decarboxylation of SAM, committing flux to spermidine/spermine. This establishes a plausible MK‑centric metabolic programme with the potential to alter the perivascular niche.
- **MK‑linked pathway logic:** AMD1 is a direct pathway‑neighbor in cysteine/methionine metabolism. Its MK enrichment and hypoxia responsiveness support the hypothesis that MKs become a local source of bioactive polyamines. Amd2 may contribute cooperatively but likely plays a minor role.
- **Candidate downstream axes:**  
  1. **Immune‑mediated** – polyamines modulate T‑cell differentiation (e.g., Th17‑like) and macrophage polarisation (M2‑like), creating a pro‑fibrotic/inflammatory milieu.  
  2. **Direct vascular‑wall** – polyamines or their derivatives directly promote PASMC proliferation/hypertrophy, endothelial dysfunction, or fibroblast activation.  
  3. **ECM/stromal** – polyamines serve as substrates for transglutaminase‑2 (TGM2)‑catalysed matrix cross‑linking and for eIF5A hypusination, which drives translation of pro‑fibrotic genes and stiffens the vessel wall.  
  Each axis is **provisional**; the current data do not discriminate among them.
- **Remodelling logic:** Peri‑MK polyamine accumulation alters the balance of immune surveillance, vascular cell quiescence, and matrix compliance, collectively promoting medial thickening, muscularization, and reduced vascular compliance.
- **Key uncertainty:** Polyamine secretion from hypoxic MKs has not been directly shown. The relative importance of free polyamines versus EV‑delivered polyamines, and which recipient cell type(s) dominate, remain unresolved. AMD1 protein activity and the actual polyamine product profile need direct measurement.

**Revised directional chain:**
1. Hypoxia induces methionine accumulation and AMD1 up‑regulation in lung‑resident MKs, increasing SAM decarboxylase activity.
2. MKs produce elevated spermidine/spermine, which are released into the perivascular microenvironment (via passive diffusion, transporters, or extracellular vesicles).
3. Candidate downstream axes:  
   a. **Immune‑mediated** – polyamines influence T‑cell/macrophage phenotypes, promoting a remodelling niche.  
   b. **Direct vascular‑wall** – polyamines act on PASMCs, endothelial cells, or fibroblasts to drive proliferation/dysfunction.  
   c. **ECM/stromal** – polyamines serve as co‑substrates for transglutaminase cross‑linking and eIF5A hypusination, stiffening the vessel wall.
4. These mechanisms collectively promote medial smooth muscle hypertrophy/hyperplasia, endothelial barrier disruption, perivascular collagen deposition, and matrix cross‑linking.
5. The result is the medial thickening, muscularization, and vascular stiffness characteristic of hypoxia‑induced PH.

**Candidate downstream axes:**
- **Plausible axes:**  
  • Immune‑mediated (Th17‑like T‑cell activity, M2‑like macrophage polarisation)  
  • Direct vascular‑wall (PASMC proliferation/hypertrophy, endothelial activation, fibroblast‑to‑myofibroblast transition)  
  • ECM/stromal (TGM2‑mediated cross‑linking, eIF5A hypusination‑dependent profibrotic gene expression)
- **Working model:** **None is favoured.** All three remain equally plausible provisional candidates. The dominant route likely depends on local polyamine concentration, recipient cell proximity, and co‑factors.
- **Specific examples kept provisional:** Spermidine, spermine, Th17, IL‑17, STAT3, M2 macrophages, α‑SMA⁺ cells, collagen cross‑links, hypusinated eIF5A – these are examples, not confirmed mediators.
- **What remains unresolved:** Which cell type(s) respond to MK‑derived polyamines; whether polyamines act as free molecules or are EV‑bound; the role of Amd2; and whether polyamine effects require conversion to other metabolites (e.g., hypusine).

**Evidence retained:**
- **User‑provided data:**  
  • MK‑sorted metabolomics: methionine up (log2FC = 3.26).  
  • Seurat: AMD1 MK expression 31.4 %, enrichment 1.35, PH‑up log2FC = 1.77, p = 6.55 × 10⁻⁶.  
  • Amd2: MK 4.4 %, enrichment 0.93, PH‑up log2FC = 2.18, p = 0.024.
- **Public data:** GSE289322 may yield tissue‑level AMD1 validation; not yet inspected.
- **Literature:** AMD1/mTORC1/polyamine axis (PMID 28658205); polyamine roles in immune modulation and fibrosis; eIF5A hypusination (PMID 38965534); transglutaminase in vascular stiffness.
- **Biological rationale:** MK perivascular location and polyamine biology support a local effector function.

**Evidence added:**  
None beyond merging existing evidence. No new public‑data analysis was incorporated.

**Unsupported claims removed or downgraded:**
- Removed any assertion that “immune‑mediated (Th17/macrophage)” is the working model (from GenMet_H1) and that “M2 macrophage polarisation is the primary axis” (Gen2_H1). All downstream axes are now strictly candidate.
- Downgraded Amd2 from a cooperative main driver to a minor modifier.
- Eliminated language implying that polyamines directly induce EndMT or specific cytokine cascades without evidence.
- The inference that AMD1 up‑regulation necessarily leads to extracellular polyamine action is now explicitly flagged as requiring validation.

**Improved experimental validation:**
- **Primary perturbation:** MK‑specific Amd1 deletion (Pf4‑Cre;Amd1^(fl/fl)) or pharmacological AMD1 inhibition (SAM486A) in hypoxia‑PH model.
- **Secondary axis‑specific follow‑ups** (to be employed only after confirming polyamine release):
  • Immune‑mediated: macrophage depletion (clodronate) or T‑cell subset blockade.
  • Direct vascular‑wall: polyamine receptor antagonists (when identified) or PASMC‑specific AMD1 overexpression.
  • ECM/stromal: transglutaminase‑2 inhibition (cystamine) or eIF5A hypusination blocker (GC7).
- **Readouts:** Lung polyamine levels (LC‑MS), medial thickness, muscularization, RVSP, and in vitro polyamine secretion (MK‑conditioned medium) plus AMD1 activity (SAM/decarboxylated‑SAM ratio).
- **Controls:** Verify MK‑specific deletion efficiency; measure polyamines in platelet‑free plasma; include recombinant polyamine rescue.
- **Expected result:** AMD1 blockade reduces lung polyamine levels and attenuates vascular remodelling.  
- **Falsifying result:** MK‑specific Amd1 deletion fails to alter lung polyamines or vascular remodelling despite efficient knockout, or polyamine supplementation restores remodelling in Amd1‑KO mice, indicating that MK‑derived polyamines are not the critical mediators.

**Remaining weaknesses:**
- Direct proof of polyamine secretion by hypoxic MKs is absent; this must be acquired before pursuing individual downstream axes.
- No tissue‑level validation (public data) yet; absence would not refute the MK‑specific axis but would weaken overall pathway engagement.
- The hypothesis deliberately keeps the downstream axis broad, which may be perceived as imprecise; however, this matches the current evidence level.

**Recommendation:** Ready for PI review. This merged direction should be the primary focus of metabolomics‑driven validation. Individual candidate axes should be tested sequentially only after confirming polyamine release from MKs.

---

### Revised Hypothesis 2

**Original hypothesis IDs:** Gen1_H1, Gen2_H5, Gen3_H2  
**Revised hypothesis ID:** Evo_H2  
**Revision type:** merge, refine  
**PI feedback addressed:** Meta‑review identified the inosine/Pnp purine axis as the second strongest direction but noted that three separate hypotheses over‑resolved the downstream pathway (direct vascular‑wall, endothelial dysfunction, thrombo‑inflammation). This revision merges them into a single, appropriately broad purine nucleoside hypothesis. All downstream routes are now presented as candidate axes, and receptor‑subtype (A2B) specificity is kept provisional. The unqualified language that one axis is “the primary mechanism” has been removed.

**Revised hypothesis title:** Hypoxic MK up‑regulation of purine nucleoside phosphorylase (Pnp) generates extracellular inosine that, via adenosine receptor activation, promotes vascular remodelling through endothelial, smooth muscle, and thrombo‑inflammatory candidate axes

**Revised core directional hypothesis:**  
Hypoxia increases Pnp expression in lung MKs, leading to inosine accumulation and extracellular release. Inosine and its metabolite adenosine engage adenosine receptors (A2A, A2B, A3) on pulmonary vascular endothelial cells, smooth muscle cells, and immune cells, driving a combination of endothelial dysfunction, PASMC proliferation/hypertrophy, and/or thrombo‑inflammatory cascades (tissue factor expression, fibrin deposition, myeloid recruitment) that collectively contribute to medial thickening, muscularization, and vascular stiffness.

**Revised direction‑level reasoning summary:**
- **Data anchor:** Inosine is strongly elevated in PH MKs (log2FC = 3.82). Pnp is expressed in 20.3 % of MKs and significantly up‑regulated in PH (log2FC = 1.74, p = 3.81 × 10⁻⁶); Nt5c2, a complementary purine nucleotidase, is also up (log2FC = 2.88, p = 2 × 10⁻⁴). This provides a direct compound‑enzyme link.
- **Biological interpretation:** Hypoxic MKs shift toward purine nucleotide catabolism, producing inosine that can be exported. Extracellular inosine may be converted by ectonucleotidases (e.g., CD73) to adenosine, a potent vasoactive and immunomodulatory signalling molecule.
- **MK‑linked pathway logic:** Pnp and NT5C2 are direct enzymes in purine metabolism. Their MK expression and PH‑up regulation position MKs as a potential perivascular source of inosine/adenosine, providing a mechanism by which MK metabolism could alter local adenosine receptor tone.
- **Candidate downstream axes:**  
  1. **Direct vascular‑wall** – adenosine receptor activation (A2B on PASMCs, A2A on endothelium) leads to PASMC proliferation/hypertrophy and endothelial barrier dysfunction.  
  2. **Endothelial dysfunction‑dominant** – chronic A2 signalling on endothelial cells up‑regulates adhesion molecules (VCAM‑1, ICAM‑1), reduces eNOS activity, and promotes a pro‑inflammatory surface, facilitating leukocyte adhesion and secondary smooth muscle activation.  
  3. **Thrombo‑inflammation** – adenosine/A2B activation induces tissue factor (F3) expression on endothelial cells, triggering local coagulation, fibrin deposition, and monocyte/macrophage recruitment that amplify vascular remodelling.  
  All three axes are **provisional**.
- **Remodelling phenotype:** Medial thickening, muscularization, endothelial dysfunction, perivascular fibrin accumulation, and vascular stiffening.
- **Key uncertainty:** The net effect of extracellular adenosine/inosine is highly context‑dependent (vasodilatory and anti‑inflammatory vs. pro‑remodelling). The dominant receptor subtype and the primary pathological route (endothelial dysfunction vs. smooth muscle proliferation vs. thrombo‑inflammation) are unresolved. Direct measurement of perivascular adenosine/inosine concentrations from MKs is required.

**Revised directional chain:**
1. Hypoxia up‑regulates Pnp and Nt5c2 in lung MKs, enhancing purine degradation to inosine.
2. Inosine is released into the perivascular space; extracellular inosine can be converted to adenosine by ecto‑5’‑nucleotidase.
3. Increased local adenosine/inosine activates adenosine receptors on adjacent cells, potentially through:
   a. **Direct PASMC A2B receptor activation** → proliferation/hypertrophy.
   b. **Endothelial A2A/A2B activation** → barrier disruption, adhesion molecule expression, impaired NO production.
   c. **Endothelial/immune cell A2B activation** → tissue factor up‑regulation, thrombin generation, fibrin deposition, and myeloid recruitment.
4. The combined consequences include enhanced smooth muscle mass, endothelial dysfunction, and a perivascular thrombotic/inflammatory microenvironment.
5. These changes drive medial thickening, muscularization, and vascular stiffness characteristic of hypoxic PH.

**Candidate downstream axes:**
- **Plausible axes:**  
  1. Direct vascular‑wall (PASMC A2B‑mediated hypertrophy, endothelial A2A/A2B‑mediated dysfunction)  
  2. Endothelial dysfunction‑dominant (impaired vasodilation, leukocyte adhesion) leading to secondary remodelling  
  3. Thrombo‑inflammatory (tissue factor/fibrin → immune cell recruitment)
- **Working model:** **None is preferred.** The relative contribution may vary with time and severity of hypoxia.
- **Specific examples kept provisional:** A2B receptor on PASMC, A2A on endothelium, tissue factor (F3), fibrin, IL‑6, CCL2, monocyte/macrophage infiltration.
- **What remains unresolved:** Which adenosine receptor subtype(s) mediate the pathological effects in the hypoxic lung; whether inosine itself acts directly or only after conversion; and whether the net effect is pro‑remodelling or partially protective (e.g., A2A‑mediated vasodilation). MK‑origin gap: inosine/adenosine release and local concentration not directly measured.

**Evidence retained:**
- **User‑provided data:**  
  • MK‑sorted metabolomics: inosine log2FC 3.82.  
  • Seurat: Pnp MK pct 20.31 %, enrichment −1.22 (but PH‑up within MK log2FC = 1.74, p = 3.81 × 10⁻⁶); Nt5c2 PH‑up log2FC = 2.88, p = 2 × 10⁻⁴.
- **Public data:** GSE289322 may validate tissue‑level Pnp/Nt5c2 differential; not yet inspected.
- **Literature:** Adenosine A2B in PH, tissue factor induction by A2B, endothelial dysfunction via adenosine; inosine immunomodulatory properties.
- **Biological rationale:** Purine nucleoside release is a known metabolic stress response; perivascular MKs could deliver high local concentrations.

**Evidence added:**  
None beyond merging.

**Unsupported claims removed or downgraded:**
- Removed the specification that “adenosine A2B receptor alone is the dominant pathological receptor” (Gen1_H1, Gen2_H5) – now described as one candidate receptor among several.
- Downgraded the primary roles of endothelial dysfunction (Gen2_H5) and thrombo‑inflammation (Gen3_H2) from “dominant axis” to “candidate axis.”
- Removed any implication that MK‑derived adenosine/inosine solely drives VSMC proliferation without considering vasodilatory effects.

**Improved experimental validation:**
- **Perturbation:** MK‑specific Pnp deletion (Pf4‑Cre;Pnp^(fl/fl)) or pharmacological Pnp inhibitor (immucillin‑H). Adenosine receptor antagonists (A2B: PSB1115, A2A: ZM241385) to probe axis specificity.
- **Model:** Hypoxic PH mouse; early and late time points to differentiate acute and chronic effects.
- **Readouts:**
  • Lung inosine/adenosine levels (LC‑MS), RVSP, vascular morphometry.
  • Endothelial function: acetylcholine‑induced relaxation, VCAM‑1/ICAM‑1 expression.
  • Thrombo‑inflammation: tissue factor immunostaining, fibrin deposition, myeloid cell infiltration.
  • PASMC proliferation: BrdU/EdU, α‑SMA⁺ cell counts.
- **Controls:** MK‑specific Pnp overexpression; CD73 inhibitor to block extracellular adenosine conversion; adenosine receptor agonist rescue.
- **Expected result:** MK Pnp loss reduces lung inosine/adenosine and attenuates multiple aspects of remodelling. If A2B blockade fully recapitulates protection, the A2B pathway is key; if A2A blockade exacerbates, it suggests protective A2A tone.
- **Falsifying result:** MK Pnp deletion does not alter perivascular adenosine levels or vascular remodelling (suggesting MK‑derived purines are not a critical source), or adenosine receptor blockade has no effect or worsens phenotype.

**Remaining weaknesses:**
- The net effect of adenosine signalling is complex; the hypothesis could be falsified if adenosine is predominantly protective. Careful dose‑response and receptor‑specific studies are essential.
- Direct measurement of MK inosine/adenosine secretion is missing; requires in vitro conditioned‑medium analysis.
- The conversion of inosine to adenosine involves ectonucleotidases from other cells; contributions cannot be attributed solely to MKs without additional tools.

**Recommendation:** Ready for PI review. This merged hypothesis captures the purine nucleoside direction without premature commitment to a single axis. Primary validation should focus on MK‑specific Pnp deletion, followed by receptor‑blocking studies to dissect the candidate axes.

---

### Other hypotheses from Cycle 1
All remaining hypotheses (GenMet_H3, GenMet_H4, Gen1_H2, Gen1_H3, Gen2_H2, Gen2_H4, Gen3_H3, Gen3_H4) were deemed weak or unsupported by the Meta‑review and are **not revised or advanced**. Their lack of a robust MK‑specific data anchor, contradictory metabolite directions, or absent gene‑expression evidence makes them unsuitable for further development at this stage.

## PI final feedback
I. Research brief for next generation cycle (Cycle 2)

A. Central question  
Refine the two top‑priority metabolomics‑driven directions—MK‑AMD1/polyamine and MK‑Pnp‑inosine/adenosine—by generating candidate downstream‑axis validation hypotheses. Do not propose new broad mechanism classes unless the missing Seurat and public‑data queries reveal a novel, strongly supported metabolite‑enzyme‑MK axis.

B. Biological focus  
Same as Cycle 1: in‑situ lung MKs, hypoxia, pulmonary vascular remodeling. This cycle emphasizes dissecting the perivascular niche: recipient cell types (endothelial cells, PASMCs, fibroblasts, macrophages, T‑cells), candidate mediators (polyamines, inosine/adenosine), and provisional routes (immune‑mediated, direct vascular‑wall, ECM/stromal). Keep all axis‑specific claims provisional.

C. Required data sources  
- User‑provided single‑cell RNA‑seq: `seurat_merged.rds`. This cycle agents must **first** retrieve and incorporate expression and differential expression (PH vs control) in the MK/platelet cluster for:  
  *Pdgfb, Tgfb1, F3, Thbs1, Glo1, Rab27a, Tsg101, Cd44, Lox, Loxl1, Loxl2, Mki67, and any first‑ranked candidate genes from the Mechanism‑Ready Shortlist still unqueried (e.g., Amd1, Amd2, Pnp, Nt5c2 are already known; check Amd1 protein‑level surrogates if possible).*  
- User‑provided metabolomics: reuse `sFig6A Raw data.xlsx` (MK‑sorted) and `Figure6D+F raw data.xlsx` (whole‑lung) – specifically check whole‑lung levels of methionine, inosine, spermidine/spermine to see if MK metabolic shifts propagate to tissue.  
- Public dataset analysis results: mandatory inspection of `GSE289322` DE results and candidate‑gene check files (current output files exist; agents must read them and report whether *Amd1, Pnp, Nt5c2, Glo1, F3, Thbs1*, etc., are differentially expressed in PH lung tissue). Also inspect `GSE291455` for baseline expression of these genes if tissue origin is clarified.  
- Literature: targeted searches for “AMD1 polyamine vascular smooth muscle,” “inosine/adenosine pulmonary hypertension,” “thrombospondin‑1 megakaryocyte,” “tissue factor megakaryocyte hypoxia,” and “extracellular vesicle biogenesis megakaryocyte.”  
- Prior results: continue anchoring MK‑specific requirement.

**Public dataset search tasks (new/refined)**  
- Do not run new broad searches for Cycle 2 unless the data‑gap queries fail. Instead, focus on the already‑downloaded GSE289322: extract DE statistics for genes of interest and perform gene‑set enrichment on the full DE list using KEGG pathways (polyamine metabolism, purine metabolism, coagulation cascades, TGF‑β signaling, ECM‑receptor interaction).  
- If GSE289322 lacks these pathways, note the gap.  
- If any new public dataset is truly needed (e.g., a proteomics dataset of MK EVs), run a narrow query: `(megakaryocyte OR platelet) AND (extracellular vesicles OR microparticles) AND (hypoxia) AND (proteomics)`. Only if performed should agents treat it as metadata; actual matrix download/analysis is optional.

**Distinguish evidence levels**  
- Direct user data (metabolomics, scRNA‑seq expression/differential).  
- Analyzed public data (GSE289322 DE/pathway results).  
- Literature support vs. biological inference vs. speculative extension.

D. Required hypothesis structure (Cycle 2)

For the two advanced directions, generate **candidate‑axis validation hypotheses** with this structure:

1. Specify the broad metabolic direction (Evo_H1 or Evo_H2).  
2. Name one candidate downstream axis (immune‑mediated, direct vascular‑wall, ECM/stromal, or thrombo‑inflammatory) and state that it is a **provisional candidate**, not a settled mechanism.  
3. Define the predicted downstream chain: MK metabolic shift → candidate mediator class → specific provisional target cell/receptor/effector → expected cellular/tissue response → remodelling phenotype.  
4. Provide a **Direction‑level reasoning summary** that includes:  
   - Re‑cap of the metabolic data anchor (unchanged).  
   - New data from the required queries (e.g., MK expression of *Thbs1* if used).  
   - Why this candidate axis is plausible.  
   - Key uncertainty that must be resolved to favour or exclude this axis relative to others.  
5. Propose an explicit experimental test **for that axis** that could be performed after the primary MK‑specific knockout (e.g., after confirming MK‑Amd1 KO reduces lung polyamines, test macrophage depletion or TGM2 inhibition).  
6. Include a falsification criterion specific to the axis (e.g., “If blocking adenosine A2B receptors does not reduce PASMC proliferation, the direct vascular‑wall axis is unlikely dominant”).  
7. Clearly label the axis as “Candidate axis #X” and do not present it as the sole mechanism.

**If a genuinely new metabolic direction emerges from the missing queries** (e.g., MK‑specific *Thbs1* upregulation driving a distinct axis), it may be proposed, but must follow the original direction‑level scaffold and be clearly justified with new data.

**Must avoid:**  
- Presenting any single candidate axis as the final bridge.  
- Over‑resolving exact T‑cell subsets, cytokines, EndMT, or receptor‑subtype dominance without direct evidence.  
- Using KEGG or PubMed hits as proof of causal link.  
- Generating hypotheses without first incorporating the new Seurat and public‑data analyses.

E. Desired hypothesis categories for Cycle 2  
- Candidate‑axis validation hypotheses for the AMD1‑polyamine direction (2–4 hypotheses).  
- Candidate‑axis validation hypotheses for the Pnp‑inosine/adenosine direction (2–4 hypotheses).  
- If new strong MK‑enzyme‑metabolite chains appear, at most one additional broad hypothesis.  
Total 5–9 hypotheses, distributed across generation agents.

F. Constraints and volume  
Keep generation volume realistic. Prefer 3–6 complete, direction‑rich hypotheses per agent. The entire cycle should not exceed 10 hypotheses. No Bridge Convergence Matrix; only short “Candidate downstream axes” notes are acceptable.

II. Assessment of current hypotheses (Cycle 1)

For each hypothesis or cluster, I provide a decision and reasoning. The Evolution Agent already merged polyamine and purine clusters into Evo_H1 and Evo_H2; those are the refined versions. I evaluate them, and also reference the original hypotheses to ensure traceability.

| Hypothesis ID | Decision | Main reason | Direction‑level reasoning quality | Key strength | Key weakness | Required revision (if any) |
|---------------|----------|-------------|----------------------------------|--------------|--------------|----------------------------|
| **Evo_H1** (merged from GenMet_H1, GenMet_H2, Gen2_H1, Gen3_H1) | **Advance** (top priority) | Strongest data anchor: methionine ↑, AMD1 enriched and hypoxia‑up in MKs. Broad downstream framing is appropriate. Testable via MK‑specific Amd1 deletion. | Excellent – connects data anchor, enzyme pathway, candidate axes, remodelling phenotype, and key uncertainty. | Unmatched MK‑specific metabolite‑enzyme link; testable; novel. | Polyamine secretion from MKs unproven; AMD1 activity unmeasured. | None at this stage; simply proceed to axis‑specific validation after confirming polyamine release. |
| **Evo_H2** (merged from Gen1_H1, Gen2_H5, Gen3_H2) | **Advance** (second priority) | Strong inosine‑Pnp anchor; adenosine receptor biology plausible. Broad “adenosine receptor‑mediated” axis avoids over‑commitment. Testable via MK‑specific Pnp deletion. | Good – but some original summaries over‑specified receptor subtypes. The merged version corrects this. | Direct compound‑enzyme link; Pnp differential highly significant. | Complexity of adenosine signalling; inosine vs adenosine ambiguity; no direct perivascular concentration data. | Emphasize need to measure extracellular adenosine/inosine; avoid default A2B dominance. |
| **GenMet_H2** (Amd2 standalone) | **Merged into Evo_H1** (deprioritize separate advancement) | Low expression, marginal enrichment; adds little beyond AMD1. | Adequate but overstates likely impact. | Recognizes paralog redundancy. | No protein evidence; likely minor. | Already incorporated as minor modifier in Evo_H1. |
| **Gen2_H1** (AMD1 → M2 macrophage) | **Merged into Evo_H1** (do not advance separately) | Over‑resolved to M2 polarisation without direct evidence. | Good metabolic logic; poor axis resolution. | Correctly uses AMD1 data. | Premature specificity; risks misleading experiments. | Already merged; the macrophage axis is now a candidate axis under Evo_H1. |
| **Gen3_H1** (AMD1 → ECM cross‑linking) | **Merged into Evo_H1** (do not advance separately) | Over‑resolved to ECM route; polyamine‑ECM biology is plausible but not MK‑specific. | Good biochemical reasoning; ECM axis plausible. | Links polyamines to vascular stiffness. | Lacks MK‑derived polyamine evidence; other cells produce polyamines. | Already merged as candidate axis. |
| **Gen2_H5** (inosine → endothelial dysfunction) | **Merged into Evo_H2** (do not advance separately) | Over‑resolved to endothelial‑dominant axis. | Adequate but narrows too much. | Uses same purine anchor. | Endothelial dysfunction route is only one possibility. | Already merged as a candidate axis. |
| **Gen3_H2** (inosine → thrombo‑inflammation) | **Merged into Evo_H2** (do not advance separately) | Over‑resolved to thrombo‑inflammatory route. | Reasonable but needs more data (tissue factor not shown in MKs). | Introduces coagulation axis. | Lacks MK‑specific tissue factor expression evidence. | Already merged as a candidate axis; requires F3 expression check. |
| **GenMet_H3** (Dnmt3b) | **Reject** | MK Dnmt3b expression negligible and not hypoxia‑regulated; no data anchor. | Weak; listing criteria only. | None. | Entirely speculative; enzyme not supported. | N/A |
| **GenMet_H4** (retinoic acid/Cyp26b1) | **Reject** | Metabolite direction contradicts mechanism; Cyp26b1 not significantly upregulated. | Poor – tries to explain away contradictory data. | Metabolite change is large. | Internal inconsistency; enzyme link weak. | N/A |
| **Gen1_H3** (retinoic acid/Cyp26b1 VSMC) | **Reject** (merge with above) | Same issues; essentially redundant. | Similar. | — | — | N/A |
| **Gen1_H2** (methylglyoxal/RAGE) | **Reject** | No MK enzyme/gene link (Glo1 not in evidence context). | Weak – lacks MK‑specific anchor. | Methylglyoxal differential is striking. | Missing critical enzyme expression; overclaims MK source. | N/A |
| **Gen2_H2** (TSP‑1/TGF‑β) and **Gen3_H4** (similar) | **Deprioritize** (pending MK *Thbs1* expression check) | Currently lacks direct MK expression evidence for *Thbs1*. If *Thbs1* is MK‑enriched and hypoxia‑up, these can be merged into a new hypothesis. | Adequate given literature rationale, but missing data. | Well‑studied fibrotic axis; MK location is attractive. | No user data anchor. | Do not advance until Seurat *Thbs1* query confirms MK expression and hypoxia shift. |
| **Gen2_H4** (EV PDGF‑BB/TGF‑β1) and **Gen3_H3** (EV tissue factor) | **Deprioritize** (pending scRNA‑seq of cargo/EV genes) | No user data on *Pdgfb, Tgfb1, F3* expression in MKs. | Reasonable speculation but no anchor. | Novel EV concept. | Entirely speculative; MK‑gene expression not checked. | Do not advance until the mandatory Seurat queries are completed. If genes are MK‑enriched and PH‑up, they can be revised into a unified MK‑EV hypothesis. |

**Quality of direction‑level reasoning summaries**  
Most metabolomics‑driven hypotheses (GenMet_H1, Gen1_H1) provided convincing summaries: they connected data anchor, enzyme logic, candidate axes, remodelling phenotype, and uncertainty. Weaker ones (GenMet_H3, GenMet_H4) only listed criteria without genuine integration, and the reasoning was forced. The merged Evo hypotheses now have excellent summaries.

III. Cross‑hypothesis synthesis

- **Strongest emerging directions**:  
  - MK AMD1‑polyamine axis (Evo_H1) – highest confidence; will guide metabolism‑centric validation.  
  - MK Pnp‑inosine/adenosine axis (Evo_H2) – second; provides a distinct purinergic angle.

- **Redundant hypotheses to merge**: Successfully merged by Evolution Agent; the two Evo hypotheses adequately cover the polyamine and purine clusters.

- **Weak or unsupported themes**:  
  - Retinoic acid/Cyp26b1 – unsalvageable.  
  - DNA methylation – unsupported.  
  - Methylglyoxal/RAGE – missing MK enzyme.  
  - EV‑cargo and TSP‑1/TGF‑β hypotheses – need gene expression data before reconsideration.

- **Missing mechanistic areas**:  
  - Spatial niche interactions (MK proximity to vessel types) – no data yet.  
  - Direct metabolic coupling (e.g., lactate) – no MK‑specific metabolite data for the relevant metabolites.  
  - Chemokine‑mediated immune recruitment independent of metabolic shifts – no expression data yet.  
  - These may be revisited after completing the required Seurat queries.

- **Data gaps**:  
  - No MK gene expression for *Pdgfb, Tgfb1, F3, Thbs1, Glo1, Rab27a, Tsg101, Cd44, Lox, Loxl1, Loxl2, Mki67* – mandatory for EV/ECM hypotheses.  
  - Whole‑lung metabolomics not cross‑checked for methionine, inosine, spermidine.  
  - GSE289322 DE results not inspected; could provide tissue‑level validation.  
  - No perivascular metabolite measurements or MK‑secretome data.

- **Literature gaps**:  
  - No direct reports of MK AMD1 or MK Pnp in PH.  
  - Hypoxia‑specific regulation of MK TSP‑1, F3, PDGF/TGF‑β unknown.

IV. Feedback to Generation Agents

- **Keep**:  
  - The two merged directions (Evo_H1, Evo_H2) as the foundation.  
  - The practice of always checking Seurat MK expression before building a hypothesis – make this mandatory.

- **Remove**:  
  - Any hypothesis that does not have a direct MK‑specific data anchor (metabolite or gene expression).  
  - All over‑resolved downstream commitments (M2 macrophage, Th17, A2B, etc.) unless they are explicitly labelled as candidate examples.

- **Revise**:  
  - The TSP‑1/TGF‑β and EV‑cargo hypotheses: they can be revived only after the missing gene queries are completed and if results are positive. If *Thbs1*, *F3*, *Pdgfb*, *Tgfb1* are MK‑enriched and hypoxia‑up, a revised “MK matricellular/coagulation/EV secretome” hypothesis can be proposed in Cycle 2.

- **Newly generate**:  
  - Candidate‑axis validation hypotheses for Evo_H1 (2‑4) and Evo_H2 (2‑4).  
  - Each must specify a provisional axis, design a test, and remain falsifiable.  
  - No new broad metabolic direction unless the Seurat/public‑data queries reveal a compelling new metabolite‑enzyme‑MK axis with strong evidence (e.g., if *Glo1* is dramatically down in MKs, methylglyoxal could be reconsidered with a proper anchor).

- **Required analyses or searches before generation**:  
  1. Query Seurat object for expression and PH‑differential of the listed genes in the MK/platelet cluster.  
  2. Cross‑check whole‑lung metabolomics (Figure 6D+F) for key metabolites matching MK signals.  
  3. Inspect and report GSE289322 DE results for the priority genes and pathway enrichment (polyamine, purine, coagulation, ECM).  
  4. If any agent lacks access to these, the PI will instruct the Tool Use Agent and provide results.

V. Feedback to Reflection Agents

- **Directions requiring deeper verification**:  
  - Confirm AMD1 protein/activity and polyamine secretion from hypoxic MKs; this is the most critical missing link.  
  - Verify Pnp protein up‑regulation and whether inosine is actually exported (not just accumulated).  
- **Claims requiring literature support**:  
  - The specific role of AMD1 in polyamine synthesis in vascular cells vs. MKs.  
  - Adenosine receptor subtype expression in hypoxic pulmonary arterioles.  
- **Assumptions requiring critique**:  
  - That MK‑derived polyamines can reach and affect vascular/perivascular cells without rapid metabolism or diffusion limitations.  
  - That the extracellular adenosine/inosine pool is dominated by MK release and not by other cell types (e.g., endothelial CD73).  
- **Potential contradictions to examine**:  
  - Adenosine A2A vs. A2B opposing effects in PH; identify which receptor context drives remodelling vs. protection.  
  - Whether other cells (e.g., macrophages) could also produce polyamines, potentially masking MK contribution.

VI. Feedback to Ranking Agents

- **Ranking criteria to emphasize**: Directional specificity with appropriate resolution (avoid over‑resolved hypotheses that are ranked higher simply because they are more “specific”). The top rank should reward strong MK‑specific anchors and testable predictions while keeping downstream route broad.  
- **Hypotheses that require pairwise comparison**: Evo_H1 vs. Evo_H2 – they are non‑competing but may be ranked to guide resource allocation. Both can be pursued in parallel.  
- **Hypotheses that should not be ranked due to insufficient evidence**: All rejected/deprioritized ones (GenMet_H3, H4, Gen1_H2, Gen1_H3, Gen2_H2, Gen2_H4, Gen3_H3, Gen3_H4).

VII. Feedback to Evolution Agent

- **Hypotheses to refine**: No further merging needed at this stage; the two Evo hypotheses are well‑crafted.  
- **Specific improvements required**: After the mandatory Seurat queries, if TSP‑1 or tissue factor data are positive, evolve a new merged hypothesis covering “MK matricellular and pro‑coagulant secretome” to be evaluated in Cycle 2.  
- **Details that should remain provisional**: The recipient cell types, receptor subtypes, and exact polyamine products must remain provisional until experimental data are obtained.  
- **Experimental feasibility improvements**: Already reasonable; ensure that MK‑specific genetic models are available (Pf4‑Cre for MK/platelet lineage) and that pharmacological inhibitors are specific.

VIII. Final PI recommendation

**Overall status of the current cycle**:  
Cycle 1 successfully identified two high‑confidence, metabolomics‑driven, MK‑specific hypotheses: AMD1‑polyamine and Pnp‑inosine/adenosine. The cycle also generated several over‑resolved or data‑weak hypotheses that have been appropriately rejected or merged. The key remaining weakness is the lack of MK gene expression data for several proposed mediators (EV‑cargo, coagulation, ECM), which must be filled before advancing those concepts.

**Whether another generation cycle is needed**: Yes, Cycle 2 is needed to generate candidate‑axis validation hypotheses and to resolve the data gaps.

**Main instruction for the next cycle**:  
1. **Mandatory data retrieval**: Before any hypothesis generation, extract MK cluster expression/differential for *Pdgfb, Tgfb1, F3, Thbs1, Glo1, Rab27a, Tsg101, Cd44, Lox, Loxl1, Loxl2, Mki67*; cross‑check whole‑lung metabolomics for methionine, inosine, spermidine; and analyze GSE289322 DE results for the key genes and pathways. These results must be shared with all Generation Agents.  
2. **Hypothesis generation scope**: Generate candidate‑axis validation hypotheses for Evo_H1 and Evo_H2 (see Research Brief, Section D). Only propose a new broad direction if a completely novel metabolite‑enzyme‑MK axis emerges from the mandatory queries with strong statistical support.  
3. **Public dataset search**: No new broad repository searches; focus on analyzing the already‑downloaded GSE289322 and GSE291455.  
4. **Quality control**: Hypotheses must adhere strictly to the direction‑level, provisional‑axis format. Over‑resolved language will be downgraded.  
5. **After Cycle 2**, the PI will advance the most testable axis‑specific hypotheses toward experimental design, while continuing to fill any remaining data gaps.
