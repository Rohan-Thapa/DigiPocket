from fastapi import APIRouter, Depends
from schemas.wallet import TransferRequest
from dependencies import get_current_active_user
from service.transaction_service import TransactionService

router = APIRouter(prefix="/transactions", tags=["transactions"])

@router.post("/transfer", response_model=dict)
async def transfer(req: TransferRequest, user=Depends(get_current_active_user)):
    txn_id = await TransactionService().transfer(user.username, req.to_username, req.amount)
    return {"transaction_id": txn_id}