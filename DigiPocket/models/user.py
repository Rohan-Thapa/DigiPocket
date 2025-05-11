from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum

class Tier(str, Enum):
    BASIC = "BASIC"
    PREMIUM = "PREMIUM"

class User(BaseModel):
    id: Optional[str] = Field(alias="_id")
    username: str
    hashed_password: str
    tier: Tier
    disabled: bool = False

    class Config:
        allow_population_by_field_name = True
        json_encoders = {"_id": str}