#!/usr/bin/env python3
"""Plot the external v0.4 source-reported Vina summary with an explicit provenance boundary."""
from __future__ import annotations

from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
FIG = ROOT / "manuscript" / "figures"
SVG = FIG / "fig5_docking_scores.svg"
PNG = FIG / "fig5_docking_scores.png"
DATA = [
    ("FLLHTTR", -9.60, 0.08), ("YLSLLQR", -9.49, 0.05),
    ("ALLLHRC", -9.29, 0.11), ("FCLHLQLR", -9.27, 0.09),
    ("YHHLLCRR", -9.03, 0.07), ("LLHLPKRTT", -9.01, 0.06),
    ("LLHPLRL", -8.94, 0.10), ("WLLVHLKK", -8.94, 0.04),
    ("LLHPLRC", -8.91, 0.08), ("HLLTLKKHV", -8.88, 0.05),
    ("HLPLLHRCC", -8.35, 0.12), ("HVLLLRQCA", -8.25, 0.09),
]


def ymap(value: float) -> float:
    # Plot range -10.0 to -7.8 onto y=690 to y=160.
    return 160 + (-7.8 - value) / 2.2 * 530


def main() -> None:
    FIG.mkdir(parents=True, exist_ok=True)
    width, height = 1600, 940
    left, right, baseline = 130, 1540, ymap(-7.8)
    bar_w, gap = 78, 34
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="1600" height="940" fill="#FFFFFF"/>',
        '<style>.t{font-family:Arial,Helvetica,sans-serif;fill:#102A43}.s{font-family:Arial,Helvetica,sans-serif;fill:#52616B}</style>',
        '<text x="130" y="58" class="t" font-size="34" font-weight="700">Source-reported PAS-focused docking summary (human AChE, PDB 4EY6)</text>',
        '<text x="130" y="96" class="s" font-size="22">Mean ± SD values transcribed from external v0.4; raw runs and poses were unavailable for independent reproduction</text>',
        f'<line x1="{left}" y1="{baseline}" x2="{right}" y2="{baseline}" stroke="#263238" stroke-width="3"/>',
        f'<line x1="{left}" y1="150" x2="{left}" y2="{baseline}" stroke="#263238" stroke-width="3"/>',
    ]
    for tick in (-10.0, -9.5, -9.0, -8.5, -8.0):
        y = ymap(tick)
        parts += [
            f'<line x1="{left-10}" y1="{y}" x2="{right}" y2="{y}" stroke="#D7DEE3" stroke-width="2"/>',
            f'<text x="{left-18}" y="{y+8}" class="s" font-size="21" text-anchor="end">{tick:.1f}</text>',
        ]
    yref = ymap(-8.0)
    parts.append(f'<line x1="{left}" y1="{yref}" x2="{right}" y2="{yref}" stroke="#66757F" stroke-width="3" stroke-dasharray="12 9"/>')
    for i, (name, mean, sd) in enumerate(DATA):
        x = left + 48 + i * (bar_w + gap)
        y = ymap(mean)
        color = "#0072B2" if i == 0 else "#D55E00"
        parts.append(f'<rect x="{x}" y="{baseline}" width="{bar_w}" height="{y-baseline}" fill="{color}"/>')
        y1, y2 = ymap(mean - sd), ymap(mean + sd)
        parts += [
            f'<line x1="{x+bar_w/2}" y1="{y1}" x2="{x+bar_w/2}" y2="{y2}" stroke="#455A64" stroke-width="4"/>',
            f'<line x1="{x+bar_w/2-10}" y1="{y1}" x2="{x+bar_w/2+10}" y2="{y1}" stroke="#455A64" stroke-width="4"/>',
            f'<line x1="{x+bar_w/2-10}" y1="{y2}" x2="{x+bar_w/2+10}" y2="{y2}" stroke="#455A64" stroke-width="4"/>',
            f'<text x="{x+bar_w/2}" y="{720+(i%2)*28}" class="t" font-size="18" text-anchor="middle">{name}</text>',
        ]
    parts += [
        '<text x="130" y="132" class="t" font-size="22">Source-reported AutoDock Vina score (kcal/mol)</text>',
        '<text x="1540" y="890" class="s" font-size="18" text-anchor="end">Descriptive within-set ordering only; scores are not binding free energies.</text>',
        '</svg>',
    ]
    SVG.write_text("\n".join(parts), encoding="utf-8")
    try:
        subprocess.run(["convert", "-density", "150", str(SVG), "-resize", "1600x940", str(PNG)], check=True, capture_output=True, text=True)
    except (FileNotFoundError, subprocess.CalledProcessError):
        # Draw the equivalent plot directly when ImageMagick lacks an SVG delegate.
        cmd = ["convert", "-size", "1600x940", "xc:white", "-gravity", "NorthWest", "-font", "DejaVu-Sans"]
        def draw(spec: str, *, fill="none", stroke="#263238", sw=2):
            cmd.extend(["-fill", fill, "-stroke", stroke, "-strokewidth", str(sw), "-draw", spec])
        def text(x: float, y: float, value: str, size: int, color="#102A43", anchor="start", bold=False):
            if bold:
                cmd.extend(["-font", "DejaVu-Sans-Bold"])
            cmd.extend(["-fill", color, "-stroke", "none", "-pointsize", str(size), "-draw", f"text-anchor {anchor} text {x},{y} '{value}'"])
            if bold:
                cmd.extend(["-font", "DejaVu-Sans"])
        text(130, 58, "Source-reported PAS-focused docking summary (human AChE, PDB 4EY6)", 34, bold=True)
        text(130, 96, "Mean +/- SD values transcribed from external v0.4; raw runs and poses unavailable for reproduction", 22, "#52616B")
        draw(f"line {left},{baseline} {right},{baseline}", sw=3)
        draw(f"line {left},150 {left},{baseline}", sw=3)
        for tick in (-10.0, -9.5, -9.0, -8.5, -8.0):
            yy = ymap(tick)
            draw(f"line {left-10},{yy} {right},{yy}", stroke="#D7DEE3", sw=2)
            text(left-18, yy+8, f"{tick:.1f}", 21, "#52616B", "end")
        # A segmented line is portable across minimal ImageMagick builds.
        yy = ymap(-8.0)
        for xx in range(left, right, 24):
            draw(f"line {xx},{yy} {min(xx+13,right)},{yy}", stroke="#66757F", sw=3)
        for i, (name, mean, sd) in enumerate(DATA):
            xx = left + 48 + i * (bar_w + gap)
            yy = ymap(mean)
            color = "#0072B2" if i == 0 else "#D55E00"
            draw(f"rectangle {xx},{yy} {xx+bar_w},{baseline}", fill=color, stroke=color, sw=1)
            y1, y2 = ymap(mean - sd), ymap(mean + sd)
            draw(f"line {xx+bar_w/2},{y1} {xx+bar_w/2},{y2}", stroke="#455A64", sw=4)
            draw(f"line {xx+bar_w/2-10},{y1} {xx+bar_w/2+10},{y1}", stroke="#455A64", sw=4)
            draw(f"line {xx+bar_w/2-10},{y2} {xx+bar_w/2+10},{y2}", stroke="#455A64", sw=4)
            text(xx+bar_w/2, 720+(i%2)*28, name, 17, anchor="middle")
        text(130, 132, "Source-reported AutoDock Vina score (kcal/mol)", 22)
        text(1540, 890, "Descriptive within-set ordering only; scores are not binding free energies.", 18, "#52616B", "end")
        cmd.append(str(PNG))
        subprocess.run(cmd, check=True)
    print(SVG)
    print(PNG)


if __name__ == "__main__":
    main()
