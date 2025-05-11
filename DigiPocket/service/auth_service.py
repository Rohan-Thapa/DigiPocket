from repository.user_repo import UserRepository
from repository.wallet_repo import WalletRepository
from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta
from schemas.auth import SignupRequest, LoginRequest, TokenResponse
from service.tier_strategy import TierFactory
from dependencies import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES

pwd_ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")

class AuthService:
    def __init__(self):
        self.user_repo = UserRepository()
        self.wallet_repo = WalletRepository()

    async def signup(self, req: SignupRequest) -> TokenResponse:
        if await self.user_repo.get_by_username(req.username):
            raise ValueError("Username taken")
        hashed = pwd_ctx.hash(req.password)
        data = {"username": req.username, "hashed_password": hashed, "tier": req.tier.value, "disabled": False}
        user_id = await self.user_repo.create(data)
        strat = TierFactory.get_strategy(req.tier)
        limit = strat.get_limit()
        await self.wallet_repo.create({"user_id": user_id, "balance": 0.0, "limit": limit})
        token = self._create_token(req.username)
        return TokenResponse(access_token=token, tier=req.tier)

    async def login(self, req: LoginRequest) -> TokenResponse:
        data = await self.user_repo.get_by_username(req.username)
        if not data or not pwd_ctx.verify(req.password, data["hashed_password"]):
            return None
        tier = data["tier"]
        token = self._create_token(req.username)
        return TokenResponse(access_token=token, tier=tier)

    def _create_token(self, username: str) -> str:
        to_encode = {"sub": username, "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)}
        return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)