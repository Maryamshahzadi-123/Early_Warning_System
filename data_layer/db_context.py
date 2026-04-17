from entities.user import User
from typing import Optional


class DbContext:
    _users: list[User] = [
        User(id=1, email="hy@example.com", password="password123"),
        User(id=2, email="hi@example.com", password="secret456"),
    ]

    def get_user_by_email(self, email: str) -> Optional[User]:
        for user in DbContext._users:
            if user.email == email:
                return user
        return None
