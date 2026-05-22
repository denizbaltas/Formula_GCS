import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

def plot_speed_heatmap(ax, x, y, speed):

    #x, y: track coordinates
    #speed: speed per segment/node

    norm = mcolors.Normalize(vmin=min(speed), vmax=max(speed))
    cmap = plt.cm.get_cmap("jet")  # blue -> red

    for i in range(len(x) - 1):
        ax.plot(
            [x[i], x[i+1]],
            [y[i], y[i+1]],
            color=cmap(norm(speed[i])),
            linewidth=3
        )

    ax.set_title("Speed Heatmap")
    ax.set_aspect("equal")
    ax.grid(True)