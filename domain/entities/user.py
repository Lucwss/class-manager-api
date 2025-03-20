from datetime import datetime

from pydantic import BaseModel, EmailStr, Field, ConfigDict
from bson.objectid import ObjectId

class UserInput(BaseModel):
    """
    User model representing a user in the application with additional fields for input.
    """

    username: str = Field(max_length=100, min_length=5)
    email: EmailStr
    password: str = Field(max_length=100, min_length=6)


class UserOutput(UserInput):
    """
    User model representing a user in the application with additional fields for output.
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