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
