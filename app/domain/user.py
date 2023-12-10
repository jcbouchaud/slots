from pydantic import BaseModel, ConfigDict, EmailStr


class User(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    first_name: str
    last_name: str
    email: EmailStr
    favorites_spots: set[int] = set()
    
    def add_spot_to_favorites(self, spot_id: int):
        self.favorites_spots = self.favorites_spots or set()
        self.favorites_spots.add(spot_id)
        return self

    def remove_spot_from_favorites(self, spot_id: int):
        if spot_id in self.favorites_spots:
            self.favorites_spots.remove(spot_id)
        return self
    
    
class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr


class UserUpdate(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    email: EmailStr | None = None
    favorites_spots: set[str] | None = None
