from entities.user import User
from typing import Optional, Dict, Tuple


class DbContext:
    _users: list[User] = [
        User(id=1, email="hy@example.com", password="password123"),
        User(id=2, email="hi@example.com", password="secret456"),
    ]
    _entered_drones: Dict[str, Tuple[float, float]] = {}

    def get_user_by_email(self, email: str) -> Optional[User]:
        for user in DbContext._users:
            if user.email == email:
                return user
        return None

    def get_entered_drones(self) -> set[str]:
        return set(DbContext._entered_drones.keys())

    def add_entered_drone(self, drone_id: str, latitude: float = 0.0, longitude: float = 0.0):
        DbContext._entered_drones[drone_id] = (latitude, longitude)

    def remove_entered_drone(self, drone_id: str):
        DbContext._entered_drones.pop(drone_id, None)

    def update_drone_position(self, drone_id: str, latitude: float, longitude: float) -> bool:
        if drone_id not in DbContext._entered_drones:
            return False
        DbContext._entered_drones[drone_id] = (latitude, longitude)
        return True

    def get_drone_position(self, drone_id: str) -> Optional[Tuple[float, float]]:
        return DbContext._entered_drones.get(drone_id)
    
    