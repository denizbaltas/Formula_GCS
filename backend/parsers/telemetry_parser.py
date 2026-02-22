"""
Telemetry Parser.
Ham byte verisini TelemetryData modeline dönüştürür.
"""
import struct
from backend.models.telemetry_data import TelemetryData


class TelemetryParser:
    """Ham byte dizisini yapılandırılmış TelemetryData nesnesine çevirir."""

    # Paket formatı: speed(f) rpm(f) battery(f) throttle(f) lat(d) lon(d)
    PACKET_FORMAT = "<ffffdd"
    PACKET_SIZE = struct.calcsize(PACKET_FORMAT)

    def parse(self, raw: bytes) -> TelemetryData:
        """
        Ham byte verisini parse eder.

        Parameters
        ----------
        raw : bytes
            DataSource'dan gelen ham byte dizisi.

        Returns
        -------
        TelemetryData
            Parse edilmiş telemetri verisi.
        """
        if len(raw) < self.PACKET_SIZE:
            return TelemetryData()  # Eksik paket → varsayılan değerler

        speed, rpm, battery, throttle, lat, lon = struct.unpack(self.PACKET_FORMAT, raw[:self.PACKET_SIZE])

        return TelemetryData(
            speed=speed,
            rpm=rpm,
            battery=battery,
            throttle=throttle,
            latitude=lat,
            longitude=lon,
        )
