from __future__ import annotations

import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
import numpy as np

OUT_DIR = Path(__file__).resolve().parent
GIF_PATH = OUT_DIR / "exp1_trayectoria_discreta.gif"
PNG_PATH = OUT_DIR / "exp1_trayectoria_discreta.png"
JSON_PATH = OUT_DIR / "exp1_trayectoria_discreta.json"

X0 = np.array([0.72, 0.18, 0.10], dtype=float)
P = np.array([0.15, 0.30, 0.55], dtype=float)
EPS = 0.03
ALPHA = 0.35
R = 0.60
T = 40
VERTS = np.array([
    [0.0, 0.0],
    [1.0, 0.0],
    [0.5, np.sqrt(3.0) / 2.0],
], dtype=float)


def project(x: np.ndarray) -> np.ndarray:
    return x @ VERTS


def k_sm_3(eps: float) -> np.ndarray:
    k = np.full((3, 3), eps, dtype=float)
    np.fill_diagonal(k, 1.0 - 2.0 * eps)
    return k


def normalize(z: np.ndarray) -> np.ndarray:
    return z / np.sum(z)


def bayes_update(y: np.ndarray, l: np.ndarray) -> np.ndarray:
    return normalize(y * l)


def kl(p: np.ndarray, x: np.ndarray) -> float:
    return float(np.sum(p * np.log(p / x)))


def draw_simplex(ax: plt.Axes) -> None:
    verts = VERTS
    closed = np.vstack([verts, verts[0]])
    ax.plot(closed[:, 0], closed[:, 1], color="black", lw=1.7)
    labels = ["1", "2", "3"]
    offsets = [(0.0, -0.05), (0.03, -0.03), (0.0, 0.05)]
    for i, lab in enumerate(labels):
        ax.scatter(verts[i, 0], verts[i, 1], s=22, color="black", zorder=5)
        dx, dy = offsets[i]
        ax.text(verts[i, 0] + dx, verts[i, 1] + dy, lab, fontsize=9, ha="center", va="center")
    ax.set_xlim(-0.06, 1.06)
    ax.set_ylim(-0.07, np.sqrt(3.0) / 2.0 + 0.09)
    ax.set_aspect("equal", adjustable="box")
    ax.set_xticks([])
    ax.set_yticks([])


K = k_sm_3(EPS)
X_hist = [X0.copy()]
Y_hist: list[np.ndarray] = []
V_hist: list[np.ndarray] = []
KL_hist = [kl(P, X0)]
for _ in range(T):
    x = X_hist[-1]
    y = x @ K
    v = ALPHA * (np.log(P) - np.log(np.maximum(y, 1e-15)))
    v = np.clip(v, -R, R)
    l = np.exp(v)
    x_next = bayes_update(y, l)
    Y_hist.append(y)
    V_hist.append(v)
    X_hist.append(x_next)
    KL_hist.append(kl(P, x_next))

monotone = all(KL_hist[i + 1] <= KL_hist[i] + 1e-12 for i in range(T))

summary = {
    "X0": X0.tolist(),
    "P": P.tolist(),
    "eps": EPS,
    "alpha": ALPHA,
    "R": R,
    "T": T,
    "final_state": X_hist[-1].tolist(),
    "start_kl": KL_hist[0],
    "end_kl": KL_hist[-1],
    "monotone_kl": monotone,
    "min_coordinate": float(np.min(X_hist[-1])),
}
JSON_PATH.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")

fig = plt.figure(figsize=(11, 5))
gs = fig.add_gridspec(1, 2, width_ratios=[1.25, 1.0], wspace=0.28)
ax = fig.add_subplot(gs[0, 0])
ax2 = fig.add_subplot(gs[0, 1])

p_proj = project(P)


def render(frame: int) -> None:
    ax.clear()
    ax2.clear()

    draw_simplex(ax)
    ax.set_title("Trayectoria discreta admisible", fontsize=11)

    path = np.array([project(x) for x in X_hist[: frame + 1]])
    ax.plot(path[:, 0], path[:, 1], color="#1f77b4", lw=2.2, zorder=2)
    ax.scatter(path[-1, 0], path[-1, 1], s=72, color="crimson", zorder=6, label=r"$X_t$")
    ax.scatter(p_proj[0], p_proj[1], marker="*", s=180, color="seagreen", zorder=7, label=r"$P$")

    if frame < T:
        x_proj = project(X_hist[frame])
        y_proj = project(Y_hist[frame])
        x_next_proj = project(X_hist[frame + 1])
        ax.scatter(y_proj[0], y_proj[1], s=58, color="darkorange", zorder=6, label=r"$Y_t$")
        ax.annotate("", xy=y_proj, xytext=x_proj, arrowprops=dict(arrowstyle="->", color="darkorange", lw=1.8))
        ax.annotate("", xy=x_next_proj, xytext=y_proj, arrowprops=dict(arrowstyle="->", color="crimson", lw=1.5))

    ax.legend(loc="upper right", frameon=False, fontsize=8)
    ax.text(
        0.02,
        0.03,
        f"Paso {frame}/{T}\\nE_P(X_t) = {KL_hist[frame]:.6f}\\n\n"
        f"eps = {EPS:.3f}, alpha = {ALPHA:.2f}, R = {R:.2f}",
        transform=ax.transAxes,
        fontsize=9,
        ha="left",
        va="bottom",
        bbox=dict(boxstyle="round,pad=0.30", facecolor="white", alpha=0.88, edgecolor="#999999"),
    )

    steps = np.arange(T + 1)
    ax2.plot(steps, KL_hist, color="lightgray", lw=1.2, zorder=1)
    ax2.plot(steps[: frame + 1], KL_hist[: frame + 1], color="navy", lw=2.0, zorder=2)
    ax2.scatter([frame], [KL_hist[frame]], color="crimson", s=36, zorder=3)
    ax2.set_title("Descenso del potencial KL", fontsize=11)
    ax2.set_xlabel("Paso")
    ax2.set_ylabel(r"$E_P(X_t)$")
    ax2.grid(alpha=0.25)
    ax2.text(
        0.05,
        0.96,
        f"$E_P(X_0)$ = {KL_hist[0]:.6f}\\n$E_P(X_T)$ = {KL_hist[-1]:.6f}\\nmonotono = {monotone}",
        transform=ax2.transAxes,
        ha="left",
        va="top",
        fontsize=9,
        bbox=dict(boxstyle="round,pad=0.30", facecolor="white", alpha=0.88, edgecolor="#999999"),
    )

    ax2.set_xlim(0, T)
    ymin = min(KL_hist) - 0.03 * max(KL_hist)
    ymax = max(KL_hist) + 0.03 * max(KL_hist)
    ax2.set_ylim(ymin, ymax)


render(T)
fig.tight_layout()
fig.savefig(PNG_PATH, dpi=180, bbox_inches="tight")
ani = FuncAnimation(fig, render, frames=T + 1, interval=220, blit=False, repeat=True)
ani.save(GIF_PATH, writer=PillowWriter(fps=4))
plt.close(fig)

print(json.dumps(summary, indent=2, ensure_ascii=False))