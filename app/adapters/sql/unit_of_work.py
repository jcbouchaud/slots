from app.adapters.sql.repositories.user import SqlAlchemyUserRepository
from app.adapters.sql import SessionLocal
from app.adapters.abstract.unit_of_work import AbstractUnitOfWork
from sqlalchemy.orm.session import Session


class SqlAlchemyUnitOfWork(AbstractUnitOfWork):
    def __init__(self, session_factory=SessionLocal):
        self.session_factory = session_factory

    def __enter__(self):
        self.session = self.session_factory()  # type: Session
        self.users = SqlAlchemyUserRepository(self.session)
        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)
        self.session.close()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()


def get_unit_of_work():
    uow = SqlAlchemyUnitOfWork()
    with uow:
        yield uow