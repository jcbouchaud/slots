from pydantic import BaseModel, ConfigDict


class Spot(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    description: str | None = None
    lat: float | int
    lon: float | int

    def update(self, **kwargs):
        for field, value in kwargs.items():
            if field not in ["name", "description"]:
                raise Exception(f"You are not authorized to update {field}")
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
