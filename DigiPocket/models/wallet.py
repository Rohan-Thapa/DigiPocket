from pydantic import BaseModel, Field
from typing import Optional

class Wallet(BaseModel):
    id: Optional[str] = Field(alias="_id")
    user_id: str
    balance: float = 0.0
    limit: float

    class Config:
        allow_population_by_field_name = True
        json_encoders = {"_id": str}