**Axis 1: MK‑AMD1‑polyamine → immune‑mediated vascular remodelling**  
(merged from generation_metabolic H1, generation_1 H1, generation_2 H1)

**Review decision:** *Promising but incomplete*

**Directional assessment:**
- **Strengths:**  
  - Strong metabolite‑enzyme‑expression chain: methionine accumulation (log2FC +3.26) in PH‑MKs and *Amd1* MK‑enrichment (log2 1.35) with highly significant PH‑upregulation (log2FC +1.77, p=6.6e‑06) are directly observed.  
  - Plausible metabolic logic: elevated methionine and *Amd1* would promote polyamine synthesis; this axis is well‑established in other contexts (cancer, immunology).  
  - Clearly positioned as broad immune‑mediated remodelling, with multiple candidate downstream routes (T‑cell/Th17‑like, macrophage polarization) explicitly labelled as provisional.  
- **Weaknesses:**  
  - The key polyamine products (spermidine/spermine) were not measured, so the entire chain from *Amd1* induction to functional polyamine output is inferred.  
  - The mechanism by which MK‑derived polyamines act on immune cells – free secretion, vesicle packaging, or indirect cytokine induction – is entirely unresolved.  
  - No spatial evidence exists that MKs are near perivascular T‑cells/macrophages or that polyamine concentrations in the local niche are sufficient to alter immune programmes.  
- **Reasoning quality:** Good at the broad‑axis level. The authors correctly identify the missing spermidine/spermine data and avoid over‑claiming (e.g., “Th17‑like tone” is labelled as a provisional example). The logical flow from substrate/enzyme to candidate downstream axis is sound, though it jumps from MK metabolites to immune outcomes without a concrete mediator.  
- **Appropriate resolution:** Direction‑level. The hypothesis appropriately refrains from specifying a single cytokine, receptor, or immune subset, acknowledging that evidence only supports a broader immunological direction.

**Evidence assessment:**
- **User‑provided data:** Direct support for MK methionine fold change and *Amd1* expression (Seurat table, metabolite cross‑check).  
- **Public data:** None – the retrieved datasets (GSE289322, GSE291455) are unusable; whole‑lung transcriptomic support is absent.  
- **Literature:** Minimal. The cited papers (PMID 38965534, 28658205) link AMD1‑polyamine‑eIF5A to cancer, not PH or MKs; polyamine‑immune interactions are known but not in the lung perivascular context.  
- **Inference:** Spermidine/spermine accumulation, MK polyamine export, and immune cell modulation are all inferred from the enzyme/metabolite data. The link to Th17‑like tone, IL‑17, or macrophage NLRP3 is speculative.  
- **Speculation:** Any claim of a specific immune effector (e.g., “IL‑17 from Th17 cells drives VSMC activation”) goes beyond the data and must be treated as speculative. The hypothesis largely maintains appropriate caution.

**Major concerns:**
- The hypothesis rests entirely on the assumption that *Amd1* upregulation leads to functionally relevant polyamine output, yet polyamines are not quantified. This gap is critical for falsifiability.  
- MK‑origin specificity is partially weakened because *Amd1* is expressed in other lung cells; the PH‑upregulation is MK‑specific in the dataset, but without cell‑type‑specific deletion it is difficult to attribute function solely to MKs.  
- The immune axis is broad; a pharma‑logical inhibitor of AMD1 might have systemic effects, complicating interpretation of immune changes.

**Downstream‑axis assessment:**
- **Broad axis:** Immune‑mediated – polyamines shape perivascular T‑cell/macrophage activity.  
- **Candidate examples:** Th17‑like polarization, macrophage M1/M2 shift, NLRP3 inflammasome priming, arginase‑1 induction.  
- **What remains unresolved:** Which immune cell type(s) are the primary responders; which polyamine species (spermidine vs. spermine) is responsible; whether polyamines act directly or through altered MK secretome (eIF5A‑dependent translation).  
- **MK‑origin gap:** Polyamine secretion from MKs has not been demonstrated; it is not known whether MKs export polyamines or retain them.  
- **Direction‑specific falsification:** If MK‑specific *Amd1* deletion fails to reduce lung polyamine levels or does not alter perivascular immune composition, the hypothesis would be falsified. The provided falsification criterion (no change in immune infiltration despite polyamine reduction) is appropriate.

