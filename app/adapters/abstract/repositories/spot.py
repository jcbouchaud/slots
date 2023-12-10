import abc
from app.domain.spot import Spot, SpotCreate, SpotUpdate


class AbstractSpotRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, spot_create: SpotCreate) -> Spot:
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, id: int) -> Spot:
        raise NotImplementedError
    
    @abc.abstractmethod
    def list(self) -> list[Spot]:
        raise NotImplementedError

    @abc.abstractmethod
    def update(self, id: int, spot_update: SpotUpdate) -> Spot:
        raise NotImplementedError
