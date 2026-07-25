# Public Dataset Analysis Context

Purpose: analyze processed public dataset matrices when available. This module does not process FASTQ/SRA files.
- Analysis enabled: True
- Results: 2

## Dataset Analysis Summary
| Accession | Status | Matrix | Genes | Samples | Comparison | Key outputs | Reason |
|---|---|---|---:|---:|---|---|---|
| GSE289322 | completed | GSE289322_Processed_data_files.xlsx | 30495 | 19 | 8 case vs 4 control samples | [candidate genes](C:\Users\18553\Desktop\Phd_S4\jiawei_framework\outputs\public_dataset_analysis\GSE289322\candidate_gene_check.tsv), [DE results](C:\Users\18553\Desktop\Phd_S4\jiawei_framework\outputs\public_dataset_analysis\GSE289322\de_results.tsv), [report](C:\Users\18553\Desktop\Phd_S4\jiawei_framework\outputs\public_dataset_analysis\GSE289322\analysis_report.md) | Processed expression matrix parsed and analyzed. |
| GSE291455 | completed | GSE291455_All.fpkm.anno.txt.gz | 58302 | 4 | 0 case vs 0 control samples | [candidate genes](C:\Users\18553\Desktop\Phd_S4\jiawei_framework\outputs\public_dataset_analysis\GSE291455\candidate_gene_check.tsv), [report](C:\Users\18553\Desktop\Phd_S4\jiawei_framework\outputs\public_dataset_analysis\GSE291455\analysis_report.md) | Processed expression matrix parsed and analyzed. |

## Interpretation Rules
- Completed analyses may be treated as public-data evidence at the expression-matrix level.
- Skipped datasets remain metadata-only validation opportunities.
- Approximate differential analysis uses inferred sample labels and lightweight statistics; validate important findings manually.
- Do not treat absent candidate genes as biological absence when identifiers may use Ensembl IDs or probe IDs.
