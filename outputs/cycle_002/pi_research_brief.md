PI_TO_GENERATION_BRIEF

Cycle ID:  
2

Central question:  
Refine the two top‑priority metabolomics‑driven directions—MK‑AMD1/polyamine and MK‑Pnp‑inosine/adenosine—by generating candidate downstream‑axis validation hypotheses. Do not propose new broad mechanism classes unless the mandatory Seurat and public‑data queries reveal a novel, strongly supported metabolite‑enzyme‑MK axis.

Biological focus:  
In‑situ lung megakaryocytes, hypoxia exposure, pulmonary vascular remodeling.  
Perivascular niche dissection: recipient cell types (endothelial cells, PASMCs, fibroblasts, macrophages, T‑cells), candidate mediators (polyamines, inosine/adenosine), and provisional routes (immune‑mediated, direct vascular‑wall, ECM/stromal, thrombo‑inflammatory). All axis‑specific claims must remain **provisional**.

Data sources to prioritize:

- **User‑provided single‑cell RNA‑seq** (seurat_merged.rds):  
  **Before generating any hypothesis**, each agent must retrieve and incorporate expression and differential expression (PH vs control) in the MK/platelet cluster for the following genes:  
  *Pdgfb, Tgfb1, F3, Thbs1, Glo1, Rab27a, Tsg101, Cd44, Lox, Loxl1, Loxl2, Mki67*.  
  Also check any still‑unqueried first‑ranked candidate genes from the Mechanism‑Ready Shortlist (e.g., *Amd1*, *Amd2*, *Pnp*, *Nt5c2* are known; verify Amd1 protein‑level surrogates if possible).  
  Results must be shared as a common evidence base for all downstream candidates.

- **User‑provided metabolomics**:  
  Reuse `sFig6A Raw data.xlsx` (MK‑sorted) and `Figure6D+F raw data.xlsx` (whole‑lung). Specifically, cross‑check whole‑lung levels of methionine, inosine, spermidine/spermine to determine whether MK metabolic shifts propagate to tissue. If these measurements are absent, note the gap.

- **Public dataset analysis results** (mandatory):  
  Analyze already‑downloaded `GSE289322` differential expression results and candidate‑gene check files. Extract DE statistics for the full gene list above and for any high‑readiness metabolic genes. Perform gene‑set enrichment on the full DE list using KEGG pathways: arginine/proline metabolism (polyamine context), cysteine/methionine metabolism, purine metabolism, coagulation cascades, TGF‑β signaling, and ECM‑receptor interaction. Report enrichment scores and FDR.  
  If GSE289322 lacks these pathways or fails to show relevant enrichment, explicitly note the gap.  
  Also inspect `GSE291455` for baseline expression of the same genes, but only after clarifying the tissue/cell context from its metadata.

- **Literature**:  
  Targeted searches for “AMD1 polyamine vascular smooth muscle,” “inosine/adenosine pulmonary hypertension,” “thrombospondin‑1 megakaryocyte,” “tissue factor megakaryocyte hypoxia,” and “extracellular vesicle biogenesis megakaryocyte.”

- **Prior results** (prior_results.docx):  
  Continue anchoring the lung‑resident MK requirement for pathogenic remodeling.

Public dataset search tasks:  
The following tasks are assigned to the Public Dataset Discovery Module for this cycle. Do not run new broad searches unless results are missing; focus on the already‑retrieved GSE289322 and GSE291455, with one narrow proteomics query if justified.

1. Extract differential expression statistics from **GSE289322** for the MK‑candidate gene set: *Pdgfb, Tgfb1, F3, Thbs1, Glo1, Rab27a, Tsg101, Cd44, Lox, Loxl1, Loxl2, Mki67, Amd1, Amd2, Pnp, Nt5c2*. Provide log2FC, p‑value, and adjusted p‑value (if available).  
2. Perform GSEA on the full GSE289322 DE list using the following KEGG gene sets:  
   - Arginine and proline metabolism (polyamine pathway context)  
   - Cysteine and methionine metabolism  
   - Purine metabolism  
   - Coagulation cascades  
   - TGF‑beta signaling pathway  
   - ECM‑receptor interaction  
   Report normalized enrichment scores, nominal p‑values, and FDR. If none of the pathways show significant enrichment (FDR < 0.25), note that the tissue‑level transcriptome does not support the hypothesized axes.  
3. Inspect **GSE291455** metadata to confirm tissue/organ of origin. If it is lung‑derived, extract baseline expression values for the same gene list.  
4. Only if the above analyses fail to provide proteomics insight into MK‑derived vesicles: execute a narrow repository query `(megakaryocyte OR platelet) AND (extracellular vesicles OR microparticles) AND (hypoxia) AND (proteomics)` in ProteomeXchange/PRIDE/MassIVE. Retrieve dataset accession and metadata; actual matrix download is optional.

Distinguish evidence levels:  
- **Direct user data** (MK metabolomics, scRNA‑seq expression/differential)  
- **Analyzed public data** (GSE289322 DE/pathway results)  
- **Literature support** vs. **biological inference** vs. **speculative extension**

Required hypothesis categories:

- **Candidate‑axis validation hypotheses for the AMD1‑polyamine direction (Evo_H1)**: 2–4 hypotheses  
- **Candidate‑axis validation hypotheses for the Pnp‑inosine/adenosine direction (Evo_H2)**: 2–4 hypotheses  
- If the mandatory Seurat/public‑data queries reveal a **novel, strongly supported metabolite‑enzyme‑MK axis** (e.g., MK‑enriched and hypoxia‑up *Thbs1* triggering a distinct matricellular or coagulation axis), at most **one additional broad hypothesis** following the original direction‑level scaffold.  

