from PyQt6.QtWidgets import QWidget, QVBoxLayout, QComboBox
from track.track_page import TrackPage
from track.components.track_map import plot_track
from track.components.curvature_heatmap import plot_curvature_heatmap
# frontend.lts.  -->mainde çalıştırılacaksa bu path in eklenmesi lazım

import numpy as np

class LTSPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self._init_ui()
        self._init_data()

        # İlk çizim
        self._update_view(0)

    def _init_ui(self):
        layout = QVBoxLayout(self)

        # Dropdown 
        # mode ile kontrol sağlanıyor
        self.dropdown = QComboBox()
        self.dropdown.addItems([
            "Track Map",
            "Curvature Heatmap"
        ])
        layout.addWidget(self.dropdown)

        # Track Page 
        self.track_page = TrackPage()
        layout.addWidget(self.track_page)

        # Event
        self.dropdown.currentIndexChanged.connect(self._update_view)

    def _init_data(self):
        """Fake map dataları"""
        self.data = self._generate_fake_data(seed=1)

    def _update_view(self, mode: int):
        """Dropdown değişince çalışır"""
        #not:track page dokunmadan çizim yapacak şekilde tasarlandı
        self.track_page.draw(self.data)

        # görünürlük kontrolü yapar
        if mode == 0:
            # Track Map göster
            self.track_page.track_canvas.show()
            self.track_page.curv_canvas.hide()
        else:
            # Curvature göster
            self.track_page.track_canvas.hide()
            self.track_page.curv_canvas.show()

    def _generate_fake_data(self, seed=0):
        """Geçici veri üretici"""
        np.random.seed(seed)

        t = np.linspace(0, 2*np.pi, 200)

        x_raw = np.cos(t) + 0.1*np.random.randn(len(t))
        y_raw = np.sin(t) + 0.1*np.random.randn(len(t))

        x_s = np.cos(t)
        y_s = np.sin(t)

        kappa = np.abs(np.sin(2*t))
        apex_idx = np.array([50, 100, 150])

        return {
            "x_raw": x_raw,
            "y_raw": y_raw,
            "x_s": x_s,
            "y_s": y_s,
            "kappa": kappa,
            "apex_idx": apex_idx,
            "s": t,
            "R": 1 / (kappa + 0.1)
        }
