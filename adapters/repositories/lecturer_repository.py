from datetime import datetime

from domain.entities.lecturer import LecturerInput, LecturerOutput
from domain.interfaces.lecturer_repository import ILecturerRepository
from infra.databases.mongodatabase import MongoDatabase
from motor.core import AgnosticCollection
from bson.objectid import ObjectId

from pymongo.results import (
    InsertOneResult
)

class LecturerRepository(ILecturerRepository):
    """ Class implementation for ILecturerRepository with all methods """

    async def count_all_lecturer(self):
        return await MongoDatabase.db.get_collection("lecturers").count_documents({})

    async def find_all(self, page: int, page_size: int):
        pass

    async def find_by_email(self, email: str) -> LecturerOutput | None:
        lecturers: AgnosticCollection = MongoDatabase.db.get_collection("lecturers")

        lecturer = await lecturers.find_one({"email": email})

        if not lecturer:
            return None

        return LecturerOutput(**lecturer)

    async def create(self, lecturer_input: LecturerInput) -> LecturerOutput | None:
        lecturers: AgnosticCollection = MongoDatabase.db.get_collection("lecturers")

        dict_parsed_lecturer = lecturer_input.model_dump()
        dict_parsed_lecturer["updated_at"] = datetime.now()
        dict_parsed_lecturer["created_at"] = datetime.now()

        inserted: InsertOneResult = await lecturers.insert_one(dict_parsed_lecturer)

        inserted_id = inserted.inserted_id

        if not inserted_id:
            return None

        inserted_student = await lecturers.find_one({"_id": ObjectId(inserted_id)})
        return LecturerOutput(**inserted_student)


    async def delete_all(self):
        pass

    async def delete_by_id(self, user_id: str):
        pass

    async def find_by_id(self, lecturer_id: str):
        lecturers: AgnosticCollection = MongoDatabase.db.get_collection("lecturers")

        lecturer = await lecturers.find_one({"_id": ObjectId(lecturer_id)})

        if not lecturer:
            return None

        return LecturerOutput(**lecturer)