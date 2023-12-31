import abc
from app.domain.user import User, UserCreate


class AbstractUserRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, user_create: UserCreate) -> User:
        raise NotImplementedError

    @abc.abstractmethod
    def get_by_id(self, id: int) -> User:
        raise NotImplementedError
    
    @abc.abstractmethod
    def list(self) -> list[User]:
        raise NotImplementedError

    @abc.abstractmethod
    def save(self, user: User) -> User:
        raise NotImplementedError