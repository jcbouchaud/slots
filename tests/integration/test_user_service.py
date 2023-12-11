from app.domain.spot import SpotCreate
from app.domain.user import UserCreate, UserUpdate
from app.service_layer.user import add_spot_to_favorites, remove_spot_from_favorites


def test_user_can_add_spot_to_favorites(uow):
    new_user_data = UserCreate(
        first_name="John",
        last_name="Doe",
        email="john@example.com"
    )
    
    new_user = uow.users.add(user_create=new_user_data)
    
    new_spot_data = SpotCreate(
        name="The spot",
        lat=0,
        lon=0
    )
    
    new_spot = uow.spots.add(spot_create=new_spot_data)
    
    uow.commit()
    
    updated_user = add_spot_to_favorites(
        user_id=new_user.id,
        spot=new_spot,
        unit_of_work=uow
    )
    
    assert new_spot in updated_user.favorites_spots


def test_user_can_remove_spot_from_favorites(uow):
    new_user_data = UserCreate(
        first_name="John",
        last_name="Doe",
        email="john@example.com",
    )
    
    new_user = uow.users.add(user_create=new_user_data)
    
    new_spot_data = SpotCreate(
        name="The spot",
        lat=0,
        lon=0
    )
    
    new_spot = uow.spots.add(spot_create=new_spot_data)
    uow.users.update(id=new_user.id, user_update=UserUpdate(favorites_spots=[new_spot]))

    uow.commit()
    
    updated_user = remove_spot_from_favorites(
        user_id=new_user.id,
        spot=new_spot,
        unit_of_work=uow
    )
    
    assert new_spot.id not in updated_user.favorites_spots