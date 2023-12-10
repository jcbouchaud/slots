from fastapi import APIRouter
from app.api.dependencies import UnitOfWorkDependency
from app.domain.user import User, UserCreate, UserUpdate


router = APIRouter(
    prefix="/users",
    tags=["Users"],
)

@router.post("", response_model=User)
async def create_user(user_create: UserCreate, unit_of_work: UnitOfWorkDependency):
    return unit_of_work.users.add(user_create=user_create)


@router.put("/{id}", response_model=User)
async def update_user(id:int, user_update: UserUpdate, unit_of_work: UnitOfWorkDependency):
    return unit_of_work.users.update(id=id, user_update=user_update)


@router.get("/{id}", response_model=User)
async def get_user(id: int, unit_of_work: UnitOfWorkDependency):
    return unit_of_work.users.get(id=id)


@router.get("", response_model=list[User])
async def list_users(unit_of_work: UnitOfWorkDependency):
    return unit_of_work.users.list()
