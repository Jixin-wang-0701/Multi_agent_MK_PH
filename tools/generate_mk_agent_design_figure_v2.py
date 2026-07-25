from __future__ import annotations

import generate_mk_directional_model_figure as base


base.W = 4200
base.H = 3600


def polygon(fig: base.Figure, points: list[tuple[int, int]], fill: str, outline: str, width: int = 3) -> None:
    fig.draw.polygon(points, fill=fill)
    closed = points + [points[0]]
    fig.draw.line(closed, fill=outline, width=width)
    pts_s = " ".join(f"{x},{y}" for x, y in points)
    fig.svg.append(f'<polygon points="{pts_s}" fill="{fill}" stroke="{outline}" stroke-width="{width}"/>')


def icon_agent(fig: base.Figure, x: int, y: int, outline: str) -> None:
    fig.ellipse((x, y, x + 60, y + 60), fill="#ffffff", outline=outline, width=3)
    fig.ellipse((x + 21, y + 10, x + 39, y + 28), fill="#ffffff", outline=outline, width=3)
    fig.line((x + 30, y + 31, x + 30, y + 48), fill=outline, width=4)
    fig.line((x + 17, y + 38, x + 43, y + 38), fill=outline, width=4)
    fig.line((x + 30, y + 48, x + 21, y + 55), fill=outline, width=4)
    fig.line((x + 30, y + 48, x + 39, y + 55), fill=outline, width=4)


def icon_data(fig: base.Figure, x: int, y: int, outline: str) -> None:
    fig.rect((x + 13, y + 7, x + 55, y + 43), fill="#ffffff", outline=outline, width=2, radius=6)
    fig.rect((x + 7, y + 14, x + 49, y + 50), fill="#ffffff", outline=outline, width=2, radius=6)
    for i, h in enumerate([14, 24, 18]):
        x0 = x + 18 + i * 9
        fig.line((x0, y + 41, x0, y + 41 - h), fill=outline, width=4)


def icon_target(fig: base.Figure, x: int, y: int, outline: str) -> None:
    fig.ellipse((x + 5, y + 5, x + 55, y + 55), fill="#ffffff", outline=outline, width=3)
    fig.ellipse((x + 16, y + 16, x + 44, y + 44), fill="#ffffff", outline=outline, width=3)
    fig.ellipse((x + 26, y + 26, x + 34, y + 34), fill=outline, outline=outline, width=2)


def icon_molecule(fig: base.Figure, x: int, y: int, outline: str) -> None:
    nodes = [(x + 16, y + 35), (x + 33, y + 15), (x + 48, y + 38), (x + 32, y + 50)]
    fig.line((nodes[0][0], nodes[0][1], nodes[1][0], nodes[1][1]), fill=outline, width=3)
    fig.line((nodes[1][0], nodes[1][1], nodes[2][0], nodes[2][1]), fill=outline, width=3)
    fig.line((nodes[0][0], nodes[0][1], nodes[3][0], nodes[3][1]), fill=outline, width=3)
    fig.line((nodes[2][0], nodes[2][1], nodes[3][0], nodes[3][1]), fill=outline, width=3)
    for nx, ny in nodes:
        fig.ellipse((nx - 7, ny - 7, nx + 7, ny + 7), fill="#ffffff", outline=outline, width=3)


def icon_gene(fig: base.Figure, x: int, y: int, outline: str) -> None:
    fig.rect((x + 6, y + 11, x + 56, y + 49), fill="#ffffff", outline=outline, width=2, radius=6)
    for i, h in enumerate([24, 12, 30, 18, 27, 15]):
        x0 = x + 14 + i * 7
        fig.line((x0, y + 43, x0, y + 43 - h), fill=outline, width=3)


def icon_lightbulb(fig: base.Figure, x: int, y: int, outline: str) -> None:
    fig.ellipse((x + 16, y + 7, x + 45, y + 38), fill="#ffffff", outline=outline, width=3)
    fig.rect((x + 22, y + 38, x + 39, y + 50), fill="#ffffff", outline=outline, width=3, radius=4)
    for x1, y1, x2, y2 in [(x + 30, y + 1, x + 30, y + 8), (x + 8, y + 19, x + 15, y + 22), (x + 46, y + 22, x + 54, y + 19)]:
        fig.line((x1, y1, x2, y2), fill=outline, width=3)


