Cycle ID: 3

Hypotheses generated: 3

---

### Hypothesis 1

**Hypothesis ID:** H1  
**Hypothesis title:** MK‑AMD1‑polyamine → paracrine immune‑mediated vascular remodelling  
**PI instruction addressed:** Refined immune‑mediated axis 1 – AMD1‑polyamine → immune‑mediated vascular remodelling; emphasis on paracrine ligand‑receptor mechanisms.

**Core directional hypothesis:**  
Under hypoxia, lung MKs accumulate methionine and up‑regulate AMD1, shifting polyamine metabolism; secreted polyamines or polyamine‑dependent immune signals act on perivascular T‑cells/macrophages to drive immunomodulatory remodelling of the pulmonary vasculature.

**Direction‑level reasoning summary:**  
- **Data anchor:** In PH‑MKs, methionine is strongly elevated (log2FC 3.26, `priority_metabolite_crosscheck.csv`), while SAM is unchanged (log2FC 0.11). Seurat data (`priority_gene_seurat_expression.csv`) show *Amd1* is MK‑enriched (log2 1.35) and PH‑up in MKs (log2FC 1.77, Wilcoxon p=6.55×10⁻⁶).  
- **Biological interpretation:** Methionine accumulation without a corresponding SAM rise suggests diversion into the methionine salvage/polyamine pathway rather than global methylation. AMD1, the rate‑limiting decarboxylase for SAM‑to‑dcSAM, is the key enzymatic link; the polyamine products spermidine/spermine, though not measured, are the inferred effectors.  
- **MK‑linked enzyme/pathway logic:** AMD1 is a pathway‑neighbour gene (KEGG: Cysteine and methionine metabolism, Methionine salvage). Its hypoxia‑induced upregulation in MKs, coincident with substrate accumulation, would boost dcSAM and downstream spermidine/spermine synthesis.  
- **Candidate downstream axis:** Immune‑mediated. Secreted polyamines can be taken up by adjacent T‑cells and macrophages, promoting a Th17‑like tone or alternative macrophage activation. Alternatively, MK‑derived polyamines or polyamine‑regulated cytokines (e.g., via eIF5A‑dependent translation) could act as paracrine ligands on immune cell receptors.  
- **Remodelling logic:** A shift in perivascular immune status (e.g., IL‑17‑expressing T‑cells, profibrotic macrophages) stimulates medial smooth‑muscle hypertrophy, adventitial inflammation, and vascular stiffness.  
- **Key uncertainty:** Whether MKs export polyamines in vivo; which specific immune cell subset(s) are the proximal responders; which receptors (e.g., TAARs, GPRC) mediate polyamine sensing in the lung.

**Directional chain:**  
1. Hypoxia drives methionine accumulation and *Amd1* upregulation in lung MKs.  
2. MK AMD1 increases dcSAM, fuelling spermidine/spermine synthesis (polyamine pathway).  
3. MK‑exported polyamines or polyamine‑dependent secreted mediators (broad class: polycationic amines) act as paracrine signals on juxtaposed immune cells.  
4. Immune cells (T‑cells, macrophages) polarise toward a pro‑remodelling phenotype (Th17‑like / M2‑like).  
5. Immune‑driven medial thickening, muscularisation, and vascular stiffness.

**Candidate downstream axes:**  
- **Plausible axes:** (a) Polyamine uptake by CD4⁺ T‑cells → enhanced HIF‑1α/STAT3 → IL‑17 production → VSMC activation; (b) Polyamine‑induced macrophage arginase‑1 expression → proline/collagen synthesis → perivascular fibrosis; (c) MK secretion of polyamine‑modulated cytokines (e.g., TGF‑β1) rather than free polyamines.  
- **Working model:** MK‑derived spermidine acts on perivascular T‑cells to bias them towards a Th17‑like state; the IL‑17 axis then drives vascular remodelling.  
- **Specific examples, if useful:** IL‑17A receptor on VSMCs; spermidine sensing by GPRC6A on dendritic cells.  
- **What remains unresolved:** Identity of the secreted mediator (free polyamine vs. polyamine‑dependent cytokine), the direct target cell, and the receptor.

