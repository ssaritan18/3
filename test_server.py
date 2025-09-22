from fastapi import FastAPI, APIRouter, HTTPException, Depends, UploadFile, File
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
import uuid
import time
import os
from pathlib import Path
import json

# Mock data storage
users_db = {}
chats_db = {}
messages_db = {}

# Pydantic models
class UserCreate(BaseModel):
    email: str
    password: str
    name: str

class UserLogin(BaseModel):
    email: str
    password: str

class MessageCreate(BaseModel):
    text: str
    type: str = "text"
    media_url: Optional[str] = None

class User(BaseModel):
    _id: str
    email: str
    name: str

# Mock authentication
def get_current_user():
    # For testing, return a mock user
    return {"_id": "test-user-123", "email": "test@example.com", "name": "Test User"}

# Create FastAPI app
app = FastAPI(title="Test Chat Server")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API Router
api_router = APIRouter(prefix="/api")

# Auth endpoints
@api_router.post("/auth/register")
async def register(user_data: UserCreate):
    user_id = str(uuid.uuid4())
    user = {
        "_id": user_id,
        "email": user_data.email,
        "name": user_data.name,
        "password": user_data.password  # In real app, hash this
    }
    users_db[user_id] = user
    
    # Generate mock JWT token
    token = f"mock-token-{user_id}"
    
    return {
        "success": True,
        "user": user,
        "token": token
    }

@api_router.post("/auth/login")
async def login(login_data: UserLogin):
    # Find user by email
    user = None
    for u in users_db.values():
        if u["email"] == login_data.email:
            user = u
            break
    
    if not user or user["password"] != login_data.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    token = f"mock-token-{user['_id']}"
    return {
        "success": True,
        "user": user,
        "token": token
    }

# Chat endpoints
@api_router.get("/chats")
async def list_chats(user=Depends(get_current_user)):
    # Create adhd_support chat if it doesn't exist
    if "adhd_support" not in chats_db:
        chats_db["adhd_support"] = {
            "_id": "adhd_support",
            "type": "group",
            "title": "ADHD Support Group",
            "members": [user["_id"]],
            "invite_code": "ADHD01",
            "created_by": user["_id"],
            "created_at": time.time()
        }
    
    chats = list(chats_db.values())
    return {"chats": chats}

@api_router.get("/chats/{chat_id}/messages")
async def list_messages(chat_id: str, limit: int = 50, user=Depends(get_current_user)):
    if chat_id not in chats_db:
        raise HTTPException(status_code=404, detail="Chat not found")
    
    # Get messages for this chat
    chat_messages = [msg for msg in messages_db.values() if msg["chat_id"] == chat_id]
    chat_messages.sort(key=lambda x: x["created_at"], reverse=True)
    
    return {"messages": chat_messages[:limit]}

@api_router.post("/chats/{chat_id}/messages")
async def send_message(chat_id: str, payload: MessageCreate, user=Depends(get_current_user)):
    if chat_id not in chats_db:
        raise HTTPException(status_code=404, detail="Chat not found")
    
    message_id = str(uuid.uuid4())
    current_time = time.time()
    
    message = {
        "_id": message_id,
        "chat_id": chat_id,
        "author_id": user["_id"],
        "author_name": user["name"],
        "text": payload.text,
        "type": payload.type,
        "status": "sent",
        "reactions": {"like": 0, "heart": 0, "clap": 0, "star": 0},
        "created_at": current_time,
        "updated_at": current_time,
        "server_timestamp": current_time
    }
    
    if payload.media_url:
        message["media_url"] = payload.media_url
    
    messages_db[message_id] = message
    
    return {
        "success": True,
        "message_id": message_id,
        "message": message
    }

# Media upload endpoint
@api_router.post("/chats/{chat_id}/upload")
async def upload_chat_media(
    chat_id: str, 
    file: UploadFile = File(...),
    user=Depends(get_current_user)
):
    if chat_id not in chats_db:
        raise HTTPException(status_code=404, detail="Chat not found")
    
    # Create uploads directory
    upload_dir = Path("./uploads/chat")
    upload_dir.mkdir(parents=True, exist_ok=True)
    
    # Generate unique filename
    file_extension = Path(file.filename).suffix.lower()
    unique_filename = f"{chat_id}_{user['_id']}_{int(time.time())}{file_extension}"
    file_path = upload_dir / unique_filename
    
    # Write file
    content = await file.read()
    with open(file_path, "wb") as f:
        f.write(content)
    
    # Create media URL
    media_url = f"/uploads/chat/{unique_filename}"
    
    return {
        "success": True,
        "media_url": media_url,
        "file_type": file.content_type,
        "file_size": len(content),
        "filename": file.filename
    }

# Serve uploaded files
@api_router.get("/uploads/chat/{filename}")
async def get_chat_media(filename: str):
    file_path = Path("./uploads/chat") / filename
    
    if not file_path.exists():
        raise HTTPException(status_code=404, detail="Media file not found")
    
    # Determine media type
    file_ext = filename.lower().split('.')[-1]
    if file_ext in ['jpg', 'jpeg']:
        media_type = "image/jpeg"
    elif file_ext == 'png':
        media_type = "image/png"
    elif file_ext == 'webp':
        media_type = "image/webp"
    elif file_ext == 'gif':
        media_type = "image/gif"
    elif file_ext == 'mp4':
        media_type = "video/mp4"
    else:
        media_type = "application/octet-stream"
    
    return FileResponse(
        path=str(file_path),
        media_type=media_type,
        filename=filename
    )

# Include API router
app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