def icon_review(fig: base.Figure, x: int, y: int, outline: str) -> None:
    fig.ellipse((x + 9, y + 8, x + 41, y + 40), fill="#ffffff", outline=outline, width=3)
    fig.line((x + 36, y + 35, x + 53, y + 52), fill=outline, width=4)
    fig.line((x + 18, y + 24, x + 25, y + 31), fill=outline, width=3)
    fig.line((x + 25, y + 31, x + 34, y + 18), fill=outline, width=3)


def icon_rank(fig: base.Figure, x: int, y: int, outline: str) -> None:
    for i, h in enumerate([18, 30, 42]):
        x0 = x + 10 + i * 15
        fig.rect((x0, y + 52 - h, x0 + 10, y + 52), fill="#ffffff", outline=outline, width=2, radius=3)
    fig.line((x + 7, y + 52, x + 56, y + 52), fill=outline, width=3)


def icon_cluster(fig: base.Figure, x: int, y: int, outline: str) -> None:
    for dx, dy in [(17, 12), (36, 18), (24, 36)]:
        fig.ellipse((x + dx - 11, y + dy - 11, x + dx + 11, y + dy + 11), fill="#ffffff", outline=outline, width=3)
    fig.line((x + 17, y + 12, x + 36, y + 18), fill=outline, width=3)
    fig.line((x + 17, y + 12, x + 24, y + 36), fill=outline, width=3)
    fig.line((x + 36, y + 18, x + 24, y + 36), fill=outline, width=3)


def icon_document(fig: base.Figure, x: int, y: int, outline: str) -> None:
    fig.rect((x + 12, y + 7, x + 50, y + 54), fill="#ffffff", outline=outline, width=3, radius=5)
    for yy in [y + 22, y + 32, y + 42]:
        fig.line((x + 20, yy, x + 43, yy), fill=outline, width=3)


def icon_vessel(fig: base.Figure, x: int, y: int, outline: str) -> None:
    fig.line((x + 7, y + 22, x + 55, y + 14), fill=outline, width=4)
    fig.line((x + 7, y + 42, x + 55, y + 34), fill=outline, width=4)
    fig.ellipse((x + 25, y + 23, x + 39, y + 37), fill="#ffffff", outline=outline, width=3)


def icon_funnel(fig: base.Figure, x: int, y: int, outline: str) -> None:
    polygon(fig, [(x, y), (x + 92, y + 28), (x + 58, y + 112), (x + 34, y + 112)], "#ffffff", outline, width=3)
    fig.line((x + 34, y + 112, x + 58, y + 112), fill=outline, width=4)


def draw_icon(fig: base.Figure, kind: str, x: int, y: int, outline: str) -> None:
    icons = {
        "agent": icon_agent,
        "data": icon_data,
        "target": icon_target,
        "molecule": icon_molecule,
        "gene": icon_gene,
        "idea": icon_lightbulb,
        "review": icon_review,
        "rank": icon_rank,
        "cluster": icon_cluster,
        "document": icon_document,
        "vessel": icon_vessel,
    }
    icons.get(kind, icon_agent)(fig, x, y, outline)


def module_box(fig: base.Figure, x: int, y: int, w: int, h: int, title: str, agents: str, role: str, fill: str, outline: str) -> None:
    fig.rect((x, y, x + w, y + h), fill=fill, outline=outline, radius=14, dash=True)
    icon_agent(fig, x + w - 84, y + 18, outline)
    fig.text((x + 24, y + 20), title, base.F_SUB, fill=base.INK)
    fig.text((x + 24, y + 72), agents, base.F_BOLD_SMALL, fill=outline)
    fig.paragraph((x + 24, y + 112), role, base.F_SMALL, w - 48, fill=base.INK, line_gap=5)


def input_box(fig: base.Figure, x: int, y: int, title: str, body: str, icon: str) -> None:
    fig.rect((x, y, x + 585, y + 165), fill=base.WHITE, outline=base.BLUE_DARK, radius=12)
    draw_icon(fig, icon, x + 500, y + 36, base.BLUE_DARK)
    fig.text((x + 26, y + 24), title, base.F_SUB, fill=base.INK)
    fig.paragraph((x + 26, y + 80), body, base.F_SMALL, 455, fill=base.MUTED, line_gap=5)


