.libPaths(c(file.path(getwd(), "r_library", "4.6"), .libPaths()))
suppressPackageStartupMessages({
  library(Seurat)
  library(SeuratObject)
  library(ggplot2)
  library(Matrix)
})

args <- commandArgs(trailingOnly = TRUE)
if (length(args) != 4) {
  stop("Usage: generate_amd1_celltype_dotplot.R <seurat_rds> <output_pdf> <output_svg> <output_csv>")
}

rds_path <- args[[1]]
output_pdf <- args[[2]]
output_svg <- args[[3]]
output_csv <- args[[4]]
dir.create(dirname(output_pdf), recursive = TRUE, showWarnings = FALSE)

object <- readRDS(rds_path)
metadata <- object@meta.data
assay_name <- if ("RNA" %in% names(object@assays)) "RNA" else names(object@assays)[[1]]

layers <- Layers(object[[assay_name]])
count_layers <- layers[layers == "counts" | startsWith(layers, "counts.")]
if (length(count_layers) == 0) stop("The RNA assay does not contain a counts layer.")
counts <- LayerData(object, assay = assay_name, layer = count_layers[[1]])
feature_lookup <- setNames(rownames(counts), toupper(rownames(counts)))
amd1_feature <- unname(feature_lookup[["AMD1"]])
if (is.null(amd1_feature) || is.na(amd1_feature)) stop("AMD1/Amd1 was not found in the RNA assay.")

# Match the inclusive MK/platelet definition used for the validated Fig. 6C
# single-cell violin plot and manuscript statistics.
annotation_cols <- intersect(c("manual_anno", "singleR_anno", "celltype", "cell_type", "annotation"), colnames(metadata))
if (length(annotation_cols) == 0) {
  mk <- rep(FALSE, nrow(metadata))
} else {
  annotation_labels <- apply(metadata[, annotation_cols, drop = FALSE], 1, paste, collapse = " ")
  mk <- grepl("megak|mk|platelet|cd41|pf4|ppbp|itga2b", annotation_labels, ignore.case = TRUE)
}

# Restrict the display to the requested two biologically interpretable groups.
metadata$fig6_celltype <- factor(
  ifelse(mk, "MK/platelet", "Others"),
  levels = c("Others", "MK/platelet")
)

# Seurat DotPlot expects log-normalized expression in the data layer. Build a
# temporary one-feature assay from the original RNA counts with standard
# LogNormalize scaling (scale factor = 10,000), without modifying the source RDS.
if ("nCount_RNA" %in% colnames(metadata) && all(is.finite(metadata$nCount_RNA)) && all(metadata$nCount_RNA > 0)) {
  library_size <- as.numeric(metadata$nCount_RNA)
} else {
  library_size <- as.numeric(Matrix::colSums(counts))
}
amd1_counts <- as.numeric(counts[amd1_feature, rownames(metadata), drop = TRUE])
amd1_normalized <- log1p(amd1_counts / library_size * 10000)
normalized_matrix <- Matrix::Matrix(
  amd1_normalized,
  nrow = 1,
  sparse = TRUE,
  dimnames = list(amd1_feature, rownames(metadata))
)

dot_assay <- CreateAssay5Object(data = normalized_matrix)
object[["AMD1_dotplot"]] <- dot_assay
DefaultAssay(object) <- "AMD1_dotplot"
object$fig6_celltype <- metadata$fig6_celltype

plot <- DotPlot(
  object,
  features = amd1_feature,
  assay = "AMD1_dotplot",
  group.by = "fig6_celltype",
  cols = c("#AFCBE0", "#1F5E8C"),
  dot.scale = 8,
  scale = FALSE
) +
  labs(
    title = "AMD1 expression: MK/platelet vs Others",
    subtitle = "Dot size = % cells expressing; color = average expression",
    x = NULL,
    y = NULL,
    color = "Average expression",
    size = "Percent\nexpressed"
  ) +
  theme_classic(base_size = 11) +
  theme(
    plot.title = element_text(face = "bold", hjust = 0.5, size = 13),
    plot.subtitle = element_text(hjust = 0.5, size = 8.5, color = "#4B5563"),
    axis.text.x = element_text(face = "bold"),
    axis.text.y = element_text(size = 9),
    legend.position = "right",
    plot.margin = margin(10, 30, 10, 18)
  ) +
  guides(
    color = guide_colorbar(title = "Average expression", display = "rectangles"),
    size = guide_legend(title = "Percent\nexpressed")
  )

pdf(output_pdf, width = 6.7, height = 3.5, useDingbats = FALSE)
print(plot)
dev.off()

svg(output_svg, width = 6.7, height = 3.5, pointsize = 11)
print(plot)
dev.off()

dot_data <- plot$data
write.csv(dot_data, output_csv, row.names = FALSE)
cat("MK/platelet cells:", sum(metadata$fig6_celltype == "MK/platelet"), "\n")
cat("Displayed groups:", nlevels(metadata$fig6_celltype), "\n")
