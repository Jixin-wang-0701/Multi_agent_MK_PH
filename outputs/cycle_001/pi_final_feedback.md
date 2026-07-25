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
