from datetime import datetime

from pydantic import BaseModel, Field, ConfigDict
from bson.objectid import ObjectId

from domain.entities.lecturer import LecturerOutput
from domain.entities.student import StudentOutput


class ScheduleInput(BaseModel):
    """
    Schedule model representing a appointment in the application with additional fields for input.
    """

    title: str = Field(max_length=100, min_length=5)
    description: str = Field(max_length=100, min_length=5)
    subject: str = Field(max_length=100, min_length=5)
    lecturer_id: str
    student_id: str

    model_config = ConfigDict(
        arbitrary_types_allowed=True
    )



class ScheduleOutput(ScheduleInput):
    """
    Schedule model representing a appointment in the application with additional fields for output.
    """

    id: ObjectId = Field(alias="_id")
    created_at: datetime
    updated_at: datetime
    lecturer: LecturerOutput
    student: StudentOutput

    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        json_encoders={
            datetime: lambda v: v.isoformat().replace("+00:00", "Z"),
            ObjectId: lambda v: str(v)
        },
    )