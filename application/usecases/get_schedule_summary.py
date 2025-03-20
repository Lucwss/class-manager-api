import json
import traceback
from typing import Any

from application.interfaces.usecase import UseCase
from domain.entities.pagination import PaginationResponse
from domain.entities.schedule import ScheduleInput, ScheduleOutput
from domain.interfaces.schedule_repository import IScheduleRepository
from web.http_helper import HttpResponse, HttpHelper


class GetScheduleUseCase(UseCase):
    """
    Use case for create a schedule in the system. (Implementing the UseCase interface).
    """

    def __init__(self, repository: IScheduleRepository):
        """
        Constructor assigning the repository attribute as a dependency repository. (Dependency Injection by constructor).
        """
        self.repository: IScheduleRepository = repository

    async def execute(self, search: Any, page: int = 1, page_size: int = 15) -> HttpResponse:
        """
        This method will store the user with provided data.
        :return: user information
        """
        try:

            schedule_summary = await self.repository.find_all(page, page_size, search)
            total_qtd_schedules = await self.repository.count_all_schedules()
            pagination_response = PaginationResponse(data=schedule_summary, total=total_qtd_schedules)
            return HttpHelper.ok(json.loads(pagination_response.model_dump_json()))

        except Exception as e:
            traceback.print_exc()
            return HttpHelper.internal_server_error(Exception(e))