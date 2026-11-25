#!/usr/bin/env python3
"""Figure for part 2, 6.2: simulated trajectories, OLD vs NEW vs ALT.

Numbers from gpu-queue-harness/sim-log.txt (1000 trajectories, seed 20261125),
per 100 trajectories:
  misroute 53.7 / 0.0 / 0.0, duplicate 2.7 / 0.0 / 0.0,
  stale_conflict 25.1 / 3.4 / 0.0, correct 13.1 / 7.3 / 7.3.
v2.0 style: cold grey-white canvas, white plot area; OLD bars #C7CDD5
with #B3BAC5 edge, NEW bars tech blue #2563EB, ALT bars light blue
#A5C4F7 (fill only — its value labels stay grey, light blue is never
used for small text); OLD/ALT labels #4A5158, NEW labels blue.
"""
import sys
sys.path.insert(0, "/home/hatch/workspace/modelscope-drafts/images")
from fig_common import *
import numpy as np

metrics = ["误派", "重复派单", "过期待办冲突", "正确派单"]
old = [53.7, 2.7, 25.1, 13.1]
new = [0.0, 0.0, 3.4, 7.3]
alt = [0.0, 0.0, 0.0, 7.3]

fig, ax = plt.subplots(figsize=(11, 5.8))
fig.patch.set_facecolor(BG)
ax.set_facecolor(PLOT_BG)
x = np.arange(len(metrics))
w = 0.26
b1 = ax.bar(x - w, old, w, label="OLD（§5 之前）", color=GREY_BAR,
            edgecolor=GREY_EDGE, linewidth=1, zorder=3)
b2 = ax.bar(x, new, w, label="NEW（现在）", color=BLUE, zorder=3)
b3 = ax.bar(x + w, alt, w, label="ALT（NEW + 待办状态谁说了算）",
            color=BLUE_LIGHT, zorder=3)
for bars, c in ((b1, SECONDARY), (b2, BLUE), (b3, SECONDARY)):
    for b in bars:
        h = b.get_height()
        ax.text(b.get_x() + b.get_width() / 2, h + 1.2,
                f"{h:.1f}", fontproperties=BOLD, fontsize=12,
                color=c, ha="center")
ax.set_xticks(x)
ax.set_xticklabels(metrics, fontproperties=FONT, fontsize=12, color=BODY)
ax.set_ylabel("次数（每 100 条轨迹）", fontproperties=FONT, fontsize=12, color=ANNOT)
ax.set_title("模拟轨迹：1000 条假轨迹，三套规矩",
             fontproperties=BOLD, fontsize=16, color=INK, pad=14)
ax.set_ylim(0, 62)
ax.legend(prop=FONT, fontsize=11, frameon=False, loc="upper right",
          labelcolor=ANNOT)
ax.spines[["top", "right"]].set_visible(False)
ax.spines[["left", "bottom"]].set_color(AXIS)
ax.tick_params(colors=ANNOT)
ax.tick_params(axis="y", labelsize=11)
for lbl in ax.get_yticklabels():
    lbl.set_fontproperties(FONT)
ax.yaxis.grid(True, color=GRID, linewidth=1)
ax.set_axisbelow(True)
ax.text(0, -0.20,
        "绝对数是模型假设（生成器参数），相对变化才是结论；正确派单 13.1 → 7.3 是规矩的代价。",
        transform=ax.transAxes, fontproperties=FONT, fontsize=10.5,
        color=FOOT, ha="left", va="top")

plt.tight_layout()
chart_title_rule(ax)
plt.savefig("/home/hatch/workspace/modelscope-drafts/images/sim-bars-mono-v1.png",
            dpi=200, facecolor=BG, bbox_inches="tight")
print("saved")
