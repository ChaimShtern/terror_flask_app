from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.models import Base
from app.models.attack_group_bridge_model import attack_group_association


class Group(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String)
    uncertain = Column(Boolean)
    num_perpetrators = Column(Integer)

    attacks = relationship("Attack", secondary=attack_group_association, back_populates="groups")
