from datetime import datetime

from domain.entities.student import StudentInput, StudentOutput
from domain.interfaces.student_repository import IStudentRepository
from infra.databases.mongodatabase import MongoDatabase
from motor.core import AgnosticCollection
from bson.objectid import ObjectId

from pymongo.results import (
    InsertOneResult
)

class StudentRepository(IStudentRepository):
    """ Class implementation for IStudentRepository with all methods """

    async def count_all_students(self):
        return await MongoDatabase.db.get_collection("students").count_documents({})

    async def find_all(self, page: int, page_size: int):
        pass

    async def find_by_email(self, email: str) -> StudentOutput | None:
        students: AgnosticCollection = MongoDatabase.db.get_collection("students")

        student = await students.find_one({"email": email})

        if not student:
            return None

        return StudentOutput(**student)

    async def create(self, student_input: StudentInput) -> StudentOutput | None:
        students: AgnosticCollection = MongoDatabase.db.get_collection("students")
        dict_parsed_student = student_input.model_dump()

        dict_parsed_student["updated_at"] = datetime.now()
        dict_parsed_student["created_at"] = datetime.now()

        inserted: InsertOneResult = await students.insert_one(dict_parsed_student)

        inserted_id = inserted.inserted_id

        if not inserted_id:
            return None

        inserted_student = await students.find_one({"_id": ObjectId(inserted_id)})
        return StudentOutput(**inserted_student)


    async def delete_all(self):
        pass

    async def delete_by_id(self, user_id: str):
        pass

    async def find_by_id(self, student_id: str):
        students: AgnosticCollection = MongoDatabase.db.get_collection("students")

        student = await students.find_one({"_id": ObjectId(student_id)})

        if not student:
            return None

        return StudentOutput(**student)