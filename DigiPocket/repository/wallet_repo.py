from config.database import get_db
from bson import ObjectId

class WalletRepository:
    def __init__(self):
        self.collection = get_db()["wallets"]

    async def create(self, data: dict) -> str:
        res = await self.collection.insert_one(data)
        return str(res.inserted_id)

    async def get_by_user(self, user_id: str) -> dict:
        return await self.collection.find_one({"user_id": user_id})

    async def update(self, wid: str, data: dict):
        await self.collection.update_one({"_id": ObjectId(wid)}, {"$set": data})
