from app.adapters.sql.repositories.user import SqlAlchemyUserRepository
from app.domain.user import UserCreate, User


def test_add_user(sqlite_session_factory):
    session = sqlite_session_factory()
    repo = SqlAlchemyUserRepository(session)

    user_create = UserCreate(first_name="John", last_name="Doe", email="john@example.com")
    user = repo.add(user_create=user_create)
    
    assert user.id
    assert user.first_name == user_create.first_name
    assert user.last_name == user_create.last_name
    assert user.email == user_create.email


def test_save_user(sqlite_session_factory):
    session = sqlite_session_factory()
    repo = SqlAlchemyUserRepository(session)

    user_create = UserCreate(first_name="John", last_name="Doe", email="john@example.com")
    user = repo.add(user_create=user_create)
    
    user_update = user.update(first_name="updated_first_name", last_name="updated_last_name", email="updated_email@example.com")
    updated_user = repo.save(user=user_update)

    assert updated_user.first_name == updated_user.first_name
    assert updated_user.last_name == updated_user.last_name
    assert updated_user.email == updated_user.email
    
    
def test_get_by_id(sqlite_session_factory):
    session = sqlite_session_factory()
    repo = SqlAlchemyUserRepository(session)

    user_create = UserCreate(first_name="John", last_name="Doe", email="john@example.com")
    user = repo.add(user_create=user_create)
    
    assert user == User(id=user.id, **user_create.model_dump(exclude_unset=True))


def test_list_users(sqlite_session_factory):
    session = sqlite_session_factory()
    repo = SqlAlchemyUserRepository(session)

    user_create_one = UserCreate(first_name="John", last_name="Doe", email="john@example.com")
    user_create_two = UserCreate(first_name="Jane", last_name="Doe", email="jane@example.com")

    repo.add(user_create=user_create_one)
    repo.add(user_create=user_create_two)
    
    users = repo.list()
    
    assert len(users) == 2
