from sqlalchemy import Column, Index, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from app.adapters.sql import Base
# from app.adapters.sql.mappings.spot import SpotModel


class UserFavoritesSpots(Base):
    __tablename__ = "user_favorites_spots"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    spot_id = Column( Integer, ForeignKey("spots.id"))
    
    __table_args__ = (
        UniqueConstraint("user_id", "spot_id", name="uq_user_id_spot_id"),
        Index("uq_user_id_spot_id", "user_id", "spot_id"),
    )


class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    favorites_spots = relationship("SpotModel", secondary="user_favorites_spots")
