Cycle ID: 2

Hypotheses generated: 5 (Axis1_AMD1_immune, Axis1_AMD1_ECM_niche, Axis1_AMD1_thrombo, Axis2_Pnp_immune, Axis2_Pnp_stromal).  
Each hypothesis aligned with the metabolic shortlist/Evo directions, with emphasis on thrombo-inflammatory, ECM, immune remodeling, and spatial niche mechanisms. All downstream axes are kept provisional; no single bridge is forced.

---

### Hypothesis ID: Axis1_AMD1_immune
**Hypothesis title:** MK-AMD1/polyamine promotes perivascular immune remodeling and medial thickening  
**PI instruction addressed:** Refine Evo_H1 (MK-AMD1‑polyamine) by generating a candidate downstream‑axis validation hypothesis with an immune‑mediated direction.  
**Core directional hypothesis:** Hypoxic upregulation of AMD1 in lung‑resident MKs shifts the perivascular polyamine milieu, biasing local T‑cell/macrophage phenotypes toward a pro‑remodeling state that sustains muscularization and vascular thickening.  
**Direction‑level reasoning summary:**  
- **Data anchor:** Methionine is elevated in PH MKs (log2FC 3.26, sFig6A). Amd1 is MK‑enriched (log2 enrichment 1.35, 31.4% MK+ vs 14.9% other) and significantly upregulated in PH MKs (log2FC 1.77, p=6.55e‑06, Wilcoxon). The KEGG link is through cysteine/methionine metabolism and arginine/proline metabolism to polyamine (spermidine/spermine) synthesis.  
- **Biological interpretation:** AMD1 decarboxylates S‑adenosylmethionine, a rate‑limiting step for polyamine production. Increased AMD1 activity in hypoxic MKs would raise local spermidine/spermine. Polyamines can be exported and taken up by bystander cells, or modulate immune cell function intracellularly if MK‑derived extracellular vesicles (EVs) are taken up. Literature shows polyamines shape T‑cell differentiation (e.g., promoting Th17‑like responses in some contexts) and macrophage polarization; the link to vascular remodeling in PH is indirect.  
- **Candidate downstream axis:** Immune‑mediated, with a provisional working model that MK‑derived polyamines influence perivascular T‑cell or macrophage activation, promoting a low‑grade inflammatory loop that drives PASMC proliferation and medial thickening.  
- **Remodeling logic:** Perivascular immune cell accumulation and activation (as seen in PH) facilitates vascular muscularization; polyamines could function as metabolic signals that sustain this niche.  
- **Key uncertainty:** Whether polyamines from MKs reach biologically meaningful concentrations in the perivascular space, and whether they act primarily on Th17‑like cells, macrophages, or both. No direct data show polyamine‑driven immune polarization in the PH lung.  

**Directional chain:**  
1. Hypoxia induces AMD1 expression in lung‑resident MKs.  
2. MK AMD1 activity increases polyamine (spermidine/spermine) synthesis and/or release.  
3. Polyamines act as intercellular signals on perivascular immune cells (T‑cells, macrophages) to shift activation state.  
4. Altered immune cell function sustains PASMC proliferation and medial thickening.  
5. Contributes to hypoxia‑induced pulmonary vascular muscularization and hemodynamic deterioration.  

**Candidate downstream axes:**  
- **Plausible axes:** (i) Immune‑mediated via T‑helper/Th17‑like tone; (ii) Macrophage/monocyte reprogramming toward a pro‑fibrotic phenotype; (iii) combined immune‑stromal crosstalk.  
- **Working model (provisional):** MK‑exported spermidine promotes a Th17‑biased perivascular response, which stimulates PASMC growth.  
- **What remains unresolved:** The exact immune cell subset(s) mediating polyamine effects, the receptors/transporters involved, and whether the effect requires direct cell contact or soluble mediators.  

