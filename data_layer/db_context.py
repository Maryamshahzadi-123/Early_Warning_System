from entities.user import User
from typing import Optional


class DbContext:
    _users: list[User] = [
        User(id=1, email=" hy@example.com", password="password123"),
        User(id=2, email="hi@example.com", password="secret456"),
    ]
    _entered_drones: set[str] = set()

    @staticmethod
    def get_all_users() -> list[User]:
        return DbContext._users.copy()

    @staticmethod
    def get_user_by_email(email: str) -> Optional[User]:
        for user in DbContext._users:
            if user.email == email:
                return user
        return None

    @staticmethod
    def get_entered_drones() -> set[str]:
        return DbContext._entered_drones.copy()

    @staticmethod
    def add_entered_drone(drone_id: str) -> None:
        DbContext._entered_drones.add(drone_id)
