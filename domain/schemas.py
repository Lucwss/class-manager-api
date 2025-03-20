from pydantic import BaseModel

class DefaultCreatedResponse(BaseModel):
    message: str = "Created schedule successfully"