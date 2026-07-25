.libPaths(c(file.path(getwd(), "r_library", "4.6"), .libPaths()))
suppressPackageStartupMessages({
  library(Seurat)
  library(ggplot2)
  library(patchwork)
})

args <- commandArgs(trailingOnly = TRUE)
if (length(args) != 3) {
  stop("Usage: generate_fig6_data_pdfs.R <seurat_rds> <methionine_csv> <output_dir>")
}

seurat_path <- args[[1]]
methionine_path <- args[[2]]
output_dir <- args[[3]]
dir.create(output_dir, recursive = TRUE, showWarnings = FALSE)

object <- readRDS(seurat_path)
metadata <- object@meta.data
assay_name <- if ("RNA" %in% names(object@assays)) "RNA" else names(object@assays)[[1]]
layers <- Layers(object[[assay_name]])
expression <- NULL
for (layer_name in c("data", "counts", "scale.data")) {
  candidates <- layers[layers == layer_name | startsWith(layers, paste0(layer_name, "."))]
  if (length(candidates) == 0) next
  candidate <- LayerData(object, assay = assay_name, layer = candidates[[1]])
  if (!is.null(candidate) && nrow(candidate) > 0 && ncol(candidate) > 0) {
    expression <- candidate
    break
  }
}
if (is.null(expression)) stop("No non-empty expression layer was found in the RNA assay.")
feature_lookup <- setNames(rownames(expression), toupper(rownames(expression)))
amd1_feature <- unname(feature_lookup[["AMD1"]])
if (is.null(amd1_feature) || is.na(amd1_feature)) {
  stop("AMD1/Amd1 was not found in the RNA assay.")
}

amd1 <- as.numeric(expression[amd1_feature, rownames(metadata), drop = TRUE])
# Use the same inclusive MK definition as the evidence package: a cell is
# considered MK/platelet when any available annotation column supports that
# identity. This retains 24 cells labelled Megakaryocyte/Platelet by singleR
# that are not present in manual_anno, keeping the plot aligned with the
# manuscript-level summary statistics.
annotation_cols <- intersect(c("manual_anno", "singleR_anno", "celltype", "cell_type", "annotation"), colnames(metadata))
if (length(annotation_cols) == 0) {
  mk <- rep(FALSE, nrow(metadata))
} else {
  labels <- apply(metadata[, annotation_cols, drop = FALSE], 1, paste, collapse = " ")
  mk <- grepl("megak|mk|platelet|cd41|pf4|ppbp|itga2b", labels, ignore.case = TRUE)
}
condition <- as.character(metadata$Type)
condition[condition == "control"] <- "Control"
condition[condition == "PH"] <- "PH"

plot_df <- data.frame(
  expression = log1p(amd1),
  cell_class = ifelse(mk, "MK/platelet", "All other cells"),
  condition = condition,
  stringsAsFactors = FALSE
)
plot_df$cell_class <- factor(plot_df$cell_class, levels = c("All other cells", "MK/platelet"))
mk_df <- subset(plot_df, cell_class == "MK/platelet")
mk_df$condition <- factor(mk_df$condition, levels = c("Control", "PH"))

format_p <- function(value) {
  if (value < 0.001) return(paste0("Wilcoxon P = ", format(value, scientific = TRUE, digits = 3)))
  paste0("Wilcoxon P = ", signif(value, 2))
}

p_cellclass <- wilcox.test(expression ~ cell_class, data = plot_df)$p.value
p_condition <- wilcox.test(expression ~ condition, data = mk_df)$p.value

theme_fig6 <- theme_classic(base_size = 11) +
  theme(
    plot.title = element_text(face = "bold", hjust = 0.5, size = 12),
    axis.title.x = element_blank(),
    legend.position = "none",
    plot.margin = margin(8, 10, 8, 10)
  )

