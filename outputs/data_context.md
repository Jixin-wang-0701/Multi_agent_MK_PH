# User-provided data context

This context is generated locally from available files. Agents must distinguish direct evidence from extracted summaries, indirect inference, literature knowledge, and speculation.

## single_cell_rds: seurat_merged.rds
- Path: seurat_merged.rds
- Size: 3452.84 MB
- Modified: 2026-05-18T16:52:35

# RDS / Seurat Summary

- R version: 4.6.0
- Rscript path: C:/PROGRA~1/R/R-46~1.0/bin/x64/Rscript.exe
- RDS path: C:\Users\18553\Desktop\Phd_S4\jiawei_framework\seurat_merged.rds
- RDS size MB: 3452.84
- Library paths: C:/Users/18553/Desktop/Phd_S4/jiawei_framework/r_library/4.6 | C:/Program Files/R/R-4.6.0/library

## Package availability
- Seurat: available
- SeuratObject: available
- Matrix: available
- dplyr: available
- readr: available
- jsonlite: available
- future: available
- ggplot2: available

## Object loading
- Object class: Seurat
- Object size in memory: 6.9 Gb

## Seurat object structure
- Cells: 71302
- Assays: RNA, SCT
- Reductions: pca, integrated.dr, umap
- Graphs: SCT_nn, SCT_snn

## Assay feature counts
- RNA: 20888 features
- SCT: 19633 features

## Metadata
- Metadata rows: 71302
- Metadata columns: orig.ident, nCount_RNA, nFeature_RNA, percent.mt, Type, nCount_SCT, nFeature_SCT, RPCA_clusters, seurat_clusters, singleR_anno, manual_anno

## Metadata value summaries
- orig.ident: E8=13509; E6=12804; E5=11915; E4=9916; E7=7566; H7=3221; H10=3115; H9=2769; H12=2620; H11=2146; H8=1721
- Type: PH=41760; control=29542
- singleR_anno: Neutrophil=10293; CAP1=7245; VEC=6927; iMON=6333; AM=5881; AEC=5621; B=5215; AF1=4921; CD8_T=3113; maDC=2551; CAP2=1491; Secretory=1388; AT2=1249; IM=978; VSMC=940; cDC2=872; AT1=699; Basophil=695; AF2=673; cDC1=670
- manual_anno: neutrophil=13474; CAP1=6956; B=6955; VEC=5964; AEC=5287; monocyte=4555; AF1=4554; AM=4184; CD8_T=3069; IM=2829; iMON=1950; AT2=1690; CAP2=1431; mono/Mac=1187; VSMC=931; DC=930; AT1=807; AF2=672; NK=665; pericyte=620
- RPCA_clusters: 0=7270; 1=6544; 2=6211; 3=5338; 4=4287; 5=3890; 6=3883; 7=3614; 8=3081; 9=2606; 11=2453; 10=2304; 12=1950; 15=1729; 16=1690; 17=1590; 14=1551; 13=1549; 19=1239; 21=1187
- seurat_clusters: 0=7270; 1=6544; 2=6211; 3=5338; 4=4287; 5=3890; 6=3883; 7=3614; 8=3081; 9=2606; 11=2453; 10=2304; 12=1950; 15=1729; 16=1690; 17=1590; 14=1551; 13=1549; 19=1239; 21=1187

## MK-related annotation scan
- manual_anno matched cells: 434
  values: MK/platelet=434
- singleR_anno matched cells: 333
  values: Megakaryocyte/Platelet=333

## mk_metabolomics: sFig6A Raw data.xlsx
- Path: sFig6A Raw data.xlsx
- Size: 0.04 MB
- Modified: 2026-05-18T11:31:37

Workbook summary:
Workbook sheets: Sheet1

Sheet: Sheet1
- Dimensions: 238 rows x 13 columns
- Preview:
  - compound | Control-CD41--1 | Control-CD41--2 | Control-CD41--3 | PH-CD41--1 | PH-CD41--2 | PH-CD41--3 | Control-mk-1
  - glycine | 373661.34 | 323830.84 | 346572.62 | 720685.56 | 665200.75 | 668740.31 | 330516.88
  - Phosphoglycolic acid | 20516.53 | 21473.51 | 26136.53 | 41421.57 | 32901.51 | 42120.44 | 44808.06
  - taurine | 48518556 | 51565748 | 54455732 | 41186560 | 40099696 | 42848548 | 53225548
  - O-Phosphorylethanolamine | 2051843.38 | 1997999.38 | 1930972 | 1065952.38 | 1107759.88 | 1029915.31 | 1198720
  - Pyruvaldehyde | 560203.44 | 540968.06 | 474078.66 | 1036802.69 | 978559.44 | 1018166.19 | 265821.28