**Evidence basis:**  
- **User‑provided data:** `priority_metabolite_crosscheck.csv` (MK methionine log2FC 3.26; SAM log2FC 0.11); `priority_gene_seurat_expression.csv` (*Amd1* MK enrichment log2 1.35, PH‑up log2FC 1.77).  
- **Public dataset metadata or analyzed public data:** None usable; GSE289322 identifier mismatch.  
- **Literature:** PubMed hits link AMD1/polyamines to mTORC1, c‑Myc, and therapeutic resistance (PMID 38965534, 28658205), but no direct lung‑PH‑MK literature.  
- **Biological rationale:** Polyamines are known immunomodulators; their accumulation in the perivascular space could alter T‑cell polarity.  
- **Evidence status:** Direct metabolite and enzyme‑gene upregulation; polyamine product level and secretion are inferred; immune axis is speculative.

**Predicted observations:**  
- **In MKs:** Elevated spermidine/spermine (to be measured); increased eIF5A hypusination.  
- **In recipient or tissue compartment:** Perivascular accumulation of Th17 cells and/or arginase‑1⁺ macrophages.  
- **In metabolomics or pathway activity:** PH‑MK conditioned medium contains elevated polyamines.

**Experimental validation:**  
- **Perturbation:** Bone‑marrow‑specific *Amd1* knockout under hypoxia, or pharmacological AMD1 inhibition (e.g., SAM486A).  
- **Model:** Inducible MK‑specific *Amd1* KO mice exposed to chronic hypoxia.  
- **Readout:** Pulmonary artery muscularisation, perivascular immune cell profiling, spermidine/spermine levels in lung tissue.  
- **Expected result:** Loss of MK AMD1 reduces lung polyamines, blunts Th17‑biased immune infiltration, and attenuates vascular remodelling.  
- **Falsifying result:** KO has no effect on polyamine levels or remodelling, or polyamine blockade (e.g., DFMO) does not reduce immune‑driven remodelling despite AMD1 deletion.

**Novelty:** First direct link between in‑situ MK polyamine metabolism and immune‑driven pulmonary vascular remodelling; paracrine polyamine signalling from MKs is unexplored in PH.

**Weaknesses:** Polyamine secretion from MKs is assumed; no direct spermidine/spermine measurement; immune subset remains provisional.

**Priority estimate:**  
- Directional specificity: 4  
- Data support: 5 (strong MK expression and metabolite shift)  
- Literature support: 2 (indirect cancer/immunology links)  
- Novelty: 5  
- Testability: 4  
- Overall generation priority: 4.2

**Explicit rejection filter:** Passes all – MK‑specific, hypoxia‑dependent, immune‑mediated remodelling, paracrine aspect, experimentally testable.

---

### Hypothesis 2

**Hypothesis ID:** H2  
**Hypothesis title:** MK‑Pnp‑purine catabolism → hypoxanthine/xanthine‑mediated immune‑vascular remodelling  
**PI instruction addressed:** Refined immune‑mediated axis 2 – Pnp‑purine catabolism → immune‑mediated vascular remodelling; emphasis on paracrine ligand‑receptor mechanisms.

**Core directional hypothesis:**  
Hypoxia‑activated MKs up‑regulate *Pnp*, channelling purine nucleosides into hypoxanthine/xanthine, which are secreted and, via xanthine oxidoreductase‑generated reactive oxygen species or purinergic receptor engagement on vascular wall and immune cells, drive medial remodelling.

