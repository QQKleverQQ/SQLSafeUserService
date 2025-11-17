from sqlalchemy import text
from sqlalchemy.orm import Session
from .models import User
from .security import simple_hash

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_user_safe(self, user_id: int):
        return self.db.execute(
            text("SELECT * FROM users WHERE id = :id"), {"id": user_id}
        ).fetchone()

    def get_user_unsafe(self, user_input: str):
        query = f"SELECT * FROM users WHERE username = '{user_input}'"
        return self.db.execute(text(query)).fetchall()

    def create_user(self, username: str, password: str):
        user = User(username=username, password_hash=simple_hash(password))
        self.db.add(user)
        self.db.commit()
        return user

    def delete_user(self, user_id: int):
        u = self.db.get(User, user_id)
        if u:
            self.db.delete(u)
            self.db.commit()
            return True
        return False
