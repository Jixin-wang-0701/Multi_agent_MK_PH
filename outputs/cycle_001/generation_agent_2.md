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
