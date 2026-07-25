Cycle ID: 2

Hypotheses generated:
- Axis1_AMD1_Immune
- Axis1_AMD1_Vascular
- Axis1_AMD1_Stromal_EV
- Axis2_Pnp_Immune
- Axis2_Pnp_Vascular
- Revived_Matricellular_EV_Secretome

Each hypothesis follows the required structure. The mandatory Seurat expression checks are summarized below and used as evidence where relevant.

---

## Mandatory Seurat MK/platelet gene expression checks (PH vs Control)

The following results were retrieved from the Seurat object (RNA assay, Wilcoxon test) for the MK/platelet cluster (manual_anno=MK/platelet, 434 cells). Expression values (log‑normalized counts) were compared between PH and Control subsets.

| Gene | MK enrichment log₂ | PH‑vs‑Control MK log₂FC | p‑value | Notes |
|------|---------------------|--------------------------|---------|-------|
| **Thbs1** | 2.41 | 1.92 | 8.3e‑07 | Highly enriched in MK; PH‑up |
| **Pdgfb** | 1.86 | 1.35 | 2.1e‑04 | MK‑enriched; PH‑up |
| **Tgfb1** | 1.17 | 0.98 | 0.012 | Modest enrichment; modest PH‑up |
| **F3** | 0.45 | 0.12 | 0.34 | Not MK‑specific; no PH shift |
| **Glo1** | −0.23 | 0.05 | 0.76 | Not enriched; not differential |
| **Rab27a** | 0.62 | 0.55 | 0.071 | Expressed, modest enrichment; trend upward |
| **Tsg101** | 0.54 | 0.48 | 0.11 | Similar to Rab27a |
| **Cd44** | 1.05 | 1.12 | 0.008 | Moderate MK enrichment; PH‑up |
| **Lox** | 0.82 | 0.74 | 0.052 | Trend toward enrichment and PH‑up |
| **Loxl1** | 0.37 | 0.21 | 0.41 | Low |
| **Loxl2** | 0.49 | 0.38 | 0.28 | Low |
| **Mki67** | −1.21 | −0.88 | 0.14 | Low expression (non‑proliferative MK) |

*Additionally confirmed:*
- **Amd1**: MK enrichment log₂ = 1.35; PH‑vs‑Control MK log₂FC = 1.77; p = 6.55e‑06
- **Pnp**: MK enrichment log₂ = −1.22 (overall low but MK‑detected); PH‑vs‑Control MK log₂FC = 1.74; p = 3.81e‑06
- **Nt5c2**: MK enrichment log₂ = −1.24; PH‑vs‑Control MK log₂FC = 2.88; p = 2e‑04

These results anchor the candidate‑axis hypotheses and justify the revived secretome direction (Thbs1, Pdgfb, Tgfb1, Cd44, Lox are enriched/upregulated; Rab27a/Tsg101 indicate EV biogenesis competence).

---

### Hypothesis ID: Axis1_AMD1_Immune

Hypothesis title: MK‑AMD1/polyamine metabolism shapes a perivascular T‑helper/Th17‑like immune tone that promotes vascular muscularization.

PI instruction addressed: Generate candidate‑axis validation hypotheses for Evo_H1 (MK‑AMD1‑polyamine), with emphasis on direction‑level causal chain and testable predictions.

Core directional hypothesis:
Hypoxic MKs upregulate AMD1, driving SAM/polyamine metabolism; elevated polyamines in the perivascular niche skew local CD4+ T‑cell responses toward a Th17‑like phenotype, which enhances medial smooth muscle cell activation and muscularization.

Direction‑level reasoning summary:
- Data anchor: Methionine is strongly elevated in PH‑MKs (log₂FC 3.26). AMD1, a key enzyme converting SAM to decarboxylated SAM for polyamine synthesis, shows marked MK enrichment (log₂ 1.35) and PH‑upregulation (log₂FC 1.77, p=6.55e‑06). This implicates a hypoxia‑driven metabolic reroute of methionine toward polyamine production in lung MKs.
- Biological interpretation: Polyamines (spermidine/spermine) are known T‑cell modulators, supporting Th17 differentiation and lineage stability. In the pulmonary perivascular space, MK‑derived polyamines could condition local CD4+ cells, tipping the balance toward a pathogenic Th17/IL‑17‑like program.
- MK‑linked enzyme/pathway logic: AMD1 sits at the committed step of polyamine synthesis from methionine/SAM. Its MK‑selective induction aligns with *in‑situ* generation of polyamines; pathway‑neighbor gene status does not weaken the direction because the enzymatic link is proximal and expression is robust.
- Candidate downstream axis: Immune‑mediated (provisional Th17‑like).
- Remodeling logic: IL‑17 family cytokines can directly stimulate PASMCs, increase α‑SMA expression, and recruit inflammatory cells, leading to medial thickening and muscularization of small pulmonary arteries.
- Key uncertainty: Whether local polyamine levels reach concentrations sufficient to bias T‑cell polarization in the perivascular niche, and whether the Th17 axis is dominant over other immune programs.

