"""
Velocity-Force Map component.
Hız-Kuvvet haritasını çizer: Engine Force(v) ve Drag(v) eğrileri.

Inputlar:
    velocity_map  → hız dizisi (m/s)        (np.ndarray)
    force_map     → motor tekerlek kuvveti (N) (np.ndarray)
    drag_values   → aerodinamik sürükleme (N)  (np.ndarray)
"""


def plot_velocity_force_map(ax, velocity_map, force_map, drag_values):
    """
    Velocity-Force haritası çizimi.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Çizim yapılacak eksen.
    velocity_map : np.ndarray
        Hız değerleri (m/s).
    force_map : np.ndarray
        Her hızda motorun verebildiği maksimum tekerlek kuvveti (N).
    drag_values : np.ndarray
        Her hız için aerodinamik sürükleme kuvveti (N).
    """
    pass
