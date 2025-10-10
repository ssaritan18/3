# Overview

ADHDers Social Club is a full-stack social networking application designed specifically for people with ADHD. The platform provides task management, real-time chat, community features, mood tracking, and gamification elements to help users stay organized and connected. The application is built with a React Native/Expo frontend and a FastAPI Python backend, using MongoDB for data persistence.

# User Preferences

Preferred communication style: Simple, everyday language.

# System Architecture

## Frontend Architecture

**Framework**: React Native with Expo SDK ~53.0.0
- **Routing**: Expo Router for file-based navigation
- **State Management**: React Context API for global state (Auth, Tasks, Friends, Chat, Community, Mood, Subscription)
- **UI Components**: React Native Paper with custom Material Design 3 theming
- **Real-time Communication**: WebSocket connections with polling fallback for chat and presence updates
- **Storage**: Multiple strategies including AsyncStorage, SecureStore, localStorage, and sessionStorage for token persistence

**Key Design Patterns**:
- Context providers for cross-cutting concerns (authentication, real-time data, subscriptions)
- Custom hooks for reusable logic (useStreak, useAchievements, useSubscription)
- Error boundaries for graceful error handling
- Gesture handling via react-native-gesture-handler

**Authentication Flow**:
- JWT-based authentication with token stored in multiple locations for reliability
- Automatic token refresh mechanism
- OAuth integration with Google Sign-In
- Offline/demo mode support for testing

## Backend Architecture

**Framework**: FastAPI (Python)
- **Database**: MongoDB with Motor async driver
- **Authentication**: JWT tokens with bcrypt password hashing
- **Real-time**: WebSocket support for chat and presence updates
- **File Storage**: Local filesystem for media uploads
- **Email**: SMTP integration for notifications and verification

**API Structure**:
- RESTful endpoints organized by feature domain (auth, tasks, chat, friends, community, mood, subscriptions)
- WebSocket endpoint for real-time bidirectional communication
- Rate limiting (100 requests/minute) to prevent abuse
- CORS middleware for cross-origin requests

**Key Features**:
- Task management with progress tracking
- Friend system with request/accept flow
- Group and direct chat with media upload support
- Community posts with replies and reactions
- Mood tracking and analytics
- Achievement/gamification system
- Subscription management (free tier with ad-supported model)
- User blocking and account deletion (Google Play compliance)

**Security Measures**:
- Password hashing with bcrypt
- JWT token validation on protected endpoints
- Input validation with Pydantic models
- File upload size limits and type validation

## External Dependencies

**Third-Party Services**:
- **Google OAuth**: User authentication via Google Sign-In
- **SMTP Service**: Email notifications (configurable Gmail or custom SMTP)
- **MongoDB Atlas**: Production database hosting (optional, supports local MongoDB)

**Mobile Platform Integration**:
- **Expo Application Services (EAS)**: Build and deployment for iOS/Android
- **Apple App Store**: iOS distribution (bundle ID: com.adhders.socialclub)
- **Google Play Store**: Android distribution (package: com.adhders.socialclub)
- **In-App Purchases**: Subscription management (mocked in development, ready for production)
- **AdMob**: Ad serving for free tier users (mocked in development)

**Development Services**:
- **Expo Go**: Development and testing on physical devices
- **Expo Router**: File-based routing and navigation
- **React Native Reanimated**: Smooth animations and gestures

**Database Schema**:
- Users collection (authentication, profiles, settings)
- Tasks collection (user tasks with progress tracking)
- Chats collection (group and direct messages)
- Messages collection (chat messages with media support)
- Posts collection (community posts)
- Comments collection (post replies)
- Friend requests collection (friendship system)
- Mood logs collection (mood tracking data)
- Achievements collection (gamification system)
- Subscriptions collection (payment tracking)
- Reports collection (user reporting system)
- Blocked users collection (user blocking)
- Deletion requests collection (account deletion tracking)

**Environment Configuration**:
- Backend requires: MONGO_URL, JWT_SECRET, SMTP credentials, Google OAuth client ID
- Frontend requires: EXPO_PUBLIC_BACKEND_URL, Google OAuth client IDs (web, iOS, Android)
- Supports development, preview, and production environments with different configurations