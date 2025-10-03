#!/bin/bash

# 🚀 Kanka Mobile App - Hızlı Başlangıç Komutları

echo "=========================================="
echo "  KANKA MOBILE APP - HIZLI BAŞLANGIÇ"
echo "=========================================="
echo ""

echo "📍 Şu an bulunduğun yer:"
pwd
echo ""

echo "1️⃣ GitHub'dan clone et:"
echo "   git clone REPO-URL"
echo "   cd REPO-ADI/frontend"
echo ""

echo "2️⃣ Setup yap:"
echo "   ./setup-mobile.sh"
echo ""

echo "3️⃣ EAS CLI yükle:"
echo "   npm install -g expo-cli eas-cli"
echo ""

echo "4️⃣ Login ol:"
echo "   eas login"
echo ""

echo "5️⃣ iOS build al:"
echo "   eas build --platform ios --profile production"
echo ""

echo "6️⃣ Android build al:"
echo "   eas build --platform android --profile production"
echo ""

echo "=========================================="
echo "  DEVELOPMENT TEST"
echo "=========================================="
echo ""

echo "Lokal test için:"
echo "   expo start"
echo ""
echo "   Sonra:"
echo "   - 'i' tuşu → iOS Simulator"
echo "   - 'a' tuşu → Android Emulator"
echo "   - QR kod tara → Fiziksel cihaz"
echo ""

echo "=========================================="
echo "  YARDIMCI KOMUTLAR"
echo "=========================================="
echo ""

echo "Temiz kurulum:"
echo "   rm -rf node_modules yarn.lock"
echo "   yarn install"
echo ""

echo "Build durumu kontrol:"
echo "   eas build:list"
echo ""

echo "Build logları görüntüle:"
echo "   eas build:view BUILD-ID"
echo ""

echo "Tüm rehberleri gör:"
echo "   ls -la *.md"
echo ""

echo "=========================================="
echo "📚 DETAYLI REHBER:"
echo "   cat GITHUB_VE_BUILD_REHBERI.md"
echo ""
echo "✅ CHECKLIST:"
echo "   cat BUILD_CHECKLIST.md"
echo "=========================================="