p1 <- ggplot(plot_df, aes(x = cell_class, y = expression, fill = cell_class)) +
  geom_violin(trim = FALSE, color = "#3e4a59", linewidth = 0.35) +
  geom_boxplot(width = 0.14, outlier.shape = NA, fill = "white", linewidth = 0.35) +
  annotate("text", x = 1.5, y = max(plot_df$expression) * 1.06, label = format_p(p_cellclass), size = 3.1) +
  coord_cartesian(ylim = c(0, max(plot_df$expression) * 1.14)) +
  scale_fill_manual(values = c("All other cells" = "#D5E7F7", "MK/platelet" = "#E8D7F4")) +
  labs(title = "AMD1 expression across lung cell types", y = "log1p RNA count") +
  theme_fig6

p2 <- ggplot(mk_df, aes(x = condition, y = expression, fill = condition)) +
  geom_violin(trim = FALSE, color = "#3e4a59", linewidth = 0.35) +
  geom_boxplot(width = 0.14, outlier.shape = NA, fill = "white", linewidth = 0.35) +
  geom_jitter(width = 0.10, size = 0.65, alpha = 0.32, color = "#374151") +
  annotate("text", x = 1.5, y = max(mk_df$expression) * 1.06, label = format_p(p_condition), size = 3.1) +
  coord_cartesian(ylim = c(0, max(mk_df$expression) * 1.14)) +
  scale_fill_manual(values = c("Control" = "#9FC7EB", "PH" = "#F1A2A0")) +
  labs(title = "AMD1 expression in MK/platelet cells", y = "log1p RNA count") +
  theme_fig6

pdf(file.path(output_dir, "Figure6C_AMD1_single-cell_violin.pdf"), width = 8.4, height = 4.4, useDingbats = FALSE)
print(p1 + p2 + plot_annotation(tag_levels = "A"))
dev.off()

methionine <- read.csv(methionine_path, check.names = FALSE)
methionine$group <- factor(methionine$group, levels = c("Control MK", "PH MK"))
test <- t.test(log10(intensity) ~ group, data = methionine)
mean_control <- mean(methionine$intensity[methionine$group == "Control MK"])
mean_ph <- mean(methionine$intensity[methionine$group == "PH MK"])
log2fc <- log2(mean_ph / mean_control)

met_plot <- ggplot(methionine, aes(x = group, y = intensity, fill = group)) +
  geom_violin(trim = FALSE, color = "#3e4a59", linewidth = 0.40) +
  geom_boxplot(width = 0.16, outlier.shape = NA, fill = "white", linewidth = 0.40) +
  geom_jitter(width = 0.08, size = 2.6, color = "#374151") +
  annotate(
    "text", x = 1.5, y = max(methionine$intensity) * 1.08,
    label = paste0("log2FC = ", format(round(log2fc, 2), nsmall = 2), "; t-test P = ", format(test$p.value, scientific = TRUE, digits = 2)),
    size = 3.4
  ) +
  coord_cartesian(ylim = c(0, max(methionine$intensity) * 1.16)) +
  scale_fill_manual(values = c("Control MK" = "#9FC7EB", "PH MK" = "#F1A2A0")) +
  labs(
    title = "Methionine abundance in MK-enriched metabolomics samples",
    subtitle = "Raw LC-MS intensity; n = 3 biological replicates per group",
    x = NULL,
    y = "Raw LC-MS intensity"
  ) +
  theme_fig6 +
  theme(legend.position = "none")

pdf(file.path(output_dir, "Figure6C_methionine_metabolomics.pdf"), width = 5.5, height = 4.6, useDingbats = FALSE)
print(met_plot)
dev.off()

write.csv(
  data.frame(
    metric = c("AMD1 MK vs other Wilcoxon P", "AMD1 PH vs control MK Wilcoxon P", "Methionine PH vs control MK log2FC", "Methionine t-test P"),
    value = c(p_cellclass, p_condition, log2fc, test$p.value)
  ),
  file.path(output_dir, "Figure6C_plot_statistics.csv"),
  row.names = FALSE
)
