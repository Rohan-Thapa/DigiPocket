from fastapi import APIRouter, HTTPException, status, Depends
from schemas.merchant import MerchantSignupRequest, MerchantLoginRequest, MerchantTokenResponse, MerchantResponse
from service.merchant_service import MerchantService
from dependencies import get_current_merchant

router = APIRouter(prefix="/merchant", tags=["merchant"])

@router.post("/signup", response_model=MerchantTokenResponse)
async def signup(req: MerchantSignupRequest):
    try:
        return await MerchantService().signup(req)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.post("/login", response_model=MerchantTokenResponse)
async def login(req: MerchantLoginRequest):
    token = await MerchantService().login(req)
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    return token

@router.get("/me", response_model=MerchantResponse)
async def me(merchant=Depends(get_current_merchant)):
    return merchant
