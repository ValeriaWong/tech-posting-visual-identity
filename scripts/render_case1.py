#!/usr/bin/env python3
"""Figure for part 1, case 1: no task id, so the agent has to guess from words.

Flow: user says one vague word ("扩展", no task_id) -> agent guesses from
semantics -> dispatches the wrong owner's job (Douyin K07/K32, little-red's).
Bottom strip shows the contrast: with an id, check owner first.
"""
import sys
sys.path.insert(0, "/home/hatch/workspace/modelscope-drafts/images")
from fig_common import *

fig, ax = new_fig(12, 4.8)
title(ax, "情况 1：没有编号，只能靠文字猜", 4.5)

# three boxes
box(ax, 0.3, 2.5, 3.3, 1.45, GREY_BG)
ax.text(1.95, 3.72, "用户只说一句话", fontproperties=BOLD, fontsize=12.5,
        color=INK, ha="center", va="center")
ax.text(1.95, 3.2, "“扩展”\n没有 task_id（任务编号）", fontproperties=FONT,
        fontsize=11.5, color=INK, ha="center", va="center")

box(ax, 4.6, 2.5, 3.3, 1.45, AMBER_BG, AMBER_EDGE)
ax.text(6.25, 3.72, "智能体靠语义猜", fontproperties=BOLD, fontsize=12.5,
        color=INK, ha="center", va="center")
ax.text(6.25, 3.2, "“扩展”＝派所有待办？", fontproperties=FONT,
        fontsize=11.5, color=INK, ha="center", va="center")

box(ax, 8.9, 2.5, 2.8, 1.45, RED_BG, RED)
ax.text(10.3, 3.72, "派错了", fontproperties=BOLD, fontsize=12.5,
        color=RED, ha="center", va="center")
ax.text(10.3, 3.2, "豆包 K07/K32\n（小红帽旁聊的活）", fontproperties=FONT,
        fontsize=11.5, color=INK, ha="center", va="center")

ax.annotate("", xy=(4.45, 3.22), xytext=(3.75, 3.22),
            arrowprops=dict(arrowstyle="->", color=MUTED, lw=2))
ax.text(4.1, 3.5, "没有编号", fontproperties=FONT, fontsize=10.5,
        color=MUTED, ha="center")
ax.annotate("", xy=(8.75, 3.22), xytext=(8.05, 3.22),
            arrowprops=dict(arrowstyle="->", color=MUTED, lw=2))
ax.text(8.4, 3.5, "猜", fontproperties=FONT, fontsize=10.5,
        color=MUTED, ha="center")

# bottom contrast strip
box(ax, 0.3, 0.35, 11.4, 1.25, GREEN_BG, GREEN)
ax.text(6, 1.28, "有编号的样子", fontproperties=BOLD, fontsize=12.5,
        color=GREEN_DARK, ha="center", va="center")
ax.text(6, 0.78, "派 K07 → 先查 owner → 是小红帽的，不派，转交",
        fontproperties=FONT, fontsize=12, color=INK, ha="center", va="center")

plt.tight_layout()
plt.savefig("/home/hatch/workspace/modelscope-drafts/images/case1-guess-lamp-v2.png",
            dpi=200, facecolor=BG, bbox_inches="tight")
print("saved")
