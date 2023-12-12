from pydantic import BaseModel, ConfigDict


class Spot(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    description: str | None = None
    lat: float | int
    lon: float | int

    def update(self, **kwargs):
        if "id" in kwargs:
            raise Exception("You cannot update primary key")
        for field, value in kwargs.items():
            setattr(self, field, value)
        return self
    
class SpotCreate(BaseModel):
    name: str
    description: str | None = None
    lat: float | int
    lon: float | int
    
    
class SpotUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
