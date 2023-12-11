from app.adapters.abstract.unit_of_work import AbstractUnitOfWork
from app.domain.spot import Spot
from app.domain.user import User, UserUpdate


SpotDoesNotExist = Exception("Spot does not exist.")


def add_spot_to_favorites(user_id: int, spot: Spot, unit_of_work: AbstractUnitOfWork) -> User:
    user = unit_of_work.users.get(id=user_id)
    unit_of_work.spots.get(id=spot.id)
    
    if not spot:
        raise SpotDoesNotExist
    
    user.add_spot_to_favorites(spot=spot)
    unit_of_work.users.update(id=user.id, user_update=UserUpdate(favorites_spots=user.favorites_spots))
    
    return user
    

def remove_spot_from_favorites(user_id: int, spot: Spot, unit_of_work: AbstractUnitOfWork) -> User:
    user = unit_of_work.users.get(id=user_id)
    unit_of_work.spots.get(id=spot.id)
    
    if not spot:
        raise SpotDoesNotExist
    
    user.remove_spot_from_favorites(spot=spot)
    unit_of_work.users.update(id=user.id, user_update=UserUpdate(favorites_spots=user.favorites_spots))
    
    return user
