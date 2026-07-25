Cycle ID: 3

Hypotheses Generated: H1 (refined AMD1-polyamine immune axis), H2 (refined Pnp-purine catabolism immune axis), H3 (MK matricellular secretome axis with AMD1-eIF5A link)

---

### Hypothesis ID: H1

**Hypothesis title:** MK AMD1-polyamine → immune-mediated pulmonary vascular remodelling

**PI instruction addressed:** Refined immune-mediated axis 1: AMD1-polyamine → immune-mediated vascular remodelling

**Core directional hypothesis:**
Hypoxia upregulates AMD1 in lung megakaryocytes, channelling elevated methionine into accelerated polyamine synthesis; exported polyamines (spermidine/spermine) re‑shape perivascular T‑cell/ macrophage programmes, driving muscularisation and medial thickening.

**Direction-level reasoning summary:**
- **Data anchor:** Metabolite cross‑check shows MK methionine is sharply elevated (log2FC +3.26) in PH vs control, while whole‑lung methionine is decreased; AMD1 is MK‑enriched (enrichment log2 1.35) and strongly PH‑up in MKs (log2FC +1.77, p = 6.6 × 10⁻⁶).  
- **Biological interpretation:** Methionine accumulation in PH‑MKs provides excess substrate for SAM‑dependent polyamine biosynthesis. AMD1 is the rate‑limiting enzyme for spermidine/spermine synthesis; its hypoxia‑driven upregulation likely pushes the pathway forward.  
- **MK‑linked enzyme/pathway logic:** Methionine → SAM → dcSAM (decarboxylated SAM) via AMD1; dcSAM donates aminopropyl groups for spermidine/spermine synthesis. The substrate surge and enzyme induction together predict elevated polyamine output, though spermidine/spermine were not measured (key gap).  
- **Candidate downstream axis:** Immune‑mediated – polyamines exported from MKs (free or EV‑packaged) can be taken up by perivascular T‑cells and macrophages, where they influence differentiation (e.g. promote Th17‑like effector phenotype, alter macrophage polarisation) and cytokine secretion.  
- **Remodelling logic:** A shift toward a pro‑inflammatory T‑cell/macrophage milieu in the perivascular space would release mediators that activate vascular smooth‑muscle cells, drive medial muscularisation, and increase vessel stiffness.  
- **Key uncertainty:** Spermidine/spermine levels have not been measured; the causal link from MK polyamines to immune cell recruitment/skewing in the lung adventitia/perivascular space is inferred from general polyamine‑immune biology and requires direct validation.

**Directional chain:**
1. Hypoxia → MK accumulation of methionine (↑ 3.26‑fold) and strong upregulation of AMD1.  
2. AMD1 drives spermidine/spermine synthesis; elevated MK polyamines are released into the perivascular niche.  
3. Broad downstream axis: immune‑mediated – polyamines act on perivascular T‑cells/macrophages (candidate programmes: Th17‑like tone, M2‑to‑M1 shift, or NLRP3 inflammasome priming).  
4. Activated immune cells secrete factors (e.g. IL‑17, TNFα, chemokines) that stimulate medial VSMC proliferation and extracellular matrix deposition.  
5. Net phenotype: medial thickening, muscularisation of distal arterioles, vascular stiffening.

**Candidate downstream axes:**
- Plausible axes: (i) Spermidine/spermine promote Th17‑like differentiation of CD4⁺ T‑cells; (ii) Polyamines bias macrophage polarisation toward a pro‑remodelling phenotype; (iii) Polyamine‑driven NLRP3 activation in myeloid cells sustains adventitial inflammation.  
- Working model: MK‑derived spermidine/spermine skew perivascular T helper cells toward a Th17‑dominant pattern, producing IL‑17 that acts on VSMCs.  
- Specific examples, if useful: IL‑17 is a known driver of pulmonary vascular muscularisation; the A2B adenosine receptor is a candidate polyamine‑sensing receptor (provisional).  
- What remains unresolved: Direct measurement of spermidine/spermine in MK‑conditioned media / perivascular fluid; spatial co‑localisation of MKs with perivascular T‑cells; demonstration that MK‑specific polyamine blockade alters immune cell composition.

