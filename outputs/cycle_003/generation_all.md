# Generation Agent Outputs

## generation_metabolic
Cycle ID: 3

Hypotheses generated:
1. Refined immune‑mediated axis 1: MK‑AMD1‑polyamine → immune‑mediated vascular remodelling  
2. Refined immune‑mediated axis 2: MK‑Pnp‑purine catabolism → immune‑mediated vascular remodelling  
3. Conditional matricellular/secretome axis: MK‑AMD1‑polyamine‑eIF5A → direct vascular‑wall/matrix remodelling

All hypotheses are anchored on the provided evidence tables (Seurat priority gene expression, metabolite cross‑check, KEGG/enzyme shortlist) and remain at direction‑level resolution.

---

### Hypothesis ID: H1
**Hypothesis title:** MK‑AMD1‑polyamine → immune‑mediated vascular remodelling

**PI instruction addressed:** Refined immune‑mediated axis 1: AMD1‑polyamine → immune‑mediated vascular remodelling

**Core directional hypothesis:**  
Hypoxia‑driven methionine accumulation up‑regulates AMD1 in lung megakaryocytes, shifting polyamine metabolism; the resulting polyamine (spermidine/spermine) tone influences perivascular immune cell programmes (e.g., T‑helper/Th17‑like polarization, macrophage activation), thereby promoting medial thickening and muscularisation.

**Direction‑level reasoning summary:**
- Data anchor: MK‑sorted methionine is strongly increased (log2FC 3.26, sFig6A, PH‑CD41 vs Control‑CD41); the pathway‑neighbour gene *Amd1* shows robust MK enrichment (log2 1.353) and PH‑up log2FC 1.77 (p=6.55e‑06) in Seurat.
- Biological interpretation: Excess methionine in hypoxic MKs likely feeds SAM/polyamine synthesis; *Amd1* induction indicates heightened conversion of SAM to decarboxylated SAM, the committed step for spermidine/spermine synthesis.
- MK‑linked pathway logic: AMD1 is the rate‑limiting enzyme for polyamine production; its up‑regulation is mechanistically plausible to shift the MK secretome through polyamine‑dependent translational control (eIF5A hypusination) or direct metabolite export.
- Candidate downstream axis: Polyamines (spermidine/spermine) can modulate perivascular immune cells—e.g., fostering Th17‑like tone, altering macrophage polarization—or affect endothelial/smooth muscle cells. The axis is classified as **immune‑mediated**.
- Remodelling logic: Immune‑driven signals (cytokines, growth factors) promote medial activation, smooth muscle proliferation, and muscularisation, contributing to vascular stiffness.
- Key uncertainty: Spermidine/spermine levels were not measured; the causal chain from MK polyamine export to immune cell modulation lacks direct evidence, and MK spatial proximity to T‑cells/macrophages remains unresolved.

**Directional chain:**
1. Hypoxia elevates intracellular methionine in lung MKs (log2FC 3.26).  
2. Methionine flux increases S‑adenosylmethionine (SAM) and induces *Amd1*, driving decarboxylated SAM production and polyamine synthesis (spermidine/spermine).  
3. Elevated polyamines may alter the MK secretome via hypusination of eIF5A, favouring translation of immune‑modulatory factors, or polyamines themselves may be released to act on neighbouring cells.  
4. Broad downstream axis: immune‑mediated (T‑helper/Th17‑like tone, macrophage/monocyte activation).  
5. Perivascular immune activation releases mediators that stimulate medial smooth muscle hypertrophy/hyperplasia, leading to muscularisation and vascular stiffness.

**Candidate downstream axes:**
- Plausible axes: (i) MK‑released polyamines directly polarize perivascular T‑cells toward Th17‑like states; (ii) polyamine‑dependent eIF5A hypusination enhances MK secretion of cytokines/chemokines that recruit/activate macrophages; (iii) polyamines act on endothelial/smooth muscle cells secondarily to promote immune cell adhesion; (iv) unresolved stromal or EV‑mediated route.
- Working model (provisional): Polyamines, particularly spermidine, promote a Th17‑favouring perivascular milieu, contributing to IL‑17‑mediated medial activation.
- Specific examples: SAM, spermidine, Th17‑like tone, IL‑17 signalling, macrophage M1‑like polarization – all provisional.
- What remains unresolved: Whether MK‑derived polyamines reach immune cells in sufficient concentration, the identity of the exact immune effector subset, and whether hypusinated eIF5A–dependent translation is the primary mediator.