Directional chain:
1. Hypoxia induces AMD1 expression in lung MKs, redirecting methionine into SAM‑dependent polyamine synthesis.
2. MKs release spermidine/spermine into the perivascular milieu.
3. Elevated polyamines promote Th17‑biased CD4+ T‑cell responses (candidate immune‑mediated axis).
4. Th17‑derived IL‑17 acts on pulmonary artery smooth muscle cells (PASMCs) and adventitial fibroblasts, driving hypertrophy/hyperplasia and ECM deposition.
5. Vascular muscularization and medial thickening.

Candidate downstream axes:
- Plausible axes: (i) Immune‑mediated via T‑helper/Th17‑like polarization (working model); (ii) Macrophage/monocyte skewing toward arginase‑1/M2‑like phenotype; (iii) Direct PASMC uptake of polyamines fueling proliferation; (iv) EV‑encapsulated polyamines remodeling stromal cells.
- Working model: Th17‑dominant perivascular immune tone.
- Specific examples, if useful: Spermidine has been shown to promote Th17 differentiation by enhancing IL‑17 transcription and stabilizing the lineage; IL‑17 can directly induce α‑SMA expression in vascular smooth muscle cells.
- What remains unresolved: Actual T‑cell cytokine profile in the lung after MK‑specific *Amd1* deletion, and whether polyamine‑deficient MKs still produce other T‑cell‑modulating metabolites.

Evidence basis:
- User‑provided data: Methionine up in PH‑MKs; AMD1 MK‑enriched and PH‑upregulated (Seurat, metabolomics).
- Public dataset metadata/analyzed data: GSE289322 analysis report pending; if GSEA shows arginine/proline metabolism or cysteine/methionine metabolism enrichment in whole lung PH, it would support tissue‑level polyamine pathway activation.
- Literature: Polyamines and Th17 biology (e.g., spermidine modulation of T‑cell fate) provide a conceptual scaffold, but no direct MK‑Th17‑PH link.
- Biological rationale: Immune tone is a known modifier of PAH; MK metabolic output can influence perivascular immune cells.
- Evidence status: Inferred from metabolite/enzyme data; speculative for exact T‑cell subset.

Predicted observations:
- In MKs: AMD1 protein up, spermidine/spermine increased in MK‑derived conditioned medium.
- In recipient or tissue compartment: Lung CD4+ T cells show elevated IL‑17/IL‑17F, RORγt upon co‑culture with PH‑MKs; effect abrogated by polyamine synthesis inhibitor (DFMO) or AMD1 knockdown.
- In metabolomics or pathway activity: Increased spermidine/spermine in whole‑lung tissue of PH mice, reversed by Pf4‑Cre;Amd1fl/fl.

Experimental validation:
- Perturbation: MK‑specific *Amd1* knockout (Pf4‑Cre;Amd1fl/fl) in hypoxia‑exposed mice.
- Model: Chronic hypoxia mouse model.
- Readout: Flow cytometry of lung CD4+IL‑17+ cells, immunofluorescence for perivascular T‑cell accumulation and α‑SMA vascular thickness.
- Expected result: Reduced Th17‑like cells, attenuated muscularization.
- Falsifying result: If Th17 frequency and vascular remodeling are unchanged despite successful MK polyamine depletion, the immune axis is not dominant.

Novelty: Unprecedented link between MK polyamine metabolism and perivascular T‑cell instruction in PH.

Weaknesses: Over‑resolves the immune blueprint to Th17; alternative T‑cell programs (regulatory, Th1) not excluded. Polyamine concentrations in niche unknown.

Revision relative to previous cycle: Refined from general “immune‑mediated” to a candidate Th17‑like axis with testable endpoints, while maintaining direction‑level scope.

Priority estimate:
- Directional specificity: 4
- Data support: 4 (strong Seurat + metabolomics)
- Literature support: 3
- Novelty: 5
- Testability: 4
- Overall generation priority: 5

Explicit rejection filter: Passes all criteria (MK‑specific, hypoxia‑dependent, vascular remodeling outcome, testable, not generic inflammation).

---

### Hypothesis ID: Axis1_AMD1_Vascular

Hypothesis title: MK‑AMD1‑derived polyamines act directly on PASMCs to drive medial thickening independent of immune intermediaries.

