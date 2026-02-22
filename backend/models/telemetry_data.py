"""
Telemetry veri modeli.
Backend ve frontend arasında taşınan verinin yapısını tanımlar.
"""
from dataclasses import dataclass, field
from typing import Optional
import numpy as np


@dataclass
class TelemetryData:
    """Tek bir telemetri paketini temsil eder."""

    speed: float = 0.0          # km/h
    rpm: float = 0.0            # devir/dakika
    battery: float = 0.0        # yüzde (%)
    throttle: float = 0.0       # yüzde (%)
    latitude: float = 0.0       # derece
    longitude: float = 0.0      # derece

    def to_dict(self) -> dict:
        """Qt Signal ile göndermek için dict'e çevir."""
        return {
            "speed": self.speed,
            "rpm": self.rpm,
            "battery": self.battery,
            "throttle": self.throttle,
            "latitude": self.latitude,
            "longitude": self.longitude,
        }
