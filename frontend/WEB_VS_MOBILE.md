# 🔄 Web vs Mobile - Fark Nedir?

## 📊 Karşılaştırma

| Özellik | Web (Eski) | Mobile (Yeni) |
|---------|-----------|---------------|
| Framework | React 19 | React Native 0.76.5 |
| Çalışma | Tarayıcıda | Native App |
| Bundler | Craco/Webpack | Metro |
| Styling | Tailwind CSS | NativeWind |
| Navigation | React Router | Expo Router |
| Components | HTML divs | React Native Views |
| Build | npm/yarn build | EAS Build |
| Dağıtım | Web hosting | App Store / Play Store |

---

## 📱 Neden React Native?

### Web Projesi Sorunları
- ❌ `react-dom` mobilde çalışmaz
- ❌ `@radix-ui` sadece web için
- ❌ Tarayıcı bağımlı
- ❌ Native özellikler yok

### React Native Avantajları  
- ✅ Gerçek native uygulama
- ✅ iOS ve Android aynı kodla
- ✅ App Store'da yayınlanabilir
- ✅ Native API'lere erişim
- ✅ Daha iyi performans
- ✅ Offline çalışabilir

---

## 🔧 Teknik Değişiklikler

### Paket Değişimleri

**Kaldırılanlar:**
```json
- react-dom
- react-router-dom
- @radix-ui/* (tüm paketler)
- react-scripts
- craco
```

**Eklenenler:**
```json
+ expo
+ react-native
+ expo-router
+ nativewind
+ react-native-safe-area-context
+ react-native-screens
```

### Kod Değişimleri

**Web (Eski):**
```jsx
import { BrowserRouter, Routes, Route } from 'react-router-dom';

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Home />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}
```

**Mobile (Yeni):**
```jsx
import { View, Text } from 'react-native';
import { Stack } from 'expo-router';

export default function App() {
  return (
    <View style={styles.container}>
      <Text>Hello World</Text>
    </View>
  );
}
```

---

## 🎨 Styling Farkları

### Web Tailwind
```jsx
<div className="flex items-center justify-center bg-blue-500">
  <p className="text-white text-lg">Hello</p>
</div>
```

### NativeWind (Tailwind for React Native)
```jsx
<View className="flex items-center justify-center bg-blue-500">
  <Text className="text-white text-lg">Hello</Text>
</View>
```

**Neredeyse aynı!** 🎉

---

## 🚀 Build Süreci

### Web Build
```bash
npm run build
# → /build klasörüne static files
# → Netlify/Vercel'e deploy
```

### Mobile Build
```bash
eas build --platform ios
# → .ipa dosyası (iOS)
# → App Store'a yüklenebilir

eas build --platform android  
# → .aab dosyası (Android)
# → Google Play'e yüklenebilir
```

---

## 💰 Maliyet

| Platform | Geliştirme | Yayınlama |
|----------|-----------|-----------|
| Web | ÜCRETSIZ | ÜCRETSIZ (Netlify/Vercel) |
| iOS | ÜCRETSIZ | $99/yıl (Apple Developer) |
| Android | ÜCRETSIZ | $25 (bir kerelik) |

**EAS Build:** Ücretsiz seviye var (aylık sınırlı build)

---

## 🎯 Hangisini Kullanmalıyım?

### Web Projesi İçin:
- Sadece tarayıcıda çalışacak
- SEO önemli
- Hızlı prototip
- Native özellik gerekmez

### Mobile Projesi İçin:
- App Store'da olmalı
- Push notification lazım
- Kamera/GPS kullanacak
- Offline çalışmalı
- Native performans şart

### İkisi Birden? 🤔
**Expo ile mümkün!** Aynı kod:
- iOS app
- Android app  
- Web app (bonus)

---

## 📝 Özet

Senin durumunda:
- **Sorun:** Web projesi iOS build alamıyordu
- **Çözüm:** React Native/Expo'ya çevirdik
- **Sonuç:** Artık iOS + Android native app build alabilirsin!

**Önemli:** Her iki versiyonu da sakla:
- `package.json` → Mobile
- `package-web.json` → Web (yedek)

İstersen web versiyonu da çalışmaya devam edebilir!

---

**Not:** Bu rehber senin projen için özelleştirildi. Genel React Native projelerine aynen uygulanmayabilir.