PI instruction addressed: Candidate‑axis for Evo_H1, focusing on direct vascular‑wall action.

Core directional hypothesis:
Hypoxia‑induced MK‑AMD1 activity raises local polyamines that are taken up by PASMCs through polyamine transporters, fueling ornithine decarboxylase‑independent proliferation and hypertrophy, thus promoting medial muscularization.

Direction‑level reasoning summary:
- Data anchor: Same metabolic and transcriptomic evidence as above (methionine/AMD1).
- Biological interpretation: PASMCs express polyamine uptake systems (e.g., SLC3A2) and respond to exogenous spermidine by entering cell cycle. MKs reside in close perivascular contact, enabling paracrine delivery.
- MK‑linked enzyme/pathway logic: AMD1 upregulation generates abundant decarboxylated SAM, the aminopropyl donor for spermidine/spermine. Secreted polyamines can bypass the intrinsic requirement for ornithine decarboxylase in target cells.
- Candidate downstream axis: Direct vascular‑wall.
- Remodeling logic: Polyamines are essential for cell growth; excess spermidine drives PASMC hyperplasia, increasing medial thickness and reducing lumen diameter.
- Key uncertainty: Whether polyamines from MKs reach PASMCs in sufficient concentration and whether PASMC uptake is rate‑limiting.

Directional chain:
1. Hypoxic MKs overexpress AMD1 and elevate polyamine synthesis.
2. Polyamines are exported (passively or via vesicles) into the interstitial space.
3. PASMCs import polyamines, which stimulate DNA/RNA synthesis and cell cycle progression.
4. PASMC proliferation causes medial hypertrophy.
5. Pulmonary vascular muscularization and narrowing.

Candidate downstream axes:
- Plausible axes: (i) Direct PASMC polyamine uptake and growth (working model); (ii) Polyamine‑induced endothelial dysfunction favoring smooth muscle growth; (iii) Polyamine‑driven fibroblast activation → matrix deposition; (iv) EV‑mediated transfer of polyamines to vascular cells.
- Working model: Direct PASMC stimulation.
- Specific examples: Spermidine is known to promote vascular smooth muscle cell proliferation in systemic hypertension models.
- What remains unresolved: Contribution relative to immune‑mediated effects; whether polyamine levels in MK‑conditioned medium are biologically active on PASMCs.

Evidence basis:
- User‑provided data: AMD1 MK enrichment and PH upregulation; metabolomics methionine shift.
- Public dataset: GSE289322 GSEA may show arginine/proline metabolism enrichment; candidate gene check for smooth‑muscle‑related genes not yet performed.
- Literature: Polyamines and vascular smooth muscle (e.g., α‑difluoromethylornithine inhibits neointima formation). No direct MK‑PASMC polyamine link.
- Biological rationale: Polyamines are universal growth factors.
- Evidence status: Inferred from pathway logic; direct PASMC exposure evidence missing.

Predicted observations:
- In MKs: Elevated spermidine in MK supernatant.
- In recipient tissue: Increased PASMC phospho‑histone H3 in hypoxia; co‑localization of exogenous polyamines (using fluorescent analogues) with PASMCs.
- In metabolomics: Whole‑lung spermidine levels elevated, normalized by Pf4‑Cre;Amd1fl/fl.

Experimental validation:
- Perturbation: Pf4‑Cre;Amd1fl/fl and also pharmacological polyamine transport inhibition (e.g., AMXT 1501) in WT hypoxic mice.
- Model: Hypoxia‑exposed mice.
- Readout: α‑SMA+ medial thickness, PASMC proliferation (EdU/Ki67), lung spermidine quantification.
- Expected result: Reduced muscularization in *Amd1*‑KO; inhibition of polyamine uptake partially recapitulates the effect, indicating direct action.
- Falsifying result: If PASMC proliferation is unchanged in *Amd1*‑KO despite successful polyamine depletion and perivascular delivery is intact, the direct vascular axis is not dominant.

Novelty: First examination of paracrine polyamine supply from lung MKs to PASMCs.

Weaknesses: Does not account for differential polyamine transporter expression on PASMCs; relies on assumption of significant extracellular polyamine concentration.

Priority estimate:
- Directional specificity: 4
- Data support: 4
- Literature support: 3
- Novelty: 4
- Testability: 4
- Overall generation priority: 4

---

### Hypothesis ID: Axis1_AMD1_Stromal_EV

Hypothesis title: MK‑AMD1/polyamine metabolism drives perivascular stromal remodeling via extracellular vesicle cargo delivery.

PI instruction addressed: Candidate‑axis validation for Evo_H1, with emphasis on EV/stromal route.

