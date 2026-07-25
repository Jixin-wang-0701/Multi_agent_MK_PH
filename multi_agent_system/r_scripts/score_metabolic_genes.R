args <- commandArgs(trailingOnly = TRUE)
if (length(args) < 3) {
  stop("Usage: score_metabolic_genes.R <seurat_rds> <candidate_gene_csv> <output_csv>")
}

rds_path <- args[[1]]
gene_csv <- args[[2]]
output_csv <- args[[3]]

suppressPackageStartupMessages(library(Seurat))

safe_layer_data <- function(obj, assay_name) {
  assay_obj <- obj[[assay_name]]
  layer_names <- tryCatch(Layers(assay_obj), error = function(e) character())
  preferred <- c("data", "counts", "scale.data")
  for (layer in preferred) {
    matches <- layer_names[layer_names == layer | startsWith(layer_names, paste0(layer, "."))]
    if (length(matches) > 0) {
      return(LayerData(obj, assay = assay_name, layer = matches[[1]]))
    }
  }
  if (length(layer_names) > 0) {
    return(LayerData(obj, assay = assay_name, layer = layer_names[[1]]))
  }
  GetAssayData(obj, assay = assay_name)
}

safe_log2_ratio <- function(a, b) {
  log2((a + 1e-9) / (b + 1e-9))
}

safe_wilcox_p <- function(a, b) {
  a <- a[is.finite(a)]
  b <- b[is.finite(b)]
  if (length(a) < 3 || length(b) < 3) {
    return(NA_real_)
  }
  if (length(unique(c(a, b))) < 2) {
    return(NA_real_)
  }
  tryCatch(
    suppressWarnings(wilcox.test(a, b)$p.value),
    error = function(e) NA_real_
  )
}

obj <- readRDS(rds_path)
meta <- obj@meta.data
meta$.__cell_id <- rownames(meta)

annotation_cols <- intersect(c("manual_anno", "singleR_anno", "celltype", "cell_type", "annotation"), colnames(meta))
if (length(annotation_cols) == 0) {
  mk <- rep(FALSE, nrow(meta))
} else {
  labels <- apply(meta[, annotation_cols, drop = FALSE], 1, paste, collapse = " ")
  mk <- grepl("megak|mk|platelet|cd41|pf4|ppbp|itga2b", labels, ignore.case = TRUE)
}

condition_col <- if ("Type" %in% colnames(meta)) "Type" else if ("condition" %in% colnames(meta)) "condition" else NA_character_
condition <- if (!is.na(condition_col)) as.character(meta[[condition_col]]) else rep("", nrow(meta))
ph <- grepl("PH|hypox|Hx|KO", condition, ignore.case = TRUE)
control <- grepl("control|ctrl|WT", condition, ignore.case = TRUE)

assay_name <- if ("RNA" %in% names(obj@assays)) "RNA" else names(obj@assays)[[1]]
mat <- safe_layer_data(obj, assay_name)
feature_names <- rownames(mat)
feature_lookup <- setNames(feature_names, toupper(feature_names))

candidates <- read.csv(gene_csv, stringsAsFactors = FALSE, check.names = FALSE)
if (!"gene_symbol" %in% colnames(candidates)) {
  stop("candidate_gene_csv must contain gene_symbol")
}

unique_genes <- unique(candidates$gene_symbol[nzchar(candidates$gene_symbol)])
rows <- list()
for (gene in unique_genes) {
  matched <- unname(feature_lookup[toupper(gene)])
  if (length(matched) == 0 || is.null(matched) || is.na(matched)) {
    rows[[length(rows) + 1]] <- data.frame(
      gene_symbol = gene,
      matched_feature = "",
      status = "not_found_in_seurat_features",
      assay = assay_name,
      mk_pct_expr = NA_real_,
      other_pct_expr = NA_real_,
      mk_mean_expr = NA_real_,
      other_mean_expr = NA_real_,
      mk_enrichment_log2 = NA_real_,
      ph_mk_mean_expr = NA_real_,
      control_mk_mean_expr = NA_real_,
      ph_vs_control_mk_log2 = NA_real_,
      ph_mk_pct_expr = NA_real_,
      control_mk_pct_expr = NA_real_,
      ph_vs_control_mk_p_value = NA_real_,
      mk_vs_other_p_value = NA_real_,
      stringsAsFactors = FALSE
    )
    next
  }

  expr <- as.numeric(mat[matched, rownames(meta), drop = TRUE])
  mk_expr <- expr[mk]
  other_expr <- expr[!mk]
  ph_mk_expr <- expr[mk & ph]
  control_mk_expr <- expr[mk & control]
  mk_mean <- if (length(mk_expr) > 0) mean(mk_expr) else NA_real_
  other_mean <- if (length(other_expr) > 0) mean(other_expr) else NA_real_
  ph_mk_mean <- if (length(ph_mk_expr) > 0) mean(ph_mk_expr) else NA_real_
  control_mk_mean <- if (length(control_mk_expr) > 0) mean(control_mk_expr) else NA_real_
  ph_mk_pct <- if (length(ph_mk_expr) > 0) mean(ph_mk_expr > 0) * 100 else NA_real_
  control_mk_pct <- if (length(control_mk_expr) > 0) mean(control_mk_expr > 0) * 100 else NA_real_

  rows[[length(rows) + 1]] <- data.frame(
    gene_symbol = gene,
    matched_feature = matched,
    status = "matched",
    assay = assay_name,
    mk_pct_expr = if (length(mk_expr) > 0) round(mean(mk_expr > 0) * 100, 2) else NA_real_,
    other_pct_expr = if (length(other_expr) > 0) round(mean(other_expr > 0) * 100, 2) else NA_real_,
    mk_mean_expr = round(mk_mean, 5),
    other_mean_expr = round(other_mean, 5),
    mk_enrichment_log2 = round(safe_log2_ratio(mk_mean, other_mean), 3),
    ph_mk_mean_expr = round(ph_mk_mean, 5),
    control_mk_mean_expr = round(control_mk_mean, 5),
    ph_vs_control_mk_log2 = round(safe_log2_ratio(ph_mk_mean, control_mk_mean), 3),
    ph_mk_pct_expr = round(ph_mk_pct, 2),
    control_mk_pct_expr = round(control_mk_pct, 2),
    ph_vs_control_mk_p_value = signif(safe_wilcox_p(ph_mk_expr, control_mk_expr), 3),
    mk_vs_other_p_value = signif(safe_wilcox_p(mk_expr, other_expr), 3),
    stringsAsFactors = FALSE
  )
}

out <- if (length(rows) > 0) do.call(rbind, rows) else data.frame()
write.csv(out, output_csv, row.names = FALSE)