## ph_control_metabolomics: Figure6D+F raw data.xlsx
- Path: Figure6D+F raw data.xlsx
- Size: 0.10 MB
- Modified: 2026-05-18T11:31:38

Workbook summary:
Workbook sheets: Raw, FDR, Heatmap

Sheet: Raw
- Dimensions: 214 rows x 23 columns
- Preview:
  - Sample | hs-wt1 | hs-wt2 | hs-wt3 | hs-wt4 | hs-wt5 | hs-ko1 | hs-ko2
  - diet | wt | wt | wt | wt | wt | ko | ko
  - Perfluorooctanesulfonic acid | 62245.21 | 105206.43 | 74817.01 | 83407.12 | 215712.22 | 1551815.77 | 1320727.27
  - DL-Pipecolic acid | 236532.76 | 245459.86 | 330180.38 | 326454.07 | 296401.04 | 122248.54 | 125154.34
  - N-Acetyl-D-fucosamine | 378939 | 250479.12 | 354871.5 | 318400.12 | 336342.91 | 153621.95 | 155315.73
  - serine | 4163457.93 | 3465550.43 | 4389576.68 | 4704280.68 | 4146078.43 | 2442658.18 | 3266726.18

Sheet: FDR
- Dimensions: 213 rows x 18 columns
- Preview:
  - Sample | hs-wt1 | hs-wt2 | hs-wt3 | hs-wt4 | hs-wt5 | hs-ko1 | hs-ko2
  - Indole-3-acetic acid | 104454.76 | 112808.48 | 321123.28 | 185564.17 | 930064.94 | 0 | 0
  - Allantoin | 2016434.69 | 1536378.81 | 2232520.31 | 2375364.06 | 16981131.31 | 1248110.06 | 1040546.69
  - 3-Phenylpropionate | 451019.15 | 266823.71 | 440082.21 | 578450.68 | -2309.3 | 304.89 | 230745.34
  - Phenol sulphate | 12399996 | 2410751.25 | 2242949.5 | 5593886.5 | 38150276 | 2219433.25 | 2240490.75
  - Homocitrulline | 96151.79 | 72199.4 | 132190.73 | 90486.16 | 172411.7 | 15131.68 | 18884.2

Sheet: Heatmap
- Dimensions: 20 rows x 18 columns
- Preview:
  - Sample | hs-wt1 | hs-wt2 | hs-wt3 | hs-wt4 | hs-wt5 | hs-ko1 | hs-ko2
  - Perfluorooctanesulfonic acid | 62245.21 | 105206.43 | 74817.01 | 83407.12 | 215712.22 | 1551815.77 | 1320727.27
  - valine | 4861415.76 | 4120281.76 | 5131414.26 | 5426764.26 | 4362413.26 | 3369660.51 | 3597171.76
  - serine | 4163457.93 | 3465550.43 | 4389576.68 | 4704280.68 | 4146078.43 | 2442658.18 | 3266726.18
  - leucine | 5480572.23 | 5153099.23 | 6223164.23 | 6389630.23 | 6576544.73 | 3600113.98 | 3914049.98
  - citrulline | 1674781.5 | 1440624 | 1817611 | 1680889.38 | 2360169 | 1318062.12 | 1234261.75

## prior_results: prior_results.docx
- Path: prior_results.docx
- Size: 7.47 MB
- Modified: 2026-06-08T19:02:20

