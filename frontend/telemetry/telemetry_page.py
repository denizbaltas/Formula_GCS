"""
Telemetry Page — Sayfa 2.
Şimdilik boş iskelet. İleride canlı grafik ve veri tablosu eklenecek.
"""
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt


class TelemetryPage(QWidget):
    """Detaylı telemetri verisi sayfası (iskelet)."""

    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)

        placeholder = QLabel("Telemetry — Yakında")
        placeholder.setAlignment(Qt.AlignmentFlag.AlignCenter)
        placeholder.setStyleSheet("font-size: 24px; color: #888;")
        layout.addWidget(placeholder)
