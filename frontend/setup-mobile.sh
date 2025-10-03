#!/bin/bash

echo "🚀 Kanka Mobile App - Hızlı Başlangıç"
echo "===================================="
echo ""

cd /app/frontend

# Yedek oluştur
if [ -f "package.json" ]; then
    echo "📦 Web package.json yedekleniyor..."
    cp package.json package-web-backup.json
fi

# Mobile package.json'u kullan
echo "📱 Mobile package.json aktifleştiriliyor..."
cp package-mobile.json package.json

# Node modules temizle
if [ -d "node_modules" ]; then
    echo "🗑️  Eski node_modules siliniyor..."
    rm -rf node_modules
fi

if [ -f "yarn.lock" ]; then
    echo "🗑️  Eski yarn.lock siliniyor..."
    rm yarn.lock
fi

# Yarn yükle
echo "⬇️  Bağımlılıklar yükleniyor (bu biraz sürebilir)..."
yarn install

echo ""
echo "✅ Kurulum tamamlandı!"
echo ""
echo "📲 Çalıştırma Komutları:"
echo "  expo start          → Development server başlat"
echo "  expo start --ios    → iOS Simulator"
echo "  expo start --android → Android Emulator"
echo ""
echo "🔨 Build Komutları:"
echo "  eas build --platform ios     → iOS IPA build"
echo "  eas build --platform android → Android AAB build"
echo ""
echo "⚠️  EAS build için önce 'eas login' yapmalısın!"
echo ""
