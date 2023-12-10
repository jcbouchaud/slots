import pytest
from app.domain.user import UserCreate


def test_unit_of_work_commit(uow):
    new_user_data = UserCreate(
        first_name="John",
        last_name="Doe",
        email="john@example.com"
    )
    
    new_user = uow.users.add(new_user_data)
    uow.commit()

    assert new_user.first_name == new_user_data.first_name
    assert new_user.last_name == new_user_data.last_name
    assert new_user.email == new_user_data.email


def test_unit_of_work_rollback(uow):
    new_user_data = UserCreate(
        first_name="Jane",
        last_name="Smith",
        email="jane@example.com"
    )

    new_user = uow.users.add(new_user_data)
    uow.rollback()

    with pytest.raises(Exception):
        uow.users.get(new_user.id)