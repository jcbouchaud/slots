from fastapi import APIRouter
from app.api.dependencies import UnitOfWorkDependency
from app.domain.spot import Spot, SpotCreate, SpotUpdate


router = APIRouter(
    prefix="/spots",
    tags=["Spots"],
)

@router.post("", response_model=Spot)
async def create_spot(spot_create: SpotCreate, unit_of_work: UnitOfWorkDependency):
    return unit_of_work.spots.add(spot_create=spot_create)


@router.put("/{id}", response_model=Spot)
async def update_spot(id:int, spot_update: SpotUpdate, unit_of_work: UnitOfWorkDependency):
    spot = unit_of_work.spots.get_by_id(id=id)
    spot.update(**spot_update.model_dump())
    return unit_of_work.spots.save(spot=spot)


@router.get("/{id}", response_model=Spot)
async def get_spot(id: int, unit_of_work: UnitOfWorkDependency):
    return unit_of_work.spots.get_by_id(id=id)


@router.get("", response_model=list[Spot])
async def list_spots(unit_of_work: UnitOfWorkDependency):
    return unit_of_work.spots.list()
