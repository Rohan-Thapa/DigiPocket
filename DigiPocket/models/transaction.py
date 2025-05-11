from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class Transaction(BaseModel):
    id: Optional[str] = Field(alias="_id")
    wallet_id: str
    amount: float
    timestamp: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        allow_population_by_field_name = True
        json_encoders = {"_id": str, "timestamp": lambda v: v.isoformat()}