**Evidence basis:**  
- **User‑provided data:** MK‑sorted metabolomics (methionine up); single‑cell RNA‑seq showing MK enrichment and PH‑up of Amd1.  
- **Public dataset metadata or analyzed public data:** GSE289322 GSEA for KEGG “Arginine and proline metabolism” (polyamine context) may support tissue‑level pathway dysregulation; actual enrichment statistics unavailable in this cycle but analysis completed and can be checked.  
- **Literature:** AMD1‑polyamine axis is linked to immune cell function (e.g., spermidine influences Th17 differentiation in autoimmune models; polyamines affect macrophage polarization). No direct PH studies found.  
- **Biological rationale:** Metabolic competition for S‑adenosylmethionine between methylation and polyamine synthesis can shift cell state; polyamines are known immunomodulators.  
- **Evidence status:** Direct (MK metabolomics, MK scRNA‑seq) → inferred (polyamine‑immune link) → speculative (perivascular immune remodeling in PH).  

**Predicted observations:**  
- **In MKs:** Increased spermidine/spermine upon ex vivo hypoxia or in Amd1‑overexpressing MKs.  
- **In recipient or tissue compartment:** Perivascular accumulation of activated CD4+ T‑cells (potentially IL‑17‑producing) or pro‑fibrotic macrophages in hypoxic lungs; normalized in Amd1‑cKO animals.  
- **In metabolomics or pathway activity:** Elevated spermidine in whole‑lung or bronchial lavage of PH mice, reduced upon MK‑specific Amd1 deletion.  

**Experimental validation:**  
- **Perturbation:** Conditional Amd1 knockout in MK/platelet lineage (Pf4‑Cre; Amd1^(fl/fl)).  
- **Model:** Hypoxia‑induced PH in mice.  
- **Readout:** Perivascular immune cell composition (flow cytometry, IF for T‑cell/macrophage markers), pulmonary vascular muscularization (α‑SMA morphometry), spermidine/spermine in lung tissue.  
- **Expected result:** cKO mice show reduced perivascular activated T‑cells/macrophages, decreased muscularization, and lower local polyamine levels.  
- **Falsifying result:** No change in perivascular immune infiltrate or cytokine profile despite successful Amd1 deletion and polyamine reduction; or immune cell depletion does not attenuate remodeling.  

**Novelty:** First link between MK‑intrinsic polyamine metabolism and adaptive/innate immune shaping in pulmonary vascular remodeling.  
**Weaknesses:** No direct demonstration that MK‑derived polyamines reach immune cells at functional concentrations; immune axis may be secondary to other non‑immune effects.  
**Priority estimate:**  
- Directional specificity: 4  
- Data support: 4  
- Literature support: 3  
- Novelty: 5  
- Testability: 4  
- Overall generation priority: 4  

---

### Hypothesis ID: Axis1_AMD1_ECM_niche
**Hypothesis title:** MK‑AMD1/polyamine fuels ECM cross‑linking and vascular stiffness via perivascular niche reprogramming  
**PI instruction addressed:** Refine Evo_H1 with a candidate ECM/stromal downstream axis emphasizing spatial niche mechanisms.  
**Core directional hypothesis:** AMD1‑driven polyamine production in hypoxic MKs enhances extracellular matrix (ECM) cross‑linking and fibroblast/pericyte activation in the perivascular niche through soluble polyamines or polyamine‑loaded extracellular vesicles, directly contributing to medial stiffness and thickened vascular walls.  
**Direction‑level reasoning summary:**  
- **Data anchor:** Same Amd1 evidence as above; polyamine metabolism is closely tied to ECM regulation—spermidine is a substrate for transglutaminases that cross‑link ECM proteins, and polyamine availability can influence lysyl oxidase (LOX) activity indirectly. While MK intrinsic expression of ECM‑modifying genes (Lox, Loxl1, Loxl2) remains to be confirmed by the mandatory Seurat query, activated MKs are known sources of extracellular vesicles (EVs) that can transfer bioactive cargo to fibroblasts.  
- **Biological interpretation:** Elevated AMD1 in hypoxic MKs raises intracellular spermidine, which may be packaged into exosomes/EVs (Rab27a‑, Tsg101‑dependent) and delivered to adventitial fibroblasts or pericytes. Polyamines might also be secreted directly and taken up by these cells. There, they could promote cross‑linking enzyme activity or directly stabilize collagen, increasing vascular stiffness and promoting a synthetic/activated smooth muscle phenotype.  
- **Candidate downstream axis:** EV‑mediated stromal remodeling or direct ECM cross‑linking. Working model: MK‑derived EVs transport spermidine (and perhaps other polyamines) to perivascular fibroblasts, elevating transglutaminase‑mediated collagen cross‑linking and LOX expression, leading to medial stiffness.  
- **Remodeling logic:** Increased ECM stiffness is a hallmark of pulmonary hypertension; MK‑mediated metabolic niche modulation could explain how hypoxia shifts the perivascular matrix independent of platelet‑derived growth factors.  
- **Key uncertainty:** Whether polyamines in MK‑EVs are sufficient to alter fibroblast ECM output, and whether LOX family genes are indeed MK‑enriched and hypoxia‑responsive.  

