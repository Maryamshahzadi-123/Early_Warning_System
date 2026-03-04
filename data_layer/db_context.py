from entities.user import User
from entities.aircraft import Aircraft


class DbContext:
    users: list[User] = [
        User(id=1, email="hy@example.com", password="password123"),
        User(id=2, email="hi@example.com", password="secret456"),
    ]

    aircraft: list[Aircraft] = [
        Aircraft(id=1, tail_number="N12345", model="Boeing 737", manufacturer="Boeing", year=2020),
        Aircraft(id=2, tail_number="N67890", model="Airbus A320", manufacturer="Airbus", year=2021),
    ]
