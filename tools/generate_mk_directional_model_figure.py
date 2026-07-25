from __future__ import annotations

from pathlib import Path
import html
import math
import textwrap

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs" / "figures"
OUT.mkdir(parents=True, exist_ok=True)

W, H = 4200, 3300
BG = "#fbfbf8"
INK = "#1f2933"
MUTED = "#5e6a73"
LINE = "#717a83"
DASH = "#a7b0b8"
BLUE = "#dcecf8"
BLUE_DARK = "#2f7bbd"
PINK = "#fde6e7"
PINK_DARK = "#bd565b"
GREEN = "#e2efd9"
GREEN_DARK = "#4c8b4a"
YELLOW = "#fff1c9"
YELLOW_DARK = "#b08313"
PURPLE = "#eee4f8"
PURPLE_DARK = "#7b55aa"
GRAY = "#eef0f2"
GRAY_DARK = "#6b7280"
WHITE = "#ffffff"


def font(size: int, bold: bool = False, italic: bool = False) -> ImageFont.FreeTypeFont:
    if bold and italic:
        name = "arialbi.ttf"
    elif bold:
        name = "arialbd.ttf"
    elif italic:
        name = "ariali.ttf"
    else:
        name = "arial.ttf"
    path = Path("C:/Windows/Fonts") / name
    return ImageFont.truetype(str(path), size=size)


F_TITLE = font(68, bold=True)
F_PANEL = font(52, bold=True)
F_HEAD = font(42, bold=True)
F_SUB = font(34, bold=True)
F_BODY = font(31)
F_SMALL = font(27)
F_TINY = font(23)
F_BOLD_SMALL = font(27, bold=True)


