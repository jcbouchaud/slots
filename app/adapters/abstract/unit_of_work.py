# pylint: disable=attribute-defined-outside-init
from __future__ import annotations
import abc

from app.adapters.sql.repository import AbstractUserRepository

class AbstractUnitOfWork(abc.ABC):
    users: AbstractUserRepository

    def __enter__(self) -> AbstractUnitOfWork:
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is None:
            self.commit()
            return True
        else:
            self.rollback()
            return False


    @abc.abstractmethod
    def commit(self):
        raise NotImplementedError

    @abc.abstractmethod
    def rollback(self):
        raise NotImplementedError