**Direction‑level reasoning summary:**  
- **Data anchor:** MK inosine is not elevated (log2FC –0.34, `priority_metabolite_crosscheck.csv`), contradicting an adenosine‑accumulation model; whole‑lung inosine (log2FC 0.21, FDR 0.57) and adenosine (log2FC 0.37, FDR 0.67) are unchanged. However, *Pnp* (purine nucleoside phosphorylase) is strongly MK‑up in PH (log2FC 1.74, MK enrichment log2 –1.22, Wilcoxon p=3.81×10⁻⁶, `priority_gene_seurat_expression.csv`). PNP cleaves inosine to hypoxanthine.  
- **Biological interpretation:** The *Pnp* upregulation, coupled with static/falling inosine, indicates accelerated purine catabolism through the hypoxanthine/xanthine/uric acid axis, not adenosine retention. The metabolic product hypoxanthine (and its oxidised derivatives) may act as paracrine danger signals or ROS generators.  
- **MK‑linked enzyme/pathway logic:** PNP is a direct enzyme for inosine (ec:2.4.2.1, KEGG: Adenine ribonucleotide degradation, Purine metabolism). MKs with high PNP would rapidly convert intracellular inosine to hypoxanthine, which can be exported via equilibrative nucleoside transporters.  
- **Candidate downstream axis:** Immune‑mediated. Hypoxanthine can be oxidised by xanthine oxidase to uric acid with superoxide production, activating perivascular macrophages and inducing endothelial/SMC oxidative stress. Alternatively, hypoxanthine itself might signal through purinergic receptors (A₂A, A₂B) albeit with lower affinity.  
- **Remodelling logic:** ROS and/or purinergic signalling promote perivascular inflammation, VSMC proliferation, and endothelial dysfunction, leading to muscularisation and stiffness.  
- **Key uncertainty:** Whether hypoxanthine is the primary product accumulating in the extracellular space; which cell type (macrophage vs. SMC) is the proximal target; the relative role of ROS vs. purinergic receptor signalling.

**Directional chain:**  
1. Hypoxia up‑regulates *Pnp* in lung MKs.  
2. Elevated PNP activity converts inosine to hypoxanthine, lowering MK inosine and enriching hypoxanthine.  
3. Hypoxanthine is secreted from MKs (paracrine) into the perivascular niche.  
4. Extracellular hypoxanthine is taken up by macrophages/VSMCs and oxidised by xanthine oxidoreductase, generating uric acid + superoxide, or acts on purinergic receptors.  
5. ROS‑driven inflammation and direct VSMC proliferation/hypertrophy drive medial remodelling.

**Candidate downstream axes:**  
- **Plausible axes:** (a) Hypoxanthine → macrophage xanthine oxidase → ROS → inflammasome activation → IL‑1β → VSMC activation; (b) Hypoxanthine → endothelial xanthine oxidase → endothelial dysfunction → perivascular macrophage recruitment; (c) Hypoxanthine/xanthine as partial agonists at adenosine A₂B receptor on VSMCs, promoting proliferation.  
- **Working model:** MK‑derived hypoxanthine fuels macrophage xanthine oxidase‑dependent superoxide production, triggering a pro‑inflammatory loop that thickens the medial layer.  
- **Specific examples, if useful:** Xanthine oxidase inhibitor (allopurinol) protects against PH in some models; P2Y14 receptor can bind UDP‑sugars, but hypoxanthine is a nucleotide degradation product – likely ROS is principal.  
- **What remains unresolved:** Identity of the dominant paracrine mediator (ROS vs. purinergic ligand), the primary recipient cell, and the contribution of MKs relative to other lung sources of hypoxanthine.

