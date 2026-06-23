"""
Vehicle Page — Araç performans grafiklerini gösteren sayfa widget'ı.
Kendi sahte test verisini üretir ve init'te çizer.
"""
import numpy as np
from PyQt6.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from frontend.lts.vehicle.components.velocity_force_map import plot_velocity_force_map
from frontend.lts.vehicle.components.gg_diagram import plot_gg_diagram


class VehiclePage(QWidget):
    """Araç performans grafiklerini gösteren sayfa."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self._init_ui()

        # Sahte veri ile ilk çizim
        data = self._generate_fake_data()
        self.draw(data)

    def _init_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        # --- Velocity-Force Map ---
        self.vf_figure = Figure(constrained_layout=True)
        self.vf_canvas = FigureCanvas(self.vf_figure)
        layout.addWidget(self.vf_canvas)

        # --- GG Diagram ---
        self.gg_figure = Figure(constrained_layout=True)
        self.gg_canvas = FigureCanvas(self.gg_figure)
        layout.addWidget(self.gg_canvas)

    def draw(self, vehicle_data: dict):
        """
        Grafikleri verilen veri sözlüğüyle çizer.

        Parameters
        ----------
        vehicle_data : dict
            Gerekli anahtarlar:
                velocity_map, force_map, drag_values,
                total_grip, engine_force_at_v, drag_at_v, mass, velocity
        """
        velocity_map = vehicle_data["velocity_map"]
        force_map = vehicle_data["force_map"]
        drag_values = vehicle_data["drag_values"]

        total_grip = vehicle_data["total_grip"]
        engine_force_at_v = vehicle_data["engine_force_at_v"]
        drag_at_v = vehicle_data["drag_at_v"]
        mass = vehicle_data["mass"]
        velocity = vehicle_data["velocity"]

        # ---- Velocity-Force Map ----
        self.vf_figure.clear()
        ax1 = self.vf_figure.add_subplot(111)
        plot_velocity_force_map(ax1, velocity_map, force_map, drag_values)
        self.vf_canvas.draw()

        # ---- GG Diagram ----
        self.gg_figure.clear()
        ax2 = self.gg_figure.add_subplot(111)
        plot_gg_diagram(ax2, total_grip, engine_force_at_v, drag_at_v, mass, velocity)
        self.gg_canvas.draw()

    @staticmethod
    def _generate_fake_data() -> dict:
        """Geçici test verisi üretir."""
        np.random.seed(42)

        # --- Grafik 1: Velocity-Force Map verileri ---
        velocity_map = np.linspace(0, 60, 100)                  # 0-60 m/s
        force_map = 3000 * np.exp(-0.02 * velocity_map)         # Motor kuvveti (azalan)
        drag_values = 0.5 * 1.225 * 1.0 * 0.35 * velocity_map ** 2  # Drag = 0.5*rho*Cd*A*v^2

        # --- Grafik 2: GG Diagram verileri (random bir hız) ---
        v_random = np.random.choice(velocity_map[velocity_map > 5])  # 5 m/s üstü random hız
        total_grip = 8000.0          # Fmax(v) — toplam lastik kavrama (N)
        engine_force_at_v = float(3000 * np.exp(-0.02 * v_random))
        drag_at_v = float(0.5 * 1.225 * 1.0 * 0.35 * v_random ** 2)
        mass = 300.0                 # kg

        return {
            "velocity_map": velocity_map,
            "force_map": force_map,
            "drag_values": drag_values,
            "total_grip": total_grip,
            "engine_force_at_v": engine_force_at_v,
            "drag_at_v": drag_at_v,
            "mass": mass,
            "velocity": v_random,
        }
