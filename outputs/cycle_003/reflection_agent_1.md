### Generation_metabolic H1

**Hypothesis ID:** generation_metabolic H1  
**Title:** MK‑AMD1‑polyamine → immune‑mediated vascular remodelling

**Review decision:** Promising but incomplete

**Directional assessment:**
- **Strengths:**  
  Clear, well‑defined metabolite‑enzyme‑MK expression chain: methionine (MK log2FC 3.26) → SAM/dcSAM → AMD1 (MK‑enriched log2 1.35, PH‑up log2FC 1.77, p=6.55e‑06) → polyamine synthesis. The axis explicitly links MK‑specific metabolic reprogramming to an immune‑mediated vascular remodelling outcome. Hypothesis respects the required direction‑level resolution.
- **Weaknesses:**  
  Spermidine/spermine levels not measured; the causal link from MK polyamine export to perivascular immune cell modulation is entirely inferred. MK spatial proximity to T‑cells/macrophages not established. The specific immune effector (Th17, macrophage subset) remains unspecified, as appropriate, but the immune‑mediated label is broad.
- **Reasoning quality:**  
  Excellent. The direction‑level reasoning summary clearly walks from data anchor (methionine, *Amd1*) to biological interpretation (polyamine flux), MK‑linked pathway logic, candidate immune axis, and remodelling phenotype, while explicitly naming key uncertainties (missing spermidine/spermine, unknown transfer mechanism, eIF5A link inferred).
- **Appropriate resolution:**  
  Yes. It stays at a directional, broad immune‑mediated axis with provisional examples (Th17‑like tone, macrophage activation). Does not over‑claim a specific cytokine or receptor.

**Evidence assessment:**
- **User‑provided data:** Direct support: MK methionine elevation (log2FC 3.26) and *Amd1* up‑regulation (log2FC 1.77, p=6.55e‑06). Both are from the Cycle‑3 evidence tables.
- **Public data:** None usable; correctly noted.
- **Literature:** AMD1‑polyamine‑eIF5A in cancer (indirect); no lung‑PH‑MK context. Evidence level: indirect.
- **Inference:** Polyamine accumulation, eIF5A hypusination, and downstream immune modulation are inferred from the enzyme/substrate shift. Acceptable for a direction‑level hypothesis.
- **Speculation:** Perivascular Th17‑like polarisation and IL‑17‑dependent medial activation are speculative but clearly labelled as provisional working models.

**Major concerns:**
- The entire polyamine arm is extrapolated from methionine and *Amd1* without any direct measurement of spermidine or spermine. This gap weakens the central chain.
- The mechanism by which MK‑derived polyamines would reach and alter immune cells (free export, vesicle‑mediated, or eIF5A‑dependent cytokine translation) is unresolved and will be critical for functional validation.

**Downstream‑axis assessment:**
- **Broad axis:** Immune‑mediated.
- **Candidate examples:** Th17‑like tone, macrophage M1‑like polarisation; all provisional.
- **What remains unresolved:** Whether the immune response is driven by direct polyamine action or by polyamine‑dependent MK secretome (e.g., cytokines); which immune cell type is the immediate responder.
- **MK‑origin gap:** No direct evidence that MKs are the dominant source of polyamines in the perivascular niche or that their deletion alters local polyamine levels.
- **Direction‑specific falsification:** Testable via MK‑specific *Amd1* deletion or AMD1 inhibitor; if loss of MK AMD1 does not alter perivascular immune composition or vascular remodelling, the axis is falsified.

**Required revisions:**
- None; the hypothesis is already well‑structured, and its gaps are explicitly acknowledged. For a merged version, retain the clarity on inferred polyamine synthesis and the working model’s provisional status.

**Experimental critique:**
- **Strong points:**  
  Perturbation (MK‑specific *Amd1* KO, SAM486A) is feasible; readouts (immune cell profiling, medial thickness) are standard; the hypothesis makes a clear falsifiable prediction (loss of AMD1 blunts immune‑driven remodelling).
- **Weak points:**  
  No direct assay for spermidine/spermine or eIF5A hypusination is proposed as a primary readout. The experimental plan would benefit from quantifying MK polyamine release and hypusinated eIF5A to establish the biochemical intermediate.
- **Missing controls:**  
  Non‑MK‑derived polyamine sources should be considered; use of global polyamine synthesis inhibitors (DFMO) as a control for systemic effects. Confirm that MK‑specific deletion does not alter MK numbers or bone marrow function.
- **Falsification criteria:**  
  MK‑specific AMD1 loss fails to reduce lung polyamine levels, perivascular immune cell skewing, or medial thickening; or polyamine supplementation rescues the phenotype independent of MK AMD1.

**Final recommendation to PI:**  
Advance after merging with the other AMD1‑immune hypotheses (generation_1 H1, generation_2 H1). The merged version will be a solid direction‑level immune‑mediated axis.

---

### Generation_1 H1

**Hypothesis ID:** generation_1 H1  
**Title:** MK‑AMD1‑polyamine → paracrine immune‑mediated vascular remodelling

**Review decision:** Promising but incomplete (nearly identical to gen_metabolic H1; merge)

