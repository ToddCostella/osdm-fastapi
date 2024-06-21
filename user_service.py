from sqlmodel import Session, select
from models import UserCreate, User


class UserService:
    def __init__(self, session: Session):
        self.session = session

    def add_user(self, user_data: UserCreate) -> User:
        user = User(**user_data.model_dump(exclude_unset=True))
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user

    def update_user(self, user_id: int, user_data: UserCreate) -> User | None:
        user = self.session.get(User, user_id)
        if not user:
            return None
        for key, value in user_data.model_dump(exclude_unset=True).items():
            setattr(user, key, value)
        self.session.commit()
        self.session.refresh(user)
        return user

    def delete_user(self, user_id: int) -> User | None:
        user = self.session.get(User, user_id)
        if not user:
            return None
        self.session.delete(user)
        self.session.commit()
        return user

    def get_all_users(self) -> list[User]:
        statement = select(User)
        users = self.session.exec(statement).all()
        return users

    def filter_users(self, name: str | None = None, email_address: str | None = None) -> list[User]:
        statement = select(User)
        if name:
            statement = statement.where(User.name.ilike(f"%{name}%"))
        if email_address:
            statement = statement.where(User.email_address == email_address)
        users = self.session.exec(statement).all()
        return users
