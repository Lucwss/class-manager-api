from datetime import datetime
from typing import Any

from domain.entities.schedule import ScheduleInput, ScheduleOutput
from domain.interfaces.schedule_repository import IScheduleRepository
from domain.schemas import DefaultCreatedResponse
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

    async def find_all(self, page: int, page_size: int, search: Any=None):
        schedules: AgnosticCollection = MongoDatabase.db.get_collection("schedules")

        pipeline = [
            {
                "$lookup": {
                    "from": "students",
                    "localField": "student_id",
                    "foreignField": "_id",
                    "as": "student"
                }
            },
            {
                "$unwind": "$student"
            },
            {
                "$lookup": {
                    "from": "lecturers",
                    "localField": "lecturer_id",
                    "foreignField": "_id",
                    "as": "lecturer"
                }
            },
            {
                "$unwind": "$lecturer"
            },
        ]

        if page and page_size:
            pipeline.extend([
                {"$skip": (page - 1) * page_size},
                {"$limit": page_size}
            ])

        cursor = schedules.aggregate(pipeline)
        result = await cursor.to_list(length=None)

        if len(result) == 0:
            return []

        for schedule in result:
            schedule["student_id"] = str(schedule["student_id"])
            schedule["lecturer_id"] = str(schedule["lecturer_id"])

        return [ScheduleOutput(**schedule) for schedule in result]

    async def find_by_email(self, email: str) -> ScheduleOutput | None:
        pass

    async def create(self, schedule_input: ScheduleInput) -> DefaultCreatedResponse | None:
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

        return DefaultCreatedResponse()


    async def delete_all(self):
        pass

    async def delete_by_id(self, user_id: str):
        pass

    async def find_by_id(self, user_id: str):
        pass