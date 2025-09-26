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
SMTP_PORT = 465  # Use SSL port
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
            use_tls=True,  # Use SSL instead of STARTTLS for port 465
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

async def test_welcome_email():
    """Welcome email test et"""
    print("\n🎉 Welcome Email Test")
    print("=" * 50)
    
    # Test email
    test_email = input("Test için email adresi girin (kendi emailiniz): ").strip()
    if not test_email:
        print("❌ Email adresi gerekli!")
        return False
    
    try:
        # Welcome email template
        user_name = "Seyma Test"
        base_url = os.getenv("BASE_URL", "https://adhderssocialclub4.vercel.app")
        profile_url = f"{base_url}/profile"
        community_url = f"{base_url}/community"
        
        content = f"""
        <!DOCTYPE html>
        <html>
          <body style="font-family: Arial, sans-serif; line-height:1.5; color:#333;">
            <div style="max-width:600px; margin:0 auto; padding:20px; text-align:center;">
              <!-- Header with dark purple gradient matching frontend -->
              <div style="background: linear-gradient(135deg, #2D1B69 0%, #4A148C 50%, #6A1B9A 100%); padding: 35px 20px; border-radius: 20px; margin-bottom: 25px; box-shadow: 0 10px 30px rgba(45, 27, 105, 0.4), 0 0 20px rgba(106, 27, 154, 0.3); position: relative; overflow: hidden;">
                <!-- Neon glow effect -->
                <div style="position: absolute; top: -10px; left: -10px; right: -10px; bottom: -10px; background: linear-gradient(45deg, #3F51B5, #E91E63, #FF9800, #3F51B5); border-radius: 25px; opacity: 0.3; filter: blur(15px); z-index: -1;"></div>
                <h1 style="color: white; margin: 0; font-size: 28px; font-weight: bold; text-shadow: 0 0 20px rgba(255,255,255,0.5), 0 2px 8px rgba(0,0,0,0.5); position: relative; z-index: 1;">Welcome to ADHDers Social Club! 🎉</h1>
              </div>
              <p style="font-weight: bold; font-size: 16px;">Hi {user_name},</p>

              <p style="font-weight: bold; font-size: 14px; line-height: 1.6;">
                We're thrilled to have you on board! You've just joined a community designed for creative, bold, and neurodivergent minds like yours.
              </p>

              <div style="margin: 40px 0;">
                <a href="{profile_url}" 
                   style="display:inline-block; background: linear-gradient(135deg, #4A148C 0%, #6A1B9A 100%); color:#fff; padding:15px 30px; text-decoration:none; border-radius:12px; margin:8px; font-weight:bold; box-shadow: 0 4px 15px rgba(74, 20, 140, 0.3); transition: all 0.3s ease;">
                  Complete Your Profile
                </a>
                <a href="{community_url}" 
                   style="display:inline-block; background: linear-gradient(135deg, #E91E63 0%, #FF9800 100%); color:#fff; padding:15px 30px; text-decoration:none; border-radius:12px; margin:8px; font-weight:bold; box-shadow: 0 4px 15px rgba(233, 30, 99, 0.3); transition: all 0.3s ease;">
                  Find Your Community
                </a>
              </div>

              <div style="background: linear-gradient(135deg, #F3E5F5 0%, #E8F5E8 100%); padding: 20px; border-radius: 15px; margin: 25px 0; border-left: 4px solid #6A1B9A;">
                <p style="margin: 0 0 12px 0; font-size: 14px; line-height: 1.5; font-weight: bold;">📱 <strong>Track your productivity</strong> with gamified tools that make progress fun.</p>
                <p style="margin: 0 0 12px 0; font-size: 14px; line-height: 1.5; font-weight: bold;">💡 <strong>Boost your healthy dopamine</strong> by celebrating small wins every day.</p>
                <p style="margin: 0; font-size: 14px; line-height: 1.5; font-weight: bold;">🤝 <strong>Find your neurodivergent friends</strong> and feel supported.</p>
              </div>

              <p style="font-size: 16px; font-style: italic; color: #4A148C; margin: 25px 0; padding: 18px; background: linear-gradient(135deg, #F8F9FA 0%, #E3F2FD 100%); border-radius: 12px; border: 1px solid #E1BEE7; font-weight: bold;">This is more than just an app – it's your safe space to grow, connect, and thrive.</p>

              <div style="margin-top: 40px; padding: 20px; background: linear-gradient(135deg, #2D1B69 0%, #4A148C 100%); border-radius: 15px; text-align: center;">
                <p style="color: white; margin: 0; font-size: 16px; font-weight: bold;">Best regards,</p>
                <p style="color: white; margin: 5px 0 0 0; font-size: 14px; opacity: 0.9; font-weight: bold;">The ADHDers Social Club Team</p>
              </div>
            </div>
          </body>
        </html>
        """
        
        # Email gönder
        message = MIMEMultipart("alternative")
        message["Subject"] = "🎉 Welcome to ADHDers Social Club – Your Journey Starts Here! (TEST)"
        message["From"] = f"ADHDers Social Club Support <{SMTP_FROM_EMAIL}>"
        message["To"] = test_email
        
        html_part = MIMEText(content, "html")
        message.attach(html_part)
        
        await aiosmtplib.send(
            message,
            hostname=SMTP_HOST,
            port=SMTP_PORT,
            use_tls=True,  # Use SSL instead of STARTTLS for port 465
            username=SMTP_USERNAME,
            password=SMTP_PASSWORD,
        )
        
        print(f"✅ Test welcome email {test_email} adresine gönderildi!")
        return True
        
    except Exception as e:
        print(f"❌ Test welcome email gönderilemedi: {e}")
        return False

