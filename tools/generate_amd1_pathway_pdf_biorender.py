from pathlib import Path
import math
import sys

from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import landscape, letter
from reportlab.pdfgen import canvas


INK = HexColor("#243447")
MUTED = HexColor("#6B7C8F")
LINE = HexColor("#7C8EA1")
SKY = HexColor("#DFF1FB")
SKY_DARK = HexColor("#3F91C4")
LAV = HexColor("#EDE6FB")
LAV_DARK = HexColor("#8067B6")
MINT = HexColor("#E2F3E5")
MINT_DARK = HexColor("#4E9B61")
PEACH = HexColor("#FFE7E0")
PEACH_DARK = HexColor("#D97865")
GOLD = HexColor("#FFF1C8")
GOLD_DARK = HexColor("#B48722")
PALE = HexColor("#F7FAFC")
WHITE = HexColor("#FFFFFF")


def arrow(c, x1, y1, x2, y2, color=LINE, dashed=False, width=1.5):
    c.saveState()
    c.setStrokeColor(color)
    c.setFillColor(color)
    c.setLineWidth(width)
    c.setLineCap(1)
    if dashed:
        c.setDash(5, 4)
    c.line(x1, y1, x2, y2)
    c.setDash()
    angle = math.atan2(y2 - y1, x2 - x1)
    head = 7
    for side in (-1, 1):
        c.line(
            x2,
            y2,
            x2 - head * math.cos(angle) + side * 3.0 * math.sin(angle),
            y2 - head * math.sin(angle) - side * 3.0 * math.cos(angle),
        )
    c.restoreState()


def dashed_polyline(c, points, color=LINE, width=1.5):
    """Draw a routed dashed connector with one arrowhead at its endpoint."""
    c.saveState()
    c.setStrokeColor(color)
    c.setFillColor(color)
    c.setLineWidth(width)
    c.setLineCap(1)
    c.setDash(5, 4)
    path = c.beginPath()
    path.moveTo(*points[0])
    for px, py in points[1:]:
        path.lineTo(px, py)
    c.drawPath(path, stroke=1, fill=0)
    c.setDash()
    x1, y1 = points[-2]
    x2, y2 = points[-1]
    angle = math.atan2(y2 - y1, x2 - x1)
    head = 7
    for side in (-1, 1):
        c.line(
            x2,
            y2,
            x2 - head * math.cos(angle) + side * 3.0 * math.sin(angle),
            y2 - head * math.sin(angle) - side * 3.0 * math.cos(angle),
        )
    c.restoreState()


def card(c, x, y, w, h, fill=WHITE, stroke=HexColor("#D7E1EA"), radius=12):
    c.setFillColor(fill)
    c.setStrokeColor(stroke)
    c.setLineWidth(1.0)
    c.roundRect(x, y, w, h, radius, fill=1, stroke=1)


def molecule(c, x, y, r, title, subtitle, fill, stroke, accent=False):
    c.setFillColor(fill)
    c.setStrokeColor(stroke)
    c.setLineWidth(2.1 if accent else 1.2)
    c.circle(x, y, r, fill=1, stroke=1)
    # small molecular motif
    c.setStrokeColor(stroke)
    c.setLineWidth(1.2)
    c.line(x - r * 0.40, y + r * 0.10, x - r * 0.05, y + r * 0.38)
    c.line(x - r * 0.05, y + r * 0.38, x + r * 0.38, y + r * 0.08)
    for dx, dy in [(-r * 0.40, r * 0.10), (-r * 0.05, r * 0.38), (r * 0.38, r * 0.08)]:
        c.setFillColor(WHITE)
        c.circle(x + dx, y + dy, 3.0, fill=1, stroke=1)
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 8.8)
    c.drawCentredString(x, y - 4, title)
    c.setFillColor(MUTED)
    c.setFont("Helvetica", 6.7)
    c.drawCentredString(x, y - 16, subtitle)


# Alias used for readability in the pathway assembly below.
metabolite = molecule


