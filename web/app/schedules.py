from typing import Annotated, Any

from fastapi import APIRouter, Body, Depends, Query
from fastapi.responses import JSONResponse

from application.usecases.create_schedule import CreateScheduleUseCase
from application.usecases.get_schedule_summary import GetScheduleUseCase
from domain.entities.schedule import ScheduleInput
from web.dependencies import create_schedule_use_case, get_schedule_summary_use_case

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

@schedules_router.get('/summary', summary='Route for checking schedules and appointments')
async def get_schedule_summary(
        use_case: Annotated[GetScheduleUseCase, Depends(get_schedule_summary_use_case)],
        search: Any = Query(None),
        page: int = Query(default=1),
        page_size: int = Query(default=10)
):
    response = await use_case.execute(page=page, page_size=page_size, search=search)
    return JSONResponse(content=response.model_dump(), status_code=response.status_code)
