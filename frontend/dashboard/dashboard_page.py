"""
Dashboard Page — Sayfa 1.
Şimdilik boş iskelet. İleride hız, batarya vb. göstergeler eklenecek.
"""
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt


class DashboardPage(QWidget):
    """Ana gösterge paneli sayfası (iskelet)."""

    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)

        placeholder = QLabel("Dashboard — Yakında")
        placeholder.setAlignment(Qt.AlignmentFlag.AlignCenter)
        placeholder.setStyleSheet("font-size: 24px; color: #888;")
        layout.addWidget(placeholder)
