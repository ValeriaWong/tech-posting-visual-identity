#!/usr/bin/env python3
"""Figure for part 2, section 4: cross-chat is not one problem but three.

A: optimal allocation — NP-hard except one-shot one-to-one (Hungarian O(n^3)).
B: guaranteeing correct dispatch — a rules/mechanism problem, cheap fixes work.
C: guessing the intent of vague human language — no guarantee possible.
v2.0 style: cold grey-white canvas. Column A is the plain column
(white + grey edge); column B is the emphasized / solution column
(pale blue fill + blue edge, 4px blue top bar on its header); column C
is the gap column (#E8EBF0 fill + 1px dashed grey edge). Header bands
are #F2F4F7; column separators #EDF0F4. The three key numbers
(O(n³), 1.4 毫秒， 0–14%) are blue — the only emphasized numbers here.
"""
import sys
sys.path.insert(0, "/home/hatch/workspace/modelscope-drafts/images")
from fig_common import *
from matplotlib.patches import Rectangle

fig, ax = new_fig(12, 5.6)
title(ax, "串聊不是一个问题，是三个问题", 5.3)

# (x, head, fill, edge, linestyle, body lines, verdict)
# body lines: plain strings, or ("seg", [(text, colour), ...]) for the
# lines whose key number is blue. Lines are drawn one by one, centered
# as a block on y=3.55 with 0.19 line spacing.
cols = [
    (0.3, "A · 分得最优", PANEL, PANEL_EDGE, "solid", [
        "一次一活一人：",
        ("seg", [("匈牙利算法 ", BODY), ("O(n³)", BLUE), ("，算得动", BODY)]),
        "",
        "排时间 / 组队 / 多任务：",
        "NP-hard，只能找近似解",
    ], "完美解算不动，够好就行"),
    (4.15, "B · 保证派对", BLUE_PALE, BLUE, "solid", [
        ("seg", [("所有权门控：", BODY), ("1.4 毫秒", BLUE), ("一次，泄漏清零", BODY)]),
        ("seg", [("上下文隔离：污染 28–57% → ", BODY), ("0–14%", BLUE)]),
        "加 task_id：派错路修好了",
    ], "能解决，便宜有效"),
    (8.0, "C · 猜对人话", SUNK, GREY_EDGE, "dashed", [
        "“扩展”有好几种理解",
        "正确答案在用户脑子里，",
        "不在句子里",
    ], "保证不了，只能压低概率\n错了能发现、能纠正"),
]

seg_jobs = []  # (cx, y, segments) — drawn after tight_layout, see below
for x, head, bg, edge, ls, lines, verdict in cols:
    box(ax, x, 1.35, 3.55, 3.35, bg, edge, linestyle=ls)
    # header band #F2F4F7 (box() pads by 0.06, so inset the call by that)
    box(ax, x + 0.10, 4.10, 3.35, 0.52, PANEL_ALT, PANEL_ALT, lw=1.0,
        radius=0.08)
    ax.text(x + 1.775, 4.42, head, fontproperties=BOLD, fontsize=13,
            color=INK, ha="center", va="center")
    n = len(lines)
    for i, line in enumerate(lines):
        y = 3.55 + ((n - 1) / 2 - i) * 0.19
        if line == "":
            continue
        if isinstance(line, tuple) and line[0] == "seg":
            seg_jobs.append((x + 1.775, y, line[1]))
        else:
            ax.text(x + 1.775, y, line, fontproperties=FONT, fontsize=11.5,
                    color=BODY, ha="center", va="center")
    ax.plot([x + 0.35, x + 3.2], [2.35, 2.35], color=GRID, lw=1)
    ax.text(x + 1.775, 1.85, verdict, fontproperties=BOLD, fontsize=11.5,
            color=INK, ha="center", va="center")

# emphasized column (B): 4px blue top bar on its header band
ax.add_patch(Rectangle((4.15 + 0.15, 4.655), 3.25, 0.025,
                       facecolor=BLUE, edgecolor="none", zorder=5))
# column separators between the cards
for sx in (4.0, 7.85):
    ax.plot([sx, sx], [1.35, 4.7], color=GRID, lw=1)

ax.text(6, 0.85,
        "问题 A 的 NP-hard 结论来自 Gerkey 和 Mataric 2004（§5.2–§5.7）；",
        fontproperties=FONT, fontsize=11, color=FOOT, ha="center", va="center")
ax.text(6, 0.45,
        "问题 B 没有论文声称 NP-hard；问题 C 没有可判定性证明。",
        fontproperties=FONT, fontsize=11, color=FOOT, ha="center", va="center")

plt.tight_layout()
for cx, y, segments in seg_jobs:
    seg_text(ax, cx, y, segments, size=11.5, bold=False)
plt.savefig("/home/hatch/workspace/modelscope-drafts/images/nphard-split-mono-v1.png",
            dpi=200, facecolor=BG, bbox_inches="tight")
print("saved")