**Directional assessment:**
- **Strengths:** Same strong data anchor. Explicitly frames the hypothesis as a **paracrine ligand‑receptor mechanism**, highlighting the secretion of polyamines or polyamine‑modulated cytokines. This adds a useful mechanistic nuance. Direction‑level reasoning is clear and evidence‑based.
- **Weaknesses:** Identical gap: spermidine/spermine not measured; no evidence of MK secretion. The paracrine emphasis does not provide new data; the overall strength is the same as the other Cluster 1 hypotheses.
- **Reasoning quality:** High. The chain methionine→SAM→dcSAM via AMD1→spermidine/spermine is well described. Candidate downstream axes include immune cell uptake and eIF5A‑dependent cytokine secretion, staying provisional. The logic linking methionine accumulation (without a corresponding SAM rise) to polyamine diversion is a neat biological insight.
- **Appropriate resolution:** Yes, remains direction‑level. The paracrine ligand‑receptor frame is useful but does not over‑resolve.

**Evidence assessment:**  
Same as gen_metabolic H1: direct support for methionine and *Amd1*; inferred for polyamine products; immune axis speculative.

**Major concerns:**  
None beyond those already listed for the cluster: missing polyamine measurements, unknown transport, and untested immune cell targeting.

**Downstream‑axis assessment:**  
- Broad axis: Immune‑mediated.
- Candidate examples: Polyamine uptake → Th17‑like T‑cells; polyamine‑dependent cytokine secretion (eIF5A); all provisional.
- MK‑origin gap: Unresolved.
- Direction‑specific falsification: As before, MK‑specific *Amd1* ablation or DFMO should block remodelling; if polyamines are not the key secreted factor, the paracrine model fails.

**Experimental critique:**  
Similar to gen_metabolic H1; no additional experimental insights.

**Final recommendation to PI:**  
Merge into a single AMD1‑polyamine immune axis.

---

### Generation_2 H1

**Hypothesis ID:** generation_2 H1  
**Title:** MK AMD1‑polyamine → immune‑mediated pulmonary vascular remodelling

**Review decision:** Promising but incomplete (merge)

**Directional assessment:**
- **Strengths:** Clearly states the data anchor and explicitly notes that MK methionine is up but whole‑lung methionine is decreased, strengthening MK specificity. The direction‑level reasoning is sound, and the hypothesis flags that spermidine/spermine are not measured.
- **Weaknesses:** No substantive difference from the other two. Slightly less detail on the intermediate SAM/dcSAM logic, but still accurate.
- **Reasoning quality:** Good. The candidate downstream axes (Th17, macrophage polarisation, NLRP3 priming) are appropriately labelled as provisional.
- **Appropriate resolution:** Yes.

**Evidence assessment:** Same as others.

**Major concerns:** Same gap: polyamine levels absent.

**Downstream‑axis assessment:** Consistent with cluster.

**Experimental critique:** Same as others.

**Final recommendation to PI:** Merge.

---

### Generation_metabolic H2

**Hypothesis ID:** generation_metabolic H2  
**Title:** MK‑Pnp‑purine catabolism → immune‑mediated vascular remodelling

**Review decision:** Promising but incomplete

**Directional assessment:**
- **Strengths:** Correctly updates the previous inosine/adenosine hypothesis. Uses the new inosine data (log2FC –0.34) to argue for accelerated purine catabolism rather than accumulation. The chain inosine decrease + *Pnp* up (log2FC 1.74, p=3.81e‑06) + *Nt5c2* up (log2FC 2.88) is mechanistically coherent. The hypothesis stays at direction‑level, proposing broad immune‑mediated remodelling via hypoxanthine/xanthine/uric acid and ROS.
- **Weaknesses:** Hypoxanthine, xanthine, uric acid, and ROS were not measured; the shift from inosine drop to catabolite build‑up is inferred. The immune effector (NLRP3, IL‑1β) is provisional. MK enrichment of *Pnp* is negative (log2 –1.217), meaning expression is lower than other cells, though the PH‑up within MKs is strong; this may raise questions about MK‑specific contribution.
- **Reasoning quality:** Very good. The direction‑level summary integrates the enzyme data and the directional metabolite change, offers a plausible remodeled interpretation, and clearly notes the key uncertainties (catabolites unmeasured, immune sensor unresolved).
- **Appropriate resolution:** Yes, remains at broad immune‑mediated axis, with candidate examples.

**Evidence assessment:**
- **User‑provided data:** Direct: MK inosine decrease (log2FC –0.34), *Pnp* PH‑up in MKs (1.74, p=3.81e‑06), *Nt5c2* PH‑up (2.88). Whole‑lung inosine/adenosine unchanged, supporting a localised MK effect.
- **Public data:** None usable.
- **Literature:** General literature on purine catabolites as danger signals (uric acid, NLRP3); no direct PH‑MK link. Indirect.
- **Inference:** Production of hypoxanthine/xanthine/uric acid and ROS is inferred from enzyme induction and substrate consumption; no direct measurement.
- **Speculation:** NLRP3 inflammasome activation and IL‑1β‑driven remodelling are plausible but provisional.

**Major concerns:**
- The central catabolites (hypoxanthine, xanthine, uric acid) were not measured, leaving the proposed catabolic flow hypothetical. The decrease in inosine is modest (–0.34) and could be due to other processes.
- *Pnp* is not MK‑specific; its expression is lower in MKs than in other lung cells, which complicates the claim of MK‑driven purine catabolism in the per
