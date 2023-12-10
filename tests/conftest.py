import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.adapters.sql.unit_of_work import SqlAlchemyUnitOfWork
from app.adapters.sql import Base


@pytest.fixture()
def in_memory_sqlite_db():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    yield engine
    Base.metadata.drop_all(engine)
    engine.dispose()


@pytest.fixture()
def sqlite_session_factory(in_memory_sqlite_db):
    yield sessionmaker(bind=in_memory_sqlite_db, autoflush=False, autocommit=False)    
        
    
@pytest.fixture()
def uow(sqlite_session_factory):
    with SqlAlchemyUnitOfWork(session_factory=sqlite_session_factory) as uow_instance:
        yield uow_instance
