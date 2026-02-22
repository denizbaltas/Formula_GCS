"""
Simulation veri kaynağı.
Gerçek donanım olmadan UI'ı test etmek için fake telemetri verisi üretir.
"""
import struct
import math
import time

from .base_source import DataSource


class SimulationSource(DataSource):
    """Sahte telemetri verisi üreten kaynak — UI geliştirme ve test için."""

    def __init__(self, frequency_hz: int = 50):
        self._frequency_hz = frequency_hz
        self._tick = 0

    def connect(self):
        self._tick = 0

    def read(self) -> bytes:
        t = self._tick * (1.0 / self._frequency_hz)

        speed    = 80 + 30 * math.sin(t * 0.5)
        rpm      = 4000 + 2000 * math.sin(t * 0.3)
        battery  = max(0.0, 100.0 - t * 0.1)
        throttle = 50 + 40 * math.sin(t * 0.7)
        lat      = 39.925 + 0.001 * math.sin(t * 0.1)
        lon      = 32.866 + 0.001 * math.cos(t * 0.1)

        self._tick += 1
        time.sleep(1.0 / self._frequency_hz)

        # Paket formatı: speed(f) rpm(f) battery(f) throttle(f) lat(d) lon(d)
        return struct.pack("<ffffdd", speed, rpm, battery, throttle, lat, lon)

    def close(self):
        self._tick = 0