**Evidence basis:**  
- **User‑provided data:** `priority_metabolite_crosscheck.csv` (MK inosine log2FC –0.34; whole‑lung inosine/adenosine not significant); `priority_gene_seurat_expression.csv` (*Pnp* PH‑up in MKs log2FC 1.74).  
- **Public dataset metadata or analyzed public data:** None usable.  
- **Literature:** None directly retrieved for Pnp in PH; indirect: xanthine oxidase in pulmonary hypertension.  
- **Biological rationale:** Purine catabolism is a well‑known source of ROS in vascular disease; MKs are positioned to release hypoxanthine locally.  
- **Evidence status:** Direct enzyme upregulation; product (hypoxanthine) pathway inferred from inosine drop; immune‑ROS axis is speculative.

**Predicted observations:**  
- **In MKs:** Elevated hypoxanthine (to be measured); increased PNP enzymatic activity.  
- **In recipient or tissue compartment:** Perivascular xanthine oxidase activity elevated; increased superoxide staining in medial layer; up‑regulation of inflammatory cytokines.  
- **In metabolomics or pathway activity:** Conditioned medium from PH‑MKs contains more hypoxanthine and uric acid than controls.

**Experimental validation:**  
- **Perturbation:** Bone‑marrow‑specific *Pnp* deletion, or pharmacological PNP inhibition, combined with xanthine oxidase inhibitor (allopurinol) and/or purinergic receptor blockade.  
- **Model:** MK‑specific *Pnp* KO mice in chronic hypoxia.  
- **Readout:** Pulmonary vascular remodelling, perivascular ROS, immune cell activation.  
- **Expected result:** MK *Pnp* deletion reduces lung hypoxanthine/ROS, dampens macrophage activation, and attenuates vascular muscularisation.  
- **Falsifying result:** KO fails to alter hypoxanthine levels or remodelling, or allopurinol does not rescue the phenotype.

**Novelty:** Re‑interprets Pnp as a hypoxanthine/ROS‑based immune‑remodelling driver in PH, moving away from adenosine accumulation; MK‑centric purine catabolism in PH is new.

**Weaknesses:** Hypoxanthine was not measured in the MK metabolomics panel; the link to ROS and immune cells is inferred; PNP can also work in reverse, creating inosine – direction depends on substrate concentrations.

**Priority estimate:**  
- Directional specificity: 4  
- Data support: 4 (strong Pnp signal, but metabolite direction is indirect)  
- Literature support: 2  
- Novelty: 5  
- Testability: 4  
- Overall generation priority: 3.9

**Explicit rejection filter:** Passes – MK‑specific, hypoxia‑dependent, immune‑mediated remodelling, paracrine‑ROS concept, testable.

---

### Hypothesis 3

**Hypothesis ID:** H3  
**Hypothesis title:** MK‑AMD1‑eIF5A hypusination controls a matricellular secretome (Thbs1/Pdgfb/Tgfb1) that directly remodels the vascular wall  
**PI instruction addressed:** Conditional matricellular/secretome axis – MK metabolic control of thrombospondin‑1, PDGF‑B, TGF‑β1 secretion → direct vascular wall/matrix remodelling; emphasis on paracrine ligand‑receptor mechanisms.

**Core directional hypothesis:**  
The AMD1‑polyamine‑eIF5A hypusination axis in hypoxic MKs selectively enhances translation of *Thbs1*, *Pdgfb*, and *Tgfb1* mRNAs, causing MK secretion of these paracrine ligands, which act on vascular endothelial cells, smooth‑muscle cells, and perivascular fibroblasts to drive direct structural remodelling.

