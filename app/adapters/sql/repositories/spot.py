from app.adapters.abstract.repositories.spot import AbstractSpotRepository
from app.adapters.sql.mappings import SpotModel
from app.domain.spot import Spot, SpotCreate, SpotUpdate


class SqlAlchemySpotRepository(AbstractSpotRepository):
    def __init__(self, session):
        self.session = session
        
    def _validate(self, spot_model: SpotModel):
        return Spot.model_validate(spot_model)

    def add(self, spot_create: SpotCreate) -> Spot:
        spot = SpotModel(**spot_create.model_dump())
        self.session.add(spot)
        self.session.flush()
        return self._validate(spot)

    def get(self, id: int) -> Spot:
        spot = self.session.query(SpotModel).filter_by(id=id).one()
        return self._validate(spot)
    
    def list(self) -> list[Spot]:
        return [self._validate(spot) for spot in self.session.query(SpotModel).all()]
    
    def update(self, id: int, spot_update: SpotUpdate) -> Spot:
        spot = self.session.query(SpotModel).filter_by(id=id).one()
        update_data = spot_update.model_dump(exclude_unset=True)
        
        for key, value in update_data.items():
            setattr(spot, key, value)

        self.session.add(spot)
        self.session.flush()
        return self._validate(spot)