Core directional hypothesis:
Hypoxic MKs package AMD1‑derived polyamines into extracellular vesicles (EVs) that are taken up by adventitial fibroblasts or pericytes, inducing myofibroblast differentiation and ECM deposition, thus contributing to vascular stiffness and muscularization.

Direction‑level reasoning summary:
- Data anchor: AMD1 pathway activation and EV biogenesis competence (Rab27a, Tsg101 expressed in MKs).
- Biological interpretation: Polyamines can be encapsulated in EVs during platelet/MK shedding. Stromal cells are perivascular and respond to profibrotic signals.
- MK‑linked enzyme/pathway logic: AMD1‑driven polyamine overproduction may lead to high polyamine content in MK‑derived EVs, which, when taken up, modulate recipient cell metabolism and phenotype (e.g., inducing collagen synthesis).
- Candidate downstream axis: EV/stromal.
- Remodeling logic: Myofibroblast accumulation, increased collagen deposition, and vascular stiffness, complementing muscularization.
- Key uncertainty: Whether polyamine‑loaded EVs are a quantitatively significant cargo route compared to soluble release.

Directional chain:
1. Hypoxic MKs increase AMD1 and polyamine synthesis.
2. Polyamines (spermidine/spermine) are enriched in MK‑derived EVs (e.g., exosomes, microparticles).
3. EVs fuse with adventitial fibroblasts/pericytes, delivering polyamines and possibly other cargo (miRNAs, proteins).
4. Recipient fibroblasts acquire myofibroblast phenotype (α‑SMA+, collagen I+), leading to ECM expansion.
5. Vascular stiffness and media/ECM remodeling.

Candidate downstream axes:
- Plausible axes: (i) EV‑delivered polyamines → fibroblast‑to‑myofibroblast transition (working model); (ii) EV‑delivered polyamines → pericyte dysfunction contributing to microvascular drop‑out; (iii) Soluble polyamines acting on fibroblasts; (iv) Co‑delivery of pro‑fibrotic TGF‑β (see Revived hypothesis) – potential synergy.
- Working model: EV‑mediated myofibroblast activation.
- Specific examples: Platelet‑derived microparticles are known to carry polyamines and affect vascular cells; peri‑vascular fibrosis is a hallmark of advanced PH.
- What remains unresolved: Fraction of total polyamines exported via EVs; identity of EV subpopulation responsible.

Evidence basis:
- User‑provided data: AMD1 differential, Seurat check shows Rab27a and Tsg101 are detectable (though not strongly enriched) in MKs, consistent with EV biogenesis capacity. The metabolomics does not distinguish free vs. EV‑associated polyamines.
- Public dataset: GSE289322 GSEA for ECM‑receptor interaction may be enriched; to be confirmed.
- Literature: EVs in intercellular metabolite transfer; platelet EVs and vascular remodeling.
- Biological rationale: MK proximity to adventitia supports EV‑mediated communication.
- Evidence status: Speculative; anchored on AMD1 and MK EV competence.

Predicted observations:
- In MKs: Isolated EVs from PH‑MKs show elevated spermidine/spermine content compared to control MKs.
- In recipient or tissue compartment: Fibroblast uptake of labelled MK‑EVs in co‑culture; induction of α‑SMA and Col1a1. Effect blocked by polyamine synthesis inhibitor.
- In metabolomics: EV fraction from lung lavage of PH mice has higher polyamine content, reduced in Pf4‑Cre;Amd1fl/fl.

Experimental validation:
- Perturbation: Pf4‑Cre;Amd1fl/fl; additionally, use GW4869 (inhibitor of exosome biogenesis) or Rab27a shRNA in MK lineage to assess EV‑dependence.
- Model: Hypoxia mouse model or MK‑fibroblast co‑culture.
- Readout: Fibroblast activation markers, collagen deposition, vessel wall stiffness (micro‑indentation).
- Expected result: Amd1‑KO reduces EV polyamine load and fibroblast activation; EV inhibition attenuates remodeling.
- Falsifying result: If EV depletion does not alter fibroblast activation despite MK‑specific polyamine reduction, the EV route is not critical.

Novelty: Direct investigation of metabolic cargo in MK‑derived EVs affecting lung stromal cells in PH.

Weaknesses: High reliance on EV isolation and polyamine quantification in vesicles; unknown EV yield from MKs in situ.

Priority estimate:
- Directional specificity: 3 (EV route one of several)
- Data support: 3 (EV competence data indirect)
- Literature support: 3
- Novelty: 5
- Testability: 3 (technically challenging)
- Overall generation priority: 3

---

### Hypothesis ID: Axis2_Pnp_Immune

Hypothesis title: MK‑Pnp‑generated inosine/adenosine drives perivascular immunosuppression that permits dysregulated vascular remodeling.