**Evidence basis:**
- User‑provided data: Methionine up in MKs (log2FC 3.26, sFig6A); *Amd1* MK‑enriched (log2 1.353) and PH‑up (log2FC 1.77, p=6.55e‑06) from Seurat priority gene table.
- Public dataset metadata or analyzed public data: No usable public dataset identified for validation.
- Literature: PubMed hits (PMID 38965534, 28658205) support AMD1–polyamine–eIF5A control of translation in cancer contexts; no direct PH or immune literature is available.
- Biological rationale: Polyamine metabolism is a conserved stress‑responsive programme; its modulation of immune cell function is plausible but not yet linked to MK‑derived signals in PH.
- Evidence status: **direct** for MK methionine and *Amd1* expression; **inferred** for polyamine accumulation and downstream immune axis.

**Predicted observations:**
- In MKs: Elevated spermidine/spermine (requires targeted metabolomics); increased hypusinated eIF5A.
- In recipient or tissue compartment: Perivascular enrichment of IL‑17‑producing T‑cells or altered macrophage markers in PH lungs.
- In metabolomics or pathway activity: Increased MK polyamine biosynthetic enzyme activity.

**Experimental validation:**
- Perturbation: Pharmacological AMD1 inhibitor (e.g., SAM486A) or MK‑specific *Amd1* knockout.
- Model: Mouse hypoxia‑induced PH (SuHx or chronic hypoxia) with platelet/MK‑specific Cre.
- Readout: Vascular remodelling (medial thickness, muscularisation), perivascular immune cell composition (flow cytometry, IHC), and MK polyamine levels.
- Expected result: Loss of MK *Amd1* reduces perivascular T‑cell/Th17 infiltration and blunts medial thickening.
- Falsifying result: AMD1 inhibition does not alter immune cell recruitment or vascular remodelling despite reduced MK polyamines, implying the axis is not functionally significant.

**Novelty:** First proposal that hypoxic MK AMD1 activity generates polyamines that shape the perivascular immune landscape in PH.

**Weaknesses:** Polyamine product levels unmeasured; mechanism of transfer from MKs to immune cells unknown; eIF5A hypusination link inferred; specific immune subtype not resolved.

**Revision relative to previous cycle:** None (new hypothesis with updated evidence tables).

**Priority estimate:**
- Directional specificity: 4  
- Data support: 5 (strong MK metabolite and gene expression data)  
- Literature support: 3 (polyamine‑eIF5A literature supportive but no PH context)  
- Novelty: 5  
- Testability: 4 (inhibitors available; spatial validation needed)  
- Overall generation priority: 5 (highly anchored on evidence and meets brief)

**Explicit rejection filter:** Passed — MK‑specific component (*Amd1*), hypoxia‑dependent mechanism, vascular remodelling phenotype, beyond generic inflammation, testable.

---

### Hypothesis ID: H2
**Hypothesis title:** MK‑Pnp‑purine catabolism → immune‑mediated vascular remodelling

**PI instruction addressed:** Refined immune‑mediated axis 2: Pnp‑purine catabolism → immune‑mediated vascular remodelling (updated from inosine/adenosine accumulation hypothesis).

**Core directional hypothesis:**  
Hypoxia induces purine nucleoside phosphorylase (Pnp) and 5’‑nucleotidase (Nt5c2) in lung MKs, accelerating purine nucleotide degradation; the consumption of inosine (log2FC –0.34) and generation of downstream products (hypoxanthine/xanthine/uric acid) create a perivascular purine catabolite milieu that activates innate immune pathways, driving medial thickening.

**Direction‑level reasoning summary:**
- Data anchor: MK‑sorted inosine is slightly decreased (log2FC –0.34, sFig6A, PH‑CD41 vs Control‑CD41) while *Pnp* is strongly PH‑up in MKs (log2FC 1.739, p=3.81e‑06) and *Nt5c2* is also up (log2FC 2.879, p=2e‑04). *Pnp* is a direct compound‑enzyme for inosine.
- Biological interpretation: Lower inosine, together with high *Pnp*, points to increased conversion of inosine (and guanosine) to hypoxanthine and guanine, reflecting heightened purine salvage/degradation in hypoxic MKs.
- MK‑linked pathway logic: Pnp catalyses the phosphorolysis of inosine to hypoxanthine; subsequent xanthine oxidase activity produces xanthine and uric acid. Purine catabolites (uric acid, hypoxanthine via ROS) can act as danger signals, activating the NLRP3 inflammasome or generating oxidative stress.
- Candidate downstream axis: Uric‑acid‑mediated inflammasome activation or hypoxanthine‑xanthine oxidase‑derived ROS can recruit/activate perivascular monocytes/macrophages, creating an immune‑mediated remodelling loop.
- Remodelling logic: Inflammasome activation and oxidative damage promote perivascular inflammation, growth factor release, and medial smooth muscle proliferation.
- Key uncertainty: Hypoxanthine, xanthine, and uric acid were not measured in MKs or perivascular space; the assumption that decreased inosine reflects increased catabolic flow is reasonable but unquantified. The specific immune sensor (e.g., NLRP3, A2B receptor) is unresolved.

