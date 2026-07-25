# MK Hypoxia Multi-Agent Workflow

This workspace contains a runnable multi-agent research workflow based on `design.txt`.
It reads the existing agent prompts, builds a local user-data context summary, calls the
DeepSeek chat API, and stores every cycle artifact under `outputs/cycle_XXX/`.

## What is included

- PI Agent brief and final feedback
- Multiple Generation Agents with different focus lenses
- Tool Use Agent local evidence summary
- Public Dataset Agent metadata-level validation summary
- Proximity Check Agent clustering and redundancy review
- Multiple Reflection Agents with different review modes
- Ranking Agent scoring
- Meta-review Agent synthesis
- Evolution Agent refinement
- Cycle summary and per-agent markdown outputs

## Configuration

Do not hard-code API keys in source files. Use either PowerShell environment variables:

```powershell
$env:DEEPSEEK_API_KEY = "your_key_here"
$env:DEEPSEEK_MODEL = "deepseek-v4-pro"
$env:DEEPSEEK_FALLBACK_MODEL = "deepseek-v4-flash"
$env:DEEPSEEK_THINKING = "enabled"
$env:DEEPSEEK_GENERATION_MAX_TOKENS = "65536"
$env:DEEPSEEK_PI_MAX_TOKENS = "16384"
```

or copy `.env.example` to `.env` and fill in the key locally:

```powershell
Copy-Item .env.example .env
```

`.env` and `outputs/` are ignored by `.gitignore`.

## Commands

Check the workspace:

```powershell
python run_multi_agent.py doctor
```

Build the local data context summary:

```powershell
python run_multi_agent.py build-context
```

Build only the metabolomics-to-mechanism evidence package:

```powershell
python run_multi_agent.py build-metabolic-context --max-metabolites 30
```

This creates `outputs/metabolic_context.md` plus supporting CSV files under `outputs/metabolic/`.
The evidence chain is:

```text
differential metabolite -> KEGG direct enzyme or same-pathway neighbor gene -> Seurat MK expression/PH-control MK shift -> mechanism-readiness ranking -> PubMed gene and mechanism-context hits
```

The top of `outputs/metabolic_context.md` includes a `Mechanism-Ready Hypothesis Shortlist`.
Generation agents are instructed to prioritize this section over older cycle-specific metabolite
priorities, because it rewards MK enrichment, PH-up MK shift, significant expression change, and
non-generic mechanism tags.

Build only the public dataset discovery context:

```powershell
python run_multi_agent.py build-public-dataset-context --max-public-datasets 8
```

This searches public dataset repositories such as NCBI GEO/GDS and EBI BioStudies/ArrayExpress-style
records, then writes `outputs/public_dataset_context.md` plus supporting files under
`outputs/public_datasets/`. The module searches across public omics modalities, not only scRNA-seq,
and records accession-level metadata. Downstream agents must treat these hits as validation
opportunities unless a later step downloads and reanalyzes the dataset.

Analyze processed public datasets when downloadable matrices are available:

```powershell
python run_multi_agent.py analyze-public-datasets --max-public-analyses 3 --max-public-download-mb 1024
```

This reads the discovered GEO hits, downloads processed supplementary files within the size budget,
and runs lightweight bioinformatics analysis on expression/count matrices. Supported inputs include
gene-by-sample `.txt/.tsv/.csv/.xlsx` tables and 10x-style `features.tsv.gz + matrix.mtx.gz` files,
which are pseudobulked per sample before candidate-gene checks and approximate differential analysis.
FASTQ/SRA/BAM-level raw-data processing is intentionally skipped.

Rebuild the public dataset analysis context from already saved reports without downloading or
reanalyzing datasets:

```powershell
python run_multi_agent.py analyze-public-datasets --reuse-existing-only --max-public-analyses 3
```

Check the R environment and package availability:

```powershell
python run_multi_agent.py r-doctor
```

The workflow automatically prepends the workspace-local R library under `r_library/` when it exists.
This project currently uses R 4.6.0 with packages installed in `r_library/4.6`.

If you already have another R library with `Seurat` or `SeuratObject`, point the workflow to it:

```powershell
$env:RSCRIPT_PATH = "C:\Program Files\R\R-4.6.0\bin\x64\Rscript.exe"
$env:R_LIBS = "C:\path\to\existing\R\library"
python run_multi_agent.py r-doctor
```

For offline/local installation from downloaded CRAN Windows binary zips:

```powershell
python tools\download_cran_binaries.py --repo https://mirrors.tuna.tsinghua.edu.cn/CRAN/bin/windows/contrib/4.6 --output-dir cran_cache\4.6 --workers 4 Seurat
& "C:\Program Files\R\R-4.6.0\bin\x64\Rscript.exe" tools\install_local_r_packages.R r_library\4.6 cran_cache\4.6\install_order.txt
```

Run a full cycle:

```powershell
python run_multi_agent.py run-cycle --cycle-id 1 --generation-agents 3 --reflection-agents 3
```

Run a full cycle and force regeneration of the metabolic evidence package:

```powershell
python run_multi_agent.py run-cycle --cycle-id 1 --generation-agents 3 --reflection-agents 3 --rebuild-context --rebuild-metabolic-context --max-metabolites 30 --max-public-datasets 8
```

Run a full cycle with public dataset discovery plus processed-matrix analysis:

```powershell
python run_multi_agent.py run-cycle --cycle-id 1 --generation-agents 3 --reflection-agents 3 --analyze-public-datasets --max-public-analyses 3 --max-public-download-mb 1024
```

Use already completed public-dataset analyses in a cycle without rerunning the analysis step:

```powershell
python run_multi_agent.py run-cycle --cycle-id 1 --generation-agents 3 --reflection-agents 3 --reuse-existing-public-analyses --max-public-analyses 3
```

If a model call fails after some agents have already completed, resume from the existing cycle outputs:

```powershell
python run_multi_agent.py run-cycle --cycle-id 1 --generation-agents 3 --reflection-agents 3 --analyze-public-datasets --max-public-analyses 3 --max-public-download-mb 1024 --resume-existing
```

Skip public dataset search if running offline:

```powershell
python run_multi_agent.py run-cycle --cycle-id 1 --generation-agents 3 --reflection-agents 3 --skip-public-datasets
```

Run without calling DeepSeek:

```powershell
python run_multi_agent.py run-cycle --cycle-id 1 --generation-agents 1 --reflection-agents 1 --dry-run
```

## Notes

- The workflow auto-discovers `Rscript.exe`. You can override it with `RSCRIPT_PATH`.
- The `.rds` Seurat object is inspected through R when `Seurat` or `SeuratObject` is available in the
  selected R library. If those packages are missing, the workflow reports the missing packages and
  avoids loading the large RDS object.
- A dedicated `generation_agent_metabolic.md` output is produced in every cycle. It is constrained to
  metabolomics-driven hypotheses that name a differential metabolite, KEGG direct or pathway-neighbor
  enzyme/gene evidence, Seurat MK expression evidence, literature support/gaps, recipient cell,
  remodeling endpoint, and falsification test.
- The Tool Use Agent currently summarizes local data context only. PubMed/KEGG MCP servers are present
  in this workspace and can be connected later as real retrieval tools. Public dataset discovery is
  handled by `multi_agent_system/public_dataset_context.py`; processed public-matrix analysis is
  handled by `multi_agent_system/public_dataset_analysis.py`; and the Public Dataset Agent interprets
  both contexts while keeping metadata-only hits separate from analyzed evidence.
- Agent outputs should not be treated as verified facts. The prompts require every agent to separate
  direct user-data evidence, public data, literature, inference, and speculation.
