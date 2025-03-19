import os
from motor.core import AgnosticDatabase
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
class MongoDatabase:
    db: AgnosticDatabase

    @classmethod
    async def connect(cls):
        """ Establish connection to Mongo Database """
        host = os.getenv("MONGODB_HOST")
        port = int(os.getenv("MONGODB_PORT"))
        # user = os.getenv("MONGODB_USERNAME")
        # password = os.getenv("MONGODB_PASSWORD")
        database = os.getenv("MONGODB_DATABASE")

        client: AsyncIOMotorClient = AsyncIOMotorClient(
            host=host,
            port=port
        )

        cls.db: AsyncIOMotorDatabase = client.get_database(database)