def enzyme(c, x, y, w, h, title, subtitle, fill=WHITE, stroke=LINE, highlight=False):
    c.setFillColor(fill)
    c.setStrokeColor(stroke)
    c.setLineWidth(2.0 if highlight else 1.1)
    c.roundRect(x - w / 2, y - h / 2, w, h, 9, fill=1, stroke=1)
    # protein-like blobs
    c.setFillColor(stroke)
    c.circle(x - w / 2 + 12, y + 7, 3.0, fill=1, stroke=0)
    c.circle(x - w / 2 + 20, y + 9, 2.0, fill=1, stroke=0)
    c.circle(x - w / 2 + 16, y - 8, 2.4, fill=1, stroke=0)
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 8.2)
    c.drawCentredString(x + 6, y + 3, title)
    c.setFillColor(MUTED)
    c.setFont("Helvetica", 6.3)
    c.drawCentredString(x + 6, y - 9, subtitle)


def cell_icon(c, x, y, r, fill, stroke, label):
    c.setFillColor(fill)
    c.setStrokeColor(stroke)
    c.setLineWidth(1.6)
    c.circle(x, y, r, fill=1, stroke=1)
    c.setFillColor(LAV)
    c.setStrokeColor(LAV_DARK)
    c.circle(x + 6, y + 4, r * 0.30, fill=1, stroke=1)
    for dx, dy in [(-9, 11), (-13, -7), (11, -11)]:
        c.setFillColor(WHITE)
        c.setStrokeColor(stroke)
        c.circle(x + dx, y + dy, 3, fill=1, stroke=1)
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 7.5)
    c.drawCentredString(x, y - r - 14, label)


def downstream_icon(c, x, y, kind, label, color):
    c.setStrokeColor(color)
    c.setFillColor(WHITE)
    c.setLineWidth(1.5)
    if kind == "immune":
        c.circle(x - 8, y + 3, 9, fill=1, stroke=1)
        c.circle(x + 8, y - 2, 9, fill=1, stroke=1)
        c.circle(x - 7, y + 6, 2.3, fill=0, stroke=1)
        c.circle(x + 7, y + 1, 2.3, fill=0, stroke=1)
    elif kind == "vessel":
        c.roundRect(x - 24, y - 12, 48, 7, 3, fill=1, stroke=1)
        c.roundRect(x - 24, y + 5, 48, 7, 3, fill=1, stroke=1)
        c.setFillColor(HexColor("#FFE2DD"))
        c.circle(x, y, 3, fill=1, stroke=1)
    else:
        c.circle(x, y, 17, fill=1, stroke=1)
        c.circle(x - 7, y + 4, 3, fill=0, stroke=1)
        c.circle(x + 7, y - 3, 3, fill=0, stroke=1)
        c.line(x - 4, y + 2, x + 4, y - 1)
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 7.2)
    c.drawCentredString(x, y - 30, label)


output = Path(sys.argv[1])
output.parent.mkdir(parents=True, exist_ok=True)
width, height = landscape(letter)
c = canvas.Canvas(str(output), pagesize=(width, height))
c.setTitle("BioRender-style AMD1 methionine-SAM-polyamine pathway")

c.setFillColor(INK)
c.setFont("Helvetica-Bold", 17)
c.drawCentredString(width / 2, 577, "AMD1-linked methionine-SAM-polyamine pathway in hypoxic lung MKs")
c.setFillColor(MUTED)
c.setFont("Helvetica", 9.2)
c.drawCentredString(width / 2, 560, "BioRender-style scientific schematic: measured upstream evidence, pathway chemistry, and candidate downstream biology")

# Legend pills.
card(c, 38, 524, 96, 23, SKY, SKY_DARK, 11)
c.setFillColor(SKY_DARK)
c.setFont("Helvetica-Bold", 7.0)
c.drawCentredString(86, 532, "metabolite")
card(c, 143, 524, 102, 23, GOLD, GOLD_DARK, 11)
c.setFillColor(GOLD_DARK)
c.drawCentredString(194, 532, "enzyme / gene")
card(c, 254, 524, 106, 23, WHITE, PEACH_DARK, 11)
c.setFillColor(PEACH_DARK)
c.drawCentredString(307, 532, "candidate route")

# Central cell-and-pathway panel.
card(c, 38, 205, 716, 294, PALE, HexColor("#D8E4ED"), 17)
c.setFillColor(INK)
c.setFont("Helvetica-Bold", 10.2)
c.drawString(55, 480, "Hypoxic lung MK metabolic state")
c.setFillColor(MUTED)
c.setFont("Helvetica", 7.8)
c.drawString(55, 466, "The upstream chain is supported by metabolomics and MK-resolved scRNA-seq; downstream links remain testable candidates.")

