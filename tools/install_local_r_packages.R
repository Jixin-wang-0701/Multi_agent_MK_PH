args <- commandArgs(trailingOnly = TRUE)
if (length(args) < 2) {
  stop("Usage: install_local_r_packages.R <library_dir> <install_order_file>")
}

lib <- normalizePath(args[[1]], mustWork = TRUE)
manifest <- normalizePath(args[[2]], mustWork = TRUE)
.libPaths(c(lib, .libPaths()))
pkgs <- normalizePath(readLines(manifest, warn = FALSE), mustWork = TRUE)

install.packages(pkgs, lib = lib, repos = NULL, type = "win.binary")

installed <- rownames(installed.packages(lib.loc = .libPaths()))
cat("LIBS=", paste(.libPaths(), collapse = "|"), "\n", sep = "")
cat("SeuratObject=", "SeuratObject" %in% installed, "\n", sep = "")
cat("Seurat=", "Seurat" %in% installed, "\n", sep = "")
