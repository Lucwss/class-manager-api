from typing import Annotated
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from adapters.libs.bcrypt import BcryptAdapter
from adapters.repositories.lecturer_repository import LecturerRepository
from adapters.repositories.schedule_repository import ScheduleRepository
from adapters.repositories.student_repository import StudentRepository
from adapters.repositories.user_repository import UserRepository
from application.usecases.create_lecturer import CreateLecturerUseCase
from application.usecases.create_schedule import CreateScheduleUseCase
from application.usecases.create_student import CreateStudentUseCase
from application.usecases.create_user import CreateUserUseCase
from application.usecases.get_schedule_summary import GetScheduleUseCase
from application.usecases.sign_in import SignInUseCase


def student_repository():
    """
    function that injects the dependencies for StudentRepository
    """

    return StudentRepository()

def user_repository():
    """
    function that injects the dependencies for UserRepository
    """

    return UserRepository()


def lecturer_repository():
    """
    function that injects the dependencies for LecturerRepository
    """

    return LecturerRepository()

def schedule_repository():
    """
    function that injects the dependencies for ScheduleRepository
    """

    return ScheduleRepository()

def sign_in_use_case(repository: Annotated[UserRepository, Depends(user_repository)]) -> SignInUseCase:
    """
    function that injects the dependencies for SignInUseCase
    """

    return SignInUseCase(repository)

def jwt_encoder() -> BcryptAdapter:
    """
    function that injects the dependencies for JwtEncoder
    """

    return BcryptAdapter()

def get_token(
    token: Annotated[str, Depends(OAuth2PasswordBearer(tokenUrl="api/v1/auth/sign-in/"))],
) -> str:
    """
    function that injects the dependencies for token
    """

    return token

def create_student_use_case(
        repository: Annotated[StudentRepository, Depends(student_repository)],
        encoder: Annotated[BcryptAdapter, Depends(jwt_encoder)],
) -> CreateStudentUseCase:
    """
    function that injects the dependencies for CreateUserUseCase
    """

    return CreateStudentUseCase(repository, encoder)

def create_user_use_case(
        repository: Annotated[UserRepository, Depends(user_repository)],
        encoder: Annotated[BcryptAdapter, Depends(jwt_encoder)],
) -> CreateUserUseCase:
    """
    function that injects the dependencies for CreateUserUseCase
    """

    return CreateUserUseCase(repository, encoder)

def create_lecturer_use_case(
        repository: Annotated[LecturerRepository, Depends(lecturer_repository)],
) -> CreateLecturerUseCase:
    """
    function that injects the dependencies for CreateUserUseCase
    """

    return CreateLecturerUseCase(repository)

def create_schedule_use_case(
        repository: Annotated[ScheduleRepository, Depends(schedule_repository)],
        student_repo: Annotated[StudentRepository, Depends(student_repository)],
        lecturer_repo: Annotated[LecturerRepository, Depends(lecturer_repository)],

) -> CreateScheduleUseCase:
    """
    function that injects the dependencies for CreateScheduleUseCase
    """

    return CreateScheduleUseCase(repository, student_repo, lecturer_repo)

def get_schedule_summary_use_case(
        repository: Annotated[ScheduleRepository, Depends(schedule_repository)],
) -> GetScheduleUseCase:
    """
    function that injects the dependencies for GetScheduleUseCase
    """

    return GetScheduleUseCase(repository)