# ✅ iOS/Android Build - Hızlı Checklist

## 📋 Başlamadan Önce

- [ ] Node.js yüklü (v18+) → `node --version`
- [ ] Git yüklü → `git --version`
- [ ] Expo hesabı açıldı → https://expo.dev/
- [ ] iOS için Apple Developer hesabı ($99/yıl) - opsiyonel test için

---

## 🚀 Adımlar

### 1. GitHub'a Push Et
- [ ] Emergent'ta "Save to GitHub" butonuna tıkla
- [ ] Veya: `git push origin main`

### 2. Lokal'e Clone Et
```bash
cd ~/Desktop
git clone REPO-URL
cd REPO-ADI/frontend
```
- [ ] Tamamlandı

### 3. Setup
```bash
./setup-mobile.sh
```
- [ ] Script çalıştırıldı
- [ ] Yarn install tamamlandı
- [ ] package-mobile.json → package.json oldu

### 4. Icon Dosyalarını Ekle (Opsiyonel)
```bash
cd assets/
# icon.png, splash.png, adaptive-icon.png ekle
```
- [ ] İkonlar eklendi veya şimdilik atla

### 5. EAS CLI Yükle
```bash
npm install -g expo-cli eas-cli
```
- [ ] Yüklendi
- [ ] `eas --version` çalışıyor

### 6. Expo Login
```bash
eas login
```
- [ ] Kullanıcı adı + şifre girildi
- [ ] Login başarılı

### 7. iOS Build Başlat
```bash
eas build:configure
eas build --platform ios --profile production
```
- [ ] Sorulara "Yes" dendi
- [ ] Build başladı
- [ ] Build URL kaydedildi

### 8. Android Build Başlat
```bash
eas build --platform android --profile production
```
- [ ] Build başladı
- [ ] Build URL kaydedildi

### 9. Build'leri Bekle
- [ ] iOS build tamamlandı (15-30dk)
- [ ] Android build tamamlandı (10-20dk)
- [ ] .ipa dosyası indirildi
- [ ] .aab dosyası indirildi

### 10. Test Et
- [ ] iOS: TestFlight'a yüklendi
- [ ] Android: Cihaza yüklendi
- [ ] Uygulama çalışıyor
- [ ] Backend bağlantısı OK

---

## 🎉 Başarılı!

Artık gerçek native uygulamanı aldın!

**Sonraki adımlar:**
- App Store'a yükle (iOS)
- Google Play'e yükle (Android)
- Kullanıcılara dağıt

---

## 📞 Yardım

Bu checklist'teki herhangi bir adımda takılırsan:

```bash
cat /app/frontend/GITHUB_VE_BUILD_REHBERI.md
```

Detaylı rehbere bak! 🚀
