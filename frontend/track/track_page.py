"""
Track Page — Sayfa 3.
LTS/main.py → MainWindow'dan taşındı.
Pist haritası ve eğrilik haritasını gösteren sayfa widget'ı.
"""
import numpy as np
from PyQt6.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from frontend.track.components.track_map import plot_track
from frontend.track.components.curvature_heatmap import plot_curvature_heatmap


class TrackPage(QWidget):
    """Pist ve eğrilik haritalarını gösteren sayfa."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self._init_ui()

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
                x_raw     : np.ndarray  – Ham pist X koordinatları
                y_raw     : np.ndarray  – Ham pist Y koordinatları
                x_s       : np.ndarray  – Spline X koordinatları
                y_s       : np.ndarray  – Spline Y koordinatları
                kappa     : np.ndarray  – Eğrilik (curvature) değerleri
                apex_idx  : np.ndarray  – Viraj tepe noktası indeksleri
            Opsiyonel anahtarlar:
                s         : np.ndarray | None – Yol uzunluğu parametresi
                R         : np.ndarray | None – Dönüş yarıçapı
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
