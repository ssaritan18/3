# 🚀 Kanka Mobile App - iOS & Android

Bu proje React Native + Expo kullanarak iOS ve Android için native uygulama build edilebilir hale getirildi!

## 📱 Özellikler

- ✅ iOS IPA build desteği
- ✅ Android AAB/APK build desteği  
- ✅ Backend API entegrasyonu
- ✅ Modern React Native 0.76.5
- ✅ Expo Router navigasyon
- ✅ NativeWind (Tailwind for React Native)

## 🛠️ Kurulum

### 1. Bağımlılıkları Yükle

```bash
cd /app/frontend

# Önce web package.json'u yedekle
cp package.json package-web.json

# Mobile package.json'u kullan
cp package-mobile.json package.json

# Yarn ile yükle (NPM KULLANMA!)
yarn install
```

### 2. Expo CLI'yi Global Yükle

```bash
npm install -g expo-cli eas-cli
```

### 3. Expo Hesabı Oluştur

https://expo.dev/ adresinden ücretsiz hesap aç

```bash
# Login ol
eas login
```

## 📦 Asset Dosyalarını Ekle

`/app/frontend/assets/` klasörüne şu dosyaları ekle:

- **icon.png** (1024x1024) - Uygulama ikonu
- **splash.png** (1284x2778) - Açılış ekranı
- **adaptive-icon.png** (1024x1024) - Android adaptive icon
- **favicon.png** (48x48) - Web favicon

**Hızlı çözüm:** https://www.appicon.co/ kullanarak ücretsiz oluşturabilirsin

## 🔥 Çalıştırma

### Development Mode

```bash
cd /app/frontend
expo start
```

Sonra:
- **i** tuşuna bas → iOS Simulator
- **a** tuşuna bas → Android Emulator
- QR kod tara → Fiziksel cihazda test et (Expo Go app ile)

## 📲 Production Build

### iOS IPA Build

```bash
cd /app/frontend

# İlk seferinde configure et
eas build:configure

# iOS build başlat
eas build --platform ios --profile production

# Build tamamlanınca .ipa dosyasını indir
```

**Not:** iOS için Apple Developer hesabına ihtiyacın var ($99/yıl)

### Android AAB Build

```bash
cd /app/frontend

# Android build başlat
eas build --platform android --profile production

# APK istersan (Google Play Store dışında dağıtım için)
eas build --platform android --profile production --android-build-type apk
```

### Her İkisi Birden

```bash
eas build --platform all --profile production
```

## 🔧 Sorun Giderme

### React Version Conflict

Eğer hala dependency error alırsan:

```bash
cd /app/frontend
rm -rf node_modules yarn.lock
yarn install
```

### iOS Simulator Çalışmıyor

```bash
# Xcode Command Line Tools'u yükle
xcode-select --install
```

### Android Build Crash Ediyor

`app.json` dosyasında `versionCode`'u artır:

```json
"android": {
  "versionCode": 2  // Her build'de +1 artır
}
```

## 📝 Önemli Dosyalar

- `app.json` - Expo yapılandırması (iOS/Android ayarları)
- `eas.json` - Build profilleri
- `app/index.js` - Ana uygulama ekranı
- `app/_layout.js` - Navigation layout

## 🌐 Backend Bağlantısı

Backend URL: `https://kanka-hello.preview.emergentagent.com`

Değiştirmek için `app/index.js` dosyasındaki `BACKEND_URL` değişkenini düzenle.

## 📚 Kaynaklar

- [Expo Documentation](https://docs.expo.dev/)
- [EAS Build Guide](https://docs.expo.dev/build/introduction/)
- [React Native Docs](https://reactnative.dev/)

## 🆘 Yardım

Problem yaşarsan:
1. `expo doctor` komutu çalıştır
2. Expo Forums: https://forums.expo.dev/
3. Discord: https://chat.expo.dev/

---

**Hazırladı:** E1 Agent 🤖
