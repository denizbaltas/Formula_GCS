"""
Abstract base class for all data sources.
Her veri kaynağı (Serial, UDP, Simulation) bu sınıfı implement eder.
"""
from abc import ABC, abstractmethod


class DataSource(ABC):
    """Veri kaynağı soyut arayüzü."""

    @abstractmethod
    def connect(self):
        """Veri kaynağına bağlan."""
        ...

    @abstractmethod
    def read(self) -> bytes:
        """Ham veri oku. Blocking çağrıdır."""
        ...

    @abstractmethod
    def close(self):
        """Bağlantıyı kapat ve kaynakları serbest bırak."""
        ...
