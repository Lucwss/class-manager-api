from typing import Annotated

from fastapi import APIRouter, Body, Depends
from fastapi.responses import JSONResponse

from application.usecases.create_schedule import CreateScheduleUseCase
from domain.entities.schedule import ScheduleInput
from web.dependencies import create_schedule_use_case

schedules_router = APIRouter(
    prefix="/schedules",
    tags=["Schedules"],
)

@schedules_router.post('/', summary='Route for creation of a schedule.')
async def create_schedule(
    schedule_input: Annotated[ScheduleInput, Body(...)],
    use_case: Annotated[CreateScheduleUseCase, Depends(create_schedule_use_case)]
):
    response = await use_case.execute(schedule_input=schedule_input)
    return JSONResponse(content=response.model_dump(), status_code=response.status_code)