**Required revisions:**
- Explicitly state that spermidine/spermine measurement is a necessary prerequisite for validating the metabolic arm.  
- Emphasize that MK‑conditioned medium or perivascular fluid must be profiled to confirm polyamine export.  
- The working model should be clearly separated from the direction: “polyamines → immune modulation” is the testable direction; any mention of Th17, IL‑17, etc., must carry a stronger “provisional” label.  
- Add a note that the role of AMD1 in other lung cells cannot be ruled out without cell‑type‑specific KO, but that MK‑targeted experiments are proposed.

**Experimental critique:**
- **Strong points:** Well‑defined perturbation (MK‑specific *Amd1* KO), clear vascular remodelling readouts, and built‑in falsification.  
- **Weak points:** The experimental design does not include direct polyamine measurements or assays of immune cell function (e.g., cytokine production); without these, a negative result could be due to lack of polyamine change rather than pathway irrelevance.  
- **Missing controls:** A control for off‑target AMD1 inhibition in other cells; measurement of spermidine/spermine in MKs and lung tissue; demonstration that KO actually reduces polyamine levels.  
- **Falsification criteria:** As stated, if polyamine levels remain unchanged despite *Amd1* deletion, the hypothesis is weakened. The proposed criterion (no effect on immune composition/remodelling) is valid.

**Final recommendation to PI:** *Revise* – strengthen by incorporating explicit polyamine measurement endpoints and by distinguishing the core directional hypothesis from the illustrative candidate examples. The axis is highly promising but currently incomplete due to missing product‑level evidence.  

---

**Axis 2: MK‑Pnp‑purine catabolism → immune‑mediated vascular remodelling**  
(merged from generation_metabolic H2, generation_1 H2, generation_2 H2)

**Review decision:** *Promising but incomplete*

**Directional assessment:**
- **Strengths:**  
  - The updated interpretation correctly abandons the adenosine‑accumulation model and uses the decreased inosine (log2FC –0.34) and strong *Pnp* upregulation (log2FC +1.74, p=3.8e‑06) to propose accelerated purine catabolism.  
  - *Nt5c2* upregulation provides additional support for nucleotide degradation.  
  - The proposed downstream axis (hypoxanthine/xanthine/uric acid via xanthine oxidase → ROS/NLRP3 activation) is directionally plausible and consistent with known purine catabolite‑driven inflammation.  
- **Weaknesses:**  
  - *Pnp* is not MK‑enriched in absolute terms (enrichment log2 –1.22, meaning lower expression in MKs than in other lung cells). While it is still PH‑up in MKs, the lack of MK specificity weakens the claim that MKs are the dominant source of purine catabolism.  
  - The critical downstream metabolites (hypoxanthine, xanthine, uric acid) were not measured, and the inosine decrease is modest; this makes the directionality less certain than for the methionine/AMD1 chain.  
  - The axis requires xanthine oxidase activity to generate ROS; evidence for xanthine oxidase expression or activity in the perivascular niche is lacking.  
  - The immune‑mediated outcome is again broad and relies on NLRP3 as the provisional sensor; other purinergic receptors (e.g., A2B, P2X7) or direct oxidative damage could also be involved, adding ambiguity.  
- **Reasoning quality:** Solid at the level of reframing the Pnp‑inosine data. The hypothesis correctly identifies the inferential leap from enzyme upregulation to hypoxanthine/uric acid production and explicitly acknowledges the missing metabolite measurements.  
- **Appropriate resolution:** Direction‑level; the authors do not over‑specify the ROS source or immune sensor beyond working models.

**Evidence assessment:**
- **User‑provided data:** Direct for *Pnp* and *Nt5c2* upregulation; directionally supportive for inosine decrease. Whole‑lung inosine/adenosine unchanged is consistent with a local effect.  
- **Public data:** None usable.  
- **Literature:** No direct citations connecting Pnp, MKs, and PH. The link between uric acid/ROS and NLRP3 is well‑established in immunology, but that is a generic mechanism, not validated here.  
- **Inference:** Enhanced hypoxanthine production, xanthine oxidase activity, and subsequent ROS/inflammasome activation are all inferred from the enzyme and inosine data.  
- **Speculation:** Statements that “MK‑derived uric acid triggers macrophage NLRP3” are speculative; the hypothesis handles this by labeling NLRP3 as provisional.

