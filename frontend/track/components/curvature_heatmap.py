"""
Curvature Heatmap component.
LTS/plotting.py → plot_curvature_heatmap fonksiyonundan taşındı.
Eğrilik (curvature) haritasını çizer.
"""
import numpy as np


def plot_curvature_heatmap(ax, x_s, y_s, kappa, apex_idx):
    """
    Curvature haritası çizimi:
    - Spline noktaları kappa değerine göre renklenir
    - Apex noktaları işaretlenir
    """

    sc = ax.scatter(x_s, y_s, c=kappa, cmap="viridis", s=30)
    ax.figure.colorbar(sc, label="Curvature Kappa")

    ax.scatter(
        x_s[apex_idx],
        y_s[apex_idx],
        color="HotPink",
        s=80,
        marker="*",
        label="Apex"
    )

    ax.axis("equal")
    ax.grid(True)
    ax.set_xlabel("X [m]")
    ax.set_ylabel("Y [m]")
    ax.set_title("Curvature Map")
    ax.legend()
