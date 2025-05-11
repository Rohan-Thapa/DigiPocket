from pydantic import BaseModel, constr
from models.user import Tier

class SignupRequest(BaseModel):
    username: constr(min_length=3)
    password: constr(min_length=6)
    tier: Tier

class LoginRequest(BaseModel):
    username: str
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    tier: Tier = None

# As a schemas I am creating the request response here.