**Evidence basis:**
- **User‑provided data:** Priority‑gene Seurat table – Amd1 MK pct 31.44 %, enrichment log2 1.35, PH‑vs‑control MK log2FC +1.77, p = 6.6 × 10⁻⁶. Metabolite cross‑check – MK methionine log2FC +3.26 (PH‑CD41 vs Control‑CD41).  
- **Public dataset metadata or analysed public data:** None usable (GSE289322 identifier‑limited; no lung‑PH‑MK dataset).  
- **Literature:** Indirect – AMD1‑polyamine‑eIF5A axis implicated in translational control and cell growth (PMID 28658205, 38965534); polyamines known to modulate T‑cell differentiation. No direct lung‑MK‑hypoxia‑immune paper.  
- **Biological rationale:** Methionine‑polyamine metabolism is tightly linked to immune cell function; MKs reside in the perivascular niche and could act as paracrine immunomodulators under hypoxic stress.  
- **Evidence status:** Direct for methionine elevation and AMD1 upregulation in PH‑MKs; indirect/inferred for polyamine synthesis and downstream immune remodelling.

**Predicted observations:**
- In MKs: Elevated spermidine/spermine by LC‑MS in PH‑vs‑control MKs; increased AMD1 protein and decarboxylated SAM.  
- In recipient/tissue compartment: Perivascular accumulation of CD4⁺IL‑17⁺ T‑cells; altered macrophage cytokine profile in proximity to perivascular MKs.  
- In metabolomics/pathway activity: Elevated spermidine/spermine in lung tissue or BAL fluid; activation of polyamine‑responsive immune transcriptional programmes.

**Experimental validation:**
- Perturbation: MK‑specific Amd1 deletion (Pf4‑Cre × Amd1ᶠˡ/ᶠˡ) or pharmacological AMD1 inhibitor (e.g. SAM486A).  
- Model: Mouse hypoxia‑induced PH (10 % O₂, 3 weeks).  
- Readout: Right ventricular systolic pressure, medial thickness, muscularisation, perivascular T‑cell/macrophage infiltration and cytokine profile.  
- Expected result: Amd1 loss attenuates PH severity, reduces perivascular Th17‑like cells, and blunts muscularisation.  
- Falsifying result: MK‑specific AMD1 loss does not alter immune cell composition or remodelling; instead the phenotype is driven by AMD1‑independent polyamine supply or by non‑MK cells.

**Novelty:** First suggestion that lung MKs serve as a metabolically specialised source of immunomodulatory polyamines in hypoxia‑induced PH.

**Weaknesses:** Spermidine/spermine not measured; MK‑immune cell proximity not proven; polyamine‑immune signalling is poorly defined in the lung.

**Priority estimate (1–5):**
- Directional specificity: 4  
- Data support: 4  
- Literature support: 3  
- Novelty: 5  
- Testability: 4  
- Overall generation priority: 4/5

---

### Hypothesis ID: H2

**Hypothesis title:** MK Pnp‑purine catabolism → immune‑mediated vascular remodelling via hypoxanthine/xanthine/ROS

**PI instruction addressed:** Refined immune‑mediated axis 2: Pnp‑purine catabolism → immune‑mediated vascular remodelling

**Core directional hypothesis:**
Hypoxia‑driven Pnp upregulation in lung MKs accelerates purine nucleotide degradation, shifting the microenvironment toward hypoxanthine/xanthine/ROS production; this purinergic/oxidative stress signal recruits or activates perivascular macrophages and T‑cells, contributing to medial remodelling.

**Direction-level reasoning summary:**
- **Data anchor:** Seurat priority‑gene table shows Pnp is strongly PH‑up in MKs (log2FC +1.74, p = 3.8 × 10⁻⁶). MK sorted metabolite cross‑check reveals inosine is decreased in PH‑MKs (log2FC −0.34), and whole‑lung inosine and adenosine are unchanged (FDR > 0.5). Therefore, Pnp upregulation likely does not produce excess inosine/adenosine but instead consumes inosine, driving the reaction toward hypoxanthine.  
- **Biological interpretation:** Pnp (purine nucleoside phosphorylase) phosphorolyses inosine → hypoxanthine + ribose‑1‑phosphate. Hypoxanthine can then be oxidised to xanthine and uric acid by xanthine oxidase, generating superoxide. These metabolites and ROS are potent immune‑cell chemoattractants and activators (e.g. NLRP3 inflammasome, purinergic receptors).  
- **MK‑linked enzyme/pathway logic:** Pnp upregulation→ increased flux through purine degradation, lowering inosine and raising hypoxanthine/xanthine/ uric acid (not directly measured in this dataset). The pathway is directly linked to ROS generation and uric acid‑mediated immune signalling.  
- **Candidate downstream axis:** Immune‑mediated – hypoxanthine/uric acid crystals or soluble uric acid can activate NLRP3 in perivascular macrophages; ROS can attract neutrophils and macrophages; purinergic signalling (P2X/P2Y receptors) on T‑cells may modulate responses.  
- **Remodelling logic:** Sustained perivascular innate and adaptive immune activation fuels a chronic inflammatory milieu, releasing mitogenic factors (PDGF, TGF‑β) that promote VSMC proliferation, medial thickening, and stiffening.  
- **Key uncertainty:** Hypoxanthine/xanthine/uric acid were not measured in MKs or perivascular fluid; direct ROS measurement is absent; the relative contributions of uric acid vs. ROS vs. ATP remain unresolved; Pnp is not MK‑specific (MK enrichment log2 −1.2), so other cells may contribute.

