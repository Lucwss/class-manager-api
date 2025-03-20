from typing import Annotated

from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse

from application.usecases.users_me import UsersMeUseCase
from web.dependencies import get_token, get_current_user_use_case

users_router = APIRouter(
    prefix="/users",
    tags=["Users"],
    dependencies=[
        Depends(get_token)
    ]
)

@users_router.get('/me/', summary='Route for getting user information.')
async def get_user_info(
        request: Request,
        use_case: Annotated[UsersMeUseCase, Depends(get_current_user_use_case)]
):
    """
    This method is used to get user information by a decorated Fast API route.
    :return:
    """
    token = request.headers['Authorization'].split(' ')[1]
    response = await use_case.execute(token)
    return JSONResponse(content=response.model_dump(), status_code=response.status_code)