**Directional chain:**  
1. Hypoxia upregulates AMD1 in lung MKs.  
2. MKs produce spermidine/spermine, potentially enriched in EVs (requiring Tsg101/Rab27a).  
3. EVs or secreted polyamines act on perivascular fibroblasts/pericytes.  
4. Fibroblasts increase ECM cross‑linking (via transglutaminase/LOX) and transition to a contractile/myofibroblast phenotype.  
5. Medial thickness and vascular stiffness increase, contributing to hemodynamic stress.  

**Candidate downstream axes:**  
- **Plausible axes:** (i) EV‑cargo delivery to fibroblasts; (ii) direct polyamine transport into vascular smooth muscle cells; (iii) polyamine‑driven stabilization of ECM components.  
- **Working model (provisional):** EV‑borne spermidine activates fibroblast transglutaminase, stiffening the perivascular matrix.  
- **What remains unresolved:** Reliance on unknown MK expression of EV biogenesis markers and ECM‑modifying enzymes; must be confirmed by the mandatory Seurat query.  

**Evidence basis:**  
- **User‑provided data:** Metabolomics and scRNA‑seq for Amd1 (direct). No data yet on LOX family, Rab27a, Tsg101 in MKs; these are pending the current cycle’s mandatory query.  
- **Public dataset metadata or analyzed public data:** GSE289322 ECM‑receptor interaction pathway enrichment, if significant, would support tissue‑level ECM dysregulation; results pending review.  
- **Literature:** Polyamines (spermidine) are substrates for transglutaminase‑mediated cross‑linking; LOX activity can be influenced by polyamine‑dependent eIF5A hypusination. EV release from MKs is a known phenomenon (platelet microparticles).  
- **Biological rationale:** Metabolic niche crosstalk between MKs and fibroblasts is plausible given their perivascular proximity.  
- **Evidence status:** Direct (Amd1 MK data) → inferred (polyamine‑ECM link) → speculative (EV‑mediated transfer).  

**Predicted observations:**  
- **In MKs:** Co‑enrichment of EV markers (Tsg101, Rab27a, CD63) and LOX family genes upon hypoxia, if the mandatory Seurat check is positive.  
- **In recipient or tissue compartment:** Increased collagen cross‑links (hydroxyproline, pyridinoline) and LOX activity in hypoxic lung tissue; reduced in Amd1‑cKO mice.  
- **In metabolomics or pathway activity:** Polyamine content in isolated lung EVs elevated in PH.  

