from data_layer.db_context import DbContext
from entities.user import User


class AuthService:
    @staticmethod
    def get_user(email: str) -> User | None:
        for user in DbContext.users:
            if user.email == email:
                return user
        return None

    def login(self, email: str, password: str) -> None:
        user = self.get_user(email)

        if user is None:
            raise ValueError("User not found with this email")

        if user.password != password:
            raise ValueError("Incorrect password")