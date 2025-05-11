from config.database import get_db

class TransactionRepository:
    def __init__(self):
        self.collection = get_db()["transactions"]

    async def create(self, data: dict) -> str:
        res = await self.collection.insert_one(data)
        return str(res.inserted_id)

    async def list_by_wallet(self, wid: str) -> list:
        cur = self.collection.find({"wallet_id": wid}).sort("timestamp", -1)
        return await cur.to_list(100)
