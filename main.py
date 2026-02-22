"""
Formula GCS — Giriş Noktası.
Uygulamayı başlatır, simulation mode ile test verisi yükler.
"""
import sys
import numpy as np
from PyQt6.QtWidgets import QApplication

from frontend.app import App


def _generate_test_track_data() -> dict:
    """
    Fake pist verisi üretir (LTS/main.py → test_draw'dan taşındı).
    Dairesel bir pist oluşturur: raw noktalar gürültülü, spline düzgün.
    """
    # --- Raw pist (gürültülü daire) ---
    n_raw = 60
    t_raw = np.linspace(0, 2 * np.pi, n_raw, endpoint=False)
    radius = 100
    noise = 3.0
    x_raw = radius * np.cos(t_raw) + np.random.normal(0, noise, n_raw)
    y_raw = radius * np.sin(t_raw) + np.random.normal(0, noise, n_raw)

    # --- Spline pist (düzgün daire) ---
    n_spline = 300
    t_s = np.linspace(0, 2 * np.pi, n_spline, endpoint=False)
    x_s = radius * np.cos(t_s)
    y_s = radius * np.sin(t_s)

    # --- Curvature (sabit, daire için 1/R) ---
    kappa = np.full(n_spline, 1.0 / radius)

    # --- Yol uzunluğu ---
    s = np.linspace(0, 2 * np.pi * radius, n_spline)

    # --- Yarıçap ---
    R = np.full(n_spline, radius)

    # --- Apex noktaları (4 adet, çeyrek dairelerde) ---
    apex_idx = np.array([0, n_spline // 4, n_spline // 2, 3 * n_spline // 4])

    return {
        "x_raw":    x_raw,
        "y_raw":    y_raw,
        "x_s":      x_s,
        "y_s":      y_s,
        "kappa":    kappa,
        "apex_idx": apex_idx,
        "s":        s,
        "R":        R,
    }


def main():
    app = QApplication(sys.argv)

    window = App()
    window.show()

    # Simulation: Track sayfasına test verisi yükle
    track_data = _generate_test_track_data()
    window.track_page.draw(track_data)

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
