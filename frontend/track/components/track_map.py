"""
Track Map component.
LTS/plotting.py → plot_track fonksiyonundan taşındı.
Pist haritasını (top view) çizer.
"""
import numpy as np


def plot_track(ax, x_raw, y_raw, x_s, y_s, s, kappa, R, apex_idx):
    """
    Track Map (Top View) çizimi:
    - x_raw, y_raw -> ham pist (scatter)
    - x_s, y_s     -> spline edilmiş pist (line)
    - apex_idx     -> viraj tepe noktaları (marker)
    """

    # Ham pist (ince çizgi + scatter)
    ax.plot(x_raw, y_raw, color='blue', linewidth=0.8, linestyle='--', label='Raw Track')
    ax.scatter(x_raw, y_raw, color='blue', s=15, zorder=3)

    # Spline edilmiş pist (line)
    ax.plot(x_s, y_s, color='HotPink', linewidth=2, label='Spline Track')

    # Apex noktaları
    ax.scatter(
        x_s[apex_idx],
        y_s[apex_idx],
        color='red',
        s=120,
        marker='*',
        label='Apex Points'
    )

    ax.set_title("Track Map (Top View)")
    ax.set_xlabel("X [m]")
    ax.set_ylabel("Y [m]")
    ax.axis('equal')
    ax.grid(True)
    ax.legend()
