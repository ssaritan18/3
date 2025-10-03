#!/bin/bash

# 🚀 GitHub'a Yeni Repo Push Scripti

echo "=========================================="
echo "  YENİ GITHUB REPO'YA PUSH İŞLEMİ"
echo "=========================================="
echo ""

# Kullanıcıdan bilgi al
read -p "GitHub kullanıcı adın: " GITHUB_USER
read -p "Yeni repo adı (örn: adhders-mobile-app): " REPO_NAME

echo ""
echo "📦 Yeni repo: https://github.com/$GITHUB_USER/$REPO_NAME"
echo ""
read -p "Devam etmek için Enter'a bas..."

cd /app

# Mevcut remote'u kontrol et
echo "🔍 Mevcut remote kontrolü..."
git remote -v

# Yeni remote ekle veya değiştir
echo ""
echo "🔗 Yeni remote ekleniyor..."
git remote remove origin 2>/dev/null || true
git remote add origin "https://github.com/$GITHUB_USER/$REPO_NAME.git"

echo "✅ Remote eklendi: https://github.com/$GITHUB_USER/$REPO_NAME.git"

# Branch'i kontrol et
echo ""
echo "🌿 Branch kontrolü..."
CURRENT_BRANCH=$(git branch --show-current)
echo "Mevcut branch: $CURRENT_BRANCH"

# Master/main'e çevir
if [ "$CURRENT_BRANCH" != "main" ] && [ "$CURRENT_BRANCH" != "master" ]; then
    echo "Branch'i main olarak değiştiriliyor..."
    git branch -M main
fi

# .env dosyalarını git'ten kaldır
echo ""
echo "🔒 Güvenlik: .env dosyaları kaldırılıyor..."
git rm --cached backend/.env 2>/dev/null || true
git rm --cached frontend/.env 2>/dev/null || true
git rm --cached frontend/.env.mobile 2>/dev/null || true

# Değişiklikleri commit et
echo ""
echo "💾 Commit yapılıyor..."
git add .
git commit -m "React Native/Expo mobile app - iOS & Android ready" || echo "Değişiklik yok veya zaten commit edilmiş"

# Push et
echo ""
echo "🚀 GitHub'a push ediliyor..."
echo "⚠️  İlk push için username ve personal access token gerekecek!"
echo ""

git push -u origin main

if [ $? -eq 0 ]; then
    echo ""
    echo "=========================================="
    echo "  ✅ BAŞARILI!"
    echo "=========================================="
    echo ""
    echo "📦 Repo: https://github.com/$GITHUB_USER/$REPO_NAME"
    echo "🌐 Clone: git clone https://github.com/$GITHUB_USER/$REPO_NAME.git"
    echo ""
    echo "📱 Sonraki adım:"
    echo "   1. Repo'yu clone et"
    echo "   2. cd $REPO_NAME/frontend"
    echo "   3. ./setup-mobile.sh"
    echo "   4. eas build --platform ios"
    echo ""
else
    echo ""
    echo "=========================================="
    echo "  ❌ HATA!"
    echo "=========================================="
    echo ""
    echo "GitHub'da önce repo oluşturmalısın:"
    echo "1. https://github.com/new adresine git"
    echo "2. Repository name: $REPO_NAME"
    echo "3. Public veya Private seç"
    echo "4. 'Create repository' tıkla"
    echo "5. Bu scripti tekrar çalıştır"
    echo ""
fi
