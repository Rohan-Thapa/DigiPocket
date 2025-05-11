from fastapi import APIRouter, Depends
from schemas.wallet import BalanceResponse
from dependencies import get_current_active_user
from service.wallet_service import WalletService

router = APIRouter(prefix="/wallet", tags=["wallet"])

@router.get("/balance", response_model=BalanceResponse)
async def balance(user=Depends(get_current_active_user)):
    return await WalletService().get_balance(user.id)