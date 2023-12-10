from app.adapters.abstract.unit_of_work import AbstractUnitOfWork
from app.domain.user import User, UserUpdate


SpotDoesNotExist = Exception("Spot does not exist.")


def add_spot_to_favorites(user_id: int, spot_id: int, unit_of_work: AbstractUnitOfWork) -> User:
    user = unit_of_work.users.get(id=user_id)
    spot = unit_of_work.spots.get(id=spot_id)
    
    if not spot:
        raise SpotDoesNotExist
    
    user.add_spot_to_favorites(spot_id=spot_id)
    return unit_of_work.users.update(id=user_id, user_update=UserUpdate(favorites_spots=user.favorites_spots))
    

def remove_spot_from_favorites(user_id: int, spot_id: int, unit_of_work: AbstractUnitOfWork) -> User:
    user = unit_of_work.users.get(id=user_id)
    spot = unit_of_work.spots.get(id=spot_id)
    
    if not spot:
        raise SpotDoesNotExist
    
    user.model_validate(user).remove_spot_from_favorites(spot_id=spot_id)
    return unit_of_work.users.update(id=user_id, user_update=UserUpdate(favorites_spots=user.favorites_spots))
