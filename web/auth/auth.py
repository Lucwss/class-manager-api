from typing import Annotated

from fastapi import APIRouter, Depends, Body
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm

auth_router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@auth_router.post('/sign-in/', summary="Route for authenticating user in the System.")
async def sign_in(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
):
    """
    This method is used to authenticate user by a decorated Fast API route.
    :param form_data: necessary information for authentication

    """
    return JSONResponse(content={}, status_code=200)

@auth_router.post('/sign-up/', summary='Route for registering user in the System.')
async def sign_up(
        user_input: Annotated[dict, Body(...)]
):
    """
    This method is used to register user by a decorated Fast API route.
    :param user_input: user information to be stored.
    :param use_case: use case class for registration the user. (execute)
    :return:
    """

    return JSONResponse(content={}, status_code=201)