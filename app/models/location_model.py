from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from app.models import Base


class Location(Base):
    __tablename__ = 'locations'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    country = Column(String)
    region = Column(String)
    city = Column(String)

    attacks = relationship("Attack", back_populates="location")