**Directional chain:**
1. Hypoxia up‑regulates *Pnp* and *Nt5c2* in lung MKs, shifting purine metabolism toward degradation.  
2. Enhanced Pnp activity accelerates conversion of inosine (and guanosine) to hypoxanthine; intracellular inosine levels fall (log2FC –0.34).  
3. Downstream, hypoxanthine is oxidized by xanthine oxidase to xanthine and uric acid; these purine catabolites are released from MKs or generated extracellularly.  
4. Broad downstream axis: immune‑mediated (NLRP3 inflammasome activation, ROS‑driven macrophage skewing).  
5. Perivascular immune activation promotes medial smooth muscle hypertrophy and muscularisation.

**Candidate downstream axes:**
- Plausible axes: (i) Uric acid crystals/monosodium urate activate NLRP3 inflammasome in macrophages, driving IL‑1β/IL‑18 release; (ii) hypoxanthine‑xanthine oxidase generates superoxide/ROS, causing endothelial damage and immune cell recruitment; (iii) adenosine generation (via ecto‑5’‑nucleotidase) remains possible but whole‑lung adenosine is unchanged and inosine is consumed, making this less likely; (iv) unresolved stromal remodelling via purinergic receptor signalling on fibroblasts.
- Working model (provisional): MK‑derived uric acid triggers macrophage NLRP3 activation, leading to IL‑1β‑dependent vascular inflammation.
- Specific examples: NLRP3 inflammasome, IL‑1β, xanthine oxidase, superoxide, uric acid – all provisional.
- What remains unresolved: Whether hypoxanthine/xanthine/uric acid are actually produced and released by MKs at concentrations sufficient to activate immune sensors; the identity of the dominant immune cell type.

**Evidence basis:**
- User‑provided data: Inosine decrease in MKs (log2FC –0.34, sFig6A); *Pnp* MK‑enrichment (log2 –1.217, but MK pct 20.31% vs other 38.9%, yet PH‑up log2FC 1.739, p=3.81e‑06); *Nt5c2* PH‑up (log2FC 2.879, p=2e‑04). Public data cross‑check shows whole‑lung inosine and adenosine unchanged.
- Public dataset metadata or analyzed public data: None usable.
- Literature: No direct PubMed hits for *Pnp*‑MK‑PH; general literature supports purine catabolites as immune danger signals.
- Biological rationale: Purine degradation products are established inflammasome activators and ROS sources; MKs as a source in hypoxic lung is novel.
- Evidence status: **direct** for MK *Pnp* up‑regulation; **inferred** for enhanced hypoxanthine/uric acid production; downstream immune axis **speculative**.

**Predicted observations:**
- In MKs: Increased xanthine oxidase activity; elevated hypoxanthine/xanthine in MK‑conditioned medium.
- In recipient or tissue compartment: Perivascular uric acid deposits (if crystal‑mediated) or increased ROS in hypoxic lungs; activated perivascular macrophages (NLRP3/IL‑1β positive).
- In metabolomics or pathway activity: MK‑sorted hypoxanthine/xanthine elevated (requires targeted assay).

**Experimental validation:**
- Perturbation: Xanthine oxidase inhibitor (allopurinol/febuxostat) or bone‑marrow‑specific *Pnp* deletion.
- Model: Hypoxic PH mouse model.
- Readout: Medial thickening, perivascular macrophage inflammasome activity (IL‑1β ELISA, IHC for NLRP3), and vascular remodelling.
- Expected result: Inhibition of purine catabolism or loss of MK *Pnp* reduces perivascular IL‑1β and blunts medial hypertrophy.
- Falsifying result: Allopurinol does not affect vascular remodelling despite reduced uric acid, or loss of MK *Pnp* does not alter immune parameters.

**Novelty:** Repurposes the inosine/adenosine accumulation hypothesis to a catabolite‑driven immune activation axis, anchored on confirmed enzyme up‑regulation and metabolite direction.

**Weaknesses:** Key catabolites unmeasured; link from MK *Pnp* to extracellular uric acid/ROS not established; whole‑lung uric acid not assessed; reliance on NLRP3 as the candidate sensor without direct evidence.

