from fastapi import APIRouter, Depends
from schemas.user import UserResponse
from dependencies import get_current_active_user
from service.user_service import UserService

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/me", response_model=UserResponse)
async def me(user=Depends(get_current_active_user)):
    return await UserService().get_profile(user.username)