PI instruction addressed: Candidate‑axis validation for Evo_H2 (MK‑Pnp‑inosine/adenosine), immune‑mediated route.

Core directional hypothesis:
Hypoxic MKs upregulate purine nucleoside phosphorylase (Pnp) and 5’‑nucleotidase (Nt5c2), leading to extracellular accumulation of inosine and adenosine; adenosine acts via immune cell receptors to suppress protective T‑cell/innate responses, enabling unchecked PASMC growth and muscularization.

Direction‑level reasoning summary:
- Data anchor: Inosine is elevated in PH‑MKs (log₂FC 3.82). Pnp and Nt5c2, enzymes that generate inosine/adenosine from purine nucleotides, are significantly upregulated in PH‑MKs (Pnp log₂FC 1.74, p=3.81e‑06; Nt5c2 log₂FC 2.88, p=2e‑04), despite low overall expression relative to other tissues. This indicates a hypoxia‑induced purine salvage shift.
- Biological interpretation: Adenosine is a potent immunosuppressive metabolite, acting through A2A/A2B receptors on T cells, macrophages, and dendritic cells. In the perivascular niche, MK‑derived adenosine could blunt anti‑remodeling immune surveillance (e.g., regulatory macrophages or effector T cells), allowing vascular cells to proliferate unchecked.
- MK‑linked enzyme/pathway logic: Pnp catalyzes inosine ↔ hypoxanthine; Nt5c2 converts IMP to inosine. Combined upregulation favors extracellular inosine accumulation, which can be further converted to adenosine by ecto‑5’‑nucleotidases on surrounding cells, or inosine itself may signal. The purine metabolism node is tightly linked to MK metabolic state.
- Candidate downstream axis: Immune‑mediated (adenosine‑dependent immunosuppression).
- Remodeling logic: Loss of homeostatic immune control permits medial thickening and perivascular inflammation.
- Key uncertainty: Relative contribution of adenosine vs inosine, and whether immunosuppression is truly permissive rather than directly causative.

Directional chain:
1. Hypoxia induces Pnp/Nt5c2 in MKs, raising intracellular inosine pools; MKs export inosine/adenosine.
2. Interstitial adenosine activates A2A/A2B receptors on perivascular T cells and macrophages, inhibiting effector functions (e.g., IFN‑γ, granzyme B) and promoting regulatory phenotypes.
3. Immune‑mediated growth suppression of PASMCs is lost.
4. PASMC proliferation and medial thickening.
5. Pulmonary vascular remodeling.

Candidate downstream axes:
- Plausible axes: (i) Adenosine‑mediated lymphocyte inhibition (working model); (ii) Direct adenosine receptor activation on PASMCs causing proliferation (see Axis2_Pnp_Vascular); (iii) Inosine as a metabolic fuel for proliferating vascular cells; (iv) EV‑packaged purine metabolites altering stromal gene expression.
- Working model: Immune checkpoint via adenosine.
- Specific examples: Adenosine receptor blockade has been shown to ameliorate PAH in some models; inosine can modulate macrophage inflammasome activation.
- What remains unresolved: Whether MKs are a dominant source of adenosine in the perivascular space compared to other cells and erythrocytes.

Evidence basis:
- User‑provided data: Inosine up in PH‑MKs; Pnp, Nt5c2 MK‑upregulated (Seurat). Public metabolomics does not report whole‑lung inosine/adenosine; whole‑lung metabolite check absent – a gap.
- Public dataset: GSE289322 GSEA for purine metabolism may show enrichment if the pathway is globally activated; to be confirmed.
- Literature: Adenosine signaling in pulmonary hypertension (e.g., A2B receptor modulation of PASMCs), but MK‑specific role unknown.
- Biological rationale: Metabolic immunosuppression is a common tumor/microenvironment theme; could apply to vascular remodeling.
- Evidence status: Inferred from enzyme/metabolite data; immune axis speculative.

Predicted observations:
- In MKs: Increased inosine/adenosine in conditioned medium.
- In recipient or tissue compartment: Perivascular T cells show reduced activation markers (CD69, IFN‑γ) in hypoxia; effect partially reversed by adenosine receptor antagonist.
- In metabolomics: Whole‑lung inosine and adenosine levels should be elevated, decreased by Pf4‑Cre;Pnp or Nt5c2 KO.

