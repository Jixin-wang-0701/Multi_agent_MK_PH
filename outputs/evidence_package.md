# Cycle Evidence Package

Generated: 2026-07-13T15:28:03

This package is generated before PI briefing and hypothesis generation. Agents must treat these
tables as direct local evidence when status is completed, and must explicitly label missing
or identifier-limited rows as evidence gaps rather than negative biological findings.

## Seurat MK/Platelet Priority Gene Query

Status: completed
CSV: C:\Users\18553\Desktop\Phd_S4\jiawei_framework\outputs\evidence_package\priority_gene_seurat_expression.csv

| gene_symbol | status | mk_pct_expr | mk_enrichment_log2 | ph_vs_control_mk_log2 | ph_mk_pct_expr | control_mk_pct_expr | ph_vs_control_mk_p_value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Pdgfb | matched | 26.86 | 0.634 | 1 | 32.13 | 16.34 | 0.000317 |
| Tgfb1 | matched | 68.56 | 1.093 | 0.434 | 71.8 | 62.09 | 0.0154 |
| F3 | matched | 2.4 | -2.332 | 0.327 | 2.95 | 1.31 | 0.285 |
| Thbs1 | matched | 87.99 | 3.76 | 0.469 | 88.52 | 86.93 | 0.00687 |
| Glo1 | matched | 17.03 | -0.277 | 0.941 | 19.67 | 11.76 | 0.0266 |
| Rab27a | matched | 13.32 | -0.409 | 0.033 | 14.1 | 11.76 | 0.52 |
| Tsg101 | matched | 24.89 | -0.08 | 0.442 | 25.9 | 22.88 | 0.383 |
| Cd44 | matched | 52.84 | -1.083 | 0.083 | 53.11 | 52.29 | 0.588 |
| Lox | matched | 4.15 | -1.318 | 2.733 | 5.57 | 1.31 | 0.0303 |
| Loxl1 | matched | 4.37 | -2.344 | 0.083 | 4.59 | 3.92 | 0.741 |
| Loxl2 | matched | 3.71 | -0.934 | 3.092 | 5.25 | 0.65 | 0.0143 |
| Mki67 | matched | 0.66 | -4.134 | -1.995 | 0.33 | 1.31 | 0.222 |
| Amd1 | matched | 31.44 | 1.353 | 1.77 | 38.03 | 18.3 | 6.55e-06 |
| Amd2 | matched | 4.37 | 0.931 | 2.175 | 5.9 | 1.31 | 0.0235 |
| Pnp | matched | 20.31 | -1.217 | 1.739 | 26.56 | 7.84 | 3.81e-06 |
| Nt5c2 | matched | 8.95 | -1.24 | 2.879 | 12.46 | 1.96 | 2e-04 |
| Nt5e | matched | 3.06 | -1.39 | 0.383 | 3.61 | 1.96 | 0.34 |

## Public Dataset DE Extraction: GSE289322

Status: completed with identifier-limited matching
CSV: C:\Users\18553\Desktop\Phd_S4\jiawei_framework\outputs\evidence_package\priority_gene_public_de.csv

| query_gene | matched_identifier | log2fc_case_vs_control | p_value_approx | fdr_approx | note |
| --- | --- | --- | --- | --- | --- |
| Pdgfb |  |  |  |  | not found by gene symbol; DE table appears to use Ensembl-like identifiers |
| Tgfb1 |  |  |  |  | not found by gene symbol; DE table appears to use Ensembl-like identifiers |
| F3 |  |  |  |  | not found by gene symbol; DE table appears to use Ensembl-like identifiers |
| Thbs1 |  |  |  |  | not found by gene symbol; DE table appears to use Ensembl-like identifiers |
| Glo1 |  |  |  |  | not found by gene symbol; DE table appears to use Ensembl-like identifiers |
| Rab27a |  |  |  |  | not found by gene symbol; DE table appears to use Ensembl-like identifiers |
| Tsg101 |  |  |  |  | not found by gene symbol; DE table appears to use Ensembl-like identifiers |
| Cd44 |  |  |  |  | not found by gene symbol; DE table appears to use Ensembl-like identifiers |
| Lox |  |  |  |  | not found by gene symbol; DE table appears to use Ensembl-like identifiers |
| Loxl1 |  |  |  |  | not found by gene symbol; DE table appears to use Ensembl-like identifiers |
| Loxl2 |  |  |  |  | not found by gene symbol; DE table appears to use Ensembl-like identifiers |
| Mki67 |  |  |  |  | not found by gene symbol; DE table appears to use Ensembl-like identifiers |
| Amd1 |  |  |  |  | not found by gene symbol; DE table appears to use Ensembl-like identifiers |
| Amd2 |  |  |  |  | not found by gene symbol; DE table appears to use Ensembl-like identifiers |
| Pnp |  |  |  |  | not found by gene symbol; DE table appears to use Ensembl-like identifiers |
| Nt5c2 |  |  |  |  | not found by gene symbol; DE table appears to use Ensembl-like identifiers |
| Nt5e |  |  |  |  | not found by gene symbol; DE table appears to use Ensembl-like identifiers |

