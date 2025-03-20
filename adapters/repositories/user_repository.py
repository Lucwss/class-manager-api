from datetime import datetime

from domain.entities.user import UserInput, UserOutput
from domain.interfaces.user_repository import IUserRepository
from infra.databases.mongodatabase import MongoDatabase
from motor.core import AgnosticCollection
from bson.objectid import ObjectId

from pymongo.results import (
    InsertOneResult
)

class UserRepository(IUserRepository):
    """ Class implementation for IUserRepository with all methods """

    async def count_all_users(self):
        return await MongoDatabase.db.get_collection("users").count_documents({})

    async def find_all(self, page: int, page_size: int):
        pass

    async def find_by_email(self, email: str) -> UserOutput | None:
        users: AgnosticCollection = MongoDatabase.db.get_collection("users")

        user = await users.find_one({"email": email})

        if not user:
            return None

        return UserOutput(**user)

    async def create(self, user_input: UserInput) -> UserOutput | None:
        users: AgnosticCollection = MongoDatabase.db.get_collection("users")
        dict_parsed_user = user_input.model_dump()

        dict_parsed_user["updated_at"] = datetime.now()
        dict_parsed_user["created_at"] = datetime.now()

        inserted: InsertOneResult = await users.insert_one(dict_parsed_user)

        inserted_id = inserted.inserted_id

        if not inserted_id:
            return None

        inserted_user = await users.find_one({"_id": ObjectId(inserted_id)})
        return UserOutput(**inserted_user)


    async def delete_all(self):
        pass

    async def delete_by_id(self, user_id: str):
        pass

    async def find_by_id(self, user_id: str):
        users: AgnosticCollection = MongoDatabase.db.get_collection("users")

        user = await users.find_one({"_id": ObjectId(user_id)})

        if not user:
            return None

        return UserOutput(**user)