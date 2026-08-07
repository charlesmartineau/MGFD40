import numpy as np
import matplotlib.pyplot as plt

n = 6
panels = {}

panels["Plain OLS"] = np.eye(n) * 0.75

rng = np.random.default_rng(0)
hc = np.zeros((n, n))
np.fill_diagonal(hc, [0.35, 0.9, 0.2, 0.6, 1.0, 0.3])
panels["White / HC"] = hc

hac = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        d = abs(i - j)
        hac[i, j] = {0: 0.8, 1: 0.45, 2: 0.2}.get(d, 0.0)
panels["Newey-West"] = hac

cl = np.zeros((n, n))
for blk in (range(0, 3), range(3, 6)):
    for i in blk:
        for j in blk:
            cl[i, j] = 0.8 if i == j else 0.5
panels["Clustered"] = cl

subtitles = [
    "equal variance\nno correlation",
    "variance varies\nno correlation",
    "variance varies\nnearby periods link",
    "variance varies\nsame group links",
]

fig, axes = plt.subplots(1, 4, figsize=(11, 3.4))
for ax, (name, M), sub in zip(axes, panels.items(), subtitles):
    ax.imshow(M, cmap="BuGn", vmin=0, vmax=1)
    ax.set_xticks(np.arange(-0.5, n, 1), minor=True)
    ax.set_yticks(np.arange(-0.5, n, 1), minor=True)
    ax.grid(which="minor", color="0.85", linewidth=0.5)
    ax.tick_params(which="both", length=0, labelbottom=False, labelleft=False)
    ax.set_title(name, fontsize=11)
    ax.set_xlabel(sub, fontsize=9, color="0.35")
    for s in ax.spines.values():
        s.set_visible(False)
fig.tight_layout()
plt.show()
