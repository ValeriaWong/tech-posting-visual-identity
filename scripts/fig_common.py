#!/usr/bin/env python3
"""Shared style for the cross-chat article figures.

v2.0 (2026-11-25, WorkBuddy visual-designer expert spec, via Allen):
monochrome minimal — cold grey-white canvas, white cards, ONE tech blue
as the only highlight. This voids every dark / lamp-yellow / green /
red / amber value from v1.x:

- canvas #F7F8FA (cold grey-white, faintly blue, never warm); cards
  #FFFFFF; header/group backing #F2F4F7; sunk/zebra backing #E8EBF0
  (backing only, never carries body text). No dark background anywhere;
  no halo of any kind.
- text greys (cold neutral, no warm grey): title #111318 Bold
  (~17:1), body #2B3036 (~13:1), secondary #4A5158 (~8:1, never
  lighter), footnotes #6B727B (lowest, ~4.9:1, never lighter);
  inverse-card text #FFFFFF.
- borders: card edge #E2E6EB 1.5px; divider/axis/grid #D6DBE2 1px;
  weak divider #EDF0F4 1px; arrows #B3BAC5 1.5px (only the one key-path
  arrow may be blue); emphasis divider #111318 2px, max 2 per figure.
- tech blue (one main + one light): main #2563EB, light #A5C4F7,
  pale fill #EEF3FE. Blue appears ONLY at 5 places: (1) title rule
  (blue block 6px x ~140px, centered, 1 per figure); (2) key-card edge
  (blue 1.5px + #EEF3FE fill; secondary key card light blue 1.5px +
  white fill), <=2 cards per figure; (3) "new" bars solid blue;
  (4) "tested" status blue text (partially tested = light-blue hollow
  dot + blue text); (5) emphasized numbers blue, <=3 per figure.
  Blue pixels <=5% per figure (bar charts <=8%). Any blue elsewhere
  is a violation.
- old semantics, zero red / zero amber / zero warm: danger/error card
  -> inverse card #14171C bg + edge, title and body #FFFFFF, area
  <=8%, <=1 per figure. "Not tested" -> grey #6B727B regular weight +
  hollow dot (white fill / #B3BAC5 1px edge). "Tested" -> blue #2563EB
  (solid dot + blue text). "Partially tested" -> light-blue hollow dot
  + blue text. "Old" bars -> #C7CDD5 solid + 1px #B3BAC5 edge, value
  labels #4A5158. Old "total" highlight band -> neutral #F2F4F7.
  Bar-top highlight deleted (useless on white).
- acceptance: white/near-white (#FFFFFF-#F7F8FA) >=60%, only one blue
  family <=5% (bars <=8%), every text >=4.5:1 against its background
  (titles >=3:1), inverse elements total <=8% and never a background.

Only style changes here — no data, numbers, copy or layout. E16 and the
queue board do NOT import this module and are unaffected.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch
import matplotlib.font_manager as fm

SERIF = "/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc"
SERIF_BOLD = "/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc"
FONT = fm.FontProperties(fname=SERIF)
BOLD = fm.FontProperties(fname=SERIF_BOLD)

# --- v2.0 palette (monochrome minimal + one tech blue, 2026-11-25) ---
BG = "#f7f8fa"          # canvas, cold grey-white
PLOT_BG = "#ffffff"     # chart plot area (cards / paper white)
PANEL = "#ffffff"       # card background
PANEL_ALT = "#f2f4f7"   # header / group backing
PANEL2 = "#f2f4f7"      # column-header backing
SUNK = "#e8ebf0"        # sunk / disabled / zebra backing (no body text on it)
PANEL_EDGE = "#e2e6eb"  # card border, 1.5px
RULE = "#d6dbe2"        # divider / axis / grid lines
GRID = "#edf0f4"        # grid + weak divider
WEAK = "#edf0f4"

INK = "#111318"         # titles / card headings, near black
BODY = "#2b3036"        # card body text
SECONDARY = "#4a5158"   # secondary text (ticks / legends / arrow labels)
FOOT = "#6b727b"        # footnotes (lowest grey allowed)
ANNOT = "#4a5158"       # arrow annotations / axis ticks / legends
ARROW_LINE = "#b3bac5"  # arrow / connector lines (structure figures)
ARROW_TEXT = "#4a5158"  # arrow label text (structure figures)
AXIS = "#d6dbe2"        # chart axis lines

BLUE = "#2563eb"        # tech blue — the ONLY highlight colour
BLUE_LIGHT = "#a5c4f7"  # light blue — secondary highlight (fill/edge/bar/dot only, never small text)
BLUE_PALE = "#eef3fe"   # pale blue card fill (key cards)
GREY_BAR = "#c7cdd5"    # old-practice bars / baseline points
GREY_EDGE = "#b3bac5"   # old-bar edge / hollow-dot edge
INVERSE = "#14171c"     # danger / error card: dark inverse fill + edge
INVERSE_TEXT = "#ffffff"  # text on an inverse card

# semantic aliases (same names the v1.x scripts used, new values)
GREEN = BLUE            # tested / "now" — blue in v2.0
GREEN_PART = BLUE       # partially-tested status TEXT is blue in v2.0
GREEN_BG = BLUE_PALE    # key-card fill — pale blue in v2.0
GREEN_DARK = INK        # key-card titles are ink in v2.0 (blue text is
                        # reserved for statuses and emphasized numbers)
GREY = GREY_BAR

CALLOUT_BG = "#ffffff"  # methods-map bottom callout fill
CALLOUT_EDGE = PANEL_EDGE  # methods-map bottom callout edge (grey in v2.0:
                        # the two starred chips are already the key cards)

# legacy aliases
MID = SECONDARY
MUTED = ANNOT
FAINT = FOOT

# NOTE: RED, RED_BG, LAMP, AMBER_* are deliberately NOT defined here.
# Any script still referencing them fails loudly instead of silently
# drawing a red / amber / lamp / green element.


def new_fig(w, h):
    """Cold grey-white canvas, no halo, no gradient."""
    fig, ax = plt.subplots(figsize=(w, h))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, h)
    ax.axis("off")
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)
    return fig, ax


def apply_bg(fig, ax):
    """Set the canvas to the v2.0 background."""
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)


def title(ax, text, y, size=19):
    ax.text(6, y, text, fontproperties=BOLD, fontsize=size,
            color=INK, ha="center")
    # blue rule under the title: ~140px wide, 6px high at dpi=200
    # (12 units span 2400px, so 0.7 units = 140px; 6px = ~2.2pt)
    ax.plot([5.65, 6.35], [y - 0.22, y - 0.22], color=BLUE, lw=2.2,
            solid_capstyle="round")


def chart_title_rule(ax):
    """Blue rule just below the set_title text (chart figures).

    Must be called AFTER plt.tight_layout(): it measures the title's
    real bounding box and puts the rule a hair below it, so it can
    never cross the title glyphs. Rule is ~140px wide, 6px high.
    """
    fig = plt.gcf()
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    tb = ax.title.get_window_extent(renderer)
    inv = ax.transAxes.inverted()
    (x0, y0), (x1, y1) = inv.transform([(tb.x0, tb.y0), (tb.x1, tb.y1)])
    cx = (x0 + x1) / 2
    hw = min(0.045, (x1 - x0) * 0.18)
    ax.plot([cx - hw, cx + hw], [y0 - 0.012, y0 - 0.012],
            transform=ax.transAxes, color=BLUE, lw=2.2,
            solid_capstyle="round", clip_on=False)


def subtitle(ax, text, y, size=11):
    ax.text(6, y, text, fontproperties=FONT, fontsize=size,
            color=FOOT, ha="center")


def box(ax, x, y, w, h, facecolor, edgecolor=None, lw=1.5, radius=0.12,
        linestyle="solid"):
    if edgecolor is None:
        edgecolor = PANEL_EDGE
    ax.add_patch(FancyBboxPatch((x, y), w, h,
                 boxstyle=f"round,pad=0.06,rounding_size={radius}",
                 facecolor=facecolor, edgecolor=edgecolor,
                 linewidth=lw, linestyle=linestyle))


def seg_text(ax, cx, y, segments, size=11.5, bold=False, va="center"):
    """Draw one centered line made of (text, colour) segments.

    Widths are measured from the real renderer, so segment boundaries
    align exactly with the grey text underneath. Call AFTER
    plt.tight_layout(): the axes transform is final by then.
    """
    fig = ax.figure
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    fp = BOLD if bold else FONT
    widths = []
    for text, _ in segments:
        t = ax.text(0, 0, text, fontproperties=fp, fontsize=size)
        widths.append(t.get_window_extent(renderer).width)
        t.remove()
    total = sum(widths)
    x0_disp = ax.transData.transform((cx, y))[0] - total / 2
    x = x0_disp
    for (text, color), w in zip(segments, widths):
        xd, _ = ax.transData.inverted().transform((x, 0))
        ax.text(xd, y, text, fontproperties=fp, fontsize=size,
                color=color, ha="left", va=va)
        x += w


def status_dot(ax, cx, y, kind):
    """Status dot for the methods-map three-dot system.

    kind: "tested" (solid blue), "partial" (hollow, light-blue edge),
    "untested" (hollow, grey edge). Radius ~0.065 data units.
    """
    if kind == "tested":
        ax.add_patch(Circle((cx, y), 0.065, facecolor=BLUE,
                            edgecolor=BLUE, linewidth=1.0, zorder=6))
    elif kind == "partial":
        ax.add_patch(Circle((cx, y), 0.065, facecolor="#ffffff",
                            edgecolor=BLUE_LIGHT, linewidth=1.5, zorder=6))
    else:  # untested
        ax.add_patch(Circle((cx, y), 0.065, facecolor="#ffffff",
                            edgecolor=GREY_EDGE, linewidth=1.0, zorder=6))
