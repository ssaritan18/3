"""
Google Authentication Service
Handles Google ID token verification and user authentication
"""

import os
import logging
from typing import Optional, Dict, Any
from google.auth.transport import requests
from google.oauth2 import id_token
from google.auth.exceptions import GoogleAuthError

logger = logging.getLogger(__name__)

class GoogleAuthService:
    """Service for verifying Google ID tokens and extracting user information"""
    
    def __init__(self):
        # Get Google OAuth client ID from environment
        self.client_id = os.getenv('GOOGLE_CLIENT_ID')
        if not self.client_id:
            logger.warning("GOOGLE_CLIENT_ID not set in environment variables")
    
    async def verify_id_token(self, id_token_string: str) -> Optional[Dict[str, Any]]:
        """
        Verify Google ID token and extract user information
        
        Args:
            id_token_string: The Google ID token from the client
            
        Returns:
            Dict containing user information if token is valid, None otherwise
        """
        try:
            if not self.client_id:
                logger.error("Google OAuth client ID not configured")
                return None
            
            # Verify the token
            idinfo = id_token.verify_oauth2_token(
                id_token_string, 
                requests.Request(), 
                self.client_id
            )
            
            # Check if the token is from the correct issuer
            if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
                logger.error(f"Invalid token issuer: {idinfo['iss']}")
                return None
            
            # Extract user information
            user_info = {
                'google_id': idinfo['sub'],
                'email': idinfo['email'],
                'name': idinfo.get('name', ''),
                'picture': idinfo.get('picture', ''),
                'email_verified': idinfo.get('email_verified', False),
                'given_name': idinfo.get('given_name', ''),
                'family_name': idinfo.get('family_name', ''),
            }
            
            logger.info(f"Google token verified for user: {user_info['email']}")
            return user_info
            
        except ValueError as e:
            logger.error(f"Invalid Google ID token: {e}")
            return None
        except GoogleAuthError as e:
            logger.error(f"Google authentication error: {e}")
            return None
        except Exception as e:
            logger.error(f"Unexpected error verifying Google token: {e}")
            return None
    
    def is_email_verified(self, user_info: Dict[str, Any]) -> bool:
        """Check if the user's email is verified by Google"""
        return user_info.get('email_verified', False)
    
    def extract_user_data(self, user_info: Dict[str, Any]) -> Dict[str, Any]:
        """Extract relevant user data for our application"""
        return {
            'google_id': user_info['google_id'],
            'email': user_info['email'],
            'name': user_info['name'],
            'profile_picture': user_info['picture'],
            'email_verified': user_info['email_verified'],
            'first_name': user_info.get('given_name', ''),
            'last_name': user_info.get('family_name', ''),
        }

# Singleton instance
google_auth_service = GoogleAuthService()
