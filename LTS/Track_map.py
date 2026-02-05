import numpy as np
import matplotlib.pyplot as plt

def plot_track(x_raw, y_raw, x_s, y_s, s, kappa, R, apex_idx):
    """
    Track Map (Top View) çizimi:
    - x_raw, y_raw -> ham pist (scatter)
    - x_s, y_s     -> spline edilmiş pist (line)
    - apex_idx     -> viraj tepe noktaları (marker)
    """

    plt.figure(figsize=(8, 6))

    #Ham pist (scatter)
    plt.scatter(x_raw, y_raw, color='blue', s=40, label='Raw Track')

    #Spline edilmiş pist (line)
    plt.plot(x_s, y_s, color='HotPink', linewidth=2, label='Spline Track')

    #Apex noktaları
    plt.scatter(
        x_s[apex_idx],
        y_s[apex_idx],
        color='red',
        s=120,
        marker='*',
        label='Apex Points'
    )

    plt.title("Track Map (Top View)")
    plt.xlabel("X [m]")
    plt.ylabel("Y [m]")
    plt.axis('equal')     # Pist ölçeği bozulmasın
    plt.grid(True)
    plt.legend()

    plt.show()
