from datetime import datetime

from domain.entities.schedule import ScheduleInput, ScheduleOutput
from domain.interfaces.schedule_repository import IScheduleRepository
from infra.databases.mongodatabase import MongoDatabase
from motor.core import AgnosticCollection
from bson.objectid import ObjectId

from pymongo.results import (
    InsertOneResult
)

class ScheduleRepository(IScheduleRepository):
    """ Class implementation for IScheduleRepository with all methods """

    async def count_all_schedules(self):
        return await MongoDatabase.db.get_collection("schedules").count_documents({})

    async def find_all(self, page: int, page_size: int):
        pass

    async def find_by_email(self, email: str) -> ScheduleOutput | None:
        pass

    async def create(self, schedule_input: ScheduleInput) -> ScheduleOutput | None:
        schedules: AgnosticCollection = MongoDatabase.db.get_collection("schedules")

        dict_parsed_schedule = schedule_input.model_dump()
        dict_parsed_schedule["updated_at"] = datetime.now()
        dict_parsed_schedule["created_at"] = datetime.now()
        dict_parsed_schedule["lecturer_id"] = ObjectId(dict_parsed_schedule["lecturer_id"])
        dict_parsed_schedule["student_id"] = ObjectId(dict_parsed_schedule["student_id"])

        inserted: InsertOneResult = await schedules.insert_one(dict_parsed_schedule)

        inserted_id = inserted.inserted_id

        if not inserted_id:
            return None

        inserted_student = await schedules.find_one({"_id": ObjectId(inserted_id)})

        inserted_student["lecturer_id"] = str(inserted_student["lecturer_id"])
        inserted_student["student_id"] = str(inserted_student["student_id"])

        return ScheduleOutput(**inserted_student)


    async def delete_all(self):
        pass

    async def delete_by_id(self, user_id: str):
        pass

    async def find_by_id(self, user_id: str):
        pass