Extracted text excerpt:
Lung MKs drive hypoxia-induced PE and pulmonary vascular remodeling
180 The link among lung MK accumulation, thrombocytopenia, and PH progression
suggests a pathogenic contribution of MKs. To test this hypothesis, we manipulated
systemic and local MK abundance through thrombopoietin (TPO) signaling31,32,
mature MK cell adoptive transfer, and bone-marrow transplantation approaches.
Continuous TPO administration doubled MK numbers in bone marrow and lung
185 from both Hx- and HxSu-induced PH mice (Figure 4A/4B, S4A). Relative to vehicle
controls, TPO-treated mice developed markedly worse hypoxic PH with increased
right ventricular systolic pressure (RVSP) and RV hypertrophy (RV/[LV+S]) and
reduced PA AT/ET (Figure 4C, S4B/S4C). Correspondingly, α-SMA+ vascular
thickening and muscularization intensified (Figure 4D-4F). To complement this
190 gain-of-function model, we generated TPOR (Mpl) knockout mice (TPOR–/–), which
displayed substantially reduced lung MKs (Figure 4G/4H, S4D/S4E). TPOR–/– mice were protected from hemodynamic impairment (Figure 4I, S4F/S4G) and exhibited
attenuated vascular remodelling (Figure 4J-4L). These results establish MK
expansion as a potentiator of hypoxic PH.
To disentangle MK compartment-specific contributions, 195 we used chimeric
strategies to isolate bone marrow- versus lung-resident MKs. Adoptive transfer of
eGFP+ mature MKs selectively increased bone marrow MKs without affecting lung
MK counts (Figure 4M/4N, S4H) and did not alter PH severity or vascular
remodeling (Figure 4O-4R, S4I/S4J), excluding a direct pathogenic role for mature
200 bone marrow MKs. Conversely, bone marrow transplantation into thorax-shielded
irradiated mice (Figure 4S) yielded TPOR–/– chimeras with selectively reduced lung
MKs but normal bone marrow MKs (Figure 4T, S4K). These lung MK-deficient
TPOR–/– GFP-BM recipients exhibited reduced RVSP, RV hypertrophy, and vascular
remodeling compared with WTGFP-BM controls after hypoxia (Figure 4U-X,
205 S4L/S4M).
Together, these genetic and chimeric models identify lung-resident MKs as the
essential drivers of hypoxia-induced pulmonary vascular remodeling and PH.
Suppression of TPO-TPOR signaling effectively mitigates disease progression.
Figure 4. Lung MKs promote hypoxia-induced PH and pulmonary vascular
remodeling.
(A) Schematic of the experimental setup for TPO/Vehicle injection 1105 for (B-F). (n=6 per group). (B) Flow cytometry analysis of lung MKs. Representative plots (left) and
MK percentage (right). (C) RVSP of vehicle- or TPO-injected mice. (D)
Representative lung IF images stained for α-SMA and DAPI. Scale bar: 25 μm. (E)
Proportion of pulmonary vascular muscularization, categorized as non- (N), partially-
(P), or fully-muscularized (F). (F) Quantification of pulmonary 1110 vascular medial
thickness to total cross-sectional area (Media/CSA). (G) Schematic of the
experimental setup in WT and TPOR⁻/⁻ mice for (H-L) (n=8 per group). (H) Flow
cytometry analysis of lung MKs. Representative plots (left) and MK percentage
(right). (I) RVSP of WT or TPOR⁻/⁻ mice. (J) Representative lung IF images stained as
1115 in D. Scale bar: 25 μm. (K) Proportion of N, P, F categories in pulmonary vessels. (L)
Quantification of Media/CSA. (M) Schematic of the experimental setup of bone
marrow eGFP+ MK adoptive transfer for (N-R) (n=6 per group). (N) Flow cytometry
analysis of bone marrow MKs. Representative plots (left) and MK percentage (right).
(O) RVSP of PBS- or transferred MK-injected mice. (P) Representative lung IF
1120 images stained as in D. Scale bar: 25 μm. (Q) Proportion of N, P, F categories in
pulmonary vessels. (R) Quantification of Media/CSA. (S) Schematic of the
experimental setup of thorax-shielded eGFP⁺ bone marrow transplantation in WT and
TPOR⁻/⁻ recipient mice for (T-X) (n=8 per group). (T) Flow cytometry analysis of
lung MKs. Representative plots (left) and MK percentage (right). (U) RVSP of
1125 WTGFP-BM or TPOR-/-GFP-BM recipient mice. (V) Representative lung IF images stained
as in D. Scale bar: 25 μm. (W) Proportion of N, P, F categories in pulmonary vessels.
(X) Quantification of Media/CSA.
All data are shown as mean ± SEM. Differences were evaluated by two-way
ANOVA with Bonferroni’s post hoc test.
1130 ****p < 0.0001; ***p < 0.001; **p < 0.01; *p < 0.05; ns, not significant;
####p < 0.0001; ###p < 0.001; ##p < 0.01, #p < 0.05.
