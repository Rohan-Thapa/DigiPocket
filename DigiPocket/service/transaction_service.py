from repository.transaction_repo import TransactionRepository
from repository.wallet_repo import WalletRepository
from fastapi import HTTPException, status

class TransactionService:
    def __init__(self):
        self.txn_repo = TransactionRepository()
        self.wallet_repo = WalletRepository()

    async def transfer(self, frm: str, to: str, amt: float) -> str:
        w_from = await self.wallet_repo.get_by_user(frm)
        w_to = await self.wallet_repo.get_by_user(to)
        if not w_to:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Recipient not found")
        if amt > w_from["balance"] + w_from["limit"]:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Amount exceeds tier limit")
        new_from = w_from["balance"] - amt
        new_to = w_to["balance"] + amt
        await self.wallet_repo.update(str(w_from["_id"]), {"balance": new_from})
        await self.wallet_repo.update(str(w_to["_id"]), {"balance": new_to})
        await self.txn_repo.create({"wallet_id": str(w_from["_id"]), "amount": -amt})
        return await self.txn_repo.create({"wallet_id": str(w_to["_id"]), "amount": amt})