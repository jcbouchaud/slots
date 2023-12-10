import abc
from app.adapters.abstract.repositories.spot import AbstractSpotRepository
from app.adapters.sql.mappings import SpotModel
from app.domain.spot import Spot, SpotCreate, SpotUpdate


class SqlAlchemySpotRepository(AbstractSpotRepository):
    def __init__(self, session):
        self.session = session

    def add(self, spot_create: SpotCreate) -> Spot:
        spot = SpotModel(**spot_create.model_dump())
        self.session.add(spot)
        self.session.flush()
        return spot

    def get(self, id: int) -> Spot:
        return self.session.query(SpotModel).filter_by(id=id).one()
    
    def list(self) -> list[Spot]:
        return self.session.query(SpotModel).all()
    
    def update(self, id: int, spot_update: SpotUpdate) -> Spot:
        spot = self.session.query(SpotModel).filter_by(id=id)
        spot.update(spot_update.model_dump(exclude_unset=True))
        self.session.flush()
        return spot.one()
