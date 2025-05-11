from pydantic import BaseModel, Field
from typing import Optional

class Merchant(BaseModel):
    id: Optional[str] = Field(alias="_id")
    name: str
    hashed_password: str
    disabled: bool = False

    class Config:
        allow_population_by_field_name = True
        json_encoders = {"_id": str}