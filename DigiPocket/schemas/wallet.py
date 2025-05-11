from pydantic import BaseModel

class TransferRequest(BaseModel):
    to_username: str
    amount: float

class BalanceResponse(BaseModel):
    balance: float
    limit: float

# As a schemas I am creating the request response here.