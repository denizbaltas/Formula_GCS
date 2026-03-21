"""
GG-Diagram component.
Seçilen bir hız için aracın GG diyagramını çizer (lastik limitleri).

Inputlar:
    total_grip    → toplam lastik kavrama kuvveti Fmax(v) (N) (float)
    engine_force  → motor kuvveti (N)                        (float)
    drag          → aerodinamik sürükleme kuvveti (N)        (float)
    mass          → araç kütlesi (kg)                        (float)
    velocity      → seçilen hız (m/s)                        (float)
"""


def plot_gg_diagram(ax, total_grip, engine_force, drag, mass, velocity):
    """
    GG diyagramı çizimi — Ax vs Ay.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Çizim yapılacak eksen.
    total_grip : float
        Toplam lastik kavrama kuvveti Fmax(v) (N).
    engine_force : float
        Motor kuvveti (N).
    drag : float
        Aerodinamik sürükleme kuvveti (N).
    mass : float
        Araç kütlesi (kg).
    velocity : float
        Seçilen hız (m/s).
    """
    pass
