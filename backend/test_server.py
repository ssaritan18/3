from fastapi import FastAPI
from contextlib import asynccontextmanager

# Mock database for testing
class MockDB:
    def __getitem__(self, name):
        return self
    def find_one(self, *args, **kwargs):
        return None
    def insert_one(self, *args, **kwargs):
        return type('obj', (object,), {'inserted_id': 'mock_id'})()
    def find(self, *args, **kwargs):
        return []
    def update_one(self, *args, **kwargs):
        return type('obj', (object,), {'modified_count': 1})()
    def delete_one(self, *args, **kwargs):
        return type('obj', (object,), {'deleted_count': 1})()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    global db
    print("🚀 Starting server without MongoDB for testing...")
    db = MockDB()
    print("✅ Using mock database for testing - NO MONGODB!")
    yield
    # shutdown
    print("✅ Server shutdown complete")

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def root():
    return {"message": "ADHDers Backend API is running!", "status": "ok"}

@app.get("/api/test")
async def test():
    return {"message": "API is working!", "status": "ok"}

@app.post("/api/auth/register")
async def register(data: dict):
    print(f"📝 Registration attempt: {data}")
    return {"message": "Registration successful! (Mock)", "status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
