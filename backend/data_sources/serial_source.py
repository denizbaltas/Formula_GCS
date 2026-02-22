"""
Serial port (UART) veri kaynağı.
Araç üzerindeki mikrodenetleyiciden seri port ile veri okur.
"""
import serial
from .base_source import DataSource


class SerialSource(DataSource):
    """Serial port üzerinden ham telemetri verisi okur."""

    def __init__(self, port: str = "COM3", baudrate: int = 115200, timeout: float = 1.0):
        self._port = port
        self._baudrate = baudrate
        self._timeout = timeout
        self._serial: serial.Serial | None = None

    def connect(self):
        self._serial = serial.Serial(
            port=self._port,
            baudrate=self._baudrate,
            timeout=self._timeout,
        )

    def read(self) -> bytes:
        if self._serial is None:
            raise RuntimeError("Serial port bağlantısı açılmadı. Önce connect() çağırın.")
        # Satır bazlı okuma — protokolünüze göre değiştirin
        return self._serial.readline()

    def close(self):
        if self._serial and self._serial.is_open:
            self._serial.close()
