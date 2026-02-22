"""
App Shell — Ana pencere ve sayfa navigasyonu.
QStackedWidget ile sayfalar arası geçiş sağlar.
"""
import sys
from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QStackedWidget,
)
from PyQt6.QtCore import Qt

from frontend.dashboard.dashboard_page import DashboardPage
from frontend.telemetry.telemetry_page import TelemetryPage
from frontend.track.track_page import TrackPage


class App(QMainWindow):
    """GCS Ana Penceresi — sayfa yönetimi ve navigasyon."""

    PAGE_NAMES = ["Dashboard", "Telemetry", "Track"]

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Formula GCS — Ground Control Station")
        self.resize(1200, 800)

        # --- Central widget ---
        central = QWidget()
        self.setCentralWidget(central)
        main_layout = QVBoxLayout(central)

        # --- Navigation bar ---
        nav_layout = QHBoxLayout()
        self._nav_buttons: list[QPushButton] = []

        for i, name in enumerate(self.PAGE_NAMES):
            btn = QPushButton(name)
            btn.setCheckable(True)
            btn.setMinimumHeight(36)
            btn.clicked.connect(lambda checked, idx=i: self._switch_page(idx))
            nav_layout.addWidget(btn)
            self._nav_buttons.append(btn)

        main_layout.addLayout(nav_layout)

        # --- Stacked pages ---
        self._stack = QStackedWidget()

        self.dashboard_page = DashboardPage()
        self.telemetry_page = TelemetryPage()
        self.track_page = TrackPage()

        self._stack.addWidget(self.dashboard_page)   # index 0
        self._stack.addWidget(self.telemetry_page)    # index 1
        self._stack.addWidget(self.track_page)        # index 2

        main_layout.addWidget(self._stack)

        # İlk sayfa
        self._switch_page(0)

    def _switch_page(self, index: int):
        """Sayfayı değiştir ve navigasyon butonlarını güncelle."""
        self._stack.setCurrentIndex(index)
        for i, btn in enumerate(self._nav_buttons):
            btn.setChecked(i == index)
