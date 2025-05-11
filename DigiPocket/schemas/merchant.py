from pydantic import BaseModel

class MerchantSignupRequest(BaseModel):
    name: str
    password: str

class MerchantLoginRequest(BaseModel):
    name: str
    password: str

class MerchantResponse(BaseModel):
    id: str
    name: str
    disabled: bool

class MerchantTokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

# As a schemas I am creating the request response here.