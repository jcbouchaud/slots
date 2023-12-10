import abc
from app.domain.user import User, UserCreate


class AbstractUserRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, user_create: UserCreate) -> User:
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, id: int) -> User:
        raise NotImplementedError
    
    @abc.abstractmethod
    def list(self) -> list[User]:
        raise NotImplementedError
