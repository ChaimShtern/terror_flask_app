from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.models import Base


class HostageSituation(Base):
    __tablename__ = 'hostage_situations'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    is_hostage = Column(Boolean)
    num_hostages = Column(Integer)
    ransom = Column(Boolean)
    ransom_amount = Column(Float)
    outcome = Column(String)

    attack_id = Column(Integer, ForeignKey("attacks.id"))
    attack = relationship("Attack", back_populates="hostage_situation")
