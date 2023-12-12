from fastapi import APIRouter, status
from app.api.dependencies import UnitOfWorkDependency
from app.domain.user import User, UserCreate, UserUpdate
from app.service_layer.user import add_spot_to_favorites, remove_spot_from_favorites


router = APIRouter(
    prefix="/users",
    tags=["Users"],
)

@router.post("", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(user_create: UserCreate, unit_of_work: UnitOfWorkDependency):
    return unit_of_work.users.add(user_create=user_create)


@router.put("/{id}", response_model=User, status_code=status.HTTP_200_OK)
async def update_user(id:int, user_update: UserUpdate, unit_of_work: UnitOfWorkDependency):
    user = unit_of_work.users.get_by_id(id=id)
    user.update(**user_update.model_dump())
    return unit_of_work.users.save(user=user)


@router.get("/{id}", response_model=User, status_code=status.HTTP_200_OK)
async def get_user(id: int, unit_of_work: UnitOfWorkDependency):
    return unit_of_work.users.get_by_id(id=id)


@router.get("", response_model=list[User], status_code=status.HTTP_200_OK)
async def list_users(unit_of_work: UnitOfWorkDependency):
    return unit_of_work.users.list()


@router.put("/favorites/add/{spot_id}", response_model=User, status_code=status.HTTP_200_OK)
async def add_spot_to_favorite(user_id: int, spot_id: int, unit_of_work: UnitOfWorkDependency):
    return add_spot_to_favorites(user_id=user_id, spot_id=spot_id, unit_of_work=unit_of_work)


@router.put("/favorites/remove/{spot_id}", response_model=User, status_code=status.HTTP_200_OK)
async def remove_spot_from_favorite(user_id: int, spot_id: int, unit_of_work: UnitOfWorkDependency):
    return remove_spot_from_favorites(user_id=user_id, spot_id=spot_id, unit_of_work=unit_of_work)
