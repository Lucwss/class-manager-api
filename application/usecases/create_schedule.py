import json
import traceback

from application.interfaces.usecase import UseCase
from domain.entities.schedule import ScheduleInput, ScheduleOutput
from domain.interfaces.lecturer_repository import ILecturerRepository
from domain.interfaces.schedule_repository import IScheduleRepository
from domain.interfaces.student_repository import IStudentRepository
from web.http_helper import HttpResponse, HttpHelper


class CreateScheduleUseCase(UseCase):
    """
    Use case for create a schedule in the system. (Implementing the UseCase interface).
    """

    def __init__(self,
                 repository: IScheduleRepository,
                 student_repository: IStudentRepository,
                 lecturer_repository: ILecturerRepository
                 ):
        """
        Constructor assigning the repository attribute as a dependency repository. (Dependency Injection by constructor).
        """
        self.repository: IScheduleRepository = repository
        self.student_repository: IStudentRepository = student_repository
        self.lecturer_repository: ILecturerRepository = lecturer_repository

    async def execute(self, schedule_input: ScheduleInput) -> HttpResponse:
        """
        This method will store the user with provided data.
        :return: user information
        """
        try:

            student = await self.student_repository.find_by_id(schedule_input.student_id)

            if not student:
                return HttpHelper.bad_request(Exception("Student not found."))

            lecturer = await self.lecturer_repository.find_by_id(schedule_input.lecturer_id)

            if not lecturer:
                return HttpHelper.bad_request(Exception("Lecturer not found."))


            inserted_schedule: ScheduleOutput = await self.repository.create(schedule_input)
            inserted_schedule = json.loads(inserted_schedule.model_dump_json())
            return HttpHelper.created(inserted_schedule)

        except Exception as e:
            traceback.print_exc()
            return HttpHelper.internal_server_error(Exception(e))