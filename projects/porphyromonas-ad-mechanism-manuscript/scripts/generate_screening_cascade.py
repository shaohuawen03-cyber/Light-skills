#!/usr/bin/env python3
"""Redraw Figure 1: centred arrows, unified initial capitals. No titles or footnotes."""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "manuscript" / "figures"
SVG = OUT / "fig_screening_cascade.svg"
PNG = OUT / "fig_screening_cascade.png"

BLUE = "#1b4f72"
BLUE_NUM = "#0072B2"
BLUE_FILL = "#eaf4fa"
GRAY_FILL = "#f2f4f5"
GRAY_STROKE = "#7f8c8d"
CREAM = "#fbf0dc"
GREEN = "#009E73"
GREEN_FILL = "#e6f4ef"
LABEL = "#333333"


def rbox(ax, x, y, w, h, fill, stroke, lw=1.6):
    p = FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle="round,pad=0.02,rounding_size=0.35",
        facecolor=fill,
        edgecolor=stroke,
        linewidth=lw,
        mutation_aspect=1,
        clip_on=False,
        zorder=2,
    )
    ax.add_patch(p)
    return x + w / 2.0, y + h / 2.0


def v_arrow(ax, x, y_from, y_to, color=BLUE):
    """Vertical arrow, same x, from upper edge to lower edge."""
    ax.add_patch(
        FancyArrowPatch(
            (x, y_from),
            (x, y_to),
            arrowstyle="-|>",
            mutation_scale=11,
            linewidth=1.55,
            color=color,
            shrinkA=0.0,
            shrinkB=0.0,
            clip_on=False,
            zorder=3,
        )
    )


def h_arrow(ax, x_from, x_to, y, color=BLUE):
    """Horizontal arrow, same y."""
    ax.add_patch(
        FancyArrowPatch(
            (x_from, y),
            (x_to, y),
            arrowstyle="-|>",
            mutation_scale=11,
            linewidth=1.55,
            color=color,
            shrinkA=0.0,
            shrinkB=0.0,
            clip_on=False,
            zorder=3,
        )
    )


def main() -> None:
    fig, ax = plt.subplots(figsize=(7.105, 8.602), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis("off")
    fig.subplots_adjust(left=0.035, right=0.965, top=0.975, bottom=0.03)

    cx = 50.0
    gap = 2.15

    # Top pair
    hw, hh = 43.5, 13.6
    hy = 84.6
    hx1, hx2 = 4.4, 52.1
    rbox(ax, hx1, hy, hw, hh, GRAY_FILL, GRAY_STROKE, lw=1.35)
    rbox(ax, hx2, hy, hw, hh, BLUE_FILL, BLUE, lw=1.7)
    ax.text(hx1 + hw / 2, hy + 10.35, "Healthy", ha="center", va="center", fontsize=12.5, fontweight="bold", color="#111", zorder=4)
    ax.text(hx1 + hw / 2, hy + 6.15, "11.27 million", ha="center", va="center", fontsize=16.5, fontweight="bold", color=BLUE_NUM, zorder=4)
    ax.text(hx1 + hw / 2, hy + 2.35, "22 Models Only", ha="center", va="center", fontsize=9.2, color=LABEL, zorder=4)
    ax.text(hx2 + hw / 2, hy + 10.35, "Periodontitis", ha="center", va="center", fontsize=12.5, fontweight="bold", color="#111", zorder=4)
    ax.text(hx2 + hw / 2, hy + 6.15, "11.72 million", ha="center", va="center", fontsize=16.5, fontweight="bold", color=BLUE_NUM, zorder=4)
    ax.text(hx2 + hw / 2, hy + 2.35, "22 Models, Then Matched", ha="center", va="center", fontsize=9.2, color=LABEL, zorder=4)

    # Funnel steps: (width, height, fill, stroke, lw, label, number, num_size)
    steps = [
        (74.0, 9.6, BLUE_FILL, BLUE, 1.55, "BBB ≥ 0.80", "1.13 million", 16.5),
        (66.0, 9.6, BLUE_FILL, BLUE, 1.55, "Metaproteome Unique", "33,786", 17.5),
        (58.0, 9.6, BLUE_FILL, BLUE, 1.55, "BBB × Catalogue", "3,518", 17.5),
        (51.0, 9.6, BLUE_FILL, BLUE, 1.55, "NTxPred2 Positive", "923", 17.5),
        (46.0, 9.6, CREAM, BLUE, 1.55, "Mebipred + AnOxPePred", "12 Peptides", 16.5),
    ]

    y = hy - gap
    boxes = []
    for w, h, fill, stroke, lw, lab, num, ns in steps:
        y -= h
        x = cx - w / 2.0
        rbox(ax, x, y, w, h, fill, stroke, lw=lw)
        ax.text(cx, y + 6.85, lab, ha="center", va="center", fontsize=9.4, color=LABEL, zorder=4)
        ax.text(cx, y + 2.85, num, ha="center", va="center", fontsize=ns, fontweight="bold", color=BLUE_NUM, zorder=4)
        boxes.append((x, y, w, h))
        y -= gap

    # Periodontitis → first funnel box (vertical, under Periodontitis centre)
    perio_cx = hx2 + hw / 2.0
    b0x, b0y, b0w, b0h = boxes[0]
    v_arrow(ax, perio_cx, hy, b0y + b0h)

    # Funnel arrows on the shared centre line
    for i in range(len(boxes) - 1):
        _, y1, _, h1 = boxes[i]
        _, y2, _, h2 = boxes[i + 1]
        v_arrow(ax, cx, y1, y2 + h2)

    # Bottom row: Docking centred under funnel; MD to the right; horizontal arrow
    dw, dh = 31.6, 12.4
    dx = cx - dw / 2.0
    last = boxes[-1]
    dy = last[1] - gap - dh
    if dy < 1.6:
        dy = 1.6
    mx = dx + dw + 4.2
    mw = 31.6
    rbox(ax, dx, dy, dw, dh, BLUE_FILL, BLUE, lw=1.7)
    rbox(ax, mx, dy, mw, dh, GREEN_FILL, GREEN, lw=1.7)
    ax.text(dx + dw / 2, dy + 9.15, "Docking", ha="center", va="center", fontsize=12.5, fontweight="bold", color="#111", zorder=4)
    ax.text(dx + dw / 2, dy + 4.15, "12 Peptides", ha="center", va="center", fontsize=16.0, fontweight="bold", color=BLUE_NUM, zorder=4)
    ax.text(mx + mw / 2, dy + 9.15, "MD", ha="center", va="center", fontsize=12.5, fontweight="bold", color="#111", zorder=4)
    ax.text(mx + mw / 2, dy + 4.15, "3 Complexes", ha="center", va="center", fontsize=16.0, fontweight="bold", color=GREEN, zorder=4)

    # 12 peptides → Docking, vertical on centre line
    last = boxes[-1]
    v_arrow(ax, cx, last[1], dy + dh)
    # Docking → MD, horizontal at box mid-height
    h_arrow(ax, dx + dw, mx, dy + dh / 2.0)

    fig.savefig(PNG, dpi=300, facecolor="white")
    fig.savefig(SVG, facecolor="white")
    plt.close(fig)
    print(PNG)
    print(SVG)


if __name__ == "__main__":
    main()
