#!/usr/bin/env python3
"""Figure for part 1, case 3: a capability signal misheard as a task list.

Left: capability signals (statements about state). Right: what the agent
hears — an order to dispatch everything pending. Bottom: accident 2's echo.
"""
import sys
sys.path.insert(0, "/home/hatch/workspace/modelscope-drafts/images")
from fig_common import *

fig, ax = new_fig(12, 4.8)
title(ax, "情况 3：“能做”被听成“去做”", 4.5)

# left: capability signal
box(ax, 0.3, 2.4, 5.0, 1.6, GREEN_BG, GREEN)
ax.text(2.8, 3.75, "能力信号（说的是状态）", fontproperties=BOLD,
        fontsize=12.5, color=GREEN_DARK, ha="center", va="center")
ax.text(2.8, 3.25, "“扩展浏览器能用了”\n“GPU 空出来了” / “额度刷新了”",
        fontproperties=FONT, fontsize=11.5, color=INK, ha="center", va="center")

ax.annotate("", xy=(6.55, 3.2), xytext=(5.45, 3.2),
            arrowprops=dict(arrowstyle="->", color=RED, lw=2))
ax.text(6.0, 3.5, "听成", fontproperties=BOLD, fontsize=12,
        color=RED, ha="center")

# right: task list
box(ax, 6.8, 2.4, 4.9, 1.6, RED_BG, RED)
ax.text(9.25, 3.75, "任务清单（以为要动手）", fontproperties=BOLD,
        fontsize=12.5, color=RED, ha="center", va="center")
ax.text(9.25, 3.25, "眼前所有待办\n全派一遍", fontproperties=FONT,
        fontsize=11.5, color=INK, ha="center", va="center")

# bottom strip: accident 2 echo
box(ax, 0.3, 0.35, 11.4, 1.25, AMBER_BG, AMBER_EDGE)
ax.text(6, 1.28, "事故 2 也是这个影子", fontproperties=BOLD, fontsize=12.5,
        color=INK, ha="center", va="center")
ax.text(6, 0.78, "派了没回音 → 以为“没派成” → 又派一次，差点双烧额度",
        fontproperties=FONT, fontsize=12, color=INK, ha="center", va="center")

plt.tight_layout()
plt.savefig("/home/hatch/workspace/modelscope-drafts/images/case3-signal-lamp-v2.png",
            dpi=200, facecolor=BG, bbox_inches="tight")
print("saved")
