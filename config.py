"""
GCS Yapılandırma Dosyası.
Mode seçimi, bağlantı parametreleri ve simulation ayarları.
"""
from enum import Enum


class DataMode(Enum):
    SERIAL     = "serial"
    UDP        = "udp"
    SIMULATION = "simulation"


# ── Aktif mode ─────────────────────────────────────────
ACTIVE_MODE = DataMode.SIMULATION

# ── Serial ayarları ────────────────────────────────────
SERIAL_PORT = "COM3"
SERIAL_BAUD = 115200

# ── UDP ayarları ───────────────────────────────────────
UDP_HOST = "0.0.0.0"
UDP_PORT = 5005

# ── Simulation ayarları ───────────────────────────────
SIM_FREQUENCY_HZ = 50   # Saniyede kaç paket üretilecek