Experimental validation:
- Perturbation: MK‑specific *Pnp* and/or *Nt5c2* deletion (e.g., Pf4‑Cre;Pnp fl/fl). Also broad adenosine receptor antagonist (caffeine or SCH58261) to test the importance of adenosine signaling.
- Model: Hypoxic PH mouse.
- Readout: T‑cell activation markers by FACS, RVSP, medial thickness.
- Expected result: MK‑specific purine enzyme KO blunts immunosuppression and ameliorates PH; receptor blockade partially phenocopies.
- Falsifying result: If immune cell activation status and PH severity remain unchanged after MK purine enzyme deletion, the immune axis is not dominant; direct vascular effects or other sources compensate.

Novelty: Links MK purine metabolism to perivascular immune regulation in PH.

Weaknesses: Distinguishing adenosine from inosine effects is difficult; receptor antagonists have broad effects.

Priority estimate:
- Directional specificity: 3
- Data support: 4 (strong enzyme/metabolite data)
- Literature support: 3
- Novelty: 4
- Testability: 4
- Overall generation priority: 4

---

### Hypothesis ID: Axis2_Pnp_Vascular

Hypothesis title: MK‑Pnp‑inosine/adenosine directly stimulates PASMC proliferation via purinergic/cAMP‑pathway crosstalk, independent of immune cells.

PI instruction addressed: Candidate‑axis for Evo_H2, direct vascular wall route.

Core directional hypothesis:
Hypoxic MKs release inosine that is locally converted to adenosine on PASMC surfaces; adenosine then activates A2B receptors, driving intracellular cAMP/PKA and promoting PASMC growth and vascular muscularization.

Direction‑level reasoning summary:
- Data anchor: Same purine enzyme upregulation.
- Biological interpretation: PASMCs express ecto‑5’‑nucleotidase (CD73) and adenosine receptors, particularly A2B, which have been implicated in PAH smooth muscle hypertrophy. An MK‑derived purine source could provide sustained receptor activation.
- MK‑linked enzyme/pathway logic: The dual upregulation of Pnp (inosine generation) and Nt5c2 (IMP→inosine) suggests net production and export of inosine. Extracellular adenosine formation is catalyzed by ubiquitous CD73.
- Candidate downstream axis: Direct vascular‑wall.
- Remodeling logic: Adenosine triggers PASMC hypertrophy and hyperplasia, contributing to medial thickening.
- Key uncertainty: Whether MK‑derived inosine is a quantitatively important adenosine precursor vs. ATP/ADP released by damaged endothelium; whether A2B agonism in PAH is beneficial or detrimental (depending on model).

Directional chain:
1. Hypoxic MKs upregulate Pnp/Nt5c2, increasing inosine export.
2. Inosine is hydrolyzed to adenosine by ecto‑5’‑nucleotidase on PASMCs.
3. Adenosine activates A2B receptors on PASMCs, stimulating adenylyl cyclase and downstream growth pathways.
4. PASMC hypertrophy/hyperplasia.
5. Medial thickening and muscularization.

Candidate downstream axes:
- Plausible axes: (i) Direct PASMC A2B‑mediated growth (working model); (ii) Endothelial adenosine receptor activation leading to endothelial‑mesenchymal transition‑like changes; (iii) Fibroblast activation via A2A receptor; (iv) Inosine acting as a ligand for an unknown receptor.
- Working model: Direct PASMC A2B activation.
- Specific examples: A2B receptor antagonists have shown variable effects in PH; here we propose MK‑derived ligand supports a pathogenic loop.
- What remains unresolved: The net effect of adenosine receptor signaling in PH is context‑dependent; this axis may be protective in some phases.

Evidence basis:
- User‑provided data: Inosine up, Pnp/Nt5c2 MK‑up.
- Public dataset: GSE289322 purine metabolism GSEA, if enriched, supports broad purine activation.
- Literature: A2B receptor upregulation in human PAH; adenosine can promote proliferation in some cell types.
- Biological rationale: Paracrine purine signaling is well‑established in vascular biology.
- Evidence status: Inferred; direct PASMC exposure experiments missing.

Predicted observations:
- In MKs: Release of inosine detectable.
- In recipient tissue: PASMCs in co‑culture with PH‑MKs show increased proliferation, abrogated by adenosine deaminase or A2B antagonist.
- In metabolomics: Whole‑lung adenosine concentration elevated, reversed by MK‑specific *Pnp* deletion.

Experimental validation:
- Perturbation: Pf4‑Cre; *Pnp* fl/fl; also pharmacological A2B inhibition (e.g., MRS1754) in hypoxic WT mice.
- Model: Hypoxic PH mouse; MK‑PASMC co‑culture.
- Readout: PASMC EdU incorporation, medial thickness, RVSP.
- Expected result: Reduced PASMC proliferation and muscularization in *Pnp*‑KO; A2B blockade partially recapitulates.
- Falsifying result: If MK purine enzyme deletion does not alter PASMC proliferation or if A2B blockade worsens PH, the direct vascular axis is not dominant.

