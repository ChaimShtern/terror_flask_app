from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.models import Base


class PropertyDamage(Base):
    __tablename__ = 'property_damages'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    property_damaged = Column(Boolean)
    value = Column(Float)
    extent = Column(String)

    attack_id = Column(Integer, ForeignKey("attacks.id"))
    attack = relationship("Attack", back_populates="property_damage")