# MK icon and data callouts.
cell_icon(c, 88, 390, 37, LAV, LAV_DARK, "lung MK")
card(c, 54, 220, 115, 64, WHITE, LAV_DARK, 10)
c.setFillColor(INK)
c.setFont("Helvetica-Bold", 7.5)
c.drawString(64, 268, "MK evidence")
c.setFont("Helvetica", 7.0)
c.setFillColor(MUTED)
c.drawString(64, 253, "Amd1 in MKs: 31.44%")
c.drawString(64, 241, "MK enrichment: +1.353")
c.drawString(64, 229, "PH MK log2FC: +1.77")

# Horizontal pathway.
metabolite(c, 205, 392, 31, "Methionine", "PH MK +3.26", SKY, SKY_DARK, accent=True)
enzyme(c, 263, 392, 45, 34, "MAT", "synthesis", WHITE, LINE)
molecule(c, 323, 392, 31, "SAM", "S-adenosyl", WHITE, LINE)
enzyme(c, 382, 392, 62, 42, "AMD1", "decarboxylase", GOLD, GOLD_DARK, highlight=True)
molecule(c, 454, 392, 31, "dcSAM", "donor", MINT, MINT_DARK)
enzyme(c, 512, 392, 46, 34, "SRM", "synthase", WHITE, LINE)
molecule(c, 571, 392, 32, "Spermidine", "polyamine", MINT, MINT_DARK)
enzyme(c, 632, 392, 46, 34, "SMS", "synthase", WHITE, LINE)
molecule(c, 693, 392, 30, "Spermine", "polyamine", MINT, MINT_DARK)

for start, end in [(236, 240), (286, 292), (354, 351), (413, 423), (485, 489), (535, 539), (603, 609), (655, 663)]:
    arrow(c, start, 392, end, 392)

# Putrescine side branch.
molecule(c, 454, 315, 23, "Putrescine", "substrate", PEACH, PEACH_DARK)
enzyme(c, 454, 363, 45, 28, "ODC", "entry", WHITE, LINE)
arrow(c, 454, 340, 454, 346, color=PEACH_DARK)
arrow(c, 477, 363, 512, 378, color=PEACH_DARK)
arrow(c, 485, 392, 489, 392, color=LINE)

# Data badge and cautious interpretation.
card(c, 190, 220, 252, 64, SKY, SKY_DARK, 10)
c.setFillColor(INK)
c.setFont("Helvetica-Bold", 8.5)
c.drawString(204, 268, "Observed convergence")
c.setFont("Helvetica", 7.2)
c.setFillColor(MUTED)
c.drawString(204, 253, "Methionine abundance rises in PH MK samples.")
c.drawString(204, 240, "Amd1 is MK-enriched and PH-upregulated.")
c.drawString(204, 227, "AMD1 provides the prioritized pathway anchor.")

# Candidate downstream outputs.
card(c, 455, 220, 277, 64, WHITE, PEACH_DARK, 10)
c.setFillColor(INK)
c.setFont("Helvetica-Bold", 8.5)
c.drawString(469, 268, "Candidate downstream routes")
c.setFillColor(MUTED)
c.setFont("Helvetica", 7.2)
c.drawString(469, 253, "Shown as hypotheses for subsequent perturbation and readouts.")
downstream_icon(c, 518, 243, "immune", "immune tone", MINT_DARK)
downstream_icon(c, 600, 243, "vessel", "vascular wall", SKY_DARK)
downstream_icon(c, 684, 243, "ev", "EV / stroma", PEACH_DARK)

# Dashed links from terminal polyamines to the candidate outputs.
dashed_polyline(c, [(693, 360), (740, 345), (740, 280), (518, 266)], color=MINT_DARK)
dashed_polyline(c, [(693, 360), (730, 342), (730, 276), (600, 266)], color=SKY_DARK)
dashed_polyline(c, [(693, 360), (720, 340), (720, 266), (684, 266)], color=PEACH_DARK)

# Footer note.
c.setFillColor(MUTED)
c.setFont("Helvetica-Oblique", 7.5)
c.drawRightString(width - 38, 22, "Dashed arrows indicate candidate mechanisms, not established causal links.")
c.showPage()
c.save()
