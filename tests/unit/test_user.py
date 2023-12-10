from pydantic import ValidationError
from app.domain.user import UserCreate, User
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


def test_add_spot_to_favorites():
    user_data = {
        "id": 1,
        "first_name": "John",
        "last_name": "Doe",
        "email": "john@example.com"
    }
    user = User(**user_data)
    spot_id = 1
    user.add_spot_to_favorites(spot_id=spot_id)
    assert user.favorites_spots
    assert spot_id in user.favorites_spots
    
    
def test_remove_spot_from_favorites():
    user_data = {
        "id": 1,
        "first_name": "John",
        "last_name": "Doe",
        "email": "john@example.com",
        "favorites_spots": [1]
    }
    user = User(**user_data)
    spot_id = 1
    user.remove_spot_from_favorites(spot_id=spot_id)
    assert not user.favorites_spots
