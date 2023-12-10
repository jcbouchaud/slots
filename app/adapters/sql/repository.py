import abc
from app.adapters.abstract.repository import AbstractUserRepository
from app.adapters.sql.mappings import UserModel
from app.domain.user import User, UserCreate


class SqlAlchemyUserRepository(AbstractUserRepository):
    def __init__(self, session):
        self.session = session

    def add(self, user_create: UserCreate) -> User:
        user = UserModel(**user_create.model_dump())
        self.session.add(user)
        self.session.flush()
        return user

    def get(self, id: int) -> User:
        return self.session.query(UserModel).filter_by(id=id).one()
    
    def list(self) -> list[User]:
        return self.session.query(UserModel).all()
