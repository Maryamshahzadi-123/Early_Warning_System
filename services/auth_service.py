from data_layer.db_context import DbContext


class AuthService:
    def __init__(self, db_context: DbContext):
        self.db_context = db_context

    def login(self, email: str, password: str) -> None:
        user = self.db_context.get_user_by_email(email)

        if user is None:
            raise ValueError("User not found")

        if user.password != password:
            raise ValueError("Incorrect password")
