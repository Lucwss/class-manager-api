import json
import traceback

from application.interfaces.usecase import UseCase
from domain.entities.schedule import ScheduleInput, ScheduleOutput
from domain.interfaces.schedule_repository import IScheduleRepository
from web.http_helper import HttpResponse, HttpHelper


class CreateScheduleUseCase(UseCase):
    """
    Use case for create a schedule in the system. (Implementing the UseCase interface).
    """

    def __init__(self, repository: IScheduleRepository):
        """
        Constructor assigning the repository attribute as a dependency repository. (Dependency Injection by constructor).
        """
        self.repository: IScheduleRepository = repository

    async def execute(self, schedule_input: ScheduleInput) -> HttpResponse:
        """
        This method will store the user with provided data.
        :return: user information
        """
        try:

            inserted_schedule: ScheduleOutput = await self.repository.create(schedule_input)
            inserted_schedule = json.loads(inserted_schedule.model_dump_json())
            return HttpHelper.created(inserted_schedule)

        except Exception as e:
            traceback.print_exc()
            return HttpHelper.internal_server_error(Exception(e))