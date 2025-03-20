from typing import Annotated

from fastapi import APIRouter, Depends, Body
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm

from application.usecases.create_user import CreateUserUseCase
from application.usecases.sign_in import SignInUseCase
from domain.entities.user import UserInput
from web.dependencies import create_user_use_case, sign_in_use_case

auth_router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@auth_router.post('/sign-in/', summary="Route for authenticating user in the System.")
async def sign_in(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    use_case: Annotated[SignInUseCase, Depends(sign_in_use_case)]
):
    """
    This method is used to authenticate user by a decorated Fast API route.
    :param use_case:
    :param form_data: necessary information for authentication

    """
    response = await use_case.execute(form_data)
    status_code = response.status_code

    if response.status_code == 200:
        response = response.payload
    else:
        response = response.model_dump()

    return JSONResponse(content=response, status_code=status_code)

@auth_router.post('/sign-up/', summary='Route for registering user in the System.')
async def sign_up(
        user_input: Annotated[UserInput, Body(...)],
        use_case: Annotated[CreateUserUseCase, Depends(create_user_use_case)]
):
    """
    This method is used to register user by a decorated Fast API route.
    :param user_input: user information to be stored.
    :param use_case: use case class for registration the user. (execute)
    :return:
    """

    response = await use_case.execute(user_input)
    return JSONResponse(content=response.model_dump(), status_code=response.status_code)