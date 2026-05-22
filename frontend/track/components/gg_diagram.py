import numpy as np
from matplotlib.patches import Circle


G = 9.80665


def _to_g(values, accel_unit: str):
    arr = np.asarray(values, dtype=float)
    unit = (accel_unit or "m/s²").lower()

    if unit in {"g", "g-force", "gforce"}:
        return arr
    return arr / G

def plot_gg_diagram(
    plot_ax,
    long_accel,
    lat_accel,
    accel_unit: str = "m/s²",
    color_values=None,
    colorbar_label: str = "Sample Index",
):

    ax_g = _to_g(long_accel, accel_unit)
    ay_g = _to_g(lat_accel, accel_unit)

    n = min(len(ax_g), len(ay_g))
    if color_values is not None:
        n = min(n, len(color_values))

    ax_g = ax_g[:n]
    ay_g = ay_g[:n]

    if color_values is None:
        raw_colors = np.arange(n)
    else:
        raw_colors = np.asarray(color_values, dtype=float)[:n]

    finite_mask = np.isfinite(ax_g) & np.isfinite(ay_g) & np.isfinite(raw_colors)
    ax_g = ax_g[finite_mask]
    ay_g = ay_g[finite_mask]
    colors = raw_colors[finite_mask]

    if len(ax_g) == 0:
        plot_ax.set_title("GG Diagram")
        plot_ax.text(0.5, 0.5, "No acceleration data", ha="center", va="center", transform=plot_ax.transAxes)
        plot_ax.grid(True)
        return

    max_abs = max(float(np.max(np.abs(ax_g))), float(np.max(np.abs(ay_g))), 0.5)
    lim = max_abs * 1.15
    circle_step = 0.5
    circle_limit = np.floor(lim / circle_step) * circle_step
    r = circle_step
    
    while r <= circle_limit + 1e-9:
        plot_ax.add_patch(Circle((0, 0), r, fill=False, linestyle="--", linewidth=0.8, alpha=0.25))
        plot_ax.text(r, 0, f"{r:.1f}g", fontsize=8, alpha=0.6, va="bottom", ha="left")
        r += circle_step

    plot_ax.axhline(0, color="gray", linewidth=1, alpha=0.7)
    plot_ax.axvline(0, color="gray", linewidth=1, alpha=0.7)

    sc = plot_ax.scatter(ay_g, ax_g, c=colors, cmap="viridis", s=18, alpha=0.75, edgecolors="none")
    cbar = plot_ax.figure.colorbar(sc, ax=plot_ax)
    cbar.set_label(colorbar_label)

    plot_ax.set_title("GG Diagram")
    plot_ax.set_xlabel("Lateral Acceleration ay [g]")
    plot_ax.set_ylabel("Longitudinal Acceleration ax [g]")
    plot_ax.set_xlim(-lim, lim)
    plot_ax.set_ylim(-lim, lim)
    plot_ax.set_aspect("equal", adjustable="box")
    plot_ax.grid(True, alpha=0.35)
