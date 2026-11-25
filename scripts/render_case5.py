#!/usr/bin/env python3
"""Figure for part 1, case 5: an unnamed stop hits the wrong thing.

Panel A: audit and production share one todo list; "stop the audit" with no
target named cancels production too. Panel B: no exit condition — 47 rounds
until a $180 bill trips the alarm. Bottom: the fix.
"""
import sys
sys.path.insert(0, "/home/hatch/workspace/modelscope-drafts/images")
from fig_common import *

fig, ax = new_fig(12, 5.4)
title(ax, "情况 5：停的指令没点名，停错了东西", 5.1)

# panel A
box(ax, 0.3, 1.7, 5.6, 2.9, RED_BG, RED)
ax.text(3.1, 4.32, "停不点名：下令“停审改”", fontproperties=BOLD,
        fontsize=12.5, color=RED, ha="center", va="center")
ax.text(3.1, 3.85, "一张待办清单里混着两样东西：", fontproperties=FONT,
        fontsize=11.5, color=INK, ha="center", va="center")
ax.text(3.1, 3.4, "审改（想停的）", fontproperties=FONT, fontsize=11.5,
        color=INK, ha="center", va="center")
ax.plot([1.3, 4.9], [3.4, 3.4], color=RED, lw=1.6)
ax.text(3.1, 2.95, "生产采集（还要继续的）", fontproperties=FONT,
        fontsize=11.5, color=INK, ha="center", va="center")
ax.plot([1.3, 4.9], [2.95, 2.95], color=RED, lw=1.6)
ax.text(3.1, 2.4, "结果：生产采集也被取消了", fontproperties=BOLD,
        fontsize=12, color=RED, ha="center", va="center")

# panel B
box(ax, 6.1, 1.7, 5.6, 2.9, AMBER_BG, AMBER_EDGE)
ax.text(8.9, 4.32, "没退出条件：一直转", fontproperties=BOLD,
        fontsize=12.5, color=INK, ha="center", va="center")
ax.text(8.9, 3.85, "审改 → 再审改 → 再审改 …", fontproperties=FONT,
        fontsize=12, color=INK, ha="center", va="center")
ax.text(8.9, 3.3, "47 轮之后，账单到了 $180", fontproperties=BOLD,
        fontsize=12.5, color=RED, ha="center", va="center")
ax.text(8.9, 2.8, "才触发警报", fontproperties=FONT, fontsize=11.5,
        color=INK, ha="center", va="center")
ax.text(8.9, 2.3, "第 15 轮时上下文已塞满过期中间结果", fontproperties=FONT,
        fontsize=10.5, color=MUTED, ha="center", va="center")

# bottom strip: the fix
box(ax, 0.3, 0.35, 11.4, 1.0, GREEN_BG, GREEN)
ax.text(6, 0.85, "修法：停必须点名；审改和生产分开两张清单；轮数上限（比如 5 轮就停）。",
        fontproperties=BOLD, fontsize=12, color=GREEN_DARK, ha="center", va="center")

plt.tight_layout()
plt.savefig("/home/hatch/workspace/modelscope-drafts/images/case5-stop-lamp-v2.png",
            dpi=200, facecolor=BG, bbox_inches="tight")
print("saved")
