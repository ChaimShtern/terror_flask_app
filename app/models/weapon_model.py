from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.models import Base


class Weapon(Base):
    __tablename__ = 'weapons'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    type = Column(String)
    subtype = Column(String)

    attack_id = Column(Integer, ForeignKey("attacks.id"))
    attack = relationship("Attack", back_populates="weapons")