def flow_node(fig: base.Figure, x: int, y: int, title: str, sub: str, fill: str, outline: str, icon: str | None = None) -> None:
    fig.rect((x, y, x + 460, y + 170), fill=fill, outline=outline, radius=16)
    if icon:
        draw_icon(fig, icon, x + 24, y + 24, outline)
    fig.text((x + 230, y + 43), title, base.F_SUB, anchor="ma")
    fig.text((x + 230, y + 94), sub, base.F_SMALL, fill=base.MUTED, anchor="ma")


def table_cell(fig: base.Figure, x: int, y: int, w: int, h: int, text: str, fill: str, outline: str, bold: bool = False) -> None:
    fig.rect((x, y, x + w, y + h), fill=fill, outline=outline, radius=6)
    fig.paragraph((x + 20, y + 20), text, base.F_BOLD_SMALL if bold else base.F_SMALL, w - 40, fill=base.INK, line_gap=5)


def badge(fig: base.Figure, x: int, y: int, text: str, fill: str, outline: str) -> None:
    fig.ellipse((x, y, x + 54, y + 54), fill=fill, outline=outline, width=3)
    fig.text((x + 27, y + 13), text, base.F_BOLD_SMALL, fill=outline, anchor="ma")


def source_tile(fig: base.Figure, x: int, y: int, title: str, body: str, icon: str, outline: str) -> None:
    fig.rect((x, y, x + 350, y + 100), fill="#ffffff", outline=outline, radius=12, width=2)
    draw_icon(fig, icon, x + 18, y + 22, outline)
    fig.text((x + 85, y + 18), title, base.F_BOLD_SMALL, fill=base.INK)
    fig.paragraph((x + 85, y + 54), body, base.F_TINY, 240, fill=base.MUTED, line_gap=2)


