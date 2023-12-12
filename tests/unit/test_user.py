from pydantic import ValidationError
from app.domain.spot import Spot
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
    spot_data = {
        "id": 1,
        "name": "The spot",
        "lat": 0,
        "lon": 0
    }
    spot = Spot(**spot_data)
    user.add_spot_to_favorites(spot=spot)
    assert user.favorites_spots
    assert spot in user.favorites_spots
    
    
def test_remove_spot_from_favorites():
    spot_data = {
        "id": 1,
        "name": "The spot",
        "lat": 0,
        "lon": 0
    }
    spot = Spot(**spot_data)
    user_data = {
        "id": 1,
        "first_name": "John",
        "last_name": "Doe",
        "email": "john@example.com",
        "favorites_spots": [spot]
    }
    user = User(**user_data)
    user.remove_spot_from_favorites(spot=spot)
    assert len(user.favorites_spots) == 0


def test_spot_is_favorite_user_spot():
    spot_data = {
        "id": 1,
        "name": "The spot",
        "lat": 0,
        "lon": 0
    }
    spot = Spot(**spot_data)
    user_data = {
        "id": 1,
        "first_name": "John",
        "last_name": "Doe",
        "email": "john@example.com",
        "favorites_spots": [spot]
    }
    user = User(**user_data)
    assert user._is_favorite_spot(spot=spot)


def test_spot_is_not_favorite_user_spot():
    spot_data = {
        "id": 1,
        "name": "The spot",
        "lat": 0,
        "lon": 0
    }
    spot = Spot(**spot_data)
    user_data = {
        "id": 1,
        "first_name": "John",
        "last_name": "Doe",
        "email": "john@example.com",
        "favorites_spots": []
    }
    user = User(**user_data)
    assert not user._is_favorite_spot(spot=spot)