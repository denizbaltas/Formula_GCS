import sys
import numpy as np

from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from plot_ui import Ui_MainWindow   
from plotting import plot_track, plot_curvature_heatmap


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("Formula Grand Station - Track Viewer")

        # -------------------------
        # TRACK MAP
        # -------------------------
        self.trackFigure = Figure(constrained_layout=True)
        self.trackCanvas = FigureCanvas(self.trackFigure)

        trackLayout = QVBoxLayout(self.ui.track_map_widget)
        trackLayout.setContentsMargins(0, 0, 0, 0)
        trackLayout.addWidget(self.trackCanvas)

        # -------------------------
        # CURVATURE MAP
        # -------------------------
        self.curvFigure = Figure(constrained_layout=True)
        self.curvCanvas = FigureCanvas(self.curvFigure)

        curvLayout = QVBoxLayout(self.ui.curvature_widget)
        curvLayout.setContentsMargins(0, 0, 0, 0)
        curvLayout.addWidget(self.curvCanvas)

        self.test_draw()

    def test_draw(self):

        x = np.linspace(0, 10, 300)
        y = np.sin(x)

        x_raw = x
        y_raw = y
        x_s = x
        y_s = y
        s = None
        kappa = np.abs(np.cos(x))
        R = None
        apex_idx = np.array([50, 150, 250])

        # ---- TRACK ----
        self.trackFigure.clear()
        ax1 = self.trackFigure.add_subplot(111)

        plot_track(ax1, x_raw, y_raw, x_s, y_s, s, kappa, R, apex_idx)
        self.trackCanvas.draw()

        # ---- CURVATURE ----
        self.curvFigure.clear()
        ax2 = self.curvFigure.add_subplot(111)

        plot_curvature_heatmap(ax2, x_s, y_s, kappa, apex_idx)
        self.curvCanvas.draw()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())   