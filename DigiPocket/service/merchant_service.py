from repository.merchant_repo import MerchantRepository
from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta
from schemas.merchant import MerchantSignupRequest, MerchantLoginRequest, MerchantTokenResponse
from dependencies import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES

pwd_ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")

class MerchantService:
    def __init__(self):
        self.repo = MerchantRepository()

    async def signup(self, req: MerchantSignupRequest) -> MerchantTokenResponse:
        if await self.repo.get_by_name(req.name):
            raise ValueError("Merchant name taken")
        hashed = pwd_ctx.hash(req.password)
        await self.repo.create({"name": req.name, "hashed_password": hashed, "disabled": False})
        token = self._create_token(req.name)
        return MerchantTokenResponse(access_token=token)

    async def login(self, req: MerchantLoginRequest) -> MerchantTokenResponse:
        data = await self.repo.get_by_name(req.name)
        if not data or not pwd_ctx.verify(req.password, data["hashed_password"]):
            return None
        token = self._create_token(req.name)
        return MerchantTokenResponse(access_token=token)

    def _create_token(self, subject: str) -> str:
        to_encode = {"sub": subject, "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)}
        return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
