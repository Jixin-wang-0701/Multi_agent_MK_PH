PI_TO_GENERATION_BRIEF

Cycle ID: 3

Central question:
Resolve the leading immune-mediated candidate axes and, where newly confirmed MK‑secretory gene
expression permits, introduce one MK matricellular secretome axis.  After mandatory data retrieval,
cycle‑3 generation is strictly limited to **2–3 fully evidence‑anchored, direction‑level hypotheses**.
Do **not** generate any new broad mechanism classes beyond these three axes.

Biological focus:
- In‑situ lung megakaryocytes (MKs) under hypoxia
- Pulmonary vascular remodelling: medial thickening, muscularisation, stiffness
- Immune‑mediated remodelling (candidate downstream cells: T‑cells, macrophages; all specific subsets
  remain provisional)
- MK matricellular/coagulation secretome that may act directly on vascular smooth‑muscle cells,
  endothelial cells, or perivascular fibroblasts
- Metabolic pathways that tie MK metabolic reprogramming to the secretome (polyamine‑eIF5A
  translational control remains the preferred candidate link, but others may be proposed as
  direction‑level examples)

Data sources to prioritize (all already generated in the Cycle‑3 Evidence Package):
1. **Seurat priority‑gene table (`priority_gene_seurat_expression.csv`):** Contains expression,
   MK‑enrichment, and PH‑vs‑control MK differential results for the full gene set. **This is the
   sole source of MK transcriptomic anchoring.**
2. **Metabolite cross‑check table (`priority_metabolite_crosscheck.csv`):** Provides MK‑sorted
   metabolite fold‑changes and whole‑lung metabolite levels (from `Figure6D+F`). **All
   metabolite‑anchored hypotheses must use the values in this table, not prior cycle self‑reports.**
3. **Metabolomics‑to‑mechanism context (ready‑only shortlist provided earlier):** Contains KEGG‑enzyme
   linkages, Seurat expression metrics, and literature cues for the top mechanism‑ready chains.
   Generation agents should draw primarily from the shortlist; if using unlisted metabolites, they
   must show how the chain satisfies MK‑enrichment and PH‑up criteria.
4. **Public dataset DE extraction (`priority_gene_public_de.csv`):** Entirely identifier‑limited;
   no meaningful results. **Do not use** this as positive or negative evidence. Note the gap; if a
   hypothesis requires whole‑lung transcriptomic support, state it as an inference that cannot be
   tested with currently available public data.
5. **Literature:** Limited targeted searches are permissible only to support a direction, e.g.,
   “polyamine‑immune crosstalk” or “thrombospondin‑1 in PH”. Do not use literature as a substitute
   for missing primary data.

Public dataset search tasks (for future validation cycles – **not for hypothesis generation in
cycle 3**):
1. `(pulmonary hypertension OR hypoxia‑induced pulmonary vascular remodelling) AND (megakaryocyte OR
   platelet) AND (single‑cell RNA‑seq OR single‑nucleus RNA‑seq)`
2. `(polyamine OR spermidine OR spermine) AND (lung OR pulmonary) AND (immune OR T‑cell OR
   macrophage) AND (vascular remodelling)`
3. `(AMD1 OR adenosylmethionine decarboxylase) AND (pulmonary hypertension OR hypoxia)`
4. `(purine nucleoside phosphorylase OR Pnp) AND (pulmonary vascular disease)`
5. `(thrombospondin‑1 OR Thbs1) AND (megakaryocyte OR MK) AND (hypoxia) AND (gene expression
   dataset)`
6. `(inosine OR adenosine) AND (megakaryocyte) AND (metabolomics OR proteomics)`
7. `(lung megakaryocyte spatial transcriptomics) OR (perivascular MK imaging mass cytometry)`
8. `(retinoic acid AND megakaryocyte) AND (pulmonary hypertension OR vascular remodelling)`