**Experimental validation:**  
- **Perturbation:** MK‑specific Amd1 KO (Pf4‑Cre).  
- **Model:** Hypoxic PH mouse; additionally, isolation of MK‑derived EVs for functional assays on fibroblasts.  
- **Readout:** Fibroblast activation (α‑SMA, collagen I), ECM stiffness (atomic force microscopy), LOX activity, and spermidine content in recipient fibroblasts after EV uptake.  
- **Expected result:** Amd1‑KO derived EVs fail to activate fibroblasts, and lung ECM stiffness is reduced.  
- **Falsifying result:** No difference in EV polyamine content or fibroblast activation despite Amd1 deletion; or ECM cross‑linking unchanged.  

**Novelty:** Links MK metabolic state to ECM stiffness via polyamine‑EV axis, a spatial niche mechanism.  
**Weaknesses:** Requires positive expression data for EV machinery and ECM‑modifying genes in MKs; EV isolation and functional assignment are technically challenging.  
**Priority estimate:**  
- Directional specificity: 3 (EV route needs confirmation)  
- Data support: 3 (Amd1 solid; EV/ECM genes unknown)  
- Literature support: 3  
- Novelty: 5  
- Testability: 3  
- Overall generation priority: 3  

---

### Hypothesis ID: Axis1_AMD1_thrombo
**Hypothesis title:** MK‑AMD1/polyamine activates thrombo‑inflammatory remodeling via coagulation factor expression and platelet‑like microparticle release  
**PI instruction addressed:** Generate a thrombo‑inflammatory candidate downstream axis for Evo_H1.  
**Core directional hypothesis:** AMD1 upregulation in hypoxic MKs alters polyamine‑dependent eIF5A hypusination and translation of coagulation/platelet activators (e.g., tissue factor F3, thrombospondin‑1 Thbs1), promoting local microthrombosis and thrombo‑inflammatory signals that worsen vascular muscularization and obliteration.  
**Direction‑level reasoning summary:**  
- **Data anchor:** Amd1 MK enrichment/PH‑up as above; polyamine pathway is linked to hypusination of eIF5A, a translation factor that controls synthesis of specific proteins, including some involved in coagulation. The mandatory Seurat query for F3 and Thbs1 is pending; if these are MK‑enriched and hypoxia‑up, the hypothesis gains strong support.  
- **Biological interpretation:** AMD1 activity ultimately drives the synthesis of spermidine, which is essential for hypusination of eIF5A. Hypusinated eIF5A facilitates translation of mRNAs with specific motifs, potentially including F3 (tissue factor) and Thbs1. Increased tissue factor on MK‑derived particles or platelets could initiate local fibrin deposition and microvascular thrombosis, known to occur in PH. Thrombospondin‑1 can activate latent TGF‑β, creating a pro‑remodeling feed‑forward loop.  
- **Candidate downstream axis:** Thrombo‑inflammatory, with local coagulation and TGF‑β activation driving smooth muscle hypertrophy.  
- **Remodeling logic:** Microthrombi and persistent thrombo‑inflammation are pathological features of PH; MK‑intrinsic metabolic reprogramming could be a proximate cause.  
- **Key uncertainty:** Whether F3 and Thbs1 are truly MK‑enriched and PH‑responsive, and whether polyamine flux controls their expression post‑transcriptionally via eIF5A.  

**Directional chain:**  
1. Hypoxia increases AMD1 in lung MKs.  
2. Elevated spermidine drives eIF5A hypusination, enhancing translation of pro‑coagulant/platelet‑activating proteins (F3, Thbs1).  
3. MKs or their derived microparticles display higher tissue factor activity and thrombospondin‑1 release.  
4. Local thrombin generation and thrombospondin‑1‑mediated TGF‑β activation promote PASMC proliferation and matrix deposition.  
5. Small‑vessel obliteration and medial thickening accelerate.  

**Candidate downstream axes:**  
- **Plausible axes:** (i) Thrombo‑inflammatory via tissue factor/fibrin; (ii) TGF‑β‑mediated muscularization via thrombospondin‑1; (iii) combined coagulation‑immune crosstalk.  
- **Working model (provisional):** Polyamine‑dependent tissue factor expression on MK microparticles triggers perivascular microthrombosis and smooth muscle hypertrophy.  
- **What remains unresolved:** Direct evidence for F3/Thbs1 MK expression and their regulation by AMD1.  