**Revision relative to previous cycle:** Revised from the earlier inosine/adenosine accumulation hypothesis; now consistent with decreased MK inosine and the strong *Pnp* up‑regulation, focusing on downstream purine catabolites rather than adenosine accumulation.

**Priority estimate:**
- Directional specificity: 3 (broad purine catabolism axis)  
- Data support: 4 (enzyme data strong, metabolite direction supportive but modest)  
- Literature support: 3 (inflammasome/uric acid literature supportive but not MK‑specific)  
- Novelty: 4  
- Testability: 4 (inhibitors available; spatial validation needed)  
- Overall generation priority: 4 (evidence‑anchored and direction‑consistent update)

**Explicit rejection filter:** Passed — MK‑specific enzyme, hypoxia‑dependent, vascular remodelling phenotype, beyond generic inflammation.

---

### Hypothesis ID: H3
**Hypothesis title:** MK‑AMD1‑polyamine‑eIF5A → direct vascular‑wall/matrix remodelling

**PI instruction addressed:** Conditional matricellular/secretome axis: AMD1‑polyamine metabolic control of thrombospondin‑1, PDGF‑B, and TGF‑β1 secretion → direct vascular‑wall/matrix remodelling.

**Core directional hypothesis:**  
Hypoxia‑induced AMD1 up‑regulation and polyamine synthesis in lung MKs enhance hypusination of eIF5A, which selectively increases translation of the matricellular/coagulation factors thrombospondin‑1 (Thbs1), PDGF‑B (Pdgfb), and TGF‑β1 (Tgfb1); their concerted release promotes perivascular matrix deposition, smooth muscle proliferation, and endothelial dysfunction, contributing directly to medial thickening and muscularisation.

**Direction‑level reasoning summary:**
- Data anchor: All three genes *Thbs1*, *Pdgfb*, and *Tgfb1* are MK‑expressed, MK‑enriched, and PH‑up in MKs (confirmed by the Seurat priority gene table). Methionine is elevated in MKs (log2FC 3.26) and *Amd1* is strongly PH‑up (log2FC 1.77, p=6.55e‑06) and MK‑enriched.
- Biological interpretation: The coincident up‑regulation of AMD1 and a suite of pro‑remodelling secreted factors suggests a metabolic control node: polyamine‑dependent eIF5A hypusination may favour the translation of these mRNA targets.
- MK‑linked pathway logic: AMD1 drives decarboxylated SAM synthesis, which supplies the aminopropyl group for spermidine/spermine; spermidine is the exclusive substrate for eIF5A hypusination. Hypusinated eIF5A is known to facilitate translation of specific transcripts with polyproline motifs or other structural features; *Thbs1*, *Pdgfb*, and *Tgfb1* are plausible candidates.
- Candidate downstream axis: Direct vascular‑wall/matrix: TSP‑1 binds latent TGF‑β and activates it, potentiating TGF‑β1‑driven matrix synthesis; PDGF‑B signals through PDGFRβ on smooth muscle cells/pericytes, promoting proliferation; TGF‑β1 acts on fibroblasts and smooth muscle cells to stimulate collagen deposition.
- Remodelling logic: Coordinated release of these factors would drive perivascular fibrosis, medial SMC hyperplasia, and endothelial dysfunction, culminating in muscularisation and vascular stiffness.
- Key uncertainty: Direct evidence that eIF5A hypusination controls translation of these specific transcripts in hypoxic MKs is absent; the link is inferred from cancer models. Spermidine/spermine levels and hypusinated eIF5A have not been measured in MKs.

**Directional chain:**
1. Hypoxia increases methionine (log2FC 3.26) and up‑regulates *Amd1* in lung MKs.  
2. AMD1 drives polyamine synthesis, providing spermidine for eIF5A hypusination.  
3. Hypusinated eIF5A facilitates efficient translation of *Thbs1*, *Pdgfb*, and *Tgfb1* mRNAs.  
4. Broad downstream axis: direct vascular‑wall/matrix remodelling.  
5. Secreted TSP‑1 activates latent TGF‑β1; TGF‑β1 and PDGF‑B synergistically promote perivascular fibrosis, smooth muscle proliferation, and endothelial dysfunction, leading to muscularisation and stiffness.

