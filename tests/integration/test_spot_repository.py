from sqlalchemy.exc import IntegrityError
import pytest
from app.adapters.sql.repositories.spot import SqlAlchemySpotRepository
from app.domain.spot import SpotCreate, SpotUpdate, Spot


def test_add_spot(sqlite_session_factory):
    session = sqlite_session_factory()
    repo = SqlAlchemySpotRepository(session)

    spot_create = SpotCreate(name="The spot", lat=0, lon=0)
    spot = repo.add(spot_create=spot_create)
    
    assert spot.id
    assert spot.name == spot_create.name
    assert spot.lat == spot_create.lat
    assert spot.lon == spot_create.lon
    
    
def test_add_spot_with_same_lat_lon_raises_error(sqlite_session_factory):
    session = sqlite_session_factory()
    repo = SqlAlchemySpotRepository(session)

    spot_create = SpotCreate(name="The spot", lat=0, lon=0)
    repo.add(spot_create=spot_create)
    
    with pytest.raises(IntegrityError):
        other_spot_create = SpotCreate(name="The other spot", lat=0, lon=0)
        repo.add(spot_create=other_spot_create)
        
        
def test_save_spot(sqlite_session_factory):
    session = sqlite_session_factory()
    repo = SqlAlchemySpotRepository(session)

    spot_create = SpotCreate(name="The spot", lat=0, lon=0)
    spot = repo.add(spot_create=spot_create)
    
    spot_update = spot.update(name="The updated spot")
    updated_spot = repo.save(spot=spot_update)
    
    assert updated_spot.name == spot_update.name
    
    
def test_get_by_id(sqlite_session_factory):
    session = sqlite_session_factory()
    repo = SqlAlchemySpotRepository(session)

    spot_create = SpotCreate(name="The spot", lat=0, lon=0)
    spot = repo.add(spot_create=spot_create)
    
    assert spot == Spot(id=spot.id, **spot_create.model_dump())


def test_list_users(sqlite_session_factory):
    session = sqlite_session_factory()
    repo = SqlAlchemySpotRepository(session)

    spot_create = SpotCreate(name="The spot", lat=0, lon=0)
    other_spot_create = SpotCreate(name="The other spot", lat=1, lon=1)
    
    repo.add(spot_create=spot_create)
    repo.add(spot_create=other_spot_create)
    
    spots = repo.list()
    
    assert len(spots) == 2