**Evidence basis:**  
- **User‑provided data:** Metabolomics and scRNA‑seq for Amd1 (direct). F3, Thbs1, and coagulation‑relevant genes not yet queried.  
- **Public dataset metadata or analyzed public data:** GSE289322 KEGG “Coagulation cascades” enrichment could indicate tissue‑level thrombosis pathway activation; pending inspection.  
- **Literature:** Polyamine‑dependent hypusination of eIF5A controls translation of a subset of mRNAs; some studies link polyamine metabolism to tissue factor expression in cancer cells. Thrombospondin‑1 is a known MK product and modulates TGF‑β in vascular disease.  
- **Biological rationale:** MKs are the source of most circulating tissue factor and thrombospondin‑1; metabolic reprogramming could alter their release.  
- **Evidence status:** Direct (Amd1 pathway) → indirect (eIF5A hypusination) → speculative (F3/Thbs1 upregulation and thrombo‑inflammatory effect).  

**Predicted observations:**  
- **In MKs:** Co‑localization of AMD1 expression with increased tissue factor protein and Thbs1 mRNA in hypoxic MKs; elevated hypusinated eIF5A.  
- **In recipient or tissue compartment:** Enhanced perivascular fibrin deposition and microthrombi in lungs of hypoxic mice; reduced in Amd1‑cKO.  
- **In metabolomics or pathway activity:** Correlation between spermidine levels and thrombin‑antithrombin complexes in bronchoalveolar lavage.  

**Experimental validation:**  
- **Perturbation:** Conditional Amd1 KO (Pf4‑Cre).  
- **Model:** Hypoxic PH; also, MK‑derived microparticle isolation and functional thrombin generation assay.  
- **Readout:** Tissue factor activity on MK microparticles, lung fibrin(ogen) immunostaining, TGF‑β/Smad2 activation, and vascular muscularization.  
- **Expected result:** cKO mice show reduced tissue factor activity, less fibrin deposition, and attenuated TGF‑β signaling/vascular remodeling.  
- **Falsifying result:** No change in F3/Thbs1 expression or microparticle procoagulant activity despite Amd1 deletion; or pharmacological blockade of tissue factor/TGF‑β does not ameliorate remodeling.  

**Novelty:** Connects MK metabolic reprogramming directly to thrombo‑inflammation via polyamine‑eIF5A axis.  
**Weaknesses:** Heavily dependent on pending Seurat data; the polyamine‑eIF5A‑F3 link is not yet established in MKs.  
**Priority estimate:**  
- Directional specificity: 4  
- Data support: 2 (Amd1 solid; coagulation genes unknown)  
- Literature support: 3  
- Novelty: 5  
- Testability: 4  
- Overall generation priority: 3  

---