**Major concerns:**
- The low MK enrichment of *Pnp* (log2 –1.2) raises the possibility that other lung cells (e.g., macrophages, endothelial cells) are the primary sites of purine catabolism, potentially overshadowing any MK contribution. The hypothesis would benefit from demonstrating that the MK‑specific fraction of PNP activity is functionally relevant.  
- The missing hypoxanthine/xanthine/uric acid data make it impossible to distinguish between ROS‑dependent and purinergic receptor‑dependent mechanisms, muddying the falsification design.  
- The immune axis (e.g., NLRP3, IL‑1β) is similar to that proposed for Axis 1; without clear discriminating evidence, it may be difficult to attribute remodelling specifically to this pathway versus the polyamine axis.

**Downstream‑axis assessment:**
- **Broad axis:** Immune‑mediated – purine catabolites (hypoxanthine/xanthine/uric acid + ROS) activate perivascular innate immune cells.  
- **Candidate examples:** NLRP3 inflammasome activation, IL‑1β release, ROS‑driven macrophage polarization, uric acid as a DAMP.  
- **What remains unresolved:** The relative contribution of ROS vs. uric acid crystals; the identity of the exact immune sensor (NLRP3, AIM2, P2X7); whether MKs are the dominant source.  
- **MK‑origin gap:** Pnp is not MK‑specific; other cells may contribute. Additionally, it is unclear whether MKs export hypoxanthine or uric acid, or whether these products are generated extracellularly after nucleoside release.  
- **Direction‑specific falsification:** MK‑specific *Pnp* deletion or allopurinol treatment would test the catabolic arm. A falsifying result would be no reduction in perivascular ROS/IL‑1β and no attenuation of remodelling. However, because Pnp is not exclusive to MKs, an MK‑specific KO might yield a negative result even if the pathway is active in other cells, complicating interpretation.

**Required revisions:**
- Explicitly address the low MK enrichment of *Pnp* and propose how to distinguish MK‑derived purine catabolism from that of other lung cells (e.g., using MK‑specific KO).  
- Emphasize that direct measurement of hypoxanthine/xanthine/uric acid in MK‑conditioned medium or perivascular fluid is a prerequisite.  
- The downstream immune mechanism should be labeled as “ROS/inflammasome or purinergic” rather than focused on NLRP3 alone, to reflect the evidence gap.  
- The working model should be presented as one of several possible routes, with a clear statement that the specific immune sensor is unresolved.

**Experimental critique:**
- **Strong points:** Use of MK‑specific *Pnp* KO and xanthine oxidase inhibitors provides a clean reductionist approach.  
- **Weak points:** Without measuring purine catabolites, it will be unclear whether the intervention actually alters the metabolic endpoint. The modest inosine decrease may mean the catabolic flux is small; negative results could be due to insufficient flux rather than pathway irrelevance.  
- **Missing controls:** Measurement of hypoxanthine, xanthine, and uric acid in lung tissue and MKs; assessment of xanthine oxidase activity; control for systemic effects of allopurinol.  
- **Falsification criteria:** Adequate in principle but would need to be refined to include metabolite benchmarks.

**Final recommendation to PI:** *Revise* – the axis is directionally consistent and a legitimate update of the previous adenosine hypothesis. However, it faces significant challenges with MK specificity and the lack of product‑level data. Consider pairing with Axis 1 as complementary immune mechanisms, but note that both require extensive metabolite validation before functional studies.

---

**Axis 3: MK‑AMD1‑polyamine‑eIF5A → direct vascular‑wall/matrix remodelling**  
(merged from generation_metabolic H3, generation_1 H3, generation_2 H3)

**Review decision:** *Promising but incomplete*

**Directional assessment:**
- **Strengths:**  
  - All three matricellular genes (*Thbs1*, *Pdgfb*, *Tgfb1*) are confirmed as MK‑expressed, MK‑enriched, and PH‑up in MKs, providing a very strong gene‑expression foundation.  
  - The metabolic anchor (methionine/AMD1) is identical to Axis 1, so the metabolic portion is equally well‑supported.  
  - The concept that eIF5A hypusination selectively enhances translation of pro‑remodelling proteins is biologically plausible and supported by cancer literature, though not in MKs.  
  - The downstream axis – direct vascular‑wall/matrix remodelling – is coherent and avoids over‑resolution by presenting multiple cooperative effects.  
- **Weaknesses:**  
  - The entire translational control mechanism (AMD1 → spermidine → eIF5A hypusination → translation of specific mRNAs) is inferred; spermidine levels, eIF5A hypusination status, and polysome profiling for these transcripts have not been performed.  
  - It is not known whether these mRNAs contain the motifs that confer eIF5A‑dependent translation; this is a critical gap in the reasoning chain.