async def test_verification_email():
    """Verification email test et"""
    print("\n📧 Verification Email Test")
    print("=" * 50)
    
    # Test email
    test_email = input("Test için email adresi girin (kendi emailiniz): ").strip()
    if not test_email:
        print("❌ Email adresi gerekli!")
        return False
    
    try:
        # Verification email template
        verification_token = "test-verification-token-12345"
        base_url = os.getenv("BASE_URL", "https://adhderssocialclub4.vercel.app")
        verify_url = f"{base_url}/verify-email?token={verification_token}"
        
        content = f"""
        <h2>Welcome to ADHDers Social Club! 🎉</h2>
        <p>Thanks for signing up! Please verify your email address to complete your registration.</p>
        <p>
            <a href="{verify_url}" style="background: #A3C9FF; color: #0c0c0c; padding: 12px 24px; text-decoration: none; border-radius: 6px; font-weight: bold;">Verify Email Address</a>
        </p>
        <p>Or copy and paste this link: <br><code>{verify_url}</code></p>
        <p>This link will expire in 24 hours.</p>
        <p>This is a test email - the token is not real.</p>
        """
        
        # Email gönder
        message = MIMEMultipart("alternative")
        message["Subject"] = "Verify Your Email - ADHDers Social Club (TEST)"
        message["From"] = f"ADHDers Social Club Support <{SMTP_FROM_EMAIL}>"
        message["To"] = test_email
        
        html_part = MIMEText(content, "html")
        message.attach(html_part)
        
        await aiosmtplib.send(
            message,
            hostname=SMTP_HOST,
            port=SMTP_PORT,
            use_tls=True,  # Use SSL instead of STARTTLS for port 465
            username=SMTP_USERNAME,
            password=SMTP_PASSWORD,
        )
        
        print(f"✅ Test verification email {test_email} adresine gönderildi!")
        return True
        
    except Exception as e:
        print(f"❌ Test verification email gönderilemedi: {e}")
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
            use_tls=True,  # Use SSL instead of STARTTLS for port 465
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
        # 2. Welcome email test et
        await test_welcome_email()
        
        # 3. Verification email test et
        await test_verification_email()
        
        # 4. Forgot password flow'unu test et
        await test_forgot_password_flow()
    
    print("\n" + "=" * 50)
    if smtp_ok:
        print("🎉 SMTP konfigürasyonu çalışıyor!")
        print("Backend'de welcome, verification ve forgot password mailleri gönderebilir.")
    else:
        print("❌ SMTP konfigürasyonu düzeltilmeli.")
        print("Lütfen .env dosyasındaki SMTP bilgilerini kontrol edin.")

if __name__ == "__main__":
    asyncio.run(main())