### Hypothesis ID: Axis2_Pnp_immune
**Hypothesis title:** MK‑Pnp/inosine/adenosine shapes perivascular immune suppression that permits unchecked medial remodeling  
**PI instruction addressed:** Refine Evo_H2 (MK‑Pnp‑inosine/adenosine) with an immune‑mediated candidate downstream axis.  
**Core directional hypothesis:** Hypoxic upregulation of Pnp in lung MKs increases local inosine/adenosine generation, which signals through adenosine receptors on perivascular T‑cells and macrophages to create an immunosuppressive niche, blunting protective anti‑remodeling immunity and allowing PASMC hyperplasia and muscularization.  
**Direction‑level reasoning summary:**  
- **Data anchor:** Inosine is elevated in PH MKs (log2FC 3.82, sFig6A). Pnp is MK‑expressed (20.3% MK+ vs 38.9% other, but log2 enrichment negative; however PH‑vs‑control MK log2FC 1.739, p=3.81e‑06, indicating strong hypoxia‑induced upregulation in MKs). Nt5c2 also upregulated in PH MK (log2FC 2.879, p=2e‑04). Together, Pnp and Nt5c2 can generate inosine from adenosine or IMP, and can also generate adenosine under certain conditions. Extracellular inosine/adenosine is a potent immunosuppressant, acting on A2A/A2B receptors to inhibit effector T‑cell function and promote regulatory phenotypes.  
- **Biological interpretation:** In PH, perivascular immune cells often fail to adequately resolve vascular remodeling. MK‑derived nucleosides could contribute to this failure by suppressing local T‑cell and macrophage activation. This is not generic inflammation but a specific metabolic checkpoint that paralyzes the beneficial immune response.  
- **Candidate downstream axis:** Immune‑mediated suppression (provisional).  
- **Remodeling logic:** Without active immune surveillance, stress signals from endothelial or smooth muscle cells are not counteracted, allowing unopposed PASMC proliferation and ECM deposition.  
- **Key uncertainty:** Whether MK‑derived inosine/adenosine reaches sufficient concentrations to affect immune cells in the perivascular niche, and which receptors (A2B on macrophages, A2A on T‑cells) dominate in PH lung.  

**Directional chain:**  
1. Hypoxia upregulates Pnp and Nt5c2 in lung MKs, enhancing inosine production.  
2. MKs release inosine (and potentially adenosine) into the perivascular microenvironment.  
3. Elevated nucleosides engage adenosine receptors on perivascular T‑cells/macrophages, suppressing effector functions and promoting regulatory/tolerogenic phenotypes.  
4. Immune‑mediated vascular repair is impaired; pro‑remodeling signals from injured endothelium/SMCs are unchecked.  
5. Progressive medial thickening and muscularization ensue.  

**Candidate downstream axes:**  
- **Plausible axes:** (i) Immune‑mediated suppression via adenosine A2B receptor on macrophages; (ii) A2A‑mediated T‑cell anergy; (iii) combined purinergic signaling on fibroblasts that also attracts suppressive immune cells.  
- **Working model (provisional):** Pnp‑generated adenosine/inosine acts on perivascular myeloid cells to suppress IL‑12/IFNγ and promote a pro‑fibrotic profile, weakening anti‑remodeling immunity.  
- **What remains unresolved:** Characterization of the perivascular immune receptor expression and which nucleoside (inosine vs adenosine) is the dominant mediator.  

**Evidence basis:**  
- **User‑provided data:** Metabolomics (inosine up); scRNA‑seq for Pnp and Nt5c2 (MK‑enriched in PH MKs).  
- **Public dataset metadata or analyzed public data:** GSE289322 purine metabolism pathway enrichment, if significant, supports tissue‑level nucleoside pathway activation; pending review.  
- **Literature:** Adenosine/Inosine signaling via A2B on macrophages promotes IL‑10 and tissue fibrosis; A2A on T‑cells inhibits effector function. No direct PH‑MK link found but plausible.  
- **Biological rationale:** MKs are positioned in the perivascular niche and can deliver high local concentrations of small molecules.  
- **Evidence status:** Direct (MK metabolomics, Pnp upregulation) → inferred (inosine‑immune axis) → speculative (immune suppression in PH).  

**Predicted observations:**  
- **In MKs:** Concurrent elevation of Pnp enzyme activity and inosine in conditioned media of hypoxic MKs.  
- **In recipient or tissue compartment:** Increased lung inosine/adenosine and A2B/A2A activation in immune cells; immune cells adopt a regulatory/suppressed phenotype (low IFNγ, high IL‑10).  
- **In metabolomics or pathway activity:** Correlation between lung inosine and T‑cell exhaustion markers.  

