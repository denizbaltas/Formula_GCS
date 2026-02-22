# GCS Gelecek Planı — Roadmap

> **Mevcut durum:** Yapı oluşturuldu, Track sayfası fake data ile çalışıyor. Dashboard ve Telemetry sayfaları placeholder.

---

## Faz 1 — Dashboard Sayfası (Canlı Göstergeler)

**Amaç:** Araçtan gelen temel verileri anlık gösterecek göstergeler.

| Component | Dosya | Açıklama |
|---|---|---|
| Hız Göstergesi | `dashboard/components/speed_gauge.py` | Sürat (km/h) — dairesel gauge |
| RPM Göstergesi | `dashboard/components/rpm_gauge.py` | Motor devir göstergesi |
| Batarya Durumu | `dashboard/components/battery_indicator.py` | Yüzde + bar indicator |
| Throttle | `dashboard/components/throttle_bar.py` | Gaz pozisyonu — progress bar |
| Durum Çubuğu | `dashboard/components/status_bar.py` | Bağlantı durumu, mode, timestamp |

---

## Faz 2 — Telemetry Sayfası (Grafikler + Tablo)

**Amaç:** Zaman serisi grafikleriyle detaylı veri analizi.

| Component | Dosya | Açıklama |
|---|---|---|
| Canlı Grafik | `telemetry/components/live_chart.py` | Kaydırılabilir zaman serisi |
| Veri Tablosu | `telemetry/components/data_table.py` | Son N paketi gösteren QTableWidget |
| GPS Harita | `telemetry/components/gps_view.py` | Lat/Lon noktalarını harita üzerinde gösterme |

---

## Faz 3 — Simulation Altyapısı & Veri Akışı

**Amaç:** Backend'den frontend'e veri akışını simülasyon ile uçtan uca çalıştırmak.

| Adım | Dosya / Modül | Açıklama |
|---|---|---|
| DataMode switch | `config.py` | `SIMULATION` mode aktifken `SimulationSource` otomatik seçilsin |
| Data Pipeline | `backend/data_pipeline.py` | `QThread` ile `SimulationSource.read()` → parse → `TelemetryData` → Qt Signal yayını |
| TelemetryData timestamp | `backend/models/telemetry_data.py` | Her pakete `timestamp: float` alanı eklenmesi |
| Veri loglama (CSV) | `backend/logger/csv_logger.py` | Gelen her `TelemetryData` paketini zaman damgalı CSV'ye kaydetme |
| Replay Source | `backend/data_sources/replay_source.py` | Kayıtlı CSV log dosyasını satır satır okuyup `DataSource` gibi yayımlama |
| DataMode.REPLAY | `config.py` | Yeni mod: `REPLAY` — dosya yolunu belirt, kaydı tekrar oynat |

---

## Faz 4 — UI / UX İyileştirme

| Konu | Detay |
|---|---|
| Dark Theme | `styles/theme.qss` ile tüm uygulamaya dark mode |
| Nav Bar | İkon + yazı, aktif sayfa vurgulu |
| Responsive Layout | Pencere küçüldüğünde component'ler otomatik dizilmeli |
| Splash Screen | Uygulama açılışında logo + yükleniyor ekranı |
| Kısayollar | Ctrl+1/2/3 ile hızlı sayfa geçişi |

---

## Faz 5 — Backend Canlı Bağlantı

**Amaç:** Simulation yerine gerçek veri kaynağına bağlanma.

| Adım | Açıklama |
|---|---|
| Serial entegrasyonu | `serial_source.py` → gerçek UART protokolüyle test |
| Telemetry parser | `telemetry_parser.py` → araç firmware paket formatına göre güncelleme |
| `config.py` geçişi | `DataMode.SERIAL` seçilince gerçek veriye geçiş |
| Thread yapısı | `QThread` ile arka planda veri okuma |

---

## Faz 6 — İleri Özellikler

| Özellik | Açıklama |
|---|---|
| Alarm Sistemi | Kritik değer aşıldığında sesli/görsel uyarı |
| Komut Gönderme | GCS → Araç yönünde komut (kalibrasyon, mod değişikliği) |
| Replay Mode | Kayıtlı log dosyasını tekrar oynatma |
| Çoklu Araç | Birden fazla araçtan eş zamanlı veri |
| Plugin Sistemi | Yeni sayfa/component eklemeyi kolaylaştırma |
