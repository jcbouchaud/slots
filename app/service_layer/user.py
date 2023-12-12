from app.adapters.abstract.unit_of_work import AbstractUnitOfWork
from app.domain.user import User


def add_spot_to_favorites(user_id: int, spot_id: int, unit_of_work: AbstractUnitOfWork) -> User:
    user = unit_of_work.users.get_by_id(id=user_id)
    spot = unit_of_work.spots.get_by_id(id=spot_id)
    
    user.add_spot_to_favorites(spot=spot)
    
    return unit_of_work.users.save(user=user)
        

def remove_spot_from_favorites(user_id: int, spot_id: int, unit_of_work: AbstractUnitOfWork) -> User:
    user = unit_of_work.users.get_by_id(id=user_id)
    spot = unit_of_work.spots.get_by_id(id=spot_id)

    user.remove_spot_from_favorites(spot=spot)
    
    return unit_of_work.users.save(user=user)
