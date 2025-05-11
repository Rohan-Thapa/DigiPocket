from repository.wallet_repo import WalletRepository
from fastapi import HTTPException, status
from schemas.wallet import BalanceResponse

class WalletService:
    def __init__(self):
        self.repo = WalletRepository()

    async def get_balance(self, user_id: str) -> BalanceResponse:
        w = await self.repo.get_by_user(user_id)
        if not w:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Wallet not found")
        return BalanceResponse(balance=w["balance"], limit=w["limit"])
