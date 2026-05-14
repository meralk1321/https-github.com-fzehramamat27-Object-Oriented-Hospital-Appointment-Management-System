# https-github.com-fzehramamat27-Object-Oriented-Hospital-Appointment-Management-System
# Object-Oriented-Hospital-Appointment-Management-System
Nesne Tabanlı Programlama(OOP) ilkeleri ile geliştirilmiş Python tabanlı hastane randevu yönetim sistemi
​Bu proje, Kastamonu Üniversitesi Tosya Meslek Yüksekokulu Programlama II dersi dönem sonu ödevi kapsamında geliştirilmiştir. 
Proje Özeti ve Amacı
# Hastane Randevu Sistemi

Python ve Tkinter kullanılarak geliştirilmiş basit bir **Hastane Randevu Yönetim Sistemi**.  
Bu uygulama sayesinde doktor ekleyebilir, hastalara randevu oluşturabilir ve mevcut randevuları görüntüleyebilirsiniz.

## Özellikler

- Doktor ekleme
- Doktor listesini görüntüleme
- Hasta için randevu oluşturma
- Oluşturulan randevuları listeleme
- SQLite veritabanı ile kalıcı veri saklama
- Basit ve kullanıcı dostu arayüz (Tkinter GUI)

---

## Proje Yapısı

```bash
📂 proje-klasoru
│── main.py
│── gui.py
│── veritabani.py
│── kullanici.py
│── hastane.db
│── README.md
```

### Dosya Açıklamaları

### `main.py`
Programın başlangıç noktasıdır.  
Tkinter ana penceresini oluşturur ve GUI'yi başlatır.

### `gui.py`
Grafik arayüzün bulunduğu dosyadır.

İçerdiği işlemler:

- Doktor ekleme
- Doktorları combobox içine yükleme
- Hasta adına randevu oluşturma
- Randevuları tablo halinde gösterme

### `veritabani.py`
SQLite veritabanı işlemlerini yönetir.

İçerdiği fonksiyonlar:

- Veritabanı bağlantısı oluşturma
- Gerekli tabloları oluşturma
- Doktor ekleme
- Doktorları listeleme
- Randevu oluşturma
- Randevuları listeleme

### `kullanici.py`
Doktor sınıfını içerir.

Örnek:

```python
class Doktor:
    def __init__(self, ad, soyad, tc, uzmanlik):
        self.ad = ad
        self.soyad = soyad
        self.tc = tc
        self.uzmanlik = uzmanlik

    def tam_ad(self):
        return f"{self.ad} {self.soyad}"
```

---

## Kurulum

### 1. Python kurulu olmalı

Python 3.x yüklü olmalıdır.

Kontrol etmek için:

```bash
python --version
```

---

### 2. Projeyi çalıştır

```bash
python main.py
```

---

## Kullanım

### Doktor ekleme

- Ad girin
- Soyad girin
- Uzmanlık girin
- **Doktor Ekle** butonuna basın

---

### Randevu oluşturma

- Hasta adını girin
- Doktor seçin
- **Randevu Oluştur** butonuna basın

---

### Randevuları görüntüleme

Alt bölümde tüm randevular tablo şeklinde gösterilir.

Örnek:

```text
ID | Hasta       | Doktor
1  | Ahmet Yılmaz | Mehmet Kaya
2  | Ayşe Demir   | Fatma Arslan
```
## Kullanılan Teknolojiler

- Python
- Tkinter
- SQLite3
- OOP (Nesne Yönelimli Programlama)
- 
## Veritabanı Yapısı

### doktorlar tablosu

| Alan | Tip |
|------|-----|
| id | INTEGER |
| ad | TEXT |
| uzmanlik | TEXT |

### randevular tablosu

| Alan | Tip |
|------|-----|
| id | INTEGER |
| hasta_ad | TEXT |
| doktor_id | INTEGER |

## Geliştirme Fikirleri

Projeye eklenebilecek özellikler:

- Doktor silme
- Randevu iptal etme
- Hasta bilgileri ekleme
- Tarih ve saat seçimi
- Doktor uzmanlık filtreleme
- Kullanıcı giriş sistemi

Bu proje, Python'da:
 Tkinter GUI geliştirme
- SQLite veritabanı kullanımı
- Sınıf yapısı oluşturma
- CRUD işlemleri

öğrenmek amacıyla hazırlanmıştır.
