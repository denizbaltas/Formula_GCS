"""
LTS Page — Ana LTS sayfası.
Alt sayfalarda bulunan sub-paketleri (track, vehicle, ...) otomatik keşfeder
ve dropdown ile aralarında geçiş sağlar.

Yeni sayfa eklemek için:
  1. frontend/lts/ altına yeni bir klasör oluştur (ör: tire/)
  2. __init__.py dosyasına PAGE_NAME ve PageWidget ekle
  3. Otomatik olarak dropdown'a eklenir
"""
import importlib
import pkgutil
import os

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QComboBox, QStackedWidget


class LTSPage(QWidget):
    """Dropdown ile alt sayfalar arasında geçiş sağlayan LTS ana sayfası."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self._pages = self._discover_pages()
        self._init_ui()

    def _discover_pages(self) -> list[tuple[str, type]]:
        """
        frontend/lts/ altındaki sub-paketleri tarar.
        Her sub-paket __init__.py'de PAGE_NAME (str) ve PageWidget (QWidget) export etmeli.
        """
        pages = []
        package_dir = os.path.dirname(__file__)

        for finder, name, ispkg in pkgutil.iter_modules([package_dir]):
            if not ispkg:
                continue
            try:
                mod = importlib.import_module(f"frontend.lts.{name}")
                if hasattr(mod, "PAGE_NAME") and hasattr(mod, "PageWidget"):
                    pages.append((mod.PAGE_NAME, mod.PageWidget))
            except ImportError as e:
                print(f"[LTSPage] '{name}' yüklenemedi: {e}")

        return pages

    def _init_ui(self):
        layout = QVBoxLayout(self)

        # --- Dropdown ---
        self.dropdown = QComboBox()
        for page_name, _ in self._pages:
            self.dropdown.addItem(page_name)
        layout.addWidget(self.dropdown)

        # --- Stacked pages ---
        self._stack = QStackedWidget()
        for _, PageClass in self._pages:
            self._stack.addWidget(PageClass())
        layout.addWidget(self._stack)

        # --- Event ---
        self.dropdown.currentIndexChanged.connect(self._stack.setCurrentIndex)

        # İlk sayfa
        if self._pages:
            self._stack.setCurrentIndex(0)
