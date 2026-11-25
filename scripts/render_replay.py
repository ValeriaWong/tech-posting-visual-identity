#!/usr/bin/env python3
"""Figure for part 2, 6.2: real-event replay, OLD vs NEW rules.

Numbers from gpu-queue-harness/run-log.txt (21 events, 2026-11-17-11-25):
  misroute 3 -> 0, duplicate 1 -> 0, no_receipt 1 -> 0,
  stale_todo_conflict 1 -> 1, dispatches 6 -> 3.
v2.0 style: cold grey-white canvas, white plot area; old bars #C7CDD5
with #B3BAC5 edge, new bars tech blue #2563EB; old value labels #4A5158,
new value labels blue; axis #D6DBE2, grid #EDF0F4; the "派单总数" group
sits on a neutral #F2F4F7 band (no colour).
"""
import sys
sys.path.insert(0, "/home/hatch/workspace/modelscope-drafts/images")
from fig_common import *
import numpy as np

metrics = ["误派", "重复派单", "无回执派单", "过期待办冲突", "派单总数\n（重算口径）"]
old = [3, 1, 1, 1, 6]
new = [0, 0, 0, 1, 3]

fig, ax = plt.subplots(figsize=(10, 5.6))
fig.patch.set_facecolor(BG)
ax.set_facecolor(PLOT_BG)
x = np.arange(len(metrics))
w = 0.36
# neutral band behind the "派单总数" group (last group, x = 4)
ax.axvspan(3.5, 4.5, facecolor=PANEL_ALT, edgecolor="none", zorder=0)
b1 = ax.bar(x - w / 2, old, w, label="旧做法（§5 之前）", color=GREY_BAR,
            edgecolor=GREY_EDGE, linewidth=1, zorder=3)
b2 = ax.bar(x + w / 2, new, w, label="现在", color=BLUE, zorder=3)
for bars, c in ((b1, SECONDARY), (b2, BLUE)):
    for b in bars:
        ax.text(b.get_x() + b.get_width() / 2, b.get_height() + 0.15,
                str(int(b.get_height())), fontproperties=BOLD, fontsize=13,
                color=c, ha="center")
ax.set_xticks(x)
ax.set_xticklabels(metrics, fontproperties=FONT, fontsize=12, color=BODY)
ax.set_ylabel("次数", fontproperties=FONT, fontsize=12, color=ANNOT)
ax.set_title("真实事件回放：21 个事件，旧规矩 vs 新规矩",
             fontproperties=BOLD, fontsize=16, color=INK, pad=14)
ax.set_ylim(0, 7)
ax.legend(prop=FONT, fontsize=11, frameon=False, loc="upper left",
          labelcolor=ANNOT)
ax.spines[["top", "right"]].set_visible(False)
ax.spines[["left", "bottom"]].set_color(AXIS)
ax.tick_params(colors=ANNOT)
ax.tick_params(axis="y", labelsize=11)
for lbl in ax.get_yticklabels():
    lbl.set_fontproperties(FONT)
ax.yaxis.grid(True, color=GRID, linewidth=1)
ax.set_axisbelow(True)
ax.text(0, -0.22, "旧做法一列是实际发生的事故数（下限）；新规矩只有 3 天观察期（2026-11-22 20:32 → 11-25）。",
        transform=ax.transAxes, fontproperties=FONT, fontsize=10.5,
        color=FOOT, ha="left", va="top")

plt.tight_layout()
chart_title_rule(ax)
plt.savefig("/home/hatch/workspace/modelscope-drafts/images/replay-bars-mono-v1.png",
            dpi=200, facecolor=BG, bbox_inches="tight")
print("saved")
