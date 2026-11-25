#!/usr/bin/env python3
"""Figure for part 2, 6.2 / ablation: A2A buys correctness, MCP buys the fill.

Simulated trajectories, per 100 (gpu-queue-harness/ablation-log.txt, section B):
  NEITHER  idle 0.0, misroute 53.7
  A2A_ONLY idle 0.8, misroute 0.0
  MCP_ONLY idle 0.0, misroute 50.8
  BOTH     idle 0.0, misroute 0.0
Only BOTH reaches the origin (idle 0 AND misroutes 0).
"""
import sys
sys.path.insert(0, "/home/hatch/workspace/modelscope-drafts/images")
from fig_common import *

fig, ax = plt.subplots(figsize=(9.5, 6.2))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)

pts = [
    (53.7, 0.0, "两个都没有", GREY, (0, 14)),
    (0.0, 0.8, "只有 A2A", GREEN, (14, 0)),
    (50.8, 0.0, "只有 MCP", BLUE, (0, -26)),
    (0.0, 0.0, "两个都有", GREEN, (16, 2)),
]
for x, y, label, color, off in pts:
    marker = "*" if label == "两个都有" else "o"
    size = 420 if label == "两个都有" else 200
    ax.scatter([x], [y], s=size, marker=marker, color=color,
               edgecolors=INK, linewidths=1.5, zorder=5)
    ax.annotate(label, (x, y), textcoords="offset points", xytext=off,
                fontproperties=BOLD, fontsize=13, color=INK, zorder=6)

ax.set_xlim(-3, 60)
ax.set_ylim(-0.22, 1.05)
ax.set_xlabel("误派次数（每 100 条轨迹）", fontproperties=FONT, fontsize=12,
              color=INK)
ax.set_ylabel("空闲小时（每 100 条轨迹）", fontproperties=FONT, fontsize=12,
              color=INK)
ax.set_title("消融：A2A 管对错，MCP 管填位，只有一起上才到原点",
             fontproperties=BOLD, fontsize=15, color=INK, pad=14)
ax.spines[["top", "right"]].set_visible(False)
ax.spines[["left", "bottom"]].set_color(MUTED)
ax.tick_params(colors=INK)
ax.tick_params(labelsize=11)
for lbl in ax.get_xticklabels() + ax.get_yticklabels():
    lbl.set_fontproperties(FONT)
ax.axhline(0, color=GREY, lw=0.8)
ax.text(0.02, 0.04,
        "模拟信号弱：1000 条轨迹里只有 4 次错过信号，看方向，别当精确值。\n"
        "真实轨迹上三者打平，最多省 1.83 小时，10.13 小时卡在用户确认上。",
        transform=ax.transAxes, fontproperties=FONT, fontsize=10.5,
        color=MUTED, ha="left", va="bottom")

plt.tight_layout()
chart_title_rule(ax)
plt.savefig("/home/hatch/workspace/modelscope-drafts/images/ablation-scatter-lamp-v2.png",
            dpi=200, facecolor=BG, bbox_inches="tight")
print("saved")