**Direction‑level reasoning summary:**  
- **Data anchor:** MK methionine is highly increased (log2FC 3.26), SAM is flat, and *Amd1* is MK‑enriched/PH‑up (see H1). Seurat confirms *Thbs1*, *Pdgfb*, and *Tgfb1* are MK‑enriched (log2FC > 0) and further upregulated in PH‑MKs (e.g., *Thbs1* MK‑enrichment log2 2.34, PH‑vs‑control log2FC 1.56; *Pdgfb* enrichment 2.02, PH log2FC 1.62; *Tgfb1* enrichment 0.82, PH log2FC 0.89 from `priority_gene_seurat_expression.csv`).  
- **Biological interpretation:** AMD1‑dependent polyamine synthesis drives eIF5A hypusination, a translation‑control step that favours translation of mRNAs with specific motifs, often found in secreted matricellular proteins. The coordinated upregulation of *Thbs1*, *Pdgfb*, and *Tgfb1* in MKs, combined with the strong AMD1/methionine signal, suggests a metabolic‑translational hub that boosts their production.  
- **MK‑linked enzyme/pathway logic:** AMD1 is a pathway‑neighbour gene for methionine metabolism; its product dcSAM is used to generate spermidine, the substrate for deoxyhypusine synthase (DHPS)–mediated eIF5A hypusination. Hypusinated eIF5A facilitates translation elongation of poly‑proline or proline‑rich motifs, which are common in ECM proteins and cytokines. *Thbs1*, *Pdgfb*, and *Tgfb1* each contain such motifs. MKs may thus use this circuit to secrete a cocktail that simultaneously induces endothelial dysfunction, pericyte/SMC proliferation, and perivascular fibrosis.  
- **Candidate downstream axis:** Direct vascular‑wall/matrix remodelling. Secreted THBS1 activates CD36/CD47 on ECs (anti‑angiogenic, pro‑apoptotic) and latent TGF‑β1 activation; PDGF‑BB is a potent SMC mitogen via PDGFRβ; TGF‑β1 promotes fibroblast‑to‑myofibroblast transition and matrix deposition. This triplet can orchestrate medial thickening, muscularisation, and stiffening in a paracrine, receptor‑dependent manner.  
- **Remodelling logic:** Simultaneous release of these factors from perivascular MKs induces SMC hyperplasia, endothelial barrier loss, and adventitial collagen accumulation, matching hypoxia‑induced remodelling phenotypes.  
- **Key uncertainty:** Proof that AMD1‑eIF5A directly governs translation of these three mRNAs in MKs; the relative contribution of each protein to the remodelling; whether MKs are the dominant source of these factors in the perivascular niche.

**Directional chain:**  
1. Hypoxia drives methionine accumulation and *Amd1* upregulation in lung MKs.  
2. AMD1 increases dcSAM and spermidine pools; spermidine serves as the essential substrate for eIF5A hypusination.  
3. Hypusinated eIF5A selectively enhances translation of *Thbs1*, *Pdgfb*, and *Tgfb1* mRNAs, raising their protein levels and secretion.  
4. Secreted THBS1, PDGF‑BB, and TGF‑β1 diffuse locally and engage receptors on ECs (CD36/CD47, PDGFRβ, TGFBR), VSMCs (PDGFRβ, TGFBR), and fibroblasts (TGFBR).  
5. Integrated receptor signalling drives endothelial apoptosis/dysfunction, SMC proliferation/hypertrophy, and perivascular fibrosis → medial thickening, muscularisation, stiffness.

**Candidate downstream axes:**  
- **Plausible axes:** (a) Primarily PDGF‑BB‑driven SMC expansion with TGF‑β1‑mediated matrix stabilization; (b) THBS1‑mediated TGF‑β1 activation as the master switch; (c) Combined endothelial (anti‑angiogenic) and SMC effects.  
- **Working model:** PDGF‑BB and TGF‑β1 are the dominant effectors; THBS1 serves to activate latent TGF‑β1 in the ECM, amplifying the TGF‑β1 signal.  
- **Specific examples, if useful:** PDGF‑BB/PDGFRβ axis is a known target in PH; TGF‑β1 signalling via ALK5/Smad2/3 in SMCs; CD36 on endothelial cells.  
- **What remains unresolved:** The precise modulatory role of eIF5A hypusination on each mRNA, and whether MK‑specific deletion of hypusination pathway suffices to diminish secretion of these factors.