**Experimental validation:**  
- **Perturbation:** Conditional Pnp KO in MK lineage (Pf4‑Cre).  
- **Model:** Hypoxic PH.  
- **Readout:** Perivascular immune cell profiling (flow cytometry, cytokine multiplex), vascular muscularization.  
- **Expected result:** Pnp‑cKO mice show restored perivascular effector T‑cell/macrophage activity, reduced IL‑10, and attenuated vascular remodeling.  
- **Falsifying result:** No alteration in immune cell activation or remodeling despite successful Pnp deletion; or adenosine receptor blockade does not reverse immunosuppression.  

**Novelty:** First proposal that MK‑derived purine nucleosides create an immunosuppressive perivascular niche in PH.  
**Weaknesses:** Inosine may predominantly act after conversion to adenosine; the cell‑type specificity of purinergic signaling is unresolved.  
**Priority estimate:**  
- Directional specificity: 4  
- Data support: 4  
- Literature support: 3  
- Novelty: 5  
- Testability: 4  
- Overall generation priority: 4  

---

### Hypothesis ID: Axis2_Pnp_stromal
**Hypothesis title:** MK‑Pnp/inosine/adenosine directly drives PASMC proliferation and fibroblast‑mediated ECM deposition  
**PI instruction addressed:** Refine Evo_H2 with a candidate direct vascular‑wall/ECM downstream axis.  
**Core directional hypothesis:** Inosine/adenosine generated by hypoxic MKs via Pnp act directly on perivascular smooth muscle cells and fibroblasts through adenosine receptors (primarily A2B) to stimulate proliferation, migration, and ECM production, thereby contributing to medial hypertrophy and wall stiffness.  
**Direction‑level reasoning summary:**  
- **Data anchor:** Same inosine elevation and Pnp upregulation. Adenosine receptors, particularly A2B, are expressed on PASMCs and fibroblasts and can couple to Gs‑protein/adenylyl cyclase and also to MAPK pathways, promoting cell growth and collagen synthesis. Literature shows adenosine A2B receptor activation can drive pulmonary hypertension in animal models, but the source of adenosine was not defined.  
- **Biological interpretation:** MK‑derived inosine can be converted to adenosine by ecto‑enzymes (CD73) on the surface of endothelial cells or fibroblasts, or directly act on adenosine receptors. Local adenosine delivery by perivascular MKs provides a sustained proliferative signal to adjacent mesenchymal cells, bypassing the need for systemic nucleoside elevation.  
- **Candidate downstream axis:** Direct vascular‑wall (PASMC) and ECM/stromal (fibroblast).  
- **Remodeling logic:** PASMC hyperplasia and adventitial fibrosis are key components of vascular remodeling in PH; a direct MK‑to‑mesenchyme purinergic signal would tightly link hypoxia sensing to structural changes.  
- **Key uncertainty:** Whether PASMCs/fibroblasts in the hypoxic lung express the relevant adenosine receptor subtypes and whether inosine or adenosine is the primary ligand.  

**Directional chain:**  
1. Hypoxia upregulates Pnp in lung MKs, resulting in inosine (and subsequently adenosine) release.  
2. Nucleosides bind A2B (or A2A) receptors on adjacent PASMCs and adventitial fibroblasts.  
3. Receptor activation triggers cAMP/PKA and/or ERK1/2 pathways, promoting proliferation and ECM gene transcription.  
4. PASMCs increase in number, media thickens; fibroblasts deposit collagen, stiffening the vessel wall.  
5. Medial hypertrophy and stiffness contribute to elevated pulmonary vascular resistance.  

**Candidate downstream axes:**  
- **Plausible axes:** (i) Direct A2B‑mediated PASMC proliferation; (ii) adenosine‑induced fibroblast‑to‑myofibroblast transition; (iii) combined effect on both cell types.  
- **Working model (provisional):** A2B on PASMCs drives proliferation, and on fibroblasts drives collagen production.  
- **What remains unresolved:** Relative contribution of MK‑derived nucleosides vs other sources (endothelial, hypoxic tissue); receptor subtype specificity.  

