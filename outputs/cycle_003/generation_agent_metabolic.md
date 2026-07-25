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
