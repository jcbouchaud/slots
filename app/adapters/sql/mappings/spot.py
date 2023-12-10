from sqlalchemy import Column, Integer, String, UniqueConstraint, Numeric, Index

from app.adapters.sql import Base


class SpotModel(Base):
    __tablename__ = "spots"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    lat = Column(Numeric(precision=5, scale=2))
    lon = Column(Numeric(precision=5, scale=2))
    
    __table_args__ = (
        UniqueConstraint('lat', 'lon', name='uq_lat_lon'),
        Index('idx_lat_lon', 'lat', 'lon'),
    )

