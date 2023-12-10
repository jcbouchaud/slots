from typing import Annotated
from fastapi import Depends
from app.adapters.abstract.unit_of_work import AbstractUnitOfWork
from app.adapters.sql.unit_of_work import get_unit_of_work


UnitOfWorkDependency = Annotated[AbstractUnitOfWork, Depends(get_unit_of_work)]
