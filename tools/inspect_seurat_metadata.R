.libPaths(c(file.path(getwd(), "r_library", "4.6"), .libPaths()))
suppressPackageStartupMessages(library(Seurat))

object <- readRDS("seurat_merged.rds")
metadata <- object@meta.data
cat("Cells:", nrow(metadata), "\n")
cat("Assays:", paste(names(object@assays), collapse = ", "), "\n")
cat("Columns:\n")
print(colnames(metadata))
for (column in intersect(c("manual_anno", "singleR_anno", "celltype", "cell_type", "annotation", "Type", "condition"), colnames(metadata))) {
  cat("\n", column, "\n", sep = "")
  print(sort(table(metadata[[column]]), decreasing = TRUE))
}
