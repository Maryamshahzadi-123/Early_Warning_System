from entities.user import User
from typing import Optional


class DbContext:
    def __init__(self):
        self._users: list[User] = [
            User(id=1, email="hy@example.com", password="password123"),
            User(id=2, email="hi@example.com", password="secret456"),
        ]
        self._entered_drones: set[str] = set()

    def get_all_users(self) -> list[User]:
        return self._users.copy()

    def get_user_by_email(self, email: str) -> Optional[User]:
        for user in self._users:
            if user.email == email:
                return user
        return None

    def get_entered_drones(self) -> set[str]:
        return self._entered_drones.copy()

    def add_entered_drone(self, drone_id: str) -> None:
        self._entered_drones.add(drone_id)
