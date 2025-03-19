import json
import traceback

from application.interfaces.usecase import UseCase
from domain.entities.student import StudentInput, StudentOutput
from domain.interfaces.encoders import IJwtEncoder
from domain.interfaces.student_repository import IStudentRepository
from web.http_helper import HttpResponse, HttpHelper


class CreateStudentUseCase(UseCase):
    """
    Use case for create a student in the system. (Implementing the UseCase interface).
    """

    def __init__(self, repository: IStudentRepository, encoder: IJwtEncoder):
        """
        Constructor assigning the repository attribute as a dependency repository. (Dependency Injection by constructor).
        """
        self.repository: IStudentRepository = repository
        self.encoder: IJwtEncoder = encoder

    async def execute(self, student_input: StudentInput) -> HttpResponse:
        """
        This method will store the user with provided data.
        :return: user information
        """
        try:
            hashed_password = self.encoder.get_password_hash(student_input.password)
            student_input.password = hashed_password

            inserted_student: StudentOutput = await self.repository.create(student_input)
            inserted_student = json.loads(inserted_student.model_dump_json())
            return HttpHelper.ok(inserted_student)

        except Exception as e:
            traceback.print_exc()
            return HttpHelper.internal_server_error(Exception(e))