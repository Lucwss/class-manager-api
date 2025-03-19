from abc import ABC, abstractmethod

from domain.entities.student import StudentOutput, StudentInput


class IStudentRepository(ABC):
    """
    Interface responsible for StudentRepository methods.
    """

    @abstractmethod
    async def count_all_students(self):
        """
        This abstract method is responsible for counting all students on the database.
        :return: number of students
        """
        raise NotImplemented()

    @abstractmethod
    async def find_all(self, page: int, page_size: int):
        """
        This abstract method is responsible for finding all students on the database.
        :return:
        """
        raise NotImplementedError()

    @abstractmethod
    async def find_by_email(self, email: str) -> StudentOutput | None:
        """
        This abstract method is responsible for finding the user on the database and return him/her information.
        :param email:
        :return: a user information
        """
        raise NotImplemented()

    @abstractmethod
    async def create(self, user_input: StudentInput) -> StudentOutput | None:
        """
        This abstract method is responsible for storing the user on the database and return him/her information.
        :param user_input:
        :return: a user information
        """
        raise NotImplemented()

    @abstractmethod
    async def delete_all(self):
        """
        This abstract method is responsible for deleting all students on the database.
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