Total hypotheses for the entire cycle: **5–9**, distributed across generation agents. Each agent should produce 3–6 complete, direction‑rich hypotheses.

Must include (for each hypothesis):

- MK‑specific mechanism (initiating change in hypoxic lung MKs).  
- Hypoxia‑dependent trigger.  
- Defined mediator class, pathway class, or metabolic axis (polyamine metabolism, purine/adenosine signaling, etc.).  
- A **candidate downstream axis** (immune‑mediated, direct vascular‑wall, ECM/stromal, thrombo‑inflammatory, EV‑mediated, or unresolved) – explicitly provisional.  
- A predicted downstream chain: hypoxic MK metabolic shift → candidate mediator class → provisional specific target cell/receptor/effector example → expected cellular/tissue response → broad vascular remodeling phenotype (muscularization, medial thickening, stiffness, endothelial dysfunction).  
- A **Direction‑level reasoning summary** linking: direct data anchor, biological interpretation, MK‑linked enzyme/pathway logic, plausible downstream axis, remodeling phenotype, and the key uncertainty that could overturn the axis choice.  
- A **testable experimental prediction** that can be performed after a primary MK‑specific knockout (e.g., conditional *Amd1*‑KO in Pf4‑Cre strain).  
- A **falsification criterion** specific to the candidate axis (e.g., “If blocking adenosine A2B receptors does not reduce PASMC proliferation, the direct vascular‑wall axis is unlikely dominant”).  
- Label each hypothesis with “Candidate axis #” and do not present any single axis as the sole mechanism.  
- Provide a short **“candidate downstream axes” note** naming 2–4 plausible routes and marking which one is provisionally emphasized as a working model.

Must avoid:  
- Generic inflammation‑only hypotheses.  
- Gene‑list‑only outputs.  
- Unsupported causal claims.  
- Hypotheses lacking MK specificity (initiation must be MK‑enriched and hypoxia‑responsive).  
- Hypotheses lacking hypoxia specificity.  
- Hypotheses lacking vascular remodeling relevance.  
- Redundant hypotheses already covered by Evo_H1 and Evo_H2.  
- Mechanisms that are not experimentally testable.  
- **Over‑resolving exact mediators, T‑cell subsets, cytokines, receptor subtypes, EndMT, or recipient cell types** when evidence only supports a broader direction. Any such specification must be explicitly labeled as “candidate example” and not as the settled mechanism.  
- Using KEGG or PubMed hits as proof of causal linkage.  
- Generating hypotheses **before** incorporating the mandatory Seurat and public‑data analyses.  
- Exceeding the allowed volume: no more than 9 hypotheses total.

Feedback from previous cycle:  
- **Keep:** The two merged directions (Evo_H1: MK‑AMD1‑polyamine; Evo_H2: MK‑Pnp‑inosine/adenosine) as the sole foundation for candidate‑axis generation. The practice of always checking Seurat MK expression before building a hypothesis – make it mandatory.  
- **Remove:** Any hypothesis that does not have a direct MK‑specific data anchor (metabolite elevation + enzyme expression/enrichment). All over‑resolved downstream commitments (M2 macrophage, Th17, A2B, etc.) unless they are explicitly labelled as candidate examples.  
- **Revise:** The TSP‑1/TGF‑β and EV‑cargo hypotheses can be revived **only after** the mandatory Seurat queries are completed and if results are positive. If *Thbs1*, *F3*, *Pdgfb*, *Tgfb1* are MK‑enriched and hypoxia‑up, a revised “MK matricellular/coagulation/EV secretome” hypothesis may be proposed in this cycle, but it must follow the same direction‑level scaffold and not default to a single axis.  
- **Newly generate:** Candidate‑axis validation hypotheses for Evo_H1 (2–4) and Evo_H2 (2–4). No new broad metabolic direction **unless** the mandatory queries reveal a compelling new metabolite‑enzyme‑MK axis with strong statistical support (e.g., MK‑specific *Glo1* downregulation bringing back methylglyoxal with a proper anchor).

Expected output:  
Each agent must produce between 3 and 6 complete hypotheses following the required structure. The whole cycle will include 5–9 hypotheses. Each hypothesis must be presented with:

- Hypothesis ID (e.g., Axis1_AMD1_immune)  
- Metabolic direction anchor (Evo_H1 or Evo_H2)  
- Candidate axis label (provisional)  
- Predicted chain (direction‑level, with one candidate example)  
- Direction‑level reasoning summary  
- Candidate downstream axes note (2–4 routes, with one marked as working model)  
- Experimental test proposal with falsification criterion  
- Evidence level breakdown (user data, public data, literature, inference, speculation)

**Metabolomics‑driven emphasis:** At least 4 of the submitted hypotheses must originate from the metabolic shortlist chains (AMD1‑polyamine and Pnp‑inosine). They must follow the chain: differential metabolite → KEGG direct or same‑pathway enzyme/gene → candidate gene with MK expression/enrichment/differential → directional downstream biology → vascular remodeling phenotype. Do not force a fully resolved multi‑hop mechanism; stop at the directional axis.

Agents should use the **Mechanism‑Ready Hypothesis Shortlist** as the authoritative source for metabolic anchors and not allow previous‑cycle named priorities to override shortlist rows with positive MK enrichment, PH‑up MK shift, and non‑generic mechanism cues. The metabolic generation agent must explicitly reference the shortlist ranks and readiness scores when selecting chains.
