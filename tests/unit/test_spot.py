from pydantic import ValidationError
from app.domain.spot import SpotCreate
import pytest

def test_create_valid_spot():
    spot_create_data = {
        "name": "The spot",
        "lat": 49.123,
        "lon": 15.008               
    }
    spot_create = SpotCreate(**spot_create_data)
    assert isinstance(spot_create, SpotCreate)

