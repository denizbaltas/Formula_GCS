import numpy as np
import matplotlib.pyplot as plt

def plot_track(ax, x_raw, y_raw, x_s, y_s, s, kappa, R, apex_idx):
    """
    Track Map (Top View) çizimi:
    - x_raw, y_raw -> ham pist (scatter)
    - x_s, y_s     -> spline edilmiþ pist (line)
    - apex_idx     -> viraj tepe noktalarý (marker)
    """


    #Ham pist (scatter)
    plt.scatter(x_raw, y_raw, color='blue', s=40, label='Raw Track')

    #Spline edilmis pist (line)
    ax.plot(x_s, y_s, color='HotPink', linewidth=2, label='Spline Track')

    #Apex noktalari
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
    ax.axis('equal')     # Pist olcegi bozulmasin
    ax.grid(True)
    ax.legend()




def plot_curvature_heatmap(ax, x_s, y_s, kappa, apex_idx):

    sc = ax.scatter(x_s, y_s, c = kappa, cmap = "viridis", s = 30)
    #draws points at x_s[i],y_s[i]
    #color for each point comes from kappa[i]
    #viridis colormap, size of marker is s

    ax.figure.colorbar(sc, label = "Curvature Kappa") # adds the color scale legend on the side

    ax.scatter(x_s[apex_idx], y_s[apex_idx], color = "HotPink", s = 80, marker = "*", label = "Apex")

    ax.axis("equal")
    ax.grid(True)
    ax.set_xlabel("X [m]")
    ax.set_ylabel("Y [m]")
    ax.set_title("Curvature Map")
    ax.legend()