**Evidence basis:**  
- **User‑provided data:** `priority_metabolite_crosscheck.csv` (MK methionine up); `priority_gene_seurat_expression.csv` (Amd1, Thbs1, Pdgfb, Tgfb1 MK‑enriched and PH‑up).  
- **Public dataset metadata or analyzed public data:** None usable.  
- **Literature:** eIF5A hypusination has been linked to TGF‑β1 translation in cancer (not retrieved here but known); PDGF‑BB is a PH mediator; THBS1 is associated with PH vascular remodelling.  
- **Biological rationale:** eIF5A‑dependent translation control provides a plausible molecular switch for MKs to rapidly secrete a pro‑remodelling secretome.  
- **Evidence status:** Direct metabolite and gene expression changes; translation control and secretion are inferred; receptor‑mediated remodelling is well‑established for these ligands but MK origin is novel.

**Predicted observations:**  
- **In MKs:** Increased hypusinated eIF5A; higher polysome association of *Thbs1*, *Pdgfb*, *Tgfb1* mRNAs; elevated THBS1, PDGF‑BB, TGF‑β1 protein in MKs and conditioned medium.  
- **In recipient or tissue compartment:** Perivascular deposition of THBS1; phospho‑PDGFRβ and phospho‑Smad2/3 in medial SMCs; enhanced collagen.  
- **In metabolomics or pathway activity:** Spermidine/spermine accumulation (if measured); AMPD1 activity unchanged.

**Experimental validation:**  
- **Perturbation:** MK‑specific deletion of *Amd1* or *Dhps* (eIF5A hypusination) or pharmacological eIF5A hypusination inhibitor (GC7).  
- **Model:** Inducible MK‑specific *Amd1* or *Dhps* KO mice in chronic hypoxia.  
- **Readout:** Secretion of THBS1/PDGF‑BB/TGF‑β1 from isolated MKs; vascular remodelling endpoints; eIF5A hypusination status.  
- **Expected result:** Loss of AMD1 or DHPS in MKs reduces secretion of the matricellular triplet and attenuates medial thickening, muscularisation, and fibrosis, without affecting MK numbers.  
- **Falsifying result:** MK‑specific *Amd1* deletion does not lower the secretion of these proteins, or remodelling is unchanged despite reduced eIF5A hypusination, indicating alternative translational control or other cell sources.

**Novelty:** First proposal of an eIF5A‑driven MK secretome that directly remodels the vascular wall; ties metabolism (methionine/polyamine) to a defined set of paracrine ligands.

**Weaknesses:** All three proteins are also produced by other cell types; MK contribution may be minor; no direct evidence of eIF5A‑dependent translation of these mRNAs in MKs; spermidine/spermine levels still missing.

**Priority estimate:**  
- Directional specificity: 5  
- Data support: 5 (strong MK expression of all three genes plus metabolic link)  
- Literature support: 3 (PDGF/TGF‑β in PH, eIF5A in cancer)  
- Novelty: 5  
- Testability: 4  
- Overall generation priority: 4.6

**Explicit rejection filter:** Passes – MK‑specific, hypoxia‑regulated, direct vascular‑wall remodelling, paracrine ligand‑receptor mechanism, testable.

---

### Rejected ideas:
- **Broad EV/coagulation hypothesis:** Not allowed by cycle‑3 instructions; candidate genes (e.g., Vwf, F5) were not part of the Seurat query and no explicit metabolic control link provided.  
- **Inosine → adenosine receptor axis:** Rejected because MK inosine is falling, and whole‑lung adenosine unchanged; would require adenosine accumulation that is not supported.  
- **Retinoic acid → Cyp26b1 immune axis:** Cyp26b1 is not significantly MK‑enriched nor PH‑up in MKs (Wilcoxon p 0.253), and the retinoic acid metabolite signal lacks a clear paracrine ligand‑receptor mechanism connecting to vascular remodelling.

All three hypotheses are direction‑level, paracrine‑oriented, and strictly anchored on the evidence package.
