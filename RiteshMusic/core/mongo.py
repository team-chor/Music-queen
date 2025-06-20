#⟶̽ जय श्री ༢།म >𝟑🙏🚩

from motor.motor_asyncio import AsyncIOMotorClient

from config import MONGO_DB_URI

from ..logging import LOGGER

LOGGER(__name__).info("⏳ Establishing a secure link to your MongoDB database...")
try:
    _mongo_async_ = AsyncIOMotorClient(MONGO_DB_URI)
    mongodb = _mongo_async_.deadline
    LOGGER(__name__).info("✅ Successfully connected to MongoDB. All systems are ready!")
except:
    LOGGER(__name__).error("❌ MongoDB connection failed!")
    exit()