## Whole-Lung and MK Metabolite Cross-check

Status: completed
CSV: C:\Users\18553\Desktop\Phd_S4\jiawei_framework\outputs\evidence_package\priority_metabolite_crosscheck.csv

| source_file | sheet | metabolite | status | control_mean | case_mean | log2fc_case_vs_control | fdr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| sFig6A Raw data.xlsx | Sheet1 | methylglyoxal / pyruvaldehyde | found | 2.535e+05 | 1.713e+06 | 2.757 |  |
| sFig6A Raw data.xlsx | Sheet1 | methionine | found | 3.398e+04 | 3.247e+05 | 3.256 |  |
| sFig6A Raw data.xlsx | Sheet1 | inosine | found | 1.139e+05 | 8.971e+04 | -0.3441 |  |
| sFig6A Raw data.xlsx | Sheet1 | retinoic acid | found | 3.887e+05 | 4.207e+06 | 3.436 |  |
| sFig6A Raw data.xlsx | Sheet1 | S-adenosylmethionine | found | 5.287e+04 | 5.722e+04 | 0.1138 |  |
| Figure6D+F raw data.xlsx | Raw | methionine | found | 1 | 0.4929 | -1.02 |  |
| Figure6D+F raw data.xlsx | Raw | S-adenosylmethionine | found | 1 | 0.8847 | -0.1767 |  |
| Figure6D+F raw data.xlsx | Raw | inosine | found |  |  |  |  |
| Figure6D+F raw data.xlsx | Raw | adenosine | found |  |  |  |  |
| Figure6D+F raw data.xlsx | Raw | methylglyoxal / pyruvaldehyde | found |  |  |  |  |
| Figure6D+F raw data.xlsx | FDR | methionine | found | 1.532e+06 | 7.551e+05 | -1.02 | 0.08785 |
| Figure6D+F raw data.xlsx | FDR | S-adenosylmethionine | found | 2.038e+06 | 1.803e+06 | -0.1767 | 0.2433 |
| Figure6D+F raw data.xlsx | FDR | methylglyoxal / pyruvaldehyde | found | 1.133e+07 | 1.114e+07 | -0.0246 | 0.9308 |
| Figure6D+F raw data.xlsx | FDR | inosine | found | 4.94e+07 | 5.724e+07 | 0.2124 | 0.5654 |
| Figure6D+F raw data.xlsx | FDR | adenosine | found | 2.786e+05 | 3.601e+05 | 0.37 | 0.6657 |
| Figure6D+F raw data.xlsx | Heatmap | methionine | found | 1.532e+06 | 7.551e+05 | -1.02 | 0.08785 |
| sFig6A Raw data.xlsx |  | adenosine | not found |  |  |  |  |
| sFig6A Raw data.xlsx |  | spermidine | not found |  |  |  |  |
| sFig6A Raw data.xlsx |  | spermine | not found |  |  |  |  |
| Figure6D+F raw data.xlsx |  | spermidine | not found |  |  |  |  |
| Figure6D+F raw data.xlsx |  | spermine | not found |  |  |  |  |
| Figure6D+F raw data.xlsx |  | retinoic acid | not found |  |  |  |  |

## How Agents Should Use This Package

- Prioritize hypotheses whose mediator genes are matched in Seurat, MK-expressed, and PH-up in MKs.
- Treat public DE rows marked as identifier-limited as unresolved, not as absent expression.
- Treat missing spermidine/spermine or adenosine rows as product-level evidence gaps.
- Do not generate EV, coagulation, or ECM hypotheses unless their candidate genes are supported
  by the Seurat query or explicitly framed as unvalidated alternatives.
