"""
Basic FastAPI application with security best practices
"""
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import uvicorn
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="DevHub API",
    description="Secure FastAPI application example",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Security
security = HTTPBearer()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://yourdomain.com"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

# Pydantic models
class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: str = Field(..., regex=r'^[^@]+@[^@]+\.[^@]+$')

class UserResponse(BaseModel):
    id: int
    username: str
    email: str

# Dependency for authentication
async def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    # Implement your token verification logic here
    if not token or token != "valid-token":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return token

# Routes
@app.get("/")
async def root():
    return {"message": "Welcome to DevHub API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "devhub-api"}

@app.post("/users", response_model=UserResponse)
async def create_user(
    user: UserCreate,
    token: str = Depends(verify_token)
):
    # Mock user creation
    logger.info(f"Creating user: {user.username}")
    return UserResponse(
        id=1,
        username=user.username,
        email=user.email
    )

@app.get("/users/{user_id}", response_model=UserResponse)
async def get_user(
    user_id: int,
    token: str = Depends(verify_token)
):
    if user_id <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid user ID"
        )
    
    # Mock user retrieval
    return UserResponse(
        id=user_id,
        username="john_doe",
        email="john@example.com"
    )

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )