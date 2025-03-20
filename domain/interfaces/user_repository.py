from abc import ABC, abstractmethod
from domain.entities.user import UserOutput, UserInput


class IUserRepository(ABC):
    """
    Interface responsible for UserRepository methods.
    """

    @abstractmethod
    async def count_all_users(self):
        """
        This abstract method is responsible for counting all users on the database.
        :return: number of users
        """
        raise NotImplemented()

    @abstractmethod
    async def find_all(self, page: int, page_size: int):
        """
        This abstract method is responsible for finding all users on the database.
        :return:
        """
        raise NotImplementedError()

    @abstractmethod
    async def find_by_email(self, email: str) -> UserOutput | None:
        """
        This abstract method is responsible for finding the user on the database and return him/her information.
        :param email:
        :return: a user information
        """
        raise NotImplemented()

    @abstractmethod
    async def create(self, user_input: UserInput) -> UserOutput | None:
        """
        This abstract method is responsible for storing the user on the database and return him/her information.
        :param user_input:
        :return: a user information
        """
        raise NotImplemented()

    @abstractmethod
    async def delete_all(self):
        """
        This abstract method is responsible for deleting all users on the database.
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