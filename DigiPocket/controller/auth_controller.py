from fastapi import APIRouter, HTTPException, status
from schemas.auth import SignupRequest, LoginRequest, TokenResponse
from service.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/signup", response_model=TokenResponse)
async def signup(req: SignupRequest):
    try:
        return await AuthService().signup(req)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.post("/login", response_model=TokenResponse)
async def login(req: LoginRequest):
    token = await AuthService().login(req)
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    return token