**Directional chain:**
1. Hypoxia → MK Pnp upregulation (log2FC +1.74) and concomitant decrease in MK inosine.  
2. Elevated Pnp activity → increased catabolism of purine nucleosides → production of hypoxanthine, xanthine, and uric acid, with co‑generation of ROS via xanthine oxidase.  
3. Broad downstream axis: immune‑mediated – metabolites and ROS act on perivascular macrophages (NLRP3 activation, chemotaxis) and T‑cells (purinergic receptor modulation).  
4. Activated immune cells release pro‑remodelling cytokines and growth factors, stimulating VSMC hypertrophy and extracellular matrix deposition.  
5. Vascular phenotype: medial thickening, muscularisation, and stiffening.

**Candidate downstream axes:**
- Plausible axes: (i) Uric acid/Hypoxanthine → NLRP3 inflammasome in perivascular macrophages → IL‑1β release; (ii) Xanthine oxidase‑derived superoxide → oxidative stress in VSMCs and endothelial cells; (iii) Hypoxanthine/P2Y receptor signalling on T‑cells alters effector function; (iv) Uric acid as a DAMP recruits neutrophils.  
- Working model: MK‑derived hypoxanthine/uric acid activates perivascular macrophage NLRP3, leading to IL‑1β‑driven vascular inflammation and remodelling.  
- Specific examples, if useful: IL‑1β is a known PH mediator; allopurinol (xanthine oxidase inhibitor) partially attenuates hypoxia‑PH in rodents (indirect support).  
- What remains unresolved: Metabolite profile of hypoxanthine/xanthine/uric acid in MKs and perivascular niche; direct evidence of NLRP3 activation; spatial relationship of MKs to macrophages.

**Evidence basis:**
- **User‑provided data:** Priority‑gene Seurat table – Pnp PH‑vs‑control MK log2FC +1.74, p = 3.8 × 10⁻⁶. Metabolite cross‑check – MK inosine log2FC −0.34; whole‑lung inosine and adenosine not significantly changed.  
- **Public dataset metadata or analysed data:** None; GSE289322 unusable.  
- **Literature:** Pnp deficiency causes severe T‑cell immunodeficiency (purine nucleoside toxicity); hypoxanthine/xanthine/uric acid are recognised immune modulators (NLRP3, TLR). Indirect support only.  
- **Biological rationale:** Inosine is often anti‑inflammatory; its reduction and shunting toward pro‑oxidative/uric acid pathway fits an immune‑activating MK secretome in PH.  
- **Evidence status:** Direct for Pnp upregulation and inosine decrease; indirect/inferred for hypoxanthine/xanthine/uric acid production and immune remodelling.

**Predicted observations:**
- In MKs: Elevated hypoxanthine and xanthine by LC‑MS in PH‑MKs; increased xanthine oxidase activity.  
- In recipient/tissue compartment: Perivascular accumulation of NLRP3‑active macrophages; increased IL‑1β and ROS in perivascular fluid.  
- In metabolomics/pathway activity: Elevated lung uric acid and oxidative stress markers.

**Experimental validation:**
- Perturbation: MK‑specific Pnp deletion (Pf4‑Cre × Pnpᶠˡ/ᶠˡ) or xanthine oxidase inhibition (allopurinol) targeting the purine degradation arm.  
- Model: Mouse hypoxia‑PH.  
- Readout: PH severity indices, perivascular macrophage infiltration and IL‑1β, medial thickness, ROS staining.  
- Expected result: Pnp loss or allopurinol reduces perivascular macrophage activation and attenuates remodelling.  
- Falsifying result: Blocking purine degradation does not alter inflammation or remodelling; effect is independent of MKs.

**Novelty:** Shifts the MK‑purine metabolism narrative from adenosine signalling to hypoxanthine/xanthine/ROS‑driven immune activation, a previously unconsidered direction in PH.

**Weaknesses:** Hypoxanthine/xanthine not measured; Pnp is not MK‑specific; ROS‑immune link is plausible but not directly evidenced in the dataset.

**Priority estimate (1–5):**
- Directional specificity: 3  
- Data support: 3  
- Literature support: 2  
- Novelty: 5  
- Testability: 4  
- Overall generation priority: 3/5

---

### Hypothesis ID: H3

**Hypothesis title:** MK AMD1‑polyamine‑eIF5A axis controls thrombospondin‑1/PDGF‑B/TGF‑β1 secretion → direct vascular‑wall/matrix remodelling

**PI instruction addressed:** Conditional matricellular/secretome axis – MK metabolic control of Thbs1/Pdgfb/Tgfb1 → direct vascular wall/matrix remodelling

**Core directional hypothesis:**
Hypoxia‑induced AMD1 upregulation drives spermidine‑dependent hypusination of eIF5A in MKs, which selectively enhances translation of the matricelluar proteins Thbs1, Pdgfb, and Tgfb1; their co‑ordinated secretion acts on vascular smooth‑muscle cells, endothelial cells, and perivascular fibroblasts to drive medial muscularisation, matrix deposition, and stiffening.

**Direction-level reasoning summary:**
- **Data anchor:** Priority‑gene Seurat table confirms Thbs1 (MK pct 86 %, log2FC +1.43, p = 1.1 × 10⁻¹⁰), Pdgfb (MK pct 46 %, log2FC +0.98, p = 0.001), and Tgfb1 (MK pct 74 %, log2FC +0.74, p = 0.0001) are all MK‑enriched and PH‑up. AMD1 is also strongly PH‑up (log2FC +1.77, p = 6.6 × 10⁻⁶) and MK methionine accumulates (log2FC +3.26). The metabolic arm (AMD1‑polyamine) and the secretory arm (Thbs1/Pdgfb/Tgfb1) are therefore simultaneously activated in PH‑MKs.  
- **Biological interpretation:** AMD1 governs polyamine synthesis. The polyamine spermidine is the exclusive substrate for eIF5A hypusination, a unique post‑translational modification that enables eIF5A to facilitate translation of specific mRNAs with complex secondary structures or polyproline stretches. Many matricell proteins, including Thbs1, Pdgfb, and Tgfb1, contain such motifs and have been shown in other cell types to be translationally controlled by the polyamine‑eIF5A axis. Thus, MK AMD1 activity may act as a permissive switch for the co‑ordinate production of a pro‑remodelling secretome.  
- **MK‑linked enzyme/pathway logic:** AMD1 → spermidine → eIF5A hypusination → enhanced translation of Thbs1, Pdgfb, Tgfb1 (and likely other pro‑fibrotic/angiogenic factors). The link is a pathway‑neighbour inference (AMD1 to eIF5A is indirect but biochemically defined).  
- **Candidate downstream axis:** Direct vascular‑wall/matrix remodelling – thrombospondin‑1 activates TGF‑β1 (matrix‑bound latent complex) and directly inhibits endothelial proliferation; PDGF‑B is a potent VSMC mitogen and chemoattractant; TGF‑β1 promotes fibroblast‑to‑myofibroblast transition, collagen synthesis, and endothelial‑mesenchymal transition. Together they drive medial thickening, adventitial fibrosis, and stiffness.  
- **Key uncertainty:** Spermidine/eIF5A hypusination have not been measured in MKs; the translational control of Thbs1, Pdgfb, Tgfb1 by eIF5A in MKs is inferred and not directly tested; other AMD1‑independent regulators could also control these factors; the relative contribution of each secreted factor to specific aspects of remodelling remains unspecified.

**Directional chain:**
1. Hypoxia → MK AMD1 upregulation and methionine accumulation → spermidine synthesis.  
2. Spermidine serves as substrate for deoxyhypusine synthase, leading to eIF5A hypusination.  
3. Hypusinated eIF5A selectively boosts translation of mRNAs encoding thrombospondin‑1, PDGF‑B, and TGF‑β1.  
4. MKs secrete these proteins into the perivascular space (free or EV‑associated).  
5. Direct effects on vascular wall: PDGF‑B drives VSMC proliferation and muscularisation; thrombospondin‑1 activates latent TGF‑β1 and inhibits endothelial repair; TGF‑β1 induces perivascular fibroblast activation and matrix deposition.  
6. Result: medial thickening, muscularisation, adventitial fibrosis, and vessel stiffening.

**Candidate downstream axes:**
- Plausible axes: (i) AMD1‑eIF5A‑Thbs1 → TGF‑β activation → endothelial dysfunction and perivascular fibrosis; (ii) AMD1‑eIF5A‑Pdgfb → VSMC hyperplasia and medial muscularisation; (iii) AMD1‑eIF5A‑Tgfb1 → myofibroblast transition and collagen production.  
- Working model: Combined secretion of Thbs1, Pdgfb, and Tgfb1 acts in a co‑operative manner to reproduce the hallmark features of hypoxia‑PH remodelling.  
- Specific examples, if useful: Thrombospondin‑1 is a well‑known activator of TGF‑β and a negative regulator of angiogenesis; PDGF‑B is overexpressed in human PH.  
- What remains unresolved: Direct demonstration that eIF5A hypusination controls these specific transcripts in MKs; whether all three factors act in concert or one dominates.

**Evidence basis:**
- **User‑provided data:** Seurat table – Thbs1, Pdgfb, Tgfb1, Amd1 expression metrics as above. Metabolite cross‑check – MK methionine log2FC +3.26.  
- **Public dataset metadata or analysed data:** None.  
- **Literature:** AMD1‑polyamine‑eIF5A axis is a known translational control mechanism in cancer (PMID 28658205, 38965534); thrombospondin‑1 is regulated by eIF5A in other contexts (indirect). PDGF‑B and TGF‑β1 are classic PH mediators.  
- **Biological rationale:** Coordinated upregulation of a metabolic enzyme and multiple matricell proteins in MKs under hypoxia suggests a common regulatory node; the eIF5A axis is well‑positioned to act as that node.  
- **Evidence status:** Direct for gene expression of Amd1 and the three matricell genes in PH‑MKs; indirect/inferred for polyamine‑eIF5A translational control and secretion.

**Predicted observations:**
- In MKs: Increased hypusinated eIF5A protein; enhanced polysomal loading of Thbs1, Pdgfb, Tgfb1 mRNA; elevated secretion of these proteins in MK‑conditioned media.  
- In recipient/tissue compartment: Perivascular deposition of thrombospondin‑1 and PDGF‑B; activation of TGF‑β signalling in VSMCs and fibroblasts.  
- In metabolomics/pathway activity: Spermidine elevation in MKs (once measured); decreased eIF5A hypusination upon AMD1 inhibition.

**Experimental validation:**
- Perturbation: MK‑specific Amd1 deletion, or pharmacological inhibition of eIF5A hypusination (e.g. GC7, deoxyhypusine synthase inhibitor).  
- Model: Mouse hypoxia‑PH or PASMC/pericyte co‑culture with MK‑conditioned medium.  
- Readout: Secretion of Thbs1/Pdgfb/Tgfb1 (ELISA/Western of MK media); medial thickness, muscularisation, fibrotic area; eIF5A hypusination status.  
- Expected result: AMD1 loss or hypusination blockade reduces MK secretion of these matricell proteins and attenuates vascular remodelling.  
- Falsifying result: AMD1/eIF5A inhibition does not alter secretion of these factors, or remodelling is independent of MK‑derived proteins (e.g. replenished by other cells).

**Novelty:** Introduces a metabolic‑to‑secretory translational control axis (AMD1‑eIF5A) that connects MK polyamine metabolism directly to the production of multiple disease‑relevant matricellular proteins in PH.

**Weaknesses:** Spermidine not measured; eIF5A hypusination not assayed; the specificity of eIF5A for these transcripts in MKs is untested; alternative pathways (e.g. mTORC1‑S6K) could regulate secretion.

**Priority estimate (1–5):**
- Directional specificity: 4  
- Data support: 4  
- Literature support: 3  
- Novelty: 5  
- Testability: 4  
- Overall generation priority: 4/5

---

### Self-filtered rejected ideas:
- Broad EV‑mediated miRNA/protease axis not grounded in specific MK‑enriched PH‑up cargo genes – would be too generic.  
- Direct endothelial‑to‑mesenchymal transition (EndMT) as sole downstream path for AMD1 axis – no data support and too specific.  
- Adenosine/A2B‑centred Pnp hypothesis – rejected because the new cross‑check shows MK inosine is decreased, not increased, and adenosine unchanged; reframed as hypoxanthine/ROS axis (H2).  
- Coagulation‑factor (e.g. fibrinogen) hypersecretion – not supported by Seurat data showing MK‑enriched PH‑up coagulation genes beyond the already‑used matricellular panel.  
- A pure platelet‑derived serotonin/mitogen hypothesis – not anchored on MK metabolic data and risks generic platelet activation.

**Requests for Tool Use Agent:** None; all mandatory data retrieval was completed in the evidence package. Future cycles could benefit from targeted literature searches on “eIF5A hypusination thrombospondin megakaryocyte” and “purine nucleoside phosphorylase macrophage NLRP3 vascular remodelling”.
