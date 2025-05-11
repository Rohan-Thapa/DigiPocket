from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from models.user import User
from models.merchant import Merchant
from repository.user_repo import UserRepository
from repository.merchant_repo import MerchantRepository
# from dependencies import SECRET_KEY, ALGORITHM

oauth2_user = OAuth2PasswordBearer(tokenUrl="/auth/login")
oauth2_merchant = OAuth2PasswordBearer(tokenUrl="/merchant/login")

SECRET_KEY = "AVeryLongSecretKeyForSecrecyAuthentication"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

async def get_current_user(token: str = Depends(oauth2_user)) -> User:
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials", headers={"WWW-Authenticate":"Bearer"})
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if not username:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    data = await UserRepository().get_by_username(username)
    if not data:
        raise credentials_exception
    return User(**data)

async def get_current_active_user(current: User = Depends(get_current_user)) -> User:
    if current.disabled:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Inactive user")
    return current

async def get_current_merchant(token: str = Depends(oauth2_merchant)) -> Merchant:
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials", headers={"WWW-Authenticate":"Bearer"})
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        name = payload.get("sub")
        if not name:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    data = await MerchantRepository().get_by_name(name)
    if not data:
        raise credentials_exception
    return Merchant(**data)