**Evidence basis:**  
- **User‑provided data:** Metabolomics and scRNA‑seq (Pnp MK PH‑up).  
- **Public dataset metadata or analyzed public data:** GSE289322 TGF‑β and ECM‑receptor interaction pathways may be enriched if mesenchymal activation is present; pending.  
- **Literature:** Adenosine A2B receptor contributes to PH in animal models; adenosine stimulates PASMC proliferation and fibroblast collagen synthesis.  
- **Biological rationale:** Spatial proximity of MKs to the vessel wall makes direct nucleoside delivery plausible.  
- **Evidence status:** Direct (MK metabolomics, Pnp expression) → inferred (nucleoside‑receptor axis) → speculative (MK‑to‑mesenchymal signal in PH).  

**Predicted observations:**  
- **In MKs:** Pnp‑dependent inosine release; conditioned medium from hypoxic MKs stimulates PASMC proliferation.  
- **In recipient or tissue compartment:** Increased phospho‑ERK and Ki67 in medial PASMCs of hypoxic lungs; reduced in Pnp‑cKO.  
- **In metabolomics or pathway activity:** Elevated inosine in perivascular microdialysate.  

**Experimental validation:**  
- **Perturbation:** Pnp‑cKO (Pf4‑Cre).  
- **Model:** Hypoxic PH; also, in vitro co‑culture of MKs with PASMCs/fibroblasts.  
- **Readout:** PASMC proliferation (EdU), fibroblast collagen gel contraction, and in vivo vascular medial thickness.  
- **Expected result:** cKO‑derived MKs fail to stimulate proliferation/collagen production; cKO mice show reduced PASMC hyperplasia and medial thickness.  
- **Falsifying result:** Adenosine receptor blockers (e.g., PSB603 for A2B) do not diminish the pro‑proliferative effect of MK‑conditioned media; or Pnp deletion does not alter vascular wall cell cycling.  

**Novelty:** Identifies MK metabolic reprogramming as a local source of adenosine/inosine that directly drives vascular wall remodeling.  
**Weaknesses:** Assumes MK‑derived nucleosides are not rapidly degraded by ecto‑adenosine deaminase; in vivo distance and diffusion may limit effect.  
**Priority estimate:**  
- Directional specificity: 4  
- Data support: 4  
- Literature support: 4  
- Novelty: 4  
- Testability: 4  
- Overall generation priority: 4  

---

**Self‑filtered rejected ideas:**  
- A matricellular/coagulation hypothesis solely based on Thbs1/F3 without metabolic anchor: rejected because mandatory Seurat queries not yet reported and would violate the rule not to propose a new class unless those genes show MK‑enriched hypoxia upregulation.  
- A Glo1‑methylglyoxal hypothesis: although metabolomics shows pyruvaldehyde (methylglyoxal) elevation in MKs, the mandatory Glo1 expression check is pending and no strong enzymatic link exists; also no KEGG pathway neighbor link for methylglyoxal was in the shortlist. Thus, cannot meet the “new broad mechanism class” bar.  
- Hypotheses that over‑resolve to M2 macrophages, Th17, or specific adenosine receptor subtypes without provisional labeling were rejected.  
- Any purely gene‑list or generic inflammation hypothesis was excluded.  

**Requests for Tool Use Agent:**  
- Retrieve and report the expression and differential expression results for the mandatory gene set (Pdgfb, Tgfb1, F3, Thbs1, Glo1, Rab27a, Tsg101, Cd44, Lox, Loxl1, Loxl2, Mki67) in the MK/platelet cluster, as the current hypotheses’ strength in ECM/thrombo‑inflammatory axes depends on these outcomes.  
- Inspect the GSE289322 analysis report to obtain DE statistics for the candidate gene list and GSEA enrichment FDR for the specified KEGG pathways; incorporate into refined hypotheses for the next cycle.  
- Clarify tissue context of GSE291455; if lung‑derived, extract baseline expression of the same gene set for contextual support.
