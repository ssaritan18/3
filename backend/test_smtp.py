#!/usr/bin/env python3
"""
SMTP Test Script - Mail gönderimini test etmek için
"""
import os
import asyncio
import aiosmtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

# Environment variables'ları yükle
load_dotenv()

# SMTP Configuration
SMTP_HOST = os.getenv("SMTP_HOST", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
SMTP_USERNAME = os.getenv("SMTP_USERNAME", "")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD", "")
SMTP_FROM_EMAIL = os.getenv("SMTP_FROM_EMAIL", "noreply@adhders.com")

print("🔧 SMTP Configuration Test")
print("=" * 50)
print(f"SMTP_HOST: {SMTP_HOST}")
print(f"SMTP_PORT: {SMTP_PORT}")
print(f"SMTP_USERNAME: {SMTP_USERNAME}")
print(f"SMTP_PASSWORD: {'***' if SMTP_PASSWORD else 'None'}")
print(f"SMTP_FROM_EMAIL: {SMTP_FROM_EMAIL}")
print(f"EMAIL_ENABLED: {bool(SMTP_USERNAME and SMTP_PASSWORD)}")
print("=" * 50)

async def test_smtp_connection():
    """SMTP bağlantısını test et"""
    if not SMTP_USERNAME or not SMTP_PASSWORD:
        print("❌ SMTP_USERNAME veya SMTP_PASSWORD eksik!")
        print("Lütfen .env dosyasında gerçek SMTP bilgilerini girin.")
        return False
    
    try:
        print("🔄 SMTP bağlantısı test ediliyor...")
        
        # Test email oluştur
        message = MIMEMultipart("alternative")
        message["Subject"] = "SMTP Test - ADHDers Social Club"
        message["From"] = f"ADHDers Social Club <{SMTP_FROM_EMAIL}>"
        message["To"] = SMTP_USERNAME  # Kendine gönder
        
        # HTML content
        html_content = """
        <html>
        <body>
            <h2>SMTP Test Başarılı! 🎉</h2>
            <p>Bu email SMTP konfigürasyonunuzun çalıştığını gösterir.</p>
            <p>ADHDers Social Club mail sistemi aktif.</p>
        </body>
        </html>
        """
        
        html_part = MIMEText(html_content, "html")
        message.attach(html_part)
        
        # Email gönder
        await aiosmtplib.send(
            message,
            hostname=SMTP_HOST,
            port=SMTP_PORT,
            start_tls=True,
            username=SMTP_USERNAME,
            password=SMTP_PASSWORD,
        )
        
        print("✅ SMTP bağlantısı başarılı!")
        print(f"📧 Test email {SMTP_USERNAME} adresine gönderildi")
        return True
        
    except Exception as e:
        print(f"❌ SMTP bağlantısı başarısız: {e}")
        print("\n🔍 Olası sorunlar:")
        print("1. Gmail App Password kullanıyor musunuz? (Normal şifre değil)")
        print("2. 2-Factor Authentication açık mı?")
        print("3. 'Less secure app access' açık mı?")
        print("4. SMTP_HOST ve SMTP_PORT doğru mu?")
        return False

async def test_forgot_password_flow():
    """Forgot password flow'unu test et"""
    print("\n🔄 Forgot Password Flow Test")
    print("=" * 50)
    
    # Test email
    test_email = input("Test için email adresi girin (kendi emailiniz): ").strip()
    if not test_email:
        print("❌ Email adresi gerekli!")
        return False
    
    try:
        # Password reset email template
        reset_token = "test-token-12345"
        base_url = os.getenv("BASE_URL", "https://adhderssocialclub4.vercel.app")
        reset_url = f"{base_url}/reset-password?token={reset_token}"
        
        content = f"""
        <h2>Password Reset Request - TEST</h2>
        <p>Bu bir test email'idir. ADHDers Social Club password reset sistemi çalışıyor.</p>
        <p>
            <a href="{reset_url}" style="background: #A3C9FF; color: #0c0c0c; padding: 12px 24px; text-decoration: none; border-radius: 6px; font-weight: bold;">Reset Password</a>
        </p>
        <p>Or copy and paste this link: <br><code>{reset_url}</code></p>
        <p>This is a test email - the token is not real.</p>
        """
        
        # Email gönder
        message = MIMEMultipart("alternative")
        message["Subject"] = "Reset Your Password - ADHDers Social Club (TEST)"
        message["From"] = f"ADHDers Social Club Support <{SMTP_FROM_EMAIL}>"
        message["To"] = test_email
        
        html_part = MIMEText(content, "html")
        message.attach(html_part)
        
        await aiosmtplib.send(
            message,
            hostname=SMTP_HOST,
            port=SMTP_PORT,
            start_tls=True,
            username=SMTP_USERNAME,
            password=SMTP_PASSWORD,
        )
        
        print(f"✅ Test password reset email {test_email} adresine gönderildi!")
        return True
        
    except Exception as e:
        print(f"❌ Test email gönderilemedi: {e}")
        return False

async def main():
    print("🚀 ADHDers Social Club SMTP Test")
    print("=" * 50)
    
    # 1. SMTP bağlantısını test et
    smtp_ok = await test_smtp_connection()
    
    if smtp_ok:
        # 2. Forgot password flow'unu test et
        await test_forgot_password_flow()
    
    print("\n" + "=" * 50)
    if smtp_ok:
        print("🎉 SMTP konfigürasyonu çalışıyor!")
        print("Backend'de forgot password artık mail gönderebilir.")
    else:
        print("❌ SMTP konfigürasyonu düzeltilmeli.")
        print("Lütfen .env dosyasındaki SMTP bilgilerini kontrol edin.")

if __name__ == "__main__":
    asyncio.run(main())

