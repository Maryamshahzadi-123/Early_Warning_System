from entities.user import User
class DbContext:
    users: list[User] = [
        User(id=1, email="alice@example.com", password="password123"),
        User(id=2, email="bob@example.com", password="secret456"),
    ]