def candidate_chip(fig: base.Figure, x: int, y: int, text: str, fill: str, outline: str, w: int = 140) -> None:
    fig.rect((x, y, x + w, y + 48), fill=fill, outline=outline, radius=24, width=2)
    fig.text((x + w // 2, y + 12), text, base.F_TINY, fill=outline, anchor="ma")


def score_dots(fig: base.Figure, x: int, y: int, active: int, outline: str, total: int = 5) -> None:
    for i in range(total):
        fill = outline if i < active else "#ffffff"
        fig.ellipse((x + i * 38, y, x + i * 38 + 18, y + 18), fill=fill, outline=outline, width=2)


def rank_row(fig: base.Figure, x: int, y: int, rank: str, name: str, support: int, note: str, highlight: bool = False) -> None:
    fill = "#fff6d8" if highlight else "#ffffff"
    outline = base.YELLOW_DARK if highlight else "#cbd2d8"
    fig.rect((x, y, x + 790, y + 76), fill=fill, outline=outline, radius=12, width=3 if highlight else 2)
    fig.text((x + 28, y + 20), rank, base.F_BOLD_SMALL, fill=outline)
    fig.text((x + 95, y + 18), name, base.F_BOLD_SMALL, fill=base.INK)
    score_dots(fig, x + 245, y + 25, support, outline)
    fig.paragraph((x + 465, y + 15), note, base.F_TINY, 290, fill=base.MUTED, line_gap=2)


def main() -> None:
    fig = base.Figure()
    fig.text((2100, 70), "Multi-agent design and AMD1 reasoning path for MK-driven vascular remodeling", base.F_TITLE, anchor="ma")
    fig.text(
        (2100, 142),
        "Functional modules, clean one-cycle architecture, and evidence-funnel reasoning for AMD1 prioritization.",
        base.F_SMALL,
        fill=base.MUTED,
        anchor="ma",
    )

    # Panel A
    ax, ay, aw, ah = 110, 220, 3980, 1110
    fig.rect((ax, ay, ax + aw, ay + ah), fill=base.WHITE, outline="#bfc7ce", radius=20)
    base.panel_header(fig, "a", "Overall design grouped by functional modules", ax + 40, ay + 34, aw - 80)

    fig.rect((ax + 70, ay + 150, ax + 735, ay + 970), fill=base.BLUE, outline=base.BLUE_DARK, radius=18, dash=True)
    fig.text((ax + 402, ay + 190), "Inputs and goal", base.F_HEAD, anchor="ma")
    input_box(fig, ax + 110, ay + 260, "Research goal", "Identify how hypoxic in-situ lung MKs drive pulmonary vascular remodeling.", "target")
    input_box(fig, ax + 110, ay + 465, "User omics data", "scRNA-seq, CD41+ metabolomics, whole-lung metabolomics, prior in-vivo MK evidence.", "data")
    input_box(fig, ax + 110, ay + 670, "Knowledge scaffold", "KEGG pathway mapping and literature provide context, not causal proof.", "cluster")

    fig.arrow((ax + 755, ay + 560), (ax + 890, ay + 560), fill=base.LINE, width=5)
    sx1, sy1, sx2, sy2 = ax + 910, ay + 150, ax + 3130, ay + 970
    fig.rect((sx1, sy1, sx2, sy2), fill="#fffafa", outline=base.PINK_DARK, radius=20)
    fig.text((sx1 + 1110, sy1 + 36), "Co-scientist functional modules", base.F_HEAD, anchor="ma")
    icon_agent(fig, sx1 + 90, sy1 + 18, base.PINK_DARK)
    icon_agent(fig, sx2 - 150, sy1 + 18, base.PINK_DARK)

    modules = [
        ("Supervisor / planning", "PI Agent", "sets goal, constraints, output format, and final feedback", base.PINK, base.PINK_DARK),
        (
            "Bioinformatics and evidence",
            "Bioinformatics Agent + Tool Use Agent",
            "centralizes scRNA/omics analysis: expression, DE, cell-type specificity, receptor/marker checks; summarizes KEGG/PubMed context",
            base.GRAY,
            base.GRAY_DARK,
        ),
        ("Metabolic evidence", "Metabolic Agent", "prioritizes metabolite-enzyme-gene chains and flags mechanism-ready anchors", base.GREEN, base.GREEN_DARK),
        ("Hypothesis generation", "Generation Agents", "propose broad, non-redundant candidate mechanisms from the PI brief and evidence package", base.YELLOW, base.YELLOW_DARK),
        ("Critical review and ranking", "Proximity + Reflection + Ranking", "clusters duplicates, critiques evidence, penalizes over-claiming, scores priority", base.BLUE, base.BLUE_DARK),
        ("Synthesis and evolution", "Meta-review + Evolution", "merges, simplifies, and refines the strongest defensible directions", base.PURPLE, base.PURPLE_DARK),
    ]
    mx, my, mw, mh = sx1 + 55, sy1 + 120, 675, 205
    for i, item in enumerate(modules):
        col, row = i % 3, i // 3
        module_box(fig, mx + col * 725, my + row * 295, mw, mh, *item)

    fig.arrow((sx2 + 20, ay + 560), (ax + 3230, ay + 560), fill=base.LINE, width=5)
    fig.rect((ax + 3250, ay + 150, ax + 3910, ay + 970), fill=base.YELLOW, outline=base.YELLOW_DARK, radius=18, dash=True)
    fig.text((ax + 3580, ay + 190), "Outputs", base.F_HEAD, anchor="ma")
    y = ay + 285
    for item in ["ranked hypothesis landscape", "merged/refined directions", "current model figure", "falsifiable experiments", "next-cycle research brief"]:
        y = fig.paragraph((ax + 3315, y), item, base.F_SMALL, 530, fill=base.INK, bullet=True, line_gap=8) + 18
    fig.rect((ax + 3315, ay + 770, ax + 3845, ay + 900), fill=base.WHITE, outline=base.YELLOW_DARK, radius=12)
    fig.text((ax + 3345, ay + 795), "Figure focus", base.F_BOLD_SMALL, fill=base.YELLOW_DARK)
    fig.paragraph((ax + 3345, ay + 838), "direction-level model; bridge provisional", base.F_SMALL, 455, fill=base.INK)

    # Panel B
    bx, by, bw, bh = 110, 1405, 3980, 690
    fig.rect((bx, by, bx + bw, by + bh), fill=base.WHITE, outline="#bfc7ce", radius=20)
    base.panel_header(fig, "b", "One-cycle architecture with parallel modules", bx + 40, by + 34, bw - 80)
    fig.rect((bx + 220, by + 100, bx + bw - 220, by + 175), fill="#f8fafb", outline="#cbd2d8", radius=12)
    fig.text((bx + 260, by + 122), "Nonlinear structure:", base.F_BOLD_SMALL, fill=base.INK)
    fig.paragraph((bx + 650, by + 120), "the PI brief fans out to evidence analysis and generation branches in parallel; review modules also run in parallel before synthesis.", base.F_TINY, 3000, fill=base.MUTED, line_gap=4)

    # Input and PI supervisor
    flow_node(fig, bx + 140, by + 310, "Inputs", "goal + data", base.BLUE, base.BLUE_DARK, "data")
    flow_node(fig, bx + 700, by + 310, "PI brief", "task + constraints", base.PINK, base.PINK_DARK, "agent")
    fig.arrow((bx + 610, by + 395), (bx + 685, by + 395), fill=base.LINE, width=5, head=20)

    # Parallel branch layer
    branch_x = bx + 1280
    branch_boxes = [
        ("Bioinformatics", "scRNA / sequencing evidence", branch_x, by + 190, base.GRAY, base.GRAY_DARK, "gene"),
        ("Metabolic", "metabolite-enzyme chains", branch_x, by + 350, base.GREEN, base.GREEN_DARK, "molecule"),
        ("Generation", "candidate mechanisms", branch_x, by + 510, base.YELLOW, base.YELLOW_DARK, "idea"),
    ]
    bus_x = bx + 1190
    fig.line((bus_x, by + 275, bus_x, by + 595), fill=base.LINE, width=5)
    fig.arrow((bx + 1160, by + 395), (bus_x, by + 395), fill=base.LINE, width=5, head=18)
    for title, sub, x, y, fill, outline, icon in branch_boxes:
        flow_node(fig, x, y, title, sub, fill, outline, icon)
        fig.arrow((bus_x, y + 85), (x - 15, y + 85), fill=base.LINE, width=5, head=18)

    # Convergence into parallel review layer
    merge_x = bx + 1850
    fig.line((branch_x + 475, by + 275, merge_x, by + 275), fill=base.LINE, width=5)
    fig.line((branch_x + 475, by + 435, merge_x, by + 435), fill=base.LINE, width=5)
    fig.line((branch_x + 475, by + 595, merge_x, by + 595), fill=base.LINE, width=5)
    fig.line((merge_x, by + 275, merge_x, by + 595), fill=base.LINE, width=5)
    fig.arrow((merge_x, by + 435), (bx + 2000, by + 435), fill=base.LINE, width=5, head=20)

    review_boxes = [
        ("Proximity", "cluster / de-duplicate", bx + 2015, by + 190, base.PURPLE, base.PURPLE_DARK, "cluster"),
        ("Reflection", "critique evidence", bx + 2015, by + 350, base.BLUE, base.BLUE_DARK, "review"),
        ("Ranking", "score priority", bx + 2015, by + 510, base.YELLOW, base.YELLOW_DARK, "rank"),
    ]
    for title, sub, x, y, fill, outline, icon in review_boxes:
        flow_node(fig, x, y, title, sub, fill, outline, icon)

    review_merge = bx + 2535
    for _, _, x, y, _, _, _ in review_boxes:
        fig.line((x + 460, y + 85, review_merge, y + 85), fill=base.LINE, width=5)
    fig.line((review_merge, by + 275, review_merge, by + 595), fill=base.LINE, width=5)
    fig.arrow((review_merge, by + 435), (bx + 2690, by + 435), fill=base.LINE, width=5, head=20)

    flow_node(fig, bx + 2705, by + 350, "Synthesis", "meta-review + evolution", base.GREEN, base.GREEN_DARK, "cluster")
    fig.arrow((bx + 3175, by + 435), (bx + 3255, by + 435), fill=base.LINE, width=5, head=20)
    flow_node(fig, bx + 3270, by + 350, "Output", "PI final feedback", base.PINK, base.PINK_DARK, "document")

    fig.text((bx + 3290, by + 615), "Output feeds the next PI brief", base.F_TINY, fill=base.PINK_DARK, anchor="ma")

    # Panel C
    cx, cy, cw, ch = 110, 2165, 3980, 1280
    fig.rect((cx, cy, cx + cw, cy + ch), fill=base.WHITE, outline="#bfc7ce", radius=22)
    base.panel_header(fig, "c", "Concrete example: from broad search to AMD1 prioritization", cx + 40, cy + 34, cw - 80)

    # Step 1: broad public search.
    search_x, search_y = cx + 80, cy + 145
    fig.rect((search_x, search_y, search_x + 900, search_y + 430), fill=base.BLUE, outline=base.BLUE_DARK, radius=18)
    badge(fig, search_x + 24, search_y + 26, "1", "#ffffff", base.BLUE_DARK)
    icon_review(fig, search_x + 805, search_y + 24, base.BLUE_DARK)
    fig.text((search_x + 105, search_y + 25), "Broad evidence search", base.F_SUB, fill=base.INK)
    fig.paragraph(
        (search_x + 38, search_y + 92),
        "Start with the open question: which MK-linked genes or pathways could connect hypoxia to vascular remodeling?",
        base.F_SMALL,
        790,
        fill=base.INK,
        line_gap=6,
    )
    source_tile(fig, search_x + 38, search_y + 190, "PubMed", "mechanism and disease literature", "document", base.BLUE_DARK)
    source_tile(fig, search_x + 430, search_y + 190, "KEGG/Reactome", "pathway neighborhoods", "cluster", base.GREEN_DARK)
    source_tile(fig, search_x + 38, search_y + 300, "GEO/scRNA", "cell-type expression context", "gene", base.GRAY_DARK)
    source_tile(fig, search_x + 430, search_y + 300, "Public atlases", "markers and tissue context", "data", base.PURPLE_DARK)

    # Step 2: a broad candidate pool before AMD1 becomes focal.
    pool_x, pool_y = cx + 80, cy + 615
    fig.rect((pool_x, pool_y, pool_x + 900, pool_y + 365), fill="#ffffff", outline=base.GRAY_DARK, radius=18)
    badge(fig, pool_x + 24, pool_y + 24, "2", "#ffffff", base.GRAY_DARK)
    icon_cluster(fig, pool_x + 815, pool_y + 24, base.GRAY_DARK)
    fig.text((pool_x + 105, pool_y + 25), "Candidate pool", base.F_SUB, fill=base.INK)
    fig.paragraph(
        (pool_x + 38, pool_y + 88),
        "Agents extract many plausible directions first; AMD1 is only one item in the initial pool.",
        base.F_SMALL,
        775,
        fill=base.MUTED,
        line_gap=6,
    )
    chips = [
        ("Vegfa", 130), ("Il6", 105), ("Dnmt3b", 155), ("Cyp26b1", 170),
        ("Amd2", 120), ("Amd1", 120), ("Mmp9", 120), ("Col1a1", 150),
        ("Tgf-beta", 165), ("S100a8", 150), ("Cxcl12", 145), ("Hif1a", 125),
    ]
    chip_positions = [
        (pool_x + 50, pool_y + 165), (pool_x + 210, pool_y + 165), (pool_x + 345, pool_y + 165), (pool_x + 535, pool_y + 165),
        (pool_x + 715, pool_y + 165), (pool_x + 92, pool_y + 230), (pool_x + 245, pool_y + 230), (pool_x + 405, pool_y + 230),
        (pool_x + 590, pool_y + 230), (pool_x + 92, pool_y + 295), (pool_x + 275, pool_y + 295), (pool_x + 460, pool_y + 295),
    ]
    for (name, width), (px, py) in zip(chips, chip_positions):
        candidate_chip(fig, px, py, name, "#ffffff", base.GRAY_DARK, w=width)

    # Step 3: evidence filters narrow the pool.
    fig.arrow((search_x + 900, cy + 520), (cx + 1105, cy + 520), fill=base.LINE, width=5, head=20)
    fig.arrow((pool_x + 900, pool_y + 180), (cx + 1105, pool_y + 180), fill=base.LINE, width=5, head=20)
    funnel_x, funnel_y = cx + 1080, cy + 145
    polygon(
        fig,
        [(funnel_x + 15, funnel_y + 15), (funnel_x + 1190, funnel_y + 15), (funnel_x + 980, funnel_y + 820), (funnel_x + 230, funnel_y + 820)],
        "#f8fafb",
        "#cbd2d8",
        width=3,
    )
    badge(fig, funnel_x + 65, funnel_y + 45, "3", "#ffffff", base.GREEN_DARK)
    fig.text((funnel_x + 160, funnel_y + 45), "Evidence filters applied in parallel", base.F_SUB, fill=base.INK)
    filter_rows = [
        ("MK expression", "gene expressed/enriched in MKs", "gene", base.GRAY, base.GRAY_DARK, 980),
        ("Disease shift", "PH/hypoxia regulation in MKs", "data", base.BLUE, base.BLUE_DARK, 880),
        ("Metabolic anchor", "CD41+ metabolite change", "molecule", base.GREEN, base.GREEN_DARK, 780),
        ("Pathway support", "connected pathway neighborhood", "cluster", base.YELLOW, base.YELLOW_DARK, 680),
        ("Review penalty", "merge duplicates; soften over-specific bridges", "review", base.PINK, base.PINK_DARK, 580),
    ]
    fy = funnel_y + 130
    for title, body, icon, fill, outline, width in filter_rows:
        fx = funnel_x + 600 - width // 2
        fig.rect((fx, fy, fx + width, fy + 86), fill=fill, outline=outline, radius=18)
        draw_icon(fig, icon, fx + 24, fy + 15, outline)
        fig.text((fx + 105, fy + 16), title, base.F_BOLD_SMALL, fill=base.INK)
        fig.text((fx + 330, fy + 17), body, base.F_TINY, fill=base.MUTED)
        if title != "Review penalty":
            fig.arrow((funnel_x + 600, fy + 90), (funnel_x + 600, fy + 118), fill=base.LINE, width=4, head=12)
        fy += 122

    fig.rect((funnel_x + 360, funnel_y + 770, funnel_x + 840, funnel_y + 890), fill="#ffffff", outline=base.GREEN_DARK, radius=18, width=3)
    fig.text((funnel_x + 600, funnel_y + 800), "Shortlist after filtering", base.F_BOLD_SMALL, fill=base.GREEN_DARK, anchor="ma")
    fig.text((funnel_x + 600, funnel_y + 842), "Amd1  |  Amd2  |  Dnmt3b  |  Cyp26b1", base.F_TINY, fill=base.INK, anchor="ma")

    # Step 4: evidence aggregation and ranking.
    rank_x, rank_y = cx + 2440, cy + 145
    fig.arrow((funnel_x + 1210, cy + 520), (rank_x - 25, cy + 520), fill=base.LINE, width=5, head=20)
    fig.rect((rank_x, rank_y, rank_x + 860, rank_y + 565), fill="#fffafa", outline=base.PINK_DARK, radius=18)
    badge(fig, rank_x + 28, rank_y + 30, "4", "#ffffff", base.PINK_DARK)
    icon_rank(fig, rank_x + 770, rank_y + 28, base.PINK_DARK)
    fig.text((rank_x + 105, rank_y + 30), "Aggregate evidence and rank", base.F_SUB, fill=base.INK)
    fig.paragraph(
        (rank_x + 40, rank_y + 95),
        "Each candidate is scored by convergent support, not by one isolated observation.",
        base.F_SMALL,
        740,
        fill=base.MUTED,
        line_gap=5,
    )
    fig.text((rank_x + 245, rank_y + 165), "MK  PH  Metab  Path  Specific", base.F_TINY, fill=base.MUTED)
    rank_row(fig, rank_x + 35, rank_y + 198, "#1", "AMD1", 5, "passes all evidence filters; strongest convergence", highlight=True)
    rank_row(fig, rank_x + 35, rank_y + 286, "#2", "Amd2", 2, "related enzyme, weaker MK/PH convergence")
    rank_row(fig, rank_x + 35, rank_y + 374, "#3", "Dnmt3b", 2, "methylation link, less direct metabolic anchor")
    rank_row(fig, rank_x + 35, rank_y + 462, "#4", "Cyp26b1", 1, "plausible vascular biology, weaker pathway match")

    # Step 5: final direction-level model after prioritization.
    model_x, model_y = cx + 2440, cy + 765
    fig.arrow((rank_x + 430, rank_y + 565), (rank_x + 430, model_y - 20), fill=base.LINE, width=5, head=20)
    fig.rect((model_x, model_y, model_x + 860, model_y + 230), fill=base.YELLOW, outline=base.YELLOW_DARK, radius=18)
    badge(fig, model_x + 28, model_y + 30, "5", "#ffffff", base.YELLOW_DARK)
    icon_molecule(fig, model_x + 770, model_y + 28, base.YELLOW_DARK)
    fig.text((model_x + 105, model_y + 30), "Prioritized direction", base.F_SUB, fill=base.INK)
    fig.paragraph(
        (model_x + 45, model_y + 95),
        "Hypoxic MKs show an AMD1-linked methionine/SAM/polyamine metabolic state. Downstream immune, vascular stiffness, and EV/stromal axes remain candidate routes rather than fixed mechanisms.",
        base.F_SMALL,
        730,
        fill=base.INK,
        line_gap=7,
    )

    # Step 6: falsification loop and scope.
    test_x, test_y = cx + 1080, cy + 1040
    fig.rect((test_x, test_y, test_x + 2220, test_y + 120), fill=base.GRAY, outline=base.GRAY_DARK, radius=14)
    badge(fig, test_x + 28, test_y + 32, "6", "#ffffff", base.GRAY_DARK)
    icon_review(fig, test_x + 2120, test_y + 30, base.GRAY_DARK)
    fig.text((test_x + 105, test_y + 32), "Falsifiable test loop", base.F_SUB, fill=base.INK)
    fig.paragraph(
        (test_x + 490, test_y + 30),
        "MK Amd1 perturbation -> LC-MS for methionine/SAM/polyamines -> immune/vascular readouts -> medial thickness, muscularization, stiffness.",
        base.F_SMALL,
        1500,
        fill=base.MUTED,
        line_gap=6,
    )
    fig.line((test_x + 1120, test_y, test_x + 1120, model_y + 245), fill=base.GRAY_DARK, width=4, dash=True)
    fig.arrow((test_x + 1120, model_y + 245), (model_x + 430, model_y + 238), fill=base.GRAY_DARK, width=4, dash=True, head=18)

    note_y = cy + ch - 92
    fig.rect((cx + 70, note_y, cx + cw - 70, note_y + 62), fill="#fffafa", outline=base.PINK_DARK, radius=12)
    fig.text((cx + 105, note_y + 19), "Scope note:", base.F_BOLD_SMALL, fill=base.PINK_DARK)
    fig.paragraph(
        (cx + 330, note_y + 17),
        "Public-source hits, local omics, and agent review are used to prioritize a direction; the figure does not claim a final cytokine, receptor, immune subset, or EndMT route.",
        base.F_TINY,
        cw - 520,
        fill=base.PINK_DARK,
        line_gap=4,
    )

    lx, ly = 120, 3500
    fig.label((lx, ly), "direct data", "#ffffff", base.GREEN_DARK, w=220)
    fig.arrow((lx + 270, ly + 26), (lx + 445, ly + 26), fill=base.LINE, width=5, head=18)
    fig.text((lx + 470, ly + 13), "main information flow", base.F_TINY, fill=base.MUTED)
    fig.arrow((lx + 795, ly + 26), (lx + 970, ly + 26), fill=base.DASH, width=5, dash=True, head=18)
    fig.text((lx + 995, ly + 13), "feedback / candidate route", base.F_TINY, fill=base.MUTED)
    fig.text((base.W - 130, base.H - 55), "Figure: current Cycle 1 synthesis, generated from local multi-agent outputs", base.F_TINY, fill="#9aa3aa", anchor="ra")

    fig.save()


if __name__ == "__main__":
    main()
