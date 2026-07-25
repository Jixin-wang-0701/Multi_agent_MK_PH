from pathlib import Path
import sys
import math

from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import landscape, letter
from reportlab.pdfgen import canvas


INK = HexColor("#1F2937")
MUTED = HexColor("#657384")
LINE = HexColor("#6B7280")
BLUE = HexColor("#DCECF8")
BLUE_LINE = HexColor("#3E86BE")
GREEN = HexColor("#E3F1DE")
GREEN_LINE = HexColor("#4E9651")
PINK = HexColor("#FCE4E3")
PINK_LINE = HexColor("#D96562")
YELLOW = HexColor("#FFF1C9")
YELLOW_LINE = HexColor("#B08313")
GRAY = HexColor("#F1F3F5")
GRAY_LINE = HexColor("#6B7280")
WHITE = HexColor("#FFFFFF")


def arrow(c, x1, y1, x2, y2, color=LINE, dashed=False, width=1.35):
    c.saveState()
    c.setStrokeColor(color)
    c.setFillColor(color)
    c.setLineWidth(width)
    if dashed:
        c.setDash(4, 3)
    c.line(x1, y1, x2, y2)
    c.setDash()
    angle = math.atan2(y2 - y1, x2 - x1)
    head = 7
    for offset in (2.7, -2.7):
        c.line(
            x2,
            y2,
            x2 - head * math.cos(angle) + offset * math.sin(angle),
            y2 - head * math.sin(angle) - offset * math.cos(angle),
        )
    c.restoreState()


def metabolite(c, x, y, r, label, subtitle, fill, stroke, measured=False):
    c.setFillColor(fill)
    c.setStrokeColor(stroke)
    c.setLineWidth(2.0 if measured else 1.2)
    c.circle(x, y, r, fill=1, stroke=1)
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 9.5)
    c.drawCentredString(x, y + 4, label)
    c.setFont("Helvetica", 6.8)
    c.setFillColor(MUTED)
    c.drawCentredString(x, y - 10, subtitle)
    if measured:
        c.setFillColor(PINK_LINE)
        c.setFont("Helvetica-Bold", 6.5)
        c.drawCentredString(x, y - r - 12, "measured increase")


def enzyme(c, x, y, w, h, label, subtitle, fill, stroke, measured=False):
    points = [
        (x - w / 2 + 8, y - h / 2),
        (x + w / 2 - 8, y - h / 2),
        (x + w / 2, y),
        (x + w / 2 - 8, y + h / 2),
        (x - w / 2 + 8, y + h / 2),
        (x - w / 2, y),
    ]
    c.setFillColor(fill)
    c.setStrokeColor(stroke)
    c.setLineWidth(2.0 if measured else 1.1)
    path = c.beginPath()
    path.moveTo(*points[0])
    for point in points[1:]:
        path.lineTo(*point)
    path.close()
    c.drawPath(path, fill=1, stroke=1)
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 8.5)
    c.drawCentredString(x, y + 2, label)
    c.setFont("Helvetica", 6.4)
    c.setFillColor(MUTED)
    c.drawCentredString(x, y - 10, subtitle)
    if measured:
        c.setFillColor(PINK_LINE)
        c.setFont("Helvetica-Bold", 6.5)
        c.drawCentredString(x, y - h / 2 - 12, "MK-enriched; PH-up")


def badge(c, x, y, label, fill, stroke):
    c.setFillColor(fill)
    c.setStrokeColor(stroke)
    c.setLineWidth(1)
    c.roundRect(x, y, 92, 22, 11, fill=1, stroke=1)
    c.setFillColor(stroke)
    c.setFont("Helvetica-Bold", 7.2)
    c.drawCentredString(x + 46, y + 8, label)


def candidate_icon(c, x, y, kind, label, color):
    c.setStrokeColor(color)
    c.setFillColor(WHITE)
    c.setLineWidth(1.4)
    if kind == "immune":
        c.circle(x, y, 17, fill=1, stroke=1)
        c.circle(x - 6, y + 3, 4, fill=0, stroke=1)
        c.circle(x + 6, y - 2, 4, fill=0, stroke=1)
        c.line(x - 3, y + 1, x + 3, y - 1)
    elif kind == "vessel":
        c.roundRect(x - 20, y - 12, 40, 7, 3, fill=1, stroke=1)
        c.roundRect(x - 20, y + 5, 40, 7, 3, fill=1, stroke=1)
        c.circle(x, y, 3, fill=0, stroke=1)
    else:
        c.circle(x, y, 17, fill=1, stroke=1)
        c.circle(x - 7, y + 4, 3, fill=0, stroke=1)
        c.circle(x + 6, y - 2, 3, fill=0, stroke=1)
        c.line(x - 5, y + 2, x + 4, y - 1)
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 7.2)
    c.drawCentredString(x, y - 29, label)


output = Path(sys.argv[1])
output.parent.mkdir(parents=True, exist_ok=True)
width, height = landscape(letter)
c = canvas.Canvas(str(output), pagesize=(width, height))
c.setTitle("AMD1-linked methionine-SAM-polyamine pathway")

