from typing import Annotated
from fastapi import Depends

from adapters.libs.bcrypt import BcryptAdapter
from adapters.repositories.lecturer_repository import LecturerRepository
from adapters.repositories.student_repository import StudentRepository
from application.usecases.create_lecturer import CreateLecturerUseCase
from application.usecases.create_student import CreateStudentUseCase




def student_repository():
    """
    function that injects the dependencies for StudentRepository
    """

    return StudentRepository()

def lecturer_repository():
    """
    function that injects the dependencies for LecturerRepository
    """

    return LecturerRepository()

def jwt_encoder() -> BcryptAdapter:
    """
    function that injects the dependencies for JwtEncoder
    """

    return BcryptAdapter()

def create_student_use_case(
        repository: Annotated[StudentRepository, Depends(student_repository)],
        encoder: Annotated[BcryptAdapter, Depends(jwt_encoder)],
) -> CreateStudentUseCase:
    """
    function that injects the dependencies for CreateUserUseCase
    """

    return CreateStudentUseCase(repository, encoder)

def create_lecturer_use_case(
        repository: Annotated[LecturerRepository, Depends(lecturer_repository)],
) -> CreateLecturerUseCase:
    """
    function that injects the dependencies for CreateUserUseCase
    """

    return CreateLecturerUseCase(repository)