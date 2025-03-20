from datetime import datetime
from pydantic import BaseModel, EmailStr, Field, ConfigDict
from bson.objectid import ObjectId

from domain.enums import Role


class LecturerInput(BaseModel):
    """
    Lecturer model representing a user in the application with additional fields for input.
    """

    username: str = Field(max_length=100, min_length=5)
    discipline: str = Field(max_length=100, min_length=5)
    email: EmailStr
    enrolment: str = Field(max_length=100, min_length=6)
    role: str = Field(default=Role.lecturer)



class LecturerOutput(LecturerInput):
    """
    Lecturer model representing a user in the application with additional fields for output.
    """

    id: ObjectId = Field(alias="_id")
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        json_encoders={
            datetime: lambda v: v.isoformat().replace("+00:00", "Z"),
            ObjectId: lambda v: str(v)
        },
    )