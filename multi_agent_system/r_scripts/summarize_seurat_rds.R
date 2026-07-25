args <- commandArgs(trailingOnly = TRUE)
if (length(args) < 1) {
  stop("Usage: summarize_seurat_rds.R <path_to_rds>")
}

rds_path <- args[[1]]
wanted_env <- Sys.getenv("MULTI_AGENT_R_PACKAGES")
wanted <- if (nzchar(wanted_env)) strsplit(wanted_env, ",", fixed = TRUE)[[1]] else c("Seurat", "SeuratObject", "Matrix")
installed <- rownames(installed.packages())
available <- setNames(wanted %in% installed, wanted)

cat("# RDS / Seurat Summary\n\n")
cat("- R version: ", as.character(getRversion()), "\n", sep = "")
cat("- Rscript path: ", file.path(R.home("bin"), "Rscript.exe"), "\n", sep = "")
cat("- RDS path: ", rds_path, "\n", sep = "")
cat("- RDS size MB: ", round(file.info(rds_path)$size / 1024 / 1024, 2), "\n", sep = "")
cat("- Library paths: ", paste(.libPaths(), collapse = " | "), "\n\n", sep = "")

cat("## Package availability\n")
for (pkg in names(available)) {
  cat("- ", pkg, ": ", if (available[[pkg]]) "available" else "missing", "\n", sep = "")
}

if (!isTRUE(available[["Seurat"]]) && !isTRUE(available[["SeuratObject"]])) {
  cat("\nStatus: Rscript is available, but neither Seurat nor SeuratObject is installed in this R library.\n")
  cat("The large RDS object was not loaded, because Seurat class definitions may be unavailable.\n")
  cat("Direct scRNA-seq evidence should therefore be provided through exported Seurat summaries, or by pointing RSCRIPT_PATH/R_LIBS to an existing R library that contains SeuratObject or Seurat.\n")
  quit(status = 0)
}

if (isTRUE(available[["SeuratObject"]])) {
  suppressPackageStartupMessages(library(SeuratObject))
}
if (isTRUE(available[["Seurat"]])) {
  suppressPackageStartupMessages(library(Seurat))
}

cat("\n## Object loading\n")
obj <- readRDS(rds_path)
cat("- Object class: ", paste(class(obj), collapse = ", "), "\n", sep = "")
cat("- Object size in memory: ", format(object.size(obj), units = "auto"), "\n", sep = "")

safe_value <- function(expr, fallback = "not available") {
  tryCatch(expr, error = function(e) fallback)
}

if (inherits(obj, "Seurat")) {
  assays <- safe_value(names(slot(obj, "assays")), character())
  reductions <- safe_value(names(slot(obj, "reductions")), character())
  graphs <- safe_value(names(slot(obj, "graphs")), character())
  cells <- safe_value(length(colnames(obj)), NA_integer_)

  cat("\n## Seurat object structure\n")
  cat("- Cells: ", cells, "\n", sep = "")
  cat("- Assays: ", paste(assays, collapse = ", "), "\n", sep = "")
  cat("- Reductions: ", paste(reductions, collapse = ", "), "\n", sep = "")
  cat("- Graphs: ", paste(graphs, collapse = ", "), "\n", sep = "")

  if (length(assays) > 0) {
    cat("\n## Assay feature counts\n")
    for (assay in assays) {
      assay_obj <- safe_value(slot(obj, "assays")[[assay]], NULL)
      features <- if (!is.null(assay_obj)) safe_value(length(rownames(assay_obj)), NA_integer_) else NA_integer_
      cat("- ", assay, ": ", features, " features\n", sep = "")
    }
  }

  meta <- safe_value(obj@meta.data, NULL)
  if (!is.null(meta)) {
    cat("\n## Metadata\n")
    cat("- Metadata rows: ", nrow(meta), "\n", sep = "")
    cat("- Metadata columns: ", paste(colnames(meta), collapse = ", "), "\n", sep = "")
    likely_columns <- intersect(
      c(
        "orig.ident", "sample", "condition", "group", "treatment", "Type",
        "celltype", "cell_type", "annotation", "singleR_anno", "manual_anno",
        "RPCA_clusters", "seurat_clusters"
      ),
      colnames(meta)
    )
    if (length(likely_columns) > 0) {
      cat("\n## Metadata value summaries\n")
      for (col in likely_columns) {
        values <- meta[[col]]
        tab <- sort(table(values), decreasing = TRUE)
        tab <- head(tab, 20)
        cat("- ", col, ": ", paste(paste(names(tab), as.integer(tab), sep = "="), collapse = "; "), "\n", sep = "")
      }
    }

    annotation_columns <- intersect(c("manual_anno", "singleR_anno", "celltype", "cell_type", "annotation"), colnames(meta))
    if (length(annotation_columns) > 0) {
      cat("\n## MK-related annotation scan\n")
      pattern <- "megak|mk|platelet|cd41|pf4|ppbp|itga2b"
      for (col in annotation_columns) {
        values <- as.character(meta[[col]])
        matched <- grepl(pattern, values, ignore.case = TRUE)
        if (any(matched, na.rm = TRUE)) {
          tab <- sort(table(values[matched]), decreasing = TRUE)
          tab <- head(tab, 20)
          cat("- ", col, " matched cells: ", sum(matched, na.rm = TRUE), "\n", sep = "")
          cat("  values: ", paste(paste(names(tab), as.integer(tab), sep = "="), collapse = "; "), "\n", sep = "")
        } else {
          cat("- ", col, ": no MK/platelet-like labels detected by keyword scan\n", sep = "")
        }
      }
    }
  }
} else {
  cat("\nStatus: RDS loaded, but it is not a Seurat object. Generic class summary only.\n")
}
