from typing import Annotated

from fastapi import APIRouter, Body, Depends
from fastapi.responses import JSONResponse

from application.usecases.create_student import CreateStudentUseCase
from domain.entities.student import StudentInput
from web.dependencies import create_student_use_case, get_token

students_router = APIRouter(
    prefix="/students",
    tags=["Students"],
    dependencies=[
        Depends(get_token)
    ]
)

@students_router.post('/', summary='Route for creation of a student.')
async def create_student(
    student_input: Annotated[StudentInput, Body(...)],
    use_case: Annotated[CreateStudentUseCase, Depends(create_student_use_case)]
):
    response = await use_case.execute(student_input=student_input)
    return JSONResponse(content=response.model_dump(), status_code=response.status_code)
