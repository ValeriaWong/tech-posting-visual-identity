#!/usr/bin/env python3
"""Figure for part 1, case 2: shared state with no boundaries.

Left: a shared todo pool anyone can see, one entry stale (Douyin K07/K32,
checked done at 15:31, never cleared). Right: the pet chat picks up the
stale entry and dispatches an already-finished job. Bottom: paper numbers.
"""
import sys
sys.path.insert(0, "/home/hatch/workspace/modelscope-drafts/images")
from fig_common import *

fig, ax = new_fig(12, 5.4)
title(ax, "情况 2：共享的东西没划界，过期内容流进别人的决策", 5.1)

# left: shared pool
box(ax, 0.3, 2.5, 5.1, 2.1, GREY_BG)
ax.text(2.85, 4.35, "共享待办池（谁都看得见）", fontproperties=BOLD,
        fontsize=12.5, color=INK, ha="center", va="center")
ax.text(2.85, 3.85, "豆包 K07/K32 — 15:31 已核对完，过期，未清",
        fontproperties=BOLD, fontsize=11.5, color=RED, ha="center", va="center")
ax.text(2.85, 3.4, "Vivix 任务 — 进行中", fontproperties=FONT,
        fontsize=11.5, color=MUTED, ha="center", va="center")
ax.text(2.85, 2.95, "即梦任务 — 进行中", fontproperties=FONT,
        fontsize=11.5, color=MUTED, ha="center", va="center")

ax.annotate("", xy=(6.35, 3.55), xytext=(5.55, 3.55),
            arrowprops=dict(arrowstyle="->", color=RED, lw=2))
ax.text(5.95, 3.85, "不分你我\n直接拿来用", fontproperties=FONT, fontsize=10.5,
        color=RED, ha="center", va="center")

# right: pet chat acts on the stale entry
box(ax, 6.6, 2.5, 5.1, 2.1, RED_BG, RED)
ax.text(9.15, 4.35, "宠物旁聊按过期待办动手", fontproperties=BOLD,
        fontsize=12.5, color=RED, ha="center", va="center")
ax.text(9.15, 3.75, "派了豆包 K07/K32", fontproperties=FONT, fontsize=12,
        color=INK, ha="center", va="center")
ax.text(9.15, 3.25, "其实 15:31 已经完成了", fontproperties=FONT,
        fontsize=12, color=INK, ha="center", va="center")

# bottom strip: paper numbers
box(ax, 0.3, 0.35, 11.4, 1.45, AMBER_BG, AMBER_EDGE)
ax.text(6, 1.48, "论文测的数：共享状态不划界，正常用也会污染",
        fontproperties=BOLD, fontsize=12.5, color=INK, ha="center", va="center")
ax.text(6, 0.95, "UCC 污染 57%–71% · MemLeak 泄漏 70%–100%",
        fontproperties=FONT, fontsize=12, color=INK, ha="center", va="center")
ax.text(6, 0.55, "DACS 隔离后，污染 28–57% → 0–14%",
        fontproperties=FONT, fontsize=12, color=INK, ha="center", va="center")

plt.tight_layout()
plt.savefig("/home/hatch/workspace/modelscope-drafts/images/case2-shared-context-lamp-v2.png",
            dpi=200, facecolor=BG, bbox_inches="tight")
print("saved")
