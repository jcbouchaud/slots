import abc
from app.domain.spot import Spot, SpotCreate


class AbstractSpotRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, spot_create: SpotCreate) -> Spot:
        raise NotImplementedError

    @abc.abstractmethod
    def get_by_id(self, id: int) -> Spot:
        raise NotImplementedError
    
    @abc.abstractmethod
    def list(self) -> list[Spot]:
        raise NotImplementedError
    
    @abc.abstractmethod
    def save(self, spot: Spot) -> Spot:
        raise NotImplementedError
