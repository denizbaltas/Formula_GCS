import matplotlib.pyplot as plt
import numpy as np

def plot_curvature_heatmap(x_s, y_s, kappa, apex_idx):

    plt.figure(figsize=(8, 6))
    sc = plt.scatter(x_s, y_s, c = kappa, cmap = "viridis", s = 30)
    #draws points at x_s[i],y_s[i]
    #color for each point comes from kappa[i]
    #viridis colormap, size of marker is s

    plt.colorbar(sc, label = "Curvature Kappa") # adds the color scale legend on the side

    plt.scatter(x_s[apex_idx], y_s[apex_idx], color = "HotPink", s = 80, marker = "*", label = "Apex")
    plt.axis("equal")
    plt.grid(True)

    plt.xlabel("X [m]")
    plt.ylabel("Y [m]")

    plt.title("Curvature Map")
    plt.legend()
    plt.show()
