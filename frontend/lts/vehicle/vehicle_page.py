"""
Vehicle Page — Araç parametrelerini gösteren sayfa.
Şimdilik placeholder — ileride gerçek verilerle doldurulacak.
"""
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt

from frontend.lts.vehicle.components.vehicle_overview import plot_vehicle_overview

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class VehiclePage(QWidget):
    """Araç parametreleri sayfası (placeholder)."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self._init_ui()

    def _init_ui(self):
        layout = QVBoxLayout(self)

        # Başlık
        title = QLabel("Vehicle Overview")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("font-size: 18px; font-weight: bold; padding: 12px;")
        layout.addWidget(title)

        # Placeholder grafik
        self.figure = Figure(constrained_layout=True)
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

        # İlk çizim
        ax = self.figure.add_subplot(111)
        plot_vehicle_overview(ax)
        self.canvas.draw()
