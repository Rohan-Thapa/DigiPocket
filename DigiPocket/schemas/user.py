from pydantic import BaseModel
from models.user import Tier

class UserResponse(BaseModel):
    id: str
    username: str
    tier: Tier
    disabled: bool

# As a schemas I am creating the request response here.