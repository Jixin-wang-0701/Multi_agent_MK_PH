from pathlib import Path
import sys

from reportlab.lib import colors
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import landscape, letter
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen import canvas


def rounded_box(c, x, y, w, h, title, subtitle, fill, stroke, title_color=HexColor("#1F2937")):
    c.setFillColor(fill)
    c.setStrokeColor(stroke)
    c.setLineWidth(1.1)
    c.roundRect(x, y, w, h, 10, fill=1, stroke=1)
    c.setFillColor(title_color)
    c.setFont("Helvetica-Bold", 11)
    c.drawCentredString(x + w / 2, y + h - 20, title)
    c.setFont("Helvetica", 8.4)
    for index, line in enumerate(subtitle.split("\n")):
        c.drawCentredString(x + w / 2, y + h - 36 - index * 11, line)


def arrow(c, x1, y1, x2, y2, label=None, dashed=False, color=HexColor("#6B7280")):
    c.setStrokeColor(color)
    c.setFillColor(color)
    c.setLineWidth(1.35)
    c.setDash(4, 3) if dashed else c.setDash()
    c.line(x1, y1, x2, y2)
    c.setDash()
    angle_x = x2 - x1
    angle_y = y2 - y1
    norm = max((angle_x**2 + angle_y**2) ** 0.5, 1)
    ux, uy = angle_x / norm, angle_y / norm
    px, py = -uy, ux
    head = 7
    c.line(x2, y2, x2 - head * ux + 3 * px, y2 - head * uy + 3 * py)
    c.line(x2, y2, x2 - head * ux - 3 * px, y2 - head * uy - 3 * py)
    if label:
        c.setFont("Helvetica-Bold", 8)
        c.setFillColor(color)
        c.drawCentredString((x1 + x2) / 2, (y1 + y2) / 2 + 6, label)


output = Path(sys.argv[1])
output.parent.mkdir(parents=True, exist_ok=True)
width, height = landscape(letter)
c = canvas.Canvas(str(output), pagesize=(width, height))
c.setTitle("AMD1-linked methionine-SAM-polyamine pathway")

ink = HexColor("#1F2937")
muted = HexColor("#5B6775")
blue_fill, blue_line = HexColor("#DCECF8"), HexColor("#4C91C9")
pink_fill, pink_line = HexColor("#FCE4E3"), HexColor("#D96562")
green_fill, green_line = HexColor("#E3F1DE"), HexColor("#5C9E5A")
yellow_fill, yellow_line = HexColor("#FFF1C9"), HexColor("#B08313")
gray_fill, gray_line = HexColor("#F1F3F5"), HexColor("#6B7280")

c.setFillColor(ink)
c.setFont("Helvetica-Bold", 17)
c.drawCentredString(width / 2, height - 36, "AMD1-linked methionine-SAM-polyamine pathway in hypoxic lung MKs")
c.setFont("Helvetica", 9.5)
c.setFillColor(muted)
c.drawCentredString(width / 2, height - 53, "Direct data support the upstream metabolic state; downstream effects are candidate routes to test.")

top_y = 223
rounded_box(c, 34, top_y, 94, 66, "Methionine", "PH MK metabolomics\nlog2FC = +3.26", blue_fill, blue_line)
rounded_box(c, 144, top_y, 96, 66, "SAM", "methionine cycle\nintermediate", gray_fill, gray_line)
rounded_box(c, 256, top_y, 100, 66, "AMD1", "MK enriched; PH MK up\nlog2FC = +1.77", yellow_fill, yellow_line)
rounded_box(c, 372, top_y, 100, 66, "dcSAM", "decarboxylated SAM\naminopropyl donor", green_fill, green_line)
rounded_box(c, 488, top_y, 100, 66, "Spermidine", "candidate polyamine\neffector", green_fill, green_line)
rounded_box(c, 604, top_y, 100, 66, "Spermine", "candidate polyamine\neffector", green_fill, green_line)

arrow(c, 128, top_y + 33, 144, top_y + 33, "MAT")
arrow(c, 240, top_y + 33, 256, top_y + 33, "AMD1")
arrow(c, 356, top_y + 33, 372, top_y + 33, "")
arrow(c, 472, top_y + 33, 488, top_y + 33, "SRM")
arrow(c, 588, top_y + 33, 604, top_y + 33, "SMS")

rounded_box(c, 373, 115, 98, 54, "Putrescine", "from ornithine\nvia ODC", pink_fill, pink_line)
arrow(c, 422, 169, 422, top_y, "ODC", color=pink_line)

c.setFillColor(HexColor("#FFF8E8"))
c.setStrokeColor(yellow_line)
c.setLineWidth(1)
c.roundRect(44, 49, 444, 45, 9, fill=1, stroke=1)
c.setFillColor(ink)
c.setFont("Helvetica-Bold", 9.5)
c.drawString(59, 75, "Interpretation supported by the current data")
c.setFont("Helvetica", 8.7)
c.drawString(59, 61, "Hypoxic MKs show a methionine-high, AMD1-linked metabolic state.")

c.setFillColor(HexColor("#FFF3F3"))
c.setStrokeColor(pink_line)
c.roundRect(410, 43, 342, 59, 9, fill=1, stroke=1)
c.setFillColor(ink)
c.setFont("Helvetica-Bold", 9.5)
c.drawString(426, 79, "Candidate downstream routes - require validation")
c.setFont("Helvetica", 8.5)
c.drawString(426, 65, "Immune tone / vascular-wall effects / EV-stromal remodeling")
c.drawString(426, 52, "Not a claim of a single established recipient cell or mechanism.")

for y, label, color in [(144, "immune", green_line), (124, "vascular wall", blue_line), (104, "EV / stroma", pink_line)]:
    arrow(c, 654, top_y, 654, y + 9, dashed=True, color=color)
    c.setFillColor(color)
    c.setFont("Helvetica-Bold", 8)
    c.drawString(714, y + 5, label)

c.setFillColor(muted)
c.setFont("Helvetica-Oblique", 7.7)
c.drawRightString(width - 38, 20, "Dashed arrows indicate candidate downstream biology, not established causal links.")
c.showPage()
c.save()
