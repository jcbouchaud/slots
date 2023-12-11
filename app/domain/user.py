from pydantic import BaseModel, ConfigDict, EmailStr

from app.domain.spot import Spot


class User(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    first_name: str
    last_name: str
    email: EmailStr
    favorites_spots: list[Spot] = []
    
    def add_spot_to_favorites(self, spot: Spot):
        self.favorites_spots = self.favorites_spots or list()
        if not self._is_favorite_spot(spot=spot):
            self.favorites_spots.append(spot)
        return self

    def remove_spot_from_favorites(self, spot: Spot):
        if self._is_favorite_spot(spot=spot):
            self.favorites_spots.remove(spot)
        return self
    
    def _is_favorite_spot(self, spot: Spot):
        return spot in self.favorites_spots
    
    
class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr


class UserUpdate(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    email: EmailStr | None = None
    favorites_spots: list[Spot] = []
