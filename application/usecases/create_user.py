import json
import traceback

from application.interfaces.usecase import UseCase
from domain.entities.user import UserInput, UserOutput
from domain.interfaces.encoders import IJwtEncoder
from domain.interfaces.user_repository import IUserRepository
from web.http_helper import HttpResponse, HttpHelper


class CreateUserUseCase(UseCase):
    """
    Use case for create a user in the system. (Implementing the UseCase interface).
    """

    def __init__(self, repository: IUserRepository, encoder: IJwtEncoder):
        """
        Constructor assigning the repository attribute as a dependency repository. (Dependency Injection by constructor).
        """
        self.repository: IUserRepository = repository
        self.encoder: IJwtEncoder = encoder

    async def execute(self, user_input: UserInput) -> HttpResponse:
        """
        This method will store the user with provided data.
        :return: user information
        """
        try:

            user = await self.repository.find_by_email(str(user_input.email))

            if user:
                return HttpHelper.bad_request(Exception("User already exists."))

            hashed_password = self.encoder.get_password_hash(user_input.password)
            user_input.password = hashed_password

            inserted_user: UserOutput = await self.repository.create(user_input)
            inserted_user = json.loads(inserted_user.model_dump_json())
            return HttpHelper.created(inserted_user)

        except Exception as e:
            traceback.print_exc()
            return HttpHelper.internal_server_error(Exception(e))