from app.adapters.abstract.repositories.user import AbstractUserRepository
from app.adapters.sql.mappings import UserModel, SpotModel
from app.domain.user import User, UserCreate


class SqlAlchemyUserRepository(AbstractUserRepository):
    def __init__(self, session):
        self.session = session
        
    def _validate(self, user_model: UserModel):
        return User.model_validate(user_model)

    def add(self, user_create: UserCreate) -> User:
        user = UserModel(**user_create.model_dump())
        self.session.add(user)
        self.session.flush()
        return self._validate(user)

    def get_by_id(self, id: int) -> User:
        user = self.session.query(UserModel).filter_by(id=id).one()
        return self._validate(user)
    
    def list(self) -> list[User]:
        return [self._validate(user) for user in self.session.query(UserModel).all()]
    
    def save(self, user: User) -> User:
        user_to_update = self.session.query(UserModel).filter_by(id=user.id).one()

        for field, value in user.model_dump().items():
            if field == "favorites_spots":
                value = [self.session.query(SpotModel).filter_by(id=spot["id"]).one() for spot in value]
            setattr(user_to_update, field, value)
    
        self.session.flush()
        return self._validate(user_to_update)