from motor.motor_asyncio import AsyncIOMotorClient
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    mongo_uri: str = "mongodb://localhost:27017"
    db_name: str = "digital_wallet"

settings = Settings()
client = None

def connect_db():
    global client
    client = AsyncIOMotorClient(settings.mongo_uri)

def close_db():
    client.close()

def get_db():
    return client[settings.db_name]