Required hypothesis categories (all must be metabolomics‑anchored):
- **Refined immune‑mediated axis 1:** AMD1‑polyamine → immune‑mediated vascular remodelling
- **Refined immune‑mediated axis 2:** Pnp‑purine catabolism → immune‑mediated vascular remodelling
- **Conditional matricellular/secretome axis (only if Thbs1, Pdgfb, Tgfb1 are confirmed MK‑enriched
  and PH‑up; they are, as shown in the evidence package):** MK metabolic control (AMd1‑eIF5A or
  alternative) of thrombospondin‑1, PDGF‑B, and TGF‑β1 secretion → direct vascular wall/matrix
  remodelling

Must include (for each hypothesis):
- A direct metabolite‑enzyme‑MK expression chain anchored on the **new evidence tables**.
- A clear statement of which metabolite signal (source/comparison/log2FC) is used.
- Whether the enzyme‑gene is a direct compound‑enzyme or a pathway‑neighbour link; note any missing
  product measurements (spermidine/spermine, adenosine).
- A broad downstream axis label: **immune‑mediated** or **direct vascular‑wall/matrix**. Provide a
  **candidate downstream axes note** with 2–4 plausible routes, marking which one is the working
  model.
- A **direction‑level reasoning summary** that binds data anchor, biological interpretation,
  MK‑linked pathway logic, candidate downstream axis, broad remodelling phenotype, and key
  uncertainty.
- A testable experimental prediction and a **falsification criterion** (e.g., pharmacological blocker,
  bone‑marrow‑specific knockout, spatial co‑localisation requirement).

Must avoid:
- Over‑resolution: nailing a single cytokine, T‑cell subset, receptor, EndMT route, or definitive
  bridge when evidence only supports a direction. Use candidate examples such as Th17‑like tone,
  A2B receptor, smooth‑muscle activation, perivascular fibrosis, etc., and label them as provisional.
- Relying on the unusable GSE289322 public dataset.
- Using prior‑cycle self‑reported gene expression values.
- Introducing new broad pathway classes (EV, coagulation, ECM remodelling beyond the approved
  secretome axis) unless they meet the mandatory Seurat query criteria and are authorised.
- Duplicating hypotheses across agents; generate at most one hypothesis per axis.

Feedback from previous cycle:
- **Keep:** The direction‑level reasoning scaffold; the requirement to anchor every hypothesis on a
  metabolite‑enzyme‑MK chain; labelling of all specific downstream mediators as candidate examples.
- **Remove:** Any hypothesis that does not incorporate the new evidence tables; the previous
  assumption that MK inosine is elevated (the new cross‑check shows it is decreased, log2FC –0.34).
- **Revise:** The inosine/adenosine hypothesis must be reinterpreted in light of the unchanged/falling
  MK inosine and unchanged whole‑lung adenosine. The strong MK *Pnp* up‑regulation should be
  linked to purine nucleotide catabolism (hypoxanthine/xanthine/uric acid or alternative products)
  rather than adenosine accumulation. Immune modulation may still be plausible via these products
  or reactive oxygen species generation. Do not discard the axis; provide a direction‑consistent
  update.
- **Newly generate:** A single MK matricellular/coagulation secretome hypothesis that uses the
  confirmed MK‑enriched/PH‑up genes *Thbs1*, *Pdgfb*, and *Tgfb1* and ties them to a metabolic
  control step (preferentially AMD1‑polyamine‑eIF5A hypusination). The axis label should be
  **direct vascular‑wall/matrix remodelling**, with a candidate note that the three factors could
  collectively promote SMC proliferation, endothelial dysfunction, and perivascular fibrosis.

Expected output (from Generation Agents):
Generate exactly **three** hypotheses, each with:
- Title (e.g., “MK‑AMD1‑polyamine → immune‑mediated vascular remodelling”)
- Metabolite‑enzyme‑MK expression chain (including source and values)
- Direction‑level reasoning summary
- Candidate downstream axes note
- Broad remodelling phenotype
- Testable prediction and falsification criterion
- Explicit statement of key evidence gaps (e.g., “spermidine/spermine not measured”, “MK spatial
  proximity unknown”, “eIF5A hypusination link inferred”)

No hypothesis may exceed one page of concise, structured text.