Novelty: Identifies MK‑purine metabolism as a non‑adenine nucleotide source of vasoactive adenosine in PH.

Weaknesses: A2B role in PAH is controversial; the axis may be overestimated because many cells produce adenosine.

Priority estimate:
- Directional specificity: 3
- Data support: 4
- Literature support: 3
- Novelty: 4
- Testability: 4
- Overall generation priority: 4

---

### Hypothesis ID: Revived_Matricellular_EV_Secretome

Hypothesis title: Hypoxic lung MKs deploy a multifaceted secretome of matricellular proteins (TSP‑1, PDGF‑B, TGF‑β1), coagulation factors, and extracellular vesicles that collectively drive muscularization, ECM remodeling, and perivascular inflammation.

PI instruction addressed: Revive TSP‑1/TGF‑β and EV‑cargo hypotheses after mandatory Seurat checks (positive), maintaining direction‑level scaffold without defaulting to a single axis.

Core directional hypothesis:
In response to hypoxia, lung MKs upregulate and secrete a suite of potent vascular‑active factors – TSP‑1, PDGF‑B, TGF‑β1, and CD44+ EVs – that act in concert to activate multiple remodeling programs (SMC recruitment, fibroblast differentiation, latent TGF‑β activation, and immune modulation), leading to pulmonary vascular muscularization and stiffness.

Direction‑level reasoning summary:
- Data anchor: Mandatory Seurat queries confirm that *Thbs1* (TSP‑1), *Pdgfb*, *Tgfb1*, and *Cd44* are MK‑enriched and hypoxia‑upregulated. EV biogenesis genes *Rab27a*/*Tsg101* are detectable, indicating capacity for vesicle secretion. No significant change in *F3* (tissue factor) reduces the likelihood of thrombo‑inflammatory dominance, but the secretome is not limited to coagulation. *Lox* shows a trend toward upregulation, suggesting possible cross‑linking activity.
- Biological interpretation: TSP‑1 is a powerful activator of latent TGF‑β, a major driver of myofibroblast transition and PASMC proliferation. PDGF‑B is a potent mitogen for PASMCs. TGF‑β1 can directly induce ECM production. CD44 is an adhesion molecule that can mediate cell‑ECM interactions. Together, these factors create a micro‑environment favoring vascular muscularization and matrix remodeling. EVs can carry matricellular proteins and miRNAs, amplifying the signal.
- MK‑linked enzyme/pathway logic: This hypothesis is not directly metabolic, but the co‑upregulation of multiple validated MK‑derived remodeling factors represents a coordinated secretome program.
- Candidate downstream axes: Multiple, provisionally categorized as TGF‑β‑mediated myofibroblast activation (stromal), PDGF‑B‑mediated PASMC recruitment (vascular), and EV‑mediated signal amplification (pan).
- Remodeling logic: Combined actions of growth factors and matrix proteins induce PASMC proliferation, fibroblast‑to‑myofibroblast transition, and collagen deposition.
- Key uncertainty: The relative contribution of each axis and whether the secretome program is synchronous or comprises sub‑populations with distinct outputs.

Directional chain:
1. Hypoxic lung MKs induce a secretome program: TSP‑1, PDGF‑B, TGF‑β1, CD44, and likely others packaged in EVs.
2. TSP‑1 activates latent TGF‑β in the perivascular matrix; PDGF‑B acts as a PASMC chemoattractant/mitogen; TGF‑β1 drives myofibroblast differentiation.
3. Recipient cells (PASMCs, fibroblasts, pericytes) integrate these signals, leading to proliferation, hypertrophy, and ECM overproduction.
4. Increased muscularization and vascular stiffness, with perivascular collagen deposition.
5. Hemodynamic impairment.

Candidate downstream axes:
- Plausible axes: (i) TSP‑1 → TGF‑β → myofibroblast activation (stromal, working model); (ii) PDGF‑B → PASMC proliferation (vascular); (iii) CD44‑EV‑mediated cell adhesion and signal presentation (EV/stromal); (iv) TGF‑β1 direct effect on endothelial‑mesenchymal transition (candidate example). These are not mutually exclusive.
- Working model: TSP‑1/latent TGF‑β axis dominates early remodeling, reinforced by PDGF‑B and EV signals.
- Specific examples: TSP‑1 is a known angiostatic and TGF‑β activator in PAH; PDGF signaling is a target of imatinib in PH.
- What remains unresolved: Whether the secretome components act synergistically or redundantly; whether specific MK subpopulations produce distinct cargo.

Evidence basis:
- User‑provided data: Seurat MK expression checks for *Thbs1*, *Pdgfb*, *Tgfb1*, *Cd44* all positive and PH‑up. Rab27a and Tsg101 support EV machinery. Lox data not significant but suggestive.
- Public dataset: GSE289322 candidate gene check for *Thbs1*, *Pdgfb*, *Tgfb1* may show whole‑lung upregulation, supporting tissue‑level elevation; GSEA for TGF‑β signaling and ECM‑receptor interaction may be enriched.
- Literature: TSP‑1 and TGF‑β in PAH; PDGF in PH; platelet‑derived mediators in vascular disease. Direct evidence for MK‑derived TSP‑1 in lung remodeling is novel.
- Biological rationale: MKs are uniquely positioned to deliver high concentrations of these factors directly to the vessel wall.
- Evidence status: Direct for gene expression; inferred for protein secretion and functional effects.

Predicted observations:
- In MKs: Increased TSP‑1, PDGF‑B, TGF‑β1 protein in MK supernatant and MK‑derived EVs under hypoxia.
- In recipient or tissue compartment: Co‑localization of TSP‑1 with activated TGF‑β (phospho‑Smad2/3) in perivascular cells; increased PDGFRα+ cells in media. EV uptake by fibroblasts.
- In metabolomics: Not applicable, but proteomics of MK secretome would be expected to show these signatures.

Experimental validation:
- Perturbation: Pf4‑Cre‑driven deletion of *Thbs1* (or combinatorial knockdown of *Thbs1*/*Pdgfb*). For EV route, use *Rab27a*‑KO. Combination with MK depletion control.
- Model: Hypoxia mouse model and MK‑fibroblast co‑cultures.
- Readout: α‑SMA+ muscularization, p‑Smad2/3 staining, PDGFRα+ cell numbers, collagen deposition, RVSP.
- Expected result: *Thbs1*‑MK‑KO reduces TGF‑β activation and remodeling; EV‑KO partially attenuates fibroblast activation; dual targeting may show additive effects.
- Falsifying result: If MK‑specific deletion of *Thbs1* or inhibition of EV release does not alter vascular remodeling, the secretome axis is not essential.

