#!/usr/bin/env python3
"""Shared style for the cross-chat article figures.

Real spec: "深夜台灯风" option C from the P0 legal self-media chat
(2026-11-25 01:46) — the AGENTS.md cover v3 route: deep teal-black
background, serif white text, a touch of warm yellow lamplight.
Reference implementation:
~/workspace/graphic-matrix/agentsmd-tutorials-viz-alt-night-20261125.html
and the v3 cover image media-generation-agentsmd-v3-cover-0-*.webp.

Lamp yellow (#e8b34b) is used SPARINGLY: exactly one crisp lamp element
per figure — the short rule under the title, as on the v3 cover.
Everything else is teal-black panels, warm white serif text, and the
semantic data colours (green = correct, red = wrong/stale,
blue = third series, grey = old). Amber-tinted panels are a muted
lamplight wash only; they take the neutral panel edge, never a lamp
border. All nine figures that import this module share the palette.
E16 and the queue board do NOT import this module and are unaffected.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import matplotlib.font_manager as fm

SERIF = "/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc"
SERIF_BOLD = "/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc"
FONT = fm.FontProperties(fname=SERIF)
BOLD = fm.FontProperties(fname=SERIF_BOLD)

# --- real spec palette (from agentsmd-tutorials-viz-alt-night) ---
BG = "#101d1d"          # page background
DARKEST = "#0b1414"     # darkest, page outer
PANEL = "#1d2b2b"       # card background
PANEL2 = "#223232"      # card border / alt panel
PANEL_EDGE = "#2c3f3f"  # panel border
INK = "#f5f5f4"         # warm white, primary text
SECONDARY = "#d6d1c2"   # secondary text
MID = "#c9c4b4"         # secondary text (alt)
MUTED = "#9aa39a"       # muted text
FAINT = "#8f8a7c"       # weakest text

LAMP = "#e8b34b"        # lamp yellow — title rule only, one per figure

GREEN = "#6fcf9a"       # correct, on teal-black
GREEN_BG = "#14261f"    # dark green-teal panel
GREEN_DARK = "#a9e8c3"  # light green text on green panels

RED = "#f0807a"         # wrong / stale, on teal-black
RED_BG = "#2a1b1d"      # dark red panel

BLUE = "#7ab3f0"        # third series colour, on teal-black
BLUE_BG = "#152430"

GREY = "#7c857f"        # old / neutral series colour, on teal-black
GREY_BG = PANEL         # neutral panel

AMBER_BG = "#262214"    # warm tint panel (muted lamplight wash)
AMBER_EDGE = PANEL_EDGE # amber boxes take the neutral edge on purpose:
                        # the only crisp lamp element is the title rule.
AMBER = LAMP            # kept for compatibility; do not use as a data colour


def new_fig(w, h):
    fig, ax = plt.subplots(figsize=(w, h))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, h)
    ax.axis("off")
    fig.patch.set_facecolor(BG)
    return fig, ax


def title(ax, text, y, size=19):
    ax.text(6, y, text, fontproperties=BOLD, fontsize=size,
            color=INK, ha="center")
    # the one lamp accent: short rule under the title, as on the v3 cover
    ax.plot([5.55, 6.45], [y - 0.22, y - 0.22], color=LAMP, lw=3,
            solid_capstyle="round")


def chart_title_rule(ax):
    """Lamp rule just below the set_title text (chart figures).

    Must be called AFTER plt.tight_layout(): it measures the title's
    real bounding box and puts the rule a hair below it, so it can
    never cross the title glyphs.
    """
    fig = plt.gcf()
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    tb = ax.title.get_window_extent(renderer)
    inv = ax.transAxes.inverted()
    (x0, y0), (x1, y1) = inv.transform([(tb.x0, tb.y0), (tb.x1, tb.y1)])
    cx = (x0 + x1) / 2
    hw = min(0.037, (x1 - x0) * 0.18)
    ax.plot([cx - hw, cx + hw], [y0 - 0.012, y0 - 0.012],
            transform=ax.transAxes, color=LAMP, lw=3,
            solid_capstyle="round", clip_on=False)


def subtitle(ax, text, y, size=11):
    ax.text(6, y, text, fontproperties=FONT, fontsize=size,
            color=MUTED, ha="center")


def box(ax, x, y, w, h, facecolor, edgecolor=None, lw=1.2, radius=0.12):
    if edgecolor is None:
        edgecolor = PANEL_EDGE
    ax.add_patch(FancyBboxPatch((x, y), w, h,
                 boxstyle=f"round,pad=0.06,rounding_size={radius}",
                 facecolor=facecolor, edgecolor=edgecolor,
                 linewidth=lw))
