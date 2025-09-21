# 🚀 Production Setup Guide

## Environment Variables Setup

### Backend (.env)
```bash
# JWT Secret Key (use a strong, random secret in production)
JWT_SECRET=your-super-secret-jwt-key-here

# MongoDB Connection URL
MONGO_URL=mongodb://localhost:27017/adhders

# Base URL for your application
BASE_URL=https://your-domain.com

# SMTP Configuration for email sending
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=your-email@gmail.com
SMTP_PASSWORD=your-app-password
SMTP_FROM_EMAIL=noreply@your-domain.com

# Upload directory for files
UPLOAD_DIR=./uploads
```

### Frontend (.env)
```bash
# Backend API URL
EXPO_PUBLIC_BACKEND_URL=https://your-backend-domain.com

# Google OAuth Client IDs
EXPO_PUBLIC_GOOGLE_WEB_CLIENT_ID=your-google-web-client-id
EXPO_PUBLIC_GOOGLE_IOS_CLIENT_ID=your-google-ios-client-id
EXPO_PUBLIC_GOOGLE_ANDROID_CLIENT_ID=your-google-android-client-id
```

## Deployment Steps

### 1. Backend Deployment
```bash
cd backend
pip install -r requirements.txt
# Set environment variables
export JWT_SECRET="your-secret"
export MONGO_URL="your-mongodb-url"
# ... other variables
# Run server
python -m uvicorn server:app --host 0.0.0.0 --port 8000
```

### 2. Frontend Deployment
```bash
cd frontend
npm install
# Set environment variables
export EXPO_PUBLIC_BACKEND_URL="https://your-backend-domain.com"
# ... other variables
# Build for production
npm run build
# Deploy build folder to your hosting service
```

## Production Checklist

- [ ] Set up production MongoDB instance
- [ ] Configure SMTP service for emails
- [ ] Set up SSL certificates
- [ ] Configure domain names
- [ ] Set up monitoring and logging
- [ ] Configure backup strategy
- [ ] Set up CI/CD pipeline
- [ ] Test all features in staging
- [ ] Performance testing
- [ ] Security audit

## Monitoring

- Monitor API response times
- Track error rates
- Monitor database performance
- Set up alerts for critical issues
- Monitor user activity and engagement

## Security

- Use strong JWT secrets
- Enable HTTPS in production
- Regular security updates
- Monitor for suspicious activity
- Implement rate limiting
- Secure file uploads
