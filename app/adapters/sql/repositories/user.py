import abc
from app.adapters.abstract.repositories.user import AbstractUserRepository
from app.adapters.sql.mappings import UserModel
from app.domain.user import User, UserCreate, UserUpdate


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

    def update(self, id: int, user_update: UserUpdate) -> User:
        user = self.session.query(UserModel).filter_by(id=id)
        user.update(user_update.model_dump(exclude_unset=True))
        self.session.flush()
        return user.one()