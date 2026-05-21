"""
Acceleration Profile component.
"""
import numpy as np


def plot_acceleration_profile(ax, s, long_accel):
    """
    Acceleration Profile çizimi:
    - s: Yol uzunluğu / konum parametresi (X ekseni)
    - long_accel: Boyuna ivme [m/s^2] veya [G] (Y ekseni)
    """
    # Sıfır (Nötr) çizgisini referans olarak çizelim
    ax.axhline(0, color='gray', linestyle='--', linewidth=1, alpha=0.7)
    ax.plot(s, long_accel, color='dimgray', linewidth=1.5, alpha=0.5)
    
    # Gaz bölgeleri (Yeşil)
    ax.fill_between(s, long_accel, 0, where=(long_accel >= 0), 
                    color='green', alpha=0.4, interpolate=True, label='Throttle (Gas)')
    
    # Fren bölgeleri (Kırmızı)
    ax.fill_between(s, long_accel, 0, where=(long_accel < 0), 
                    color='red', alpha=0.4, interpolate=True, label='Brake (Negative Accel)')

    ax.set_title("Acceleration Profile")
    ax.set_xlabel("Distance [s]")  # s -> zaman/konum 
    ax.set_ylabel("Longitudinal Acceleration [m/s²]")
    ax.grid(True)
    ax.legend(loc='upper right')
