.libPaths(c(file.path(getwd(), "r_library", "4.6"), .libPaths()))
suppressPackageStartupMessages(library(ggplot2))

args <- commandArgs(trailingOnly = TRUE)
if (length(args) != 2) stop("Usage: generate_methionine_point_plot.R <input_csv> <output_pdf>")

input_path <- args[[1]]
output_path <- args[[2]]
data <- read.csv(input_path, check.names = FALSE)
data$group <- factor(data$group, levels = c("Control MK", "PH MK"))

mean_ci <- function(x) {
  n <- length(x)
  m <- mean(x)
  half_width <- qt(0.975, df = n - 1) * sd(x) / sqrt(n)
  data.frame(y = m, ymin = m - half_width, ymax = m + half_width)
}

summary_data <- do.call(rbind, lapply(split(data$intensity, data$group), mean_ci))
summary_data$group <- factor(rownames(summary_data), levels = c("Control MK", "PH MK"))
rownames(summary_data) <- NULL

mean_control <- mean(data$intensity[data$group == "Control MK"])
mean_ph <- mean(data$intensity[data$group == "PH MK"])
log2fc <- log2(mean_ph / mean_control)
p_value <- t.test(log10(intensity) ~ group, data = data)$p.value

plot <- ggplot(data, aes(x = group, y = intensity, color = group)) +
  geom_point(position = position_jitter(width = 0.075, height = 0), size = 3.2, alpha = 0.95) +
  geom_errorbar(
    data = summary_data,
    aes(x = group, y = y, ymin = ymin, ymax = ymax),
    inherit.aes = FALSE, color = "#1F2937", width = 0.11, linewidth = 0.75
  ) +
  geom_point(
    data = summary_data,
    aes(x = group, y = y),
    inherit.aes = FALSE, shape = 18, size = 4.1, color = "#1F2937"
  ) +
  annotate(
    "text", x = 1.5, y = max(summary_data$ymax) * 1.10,
    label = paste0("log2FC = ", format(round(log2fc, 2), nsmall = 2), "; t-test P = ", format(p_value, scientific = TRUE, digits = 2)),
    size = 3.7, color = "#1F2937"
  ) +
  coord_cartesian(ylim = c(0, max(summary_data$ymax) * 1.19)) +
  scale_color_manual(values = c("Control MK" = "#4C91C9", "PH MK" = "#D96562")) +
  labs(
    title = "Methionine abundance in MK-enriched samples",
    x = NULL,
    y = "Raw LC-MS intensity"
  ) +
  theme_classic(base_size = 12) +
  theme(
    plot.title = element_text(face = "bold", hjust = 0.5, size = 14),
    legend.position = "none",
    axis.text.x = element_text(face = "bold"),
    plot.margin = margin(22, 12, 10, 12)
  )

pdf(output_path, width = 5.8, height = 4.8, useDingbats = FALSE)
print(plot)
dev.off()