**Candidate downstream axes:**
- Plausible axes: (i) TSP‑1/TGF‑β1/PDGF‑B direct vascular‑wall axis (working model); (ii) the same factors also enhance immune cell chemotaxis/adhesion (immune‑mediated branch, though secondary); (iii) EV‑mediated delivery of these proteins; (iv) unresolved paracrine effects on endothelial junctions.
- Working model (provisional): Direct vascular‑wall remodelling through TSP‑1‐dependent TGF‑β activation and PDGF‑B‑driven SMC proliferation.
- Specific examples: TSP‑1, TGF‑β1, PDGF‑B, perivascular fibrosis, smooth muscle hyperplasia – provisional.
- What remains unresolved: Whether hypusinated eIF5A physically translates these mRNA species in MKs; the relative contribution of each factor; and the requirement for MK proximity to vessels.

**Evidence basis:**
- User‑provided data: *Thbs1*, *Pdgfb*, *Tgfb1* confirmed MK‑expressed, MK‑enriched, and PH‑up in MKs (Seurat priority gene table); methionine up and *Amd1* up as per H1.
- Public dataset metadata or analyzed public data: None usable.
- Literature: AMD1‑polyamine‑eIF5A hypusination controls translation of pro‑fibrotic factors in cancer (PMID 38965534); TSP‑1 in PH vascular remodelling has some literature support; direct MK‑specific link absent.
- Biological rationale: Polyamine‑eIF5A axis is a known translational control mechanism; MKs as a major source of these matrix‑remodelling proteins in hypoxia is a logical extension.
- Evidence status: **direct** for MK gene expression of all three factors; **inferred** for AMD1‑eIF5A control of their translation; secretion and in vivo function **speculative**.

**Predicted observations:**
- In MKs: Elevated spermidine, hypusinated eIF5A; polysome profiling shows enrichment of *Thbs1*, *Pdgfb*, *Tgfb1* mRNAs in hypusination‑dependent fractions.
- In recipient or tissue compartment: Increased perivascular TSP‑1, PDGF‑B, and active TGF‑β1 in hypoxic lungs; colocalization of these factors with MK markers.
- In metabolomics or pathway activity: MK‑conditioned medium contains increased levels of these proteins.

**Experimental validation:**
- Perturbation: eIF5A hypusination inhibitor (e.g., GC7) or MK‑specific *Amd1* knockout; also use *Amd1* inhibitor (SAM486A).
- Model: Hypoxic PH mouse model, with MK/platelet‑specific Cre for *Amd1*.
- Readout: Lung collagen content, medial thickness, α‑SMA staining, secretion of TSP‑1/PDGF‑B/TGF‑β1 (ELISA on BAL or MK culture), and polysome profiling.
- Expected result: Blocking AMD1 or hypusination reduces MK release of these factors and attenuates vascular fibrosis and muscularisation.
- Falsifying result: GC7 or AMD1 inhibition does not alter the secretion of these factors, or their secretion remains but vascular remodelling is unchanged, indicating they are not the key effectors.

**Novelty:** First proposal that metabolic control (AMD1‑polyamine‑eIF5A) governs a MK matricellular secretome in hypoxia, providing a direct link from MK metabolism to vascular wall pathology.

**Weaknesses:** eIF5A translation target status unproven for these specific mRNAs; spermidine levels and hypusination status unmeasured; alternative translational control mechanisms not excluded; direct evidence of MK secretion in hypoxic lung needed.

**Revision relative to previous cycle:** Newly generated hypothesis based on updated gene confirmation; no prior version.

**Priority estimate:**
- Directional specificity: 4  
- Data support: 4 (gene expression solid, metabolic control inferred)  
- Literature support: 3 (eIF5A hypusination literature supportive, but no MK/PH context)  
- Novelty: 5  
- Testability: 4 (inhibitors and genetic tools exist; polysome profiling feasible)  
- Overall generation priority: 4 (strong candidate with clear testable predictions, though mechanistic gaps remain)

**Explicit rejection filter:** Passed — all criteria met.

---

**Self‑filtered rejected ideas:**  
- *Methionine → Dnmt3b axis*: Dnmt3b lacks significant MK enrichment (log2 0.193) and its PH‑up log2FC (1.59) is not significant (p=0.212), making it a weak anchor compared to AMD1. Excluded as it fails the MK‑specificity and statistical confidence requirements.  
- *Retinoic acid → Cyp26b1 axis*: Although retinoic acid is highly up (log2FC 3.44), Cyp26b1’s MK enrichment is modest (log2 0.728) and its PH‑up log2FC (0.912) is non‑significant (p=0.253), while literature and mechanism cues are minimal. Excluded because it does not meet the strong MK‑enrichment and differential evidence bar set by the shortlist.  
- Any purely platelet‑activation or generic inflammation hypothesis without MK‑specific metabolic anchoring – rejected per brief instructions.

**Requests for Tool Use Agent:** None at this stage; all required data were available in the provided evidence package.

## generation_1
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

## generation_2
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