class Figure:
    def __init__(self) -> None:
        self.img = Image.new("RGB", (W, H), BG)
        self.draw = ImageDraw.Draw(self.img)
        self.svg: list[str] = [
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
            f'<rect width="{W}" height="{H}" fill="{BG}"/>',
            '<style>text{font-family:Arial,Helvetica,sans-serif;} .small{font-size:27px;} .tiny{font-size:23px;}</style>',
        ]

    def save(self) -> None:
        self.svg.append("</svg>")
        png = OUT / "mk_hypoxia_directional_model.png"
        tif = OUT / "mk_hypoxia_directional_model.tif"
        svg = OUT / "mk_hypoxia_directional_model.svg"
        self.img.save(png, dpi=(600, 600))
        self.img.save(tif, dpi=(600, 600), compression="tiff_lzw")
        svg.write_text("\n".join(self.svg), encoding="utf-8")

    def line(self, xy: tuple[int, int, int, int], fill: str = LINE, width: int = 4, dash: bool = False) -> None:
        x1, y1, x2, y2 = xy
        if dash:
            self._dashed_line(x1, y1, x2, y2, fill, width)
            self.svg.append(
                f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{fill}" stroke-width="{width}" '
                'stroke-dasharray="18 14" stroke-linecap="round"/>'
            )
        else:
            self.draw.line(xy, fill=fill, width=width)
            self.svg.append(
                f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{fill}" stroke-width="{width}" '
                'stroke-linecap="round"/>'
            )

    def arrow(
        self,
        start: tuple[int, int],
        end: tuple[int, int],
        fill: str = LINE,
        width: int = 5,
        dash: bool = False,
        head: int = 24,
    ) -> None:
        x1, y1 = start
        x2, y2 = end
        self.line((x1, y1, x2, y2), fill=fill, width=width, dash=dash)
        angle = math.atan2(y2 - y1, x2 - x1)
        pts = []
        for a in (angle + math.pi * 0.84, angle - math.pi * 0.84):
            pts.append((x2 + head * math.cos(a), y2 + head * math.sin(a)))
        tri = [(x2, y2), pts[0], pts[1]]
        self.draw.polygon(tri, fill=fill)
        pts_s = " ".join(f"{int(x)},{int(y)}" for x, y in tri)
        self.svg.append(f'<polygon points="{pts_s}" fill="{fill}"/>')

    def rect(
        self,
        xy: tuple[int, int, int, int],
        fill: str = WHITE,
        outline: str = "#c6ccd2",
        width: int = 3,
        radius: int = 16,
        dash: bool = False,
    ) -> None:
        x1, y1, x2, y2 = xy
        self.draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)
        dash_attr = ' stroke-dasharray="10 9"' if dash else ""
        self.svg.append(
            f'<rect x="{x1}" y="{y1}" width="{x2-x1}" height="{y2-y1}" rx="{radius}" '
            f'fill="{fill}" stroke="{outline}" stroke-width="{width}"{dash_attr}/>'
        )

    def ellipse(
        self,
        xy: tuple[int, int, int, int],
        fill: str,
        outline: str = "#c6ccd2",
        width: int = 3,
    ) -> None:
        x1, y1, x2, y2 = xy
        self.draw.ellipse(xy, fill=fill, outline=outline, width=width)
        self.svg.append(
            f'<ellipse cx="{(x1+x2)/2:.1f}" cy="{(y1+y2)/2:.1f}" rx="{(x2-x1)/2:.1f}" '
            f'ry="{(y2-y1)/2:.1f}" fill="{fill}" stroke="{outline}" stroke-width="{width}"/>'
        )

    def text(
        self,
        xy: tuple[int, int],
        text: str,
        fnt: ImageFont.FreeTypeFont,
        fill: str = INK,
        anchor: str = "la",
        align: str = "left",
    ) -> None:
        self.draw.text(xy, text, font=fnt, fill=fill, anchor=anchor, align=align)
        size = fnt.size
        weight = "700" if fnt in {F_TITLE, F_PANEL, F_HEAD, F_SUB, F_BOLD_SMALL} else "400"
        anchor_attr = {"la": "start", "ma": "middle", "ra": "end"}.get(anchor, "start")
        dominant = "hanging" if anchor.endswith("a") else "baseline"
        escaped = html.escape(text)
        self.svg.append(
            f'<text x="{xy[0]}" y="{xy[1]}" fill="{fill}" font-size="{size}" font-weight="{weight}" '
            f'text-anchor="{anchor_attr}" dominant-baseline="{dominant}">{escaped}</text>'
        )

    def wrap_lines(self, text: str, fnt: ImageFont.FreeTypeFont, max_width: int) -> list[str]:
        words = text.split()
        lines: list[str] = []
        cur = ""
        for word in words:
            test = f"{cur} {word}".strip()
            if self.draw.textbbox((0, 0), test, font=fnt)[2] <= max_width:
                cur = test
            else:
                if cur:
                    lines.append(cur)
                cur = word
        if cur:
            lines.append(cur)
        return lines

    def paragraph(
        self,
        xy: tuple[int, int],
        text: str,
        fnt: ImageFont.FreeTypeFont,
        max_width: int,
        fill: str = INK,
        line_gap: int = 10,
        bullet: bool = False,
    ) -> int:
        x, y = xy
        lines = self.wrap_lines(text, fnt, max_width - (34 if bullet else 0))
        line_h = fnt.size + line_gap
        for i, line in enumerate(lines):
            tx = x + (34 if bullet else 0)
            if bullet and i == 0:
                self.ellipse((x, y + 10, x + 12, y + 22), fill=fill, outline=fill, width=1)
            self.text((tx, y), line, fnt, fill=fill)
            y += line_h
        return y

    def label(self, xy: tuple[int, int], text: str, fill: str, outline: str, w: int = 280) -> None:
        x, y = xy
        self.rect((x, y, x + w, y + 52), fill=fill, outline=outline, radius=26, width=2)
        self.text((x + w // 2, y + 13), text, F_TINY, fill=outline, anchor="ma")

    def _dashed_line(self, x1: int, y1: int, x2: int, y2: int, fill: str, width: int) -> None:
        dx, dy = x2 - x1, y2 - y1
        dist = math.hypot(dx, dy)
        if dist == 0:
            return
        ux, uy = dx / dist, dy / dist
        pos = 0.0
        on, off = 22, 16
        while pos < dist:
            end = min(pos + on, dist)
            self.draw.line(
                (x1 + ux * pos, y1 + uy * pos, x1 + ux * end, y1 + uy * end),
                fill=fill,
                width=width,
            )
            pos += on + off


def panel_header(fig: Figure, letter: str, title: str, x: int, y: int, w: int) -> None:
    fig.text((x, y), f"({letter})", F_PANEL, fill=INK)
    fig.text((x + 90, y + 4), title, F_HEAD, fill=INK)
    fig.line((x, y + 72, x + w, y + 72), fill="#d4d8dc", width=3, dash=True)


def small_input_box(fig: Figure, xy: tuple[int, int, int, int], title: str, body: str, fill: str, outline: str) -> None:
    fig.rect(xy, fill=fill, outline=outline, radius=12, dash=True)
    x1, y1, x2, _ = xy
    fig.text((x1 + 28, y1 + 28), title, F_SUB, fill=INK)
    fig.paragraph((x1 + 28, y1 + 84), body, F_SMALL, x2 - x1 - 56, fill=MUTED, line_gap=8)


def draw_cell(fig: Figure, cx: int, cy: int, r: int, fill: str, label: str, outline: str = "#637381") -> None:
    fig.ellipse((cx - r, cy - r, cx + r, cy + r), fill=fill, outline=outline, width=4)
    for a in range(0, 360, 45):
        rad = math.radians(a)
        x1 = cx + int((r - 5) * math.cos(rad))
        y1 = cy + int((r - 5) * math.sin(rad))
        x2 = cx + int((r + 26) * math.cos(rad))
        y2 = cy + int((r + 26) * math.sin(rad))
        fig.line((x1, y1, x2, y2), fill=outline, width=4)
    fig.text((cx, cy - 16), label, F_SUB, fill=INK, anchor="ma")


def main() -> None:
    fig = Figure()
    fig.text((2100, 70), "Multi-agent design and AMD1 reasoning path for MK-driven vascular remodeling", F_TITLE, anchor="ma")
    fig.text(
        (2100, 142),
        "Cycle 1 synthesis: system design, simplified architecture, and one concrete hypothesis path.",
        F_SMALL,
        fill=MUTED,
        anchor="ma",
    )

    # Panel A: full design
    ax, ay, aw, ah = 110, 220, 3980, 1180
    fig.rect((ax, ay, ax + aw, ay + ah), fill=WHITE, outline="#bfc7ce", radius=20)
    panel_header(fig, "a", "Overall design: inputs, goal, agents, functions, and outputs", ax + 40, ay + 34, aw - 80)

    # Left inputs and goal
    fig.rect((ax + 70, ay + 145, ax + 720, ay + 1035), fill=BLUE, outline=BLUE_DARK, radius=18, dash=True)
    fig.text((ax + 395, ay + 185), "Scientist inputs", F_HEAD, anchor="ma")
    small_input_box(
        fig,
        (ax + 105, ay + 250, ax + 685, ay + 420),
        "Research goal",
        "Identify how hypoxic in-situ lung MKs drive pulmonary vascular remodeling.",
        WHITE,
        BLUE_DARK,
    )
    small_input_box(
        fig,
        (ax + 105, ay + 455, ax + 685, ay + 670),
        "User datasets",
        "seurat_merged.rds; CD41+ metabolomics; whole-lung metabolomics; prior in-vivo MK necessity/sufficiency.",
        WHITE,
        BLUE_DARK,
    )
    small_input_box(
        fig,
        (ax + 105, ay + 705, ax + 685, ay + 910),
        "Knowledge scaffold",
        "KEGG pathway mapping; PubMed and biological priors as indirect support, not proof.",
        WHITE,
        BLUE_DARK,
    )

    # Center system
    sys_x1, sys_y1, sys_x2, sys_y2 = ax + 835, ay + 145, ax + 3085, ay + 1035
    fig.rect((sys_x1, sys_y1, sys_x2, sys_y2), fill="#fffafa", outline=PINK_DARK, radius=22)
    fig.text((sys_x1 + 1125, sys_y1 + 38), "Co-scientist multi-agent system", F_HEAD, anchor="ma")
    fig.arrow((ax + 735, ay + 590), (sys_x1 - 25, ay + 590), fill=LINE, width=5)

    agents = [
        ("PI Agent", "sets goal, constraints, brief; final decisions", PINK, PINK_DARK),
        ("Generation Agents", "propose diverse candidate directions", YELLOW, YELLOW_DARK),
        ("Metabolic Agent", "prioritizes metabolite-enzyme-MK chains", GREEN, GREEN_DARK),
        ("Tool Use Agent", "summarizes local data, KEGG/PubMed evidence", GRAY, GRAY_DARK),
        ("Proximity Check", "clusters and removes redundant hypotheses", PURPLE, PURPLE_DARK),
        ("Reflection Agents", "critique evidence, plausibility, testability", BLUE, BLUE_DARK),
        ("Ranking Agent", "scores and ranks competing hypotheses", YELLOW, YELLOW_DARK),
        ("Meta-review Agent", "synthesizes consensus and failure modes", PINK, PINK_DARK),
        ("Evolution Agent", "merges, simplifies, refines strongest models", GREEN, GREEN_DARK),
    ]
    gx, gy = sys_x1 + 55, sys_y1 + 120
    card_w, card_h = 675, 155
    for i, (name, role, fill, outline) in enumerate(agents):
        col = i % 3
        row = i // 3
        x1 = gx + col * 725
        y1 = gy + row * 220
        fig.rect((x1, y1, x1 + card_w, y1 + card_h), fill=fill, outline=outline, radius=14, dash=True)
        fig.text((x1 + 28, y1 + 22), name, F_SUB, fill=INK)
        fig.paragraph((x1 + 28, y1 + 75), role, F_SMALL, card_w - 56, fill=INK, line_gap=7)

    # Internal agent interaction network: parallel proposal, evidence constraint, review, synthesis.
    fig.text((sys_x1 + 1125, sys_y1 + 88), "parallel proposal + evidence-constrained review loop", F_TINY, fill=PINK_DARK, anchor="ma")
    # Short edge-to-edge arrows avoid visually striking through text.
    fig.arrow((gx + 682, gy + 78), (gx + 718, gy + 78), fill=PINK_DARK, width=4, dash=True, head=18)
    fig.arrow((gx + 1407, gy + 78), (gx + 1443, gy + 78), fill=PINK_DARK, width=4, dash=True, head=18)
    fig.arrow((gx + 682, gy + 298), (gx + 718, gy + 298), fill=GRAY_DARK, width=4, dash=True, head=18)
    fig.arrow((gx + 1407, gy + 298), (gx + 1443, gy + 298), fill=GRAY_DARK, width=4, dash=True, head=18)
    fig.arrow((gx + 1062, gy + 158), (gx + 1062, gy + 202), fill=YELLOW_DARK, width=4, dash=True, head=18)
    fig.arrow((gx + 1787, gy + 158), (gx + 1787, gy + 202), fill=GREEN_DARK, width=4, dash=True, head=18)
    fig.arrow((gx + 2062, gy + 378), (gx + 2062, gy + 422), fill=BLUE_DARK, width=4, dash=True, head=18)
    fig.arrow((gx + 682, gy + 518), (gx + 718, gy + 518), fill=LINE, width=4, dash=True, head=18)
    fig.arrow((gx + 1407, gy + 518), (gx + 1443, gy + 518), fill=LINE, width=4, dash=True, head=18)
    fig.line((gx + 1787, gy + 518, gx + 1787, gy + 600), fill=GREEN_DARK, width=4, dash=True)
    fig.line((gx + 1787, gy + 600, gx + 15, gy + 600), fill=GREEN_DARK, width=4, dash=True)
    fig.arrow((gx + 15, gy + 600), (gx + 15, gy + 170), fill=GREEN_DARK, width=4, dash=True, head=18)

    # Context memory layer inside the system.
    fig.rect((sys_x1 + 60, sys_y2 - 120, sys_x2 - 60, sys_y2 - 35), fill=GRAY, outline=GRAY_DARK, radius=14, dash=True)
    fig.text((sys_x1 + 95, sys_y2 - 95), "Context memory", F_BOLD_SMALL, fill=INK)
    fig.paragraph(
        (sys_x1 + 395, sys_y2 - 98),
        "data_context.md, metabolic_context.md, prior cycle feedback, ranked hypotheses, rejected/merged ideas",
        F_TINY,
        sys_x2 - sys_x1 - 520,
        fill=MUTED,
        line_gap=4,
    )
    fig.arrow((sys_x1 + 1125, sys_y2 - 122), (sys_x1 + 1125, gy + 650), fill=GRAY_DARK, width=4, dash=True, head=18)

    # Right outputs
    out_x1, out_y1, out_x2, out_y2 = ax + 3220, ay + 145, ax + 3910, ay + 1035
    fig.arrow((sys_x2 + 25, ay + 590), (out_x1 - 25, ay + 590), fill=LINE, width=5)
    fig.rect((out_x1, out_y1, out_x2, out_y2), fill=YELLOW, outline=YELLOW_DARK, radius=20, dash=True)
    fig.text((out_x1 + 345, out_y1 + 40), "Outputs", F_HEAD, anchor="ma")
    outs = [
        "Ranked hypothesis landscape",
        "Merged/refined directions",
        "Current model figure",
        "Experimental falsification plan",
        "Next-cycle research brief",
    ]
    y = out_y1 + 140
    for item in outs:
        y = fig.paragraph((out_x1 + 55, y), item, F_SMALL, 585, fill=INK, bullet=True, line_gap=8) + 18
    fig.rect((out_x1 + 55, out_y1 + 695, out_x2 - 55, out_y1 + 825), fill=WHITE, outline=YELLOW_DARK, radius=14)
    fig.text((out_x1 + 85, out_y1 + 722), "Current output focus", F_BOLD_SMALL, fill=YELLOW_DARK)
    fig.paragraph((out_x1 + 85, out_y1 + 765), "Direction-level mechanisms; exact bridge provisional.", F_SMALL, 550, fill=INK)

    # Panel B: layered non-linear architecture
    bx, by, bw, bh = 110, 1470, 3980, 720
    fig.rect((bx, by, bx + bw, by + bh), fill=WHITE, outline="#bfc7ce", radius=20)
    panel_header(fig, "b", "Layered architecture for one cycle", bx + 40, by + 34, bw - 80)

    # Input and supervisor
    fig.rect((bx + 120, by + 170, bx + 510, by + 365), fill=BLUE, outline=BLUE_DARK, radius=16)
    fig.text((bx + 315, by + 225), "Goal + data", F_SUB, anchor="ma")
    fig.text((bx + 315, by + 275), "context bundle", F_SMALL, anchor="ma", fill=MUTED)
    fig.rect((bx + 720, by + 115, bx + 1280, by + 295), fill=PINK, outline=PINK_DARK, radius=16)
    fig.text((bx + 1000, by + 160), "PI / supervisor", F_SUB, anchor="ma")
    fig.text((bx + 1000, by + 212), "brief + constraints", F_SMALL, anchor="ma", fill=MUTED)
    fig.arrow((bx + 520, by + 270), (bx + 705, by + 205), fill=LINE, width=5)

    # Parallel worker layer
    worker_y = by + 360
    workers = [
        ("Generation\nbranches", YELLOW, YELLOW_DARK, bx + 650),
        ("Metabolic\nbranch", GREEN, GREEN_DARK, bx + 1125),
        ("Tool-use\nevidence", GRAY, GRAY_DARK, bx + 1600),
    ]
    for label, fill, outline, x1 in workers:
        fig.rect((x1, worker_y, x1 + 380, worker_y + 170), fill=fill, outline=outline, radius=16)
        for j, line in enumerate(label.split("\n")):
            fig.text((x1 + 190, worker_y + 48 + j * 43), line, F_SUB if j == 0 else F_SMALL, anchor="ma", fill=INK)
        fig.arrow((bx + 1000, by + 300), (x1 + 190, worker_y - 15), fill=PINK_DARK, width=4, dash=True, head=18)

    # Review layer as separate gate
    review_x = bx + 2125
    review_nodes = [
        ("Proximity", "deduplicate", review_x, by + 200, PURPLE, PURPLE_DARK),
        ("Reflection", "critique", review_x + 410, by + 200, BLUE, BLUE_DARK),
        ("Ranking", "score", review_x + 820, by + 200, YELLOW, YELLOW_DARK),
    ]
    fig.text((review_x + 600, by + 145), "Review layer", F_SUB, anchor="ma", fill=INK)
    for title, sub, x1, y1, fill, outline in review_nodes:
        fig.rect((x1, y1, x1 + 340, y1 + 150), fill=fill, outline=outline, radius=16)
        fig.text((x1 + 170, y1 + 38), title, F_SUB, anchor="ma")
        fig.text((x1 + 170, y1 + 88), sub, F_SMALL, anchor="ma", fill=MUTED)
    fig.arrow((bx + 1995, worker_y + 85), (review_x - 25, by + 275), fill=LINE, width=5)
    fig.arrow((review_x + 350, by + 275), (review_x + 395, by + 275), fill=LINE, width=4)
    fig.arrow((review_x + 760, by + 275), (review_x + 805, by + 275), fill=LINE, width=4)

    # Synthesis and output
    fig.rect((bx + 3050, by + 430, bx + 3470, by + 610), fill=GREEN, outline=GREEN_DARK, radius=16)
    fig.text((bx + 3260, by + 475), "Meta-review", F_SUB, anchor="ma")
    fig.text((bx + 3260, by + 525), "+ evolution", F_SMALL, anchor="ma", fill=MUTED)
    fig.rect((bx + 3570, by + 430, bx + 3860, by + 610), fill=PINK, outline=PINK_DARK, radius=16)
    fig.text((bx + 3715, by + 475), "PI final", F_SUB, anchor="ma")
    fig.text((bx + 3715, by + 525), "feedback", F_SMALL, anchor="ma", fill=MUTED)
    fig.arrow((review_x + 990, by + 350), (bx + 3100, by + 430), fill=LINE, width=5)
    fig.arrow((bx + 3478, by + 520), (bx + 3555, by + 520), fill=LINE, width=5)

    # Memory/context and feedback loops
    fig.rect((bx + 120, by + 500, bx + 510, by + 660), fill=GRAY, outline=GRAY_DARK, radius=16, dash=True)
    fig.text((bx + 315, by + 542), "Context memory", F_SUB, anchor="ma")
    fig.text((bx + 315, by + 590), "cycle artifacts + feedback", F_SMALL, anchor="ma", fill=MUTED)
    fig.arrow((bx + 510, by + 580), (bx + 635, worker_y + 85), fill=GRAY_DARK, width=4, dash=True, head=18)
    fig.arrow((bx + 510, by + 580), (bx + 2110, by + 320), fill=GRAY_DARK, width=4, dash=True, head=18)
    fig.line((bx + 3715, by + 430, bx + 3715, by + 85), fill=PINK_DARK, width=4, dash=True)
    fig.line((bx + 3715, by + 85, bx + 1000, by + 85), fill=PINK_DARK, width=4, dash=True)
    fig.arrow((bx + 1000, by + 85), (bx + 1000, by + 105), fill=PINK_DARK, width=4, dash=True, head=18)
    fig.text((bx + 2350, by + 45), "feedback loop: revise prompts, constraints, and next-cycle priorities", F_TINY, fill=PINK_DARK, anchor="ma")

    fig.rect((bx + 650, by + 590, bx + 2860, by + 675), fill="#f8fafb", outline="#cbd2d8", radius=12)
    fig.text((bx + 690, by + 615), "Architecture principle:", F_BOLD_SMALL, fill=INK)
    fig.paragraph(
        (bx + 1030, by + 613),
        "parallel generation is constrained by evidence, filtered by multiple review agents, synthesized by evolution, and fed back into the next PI brief.",
        F_TINY,
        1750,
        fill=MUTED,
        line_gap=4,
    )

    # Panel C: AMD1 evidence convergence and branching example
    cx0, cy0, cw0, ch0 = 110, 2255, 3980, 860
    fig.rect((cx0, cy0, cx0 + cw0, cy0 + ch0), fill=WHITE, outline="#bfc7ce", radius=22)
    panel_header(fig, "c", "Concrete example: AMD1 evidence convergence and candidate branching", cx0 + 40, cy0 + 34, cw0 - 80)

    evidence = [
        ("Metabolomics", "PH CD41+ methionine ↑\nlog2FC +3.26", BLUE, BLUE_DARK, cy0 + 165),
        ("Pathway mapping", "methionine/SAM pathway\nlinks to polyamine flux", GREEN, GREEN_DARK, cy0 + 360),
        ("MK scRNA-seq", "Amd1 MK+ 31.44%; enrichment +1.35\nPH log2FC +1.77; p=6.55e-6", GREEN, GREEN_DARK, cy0 + 555),
    ]
    for title, body, fill, outline, y1 in evidence:
        fig.rect((cx0 + 90, y1, cx0 + 740, y1 + 150), fill=fill, outline=outline, radius=16)
        fig.text((cx0 + 125, y1 + 25), title, F_SUB, fill=INK)
        yy = y1 + 78
        for line in body.split("\n"):
            yy = fig.paragraph((cx0 + 125, yy), line, F_SMALL, 585, fill=INK, line_gap=4)
        fig.arrow((cx0 + 750, y1 + 75), (cx0 + 980, cy0 + 435), fill=LINE, width=5)

    # Convergence node
    fig.rect((cx0 + 990, cy0 + 280, cx0 + 1540, cy0 + 590), fill="#f4fbf0", outline=GREEN_DARK, radius=24)
    fig.text((cx0 + 1265, cy0 + 320), "Evidence convergence", F_SUB, anchor="ma")
    fig.paragraph(
        (cx0 + 1040, cy0 + 385),
        "Metabolite shift + pathway plausibility + MK-specific PH-up transcript support converge on the AMD1 direction.",
        F_SMALL,
        450,
        fill=INK,
        line_gap=8,
    )
    fig.label((cx0 + 1120, cy0 + 520), "direct anchor", "#ffffff", GREEN_DARK, w=280)

    # Agent decision gate
    fig.arrow((cx0 + 1555, cy0 + 435), (cx0 + 1765, cy0 + 435), fill=LINE, width=5)
    fig.rect((cx0 + 1780, cy0 + 295, cx0 + 2310, cy0 + 575), fill=PINK, outline=PINK_DARK, radius=18, dash=True)
    fig.text((cx0 + 2045, cy0 + 335), "Agent decision gate", F_SUB, anchor="ma")
    gate_steps = [
        "merge duplicate Amd1 hypotheses",
        "rank above Amd2/Dnmt3b/Cyp26b1",
        "downgrade Th17/EndMT to examples",
    ]
    yy = cy0 + 400
    for item in gate_steps:
        yy = fig.paragraph((cx0 + 1835, yy), item, F_SMALL, 410, fill=INK, bullet=True, line_gap=4) + 4

    # Branching model
    fig.arrow((cx0 + 2325, cy0 + 435), (cx0 + 2535, cy0 + 435), fill=LINE, width=5)
    fig.rect((cx0 + 2550, cy0 + 285, cx0 + 3135, cy0 + 585), fill=YELLOW, outline=YELLOW_DARK, radius=20)
    fig.text((cx0 + 2842, cy0 + 325), "Direction-level model", F_SUB, anchor="ma")
    fig.paragraph(
        (cx0 + 2600, cy0 + 390),
        "Hypoxic MK AMD1 may alter methionine/SAM/polyamine tone.",
        F_SMALL,
        485,
        fill=INK,
        line_gap=8,
    )
    branch_origin = (cx0 + 3138, cy0 + 435)
    branches = [
        ("Immune axis", "T-helper/Th17-like tone or macrophage programs", GREEN, GREEN_DARK, cy0 + 170),
        ("Direct vascular axis", "endothelial/VSMC effects; VEGF-family output", BLUE, BLUE_DARK, cy0 + 390),
        ("EV/stromal axis", "polyamine cargo, ECM/stiffness, niche remodeling", PURPLE, PURPLE_DARK, cy0 + 610),
    ]
    for title, body, fill, outline, y1 in branches:
        fig.arrow(branch_origin, (cx0 + 3295, y1 + 75), fill=DASH, width=5, dash=True, head=20)
        fig.rect((cx0 + 3305, y1, cx0 + 3860, y1 + 150), fill=fill, outline=outline, radius=16, dash=True)
        fig.text((cx0 + 3335, y1 + 26), title, F_SUB, fill=INK)
        fig.paragraph((cx0 + 3335, y1 + 82), body, F_SMALL, 485, fill=INK, line_gap=5)

    # Bottom validation loop
    fig.rect((cx0 + 990, cy0 + 665, cx0 + 3135, cy0 + 800), fill=GRAY, outline=GRAY_DARK, radius=14)
    fig.text((cx0 + 1028, cy0 + 695), "Falsifiable test loop", F_SUB, fill=INK)
    fig.paragraph(
        (cx0 + 1365, cy0 + 695),
        "MK Amd1 perturbation -> LC-MS for methionine/SAM/polyamines -> immune/vascular readouts -> medial thickness, muscularization, stiffness.",
        F_SMALL,
        1675,
        fill=MUTED,
        line_gap=7,
    )
    fig.line((cx0 + 2050, cy0 + 665, cx0 + 2050, cy0 + 620), fill=GRAY_DARK, width=4, dash=True)
    fig.line((cx0 + 2050, cy0 + 620, cx0 + 2840, cy0 + 620), fill=GRAY_DARK, width=4, dash=True)
    fig.arrow((cx0 + 2840, cy0 + 620), (cx0 + 2840, cy0 + 588), fill=GRAY_DARK, width=4, dash=True, head=18)

    fig.rect((cx0 + 90, cy0 + 748, cx0 + 910, cy0 + 832), fill="#fffafa", outline=PINK_DARK, radius=12)
    fig.text((cx0 + 120, cy0 + 765), "Not final", F_BOLD_SMALL, fill=PINK_DARK)
    fig.paragraph(
        (cx0 + 300, cy0 + 765),
        "No single metabolite product, immune subset, cytokine, receptor, or EndMT route is concluded.",
        F_TINY,
        560,
        fill=PINK_DARK,
        line_gap=3,
    )

    # Legend
    lx, ly = 120, 3190
    fig.label((lx, ly), "direct data", "#ffffff", GREEN_DARK, w=220)
    fig.arrow((lx + 270, ly + 26), (lx + 445, ly + 26), fill=LINE, width=5, head=18)
    fig.text((lx + 470, ly + 13), "supported direction", F_TINY, fill=MUTED)
    fig.arrow((lx + 795, ly + 26), (lx + 970, ly + 26), fill=DASH, width=5, dash=True, head=18)
    fig.text((lx + 995, ly + 13), "inferred / candidate route", F_TINY, fill=MUTED)
    fig.text((W - 130, H - 55), "Figure: current Cycle 1 synthesis, generated from local multi-agent outputs", F_TINY, fill="#9aa3aa", anchor="ra")

    fig.save()


if __name__ == "__main__":
    main()
