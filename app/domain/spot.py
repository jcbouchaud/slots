
from pydantic import BaseModel, ConfigDict


class Spot(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    description: str | None = None
    lat: float | int
    lon: float | int


class SpotCreate(BaseModel):
    name: str
    description: str | None = None
    lat: float | int
    lon: float | int
    
    
class SpotUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
