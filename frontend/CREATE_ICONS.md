# 🎨 Icon ve Asset Oluşturma Rehberi

## Hızlı Çözüm (5 dakika)

### 1. Appicon.co Kullan (ÖNERİLEN)
1. https://www.appicon.co/ adresine git
2. Logonu yükle veya oluştur
3. "Generate" tıkla
4. iOS ve Android ikonlarını indir
5. `assets/` klasörüne kopyala

### 2. Manuel Oluşturma

#### icon.png (1024x1024)
- Uygulama ikonu
- Şeffaf arka plan veya solid renk
- PNG formatında

#### splash.png (1284x2778)
- iPhone 13 Pro Max boyutu
- Açılış ekranı
- Logonu ortada göster

#### adaptive-icon.png (1024x1024)
- Android için
- İkonun ortadaki 66% kısmı her zaman görünür
- Köşeler kesilir, bunu hesaba kat

#### favicon.png (48x48)
- Web versiyonu için
- Küçük icon

## Online Araçlar

- **Appicon.co** - En kolay ve ücretsiz
- **MakeAppIcon** - Alternatif
- **Canva** - Tasarım için
- **Figma** - Professional tasarım

## Placeholder Kullan

Hemen test etmek istersen:
1. Google'da "1024x1024 placeholder icon" ara
2. İndir ve `icon.png` olarak kaydet
3. Aynısını `adaptive-icon.png` için de kullan
4. `splash.png` için daha büyük placeholder kullan

## Build Sırasında Uyarı Alırsan

EAS build sırasında "missing assets" uyarısı alırsan:
- Yukarıdaki dosyaları oluştur
- Tekrar `eas build` çalıştır

---

**Not:** İkonlar olmadan da build alabilirsin ama yayınlamak için gerekli!
