from __future__ import annotations

import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
import numpy as np

OUT_DIR = Path(__file__).resolve().parent
GIF_PATH = OUT_DIR / "exp2_convergencia_flujo.gif"
PNG_PATH = OUT_DIR / "exp2_convergencia_flujo.png"
JSON_PATH = OUT_DIR / "exp2_convergencia_flujo.json"

X0 = np.array([0.72, 0.18, 0.10], dtype=float)
P = np.array([0.15, 0.30, 0.55], dtype=float)
T = 4.0
H_LIST = [0.50, 0.25, 0.125, 0.0625]
VERTS = np.array([
    [0.0, 0.0],
    [1.0, 0.0],
    [0.5, np.sqrt(3.0) / 2.0],
], dtype=float)
COLORS = ["#d62728", "#1f77b4", "#2ca02c", "#9467bd"]


def project(x: np.ndarray) -> np.ndarray:
    return x @ VERTS


def flow(t: float) -> np.ndarray:
    e = np.exp(-t)
    return P + (X0 - P) * e


def euler_step(x: np.ndarray, h: float) -> np.ndarray:
    return (1.0 - h) * x + h * P


def l1(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.sum(np.abs(a - b)))


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


exact_t = np.linspace(0.0, T, 400)
exact_curve = np.array([flow(t) for t in exact_t])
trajectories: list[np.ndarray] = []
final_errors: list[float] = []
max_errors: list[float] = []
steps: list[int] = []
for h in H_LIST:
    m = int(round(T / h))
    steps.append(m)
    xs = [X0.copy()]
    x = X0.copy()
    max_err = 0.0
    for k in range(m):
        t = k * h
        max_err = max(max_err, l1(x, flow(t)))
        x = euler_step(x, h)
        xs.append(x.copy())
    max_err = max(max_err, l1(x, flow(T)))
    trajectories.append(np.array(xs))
    final_errors.append(l1(x, flow(T)))
    max_errors.append(max_err)

ratios = [final_errors[i] / final_errors[i + 1] for i in range(len(final_errors) - 1)]
summary = {
    "X0": X0.tolist(),
    "P": P.tolist(),
    "T": T,
    "h_list": H_LIST,
    "final_errors": final_errors,
    "max_errors": max_errors,
    "ratios": ratios,
    "exact_final": flow(T).tolist(),
}
JSON_PATH.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")

fig = plt.figure(figsize=(11.5, 5.2))
gs = fig.add_gridspec(1, 2, width_ratios=[1.20, 1.0], wspace=0.28)
ax = fig.add_subplot(gs[0, 0])
ax2 = fig.add_subplot(gs[0, 1])

p_proj = project(P)
exact_proj = np.array([project(x) for x in exact_curve])


def render(frame: int) -> None:
    ax.clear()
    ax2.clear()

    draw_simplex(ax)
    ax.set_title("Convergencia discreto-continuo", fontsize=11)
    ax.plot(exact_proj[:, 0], exact_proj[:, 1], color="#666666", lw=2.3, label="flujo exacto")

    for j in range(frame + 1):
        traj = trajectories[j]
        pts = np.array([project(x) for x in traj])
        color = COLORS[j]
        ax.plot(pts[:, 0], pts[:, 1], lw=1.8 if j < frame else 2.6, color=color, alpha=0.85 if j < frame else 1.0)
        ax.scatter(pts[0, 0], pts[0, 1], s=22, color=color, alpha=0.7)
        ax.scatter(pts[-1, 0], pts[-1, 1], s=64 if j == frame else 34, color=color, zorder=6)

    ax.scatter(p_proj[0], p_proj[1], marker="*", s=180, color="seagreen", zorder=8, label=r"$P$")
    ax.scatter(project(X0)[0], project(X0)[1], s=52, color="black", zorder=8, label=r"$X_0$")
    ax.legend(loc="upper right", frameon=False, fontsize=8)
    h = H_LIST[frame]
    ax.text(
        0.02,
        0.03,
        f"h = {h:.4f}\\nM = {steps[frame]}\\nfinal error = {final_errors[frame]:.6f}",
        transform=ax.transAxes,
        fontsize=9,
        ha="left",
        va="bottom",
        bbox=dict(boxstyle="round,pad=0.30", facecolor="white", alpha=0.88, edgecolor="#999999"),
    )

    idx = np.arange(frame + 1)
    hvals = np.array(H_LIST[: frame + 1])
    fe = np.array(final_errors[: frame + 1])
    me = np.array(max_errors[: frame + 1])
    ax2.loglog(hvals, fe, "o-", color="navy", lw=2.0, label="error final")
    ax2.loglog(hvals, me, "s--", color="darkorange", lw=2.0, label="error maximo")
    ax2.set_title("Refinamiento de la malla", fontsize=11)
    ax2.set_xlabel("Paso temporal h")
    ax2.set_ylabel("Error L1")
    ax2.grid(alpha=0.25, which="both")
    ax2.legend(frameon=False, fontsize=8)
    ax2.text(
        0.05,
        0.96,
        f"$X(T)$ exacto = ({flow(T)[0]:.4f}, {flow(T)[1]:.4f}, {flow(T)[2]:.4f})\\n"
        f"ratios = {[round(r, 3) for r in ratios[: max(0, frame)] ]}",
        transform=ax2.transAxes,
        ha="left",
        va="top",
        fontsize=9,
        bbox=dict(boxstyle="round,pad=0.30", facecolor="white", alpha=0.88, edgecolor="#999999"),
    )


render(len(H_LIST) - 1)
fig.tight_layout()
fig.savefig(PNG_PATH, dpi=180, bbox_inches="tight")
ani = FuncAnimation(fig, render, frames=len(H_LIST), interval=1200, blit=False, repeat=True)
ani.save(GIF_PATH, writer=PillowWriter(fps=1))
plt.close(fig)

print(json.dumps(summary, indent=2, ensure_ascii=False))