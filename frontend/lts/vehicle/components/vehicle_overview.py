"""
Vehicle Overview component.
Araç parametrelerini gösteren placeholder grafik.
İleride gerçek verilerle doldurulacak.
"""


def plot_vehicle_overview(ax):
    """
    Placeholder çizim — araç verileri eklendiğinde güncellenecek.
    """
    ax.text(
        0.5, 0.5,
        "Vehicle data will be displayed here",
        ha="center", va="center",
        fontsize=14, color="gray",
        transform=ax.transAxes,
    )
    ax.set_title("Vehicle Overview (placeholder)")
    ax.set_xticks([])
    ax.set_yticks([])
