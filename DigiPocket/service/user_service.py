from repository.user_repo import UserRepository
from fastapi import HTTPException, status
from schemas.user import UserResponse

class UserService:
    def __init__(self):
        self.repo = UserRepository()

    async def get_profile(self, username: str) -> UserResponse:
        data = await self.repo.get_by_username(username)
        if not data:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        return UserResponse(id=str(data["_id"]), username=data["username"], tier=data["tier"], disabled=data["disabled"])
