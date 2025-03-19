import json
import traceback

from application.interfaces.usecase import UseCase
from domain.entities.lecturer import LecturerInput, LecturerOutput
from domain.interfaces.encoders import IJwtEncoder
from domain.interfaces.lecturer_repository import ILecturerRepository
from web.http_helper import HttpResponse, HttpHelper


class CreateLecturerUseCase(UseCase):
    """
    Use case for create a lecturer in the system. (Implementing the UseCase interface).
    """

    def __init__(self, repository: ILecturerRepository):
        """
        Constructor assigning the repository attribute as a dependency repository. (Dependency Injection by constructor).
        """
        self.repository: ILecturerRepository = repository

    async def execute(self, lecturer_input: LecturerInput) -> HttpResponse:
        """
        This method will store the user with provided data.
        :return: user information
        """
        try:

            inserted_lecturer: LecturerOutput = await self.repository.create(lecturer_input)
            inserted_lecturer = json.loads(inserted_lecturer.model_dump_json())
            return HttpHelper.ok(inserted_lecturer)

        except Exception as e:
            traceback.print_exc()
            return HttpHelper.internal_server_error(Exception(e))