c.setFillColor(INK)
c.setFont("Helvetica-Bold", 17)
c.drawCentredString(width / 2, 576, "AMD1-linked methionine-SAM-polyamine pathway in hypoxic lung MKs")
c.setFillColor(MUTED)
c.setFont("Helvetica", 9.5)
c.drawCentredString(width / 2, 559, "Metabolites are shown as circles; enzymes/genes as hexagons; dashed links are candidate downstream routes.")

badge(c, 38, 523, "metabolite node", BLUE, BLUE_LINE)
badge(c, 141, 523, "enzyme / gene node", YELLOW, YELLOW_LINE)
badge(c, 274, 523, "candidate relation", WHITE, PINK_LINE)

# Main biochemical route.
metabolite(c, 80, 354, 36, "Methionine", "PH MK; +3.26", BLUE, BLUE_LINE, measured=True)
enzyme(c, 144, 354, 45, 30, "MAT", "synthesis", GRAY, GRAY_LINE)
metabolite(c, 210, 354, 34, "SAM", "S-adenosyl", GRAY, GRAY_LINE)
enzyme(c, 280, 354, 56, 32, "AMD1", "decarboxylase", YELLOW, YELLOW_LINE, measured=True)
metabolite(c, 360, 354, 34, "dcSAM", "aminopropyl donor", GREEN, GREEN_LINE)
enzyme(c, 430, 354, 48, 30, "SRM", "spermidine synthase", GRAY, GRAY_LINE)
metabolite(c, 500, 354, 36, "Spermidine", "polyamine", GREEN, GREEN_LINE)
enzyme(c, 575, 354, 48, 30, "SMS", "spermine synthase", GRAY, GRAY_LINE)
metabolite(c, 650, 354, 36, "Spermine", "polyamine", GREEN, GREEN_LINE)

for start, end in [(116, 121), (166, 176), (244, 252), (308, 326), (394, 406), (454, 464), (536, 551), (599, 614)]:
    arrow(c, start, 354, end, 354)

# Branching substrate for polyamine synthesis.
metabolite(c, 360, 229, 35, "Putrescine", "from ornithine", PINK, PINK_LINE)
enzyme(c, 360, 278, 56, 29, "ODC", "decarboxylase", GRAY, GRAY_LINE)
arrow(c, 360, 264, 360, 263, color=PINK_LINE)
arrow(c, 360, 293, 430, 338, color=PINK_LINE)
arrow(c, 394, 354, 406, 354, color=LINE)

# Evidence callouts.
c.setFillColor(BLUE)
c.setStrokeColor(BLUE_LINE)
c.roundRect(46, 108, 270, 70, 10, fill=1, stroke=1)
c.setFillColor(INK)
c.setFont("Helvetica-Bold", 9.3)
c.drawString(61, 155, "Direct evidence")
c.setFont("Helvetica", 8.2)
c.drawString(61, 138, "PH MK methionine abundance: log2FC = +3.26")
c.drawString(61, 124, "Amd1 in MKs: 31.44%; PH MK up: log2FC = +1.77")
c.drawString(61, 110, "Amd1 MK enrichment: log2 = +1.353")

c.setFillColor(HexColor("#FFF8E8"))
c.setStrokeColor(YELLOW_LINE)
c.roundRect(335, 108, 160, 70, 10, fill=1, stroke=1)
c.setFillColor(INK)
c.setFont("Helvetica-Bold", 9.2)
c.drawString(350, 155, "Biochemical logic")
c.setFont("Helvetica", 8.1)
c.drawString(350, 138, "AMD1 converts SAM to dcSAM;")
c.drawString(350, 124, "dcSAM supplies aminopropyl")
c.drawString(350, 110, "groups for polyamine synthesis.")

# Candidate outputs with small biological icons.
c.setFillColor(HexColor("#FFF4F4"))
c.setStrokeColor(PINK_LINE)
c.roundRect(526, 82, 225, 96, 10, fill=1, stroke=1)
c.setFillColor(INK)
c.setFont("Helvetica-Bold", 9.3)
c.drawString(541, 158, "Candidate downstream routes")
c.setFont("Helvetica", 7.7)
c.setFillColor(MUTED)
c.drawString(541, 144, "Not a settled causal bridge")
candidate_icon(c, 568, 116, "immune", "immune tone", GREEN_LINE)
candidate_icon(c, 638, 116, "vessel", "vascular wall", BLUE_LINE)
candidate_icon(c, 708, 116, "ev", "EV / stroma", PINK_LINE)
arrow(c, 650, 318, 568, 134, color=GREEN_LINE, dashed=True)
arrow(c, 650, 318, 638, 134, color=BLUE_LINE, dashed=True)
arrow(c, 650, 318, 708, 134, color=PINK_LINE, dashed=True)

c.setFillColor(MUTED)
c.setFont("Helvetica-Oblique", 7.5)
c.drawRightString(width - 38, 24, "Diagram adapted to KEGG-style metabolite/enzyme node semantics; candidate links require experimental validation.")
c.showPage()
c.save()
