"""
Track Page — Pist haritası ve eğrilik haritasını gösteren sayfa widget'ı.
Kendi sahte test verisini üretir ve init'te çizer.
"""
import numpy as np
from PyQt6.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from frontend.lts.track.components.track_map import plot_track
from frontend.lts.track.components.curvature_heatmap import plot_curvature_heatmap


class TrackPage(QWidget):
    """Pist ve eğrilik haritalarını gösteren sayfa."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self._init_ui()

        # Sahte veri ile ilk çizim
        data = self._generate_fake_data()
        self.draw(data)

    def _init_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        # --- Track Map ---
        self.track_figure = Figure(constrained_layout=True)
        self.track_canvas = FigureCanvas(self.track_figure)
        layout.addWidget(self.track_canvas)

        # --- Curvature Map ---
        self.curv_figure = Figure(constrained_layout=True)
        self.curv_canvas = FigureCanvas(self.curv_figure)
        layout.addWidget(self.curv_canvas)

    def draw(self, track_data: dict):
        """
        Grafikleri verilen veri sözlüğüyle çizer.

        Parameters
        ----------
        track_data : dict
            Gerekli anahtarlar:
                x_raw, y_raw, x_s, y_s, kappa, apex_idx
            Opsiyonel:
                s, R
        """
        x_raw    = track_data["x_raw"]
        y_raw    = track_data["y_raw"]
        x_s      = track_data["x_s"]
        y_s      = track_data["y_s"]
        kappa    = track_data["kappa"]
        apex_idx = track_data["apex_idx"]
        s        = track_data.get("s")
        R        = track_data.get("R")

        # ---- Track Map ----
        self.track_figure.clear()
        ax1 = self.track_figure.add_subplot(111)
        plot_track(ax1, x_raw, y_raw, x_s, y_s, s, kappa, R, apex_idx)
        self.track_canvas.draw()

        # ---- Curvature Map ----
        self.curv_figure.clear()
        ax2 = self.curv_figure.add_subplot(111)
        plot_curvature_heatmap(ax2, x_s, y_s, kappa, apex_idx)
        self.curv_canvas.draw()

    @staticmethod
    def _generate_fake_data() -> dict:
        """Geçici test verisi üretir."""
        np.random.seed(1)
        n_raw = 60
        t_raw = np.linspace(0, 2 * np.pi, n_raw, endpoint=False)
        radius = 100
        noise = 3.0
        x_raw = radius * np.cos(t_raw) + np.random.normal(0, noise, n_raw)
        y_raw = radius * np.sin(t_raw) + np.random.normal(0, noise, n_raw)

        n_spline = 300
        t_s = np.linspace(0, 2 * np.pi, n_spline, endpoint=False)
        x_s = radius * np.cos(t_s)
        y_s = radius * np.sin(t_s)

        kappa = np.full(n_spline, 1.0 / radius)
        s = np.linspace(0, 2 * np.pi * radius, n_spline)
        R = np.full(n_spline, radius)
        apex_idx = np.array([0, n_spline // 4, n_spline // 2, 3 * n_spline // 4])

        return {
            "x_raw": x_raw, "y_raw": y_raw,
            "x_s": x_s, "y_s": y_s,
            "kappa": kappa, "apex_idx": apex_idx,
            "s": s, "R": R,
        }
