#!/usr/bin/env python3
"""Figure for part 1, case 2: shared state with no boundaries.

Left: a shared todo pool anyone can see, one entry stale (Douyin K07/K32,
checked done at 15:31, never cleared). Right: the pet chat picks up the
stale entry and dispatches an already-finished job. Bottom: paper numbers.
v2.0 style: cold grey-white canvas, white cards, grey edges; the stale
entry line is ink bold (blue is reserved for the 5 allowed places); the
wrong-side box is a key card (blue edge + pale blue fill) — not an
inverse card, which at 5.1 x 2.1 units would be ~14% of the figure,
over the v2.0 inverse budget (<=8%). The only inverse card in this
set is case 1's small "派错了" card.
"""
import sys
sys.path.insert(0, "/home/hatch/workspace/modelscope-drafts/images")
from fig_common import *

fig, ax = new_fig(12, 5.4)
title(ax, "情况 2：共享的东西没划界，过期内容流进别人的决策", 5.1)

# left: shared pool
box(ax, 0.3, 2.5, 5.1, 2.1, PANEL)
ax.text(2.85, 4.35, "共享待办池（谁都看得见）", fontproperties=BOLD,
        fontsize=12.5, color=INK, ha="center", va="center")
ax.text(2.85, 3.85, "豆包 K07/K32 — 15:31 已核对完，过期，未清",
        fontproperties=BOLD, fontsize=11.5, color=INK, ha="center", va="center")
ax.text(2.85, 3.4, "Vivix 任务 — 进行中", fontproperties=FONT,
        fontsize=11.5, color=BODY, ha="center", va="center")
ax.text(2.85, 2.95, "即梦任务 — 进行中", fontproperties=FONT,
        fontsize=11.5, color=BODY, ha="center", va="center")

ax.annotate("", xy=(6.35, 3.55), xytext=(5.55, 3.55),
            arrowprops=dict(arrowstyle="->", color=ARROW_LINE, lw=1.5))
ax.text(5.95, 3.85, "不分你我\n直接拿来用", fontproperties=FONT, fontsize=10.5,
        color=ARROW_TEXT, ha="center", va="center")

# right: pet chat acts on the stale entry — key card (blue edge + pale
# blue fill). It is NOT an inverse card: at 5.1 x 2.1 units it would be
# ~14% of the figure, over the v2.0 inverse budget (<=8%); the only
# inverse card in this set is case 1's small "派错了" card.
box(ax, 6.6, 2.5, 5.1, 2.1, BLUE_PALE, BLUE)
ax.text(9.15, 4.35, "宠物旁聊按过期待办动手", fontproperties=BOLD,
        fontsize=12.5, color=INK, ha="center", va="center")
ax.text(9.15, 3.75, "派了豆包 K07/K32", fontproperties=FONT, fontsize=12,
        color=BODY, ha="center", va="center")
ax.text(9.15, 3.25, "其实 15:31 已经完成了", fontproperties=FONT,
        fontsize=12, color=BODY, ha="center", va="center")

# bottom strip: paper numbers
box(ax, 0.3, 0.35, 11.4, 1.45, PANEL, PANEL_EDGE)
ax.text(6, 1.48, "论文测的数：共享状态不划界，正常用也会污染",
        fontproperties=BOLD, fontsize=12.5, color=INK, ha="center", va="center")
ax.text(6, 0.95, "UCC 污染 57%–71% · MemLeak 泄漏 70%–100%",
        fontproperties=FONT, fontsize=12, color=BODY, ha="center", va="center")
ax.text(6, 0.55, "DACS 隔离后，污染 28–57% → 0–14%",
        fontproperties=FONT, fontsize=12, color=BODY, ha="center", va="center")

plt.tight_layout()
plt.savefig("/home/hatch/workspace/modelscope-drafts/images/case2-shared-context-mono-v1.png",
            dpi=200, facecolor=BG, bbox_inches="tight")
print("saved")
