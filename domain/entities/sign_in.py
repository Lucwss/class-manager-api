import json
import os
from dataclasses import dataclass
from datetime import timedelta

from pydantic import BaseModel, EmailStr, Field

from adapters.libs.bcrypt import BcryptAdapter
from domain.entities.user import UserOutput

class SignInFields(BaseModel):
    """
    SignInFields model for user sign
    """
    email: EmailStr = Field(min_length=1, max_length=100)
    password: str = Field(min_length=1, max_length=100)


@dataclass
class SignIn:
    """
    SignIn entity for user sign in.
    """
    email: str
    password: str

    def __post_init__(self):
        self.encoder = BcryptAdapter()

    def authenticate(self, password: str, user_info: UserOutput | None) -> bool:
        """
        This method is responsible for authenticating the user.
        :param password: current user password to de authenticated.
        :param user_info: current user information.
        :return:
        """

        if user_info is None:
            return False
        if not self.encoder.verify_password(password, user_info.password):
            return False

        return True

    def generate_access_token(self, user: UserOutput):
        access_token_expires = timedelta(minutes=float(os.environ.get('ACCESS_TOKEN_EXPIRE_MINUTES')))
        data = {'sub': user.email}

        access_token = self.encoder.create_access_token(data, expires_delta=access_token_expires)
        return Token(access_token=access_token, token_type='bearer').model_dump()



class Token(BaseModel):
    """
    Token model for user access token.
    """
    access_token: str
    token_type: str