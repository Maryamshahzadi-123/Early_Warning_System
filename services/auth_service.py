from data_layer.db_context import DbContext
from entities.user import User
from typing import Optional


class AuthService:
    def get_user(self, email: str) -> Optional[User]:
        return DbContext.get_user_by_email(email)

    def login(self, email: str, password: str) -> None:
        user = self.get_user(email)

        if user is None:
            raise ValueError("User not found with this email")

        if user.password != password:
            raise ValueError("Incorrect password")