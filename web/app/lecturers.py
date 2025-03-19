from typing import Annotated

from fastapi import APIRouter, Body, Depends
from fastapi.responses import JSONResponse

from application.usecases.create_lecturer import CreateLecturerUseCase
from domain.entities.lecturer import LecturerInput
from web.dependencies import create_lecturer_use_case

lecturers_router = APIRouter(
    prefix="/lecturers",
    tags=["Lecturers"],
)

@lecturers_router.post('/', summary='Route for creation of a lecturer.')
async def create_lecturer(
    lecturer_input: Annotated[LecturerInput, Body(...)],
    use_case: Annotated[CreateLecturerUseCase, Depends(create_lecturer_use_case)]
):
    response = await use_case.execute(lecturer_input=lecturer_input)
    return JSONResponse(content=response.model_dump(), status_code=response.status_code)
