#!/usr/bin/env python3
"""Figure for part 2, section 4: cross-chat is not one problem but three.

A: optimal allocation — NP-hard except one-shot one-to-one (Hungarian O(n^3)).
B: guaranteeing correct dispatch — a rules/mechanism problem, cheap fixes work.
C: guessing the intent of vague human language — no guarantee possible.
"""
import sys
sys.path.insert(0, "/home/hatch/workspace/modelscope-drafts/images")
from fig_common import *

fig, ax = new_fig(12, 5.6)
title(ax, "串聊不是一个问题，是三个问题", 5.3)

cols = [
    (0.3, "A · 分得最优", GREY_BG, GREY,
     "一次一活一人：\n匈牙利算法 O(n³)，算得动\n\n排时间 / 组队 / 多任务：\nNP-hard，只能找近似解",
     "完美解算不动，够好就行"),
    (4.15, "B · 保证派对", GREEN_BG, GREEN,
     "所有权门控：1.4 毫秒一次，泄漏清零\n上下文隔离：污染 28–57% → 0–14%\n加 task_id：派错路修好了",
     "能解决，便宜有效"),
    (8.0, "C · 猜对人话", RED_BG, RED,
     "“扩展”有好几种理解\n正确答案在用户脑子里，\n不在句子里",
     "保证不了，只能压低概率\n错了能发现、能纠正"),
]
for x, head, bg, edge, body, verdict in cols:
    box(ax, x, 1.35, 3.55, 3.35, bg, edge)
    ax.text(x + 1.775, 4.42, head, fontproperties=BOLD, fontsize=13,
            color=INK, ha="center", va="center")
    ax.text(x + 1.775, 3.55, body, fontproperties=FONT, fontsize=11.5,
            color=INK, ha="center", va="center")
    ax.plot([x + 0.35, x + 3.2], [2.35, 2.35], color=edge, lw=1.2)
    ax.text(x + 1.775, 1.85, verdict, fontproperties=BOLD, fontsize=11.5,
            color=INK, ha="center", va="center")

ax.text(6, 0.85,
        "问题 A 的 NP-hard 结论来自 Gerkey 和 Mataric 2004（§5.2–§5.7）；",
        fontproperties=FONT, fontsize=11, color=MUTED, ha="center", va="center")
ax.text(6, 0.45,
        "问题 B 没有论文声称 NP-hard；问题 C 没有可判定性证明。",
        fontproperties=FONT, fontsize=11, color=MUTED, ha="center", va="center")

plt.tight_layout()
plt.savefig("/home/hatch/workspace/modelscope-drafts/images/nphard-split-lamp-v2.png",
            dpi=200, facecolor=BG, bbox_inches="tight")
print("saved")
