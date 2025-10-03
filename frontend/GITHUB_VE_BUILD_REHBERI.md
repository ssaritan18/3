# 🔄 GitHub Push ve Build Alma Rehberi

## 🎯 EN İYİ YOL (ÖNERİLEN)

### Yöntem 1: Lokal Bilgisayarında Build Al

Bu en kolay ve hızlı yol!

#### 1️⃣ GitHub'a Push Et

**Emergent platformunda:**
- Chat input'un yanındaki **"Save to GitHub"** butonuna tıkla
- Veya git komutlarını kullan (aşağıda)

**Manuel push istersan:**
```bash
cd /app
git add .
git commit -m "React Native/Expo mobile app eklendi"
git push origin main
```

#### 2️⃣ Lokal Bilgisayarına Clone Et

```bash
# Terminalini aç (Mac: Terminal, Windows: Git Bash)
cd ~/Desktop
git clone https://github.com/SENIN-KULLANICI-ADIN/REPO-ADIN.git
cd REPO-ADIN/frontend
```

#### 3️⃣ Setup Yap

```bash
# Setup script'i çalıştır
./setup-mobile.sh

# Veya manuel:
cp package-mobile.json package.json
yarn install
```

#### 4️⃣ Expo/EAS CLI Yükle

```bash
npm install -g expo-cli eas-cli
```

#### 5️⃣ Expo'ya Login Ol

```bash
eas login
# Kullanıcı adı ve şifre gir (expo.dev'den kayıt ol)
```

#### 6️⃣ Build Al! 🔥

```bash
# iOS
eas build:configure
eas build --platform ios --profile production

# Android
eas build --platform android --profile production

# Her ikisi
eas build --platform all --profile production
```

**Build bulutta yapılır!** Bilgisayarın 30dk beklerken kapalı bile olabilir.

#### 7️⃣ Build Tamamlandı

EAS sana link verir:
```
✔ Build complete!
Download: https://expo.dev/artifacts/eas/xxxxx.ipa
```

.ipa veya .aab dosyasını indir!

---

## 🌐 Yöntem 2: GitHub Actions (Otomatik Build)

Her push'ta otomatik build almak istersen:

### .github/workflows/build.yml Oluştur

```yaml
name: EAS Build

on:
  push:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Setup Node
        uses: actions/setup-node@v3
        with:
          node-version: 18
      
      - name: Setup Expo
        uses: expo/expo-github-action@v8
        with:
          expo-version: latest
          eas-version: latest
          token: ${{ secrets.EXPO_TOKEN }}
      
      - name: Install dependencies
        working-directory: ./frontend
        run: |
          cp package-mobile.json package.json
          yarn install
      
      - name: Build iOS
        working-directory: ./frontend
        run: eas build --platform ios --non-interactive --no-wait
      
      - name: Build Android
        working-directory: ./frontend
        run: eas build --platform android --non-interactive --no-wait
```

**Gerekli:**
- GitHub Secrets'a `EXPO_TOKEN` ekle
- Expo dashboard'dan token al: https://expo.dev/settings/access-tokens

---

## 📦 Hangi Yöntemi Seçmeliyim?

| Yöntem | Avantaj | Dezavantaj |
|--------|---------|------------|
| **Lokal Build** | Kolay, hızlı başlangıç | Her seferinde manuel |
| **GitHub Actions** | Otomatik, push ettikçe build | İlk kurulum biraz karmaşık |

**Öneri:** İlk build için **Lokal** yap, test et. Sonra istersen GitHub Actions ekle.

---

## 💡 ADIM ADIM (Yeni Başlayan İçin)

### 1. Emergent'ta "Save to GitHub" Yap

Chat input'un yanında buton var → Tıkla → Repo'ya push edilir

### 2. Bilgisayarında Terminal Aç

**Mac:**
- Spotlight (Cmd+Space) → "Terminal" yaz → Enter

**Windows:**
- Start → "Git Bash" yaz → Enter
- (Git yoksa: https://git-scm.com/download/win indir)

### 3. Projeyi İndir

```bash
cd Desktop
git clone https://github.com/KULLANICI-ADIN/REPO-ADIN.git
cd REPO-ADIN
```

### 4. Node.js Var mı Kontrol Et

```bash
node --version
```

Yoksa → https://nodejs.org/ (LTS versiyonu indir)

### 5. Frontend Klasörüne Git

```bash
cd frontend
ls -la
# app.json, package-mobile.json görmelisin
```

### 6. Setup Yap

**Mac/Linux:**
```bash
./setup-mobile.sh
```

**Windows (Git Bash):**
```bash
bash setup-mobile.sh
```

### 7. Expo CLI Yükle

```bash
npm install -g expo-cli eas-cli
```

### 8. Expo Hesabı Aç

https://expo.dev/ → Sign Up (ücretsiz)

### 9. Login Ol

```bash
eas login
```

Kullanıcı adı + şifre gir

### 10. Build Başlat! 🚀

```bash
eas build --platform ios --profile production
```

**Sorular gelecek:**
- "Would you like to automatically create an EAS project?" → **Yes**
- "Generate a new Apple Distribution Certificate?" → **Yes**
- "Generate a new Apple Provisioning Profile?" → **Yes**

**Build başladı!** 15-30dk sürer. Link gelecek:

```
Build URL: https://expo.dev/accounts/KULLANICI-ADIN/projects/kanka-app/builds/xxxx
```

Bu linke git, build'i izle, tamamlanınca .ipa'yı indir!

---

## 🍎 iOS İçin Apple Hesabı

iOS build için **Apple Developer hesabı** şart:

1. https://developer.apple.com/ → Kayıt ol ($99/yıl)
2. EAS build sırasında Apple ID'ni gir
3. Sertifika otomatik oluşur

**Test için:** Simulator build yapabilirsin (Apple hesap gerekmez):
```bash
eas build --platform ios --profile preview
```

---

## 🤖 Android Daha Kolay

Android için hesap gerekmez! Direkt build al:

```bash
eas build --platform android --profile production
```

.aab dosyası gelir → Google Play'e yükleyebilirsin

---

## 🔧 Icon Dosyalarını Unutma!

Build başlatmadan önce `/frontend/assets/` klasörüne:

```bash
cd assets
# Buraya koy:
# - icon.png (1024x1024)
# - splash.png (1284x2778)
# - adaptive-icon.png (1024x1024)
```

**Hızlı çözüm:** https://www.appicon.co/

---

## 📝 Özet

```bash
# 1. GitHub'a push et (Emergent'ta "Save to GitHub")

# 2. Lokal'e clone et
git clone REPO-URL
cd REPO-ADI/frontend

# 3. Setup
./setup-mobile.sh

# 4. EAS yükle
npm install -g eas-cli

# 5. Login
eas login

# 6. Build!
eas build --platform ios
eas build --platform android
```

---

## 🆘 Sorun Yaşarsan

### "eas: command not found"
```bash
npm install -g eas-cli
# Sonra terminal'i kapat aç
```

### "Invalid credentials"
```bash
eas logout
eas login
```

### "Missing assets"
→ Icon dosyalarını ekle (CREATE_ICONS.md)

### "Apple authentication failed"
→ Apple Developer hesabı lazım ($99/yıl)

---

## ✅ İlk Build Sonrası

Build başarılı olduysa:

1. **Test et:** .ipa'yı iPhone'a yükle (TestFlight kullan)
2. **Android:** .aab'ı Google Play Console'a yükle
3. **iOS:** App Store Connect'e yükle

---

**Başarılar!** İlk native app build'ini alacaksın! 🎉

Sorun yaşarsan buraya yaz, yardımcı olayım! 🚀
