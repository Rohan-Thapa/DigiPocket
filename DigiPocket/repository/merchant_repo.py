from config.database import get_db
from bson import ObjectId

class MerchantRepository:
    def __init__(self):
        self.collection = get_db()["merchants"]

    async def create(self, data: dict) -> str:
        res = await self.collection.insert_one(data)
        return str(res.inserted_id)

    async def get_by_name(self, name: str) -> dict:
        return await self.collection.find_one({"name": name})

    async def get_by_id(self, mid: str) -> dict:
        return await self.collection.find_one({"_id": ObjectId(mid)})
