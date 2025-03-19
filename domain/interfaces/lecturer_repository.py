from abc import ABC, abstractmethod
from domain.entities.lecturer import LecturerOutput, LecturerInput


class ILecturerRepository(ABC):
    """
    Interface responsible for LecturerRepository methods.
    """

    @abstractmethod
    async def count_all_lecturer(self):
        """
        This abstract method is responsible for counting all lecturer on the database.
        :return: number of lecturer
        """
        raise NotImplemented()

    @abstractmethod
    async def find_all(self, page: int, page_size: int):
        """
        This abstract method is responsible for finding all lecturer on the database.
        :return:
        """
        raise NotImplementedError()

    @abstractmethod
    async def find_by_email(self, email: str) -> LecturerOutput | None:
        """
        This abstract method is responsible for finding the user on the database and return him/her information.
        :param email:
        :return: a user information
        """
        raise NotImplemented()

    @abstractmethod
    async def create(self, user_input: LecturerInput) -> LecturerOutput | None:
        """
        This abstract method is responsible for storing the user on the database and return him/her information.
        :param user_input:
        :return: a user information
        """
        raise NotImplemented()

    @abstractmethod
    async def delete_all(self):
        """
        This abstract method is responsible for deleting all lecturer on the database.
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