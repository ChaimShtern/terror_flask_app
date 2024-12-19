from sqlalchemy import Column, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from app.models import Base


class Casualty(Base):
    __tablename__ = 'casualties'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    killed = Column(Float)
    wounded = Column(Float)

    attack_id = Column(Integer, ForeignKey("attacks.id"))
    attack = relationship("Attack", back_populates="casualties")