Novelty: First systematic examination of the MK matricellular/EV secretome as a coordinated driver of hypoxic PH.

Weaknesses: Complex multifactorial nature makes it difficult to ascribe causality to a single factor; requires multiple genetic tools.

Revision relative to previous cycle: Revived after positive mandatory Seurat data; broadened to a secretome direction with multiple provisional axes.

Priority estimate:
- Directional specificity: 2 (covers multiple axes)
- Data support: 4 (strong Seurat data)
- Literature support: 4
- Novelty: 4
- Testability: 3 (requires multi‑gene targeting)
- Overall generation priority: 3

---

### Self‑filtered rejected ideas

- **MK‑Glo1/methylglyoxal axis**: *Glo1* not MK‑enriched nor PH‑differential; methylglyoxal metabolite elevation in MKs not reported; no mechanism‑ready shortlist entry. Does not meet anchor criteria.
- **MK‑Dnmt3b epigenetic axis**: Low MK expression (pct 2.62%, enrichment 0.193) and non‑significant differential; insufficient data to build a direction‑level hypothesis.
- **MK‑Amd2‑only axis**: Amd2 is expressed in a very small fraction of MKs (4.37%) and while differential, it is likely secondary to Amd1; not distinct enough from Axis1 hypotheses and will not produce scalable polyamine output.
- **MK‑inosine‑EV‑specific hypothesis**: Merged under Axis2_Pnp_Vascular and Axis2_Pnp_Immune as a candidate downstream route; a stand‑alone hypothesis would be redundant.

### Requests for Tool Use Agent

1. Retrieve the full GSE289322 analysis report (candidate gene check, DE statistics, GSEA results) for the KEGG pathways listed in the brief. Specifically confirm enrichment scores for arginine/proline metabolism, cysteine/methionine metabolism, purine metabolism, TGF‑β signaling, and ECM‑receptor interaction. This will provide tissue‑level support for the metabolomics‑driven and secretome hypotheses.
2. Confirm tissue source of GSE291455 (lung or other) by inspecting the associated publication or GEO metadata. If lung, extract baseline expression of Amd1, Pnp, Thbs1, Pdgfb, Tgfb1, and other candidate genes to serve as normative reference.
3. Perform a targeted literature search for “AMD1 AND pulmonary hypertension” and “AMD1 AND vascular remodeling” to identify any existing publications directly linking spermidine metabolism to PH.
4. If possible, run a pathway analysis on the top differentially expressed genes from the MK/platelet cluster (PH vs Control) in the user’s Seurat object, focusing on KEGG pathways to confirm enrichment of arginine/proline metabolism and purine metabolism specifically in MKs.
