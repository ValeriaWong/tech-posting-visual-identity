#!/usr/bin/env python3
"""Figure for part 2, section 5: which method addresses which root cause,
and whether we have tested it. The point the figure makes: the two most
effective methods (1 and 2) are the untested ones.
v2.0 style: cold grey-white canvas, white cards, grey edges; the two
starred chips are the key cards (blue edge + pale blue fill, <=2 per
figure); status uses the three-dot system — tested: solid blue dot +
blue text; partially tested: light-blue hollow dot + blue text;
not tested: grey hollow dot + grey #6B727B text. Bottom callout is
white + grey edge (the starred chips already use the blue budget).
"""
import sys
sys.path.insert(0, "/home/hatch/workspace/modelscope-drafts/images")
from fig_common import *

fig, ax = new_fig(12, 5.8)
title(ax, "六种方法：针对哪个原因，我们测过没有", 5.5)

# (x, column title, chips: (label, status, kind))
cols = [
    (0.3, "原因一\n任务角色不清楚", [
        ("方法 5 · 交接信封 + 回执", "测过", "tested"),
        ("方法 4 · 集中验证", "部分测过", "partial"),
    ]),
    (3.25, "原因二\n共享状态没划界", [
        ("方法 1 · 所有权门控 ★", "没测过", "untested"),
        ("方法 2 · 上下文隔离 ★", "没测过", "untested"),
    ]),
    (6.2, "原因三\n派活依据太粗", [
        ("方法 3 · 按场景校准", "没测过", "untested"),
    ]),
    (9.15, "防失控", [
        ("方法 6 · 循环硬护栏", "测过对应做法", "tested"),
    ]),
]
for x, head, chips in cols:
    # column-header backing: #F2F4F7, column width, header-row height
    box(ax, x, 4.65, 2.7, 0.6, PANEL2, PANEL2, lw=1.0)
    ax.text(x + 1.35, 5.05, head, fontproperties=BOLD, fontsize=12,
            color=INK, ha="center", va="center")
    y = 4.35
    for label, status, kind in chips:
        starred = "★" in label
        # key cards (starred): blue edge + pale blue fill, solid;
        # untested non-starred chips keep a dashed grey edge
        fill = BLUE_PALE if starred else PANEL
        edge = BLUE if starred else PANEL_EDGE
        ls = "solid" if (starred or kind != "untested") else "dashed"
        box(ax, x, y - 0.75, 2.7, 0.95, fill, edge, linestyle=ls)
        ax.text(x + 1.35, y - 0.12, label, fontproperties=BOLD,
                fontsize=11, color=INK, ha="center", va="center")
        # status word + dot: dot sits left of the centered status text
        status_color = BLUE if kind in ("tested", "partial") else FOOT
        dot_x = (x + 1.35) - len(status) * 0.08 - 0.115
        status_dot(ax, dot_x, y - 0.46, kind)
        ax.text(x + 1.35, y - 0.5, status, fontproperties=FONT,
                fontsize=11.5, color=status_color, ha="center", va="center")
        y -= 1.25

# bottom callout
box(ax, 0.3, 0.35, 11.4, 1.15, CALLOUT_BG, CALLOUT_EDGE)
ax.text(6, 1.15, "最有效的两项（方法 1、2，带 ★）还没做",
        fontproperties=BOLD, fontsize=13, color=INK, ha="center", va="center")
ax.text(6, 0.68, "不是不想做，是这两项要改机制，不是改几行规则文字 —— 原因见 6.3。",
        fontproperties=FONT, fontsize=11.5, color=BODY, ha="center", va="center")

plt.tight_layout()
plt.savefig("/home/hatch/workspace/modelscope-drafts/images/methods-map-mono-v1.png",
            dpi=200, facecolor=BG, bbox_inches="tight")
print("saved")
