from pydantic import ValidationError
from app.domain.user import UserCreate
import pytest

def test_create_valid_user():
    user_create_data = {
        "first_name": "John",
        "last_name": "Doe",
        "email": "john@example.com"
    }
    user_create = UserCreate(**user_create_data)
    assert isinstance(user_create, UserCreate)


def test_create_user_with_invalid_email():
    invalid_user_create_data = {
        "first_name": "John",
        "last_name": "Doe",
        "email": "invalid_email"
    }
    with pytest.raises(ValidationError):
        UserCreate(**invalid_user_create_data)
