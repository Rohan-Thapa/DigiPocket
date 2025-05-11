from config.database import get_db
from bson import ObjectId

class UserRepository:
    def __init__(self):
        self.collection = get_db()["users"]

    async def create(self, data: dict) -> str:
        res = await self.collection.insert_one(data)
        return str(res.inserted_id)

    async def get_by_username(self, username: str) -> dict:
        return await self.collection.find_one({"username": username})

    async def get_by_id(self, uid: str) -> dict:
        return await self.collection.find_one({"_id": ObjectId(uid)})
