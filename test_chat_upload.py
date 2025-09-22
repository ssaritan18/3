import requests
import json
import time

# Test user registration and chat message with media
BASE_URL = "http://localhost:8000/api"

def test_chat_upload():
    print("🧪 Testing chat upload functionality...")
    
    # 1. Register test user
    print("1. Registering test user...")
    register_data = {
        "email": "test@example.com",
        "password": "test123",
        "name": "Test User"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/auth/register", json=register_data)
        if response.status_code == 200:
            print("✅ User registered successfully")
            user_data = response.json()
            token = user_data.get("token")
        else:
            print(f"❌ Registration failed: {response.status_code} - {response.text}")
            return
    except Exception as e:
        print(f"❌ Registration error: {e}")
        return
    
    # 2. Get chats (this should create adhd_support chat)
    print("2. Getting chats...")
    headers = {"Authorization": f"Bearer {token}"}
    
    try:
        response = requests.get(f"{BASE_URL}/chats", headers=headers)
        if response.status_code == 200:
            chats = response.json().get("chats", [])
            print(f"✅ Found {len(chats)} chats")
            
            # Find adhd_support chat
            adhd_chat = None
            for chat in chats:
                if chat.get("_id") == "adhd_support":
                    adhd_chat = chat
                    break
            
            if adhd_chat:
                print("✅ Found adhd_support chat")
            else:
                print("❌ adhd_support chat not found")
                return
        else:
            print(f"❌ Failed to get chats: {response.status_code} - {response.text}")
            return
    except Exception as e:
        print(f"❌ Get chats error: {e}")
        return
    
    # 3. Send a text message to adhd_support
    print("3. Sending text message...")
    message_data = {
        "text": "Hello from test!",
        "type": "text"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/chats/adhd_support/messages", 
                               json=message_data, headers=headers)
        if response.status_code == 200:
            print("✅ Text message sent successfully")
            message_result = response.json()
            print(f"Message ID: {message_result.get('message_id')}")
        else:
            print(f"❌ Failed to send message: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"❌ Send message error: {e}")
    
    # 4. Test media upload
    print("4. Testing media upload...")
    
    # Create a simple test image (1x1 pixel PNG)
    test_image_data = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x02\x00\x00\x00\x90wS\xde\x00\x00\x00\tpHYs\x00\x00\x0b\x13\x00\x00\x0b\x13\x01\x00\x9a\x9c\x18\x00\x00\x00\nIDATx\x9cc```\x00\x00\x00\x04\x00\x01\xdd\x8d\xb4\x1c\x00\x00\x00\x00IEND\xaeB`\x82'
    
    files = {
        'file': ('test.png', test_image_data, 'image/png')
    }
    
    try:
        response = requests.post(f"{BASE_URL}/chats/adhd_support/upload", 
                               files=files, headers=headers)
        if response.status_code == 200:
            print("✅ Media upload successful")
            upload_result = response.json()
            print(f"Media URL: {upload_result.get('media_url')}")
            print(f"File type: {upload_result.get('file_type')}")
            print(f"File size: {upload_result.get('file_size')}")
            
            # 5. Send message with media
            print("5. Sending message with media...")
            media_message_data = {
                "text": "Here's a test image!",
                "type": "image",
                "media_url": upload_result.get('media_url')
            }
            
            response = requests.post(f"{BASE_URL}/chats/adhd_support/messages", 
                                   json=media_message_data, headers=headers)
            if response.status_code == 200:
                print("✅ Media message sent successfully")
                message_result = response.json()
                print(f"Message ID: {message_result.get('message_id')}")
            else:
                print(f"❌ Failed to send media message: {response.status_code} - {response.text}")
                
        else:
            print(f"❌ Media upload failed: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"❌ Media upload error: {e}")
    
    # 6. Test getting messages
    print("6. Getting messages...")
    try:
        response = requests.get(f"{BASE_URL}/chats/adhd_support/messages", headers=headers)
        if response.status_code == 200:
            messages = response.json().get("messages", [])
            print(f"✅ Found {len(messages)} messages")
            for msg in messages:
                print(f"  - {msg.get('type')}: {msg.get('text', '')[:50]}...")
        else:
            print(f"❌ Failed to get messages: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"❌ Get messages error: {e}")

if __name__ == "__main__":
    test_chat_upload()
