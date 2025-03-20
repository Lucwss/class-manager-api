from abc import ABC, abstractmethod
from typing import Any

from domain.entities.schedule import ScheduleOutput, ScheduleInput


class IScheduleRepository(ABC):
    """
    Interface responsible for ScheduleRepository methods.
    """

    @abstractmethod
    async def count_all_schedules(self):
        """
        This abstract method is responsible for counting all schedules on the database.
        :return: number of schedules
        """
        raise NotImplemented()

    @abstractmethod
    async def find_all(self, page: int, page_size: int, search: Any = None):
        """
        This abstract method is responsible for finding all schedules on the database.
        :return:
        """
        raise NotImplementedError()

    @abstractmethod
    async def find_by_email(self, email: str) -> ScheduleOutput | None:
        """
        This abstract method is responsible for finding the user on the database and return him/her information.
        :param email:
        :return: a user information
        """
        raise NotImplemented()

    @abstractmethod
    async def create(self, user_input: ScheduleInput) -> ScheduleOutput | None:
        """
        This abstract method is responsible for storing the user on the database and return him/her information.
        :param user_input:
        :return: a user information
        """
        raise NotImplemented()

    @abstractmethod
    async def delete_all(self):
        """
        This abstract method is responsible for deleting all schedules on the database.
        """
        raise NotImplemented()

    @abstractmethod
    async def delete_by_id(self, user_id: str):
        """
        This abstract method is responsible for deleting the user on the database and return it information.
        :param user_id:
        :return: a role information
        """
        raise NotImplemented()

    @abstractmethod
    async def find_by_id(self, user_id: str):
        """
        This abstract method is responsible for finding the user on the database and return it information.
        :param user_id:
        :return: a role information
        """
        raise NotImplemented()